#!/usr/bin/env python3
"""Rebuild memory markdown logs from event JSON files.

Event JSON files in data/history/events/ are the primary audit trail.
This script regenerates the markdown memory logs from those events so
that conflicts in append-only markdown files can be resolved by simply
running this script.

Rebuilds:
    memory/TRADE-LOG.md    from dry_run, paper_execution, order_monitor, outcome_tracker
    memory/TRIGGER-LOG.md  from trigger_scan, alert_intake, alert_router
    memory/SIGNAL-LOG.md   from alert_intake, alert_router

Usage:
    python scripts/rebuild_memory_logs.py
    python scripts/rebuild_memory_logs.py --dry-run   # print, do not write
    python scripts/rebuild_memory_logs.py --days 30   # extend lookback window

Exit codes:
    0  rebuild completed (or dry-run completed)
    1  error

Safety:
    ENABLE_PAPER_EXECUTION is never read.
    No Alpaca API calls. No order submission. No risk config changes.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import HISTORY_DIR, MEMORY_DIR
from trading_os.logging.event_log import (
    LOG_EVENT_ROUTING,
    format_event_as_markdown,
    read_events,
)

_EVENTS_DIR = HISTORY_DIR / "events"

_LOG_HEADERS = {
    "TRADE-LOG.md": (
        "# Trade Log\n\n"
        "_Rebuilt from data/history/events/ by rebuild_memory_logs.py. "
        "Event JSON files are the source of truth._\n\n"
    ),
    "TRIGGER-LOG.md": (
        "# Trigger Log\n\n"
        "_Rebuilt from data/history/events/ by rebuild_memory_logs.py. "
        "Event JSON files are the source of truth._\n\n"
    ),
    "SIGNAL-LOG.md": (
        "# Signal Log\n\n"
        "_Rebuilt from data/history/events/ by rebuild_memory_logs.py. "
        "Event JSON files are the source of truth._\n\n"
    ),
}


def rebuild_log(log_name: str, events_dir: Path, days: int) -> str:
    """Build the full markdown content for one log file from events."""
    event_types = LOG_EVENT_ROUTING[log_name]
    events = read_events(events_dir, event_types=event_types, days=days)

    header = _LOG_HEADERS.get(log_name, f"# {log_name}\n\n")
    if not events:
        return header + "_No events found in the lookback window._\n"

    sections = [format_event_as_markdown(e) for e in events]
    return header + "\n".join(sections)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Rebuild memory markdown logs from event JSON files. "
            "Research only — no execution path."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Print rebuilt content without writing files.",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=90,
        help="Number of calendar days of events to include (default: 90).",
    )
    args = parser.parse_args()

    print(
        "[rebuild_memory_logs] starting  "
        "(ENABLE_PAPER_EXECUTION is not read — execution impossible from this path)"
    )

    if not _EVENTS_DIR.is_dir():
        print(
            f"[rebuild_memory_logs] WARNING: events directory not found: {_EVENTS_DIR}",
            file=sys.stderr,
        )
        print(
            "  Run any priority script (dry_run_execute.py, monitor_orders.py, etc.) "
            "to generate the first event files.",
        )

    log_names = list(LOG_EVENT_ROUTING.keys())
    print(f"  rebuilding: {log_names}  (last {args.days} days of events)")

    results = {}
    for log_name in log_names:
        try:
            content = rebuild_log(log_name, _EVENTS_DIR, args.days)
            results[log_name] = content
            event_types = LOG_EVENT_ROUTING[log_name]
            events = read_events(_EVENTS_DIR, event_types=event_types, days=args.days)
            print(f"  {log_name}: {len(events)} event(s)")
        except Exception as exc:
            print(f"[rebuild_memory_logs] ERROR building {log_name}: {exc}", file=sys.stderr)
            return 1

    if args.dry_run:
        print("[rebuild_memory_logs] DRY RUN — not writing files.")
        for log_name, content in results.items():
            print(f"\n{'='*60}")
            print(f"  {log_name}")
            print(f"{'='*60}")
            print(content[:2000])
            if len(content) > 2000:
                print(f"  ... ({len(content)} chars total)")
        return 0

    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    for log_name, content in results.items():
        out_path = MEMORY_DIR / log_name
        try:
            tmp = out_path.with_suffix(".tmp")
            tmp.write_text(content, encoding="utf-8")
            tmp.replace(out_path)
            print(f"  wrote {out_path.relative_to(_ROOT)}")
        except Exception as exc:
            print(f"[rebuild_memory_logs] ERROR writing {log_name}: {exc}", file=sys.stderr)
            return 1

    print("[rebuild_memory_logs] done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
