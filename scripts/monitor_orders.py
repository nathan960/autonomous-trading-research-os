#!/usr/bin/env python3
"""Order lifecycle monitor — fetch broker order state for all submitted paper orders.

Usage:
    python scripts/monitor_orders.py
    python scripts/monitor_orders.py --dry-run   # use stored snapshots, no network

Exit codes:
    0  monitor completed; order_monitor_report.json written and TRADE-LOG.md updated
    1  missing env vars, missing API keys, fetch error, or unrecoverable failure

Outputs:
    data/latest/order_monitor_report.json       (latest snapshot)
    data/history/orders/order_monitor_<run_id>.json  (per-run record)
    memory/TRADE-LOG.md                         (appended)

Safety guarantees:
- Never places, cancels, or replaces orders. Read-only Alpaca calls only.
- Fails closed (exit 1) if TRADING_MODE != paper or ALPACA_PAPER is not true/1.
- Never prints, logs, or writes API keys or secrets.
- ENABLE_PAPER_EXECUTION is not read — execution is impossible from this path.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import (
    HISTORY_DIR,
    LATEST_DIR,
    MEMORY_DIR,
)
from trading_os.monitoring.order_monitor import (
    append_trade_log,
    fetch_broker_orders,
    run_order_monitor,
)
from trading_os.time_utils import utc_now_iso

_ORDERS_DIR = HISTORY_DIR / "orders"
_EXECUTIONS_DIR = HISTORY_DIR / "executions"
_TRADE_LOG_PATH = MEMORY_DIR / "TRADE-LOG.md"
_TRADE_PLAN_PATH = LATEST_DIR / "trade_plan.json"


# ---------------------------------------------------------------------------
# Env gates
# ---------------------------------------------------------------------------

def _check_env_gates() -> None:
    """Raise RuntimeError if paper-mode env vars are wrong."""
    mode = os.environ.get("TRADING_MODE", "")
    if mode.lower() != "paper":
        raise RuntimeError(
            f"TRADING_MODE must be 'paper' (got {mode!r}). "
            "monitor_orders.py never runs in live mode."
        )
    alpaca_paper = os.environ.get("ALPACA_PAPER", "").lower()
    if alpaca_paper not in ("true", "1"):
        raise RuntimeError(
            f"ALPACA_PAPER must be 'true' or '1' (got {alpaca_paper!r}). "
            "monitor_orders.py only operates in paper mode."
        )
    if os.environ.get("LIVE_TRADING_CONFIRMED", "").lower() in (
        "true", "1", "yes", "y", "on"
    ):
        raise RuntimeError(
            "LIVE_TRADING_CONFIRMED must not be set — "
            "monitor_orders.py refuses to run when live trading is confirmed."
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


def _load_json(path: Path, label: str) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"{label} not found: {path}")
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as exc:
        raise ValueError(f"Could not parse {label}: {exc}") from exc


def _build_dry_run_broker_lookup(orders_snap: dict) -> dict:
    """Build a broker lookup dict from the stored orders snapshot."""
    by_broker: dict = {}
    by_client: dict = {}
    for o in orders_snap.get("orders", []):
        if not isinstance(o, dict):
            continue
        bid = o.get("id") or o.get("order_id")
        cid = o.get("client_order_id")
        if bid:
            by_broker[str(bid)] = o
        if cid:
            by_client[str(cid)] = o
    return {"by_broker_id": by_broker, "by_client_id": by_client}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Order lifecycle monitor — read-only, never submits or cancels."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Use stored snapshots instead of fetching from Alpaca.",
    )
    args = parser.parse_args()

    print(
        f"[monitor_orders] starting  dry_run={args.dry_run}  "
        f"(ENABLE_PAPER_EXECUTION is not read — execution impossible from this path)"
    )

    # ── Env gates ────────────────────────────────────────────────────────────
    if not args.dry_run:
        try:
            _check_env_gates()
        except RuntimeError as exc:
            print(f"[monitor_orders] FATAL env gate: {exc}", file=sys.stderr)
            return 1

    # ── Fetch or load broker state ────────────────────────────────────────────
    positions: list = []
    clock: dict = {}
    broker_lookup: dict = {"by_broker_id": {}, "by_client_id": {}}

    if args.dry_run:
        print("  dry_run=True — loading stored snapshots")
        try:
            pos_snap = _load_json(LATEST_DIR / "positions_snapshot.json", "positions_snapshot")
            positions = pos_snap.get("positions", [])
        except FileNotFoundError:
            print("  WARNING: positions_snapshot.json not found — positions will be empty")
            positions = []

        try:
            acct_snap = _load_json(LATEST_DIR / "account_snapshot.json", "account_snapshot")
            clock = acct_snap.get("clock", {})
        except FileNotFoundError:
            print("  WARNING: account_snapshot.json not found — clock will be empty")
            clock = {}

        try:
            orders_snap = _load_json(LATEST_DIR / "orders_snapshot.json", "orders_snapshot")
            broker_lookup = _build_dry_run_broker_lookup(orders_snap)
            print(
                f"  loaded {len(broker_lookup['by_broker_id'])} broker orders from snapshot"
            )
        except FileNotFoundError:
            print("  WARNING: orders_snapshot.json not found — no broker orders available")
            broker_lookup = {"by_broker_id": {}, "by_client_id": {}}

    else:
        # Live fetch via Alpaca paper client
        try:
            from trading_os.data.alpaca_client import AlpacaPaperClient
            from trading_os.data.alpaca_client import _to_primitive
            from trading_os.data.account_state import fetch_account_state

            alpaca_client = AlpacaPaperClient()
        except RuntimeError as exc:
            print(f"[monitor_orders] FATAL broker gate: {exc}", file=sys.stderr)
            return 1

        try:
            fresh_state = fetch_account_state(alpaca_client)
        except Exception as exc:
            print(f"[monitor_orders] ERROR fetching account state: {exc}", file=sys.stderr)
            return 1

        positions = fresh_state.get("positions", [])
        clock = fresh_state.get("clock", {})

        print(
            f"  fetched from Alpaca  is_open={clock.get('is_open')}  "
            f"positions={len(positions)}  open_orders={fresh_state.get('open_order_count')}"
        )

        # Load known broker/client IDs from audit files so fetch_broker_orders
        # can attempt direct lookups for any orders not in the bulk results.
        from trading_os.monitoring.order_monitor import load_submitted_audits
        known_broker_ids: list = []
        known_client_ids: list = []
        for _, audit in load_submitted_audits(_ORDERS_DIR):
            bid = audit.get("broker_order_id")
            cid = audit.get("client_order_id")
            if bid:
                known_broker_ids.append(str(bid))
            if cid:
                known_client_ids.append(str(cid))

        try:
            trading_client = alpaca_client.trading_client()
            broker_lookup = fetch_broker_orders(
                trading_client,
                known_broker_ids=known_broker_ids,
                known_client_ids=known_client_ids,
            )
            fl = broker_lookup.get("fetch_log", {})
            print(
                f"  broker fetch: open={fl.get('open_count', '?')}  "
                f"closed={fl.get('closed_count', '?')}  "
                f"direct_broker_id_hits={fl.get('direct_broker_id_hits', 0)}  "
                f"direct_client_id_hits={fl.get('direct_client_id_hits', 0)}  "
                f"direct_broker_id_errors={fl.get('direct_broker_id_errors', 0)}  "
                f"direct_client_id_errors={fl.get('direct_client_id_errors', 0)}"
            )
        except Exception as exc:
            print(f"[monitor_orders] ERROR fetching broker orders: {exc}", file=sys.stderr)
            return 1

    # ── Run order monitor ────────────────────────────────────────────────────
    report = run_order_monitor(
        broker_lookup=broker_lookup,
        orders_dir=_ORDERS_DIR,
        executions_dir=_EXECUTIONS_DIR,
        positions=positions,
        clock=clock,
        trade_plan_path=_TRADE_PLAN_PATH if _TRADE_PLAN_PATH.exists() else None,
        dry_run=args.dry_run,
    )

    n_tracked = report.get("orders_tracked", 0)
    n_filled = report.get("orders_filled", 0)
    n_active = report.get("orders_active", 0)
    n_missing = report.get("orders_missing", 0)
    stale = report.get("stale_orders", [])
    warnings = report.get("warnings", [])

    print(
        f"  orders_tracked={n_tracked}  filled={n_filled}  "
        f"active={n_active}  missing={n_missing}"
    )

    for lc in report.get("lifecycles", []):
        symbol = lc.get("symbol", "?")
        cid = lc.get("client_order_id", "?")
        status = lc.get("lifecycle_status", "?")
        fill = lc.get("fill")
        fill_str = ""
        if fill:
            fill_str = (
                f"  fill_price={fill.get('fill_price')}  "
                f"filled_qty={fill.get('filled_qty')}  "
                f"position_confirmed={fill.get('position_confirmed')}"
            )
        print(f"  {symbol:6s}  {cid}  status={status}{fill_str}")

    for w in warnings:
        print(f"  WARNING: {w}", file=sys.stderr)

    for s in stale:
        print(f"  STALE ORDER: {s}", file=sys.stderr)

    # ── Write outputs ─────────────────────────────────────────────────────────
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    _write_json(LATEST_DIR / "order_monitor_report.json", report)

    run_id = report["run_id"]
    history_path = _ORDERS_DIR / f"{run_id}.json"
    _write_json(history_path, report)

    append_trade_log(report, _TRADE_LOG_PATH)
    print(f"  appended {_TRADE_LOG_PATH.relative_to(_ROOT)}")

    # ── Warn about stale orders in risk summary ──────────────────────────────
    if stale:
        print(
            f"[monitor_orders] WARNING: {len(stale)} stale day order(s) detected "
            "— review TRADE-LOG.md",
            file=sys.stderr,
        )

    print(f"[monitor_orders] done  run_id={run_id}  orders_tracked={n_tracked}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
