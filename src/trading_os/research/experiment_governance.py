"""Experiment and promotion governance for Autonomous Trading Research OS.

Provides a formal process for proposing, evaluating, and recording strategy
change candidates. All functions are pure (no I/O, no side effects).

SAFETY — non-negotiable invariants:
  - Never modifies config/strategy.json, risk_limits.json, or trigger_registry.json.
  - production_mutation_allowed is always False in every returned dict.
  - human_approval_required is always True; it cannot be waived.
  - Promotion decisions are records only — applying a change still requires a
    human to open and merge a PR.
  - No execution path, no order submission, no paper execution flag.
"""
from __future__ import annotations

import re
from typing import Optional

from ..hashing import stable_hash
from ..time_utils import utc_now_iso

SCHEMA_VERSION = "0.1.0"

# Experiment lifecycle statuses
STATUS_PROPOSED = "proposed"
STATUS_ACTIVE = "active"
STATUS_COMPLETED = "completed"
STATUS_REJECTED = "rejected"
STATUS_PROMOTED = "promoted"
STATUS_DEMOTED = "demoted"

VALID_STATUSES: frozenset = frozenset({
    STATUS_PROPOSED,
    STATUS_ACTIVE,
    STATUS_COMPLETED,
    STATUS_REJECTED,
    STATUS_PROMOTED,
    STATUS_DEMOTED,
})

# Promotion decision values
DECISION_PENDING = "pending"
DECISION_APPROVED = "approved"
DECISION_REJECTED = "rejected"

# Required top-level experiment fields
REQUIRED_EXPERIMENT_FIELDS: tuple = (
    "hypothesis",
    "affected_trigger_or_rule",
    "expected_benefit",
    "risk",
    "required_sample_size",
    "required_backtest",
    "required_paper_validation",
    "promotion_criteria",
    "demotion_criteria",
)

# Required sub-fields in promotion_criteria
REQUIRED_PROMOTION_CRITERIA_FIELDS: tuple = (
    "min_filled_trade_count",
    "min_observation_count",
    "min_expectancy_after_costs",
    "no_risk_limit_breach",
    "no_operational_failures",
    "human_approval_required",
)

# Required sub-fields in demotion_criteria
REQUIRED_DEMOTION_CRITERIA_FIELDS: tuple = (
    "max_drawdown_pct",
    "max_consecutive_losses",
    "min_expectancy_after_costs",
)

# Config files that must never be mutated by this module or its callers
PROTECTED_CONFIG_FILES: tuple = (
    "config/strategy.json",
    "config/risk_limits.json",
    "config/trigger_registry.json",
)

# Minimum sensible fill count for any promotion
ABSOLUTE_MIN_FILLS = 10


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_experiment(experiment: dict) -> tuple:
    """Validate experiment dict structure.

    Returns:
        (is_valid: bool, errors: list[str])
    """
    errors: list = []

    for field in REQUIRED_EXPERIMENT_FIELDS:
        if field not in experiment:
            errors.append(f"Missing required field: {field}")
        elif experiment[field] is None or experiment[field] == "":
            errors.append(f"Field must not be empty: {field}")

    # required_sample_size must be a positive integer
    rs = experiment.get("required_sample_size")
    if rs is not None:
        try:
            if int(rs) <= 0:
                errors.append("required_sample_size must be > 0")
        except (TypeError, ValueError):
            errors.append("required_sample_size must be a positive integer")

    # Validate promotion_criteria sub-fields
    pc = experiment.get("promotion_criteria")
    if pc is None:
        pass  # already caught above as empty
    elif not isinstance(pc, dict):
        errors.append("promotion_criteria must be a dict")
    else:
        for f in REQUIRED_PROMOTION_CRITERIA_FIELDS:
            if f not in pc:
                errors.append(f"promotion_criteria missing field: {f}")
        # human_approval_required must be True — cannot be waived
        if not pc.get("human_approval_required", True):
            errors.append(
                "promotion_criteria.human_approval_required must be true — "
                "human approval cannot be waived"
            )
        # min_filled_trade_count must meet the absolute floor
        mf = pc.get("min_filled_trade_count")
        if mf is not None:
            try:
                if int(mf) < ABSOLUTE_MIN_FILLS:
                    errors.append(
                        f"promotion_criteria.min_filled_trade_count must be "
                        f">= {ABSOLUTE_MIN_FILLS}"
                    )
            except (TypeError, ValueError):
                errors.append(
                    "promotion_criteria.min_filled_trade_count must be an integer"
                )

    # Validate demotion_criteria sub-fields
    dc = experiment.get("demotion_criteria")
    if dc is None:
        pass  # already caught above
    elif not isinstance(dc, dict):
        errors.append("demotion_criteria must be a dict")
    else:
        for f in REQUIRED_DEMOTION_CRITERIA_FIELDS:
            if f not in dc:
                errors.append(f"demotion_criteria missing field: {f}")

    return len(errors) == 0, errors


# ---------------------------------------------------------------------------
# Experiment creation
# ---------------------------------------------------------------------------

def _slugify(text: str, max_len: int = 30) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower().strip())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug[:max_len]


def _make_experiment_id(hypothesis: str, created_at: Optional[str] = None) -> str:
    ts = (created_at or utc_now_iso()).replace(":", "").replace("-", "")[:15]
    h = stable_hash({"hypothesis": hypothesis, "ts": ts})[:8]
    return f"exp-{ts}-{h}"


def create_experiment(
    hypothesis: str,
    affected_trigger_or_rule: str,
    expected_benefit: str,
    risk: str,
    required_sample_size: int,
    promotion_criteria: dict,
    demotion_criteria: dict,
    *,
    required_backtest: bool = True,
    required_paper_validation: bool = True,
    candidate_patch: Optional[dict] = None,
    affected_config_key: Optional[str] = None,
    notes: str = "",
    experiment_id: Optional[str] = None,
    created_at: Optional[str] = None,
) -> dict:
    """Build and return a new experiment dict. Does not write any files.

    The returned dict always has production_mutation_allowed=False and
    promotion_criteria.human_approval_required=True.

    Args:
        hypothesis: Clear, falsifiable statement of the expected improvement.
        affected_trigger_or_rule: Trigger ID or config rule under test.
        expected_benefit: Quantified expected gain (fill rate, return, etc.).
        risk: Potential downside or failure mode.
        required_sample_size: Minimum fills before the experiment is evaluable.
        promotion_criteria: Dict of evidence thresholds; merged with safe defaults.
        demotion_criteria: Dict of thresholds that would terminate the experiment.
        required_backtest: Whether a backtest/replay is required before paper.
        required_paper_validation: Whether paper results are required first.
        candidate_patch: Documentary record of what would change (no files touched).
        affected_config_key: Dotted key path in config (documentary only).
        notes: Free-text notes.
        experiment_id: Override auto-generated ID (useful in tests).
        created_at: Override timestamp (useful in tests).

    Returns:
        Experiment dict. Call validate_experiment() to verify it.
    """
    ts = created_at or utc_now_iso()
    eid = experiment_id or _make_experiment_id(hypothesis, ts)

    # Safe defaults for promotion criteria — caller overrides specific fields
    merged_pc: dict = {
        "min_filled_trade_count": 20,
        "min_observation_count": 50,
        "min_expectancy_after_costs": 0.001,
        "must_beat_spy": False,
        "must_beat_bil": True,
        "no_risk_limit_breach": True,
        "no_operational_failures": True,
        "human_approval_required": True,   # invariant: always True
    }
    merged_pc.update(promotion_criteria)
    merged_pc["human_approval_required"] = True  # enforce regardless of caller

    # Safe defaults for demotion criteria
    merged_dc: dict = {
        "max_drawdown_pct": -0.05,
        "max_consecutive_losses": 5,
        "min_expectancy_after_costs": -0.005,
    }
    merged_dc.update(demotion_criteria)

    exp: dict = {
        "schema_version": SCHEMA_VERSION,
        "experiment_id": eid,
        "created_at": ts,
        "status": STATUS_PROPOSED,
        "hypothesis": hypothesis,
        "affected_trigger_or_rule": affected_trigger_or_rule,
        "affected_config_key": affected_config_key,
        "expected_benefit": expected_benefit,
        "risk": risk,
        "required_sample_size": required_sample_size,
        "required_backtest": required_backtest,
        "required_paper_validation": required_paper_validation,
        "promotion_criteria": merged_pc,
        "demotion_criteria": merged_dc,
        "candidate_patch": candidate_patch or {},
        "notes": notes,
        # Safety invariant — documented in the record itself
        "production_mutation_allowed": False,
    }
    exp["experiment_hash"] = stable_hash(
        {k: v for k, v in exp.items() if k != "experiment_hash"}
    )
    return exp


# ---------------------------------------------------------------------------
# Promotion evaluation
# ---------------------------------------------------------------------------

def evaluate_promotion(
    experiment: dict,
    *,
    filled_trade_count: int = 0,
    observation_count: int = 0,
    expectancy_after_costs: Optional[float] = None,
    strategy_period_return_pct: Optional[float] = None,
    spy_period_return_pct: Optional[float] = None,
    bil_period_return_pct: Optional[float] = None,
    risk_limit_breaches: Optional[list] = None,
    operational_failures: Optional[list] = None,
    drawdown: Optional[float] = None,
    consecutive_losses: Optional[int] = None,
    notes: str = "",
    generated_at: Optional[str] = None,
) -> dict:
    """Evaluate whether an experiment meets its promotion criteria.

    Returns an evaluation dict. This function NEVER:
      - grants promotion automatically
      - sets human_approved=True
      - sets production_mutation_allowed=True
      - reads or writes files

    A separate build_promotion_decision() call is needed to record approval.

    Args:
        experiment: The experiment dict from create_experiment().
        filled_trade_count: Number of fills observed during the experiment.
        observation_count: Total observations (trigger evaluations) recorded.
        expectancy_after_costs: Average return per trade after estimated costs.
        strategy_period_return_pct: Strategy return over measurement period.
        spy_period_return_pct: SPY return over same period (benchmark).
        bil_period_return_pct: BIL return over same period (risk-free baseline).
        risk_limit_breaches: List of gate/limit breach descriptions.
        operational_failures: List of operational failure descriptions.
        drawdown: Current or peak drawdown (negative fraction, e.g. -0.03).
        consecutive_losses: Number of consecutive losing trades.
        notes: Free-text evaluation notes.
        generated_at: Override timestamp.

    Returns:
        Evaluation dict with criteria_met, demotion assessment, PR instructions,
        and promotion_ready=False (always — requires build_promotion_decision).
    """
    pc = experiment.get("promotion_criteria", {})
    dc = experiment.get("demotion_criteria", {})
    risk_limit_breaches = risk_limit_breaches or []
    operational_failures = operational_failures or []
    ts = generated_at or utc_now_iso()

    # ── Promotion criteria checks ────────────────────────────────────────────
    min_fills = int(pc.get("min_filled_trade_count", 20))
    min_obs = int(pc.get("min_observation_count", 50))
    min_exp = float(pc.get("min_expectancy_after_costs", 0.001))
    must_beat_spy = bool(pc.get("must_beat_spy", False))
    must_beat_bil = bool(pc.get("must_beat_bil", True))

    fills_ok = filled_trade_count >= min_fills
    obs_ok = observation_count >= min_obs
    exp_ok = expectancy_after_costs is not None and expectancy_after_costs >= min_exp
    no_breach = not risk_limit_breaches
    no_failures = not operational_failures

    beats_spy: Optional[bool] = None
    if spy_period_return_pct is not None and strategy_period_return_pct is not None:
        beats_spy = strategy_period_return_pct > spy_period_return_pct

    beats_bil: Optional[bool] = None
    if bil_period_return_pct is not None and strategy_period_return_pct is not None:
        beats_bil = strategy_period_return_pct > bil_period_return_pct

    spy_ok = (not must_beat_spy) or (beats_spy is True)
    bil_ok = (not must_beat_bil) or (beats_bil is True)

    all_criteria_met = (
        fills_ok and obs_ok and exp_ok
        and no_breach and no_failures
        and spy_ok and bil_ok
    )

    # ── Demotion criteria checks ─────────────────────────────────────────────
    max_dd = float(dc.get("max_drawdown_pct", -0.05))
    max_cl = int(dc.get("max_consecutive_losses", 5))
    min_exp_floor = float(dc.get("min_expectancy_after_costs", -0.005))

    demotion_triggered = False
    demotion_reasons: list = []
    if drawdown is not None and drawdown <= max_dd:
        demotion_triggered = True
        demotion_reasons.append(
            f"drawdown {drawdown:.2%} <= demotion threshold {max_dd:.2%}"
        )
    if consecutive_losses is not None and consecutive_losses >= max_cl:
        demotion_triggered = True
        demotion_reasons.append(
            f"consecutive_losses {consecutive_losses} >= max {max_cl}"
        )
    if (
        expectancy_after_costs is not None
        and expectancy_after_costs <= min_exp_floor
    ):
        demotion_triggered = True
        demotion_reasons.append(
            f"expectancy {expectancy_after_costs:.4f} <= floor {min_exp_floor:.4f}"
        )

    return {
        "schema_version": SCHEMA_VERSION,
        "experiment_id": experiment.get("experiment_id"),
        "generated_at": ts,

        # ── Evidence collected ───────────────────────────────────────────────
        "evidence": {
            "filled_trade_count": filled_trade_count,
            "observation_count": observation_count,
            "expectancy_after_costs": expectancy_after_costs,
            "strategy_period_return_pct": strategy_period_return_pct,
            "spy_period_return_pct": spy_period_return_pct,
            "bil_period_return_pct": bil_period_return_pct,
            "beats_spy": beats_spy,
            "beats_bil": beats_bil,
            "risk_limit_breaches": risk_limit_breaches,
            "operational_failures": operational_failures,
            "drawdown": drawdown,
            "consecutive_losses": consecutive_losses,
        },

        # ── Promotion criteria results ───────────────────────────────────────
        "criteria_met": {
            "min_filled_trade_count": fills_ok,
            "min_observation_count": obs_ok,
            "positive_expectancy_after_costs": exp_ok,
            "no_risk_limit_breach": no_breach,
            "no_operational_failures": no_failures,
            "beats_spy": spy_ok,
            "beats_bil": bil_ok,
        },
        "all_promotion_criteria_met": all_criteria_met,

        # ── Demotion assessment ──────────────────────────────────────────────
        "demotion_triggered": demotion_triggered,
        "demotion_reasons": demotion_reasons,

        # ── Decision state (set by build_promotion_decision) ─────────────────
        "promotion_ready": False,          # always False without human approval
        "human_approval_required": True,   # invariant
        "human_approved": False,           # set by build_promotion_decision()
        "approved_by": None,
        "approval_notes": "",
        "decision": DECISION_PENDING,

        # ── Safety invariants ────────────────────────────────────────────────
        "production_mutation_allowed": False,  # invariant — never True
        "protected_files": list(PROTECTED_CONFIG_FILES),
        "candidate_pr_instructions": _build_pr_instructions(experiment),
        "notes": notes,
    }


def _build_pr_instructions(experiment: dict) -> str:
    """Generate human-readable branch/PR instructions for a candidate change."""
    eid = experiment.get("experiment_id", "?")
    hyp = experiment.get("hypothesis", "?")
    rule = experiment.get("affected_trigger_or_rule", "?")
    cp = experiment.get("candidate_patch", {})

    lines = [
        f"# Candidate promotion PR — {eid}",
        "",
        "## Steps to apply this experiment result as a production change",
        "",
        "1. Create a branch:",
        f'   git checkout -b "experiment/promote-{eid}"',
        "",
        "2. Apply the patch manually:",
    ]

    if cp:
        patch_file = cp.get("file", "?")
        patch_key = cp.get("key", "?")
        old_val = cp.get("old_value", "?")
        new_val = cp.get("new_value", "?")
        lines += [
            f"   File:      {patch_file}",
            f"   Key:       {patch_key}",
            f"   Old value: {old_val!r}",
            f"   New value: {new_val!r}",
        ]
    else:
        lines.append(
            f"   See experiment {eid} for the proposed change details."
        )

    lines += [
        "",
        "3. Run validate_all.py and pytest before opening the PR.",
        "",
        "4. Open a PR with:",
        f"   Title:  experiment: promote {rule} change ({eid})",
        f"   Body:   Hypothesis: {hyp}",
        "   Body:   Link to this evaluation JSON and the experiment JSON.",
        "   Body:   Paper evidence and backtest results.",
        "   Body:   Rollback notes (how to revert if the change underperforms).",
        "",
        "5. Do NOT merge without explicit human review and a second approval.",
        "",
        "REMINDER: No config file has been modified. This is a proposal only.",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Promotion decision recording
# ---------------------------------------------------------------------------

def build_promotion_decision(
    experiment: dict,
    evaluation: dict,
    *,
    decision: str,
    approved_by: Optional[str] = None,
    approval_notes: str = "",
    decided_at: Optional[str] = None,
) -> dict:
    """Record a human promotion decision (approve or reject).

    This function does NOT mutate any config file. The returned dict is a
    decision record only — applying the change still requires a manual PR.

    Args:
        experiment: The experiment dict.
        evaluation: The evaluation dict from evaluate_promotion().
        decision: "approved" or "rejected".
        approved_by: Identifier of the approving operator. Required for "approved".
        approval_notes: Free-text rationale.
        decided_at: Override timestamp.

    Returns:
        Decision dict. production_mutation_allowed is always False.

    Raises:
        ValueError: If decision is "approved" but approved_by is missing or blank.
        ValueError: If decision is not "approved" or "rejected".
    """
    if decision not in (DECISION_APPROVED, DECISION_REJECTED):
        raise ValueError(
            f"decision must be 'approved' or 'rejected', got {decision!r}"
        )
    if decision == DECISION_APPROVED and not (approved_by or "").strip():
        raise ValueError(
            "approved_by must be provided and non-empty when decision='approved'"
        )

    ts = decided_at or utc_now_iso()
    ev = evaluation.get("evidence", {})

    return {
        "schema_version": SCHEMA_VERSION,
        "experiment_id": experiment.get("experiment_id"),
        "decided_at": ts,
        "decision": decision,
        "approved_by": approved_by,
        "approval_notes": approval_notes,
        "all_promotion_criteria_met": evaluation.get("all_promotion_criteria_met", False),
        "demotion_triggered": evaluation.get("demotion_triggered", False),
        "human_approved": decision == DECISION_APPROVED,
        # Safety invariants
        "production_mutation_allowed": False,  # invariant — never True
        "protected_files": list(PROTECTED_CONFIG_FILES),
        "candidate_pr_instructions": evaluation.get("candidate_pr_instructions", ""),
        "evidence_summary": {
            "filled_trade_count": ev.get("filled_trade_count"),
            "expectancy_after_costs": ev.get("expectancy_after_costs"),
            "beats_spy": ev.get("beats_spy"),
            "beats_bil": ev.get("beats_bil"),
            "risk_limit_breaches": ev.get("risk_limit_breaches", []),
            "operational_failures": ev.get("operational_failures", []),
        },
        "approval_notes": approval_notes,
    }


# ---------------------------------------------------------------------------
# Demotion check
# ---------------------------------------------------------------------------

def check_demotion(experiment: dict, evaluation: dict) -> dict:
    """Return a demotion recommendation based on evaluation evidence.

    Never terminates an experiment automatically — returns a recommendation only.
    Human judgment is required before an experiment is formally demoted.
    """
    triggered = evaluation.get("demotion_triggered", False)
    return {
        "experiment_id": experiment.get("experiment_id"),
        "triggered": triggered,
        "reasons": evaluation.get("demotion_reasons", []),
        "recommendation": (
            "Terminate experiment and record as rejected"
            if triggered
            else "Continue observation"
        ),
        "production_mutation_allowed": False,
    }


# ---------------------------------------------------------------------------
# Markdown formatters
# ---------------------------------------------------------------------------

def format_experiment_markdown(experiment: dict) -> str:
    """Return a human-readable EXPERIMENT-LOG.md entry for one experiment."""
    eid = experiment.get("experiment_id", "?")
    ts = experiment.get("created_at", "?")
    status = experiment.get("status", "?")
    hyp = experiment.get("hypothesis", "?")
    rule = experiment.get("affected_trigger_or_rule", "?")
    config_key = experiment.get("affected_config_key") or "—"
    benefit = experiment.get("expected_benefit", "?")
    risk = experiment.get("risk", "?")
    sample = experiment.get("required_sample_size", "?")
    backtest = experiment.get("required_backtest", True)
    paper = experiment.get("required_paper_validation", True)
    pc = experiment.get("promotion_criteria", {})
    dc = experiment.get("demotion_criteria", {})
    cp = experiment.get("candidate_patch", {})
    notes = experiment.get("notes", "")

    lines = [
        f"## Experiment — {eid}",
        "",
        f"**Created:** {ts}  **Status:** {status}",
        "",
        f"**Hypothesis:** {hyp}",
        f"**Affected rule / trigger:** {rule}  **Config key:** {config_key}",
        f"**Expected benefit:** {benefit}",
        f"**Risk:** {risk}",
        "",
        f"**Required sample size:** {sample} fills  "
        f"**Backtest required:** {backtest}  "
        f"**Paper validation required:** {paper}",
        "",
        "**Promotion criteria:**",
        f"- min fills: {pc.get('min_filled_trade_count', '?')}",
        f"- min observations: {pc.get('min_observation_count', '?')}",
        f"- min expectancy after costs: {pc.get('min_expectancy_after_costs', '?')}",
        f"- must beat BIL: {pc.get('must_beat_bil', '?')}",
        f"- must beat SPY: {pc.get('must_beat_spy', '?')}",
        f"- no risk breaches: {pc.get('no_risk_limit_breach', '?')}",
        f"- human approval required: {pc.get('human_approval_required', True)}",
        "",
        "**Demotion criteria:**",
        f"- max drawdown: {dc.get('max_drawdown_pct', '?')}",
        f"- max consecutive losses: {dc.get('max_consecutive_losses', '?')}",
        f"- expectancy floor: {dc.get('min_expectancy_after_costs', '?')}",
        "",
    ]

    if cp:
        lines += [
            "**Candidate patch (documentary — no config modified):**",
            f"- File: `{cp.get('file', '?')}`",
            f"- Key: `{cp.get('key', '?')}`",
            f"- Old: `{cp.get('old_value', '?')!r}`  →  New: `{cp.get('new_value', '?')!r}`",
            "",
        ]

    if notes:
        lines += [f"**Notes:** {notes}", ""]

    lines += ["**Safety:** production_mutation_allowed=False", "---", ""]
    return "\n".join(lines)


def format_promotion_decision_markdown(decision: dict) -> str:
    """Return a human-readable PROMOTION-DECISIONS.md entry."""
    eid = decision.get("experiment_id", "?")
    ts = decision.get("decided_at", "?")
    dec = (decision.get("decision") or "?").upper()
    approved_by = decision.get("approved_by") or "N/A"
    notes = decision.get("approval_notes") or "none"
    criteria_met = decision.get("all_promotion_criteria_met", False)
    demotion = decision.get("demotion_triggered", False)
    ev = decision.get("evidence_summary", {})

    lines = [
        f"## Promotion Decision — {eid}",
        "",
        f"**Decided:** {ts}  **Decision:** {dec}",
        f"**Approved by:** {approved_by}",
        f"**Notes:** {notes}",
        "",
        f"**All criteria met:** {criteria_met}  "
        f"**Demotion triggered:** {demotion}",
        "",
        "**Evidence summary:**",
        f"- fills: {ev.get('filled_trade_count', '?')}",
        f"- expectancy_after_costs: {ev.get('expectancy_after_costs', '?')}",
        f"- beats_spy: {ev.get('beats_spy', '?')}",
        f"- beats_bil: {ev.get('beats_bil', '?')}",
        f"- risk_limit_breaches: {ev.get('risk_limit_breaches', [])}",
        f"- operational_failures: {ev.get('operational_failures', [])}",
        "",
        "**Safety:** production_mutation_allowed=False  "
        "No config file was modified.",
        "---",
        "",
    ]
    return "\n".join(lines)
