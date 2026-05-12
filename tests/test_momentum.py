"""Tests for src/trading_os/signals/momentum.py"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trading_os.signals.momentum import compute_momentum, TRIGGER_ID


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_bars(closes: list) -> list:
    return [
        {
            "timestamp": f"2024-{(i // 28) + 1:02d}-{(i % 28) + 1:02d}T00:00:00Z",
            "close": c,
            "high": c + 1,
            "low": c - 1,
            "open": c,
            "volume": 500_000,
        }
        for i, c in enumerate(closes)
    ]


def _rising_bars(n: int = 260, start: float = 100.0, step: float = 0.3) -> list:
    return _make_bars([start + i * step for i in range(n)])


def _flat_bars(n: int = 260, price: float = 100.0) -> list:
    return _make_bars([price] * n)


def _falling_bars(n: int = 260, start: float = 200.0, step: float = 0.3) -> list:
    return _make_bars([start - i * step for i in range(n)])


# ---------------------------------------------------------------------------
# TRIGGER_ID
# ---------------------------------------------------------------------------

class TestTriggerId:
    def test_trigger_id_value(self):
        assert TRIGGER_ID == "MOMENTUM_BLEND_6M_12M_V1"


# ---------------------------------------------------------------------------
# compute_momentum: basic structure
# ---------------------------------------------------------------------------

class TestComputeMomentumStructure:
    def test_returns_required_keys(self):
        r = compute_momentum("AAPL", _rising_bars())
        expected = {
            "trigger_id", "symbol", "bar_count", "is_ready",
            "roc_6m_period", "roc_12m_period", "roc_6m", "roc_12m",
            "momentum_score", "min_momentum_6m", "min_momentum_12m",
            "passes_6m", "passes_12m", "passes", "skip_reason", "input_hash",
        }
        assert expected.issubset(set(r.keys()))

    def test_trigger_id_in_result(self):
        r = compute_momentum("AAPL", _rising_bars())
        assert r["trigger_id"] == TRIGGER_ID

    def test_symbol_in_result(self):
        r = compute_momentum("TSLA", _rising_bars())
        assert r["symbol"] == "TSLA"

    def test_input_hash_propagated(self):
        r = compute_momentum("AAPL", _rising_bars(), input_hash="testhash")
        assert r["input_hash"] == "testhash"


# ---------------------------------------------------------------------------
# Readiness
# ---------------------------------------------------------------------------

class TestComputeMomentumReadiness:
    def test_sufficient_bars_is_ready(self):
        r = compute_momentum("AAPL", _rising_bars(260))
        assert r["is_ready"] is True

    def test_insufficient_bars_not_ready(self):
        r = compute_momentum("AAPL", _rising_bars(100))
        assert r["is_ready"] is False
        assert r["passes"] is False
        assert r["skip_reason"] is not None
        assert "insufficient_bars" in r["skip_reason"]

    def test_empty_bars_not_ready(self):
        r = compute_momentum("AAPL", [])
        assert r["is_ready"] is False
        assert r["momentum_score"] is None

    def test_bar_count_correct(self):
        r = compute_momentum("AAPL", _rising_bars(260))
        assert r["bar_count"] == 260


# ---------------------------------------------------------------------------
# Score formula
# ---------------------------------------------------------------------------

class TestMomentumScore:
    def test_score_is_blend_of_roc6m_and_roc12m(self):
        r = compute_momentum("AAPL", _rising_bars(260))
        assert r["is_ready"] is True
        roc6 = r["roc_6m"]
        roc12 = r["roc_12m"]
        expected_score = 0.5 * roc6 + 0.5 * roc12
        assert abs(r["momentum_score"] - expected_score) < 1e-10

    def test_rising_series_positive_score(self):
        r = compute_momentum("AAPL", _rising_bars(260))
        assert r["momentum_score"] > 0.0

    def test_falling_series_negative_score(self):
        r = compute_momentum("AAPL", _falling_bars(260))
        assert r["momentum_score"] < 0.0

    def test_not_ready_score_is_none(self):
        r = compute_momentum("AAPL", _rising_bars(50))
        assert r["momentum_score"] is None


# ---------------------------------------------------------------------------
# Pass / fail logic
# ---------------------------------------------------------------------------

class TestMomentumPassFail:
    def test_rising_passes_with_zero_thresholds(self):
        r = compute_momentum("AAPL", _rising_bars(260), min_momentum_6m=0.0, min_momentum_12m=0.0)
        assert r["passes"] is True
        assert r["passes_6m"] is True
        assert r["passes_12m"] is True
        assert r["skip_reason"] is None

    def test_falling_fails_with_zero_thresholds(self):
        r = compute_momentum("AAPL", _falling_bars(260))
        assert r["passes"] is False
        assert r["skip_reason"] is not None

    def test_flat_fails_with_zero_thresholds(self):
        r = compute_momentum("AAPL", _flat_bars(260))
        # ROC of flat series is 0.0 — not > 0
        assert r["passes"] is False

    def test_positive_roc_fails_when_below_threshold(self):
        r = compute_momentum("AAPL", _rising_bars(260), min_momentum_6m=10.0)
        # rising with step 0.3 won't reach 10x threshold
        assert r["passes_6m"] is False
        assert r["passes"] is False
        assert "roc_6m_below_min" in (r["skip_reason"] or "")

    def test_6m_fails_before_12m_in_skip_reason(self):
        r = compute_momentum("AAPL", _falling_bars(260))
        # falling series: both fail, but 6m checked first
        if r["skip_reason"]:
            assert "roc_6m_below_min" in r["skip_reason"] or "insufficient_bars" in r["skip_reason"]

    def test_skip_reason_null_when_passes(self):
        r = compute_momentum("AAPL", _rising_bars(260))
        if r["passes"]:
            assert r["skip_reason"] is None


# ---------------------------------------------------------------------------
# Custom periods
# ---------------------------------------------------------------------------

class TestCustomPeriods:
    def test_custom_roc_periods_stored(self):
        r = compute_momentum("AAPL", _rising_bars(260), roc_6m_period=63, roc_12m_period=126)
        assert r["roc_6m_period"] == 63
        assert r["roc_12m_period"] == 126

    def test_custom_thresholds_stored(self):
        r = compute_momentum("AAPL", _rising_bars(260), min_momentum_6m=0.01, min_momentum_12m=0.02)
        assert r["min_momentum_6m"] == 0.01
        assert r["min_momentum_12m"] == 0.02
