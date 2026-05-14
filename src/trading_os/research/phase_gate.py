"""Phase-gate scorecard for paper operations promotion decisions.

Pure functions only — no I/O, no network calls, no secrets.
Determines whether paper operations evidence meets criteria for phase review.

Phases (in order):
  PHASE_0_BUILD                           — build/test only, no paper execution
  PHASE_1_TINY_MANUAL                     — max $25/order, manual only (current target)
  PHASE_2_SMALL_MANUAL                    — max $50/order, manual only
  PHASE_3_LIMITED_SCHEDULED_RESEARCH_ONLY — scheduled research, no scheduled execution
  PHASE_4_LIMITED_SCHEDULED_PAPER         — requires explicit human approval; always blocked here

SAFETY:
  This module never modifies risk_limits.json or any config file.
  It never approves trade plans, places orders, or enables execution.
  It never enables scheduled paper execution.
  It never recommends PHASE_4 activation — that requires human action outside this system.
"""
from __future__ import annotations

from typing import Any, Optional

from ..hashing import stable_hash
from ..time_utils import utc_now_iso

# ---------------------------------------------------------------------------
# Phase constants
# ---------------------------------------------------------------------------

PHASE_0_BUILD = "PHASE_0_BUILD"
PHASE_1_TINY_MANUAL = "PHASE_1_TINY_MANUAL"
PHASE_2_SMALL_MANUAL = "PHASE_2_SMALL_MANUAL"
PHASE_3_LIMITED_SCHEDULED_RESEARCH_ONLY = "PHASE_3_LIMITED_SCHEDULED_RESEARCH_ONLY"
PHASE_4_LIMITED_SCHEDULED_PAPER = "PHASE_4_LIMITED_SCHEDULED_PAPER"

PHASE_ORDER: tuple = (
    PHASE_0_BUILD,
    PHASE_1_TINY_MANUAL,
    PHASE_2_SMALL_MANUAL,
    PHASE_3_LIMITED_SCHEDULED_RESEARCH_ONLY,
    PHASE_4_LIMITED_SCHEDULED_PAPER,
)

PHASE_DEFINITIONS: dict = {
    PHASE_0_BUILD: {
        "description": "Build and test only. No paper execution.",
        "max_notional_per_order": None,
        "max_orders_per_run": None,
        "scheduled_execution_allowed": False,
        "manual_paper_allowed": False,
    },
    PHASE_1_TINY_MANUAL: {
        "description": "Manual paper only. Max $25/order, 1 order/run.",
        "max_notional_per_order": 25.0,
        "max_orders_per_run": 1,
        "scheduled_execution_allowed": False,
        "manual_paper_allowed": True,
    },
    PHASE_2_SMALL_MANUAL: {
        "description": "Manual paper only. Max $50/order, 1 order/run.",
        "max_notional_per_order": 50.0,
        "max_orders_per_run": 1,
        "scheduled_execution_allowed": False,
        "manual_paper_allowed": True,
    },
    PHASE_3_LIMITED_SCHEDULED_RESEARCH_ONLY: {
        "description": "Scheduled research cycle allowed. No scheduled paper execution.",
        "max_notional_per_order": 50.0,
        "max_orders_per_run": 1,
        "scheduled_execution_allowed": False,
        "manual_paper_allowed": True,
    },
    PHASE_4_LIMITED_SCHEDULED_PAPER: {
        "description": (
            "Limited scheduled paper execution. "
            "BLOCKED — requires explicit human approval outside this system."
        ),
        "max_notional_per_order": 50.0,
        "max_orders_per_run": 1,
        "scheduled_execution_allowed": True,
        "manual_paper_allowed": True,
    },
}

# Minimum filled orders required for PHASE_1 → PHASE_2 promotion
MIN_FILLED_ORDERS_FOR_PHASE_2 = 20

# Minimum lineage completeness ratio to pass LINEAGE_ADEQUATE (soft check)
MIN_LINEAGE_COMPLETE_RATIO = 0.5


# ---------------------------------------------------------------------------
# Phase determination
# ---------------------------------------------------------------------------

def determine_current_phase(risk_limits: dict) -> str:
    """Infer the current operating phase from risk_limits config values."""
    max_notional = risk_limits.get("max_notional_per_order")
    max_orders = risk_limits.get("max_orders_per_run")

    if max_notional is None and max_orders is None:
        return PHASE_0_BUILD

    try:
        notional = float(max_notional)
        orders = int(max_orders)
    except (TypeError, ValueError):
        return PHASE_0_BUILD

    if notional <= 25.0 and orders <= 1:
        return PHASE_1_TINY_MANUAL
    if notional <= 50.0 and orders <= 1:
        return PHASE_2_SMALL_MANUAL
    return PHASE_3_LIMITED_SCHEDULED_RESEARCH_ONLY


def next_phase(current_phase: str) -> Optional[str]:
    """Return the next phase in the order, or None if already at PHASE_4."""
    try:
        idx = PHASE_ORDER.index(current_phase)
    except ValueError:
        return None
    if idx >= len(PHASE_ORDER) - 1:
        return None
    return PHASE_ORDER[idx + 1]


# ---------------------------------------------------------------------------
# Gate check builder
# ---------------------------------------------------------------------------

def _check(
    check_id: str,
    passes: bool,
    blocking: bool,
    evidence: str,
    required: str,
    detail: Optional[str] = None,
) -> dict:
    return {
        "check_id": check_id,
        "passes": passes,
        "blocking": blocking,
        "evidence": evidence,
        "required": required,
        "detail": None if passes else detail,
    }


def _safe_float(v: Any) -> Optional[float]:
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


# ---------------------------------------------------------------------------
# Phase 1 → Phase 2 gate checks
# ---------------------------------------------------------------------------

def run_phase1_to_phase2_checks(
    system_status: dict,
    order_monitor_report: dict,
    outcome_snapshot: dict,
    lineage_snapshot: dict,
    trigger_performance: dict,
    risk_state: dict,
    risk_limits: dict,
    history_counts: dict,
) -> list:
    """Run all Phase 1 → Phase 2 promotion gate checks.

    Returns a list of check dicts.  None of these checks modifies any config.

    history_counts: {"daily_summaries": int, "weekly_reviews": int}
    """
    checks: list = []

    # ── 1. Sufficient fills ────────────────────────────────────────────────
    filled = int(order_monitor_report.get("orders_filled", 0))
    checks.append(_check(
        check_id="FILLED_ORDERS_MIN_20",
        passes=filled >= MIN_FILLED_ORDERS_FOR_PHASE_2,
        blocking=True,
        evidence=f"orders_filled={filled}",
        required=f">= {MIN_FILLED_ORDERS_FOR_PHASE_2}",
        detail=(
            f"Only {filled} filled order(s). "
            f"Need at least {MIN_FILLED_ORDERS_FOR_PHASE_2} before reviewing promotion."
        ),
    ))

    # ── 2. No missing orders ──────────────────────────────────────────────
    missing = int(order_monitor_report.get("orders_missing", 0))
    checks.append(_check(
        check_id="NO_MISSING_ORDERS",
        passes=missing == 0,
        blocking=True,
        evidence=f"orders_missing={missing}",
        required="== 0",
        detail=(
            f"{missing} missing order(s) detected in order monitor. "
            "Investigate and resolve before promotion."
        ),
    ))

    # ── 3. No rejected orders ─────────────────────────────────────────────
    rejected = int(order_monitor_report.get("orders_rejected", 0))
    checks.append(_check(
        check_id="NO_REJECTED_ORDERS",
        passes=rejected == 0,
        blocking=True,
        evidence=f"orders_rejected={rejected}",
        required="== 0",
        detail=(
            f"{rejected} rejected order(s). "
            "Investigate root cause before promotion — rejections may indicate system bugs."
        ),
    ))

    # ── 4. Source integrity OK ────────────────────────────────────────────
    src_ok = str(system_status.get("source_integrity_status", "unknown")).lower() == "ok"
    checks.append(_check(
        check_id="SOURCE_INTEGRITY_OK",
        passes=src_ok,
        blocking=True,
        evidence=f"source_integrity_status={system_status.get('source_integrity_status')}",
        required="== 'ok'",
        detail=(
            "Source integrity check failed — mock/unknown data sources detected. "
            "Run refresh_data.py (without --dry-run) before promotion review."
        ),
    ))

    # ── 5. No blocking issues in system status ────────────────────────────
    blocking_issues = system_status.get("blocking_issues", [])
    checks.append(_check(
        check_id="NO_SYSTEM_BLOCKING_ISSUES",
        passes=len(blocking_issues) == 0,
        blocking=True,
        evidence=f"blocking_issues={blocking_issues}",
        required="empty list",
        detail=f"system_status has {len(blocking_issues)} blocking issue(s): {blocking_issues}",
    ))

    # ── 6. No open orders ────────────────────────────────────────────────
    active = int(order_monitor_report.get("orders_active", 0))
    checks.append(_check(
        check_id="OPEN_ORDERS_ZERO",
        passes=active == 0,
        blocking=True,
        evidence=f"orders_active={active}",
        required="== 0",
        detail=(
            f"{active} open/active order(s) still pending. "
            "Wait for settlement or cancel via cancel_paper_order.py before promotion review."
        ),
    ))

    # ── 7. Drawdown not breached ──────────────────────────────────────────
    drawdown = _safe_float(risk_state.get("drawdown", 0.0)) or 0.0
    block_pct = _safe_float(risk_limits.get("max_drawdown_block_pct", -0.1)) or -0.1
    drawdown_blocked = drawdown <= block_pct
    checks.append(_check(
        check_id="DRAWDOWN_NOT_BREACHED",
        passes=not drawdown_blocked,
        blocking=True,
        evidence=f"drawdown={drawdown:.4f} block_threshold={block_pct}",
        required=f"> {block_pct}",
        detail=(
            f"Drawdown {drawdown:.2%} breaches block threshold {block_pct:.2%}. "
            "Resolve drawdown breach before promotion."
        ),
    ))

    # ── 8. Daily summaries present ────────────────────────────────────────
    daily_count = int(history_counts.get("daily_summaries", 0))
    checks.append(_check(
        check_id="DAILY_SUMMARIES_PRESENT",
        passes=daily_count >= 1,
        blocking=True,
        evidence=f"daily_summary_history_count={daily_count}",
        required=">= 1",
        detail="No daily summaries found in data/history/runs/. Run daily_summary.py.",
    ))

    # ── 9. Weekly review present ──────────────────────────────────────────
    weekly_count = int(history_counts.get("weekly_reviews", 0))
    checks.append(_check(
        check_id="WEEKLY_REVIEW_PRESENT",
        passes=weekly_count >= 1,
        blocking=True,
        evidence=f"weekly_review_history_count={weekly_count}",
        required=">= 1",
        detail="No weekly reviews found in data/history/runs/. Run weekly_review.py.",
    ))

    # ── 10. Outcome integrity OK ──────────────────────────────────────────
    outcome_integrity = str(outcome_snapshot.get("source_integrity_status", "unknown")).lower()
    checks.append(_check(
        check_id="OUTCOME_INTEGRITY_OK",
        passes=outcome_integrity == "ok",
        blocking=True,
        evidence=f"outcome_snapshot.source_integrity_status={outcome_integrity}",
        required="== 'ok'",
        detail=(
            f"Outcome snapshot source integrity is '{outcome_integrity}'. "
            "Run outcome_tracker.py with live data to resolve."
        ),
    ))

    # ── 11. Trigger performance OK ────────────────────────────────────────
    tp_status = str(trigger_performance.get("status", "unknown")).lower()
    checks.append(_check(
        check_id="TRIGGER_PERFORMANCE_OK",
        passes=tp_status == "ok",
        blocking=True,
        evidence=f"trigger_performance.status={tp_status}",
        required="== 'ok'",
        detail=(
            f"trigger_performance.status='{tp_status}'. "
            "Resolve trigger performance errors before promotion."
        ),
    ))

    # ── 12. Max orders per run is still 1 ────────────────────────────────
    max_per_run = risk_limits.get("max_orders_per_run")
    per_run_ok = max_per_run is not None and int(max_per_run) == 1
    checks.append(_check(
        check_id="MAX_ORDERS_PER_RUN_ONE",
        passes=per_run_ok,
        blocking=True,
        evidence=f"max_orders_per_run={max_per_run}",
        required="== 1",
        detail=(
            f"max_orders_per_run={max_per_run!r}. "
            "Phase 1→2 promotion requires max_orders_per_run=1 to be confirmed."
        ),
    ))

    # ── 13. Daily order limit respected ──────────────────────────────────
    # Warning (blocking=False): violations show the guard is needed; promotion
    # requires the guard be active (config key present), not that today was clean.
    churn = system_status.get("churn_state", {})
    violations = churn.get("symbol_daily_limit_violations", [])
    daily_limit_reached = bool(churn.get("daily_total_limit_reached", False))
    limit_violations = violations or (daily_limit_reached and [])
    daily_ok = not daily_limit_reached and not violations
    max_total = risk_limits.get("max_total_paper_orders_per_day")
    limit_configured = max_total is not None
    checks.append(_check(
        check_id="DAILY_ORDER_LIMIT_RESPECTED",
        passes=daily_ok or not limit_configured,
        blocking=False,  # warning only — churn guard prevents future violations
        evidence=(
            f"today_limit_reached={daily_limit_reached} "
            f"violations={violations} "
            f"max_total_paper_orders_per_day={max_total}"
        ),
        required="daily limits not exceeded",
        detail=(
            f"Daily order limit reached today (max={max_total}, violations={violations}). "
            "Churn guard is now active and will prevent future violations. "
            "Ensure churn guard config is in place before promotion."
        ),
    ))

    # ── 14. Lineage adequacy ──────────────────────────────────────────────
    # Warning (blocking=False): partial lineage on older fills is acceptable
    # when data/history/trade_plans/ archiving is now active.
    lineage_count = int(lineage_snapshot.get("lineage_count", 0))
    complete_count = int(lineage_snapshot.get("complete_count", 0))
    lineage_ratio = (complete_count / lineage_count) if lineage_count > 0 else 1.0
    lineage_ok = lineage_ratio >= MIN_LINEAGE_COMPLETE_RATIO
    checks.append(_check(
        check_id="LINEAGE_ADEQUATE",
        passes=lineage_ok,
        blocking=False,  # warning only — older partial lineage is expected
        evidence=(
            f"lineage_count={lineage_count} complete_count={complete_count} "
            f"ratio={lineage_ratio:.2f}"
        ),
        required=f">= {MIN_LINEAGE_COMPLETE_RATIO:.1f} complete ratio",
        detail=(
            f"Lineage completeness ratio {lineage_ratio:.1%} "
            f"({complete_count}/{lineage_count}). "
            "Older fills have partial lineage — trade plan archiving to "
            "data/history/trade_plans/ is now active so future fills will be complete. "
            "Run build_lineage.py to update after more fills are archived."
        ),
    ))

    return checks


# ---------------------------------------------------------------------------
# Evidence summary
# ---------------------------------------------------------------------------

def build_evidence_summary(
    order_monitor_report: dict,
    outcome_snapshot: dict,
    lineage_snapshot: dict,
    system_status: dict,
    risk_limits: dict,
) -> dict:
    """Collect evidence fields for the scorecard output."""
    churn = system_status.get("churn_state", {})
    violations = churn.get("symbol_daily_limit_violations", [])

    lineage_count = int(lineage_snapshot.get("lineage_count", 0))
    complete_count = int(lineage_snapshot.get("complete_count", 0))
    lineage_ratio = (complete_count / lineage_count) if lineage_count > 0 else None

    lineage_note: Optional[str] = None
    if lineage_count > 0 and complete_count < lineage_count:
        lineage_note = (
            f"{lineage_count - complete_count} fill(s) have partial lineage. "
            "Trade plan archiving is now active — future fills will resolve to COMPLETE."
        )

    return {
        "filled_orders_count": int(order_monitor_report.get("orders_filled", 0)),
        "active_orders_count": int(order_monitor_report.get("orders_active", 0)),
        "missing_orders_count": int(order_monitor_report.get("orders_missing", 0)),
        "rejected_orders_count": int(order_monitor_report.get("orders_rejected", 0)),
        "source_integrity_status": system_status.get("source_integrity_status", "unknown"),
        "outcome_integrity_status": outcome_snapshot.get("source_integrity_status", "unknown"),
        "lineage_count": lineage_count,
        "lineage_complete_count": complete_count,
        "lineage_partial_count": int(lineage_snapshot.get("partial_count", 0)),
        "lineage_complete_ratio": round(lineage_ratio, 4) if lineage_ratio is not None else None,
        "lineage_note": lineage_note,
        "daily_order_limit_violations": violations,
        "drawdown": _safe_float(
            (system_status.get("risk_state") or {}).get("drawdown", 0.0)
        ),
        "max_orders_per_run": risk_limits.get("max_orders_per_run"),
        "max_notional_per_order": risk_limits.get("max_notional_per_order"),
        "max_total_paper_orders_per_day": risk_limits.get("max_total_paper_orders_per_day"),
    }


# ---------------------------------------------------------------------------
# Main builder
# ---------------------------------------------------------------------------

def build_phase_gate(
    system_status: dict,
    order_monitor_report: dict,
    outcome_snapshot: dict,
    lineage_snapshot: dict,
    trigger_performance: dict,
    execution_report: dict,
    trade_plan: dict,
    risk_state: dict,
    risk_limits: dict,
    history_counts: dict,
) -> dict:
    """Build and return a complete phase-gate scorecard dict.

    Never modifies any config.  Never places orders.  Never enables execution.
    Never recommends PHASE_4 activation.

    Args:
        system_status:          loaded data/latest/system_status.json
        order_monitor_report:   loaded data/latest/order_monitor_report.json
        outcome_snapshot:       loaded data/latest/outcome_snapshot.json
        lineage_snapshot:       loaded data/latest/lineage_snapshot.json
        trigger_performance:    loaded data/latest/trigger_performance.json
        execution_report:       loaded data/latest/execution_report.json
        trade_plan:             loaded data/latest/trade_plan.json
        risk_state:             loaded memory/RISK-STATE.json
        risk_limits:            loaded config/risk_limits.json
        history_counts:         {"daily_summaries": int, "weekly_reviews": int}

    Returns:
        phase_gate dict ready to write to data/latest/phase_gate.json.
    """
    generated_at = utc_now_iso()
    current_phase = determine_current_phase(risk_limits)
    next_ph = next_phase(current_phase)

    # Run checks for current phase → next phase transition
    if current_phase == PHASE_1_TINY_MANUAL:
        checks = run_phase1_to_phase2_checks(
            system_status=system_status,
            order_monitor_report=order_monitor_report,
            outcome_snapshot=outcome_snapshot,
            lineage_snapshot=lineage_snapshot,
            trigger_performance=trigger_performance,
            risk_state=risk_state,
            risk_limits=risk_limits,
            history_counts=history_counts,
        )
    elif current_phase == PHASE_0_BUILD:
        checks = [_check(
            "AT_PHASE_0",
            passes=False,
            blocking=True,
            evidence="current_phase=PHASE_0_BUILD",
            required="execute paper orders first",
            detail="No paper orders detected. Complete PHASE_0_BUILD before reviewing promotion.",
        )]
    elif current_phase == PHASE_4_LIMITED_SCHEDULED_PAPER:
        checks = [_check(
            "PHASE_4_ALWAYS_BLOCKED",
            passes=False,
            blocking=True,
            evidence="current_phase=PHASE_4_LIMITED_SCHEDULED_PAPER",
            required="explicit human approval outside this system",
            detail=(
                "PHASE_4 promotion requires explicit human approval and is "
                "always blocked by this automated scorecard."
            ),
        )]
    else:
        checks = []

    # Separate blocking failures from warnings
    blocking_failures = [c for c in checks if not c["passes"] and c["blocking"]]
    warnings_list = [c for c in checks if not c["passes"] and not c["blocking"]]

    blocking_issues = [c["detail"] for c in blocking_failures if c["detail"]]
    warnings = [c["detail"] for c in warnings_list if c["detail"]]

    eligible = len(blocking_failures) == 0

    # PHASE_4 is always blocked by policy — this scorecard never enables it
    if next_ph == PHASE_4_LIMITED_SCHEDULED_PAPER:
        eligible = False
        blocking_issues.append(
            "PHASE_4_LIMITED_SCHEDULED_PAPER requires explicit human approval "
            "and strict evidence review outside this automated scorecard. "
            "This system will never automatically approve PHASE_4."
        )

    if eligible:
        recommendation = "eligible_for_review"
        recommended_phase = next_ph or current_phase
        required_human_actions = [
            f"Review all gate checks and evidence summary.",
            f"If evidence is satisfactory, manually update risk_limits.json to "
            f"set max_notional_per_order to the {recommended_phase} cap.",
            f"Open a PR with the config change, evidence rationale, and rollback notes.",
            f"Do NOT rely solely on this scorecard — human judgment is required.",
        ]
    else:
        recommendation = "stay_at_phase"
        recommended_phase = current_phase
        required_human_actions = [
            f"Resolve all blocking issues before requesting promotion review.",
            f"Re-run phase_gate.py after resolving blockers.",
        ]

    evidence_summary = build_evidence_summary(
        order_monitor_report=order_monitor_report,
        outcome_snapshot=outcome_snapshot,
        lineage_snapshot=lineage_snapshot,
        system_status=system_status,
        risk_limits=risk_limits,
    )
    evidence_summary["daily_summaries_count"] = history_counts.get("daily_summaries", 0)
    evidence_summary["weekly_reviews_count"] = history_counts.get("weekly_reviews", 0)

    # Run ID
    ts = generated_at.replace(":", "").replace("-", "").replace("Z", "")[:15]
    run_id = f"phase_gate-{ts}-{stable_hash({'ts': generated_at})[:8]}"

    result: dict = {
        "run_id": run_id,
        "generated_at": generated_at,
        "current_phase": current_phase,
        "next_phase": next_ph,
        "recommended_phase": recommended_phase,
        "eligible_for_next_phase": eligible,
        "recommendation": recommendation,
        "blocking_issues": blocking_issues,
        "warnings": warnings,
        "checks": checks,
        "evidence_summary": evidence_summary,
        "required_human_actions": required_human_actions,
        "safety_note": (
            "No config was changed. No orders were placed. "
            "No paper execution was enabled. No trade plans were approved. "
            "No scheduled execution was enabled."
        ),
    }
    result["phase_gate_hash"] = stable_hash(
        {k: v for k, v in result.items() if k != "phase_gate_hash"}
    )[:16]
    return result


# ---------------------------------------------------------------------------
# Markdown formatter
# ---------------------------------------------------------------------------

def format_phase_gate_markdown(result: dict) -> str:
    """Format a phase gate result as a PROMOTION-DECISIONS.md section."""
    ts = result.get("generated_at", "?")
    current = result.get("current_phase", "?")
    recommended = result.get("recommended_phase", "?")
    eligible = result.get("eligible_for_next_phase", False)
    recommendation = result.get("recommendation", "?")
    run_id = result.get("run_id", "?")

    status_str = "ELIGIBLE FOR REVIEW" if eligible else "STAY AT CURRENT PHASE"
    ev = result.get("evidence_summary", {})

    lines = [
        "",
        f"## Phase Gate — {ts}",
        "",
        f"**run_id:** `{run_id}`  ",
        f"**current_phase:** {current}  ",
        f"**recommended_phase:** {recommended}  ",
        f"**status:** {status_str}  ",
        f"**recommendation:** {recommendation}  ",
        "",
        "**Evidence:**  ",
        f"- filled_orders: {ev.get('filled_orders_count')} (need ≥ 20)  ",
        f"- active_orders: {ev.get('active_orders_count')}  ",
        f"- missing_orders: {ev.get('missing_orders_count')}  ",
        f"- rejected_orders: {ev.get('rejected_orders_count')}  ",
        f"- source_integrity: {ev.get('source_integrity_status')}  ",
        f"- outcome_integrity: {ev.get('outcome_integrity_status')}  ",
        (
            f"- lineage: {ev.get('lineage_complete_count')}/{ev.get('lineage_count')} complete "
            f"(ratio={ev.get('lineage_complete_ratio')})  "
        ),
        f"- drawdown: {ev.get('drawdown')}  ",
        f"- max_orders_per_run: {ev.get('max_orders_per_run')}  ",
        f"- max_notional_per_order: {ev.get('max_notional_per_order')}  ",
        f"- daily_summaries_in_history: {ev.get('daily_summaries_count')}  ",
        f"- weekly_reviews_in_history: {ev.get('weekly_reviews_count')}  ",
        "",
    ]

    if result.get("blocking_issues"):
        lines.append("**Blocking Issues:**  ")
        for issue in result["blocking_issues"]:
            lines.append(f"- {issue}  ")
        lines.append("")

    if result.get("warnings"):
        lines.append("**Warnings:**  ")
        for w in result["warnings"]:
            lines.append(f"- {w}  ")
        lines.append("")

    lines.append(f"*{result.get('safety_note')}*  ")
    lines.append("")
    lines.append("---")
    lines.append("")

    return "\n".join(lines)
