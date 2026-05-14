"""Open-order resolution: list and single-order cancellation for paper orders.

Pure functions only — no I/O, no network calls, no secrets.
Scripts (list_open_orders.py, cancel_paper_order.py) own all I/O.

Safety contracts enforced here:
- cancel confirmation must be the exact string "CANCEL" — any other value raises.
- Only statuses in CANCELLABLE_STATUSES may be cancelled; filled/expired/etc. raise.
- production_order_cancel_allowed is always False in all returned dicts.
- No order placement, replacement, or live-trading path exists.
"""
from __future__ import annotations

from typing import Any, Optional

from ..hashing import stable_hash
from ..time_utils import utc_now_iso

# Exact confirmation token required to proceed with cancellation.
CANCEL_CONFIRMATION_TOKEN = "CANCEL"

# Alpaca order statuses from which a cancel can be requested.
CANCELLABLE_STATUSES: frozenset = frozenset({
    "new",
    "accepted",
    "pending_new",
    "accepted_for_bidding",
    "held",
    "partially_filled",
})

# Statuses that are already terminal — cancellation is impossible.
TERMINAL_STATUSES: frozenset = frozenset({
    "filled",
    "canceled",
    "expired",
    "replaced",
    "done_for_day",
    "rejected",
    "stopped",
    "suspended",
    "calculated",
})


# ---------------------------------------------------------------------------
# Confirmation gate
# ---------------------------------------------------------------------------

def validate_cancel_confirmation(confirm_cancel: str) -> None:
    """Raise ValueError unless confirm_cancel is exactly 'CANCEL'.

    This is the primary human-gate for cancellation. The workflow and the
    script both call this independently (defense in depth).
    """
    if confirm_cancel != CANCEL_CONFIRMATION_TOKEN:
        raise ValueError(
            f"Cancellation refused: confirmation must be exactly "
            f"'{CANCEL_CONFIRMATION_TOKEN}' (got {confirm_cancel!r}). "
            "No order was cancelled."
        )


# ---------------------------------------------------------------------------
# Order validation
# ---------------------------------------------------------------------------

def validate_order_cancellable(order: dict) -> None:
    """Raise ValueError if the order cannot be cancelled.

    Checks:
    - order is a non-empty dict
    - status is in CANCELLABLE_STATUSES
    - side is 'buy' (this system is long-only; a 'sell' order would be unexpected)
    """
    if not isinstance(order, dict) or not order:
        raise ValueError("Order dict is empty or not a dict.")

    status = str(order.get("status", "")).lower()
    if not status:
        raise ValueError("Order has no status field — cannot validate cancellability.")

    if status in TERMINAL_STATUSES:
        raise ValueError(
            f"Order is already in terminal status '{status}' — cannot cancel. "
            f"client_order_id={order.get('client_order_id')!r}"
        )

    if status not in CANCELLABLE_STATUSES:
        raise ValueError(
            f"Order status '{status}' is not in the known cancellable set "
            f"{sorted(CANCELLABLE_STATUSES)}. Failing closed."
        )

    side = str(order.get("side", "")).lower()
    if side and side != "buy":
        raise ValueError(
            f"Unexpected order side '{side}' — this system is long-only. "
            "Will not cancel a non-buy order without manual review."
        )


def validate_order_id_match(
    order: dict,
    client_order_id: Optional[str],
    broker_order_id: Optional[str],
) -> None:
    """Raise ValueError if the fetched order does not match the provided IDs.

    When both IDs are provided they must both match the fetched order.
    """
    if client_order_id:
        actual_cid = str(order.get("client_order_id", ""))
        if actual_cid != client_order_id:
            raise ValueError(
                f"Fetched order client_order_id {actual_cid!r} does not match "
                f"requested {client_order_id!r}. Failing closed."
            )

    if broker_order_id:
        actual_bid = str(order.get("id", order.get("order_id", "")))
        if actual_bid != broker_order_id:
            raise ValueError(
                f"Fetched order broker_order_id {actual_bid!r} does not match "
                f"requested {broker_order_id!r}. Failing closed."
            )


# ---------------------------------------------------------------------------
# Record builders
# ---------------------------------------------------------------------------

def _run_id(prefix: str) -> str:
    ts = utc_now_iso().replace(":", "").replace("-", "").replace("Z", "")[:15]
    h = stable_hash({"ts": utc_now_iso(), "prefix": prefix})[:8]
    return f"{prefix}-{ts}-{h}"


def build_order_list_record(
    orders: list,
    run_id: str,
    fetched_at: str,
    source: str = "alpaca_paper",
) -> dict:
    """Build a JSON-serialisable order list audit record."""
    sanitised = []
    for o in orders:
        if not isinstance(o, dict):
            continue
        sanitised.append({
            "symbol": o.get("symbol"),
            "side": o.get("side"),
            "status": o.get("status"),
            "order_type": o.get("order_type") or o.get("type"),
            "notional": o.get("notional"),
            "qty": o.get("qty"),
            "limit_price": o.get("limit_price"),
            "client_order_id": o.get("client_order_id"),
            "broker_order_id": str(o.get("id") or o.get("order_id") or ""),
            "submitted_at": o.get("submitted_at"),
            "expires_at": o.get("expires_at"),
        })
    return {
        "run_id": run_id,
        "generated_at": fetched_at,
        "source": source,
        "action": "list_open_orders",
        "open_order_count": len(sanitised),
        "orders": sanitised,
        "production_order_cancel_allowed": False,
    }


def build_cancellation_record(
    order: dict,
    broker_response: Any,
    cancelled_at: str,
    confirmed_by: str,
    notes: str = "",
    source: str = "alpaca_paper",
) -> dict:
    """Build a JSON-serialisable cancellation audit record.

    production_order_cancel_allowed is always False — this record documents
    a paper cancellation, not a live one.
    """
    broker_resp_primitive: Any
    if hasattr(broker_response, "model_dump"):
        broker_resp_primitive = broker_response.model_dump()
    elif hasattr(broker_response, "dict"):
        broker_resp_primitive = broker_response.dict()
    elif isinstance(broker_response, dict):
        broker_resp_primitive = broker_response
    else:
        broker_resp_primitive = str(broker_response)

    return {
        "run_id": _run_id("order_cancel"),
        "generated_at": cancelled_at,
        "source": source,
        "action": "cancel_paper_order",
        "symbol": order.get("symbol"),
        "side": order.get("side"),
        "status_before_cancel": order.get("status"),
        "client_order_id": order.get("client_order_id"),
        "broker_order_id": str(order.get("id") or order.get("order_id") or ""),
        "notional": order.get("notional"),
        "limit_price": order.get("limit_price"),
        "submitted_at": order.get("submitted_at"),
        "cancelled_at": cancelled_at,
        "confirmed_by": confirmed_by,
        "notes": notes,
        "broker_response": broker_resp_primitive,
        "production_order_cancel_allowed": False,
    }


def format_cancellation_markdown(record: dict) -> str:
    """Format a cancellation record as a TRADE-LOG.md section."""
    lines = [
        "",
        "## order_cancel",
        "",
        f"**run_id:** `{record.get('run_id')}`  ",
        f"**cancelled_at:** {record.get('cancelled_at')}  ",
        f"**symbol:** {record.get('symbol')}  ",
        f"**side:** {record.get('side')}  ",
        f"**status_before_cancel:** {record.get('status_before_cancel')}  ",
        f"**client_order_id:** `{record.get('client_order_id')}`  ",
        f"**broker_order_id:** `{record.get('broker_order_id')}`  ",
        f"**confirmed_by:** {record.get('confirmed_by')}  ",
        f"**notes:** {record.get('notes') or '—'}  ",
        "",
    ]
    return "\n".join(lines) + "\n"


def format_order_list_markdown(record: dict) -> str:
    """Format an order list record as a brief markdown entry."""
    orders = record.get("orders", [])
    lines = [
        "",
        "## order_list",
        "",
        f"**run_id:** `{record.get('run_id')}`  ",
        f"**generated_at:** {record.get('generated_at')}  ",
        f"**open_order_count:** {record.get('open_order_count')}  ",
        "",
    ]
    for o in orders:
        lines.append(
            f"- `{o.get('client_order_id')}` "
            f"{o.get('symbol')} {o.get('side')} "
            f"status={o.get('status')} "
            f"notional={o.get('notional')}"
        )
    if not orders:
        lines.append("_(no open orders)_")
    lines.append("")
    return "\n".join(lines) + "\n"
