"""SPY regime assessment: 200DMA trend, 6-month momentum, and market breadth.

Trigger: SPY_REGIME_200DMA_V1

The regime is risk_on when ALL three sub-conditions hold:
  1. SPY latest close > SPY 200-day SMA
  2. SPY 126-day ROC (6-month momentum) > 0
  3. Breadth (fraction of universe stocks above their 200-day SMA) >= threshold
"""
from __future__ import annotations

from typing import Any

from ..hashing import stable_hash
from ._indicators import closes, roc, sma, sorted_bars

TRIGGER_ID = "SPY_REGIME_200DMA_V1"


def compute_spy_signals(
    spy_bars: list,
    sma_period: int = 200,
    roc_period: int = 126,
) -> dict:
    """Compute SPY-specific indicator values needed for regime assessment."""
    ordered = sorted_bars(spy_bars)
    close_series = closes(ordered)
    bar_count = len(ordered)
    latest_close: Any = close_series[-1] if close_series else None
    sma_val = sma(close_series, sma_period)
    roc_val = roc(close_series, roc_period)

    is_ready = latest_close is not None and sma_val is not None and roc_val is not None
    passes_200dma = bool(is_ready and latest_close > sma_val)
    passes_6m_momentum = bool(is_ready and roc_val > 0.0)

    return {
        "symbol": "SPY",
        "bar_count": bar_count,
        "is_ready": is_ready,
        "latest_close": latest_close,
        "sma_period": sma_period,
        "sma": sma_val,
        "passes_200dma": passes_200dma,
        "roc_period": roc_period,
        "roc": roc_val,
        "passes_6m_momentum": passes_6m_momentum,
    }


def evaluate_breadth(
    trend_results: list,
    breadth_threshold: float = 0.55,
) -> dict:
    """Compute market breadth from per-symbol trend results.

    trend_results: list of dicts, each with 'is_ready' and 'passes' keys.
    """
    ready = [r for r in trend_results if r.get("is_ready")]
    above = [r for r in ready if r.get("passes")]
    ready_count = len(ready)
    above_count = len(above)
    breadth = above_count / ready_count if ready_count else 0.0
    return {
        "ready_count": ready_count,
        "above_200dma_count": above_count,
        "breadth": breadth,
        "breadth_threshold": breadth_threshold,
        "breadth_ok": breadth >= breadth_threshold,
    }


def evaluate_regime(
    spy_signals: dict,
    breadth_result: dict,
    input_hash: str = "",
) -> dict:
    """Combine SPY signals and breadth into the regime trigger result."""
    spy_ready = spy_signals.get("is_ready", False)
    passes_200dma = spy_signals.get("passes_200dma", False)
    passes_6m = spy_signals.get("passes_6m_momentum", False)
    breadth_ok = breadth_result.get("breadth_ok", False)

    risk_on = bool(spy_ready and passes_200dma and passes_6m and breadth_ok)

    skip_reason: Any = None
    if not spy_ready:
        skip_reason = "spy_indicators_not_ready"
    elif not passes_200dma:
        skip_reason = "spy_below_200dma"
    elif not passes_6m:
        skip_reason = "spy_negative_6m_momentum"
    elif not breadth_ok:
        skip_reason = f"breadth_below_threshold({breadth_result.get('breadth', 0.0):.3f}<{breadth_result.get('breadth_threshold', 0.55)})"

    return {
        "trigger_id": TRIGGER_ID,
        "passed": risk_on,
        "risk_on": risk_on,
        "skip_reason": skip_reason,
        "spy_signals": spy_signals,
        "breadth": breadth_result,
        "input_hash": input_hash,
    }
