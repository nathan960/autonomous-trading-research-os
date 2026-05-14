#!/usr/bin/env python3
"""List open Alpaca paper orders — read-only, no execution path.

Fetches current open orders from the Alpaca paper account and writes an
audit record. Use this to inspect what orders are outstanding before
deciding whether to run cancel_paper_order.py.

Usage:
    python scripts/list_open_orders.py
    python scripts/list_open_orders.py --dry-run   # use stored snapshot

Exit codes:
    0  listing complete; audit file written
    1  env gate failure, API error, or unrecoverable error

Outputs:
    data/history/orders/list_open_orders_<run_id>.json
    memory/ORDER-RESOLUTION-LOG.md  (appended)

Safety guarantees:
- NEVER places, cancels, or replaces orders. Read-only Alpaca calls only.
- Requires TRADING_MODE=paper, ALPACA_PAPER=true/1.
- Refuses to run when LIVE_TRADING_CONFIRMED=true.
- Never prints, logs, or writes API keys or secrets.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import HISTORY_DIR, LATEST_DIR, MEMORY_DIR
from trading_os.data.alpaca_client import AlpacaPaperClient, _to_primitive
from trading_os.execution.open_order_resolution import (
    build_order_list_record,
    format_order_list_markdown,
)
from trading_os.time_utils import utc_now_iso

_ORDERS_DIR = HISTORY_DIR / "orders"
_LOG_PATH = MEMORY_DIR / "ORDER-RESOLUTION-LOG.md"


# ---------------------------------------------------------------------------
# Env gates
# ---------------------------------------------------------------------------

def _check_env_gates() -> None:
    mode = os.environ.get("TRADING_MODE", "").lower()
    if mode != "paper":
        raise RuntimeError(
            f"TRADING_MODE must be 'paper' (got {mode!r}). "
            "list_open_orders.py refuses to run outside paper mode."
        )
    alpaca_paper = os.environ.get("ALPACA_PAPER", "").lower()
    if alpaca_paper not in ("true", "1"):
        raise RuntimeError(
            f"ALPACA_PAPER must be 'true' or '1' (got {alpaca_paper!r})."
        )
    if os.environ.get("LIVE_TRADING_CONFIRMED", "").lower() in (
        "true", "1", "yes", "y", "on"
    ):
        raise RuntimeError(
            "LIVE_TRADING_CONFIRMED must not be set — "
            "list_open_orders.py refuses to run when live trading is confirmed."
        )


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True, default=str)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(path)
    print(f"  wrote {path.relative_to(_ROOT)}")


def _append_log(record: dict) -> None:
    _LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = format_order_list_markdown(record)
    with _LOG_PATH.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    print(f"  appended {_LOG_PATH.relative_to(_ROOT)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="List open Alpaca paper orders — read-only."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Use stored orders_snapshot.json instead of fetching from Alpaca.",
    )
    args = parser.parse_args()

    print(
        f"[list_open_orders] starting  dry_run={args.dry_run}  "
        "(no orders will be placed, cancelled, or replaced)"
    )

    # ── Env gates ────────────────────────────────────────────────────────────
    if not args.dry_run:
        try:
            _check_env_gates()
        except RuntimeError as exc:
            print(f"[list_open_orders] FATAL: {exc}", file=sys.stderr)
            return 1

    # ── Fetch or load orders ─────────────────────────────────────────────────
    fetched_at = utc_now_iso()
    raw_orders: list = []

    if args.dry_run:
        snap_path = LATEST_DIR / "orders_snapshot.json"
        if snap_path.exists():
            try:
                snap = json.loads(snap_path.read_text(encoding="utf-8"))
                raw_orders = [o for o in snap.get("orders", []) if isinstance(o, dict)]
                print(f"  dry_run: loaded {len(raw_orders)} orders from snapshot")
            except Exception as exc:
                print(f"  WARNING: could not load orders snapshot: {exc}")
        else:
            print("  dry_run: orders_snapshot.json not found — using empty list")
    else:
        try:
            client = AlpacaPaperClient()
        except RuntimeError as exc:
            print(f"[list_open_orders] FATAL broker gate: {exc}", file=sys.stderr)
            return 1

        try:
            from alpaca.trading.enums import QueryOrderStatus
            from alpaca.trading.requests import GetOrdersRequest

            tc = client.trading_client()
            request = GetOrdersRequest(status=QueryOrderStatus.OPEN, limit=100)
            orders_response = tc.get_orders(filter=request)
            raw_orders = [_to_primitive(o) for o in (orders_response or [])]
            print(f"  fetched {len(raw_orders)} open orders from Alpaca paper")
        except Exception as exc:
            print(f"[list_open_orders] ERROR fetching orders: {exc}", file=sys.stderr)
            return 1

    # ── Build record ─────────────────────────────────────────────────────────
    from trading_os.hashing import stable_hash
    run_id = (
        f"list_open_orders-"
        f"{fetched_at.replace(':', '').replace('-', '').replace('Z', '')[:15]}"
        f"-{stable_hash({'ts': fetched_at})[:8]}"
    )

    record = build_order_list_record(
        orders=raw_orders,
        run_id=run_id,
        fetched_at=fetched_at,
        source="alpaca_paper" if not args.dry_run else "dry_run_snapshot",
    )

    # ── Print summary ─────────────────────────────────────────────────────────
    print()
    print(f"[list_open_orders] open_order_count={record['open_order_count']}")
    for o in record["orders"]:
        print(
            f"  {o.get('symbol'):6s}  {o.get('side'):4s}  "
            f"status={o.get('status')}  "
            f"notional={o.get('notional')}  "
            f"client_order_id={o.get('client_order_id')}  "
            f"broker_order_id={o.get('broker_order_id')}"
        )
    if not record["orders"]:
        print("  (no open orders)")
    print()

    # ── Write outputs ─────────────────────────────────────────────────────────
    _write_json(_ORDERS_DIR / f"{run_id}.json", record)
    _append_log(record)

    print(f"[list_open_orders] done  run_id={run_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
