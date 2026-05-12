"""Per-symbol momentum scoring: 0.5 * ROC-6M + 0.5 * ROC-12M.

Trigger: MOMENTUM_BLEND_6M_12M_V1

Passes when:
  - ROC-6M (126-day) > min_momentum_6m  (default 0.0)
  - ROC-12M (252-day) > min_momentum_12m (default 0.0)

Score = 0.5 * roc_6m + 0.5 * roc_12m (used for ranking candidates).
"""
from __future__ import annotations

from typing import Any, Optional

from ._indicators import closes, roc, sorted_bars

TRIGGER_ID = "MOMENTUM_BLEND_6M_12M_V1"


def compute_momentum(
    symbol: str,
    bars: list,
    roc_6m_period: int = 126,
    roc_12m_period: int = 252,
    min_momentum_6m: float = 0.0,
    min_momentum_12m: float = 0.0,
    input_hash: str = "",
) -> dict:
    """Return momentum-trigger result for one symbol."""
    ordered = sorted_bars(bars)
    close_series = closes(ordered)
    bar_count = len(ordered)

    roc_6m: Optional[float] = roc(close_series, roc_6m_period)
    roc_12m: Optional[float] = roc(close_series, roc_12m_period)

    is_ready = roc_6m is not None and roc_12m is not None
    momentum_score: Optional[float] = (
        0.5 * roc_6m + 0.5 * roc_12m if is_ready else None
    )

    passes_6m = bool(is_ready and roc_6m > min_momentum_6m)
    passes_12m = bool(is_ready and roc_12m > min_momentum_12m)
    passes = passes_6m and passes_12m

    skip_reason: Any = None
    if not is_ready:
        skip_reason = (
            f"insufficient_bars_for_{roc_12m_period}d_roc"
            f"(have={bar_count},need>{roc_12m_period})"
        )
    elif not passes_6m:
        skip_reason = f"roc_6m_below_min({roc_6m:.4f}<={min_momentum_6m})"
    elif not passes_12m:
        skip_reason = f"roc_12m_below_min({roc_12m:.4f}<={min_momentum_12m})"

    return {
        "trigger_id": TRIGGER_ID,
        "symbol": symbol,
        "bar_count": bar_count,
        "is_ready": is_ready,
        "roc_6m_period": roc_6m_period,
        "roc_12m_period": roc_12m_period,
        "roc_6m": roc_6m,
        "roc_12m": roc_12m,
        "momentum_score": momentum_score,
        "min_momentum_6m": min_momentum_6m,
        "min_momentum_12m": min_momentum_12m,
        "passes_6m": passes_6m,
        "passes_12m": passes_12m,
        "passes": passes,
        "skip_reason": skip_reason,
        "input_hash": input_hash,
    }
