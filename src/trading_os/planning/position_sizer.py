"""Convert target allocations into proposed orders.

Pure function — no I/O. Computes the delta between target portfolio weights and
current positions. Returns ALL computed orders; the caller decides which are
actionable vs blocked (skip_reason is None ↔ actionable).

Rules enforced here:
- Never short (would_short detection).
- Skip orders below min_order_notional.
- Emit sell orders for positions not in targets (full exits).
- Limit orders use the latest_close from the target record as limit price;
  if no price is available the order_type falls back to "market".
"""
from __future__ import annotations

from typing import Any, Optional


def _position_value(positions: list, symbol: str) -> float:
    """Return the current market value of a held position (0.0 if none)."""
    for pos in positions:
        if pos.get("symbol") == symbol:
            try:
                return float(pos.get("market_value") or 0)
            except (TypeError, ValueError):
                return 0.0
    return 0.0


def compute_proposed_orders(
    targets: dict,
    equity: float,
    positions: list,
    min_order_notional: float = 25.0,
) -> list:
    """Compute proposed orders from target allocations and current positions.

    Args:
        targets:             {symbol: {weight, notional, reason, latest_close, ...}}
        equity:              total portfolio equity
        positions:           current position list from account/positions snapshot
        min_order_notional:  minimum absolute dollar change to bother ordering

    Returns:
        List of order dicts, each with:
            symbol, side, order_type, limit_price, notional, target_weight,
            current_value, target_value, delta_value, would_short, skip_reason
    """
    orders: list = []
    processed: set = set()

    # ── Orders to reach targets ──────────────────────────────────────────────
    for sym, tgt in targets.items():
        processed.add(sym)
        target_weight: float = float(tgt["weight"])
        target_value: float = float(tgt["notional"])
        current_value: float = _position_value(positions, sym)
        delta: float = target_value - current_value
        limit_price: Optional[float] = tgt.get("latest_close")

        side = "buy" if delta >= 0 else "sell"
        notional = abs(delta)
        would_short = (side == "sell") and (current_value <= 0.0)

        skip_reason: Any = None
        if would_short:
            skip_reason = "would_short_no_position"
        elif notional < min_order_notional:
            skip_reason = f"below_min_notional({notional:.2f}<{min_order_notional})"

        orders.append({
            "symbol": sym,
            "side": side,
            "order_type": "limit" if limit_price is not None else "market",
            "limit_price": limit_price,
            "notional": round(notional, 2),
            "target_weight": round(target_weight, 8),
            "current_value": round(current_value, 2),
            "target_value": round(target_value, 2),
            "delta_value": round(delta, 2),
            "would_short": would_short,
            "skip_reason": skip_reason,
        })

    # ── Full exits for positions not in targets ──────────────────────────────
    for pos in positions:
        sym = pos.get("symbol", "")
        if not sym or sym in processed:
            continue
        current_value = _position_value(positions, sym)
        if current_value <= 0:
            continue
        delta = -current_value
        orders.append({
            "symbol": sym,
            "side": "sell",
            "order_type": "market",
            "limit_price": None,
            "notional": round(current_value, 2),
            "target_weight": 0.0,
            "current_value": round(current_value, 2),
            "target_value": 0.0,
            "delta_value": round(delta, 2),
            "would_short": False,
            "skip_reason": None,
        })

    return orders
