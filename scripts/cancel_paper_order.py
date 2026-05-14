#!/usr/bin/env python3
"""Cancel a single open Alpaca paper order by client_order_id or broker_order_id.

SAFETY CONTRACTS — no exceptions:
- NEVER places new orders.
- NEVER replaces orders.
- NEVER operates in live mode.
- Requires --confirm-cancel CANCEL (exact string) — any other value fails closed.
- Requires TRADING_MODE=paper, ALPACA_PAPER=true, LIVE_TRADING_CONFIRMED not true.
- Fetches and validates the target order before issuing the cancel.
- The cancel is issued only against a paper Alpaca account (paper=True).
- All decisions and broker responses are written to audit files.
- Never prints, logs, or writes API keys or secrets.

Usage — cancel by client_order_id:
    python scripts/cancel_paper_order.py \\
        --client-order-id TOS-20260514T154817-EQIX-BUY \\
        --confirm-cancel CANCEL

Usage — cancel by broker (Alpaca) order UUID:
    python scripts/cancel_paper_order.py \\
        --broker-order-id 3351082e-8e6a-4148-af27-81e5414dd0db \\
        --confirm-cancel CANCEL

Usage — dry-run (no network, uses stored snapshot):
    python scripts/cancel_paper_order.py \\
        --client-order-id TOS-20260514T154817-EQIX-BUY \\
        --confirm-cancel CANCEL \\
        --dry-run

Exit codes:
    0  cancellation submitted; audit file written
    1  env gate failure, confirmation failure, order not found, validation
       failure, API error, or any unrecoverable error

Outputs:
    data/history/orders/order_cancel_<run_id>.json
    memory/TRADE-LOG.md  (appended)
    memory/ORDER-RESOLUTION-LOG.md  (appended)
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
    CANCEL_CONFIRMATION_TOKEN,
    build_cancellation_record,
    format_cancellation_markdown,
    format_order_list_markdown,
    validate_cancel_confirmation,
    validate_order_cancellable,
    validate_order_id_match,
)
from trading_os.time_utils import utc_now_iso

_ORDERS_DIR = HISTORY_DIR / "orders"
_TRADE_LOG_PATH = MEMORY_DIR / "TRADE-LOG.md"
_RESOLUTION_LOG_PATH = MEMORY_DIR / "ORDER-RESOLUTION-LOG.md"


# ---------------------------------------------------------------------------
# Env gates
# ---------------------------------------------------------------------------

def _check_env_gates() -> None:
    mode = os.environ.get("TRADING_MODE", "").lower()
    if mode != "paper":
        raise RuntimeError(
            f"TRADING_MODE must be 'paper' (got {mode!r}). "
            "cancel_paper_order.py refuses to run outside paper mode."
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
            "cancel_paper_order.py refuses to run when live trading is confirmed."
        )
    if os.environ.get("ENABLE_PAPER_EXECUTION", "").lower() in (
        "true", "1", "yes", "y", "on"
    ):
        raise RuntimeError(
            "ENABLE_PAPER_EXECUTION must not be set for cancel operations — "
            "this script is order-management only, not an execution path."
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


def _append_trade_log(record: dict) -> None:
    _TRADE_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = format_cancellation_markdown(record)
    with _TRADE_LOG_PATH.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    print(f"  appended {_TRADE_LOG_PATH.relative_to(_ROOT)}")


def _append_resolution_log(record: dict) -> None:
    _RESOLUTION_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = format_cancellation_markdown(record)
    with _RESOLUTION_LOG_PATH.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    print(f"  appended {_RESOLUTION_LOG_PATH.relative_to(_ROOT)}")


# ---------------------------------------------------------------------------
# Dry-run order lookup
# ---------------------------------------------------------------------------

def _find_order_in_snapshot(
    client_order_id: str | None,
    broker_order_id: str | None,
) -> dict | None:
    """Look up an order in the stored orders_snapshot.json for dry-run mode."""
    snap_path = LATEST_DIR / "orders_snapshot.json"
    if not snap_path.exists():
        return None
    try:
        snap = json.loads(snap_path.read_text(encoding="utf-8"))
    except Exception:
        return None
    for o in snap.get("orders", []):
        if not isinstance(o, dict):
            continue
        if client_order_id and o.get("client_order_id") == client_order_id:
            return o
        if broker_order_id and str(o.get("id", o.get("order_id", ""))) == broker_order_id:
            return o
    return None


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=(
            "Cancel a single open Alpaca paper order. "
            "Requires --confirm-cancel CANCEL."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    id_group = p.add_mutually_exclusive_group(required=False)
    id_group.add_argument(
        "--client-order-id",
        metavar="ID",
        help="TOS-... client order ID to cancel.",
    )
    id_group.add_argument(
        "--broker-order-id",
        metavar="UUID",
        help="Alpaca broker order UUID to cancel.",
    )
    p.add_argument(
        "--confirm-cancel",
        metavar="TOKEN",
        required=True,
        help=f"Must be exactly '{CANCEL_CONFIRMATION_TOKEN}'. Any other value fails closed.",
    )
    p.add_argument(
        "--notes",
        metavar="TEXT",
        default="",
        help="Optional free-text rationale for the cancellation.",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help=(
            "Validate and look up the order using the stored snapshot "
            "but do not call the broker cancel API."
        ),
    )
    return p


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    print(
        f"[cancel_paper_order] starting  dry_run={args.dry_run}  "
        "(no new orders will be placed or replaced)"
    )

    # ── Confirmation gate (first, before any network call) ────────────────────
    try:
        validate_cancel_confirmation(args.confirm_cancel)
    except ValueError as exc:
        print(f"[cancel_paper_order] BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(f"  confirm_cancel='{args.confirm_cancel}' — gate passed")

    # ── Must have at least one order identifier ───────────────────────────────
    if not args.client_order_id and not args.broker_order_id:
        print(
            "[cancel_paper_order] ERROR: provide --client-order-id or --broker-order-id",
            file=sys.stderr,
        )
        return 1

    # ── Env gates ────────────────────────────────────────────────────────────
    if not args.dry_run:
        try:
            _check_env_gates()
        except RuntimeError as exc:
            print(f"[cancel_paper_order] FATAL: {exc}", file=sys.stderr)
            return 1

    # ── Fetch / look up the order ─────────────────────────────────────────────
    raw_order: dict | None = None
    broker_order_id_resolved: str = args.broker_order_id or ""

    if args.dry_run:
        raw_order = _find_order_in_snapshot(args.client_order_id, args.broker_order_id)
        if raw_order is None:
            print(
                f"[cancel_paper_order] dry_run: order not found in snapshot  "
                f"client_order_id={args.client_order_id!r}  "
                f"broker_order_id={args.broker_order_id!r}",
                file=sys.stderr,
            )
            return 1
        broker_order_id_resolved = str(
            raw_order.get("id") or raw_order.get("order_id") or broker_order_id_resolved
        )
        print(f"  dry_run: found order in snapshot  symbol={raw_order.get('symbol')}  "
              f"status={raw_order.get('status')}")
    else:
        try:
            client = AlpacaPaperClient()
        except RuntimeError as exc:
            print(f"[cancel_paper_order] FATAL broker gate: {exc}", file=sys.stderr)
            return 1

        try:
            tc = client.trading_client()
            if args.client_order_id:
                fetched = tc.get_order_by_client_id(args.client_order_id)
            else:
                fetched = tc.get_order_by_id(args.broker_order_id)
            raw_order = _to_primitive(fetched)
        except Exception as exc:
            print(
                f"[cancel_paper_order] ERROR fetching order: {exc}",
                file=sys.stderr,
            )
            return 1

        broker_order_id_resolved = str(
            raw_order.get("id") or raw_order.get("order_id") or broker_order_id_resolved
        )
        print(f"  fetched order  symbol={raw_order.get('symbol')}  "
              f"status={raw_order.get('status')}  "
              f"broker_order_id={broker_order_id_resolved}")

    # ── Validate order is cancellable ─────────────────────────────────────────
    try:
        validate_order_cancellable(raw_order)
    except ValueError as exc:
        print(f"[cancel_paper_order] BLOCKED (validation): {exc}", file=sys.stderr)
        return 1

    # ── Validate IDs match the fetched order ──────────────────────────────────
    try:
        validate_order_id_match(
            raw_order,
            client_order_id=args.client_order_id,
            broker_order_id=args.broker_order_id,
        )
    except ValueError as exc:
        print(f"[cancel_paper_order] BLOCKED (ID mismatch): {exc}", file=sys.stderr)
        return 1

    print(f"  order validation passed  symbol={raw_order.get('symbol')}  "
          f"status={raw_order.get('status')}  "
          f"client_order_id={raw_order.get('client_order_id')}")

    # ── Issue cancel (or simulate in dry-run) ─────────────────────────────────
    cancelled_at = utc_now_iso()
    broker_response: object

    if args.dry_run:
        broker_response = {
            "dry_run": True,
            "message": "No broker API call made — dry_run=True",
            "broker_order_id": broker_order_id_resolved,
        }
        print(
            f"  dry_run: cancel NOT sent to broker  "
            f"broker_order_id={broker_order_id_resolved}"
        )
    else:
        if not broker_order_id_resolved:
            print(
                "[cancel_paper_order] ERROR: could not resolve broker_order_id from fetched order",
                file=sys.stderr,
            )
            return 1
        try:
            tc = client.trading_client()  # type: ignore[union-attr]
            result = tc.cancel_order_by_id(broker_order_id_resolved)
            broker_response = result if result is not None else {"status": "cancel_accepted"}
            print(
                f"  cancel submitted to Alpaca paper  "
                f"broker_order_id={broker_order_id_resolved}  "
                f"symbol={raw_order.get('symbol')}"
            )
        except Exception as exc:
            print(
                f"[cancel_paper_order] ERROR cancelling order: {exc}",
                file=sys.stderr,
            )
            return 1

    # ── Build audit record ────────────────────────────────────────────────────
    record = build_cancellation_record(
        order=raw_order,
        broker_response=broker_response,
        cancelled_at=cancelled_at,
        confirmed_by=f"operator (confirm_cancel='{CANCEL_CONFIRMATION_TOKEN}')",
        notes=args.notes,
        source="dry_run_snapshot" if args.dry_run else "alpaca_paper",
    )

    # ── Write outputs ─────────────────────────────────────────────────────────
    audit_path = _ORDERS_DIR / f"{record['run_id']}.json"
    _write_json(audit_path, record)
    _append_trade_log(record)
    _append_resolution_log(record)

    # ── Print summary ─────────────────────────────────────────────────────────
    print()
    print(f"[cancel_paper_order] run_id={record['run_id']}")
    print(f"[cancel_paper_order] symbol={record['symbol']}  "
          f"side={record['side']}  "
          f"status_before={record['status_before_cancel']}")
    print(f"[cancel_paper_order] client_order_id={record['client_order_id']}")
    print(f"[cancel_paper_order] broker_order_id={record['broker_order_id']}")
    if args.dry_run:
        print("[cancel_paper_order] dry_run=True — broker cancel was NOT sent")
    else:
        print("[cancel_paper_order] cancel submitted to Alpaca paper broker")
    print("[cancel_paper_order] production_order_cancel_allowed=False — live trading unreachable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
