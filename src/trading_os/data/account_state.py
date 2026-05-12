"""Fetch account state from Alpaca paper: account, positions, open orders, market clock."""
from __future__ import annotations

from typing import Any

from ..hashing import stable_hash
from ..time_utils import utc_now_iso
from .alpaca_client import AlpacaPaperClient, _to_primitive


def fetch_account_state(client: AlpacaPaperClient) -> dict:
    """Fetch account, positions, open orders, and market clock in one pass.

    Returns a dict with keys:
        schema_version, source, fetched_at,
        account, positions, orders, clock,
        position_count, open_order_count, data_hash
    """
    from alpaca.trading.requests import GetOrdersRequest

    fetched_at = utc_now_iso()
    trading = client.trading_client()

    account = _to_primitive(trading.get_account())
    positions_raw = _to_primitive(trading.get_all_positions())
    orders_raw = _to_primitive(
        trading.get_orders(filter=GetOrdersRequest(status="open"))
    )
    clock = _to_primitive(trading.get_clock())

    positions: list = positions_raw if isinstance(positions_raw, list) else []
    orders: list = orders_raw if isinstance(orders_raw, list) else []

    payload: dict[str, Any] = {
        "schema_version": "0.1.0",
        "source": "alpaca_paper",
        "fetched_at": fetched_at,
        "account": account,
        "positions": positions,
        "orders": orders,
        "clock": clock,
        "position_count": len(positions),
        "open_order_count": len(orders),
        "source_labels": {
            "account": "alpaca_trading_client.get_account",
            "positions": "alpaca_trading_client.get_all_positions",
            "orders": "alpaca_trading_client.get_orders(open)",
            "clock": "alpaca_trading_client.get_clock",
        },
    }
    payload["data_hash"] = stable_hash(
        {k: v for k, v in payload.items() if k != "data_hash"}
    )
    return payload
