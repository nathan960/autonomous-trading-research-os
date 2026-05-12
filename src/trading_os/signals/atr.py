"""Per-symbol ATR computation for position sizing.

Not a blocking trigger — ATR is used downstream by the trade-plan generator
to set inverse-ATR weights. Returns a result dict that gets attached to each
candidate so the sizing step has everything it needs in one place.
"""
from __future__ import annotations

from typing import Any, Optional

from ._indicators import closes, sorted_bars, wilder_atr

SIGNAL_ID = "ATR_SIZING_V1"


def compute_atr(
    symbol: str,
    bars: list,
    period: int = 20,
    input_hash: str = "",
) -> dict:
    """Return ATR signal for one symbol."""
    ordered = sorted_bars(bars)
    close_series = closes(ordered)
    bar_count = len(ordered)
    latest_close: Optional[float] = close_series[-1] if close_series else None
    atr_val = wilder_atr(ordered, period)

    is_ready = latest_close is not None and atr_val is not None and latest_close > 0
    atr_pct: Optional[float] = (
        atr_val / latest_close if is_ready and latest_close else None
    )

    return {
        "signal_id": SIGNAL_ID,
        "symbol": symbol,
        "bar_count": bar_count,
        "is_ready": is_ready,
        "atr_period": period,
        "atr": atr_val,
        "atr_pct": atr_pct,
        "latest_close": latest_close,
        "input_hash": input_hash,
    }
