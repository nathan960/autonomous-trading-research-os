"""Build execution-ready order representations from trade plan proposed_orders.

No order submission happens here — this is Phase 5 (dry-run only).
The output is a validated, enriched order dict suitable for logging and
for passing to a real executor in Phase 6.

Each returned order has:
    symbol              str
    side                "buy" | "sell"
    order_type          "limit" | "market"
    limit_price         float | None
    notional            float
    target_weight       float
    client_order_id     str
    execution_ready     bool   True if all validations pass
    validation_skip_reason  str | None
"""
from __future__ import annotations

from typing import Any, Optional

from ..tick_rounding import round_to_tick


def _apply_tick(price: Optional[float], side: str) -> Optional[float]:
    if price is None:
        return None
    try:
        v = float(price)
    except (TypeError, ValueError):
        return None
    if v <= 0:
        return None
    return float(round_to_tick(v, side))


def _client_order_id(plan_id: str, symbol: str, side: str) -> str:
    """Build a deterministic client order ID."""
    # plan_id format: "trade_plan-YYYYMMDDTHHMMSS-xxxxxxxx"
    parts = plan_id.split("-")
    ts_part = parts[1] if len(parts) > 1 else "000000"
    return f"TOS-{ts_part}-{symbol}-{side.upper()}"


def build_execution_order(
    proposed: dict,
    plan_id: str,
    universe_symbols: set,
    fallback_symbols: set,
    max_spread_pct: float,
    spreads: dict,
    min_order_notional: float,
) -> dict:
    """Enrich a single proposed order with execution metadata and validation.

    Args:
        proposed:           one proposed_order dict from trade_plan
        plan_id:            trade_plan plan_id for client_order_id generation
        universe_symbols:   set of allowed equity symbols
        fallback_symbols:   set of allowed fallback symbols (BIL, SPY, etc.)
        max_spread_pct:     maximum allowed bid-ask spread
        spreads:            spreads dict from market_snapshot
        min_order_notional: minimum order dollar amount

    Returns:
        Enriched execution order dict (never submitted).
    """
    symbol: str = proposed.get("symbol", "")
    side: str = proposed.get("side", "buy")
    order_type: str = proposed.get("order_type", "limit")
    limit_price: Optional[float] = _apply_tick(proposed.get("limit_price"), side)
    notional: float = float(proposed.get("notional", 0))
    target_weight: float = float(proposed.get("target_weight", 0))
    would_short: bool = bool(proposed.get("would_short", False))

    skip_reason: Optional[str] = proposed.get("skip_reason")

    # Additional execution-time validation
    allowed = universe_symbols | fallback_symbols
    if skip_reason is None and symbol not in allowed:
        skip_reason = f"symbol_not_in_universe_or_fallbacks({symbol})"
    if skip_reason is None and would_short:
        skip_reason = f"would_short_detected({symbol})"
    if skip_reason is None and notional < min_order_notional:
        skip_reason = f"below_min_notional({notional:.2f}<{min_order_notional})"

    sp_info = spreads.get(symbol, {})
    spread_pct: Optional[float] = sp_info.get("spread_pct")
    if skip_reason is None and spread_pct is not None and spread_pct > max_spread_pct:
        skip_reason = f"spread_too_wide({spread_pct:.4f}>{max_spread_pct})"

    execution_ready = skip_reason is None

    return {
        "symbol": symbol,
        "side": side,
        "order_type": order_type,
        "limit_price": limit_price,
        "notional": notional,
        "target_weight": target_weight,
        "client_order_id": _client_order_id(plan_id, symbol, side),
        "execution_ready": execution_ready,
        "validation_skip_reason": skip_reason,
    }


def build_execution_orders(
    trade_plan: dict,
    universe: dict,
    risk_limits: dict,
    strategy: dict,
    market_snapshot: dict,
) -> list:
    """Build execution-ready order list from a trade plan.

    Returns ALL proposed orders (including skipped ones) with execution metadata.
    Only orders where execution_ready=True would be submitted in a live run.
    """
    plan_id: str = trade_plan.get("plan_id", "")
    proposed_orders: list = trade_plan.get("proposed_orders", [])

    universe_symbols: set = set(universe.get("symbols", []))
    fallback_symbols: set = set(risk_limits.get("allowed_fallbacks") or [])
    fb = strategy.get("fallbacks", {})
    fallback_symbols |= {
        fb.get("risk_off_target", {}).get("symbol", "BIL"),
        fb.get("risk_on_no_candidates_target", {}).get("symbol", "SPY"),
    }

    max_spread_pct: float = float(
        strategy.get("parameters", {}).get("max_quote_spread_pct")
        or risk_limits.get("max_quote_spread_pct", 0.02)
    )
    min_order_notional: float = float(
        strategy.get("parameters", {}).get("min_order_notional")
        or risk_limits.get("min_order_notional", 25.0)
    )
    spreads: dict = market_snapshot.get("spreads", {})

    return [
        build_execution_order(
            proposed=o,
            plan_id=plan_id,
            universe_symbols=universe_symbols,
            fallback_symbols=fallback_symbols,
            max_spread_pct=max_spread_pct,
            spreads=spreads,
            min_order_notional=min_order_notional,
        )
        for o in proposed_orders
    ]
