#!/usr/bin/env python3
"""Score trigger performance — research only, no execution path.

Usage:
    python scripts/score_triggers.py
    python scripts/score_triggers.py --days 14
    python scripts/score_triggers.py --dry-run   # collect and print, do not write files

Exit codes:
    0  report written (or dry-run completed)
    1  error

Outputs:
    data/latest/trigger_performance.json             (replaced each run)
    data/history/trigger_performance/trigger_performance_<date>-<hash8>.json
    memory/EXPERIMENT-LOG.md                         (appended, observations only)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import HISTORY_DIR, LATEST_DIR, MEMORY_DIR
from trading_os.research.trigger_performance import (
    build_trigger_performance,
    format_experiment_log_entry,
    write_trigger_performance,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Score trigger performance. Research only — no execution.",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=7,
        help="Number of calendar days to include (default: 7).",
    )
    parser.add_argument(
        "--end-date",
        default=None,
        help="End date ISO string (default: today).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Collect data and print report without writing any files.",
    )
    args = parser.parse_args()

    print(
        "[score_triggers] starting  "
        "(ENABLE_PAPER_EXECUTION is not read — execution impossible from this path)"
    )

    try:
        perf = build_trigger_performance(
            end_date_str=args.end_date,
            days=args.days,
            latest_dir=LATEST_DIR,
            history_dir=HISTORY_DIR,
            memory_dir=MEMORY_DIR,
        )
    except Exception as exc:
        print(f"[score_triggers] ERROR building report: {exc}", file=sys.stderr)
        return 1

    summary = {
        "run_id": perf.get("run_id"),
        "generated_at": perf.get("generated_at"),
        "period": f"{perf.get('period_start')} to {perf.get('period_end')}",
        "days": perf.get("days"),
        "status": perf.get("status"),
        "triggers_scored": len(perf.get("triggers", {})),
        "regime_sessions": perf.get("regime", {}).get("sessions_total"),
        "fills_this_period": perf.get("execution_fill_stats", {}).get("total_fills"),
        "operational_issues": len(perf.get("operational_issues", [])),
    }

    if args.dry_run:
        print("[score_triggers] DRY RUN — not writing files.")
        print(json.dumps(summary, indent=2))
        print("\nResearch observations:")
        for obs in perf.get("research_observations", []):
            print(f"  - {obs}")
        if perf.get("operational_issues"):
            print("\nOperational issues:")
            for issue in perf.get("operational_issues", []):
                print(f"  [!] {issue}")
        return 0

    try:
        paths = write_trigger_performance(
            perf,
            latest_dir=LATEST_DIR,
            tp_history_dir=HISTORY_DIR / "trigger_performance",
            memory_dir=MEMORY_DIR,
        )
    except Exception as exc:
        print(f"[score_triggers] ERROR writing: {exc}", file=sys.stderr)
        return 1

    print("[score_triggers] done")
    print(f"  latest_path:          {paths['latest_path']}")
    print(f"  history_path:         {paths['history_path']}")
    if paths.get("experiment_log_path"):
        print(f"  experiment_log:       {paths['experiment_log_path']}")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
