#!/usr/bin/env python3
"""Weekly review script — research only, no execution path.

Usage:
    python scripts/weekly_review.py
    python scripts/weekly_review.py --date 2026-05-13   # end date of the 7-day window
    python scripts/weekly_review.py --days 14            # look back N days (default 7)
    python scripts/weekly_review.py --dry-run            # collect only, do not write files

Exit codes:
    0  review written
    1  error

Outputs:
    data/history/runs/weekly_review-<date>-<hash>.json
    memory/WEEKLY-REVIEW.md  (appended)
    memory/EXPERIMENT-LOG.md (appended, only if issues/observations exist)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import HISTORY_DIR, MEMORY_DIR
from trading_os.research.weekly_review import build_weekly_review, write_weekly_review


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build and write the weekly review. Research only — no execution.",
    )
    parser.add_argument(
        "--date",
        metavar="YYYY-MM-DD",
        default=None,
        help="End date of the review window (default: today).",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=7,
        help="Number of days to look back (default: 7).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Collect data and print summary without writing any files.",
    )
    args = parser.parse_args()

    print(f"[weekly_review] collecting last {args.days} days...")

    try:
        review = build_weekly_review(end_date_str=args.date, days=args.days)
    except Exception as exc:
        print(f"[weekly_review] ERROR collecting: {exc}", file=sys.stderr)
        return 1

    if args.dry_run:
        print("[weekly_review] DRY RUN — not writing files.")
        print(json.dumps({
            "run_id": review.get("run_id"),
            "period_start": review.get("period_start"),
            "period_end": review.get("period_end"),
            "generated_at": review.get("generated_at"),
            "trigger_scans_total": review.get("trigger_scans", {}).get("total_runs"),
            "dry_runs_total": review.get("dry_runs", {}).get("total_runs"),
            "paper_executions": review.get("paper_executions", {}).get("total_attempts"),
            "alerts_this_period": review.get("alerts", {}).get("alerts_this_period"),
            "operational_issues_count": len(review.get("operational_issues", [])),
        }, indent=2))
        return 0

    try:
        paths = write_weekly_review(
            review,
            runs_dir=HISTORY_DIR / "runs",
            memory_dir=MEMORY_DIR,
        )
    except Exception as exc:
        print(f"[weekly_review] ERROR writing: {exc}", file=sys.stderr)
        return 1

    print("[weekly_review] done")
    print(f"  json_path:            {paths['json_path']}")
    print(f"  md_path:              {paths['md_path']}")
    if paths.get("experiment_log_path"):
        print(f"  experiment_log_path:  {paths['experiment_log_path']}")

    issues = review.get("operational_issues", [])
    if issues:
        print(f"\n[weekly_review] {len(issues)} operational issue(s):")
        for issue in issues:
            print(f"  - {issue}")

    print(json.dumps({
        "run_id": review.get("run_id"),
        "period_start": review.get("period_start"),
        "period_end": review.get("period_end"),
        "status": review.get("status"),
        "operational_issues_count": len(issues),
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
