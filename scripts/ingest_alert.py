#!/usr/bin/env python3
"""Ingest a raw external alert (TradingView webhook, etc.) into the research pipeline.

RESEARCH-ONLY. This script never places orders, never calls execute_paper.py,
and never generates approved trade plans. It is a one-way write path into
data/history/alerts/ and memory/TRIGGER-LOG.md.

Usage:
    python scripts/ingest_alert.py --payload '{"symbol":"AAPL","next_step":"log_only"}'
    echo '{"symbol":"AAPL","next_step":"log_only"}' | python scripts/ingest_alert.py

Exit codes:
    0  alert ingested successfully
    1  validation error, duplicate, JSON parse error, or I/O failure

Outputs:
    data/history/alerts/alert-<id>.json   persisted alert record (atomic write)
    memory/TRIGGER-LOG.md                  append-only log entry

Safety:
- trade_execution_allowed is ALWAYS forced to false in the output record.
- blocked_by_default is ALWAYS forced to true in the output record.
- Never calls execute_paper.py.
- Never generates an approved trade plan.
- Never prints secrets.
- ENABLE_PAPER_EXECUTION is not read — execution is impossible from this path.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import HISTORY_DIR, MEMORY_DIR
from trading_os.research.alert_intake import AlertIntakeError, process_alert

_ALERTS_DIR = HISTORY_DIR / "alerts"
_TRIGGER_LOG = MEMORY_DIR / "TRIGGER-LOG.md"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Ingest an external alert into the research pipeline (no execution).",
    )
    parser.add_argument(
        "--payload",
        metavar="JSON",
        default=None,
        help="Raw JSON alert payload string. If omitted, reads from stdin.",
    )
    args = parser.parse_args()

    if args.payload is not None:
        raw = args.payload
    else:
        if sys.stdin.isatty():
            print(
                "[ingest_alert] ERROR: no --payload argument and stdin is a TTY.",
                file=sys.stderr,
            )
            print(
                "[ingest_alert] Usage: python scripts/ingest_alert.py "
                '--payload \'{"symbol":"AAPL","next_step":"log_only"}\'',
                file=sys.stderr,
            )
            return 1
        raw = sys.stdin.read()

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"[ingest_alert] ERROR: invalid JSON payload: {exc}", file=sys.stderr)
        return 1

    print("[ingest_alert] starting")
    print(f"  alerts_dir: {_ALERTS_DIR.relative_to(_ROOT)}")
    print(f"  trigger_log: {_TRIGGER_LOG.relative_to(_ROOT)}")

    try:
        record = process_alert(
            payload=payload,
            alerts_dir=_ALERTS_DIR,
            trigger_log_path=_TRIGGER_LOG,
        )
    except AlertIntakeError as exc:
        print(f"[ingest_alert] REJECTED: {exc.reason}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"[ingest_alert] ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"[ingest_alert] SUCCESS")
    print(f"  alert_id:              {record['alert_id']}")
    print(f"  symbol:                {record['symbol']}")
    print(f"  next_step:             {record['next_step']}")
    print(f"  trade_execution_allowed: {record['trade_execution_allowed']}")
    print(f"  blocked_by_default:    {record['blocked_by_default']}")
    print(f"  ingested_at:           {record['ingested_at']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
