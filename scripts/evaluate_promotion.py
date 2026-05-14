#!/usr/bin/env python3
"""Evaluate a strategy experiment against its promotion criteria.

Reads evidence from data/latest snapshots, runs a structured evaluation,
and writes the result. Optionally records a human approval or rejection.
NEVER modifies any production config file.

Usage — evaluate only:
    python scripts/evaluate_promotion.py --experiment-id exp-20260514T123456-a1b2c3d4

Usage — evaluate and record approval:
    python scripts/evaluate_promotion.py \\
        --experiment-id exp-20260514T123456-a1b2c3d4 \\
        --approve \\
        --approved-by "operator-name" \\
        --notes "Paper evidence sufficient; approved for candidate PR."

Usage — evaluate and record rejection:
    python scripts/evaluate_promotion.py \\
        --experiment-id exp-20260514T123456-a1b2c3d4 \\
        --reject \\
        --notes "Insufficient evidence — only 8 fills."

Exit codes:
    0  evaluation written successfully
    1  error (missing experiment, validation failure, argument error)

Outputs:
    data/history/experiments/<id>_eval_<ts>.json
    data/history/experiments/<id>_decision_<ts>.json  (if --approve or --reject)
    memory/PROMOTION-DECISIONS.md  (appended if decision recorded)

Safety guarantees:
- NEVER modifies config/strategy.json, config/risk_limits.json, or
  config/trigger_registry.json.
- NEVER enables paper execution.
- NEVER places orders or calls any execution path.
- production_mutation_allowed is always False in all written records.
- human_approved is only True when --approve is explicitly passed with --approved-by.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import HISTORY_DIR, LATEST_DIR, MEMORY_DIR
from trading_os.research.experiment_governance import (
    DECISION_APPROVED,
    DECISION_REJECTED,
    PROTECTED_CONFIG_FILES,
    build_promotion_decision,
    check_demotion,
    evaluate_promotion,
    format_promotion_decision_markdown,
)
from trading_os.time_utils import utc_now_iso

_EXPERIMENTS_DIR = HISTORY_DIR / "experiments"


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def _write_json_atomic(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True, default=str)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(path)
    print(f"  wrote {path.relative_to(_ROOT)}")


def _load_json_optional(path: Path, label: str) -> dict:
    if not path.exists():
        print(f"  [evaluate_promotion] {label} not found — using empty default")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"  [evaluate_promotion] WARNING: could not parse {label}: {exc}")
        return {}


def _append_promotion_log(decision: dict) -> None:
    log_path = MEMORY_DIR / "PROMOTION-DECISIONS.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    entry = format_promotion_decision_markdown(decision)
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    print(f"  appended {log_path.relative_to(_ROOT)}")


def _compact_ts() -> str:
    return utc_now_iso().replace(":", "").replace("-", "")[:15]


# ---------------------------------------------------------------------------
# Evidence collection from data/latest
# ---------------------------------------------------------------------------

def _collect_evidence(experiment: dict) -> dict:
    """Collect promotion evidence from data/latest snapshots.

    All sources are optional — missing files degrade gracefully to defaults.
    This function never touches any config or execution path.
    """
    outcome_snap = _load_json_optional(
        LATEST_DIR / "outcome_snapshot.json", "outcome_snapshot"
    )
    trigger_perf = _load_json_optional(
        LATEST_DIR / "trigger_performance.json", "trigger_performance"
    )
    exec_report = _load_json_optional(
        LATEST_DIR / "execution_report.json", "execution_report"
    )
    order_monitor = _load_json_optional(
        LATEST_DIR / "order_monitor_report.json", "order_monitor_report"
    )
    risk_state_raw = {}
    risk_state_path = MEMORY_DIR / "RISK-STATE.json"
    if risk_state_path.exists():
        try:
            risk_state_raw = json.loads(risk_state_path.read_text(encoding="utf-8"))
        except Exception:
            pass

    # ── Filled trade count ────────────────────────────────────────────────────
    outcomes = outcome_snap.get("outcomes", [])
    filled_trade_count = len([o for o in outcomes if o.get("filled_at")])

    # ── Observation count (trigger evaluations) ───────────────────────────────
    # Sum total_evaluations from trigger_performance stats
    trigger_stats = trigger_perf.get("trigger_stats", {})
    observation_count = sum(
        int(v.get("total_evaluations", 0))
        for v in trigger_stats.values()
        if isinstance(v, dict)
    )
    if observation_count == 0:
        # Fallback: observation_count from outcome snapshot
        observation_count = int(outcome_snap.get("outcomes_count", 0))

    # ── Expectancy after costs ────────────────────────────────────────────────
    # Use avg_current_return_pct from outcomes, minus a 0.05% cost estimate
    COST_ESTIMATE = 0.0005
    returns = [
        float(o["current_return_pct"])
        for o in outcomes
        if o.get("current_return_pct") is not None
    ]
    if returns:
        avg_return = sum(returns) / len(returns)
        expectancy_after_costs: Optional[float] = avg_return - COST_ESTIMATE
    else:
        expectancy_after_costs = None

    # ── SPY / BIL comparison ──────────────────────────────────────────────────
    # Fill outcomes from trigger performance if available
    fill_outcomes = trigger_perf.get("fill_outcomes", {})
    strategy_return = fill_outcomes.get("avg_current_return_pct")
    spy_return: Optional[float] = None   # would come from market data context
    bil_return: Optional[float] = None   # would come from market data context

    # ── Risk limit breaches ───────────────────────────────────────────────────
    failed_gates = exec_report.get("failed_gates", [])
    # Hard gate failures count as risk limit breaches
    HARD_GATES = {
        "CANONICAL_SOURCE_INTEGRITY",
        "TRADING_MODE_PAPER",
        "ALPACA_PAPER_MODE",
        "NO_PROHIBITED_ORDERS",
        "RISK_LIMITS_RESPECTED",
    }
    risk_limit_breaches = [g for g in failed_gates if g in HARD_GATES]

    # ── Operational failures ──────────────────────────────────────────────────
    rejected = int(order_monitor.get("orders_rejected", 0))
    op_failures = [f"order_rejected_{i}" for i in range(rejected)]
    warnings = order_monitor.get("warnings", [])
    if warnings:
        op_failures.extend([f"warning: {w}" for w in warnings[:5]])

    # ── Drawdown ──────────────────────────────────────────────────────────────
    drawdown: Optional[float] = None
    raw_dd = risk_state_raw.get("drawdown")
    if raw_dd is not None:
        try:
            drawdown = float(raw_dd)
        except (TypeError, ValueError):
            pass

    # ── Consecutive losses ────────────────────────────────────────────────────
    # Count trailing losses from outcomes sorted by fill date
    consecutive_losses: Optional[int] = None
    sorted_outcomes = sorted(
        [o for o in outcomes if o.get("current_return_pct") is not None],
        key=lambda o: o.get("filled_at", ""),
    )
    if sorted_outcomes:
        streak = 0
        for o in reversed(sorted_outcomes):
            if float(o["current_return_pct"]) < 0:
                streak += 1
            else:
                break
        consecutive_losses = streak

    return {
        "filled_trade_count": filled_trade_count,
        "observation_count": observation_count,
        "expectancy_after_costs": expectancy_after_costs,
        "strategy_period_return_pct": strategy_return,
        "spy_period_return_pct": spy_return,
        "bil_period_return_pct": bil_return,
        "risk_limit_breaches": risk_limit_breaches,
        "operational_failures": op_failures,
        "drawdown": drawdown,
        "consecutive_losses": consecutive_losses,
    }


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Evaluate a strategy experiment for promotion readiness.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--experiment-id",
        metavar="ID",
        required=True,
        help="Experiment ID to evaluate (must exist in data/history/experiments/).",
    )

    dg = p.add_argument_group("decision (requires explicit operator action)")
    dg.add_argument(
        "--approve",
        action="store_true",
        help="Record a human approval decision. Requires --approved-by.",
    )
    dg.add_argument(
        "--reject",
        action="store_true",
        help="Record a rejection decision.",
    )
    dg.add_argument(
        "--approved-by",
        metavar="NAME",
        help="Operator identifier. Required when --approve is set.",
    )
    dg.add_argument(
        "--notes",
        metavar="TEXT",
        default="",
        help="Rationale or free-text notes for the decision.",
    )

    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the evaluation without writing files.",
    )
    return p


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    if args.approve and args.reject:
        print(
            "[evaluate_promotion] ERROR: cannot use --approve and --reject together.",
            file=sys.stderr,
        )
        return 1

    if args.approve and not args.approved_by:
        print(
            "[evaluate_promotion] ERROR: --approve requires --approved-by <name>.",
            file=sys.stderr,
        )
        return 1

    print(
        "[evaluate_promotion] evaluating — "
        "no config will be modified, no orders placed"
    )

    # ── Load experiment ───────────────────────────────────────────────────────
    exp_path = _EXPERIMENTS_DIR / f"{args.experiment_id}.json"
    if not exp_path.exists():
        print(
            f"[evaluate_promotion] ERROR: experiment not found: {exp_path}",
            file=sys.stderr,
        )
        return 1

    try:
        experiment = json.loads(exp_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(
            f"[evaluate_promotion] ERROR: could not read experiment: {exc}",
            file=sys.stderr,
        )
        return 1

    # ── Collect evidence from data/latest ────────────────────────────────────
    evidence = _collect_evidence(experiment)
    print(f"  evidence: fills={evidence['filled_trade_count']}  "
          f"obs={evidence['observation_count']}  "
          f"expectancy={evidence['expectancy_after_costs']}")

    # ── Run evaluation ────────────────────────────────────────────────────────
    evaluation = evaluate_promotion(experiment, **evidence, notes=args.notes)

    # ── Check demotion ────────────────────────────────────────────────────────
    demotion = check_demotion(experiment, evaluation)
    if demotion["triggered"]:
        print("[evaluate_promotion] WARNING: demotion criteria triggered:")
        for r in demotion["reasons"]:
            print(f"  - {r}")

    # ── Dry run ───────────────────────────────────────────────────────────────
    if args.dry_run:
        print("\n[evaluate_promotion] --dry-run: no files written\n")
        print(json.dumps(evaluation, indent=2, sort_keys=True, default=str))
        return 0

    # ── Write evaluation ──────────────────────────────────────────────────────
    ts = _compact_ts()
    eval_path = _EXPERIMENTS_DIR / f"{args.experiment_id}_eval_{ts}.json"
    _write_json_atomic(eval_path, evaluation)

    # ── Record decision if requested ──────────────────────────────────────────
    if args.approve or args.reject:
        decision_value = DECISION_APPROVED if args.approve else DECISION_REJECTED
        try:
            decision = build_promotion_decision(
                experiment,
                evaluation,
                decision=decision_value,
                approved_by=args.approved_by,
                approval_notes=args.notes,
            )
        except ValueError as exc:
            print(
                f"[evaluate_promotion] ERROR building decision: {exc}",
                file=sys.stderr,
            )
            return 1

        decision_path = (
            _EXPERIMENTS_DIR / f"{args.experiment_id}_decision_{ts}.json"
        )
        _write_json_atomic(decision_path, decision)
        _append_promotion_log(decision)

    # ── Print summary ─────────────────────────────────────────────────────────
    eid = args.experiment_id
    met = evaluation["all_promotion_criteria_met"]
    criteria = evaluation["criteria_met"]

    print()
    print(f"[evaluate_promotion] experiment_id    = {eid}")
    print(f"[evaluate_promotion] fills            = {evidence['filled_trade_count']}")
    print(f"[evaluate_promotion] observations     = {evidence['observation_count']}")
    print(f"[evaluate_promotion] expectancy       = {evidence['expectancy_after_costs']}")
    print(f"[evaluate_promotion] all criteria met = {met}")
    print()
    print("[evaluate_promotion] Criteria breakdown:")
    for k, v in criteria.items():
        mark = "PASS" if v else "FAIL"
        print(f"  [{mark}] {k}")
    print()

    if met and not (args.approve or args.reject):
        print("[evaluate_promotion] All criteria met. To record approval:")
        print(f"  python scripts/evaluate_promotion.py \\")
        print(f"      --experiment-id {eid} \\")
        print(f"      --approve --approved-by <your-name> --notes 'rationale'")
    elif not met:
        print("[evaluate_promotion] Not all criteria met — experiment needs more evidence.")
    elif args.approve:
        print(
            f"[evaluate_promotion] Decision APPROVED by {args.approved_by}. "
            "See candidate_pr_instructions in the evaluation JSON to apply."
        )
    elif args.reject:
        print("[evaluate_promotion] Decision REJECTED.")

    print()
    print(
        "[evaluate_promotion] production_mutation_allowed=False — "
        "no config changed"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
