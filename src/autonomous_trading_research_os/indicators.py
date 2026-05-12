from __future__ import annotations

from typing import Any, Iterable

from .file_io import safe_float


def _get(bar: dict[str, Any], *keys: str) -> float:
    for key in keys:
        if key in bar:
            return safe_float(bar[key])
    return 0.0


def sorted_bars(bars: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(list(bars), key=lambda bar: str(bar.get("timestamp") or bar.get("t") or bar.get("date") or ""))


def closes(bars: Iterable[dict[str, Any]]) -> list[float]:
    return [_get(bar, "close", "c") for bar in sorted_bars(bars)]


def sma(values: list[float], period: int) -> float | None:
    if len(values) < period or period <= 0:
        return None
    window = values[-period:]
    return sum(window) / period


def roc(values: list[float], period: int) -> float | None:
    if len(values) <= period or period <= 0:
        return None
    base = values[-period - 1]
    latest = values[-1]
    if base <= 0:
        return None
    return latest / base - 1.0


def true_ranges(bars: list[dict[str, Any]]) -> list[float]:
    ordered = sorted_bars(bars)
    ranges: list[float] = []
    previous_close: float | None = None
    for bar in ordered:
        high = _get(bar, "high", "h")
        low = _get(bar, "low", "l")
        close = _get(bar, "close", "c")
        if high <= 0 or low <= 0 or close <= 0:
            previous_close = close if close > 0 else previous_close
            continue
        if previous_close is None:
            ranges.append(high - low)
        else:
            ranges.append(max(high - low, abs(high - previous_close), abs(low - previous_close)))
        previous_close = close
    return ranges


def wilder_atr(bars: list[dict[str, Any]], period: int) -> float | None:
    trs = true_ranges(bars)
    if len(trs) < period or period <= 0:
        return None
    atr = sum(trs[:period]) / period
    for tr in trs[period:]:
        atr = ((atr * (period - 1)) + tr) / period
    return atr


def latest_indicator_snapshot(
    symbol: str,
    bars: list[dict[str, Any]],
    sma_period: int = 200,
    roc_6m_period: int = 126,
    roc_12m_period: int = 252,
    atr_period: int = 20,
) -> dict[str, Any]:
    ordered = sorted_bars(bars)
    close_values = closes(ordered)
    latest_close = close_values[-1] if close_values else None
    sma_value = sma(close_values, sma_period)
    roc_6m = roc(close_values, roc_6m_period)
    roc_12m = roc(close_values, roc_12m_period)
    atr_value = wilder_atr(ordered, atr_period)
    is_ready = latest_close is not None and sma_value is not None and roc_6m is not None and roc_12m is not None and atr_value is not None
    atr_pct = (atr_value / latest_close) if is_ready and latest_close and latest_close > 0 else None
    return {
        "symbol": symbol,
        "is_ready": is_ready,
        "bar_count": len(ordered),
        "latest_close": latest_close,
        "sma200": sma_value,
        "roc126": roc_6m,
        "roc252": roc_12m,
        "atr20": atr_value,
        "atr_pct": atr_pct,
        "passes_trend_filter": bool(is_ready and latest_close and sma_value and latest_close > sma_value),
        "momentum_score": (0.5 * roc_6m + 0.5 * roc_12m) if roc_6m is not None and roc_12m is not None else None,
    }
