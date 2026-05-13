#!/usr/bin/env python3
"""Track paper trade outcomes — research only, no execution path.

Usage:
    python scripts/track_outcomes.py
    python scripts/track_outcomes.py --dry-run   # collect and print, do not write files

Exit codes:
    0  outcomes written (or dry-run completed)
    1  error

Outputs:
    data/latest/outcome_snapshot.json        (replaced each run)
    data/history/outcomes/outcome_<date>-<hash8>.json
    memory/TRADE-LOG.md                      (appended)
    memory/EXPERIMENT-LOG.md                 (appended, observations only)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import HISTORY_DIR, LATEST_DIR, MEMORY_DIR
from trading_os.research.outcome_tracker import (
    _load_json,
    build_outcome_snapshot,
    load_existing_outcomes,
    write_outcome_snapshot,
)
from trading_os.research.lineage import _load_json as _lineage_load_json


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build and write trade outcome records. Research only — no execution.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Collect data and print outcomes without writing any files.",
    )
    args = parser.parse_args()

    print(
        "[track_outcomes] starting  "
        "(ENABLE_PAPER_EXECUTION is not read — execution impossible from this path)"
    )

    monitor_report = _load_json(LATEST_DIR / "order_monitor_report.json", {})
    positions_snapshot = _load_json(LATEST_DIR / "positions_snapshot.json", {})
    market_snapshot = _load_json(LATEST_DIR / "market_snapshot.json", {})
    lineage_snapshot = _lineage_load_json(LATEST_DIR / "lineage_snapshot.json", None)

    if not monitor_report:
        print("[track_outcomes] WARNING: order_monitor_report.json not found or empty")
    if lineage_snapshot:
        print(
            f"  lineage snapshot loaded: {lineage_snapshot.get('lineage_count', 0)} records "
            f"({lineage_snapshot.get('complete_count', 0)} complete, "
            f"{lineage_snapshot.get('partial_count', 0)} partial)"
        )
    else:
        print("  lineage snapshot not found — run build_lineage.py to recover trigger provenance")

    existing_outcomes = load_existing_outcomes(LATEST_DIR)
    print(f"  existing outcomes loaded: {len(existing_outcomes)}")

    try:
        snapshot = build_outcome_snapshot(
            monitor_report=monitor_report,
            positions_snapshot=positions_snapshot,
            market_snapshot=market_snapshot,
            existing_outcomes=existing_outcomes,
            lineage_snapshot=lineage_snapshot,
        )
    except Exception as exc:
        print(f"[track_outcomes] ERROR building snapshot: {exc}", file=sys.stderr)
        return 1

    summary = {
        "run_id": snapshot.get("run_id"),
        "generated_at": snapshot.get("generated_at"),
        "outcomes_count": snapshot.get("outcomes_count"),
        "symbols": [o.get("symbol") for o in snapshot.get("outcomes", [])],
    }

    if args.dry_run:
        print("[track_outcomes] DRY RUN — not writing files.")
        print(json.dumps(summary, indent=2))
        for o in snapshot.get("outcomes", []):
            print(
                f"  {o.get('symbol')} {(o.get('side') or '').upper()} "
                f"fill=${o.get('fill_price')} "
                f"return={o.get('current_return_pct'):+.3%}"
                if o.get("current_return_pct") is not None
                else f"  {o.get('symbol')} {(o.get('side') or '').upper()} "
                f"fill=${o.get('fill_price')} return=n/a"
            )
        return 0

    try:
        paths = write_outcome_snapshot(
            snapshot,
            latest_dir=LATEST_DIR,
            outcomes_dir=HISTORY_DIR / "outcomes",
            memory_dir=MEMORY_DIR,
        )
    except Exception as exc:
        print(f"[track_outcomes] ERROR writing: {exc}", file=sys.stderr)
        return 1

    print("[track_outcomes] done")
    print(f"  latest_path:          {paths['latest_path']}")
    print(f"  history_path:         {paths['history_path']}")
    print(f"  trade_log:            {paths['trade_log_path']}")
    if paths.get("experiment_log_path"):
        print(f"  experiment_log:       {paths['experiment_log_path']}")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
