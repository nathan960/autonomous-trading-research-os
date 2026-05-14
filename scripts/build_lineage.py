#!/usr/bin/env python3
"""Build trade lineage snapshot — research only, no execution path.

Links filled orders back to the trigger snapshots, candidates, and trigger IDs
that produced them. Outputs data/latest/lineage_snapshot.json.

Usage:
    python scripts/build_lineage.py
    python scripts/build_lineage.py --dry-run   # build and print, do not write files
    python scripts/build_lineage.py --days 14   # look back further for trigger history

Exit codes:
    0  lineage snapshot written (or dry-run completed)
    1  error

Outputs:
    data/latest/lineage_snapshot.json               (replaced each run)
    data/history/lineage/lineage_<date>-<hash8>.json
    memory/SIGNAL-LOG.md                            (appended)

Safety:
    ENABLE_PAPER_EXECUTION is never read.
    No Alpaca API calls. No order submission. No trade plan approval.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import HISTORY_DIR, LATEST_DIR, MEMORY_DIR
from trading_os.research.lineage import (
    _load_json,
    build_lineage_snapshot,
    load_execution_index,
    load_trade_plan_history,
    load_trigger_history_lines,
    write_lineage_snapshot,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Build trade lineage snapshot. Research only — no execution path."
        )
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Build and print lineage without writing any files.",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=7,
        help="Number of calendar days to include in trigger history lookback (default: 7).",
    )
    args = parser.parse_args()

    print(
        "[build_lineage] starting  "
        "(ENABLE_PAPER_EXECUTION is not read — execution impossible from this path)"
    )

    # Load all required inputs
    monitor_report = _load_json(LATEST_DIR / "order_monitor_report.json", {})
    trigger_snapshot = _load_json(LATEST_DIR / "trigger_snapshot.json", {})
    current_trade_plan = _load_json(LATEST_DIR / "trade_plan.json", {})
    outcome_snapshot = _load_json(LATEST_DIR / "outcome_snapshot.json", {})

    if not monitor_report:
        print("[build_lineage] WARNING: order_monitor_report.json not found or empty")

    fills_count = sum(
        1 for lc in (monitor_report.get("lifecycles") or [])
        if lc.get("lifecycle_status") in ("filled", "partially_filled")
    )
    print(f"  filled lifecycles in monitor report: {fills_count}")

    # Load trigger history lines for lookback window
    today_str = date.today().isoformat()
    from trading_os.research.lineage import _date_range
    date_strs = _date_range(today_str, args.days)
    trigger_history_lines = load_trigger_history_lines(HISTORY_DIR, date_strs)
    print(f"  trigger history lines loaded: {len(trigger_history_lines)} (last {args.days} days)")

    # Load execution index
    execution_index = load_execution_index(HISTORY_DIR)
    print(f"  execution reports indexed: {len(execution_index)}")

    # Load trade plan history — enables complete lineage for archived plans
    trade_plan_history = load_trade_plan_history(HISTORY_DIR)
    print(f"  trade plan history loaded: {len(trade_plan_history)} plans")

    try:
        snapshot = build_lineage_snapshot(
            monitor_report=monitor_report,
            execution_index=execution_index,
            current_trade_plan=current_trade_plan,
            trigger_history_lines=trigger_history_lines,
            trigger_snapshot=trigger_snapshot,
            outcome_snapshot=outcome_snapshot,
            trade_plan_history=trade_plan_history,
        )
    except Exception as exc:
        print(f"[build_lineage] ERROR building snapshot: {exc}", file=sys.stderr)
        return 1

    summary = {
        "run_id": snapshot.get("run_id"),
        "generated_at": snapshot.get("generated_at"),
        "lineage_count": snapshot.get("lineage_count"),
        "complete_count": snapshot.get("complete_count"),
        "partial_count": snapshot.get("partial_count"),
    }

    if args.dry_run:
        print("[build_lineage] DRY RUN — not writing files.")
        print(json.dumps(summary, indent=2))
        for r in snapshot.get("lineage_records", []):
            tids = r.get("trigger_ids") or []
            print(
                f"  {r.get('symbol')} {(r.get('side') or '').upper()} "
                f"status={r.get('lineage_status')} "
                f"trigger_hash={str(r.get('trigger_snapshot_hash') or 'null')[:16]} "
                f"trigger_ids={tids}"
            )
        return 0

    try:
        paths = write_lineage_snapshot(
            snapshot,
            latest_dir=LATEST_DIR,
            lineage_history_dir=HISTORY_DIR / "lineage",
            memory_dir=MEMORY_DIR,
        )
    except Exception as exc:
        print(f"[build_lineage] ERROR writing: {exc}", file=sys.stderr)
        return 1

    print("[build_lineage] done")
    print(f"  latest_path:   {paths['latest_path']}")
    print(f"  history_path:  {paths['history_path']}")
    print(f"  signal_log:    {paths['signal_log_path']}")
    print(json.dumps(summary, indent=2))

    # Report lineage completeness
    for r in snapshot.get("lineage_records", []):
        status = r.get("lineage_status")
        sym = r.get("symbol")
        tids = r.get("trigger_ids") or []
        h_short = str(r.get("trigger_snapshot_hash") or "null")[:16]
        print(
            f"  {sym} {(r.get('side') or '').upper()} "
            f"status={status} hash={h_short} trigger_ids={tids}"
        )
        if r.get("lineage_note"):
            print(f"    note: {r['lineage_note']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
