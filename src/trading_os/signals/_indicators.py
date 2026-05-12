"""Private indicator math shared across signal modules.

All functions are pure (no I/O, no side effects) and operate on plain Python lists.
"""
from __future__ import annotations

from typing import Any, Optional


def sorted_bars(bars: list) -> list:
    """Return bars sorted ascending by timestamp/t/date field."""
    return sorted(
        bars,
        key=lambda b: str(b.get("timestamp") or b.get("t") or b.get("date") or ""),
    )


def closes(bars: list) -> list:
    """Extract close prices from sorted bars."""
    out: list = []
    for b in bars:
        c = b.get("close") or b.get("c")
        try:
            out.append(float(c))
        except (TypeError, ValueError):
            pass
    return out


def volumes(bars: list) -> list:
    """Extract volumes from sorted bars (skips zero/None)."""
    out: list = []
    for b in bars:
        v = b.get("volume") or b.get("v")
        try:
            fv = float(v)
            if fv > 0:
                out.append(fv)
        except (TypeError, ValueError):
            pass
    return out


def sma(values: list, period: int) -> Optional[float]:
    """Simple moving average over the last `period` values."""
    if period <= 0 or len(values) < period:
        return None
    window = values[-period:]
    return sum(window) / period


def roc(values: list, period: int) -> Optional[float]:
    """Rate of change: (latest / base) - 1, where base is `period` bars back."""
    if period <= 0 or len(values) <= period:
        return None
    base = values[-(period + 1)]
    latest = values[-1]
    if base <= 0:
        return None
    return latest / base - 1.0


def true_ranges(bars: list) -> list:
    """True range for each bar (requires previous close for first gap)."""
    ordered = sorted_bars(bars)
    ranges: list = []
    prev_close: Optional[float] = None
    for bar in ordered:
        try:
            high = float(bar.get("high") or bar.get("h") or 0)
            low = float(bar.get("low") or bar.get("l") or 0)
            close = float(bar.get("close") or bar.get("c") or 0)
        except (TypeError, ValueError):
            continue
        if high <= 0 or low <= 0 or close <= 0:
            if close > 0:
                prev_close = close
            continue
        if prev_close is None:
            ranges.append(high - low)
        else:
            ranges.append(max(high - low, abs(high - prev_close), abs(low - prev_close)))
        prev_close = close
    return ranges


def wilder_atr(bars: list, period: int) -> Optional[float]:
    """ATR using Wilder's smoothing method."""
    trs = true_ranges(bars)
    if period <= 0 or len(trs) < period:
        return None
    atr = sum(trs[:period]) / period
    for tr in trs[period:]:
        atr = (atr * (period - 1) + tr) / period
    return atr


def avg_vol_n(bars: list, period: int) -> Optional[float]:
    """Average daily volume over the last `period` bars that have volume."""
    vols = volumes(bars)
    if not vols:
        return None
    window = vols[-period:] if period > 0 else vols
    return sum(window) / len(window) if window else None
