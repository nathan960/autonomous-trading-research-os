"""Tests for src/trading_os/signals/regime.py"""
from __future__ import annotations

import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trading_os.signals.regime import (
    compute_spy_signals,
    evaluate_breadth,
    evaluate_regime,
)

_BASE_DATE = date(2018, 1, 2)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_bars(closes: list, base_high_offset: float = 1.0) -> list:
    """Build minimal bar dicts for testing."""
    bars = []
    for i, c in enumerate(closes):
        d = _BASE_DATE + timedelta(days=i)
        bars.append({
            "timestamp": f"{d.isoformat()}T00:00:00Z",
            "close": c,
            "high": c + base_high_offset,
            "low": c - base_high_offset,
            "open": c,
            "volume": 1_000_000,
        })
    return bars


def _make_uptrend_bars(n: int = 260, start: float = 100.0) -> list:
    """Rising price series — will be above 200-DMA and have positive ROC."""
    return _make_bars([start + i * 0.5 for i in range(n)])


def _make_downtrend_bars(n: int = 260, start: float = 200.0) -> list:
    """Falling price series — will be below 200-DMA."""
    return _make_bars([start - i * 0.5 for i in range(n)])


def _make_trend_result(is_ready: bool, passes: bool) -> dict:
    return {"is_ready": is_ready, "passes": passes}


# ---------------------------------------------------------------------------
# compute_spy_signals
# ---------------------------------------------------------------------------

class TestComputeSpySignals:
    def test_uptrend_is_ready_and_passes(self):
        bars = _make_uptrend_bars(260)
        r = compute_spy_signals(bars)
        assert r["symbol"] == "SPY"
        assert r["is_ready"] is True
        assert r["passes_200dma"] is True
        assert r["passes_6m_momentum"] is True

    def test_downtrend_fails_200dma(self):
        bars = _make_downtrend_bars(260)
        r = compute_spy_signals(bars)
        assert r["is_ready"] is True
        assert r["passes_200dma"] is False

    def test_insufficient_bars_not_ready(self):
        bars = _make_bars([100.0] * 50)
        r = compute_spy_signals(bars)
        assert r["is_ready"] is False
        assert r["passes_200dma"] is False
        assert r["passes_6m_momentum"] is False

    def test_empty_bars_not_ready(self):
        r = compute_spy_signals([])
        assert r["is_ready"] is False
        assert r["latest_close"] is None
        assert r["sma"] is None
        assert r["roc"] is None

    def test_bar_count_returned(self):
        bars = _make_uptrend_bars(260)
        r = compute_spy_signals(bars)
        assert r["bar_count"] == 260

    def test_custom_periods(self):
        bars = _make_uptrend_bars(300)
        r = compute_spy_signals(bars, sma_period=50, roc_period=20)
        assert r["sma_period"] == 50
        assert r["roc_period"] == 20
        assert r["is_ready"] is True

    def test_flat_price_negative_6m_momentum_false(self):
        """Flat price → ROC ≈ 0.0; with > 0 requirement, passes_6m_momentum=False."""
        bars = _make_bars([100.0] * 260)
        r = compute_spy_signals(bars)
        # ROC of flat series is 0.0 — not > 0
        assert r["passes_6m_momentum"] is False

    def test_latest_close_and_sma_populated(self):
        bars = _make_uptrend_bars(260)
        r = compute_spy_signals(bars)
        assert r["latest_close"] is not None
        assert r["sma"] is not None
        assert r["latest_close"] > r["sma"]  # uptrend


# ---------------------------------------------------------------------------
# evaluate_breadth
# ---------------------------------------------------------------------------

class TestEvaluateBreadth:
    def test_all_above_breadth_ok(self):
        results = [_make_trend_result(True, True)] * 10
        r = evaluate_breadth(results, breadth_threshold=0.55)
        assert r["breadth"] == 1.0
        assert r["breadth_ok"] is True
        assert r["ready_count"] == 10
        assert r["above_200dma_count"] == 10

    def test_none_above_breadth_fail(self):
        results = [_make_trend_result(True, False)] * 10
        r = evaluate_breadth(results, breadth_threshold=0.55)
        assert r["breadth"] == 0.0
        assert r["breadth_ok"] is False

    def test_exactly_at_threshold_passes(self):
        above = [_make_trend_result(True, True)] * 55
        below = [_make_trend_result(True, False)] * 45
        r = evaluate_breadth(above + below, breadth_threshold=0.55)
        assert abs(r["breadth"] - 0.55) < 1e-9
        assert r["breadth_ok"] is True

    def test_not_ready_symbols_excluded(self):
        ready_above = [_make_trend_result(True, True)] * 6
        not_ready = [_make_trend_result(False, False)] * 4
        r = evaluate_breadth(ready_above + not_ready, breadth_threshold=0.55)
        assert r["ready_count"] == 6
        assert r["above_200dma_count"] == 6

    def test_empty_list_zero_breadth(self):
        r = evaluate_breadth([], breadth_threshold=0.55)
        assert r["breadth"] == 0.0
        assert r["breadth_ok"] is False
        assert r["ready_count"] == 0

    def test_all_not_ready_zero_breadth(self):
        results = [_make_trend_result(False, True)] * 10
        r = evaluate_breadth(results, breadth_threshold=0.55)
        assert r["ready_count"] == 0
        assert r["breadth"] == 0.0


# ---------------------------------------------------------------------------
# evaluate_regime
# ---------------------------------------------------------------------------

class TestEvaluateRegime:
    def _ready_spy(self, passes_200dma: bool = True, passes_6m: bool = True) -> dict:
        return {
            "is_ready": True,
            "passes_200dma": passes_200dma,
            "passes_6m_momentum": passes_6m,
        }

    def _breadth(self, ok: bool = True) -> dict:
        return {"breadth": 0.60 if ok else 0.40, "breadth_threshold": 0.55, "breadth_ok": ok}

    def test_all_conditions_risk_on(self):
        r = evaluate_regime(self._ready_spy(), self._breadth(), input_hash="abc")
        assert r["risk_on"] is True
        assert r["passed"] is True
        assert r["skip_reason"] is None
        assert r["input_hash"] == "abc"

    def test_spy_not_ready_risk_off(self):
        spy = {"is_ready": False, "passes_200dma": False, "passes_6m_momentum": False}
        r = evaluate_regime(spy, self._breadth())
        assert r["risk_on"] is False
        assert r["skip_reason"] == "spy_indicators_not_ready"

    def test_spy_below_200dma_risk_off(self):
        r = evaluate_regime(self._ready_spy(passes_200dma=False), self._breadth())
        assert r["risk_on"] is False
        assert r["skip_reason"] == "spy_below_200dma"

    def test_spy_negative_momentum_risk_off(self):
        r = evaluate_regime(self._ready_spy(passes_6m=False), self._breadth())
        assert r["risk_on"] is False
        assert r["skip_reason"] == "spy_negative_6m_momentum"

    def test_breadth_below_threshold_risk_off(self):
        r = evaluate_regime(self._ready_spy(), self._breadth(ok=False))
        assert r["risk_on"] is False
        assert "breadth_below_threshold" in r["skip_reason"]

    def test_trigger_id_correct(self):
        r = evaluate_regime(self._ready_spy(), self._breadth())
        assert r["trigger_id"] == "SPY_REGIME_200DMA_V1"

    def test_spy_signals_and_breadth_embedded(self):
        spy = self._ready_spy()
        breadth = self._breadth()
        r = evaluate_regime(spy, breadth)
        assert r["spy_signals"] is spy
        assert r["breadth"] is breadth
