"""Per-symbol 200-day SMA trend filter.

Trigger: STOCK_TREND_200DMA_V1

Passes when:  latest_close > sma(close, sma_period)
Requires at least sma_period + 1 bars to be 'ready'.
"""
from __future__ import annotations

from typing import Any

from ._indicators import closes, sma, sorted_bars

TRIGGER_ID = "STOCK_TREND_200DMA_V1"


def compute_trend(
    symbol: str,
    bars: list,
    sma_period: int = 200,
    input_hash: str = "",
) -> dict:
    """Return trend-filter result for one symbol."""
    ordered = sorted_bars(bars)
    close_series = closes(ordered)
    bar_count = len(ordered)
    latest_close: Any = close_series[-1] if close_series else None
    sma_val = sma(close_series, sma_period)

    is_ready = latest_close is not None and sma_val is not None
    passes = bool(is_ready and latest_close > sma_val)

    skip_reason: Any = None
    if not is_ready:
        skip_reason = f"insufficient_bars_for_{sma_period}d_sma(have={bar_count})"
    elif not passes:
        skip_reason = f"close_below_{sma_period}dma"

    return {
        "trigger_id": TRIGGER_ID,
        "symbol": symbol,
        "bar_count": bar_count,
        "is_ready": is_ready,
        "latest_close": latest_close,
        "sma_period": sma_period,
        "sma": sma_val,
        "passes": passes,
        "skip_reason": skip_reason,
        "input_hash": input_hash,
    }
