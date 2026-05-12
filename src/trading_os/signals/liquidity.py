"""Per-symbol average-volume liquidity gate.

Trigger: LIQUIDITY_GATE_V1

The gate only blocks if volume data is present AND average 20-day volume
falls below min_avg_volume. If bars contain no meaningful volume values,
the gate passes (cannot block on absent data).

The default min_avg_volume is 0, which means the gate is informational unless
a threshold is configured (future phases may add a param to strategy.json).
"""
from __future__ import annotations

from typing import Any, Optional

from ._indicators import avg_vol_n, sorted_bars, volumes

TRIGGER_ID = "LIQUIDITY_GATE_V1"
DEFAULT_PERIOD = 20


def compute_liquidity(
    symbol: str,
    bars: list,
    period: int = DEFAULT_PERIOD,
    min_avg_volume: float = 0.0,
    input_hash: str = "",
) -> dict:
    """Return liquidity-gate result for one symbol."""
    ordered = sorted_bars(bars)
    bar_count = len(ordered)
    all_vols = volumes(ordered)
    volume_present = len(all_vols) > 0
    avg_vol = avg_vol_n(ordered, period)

    if not volume_present:
        passes = True
        skip_reason: Any = None
    elif min_avg_volume <= 0:
        passes = True
        skip_reason = None
    else:
        passes = bool(avg_vol is not None and avg_vol >= min_avg_volume)
        skip_reason = (
            None
            if passes
            else f"avg_volume_below_min({avg_vol:.0f}<{min_avg_volume:.0f})"
        )

    return {
        "trigger_id": TRIGGER_ID,
        "symbol": symbol,
        "bar_count": bar_count,
        "volume_present": volume_present,
        "avg_volume_period": period,
        "avg_volume": avg_vol,
        "min_avg_volume": min_avg_volume,
        "passes": passes,
        "skip_reason": skip_reason,
        "input_hash": input_hash,
    }
