#!/usr/bin/env python3
"""Daily summary script — research only, no execution path.

Usage:
    python scripts/daily_summary.py
    python scripts/daily_summary.py --date 2026-05-13
    python scripts/daily_summary.py --dry-run       # collect only, do not write files

Exit codes:
    0  summary written
    1  error

Outputs:
    data/history/runs/daily_summary-<date>-<hash>.json
    memory/DAILY-SUMMARY.md  (appended)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import HISTORY_DIR, MEMORY_DIR
from trading_os.research.daily_summary import build_daily_summary, write_daily_summary


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build and write the daily summary. Research only — no execution.",
    )
    parser.add_argument(
        "--date",
        metavar="YYYY-MM-DD",
        default=None,
        help="Date to summarise (default: today).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Collect data and print summary without writing any files.",
    )
    args = parser.parse_args()

    print("[daily_summary] collecting...")

    try:
        summary = build_daily_summary(date_str=args.date)
    except Exception as exc:
        print(f"[daily_summary] ERROR collecting: {exc}", file=sys.stderr)
        return 1

    if args.dry_run:
        print("[daily_summary] DRY RUN — not writing files.")
        print(json.dumps({
            "run_id": summary.get("run_id"),
            "date": summary.get("date"),
            "generated_at": summary.get("generated_at"),
            "positions_count": len(summary.get("positions", [])),
            "open_orders_count": len(summary.get("open_orders", [])),
            "dry_runs_today": summary.get("dry_runs", {}).get("count", 0),
            "paper_executions_today": summary.get("paper_executions", {}).get("count", 0),
            "alerts_total": summary.get("alerts", {}).get("total_count", 0),
        }, indent=2))
        return 0

    try:
        paths = write_daily_summary(
            summary,
            runs_dir=HISTORY_DIR / "runs",
            memory_dir=MEMORY_DIR,
        )
    except Exception as exc:
        print(f"[daily_summary] ERROR writing: {exc}", file=sys.stderr)
        return 1

    print("[daily_summary] done")
    print(f"  json_path: {paths['json_path']}")
    print(f"  md_path:   {paths['md_path']}")
    print(json.dumps({
        "run_id": summary.get("run_id"),
        "date": summary.get("date"),
        "generated_at": summary.get("generated_at"),
        "status": summary.get("status"),
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
