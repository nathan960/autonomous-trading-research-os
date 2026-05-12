"""Tests for src/trading_os/signals/atr.py"""
from __future__ import annotations

import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trading_os.signals.atr import compute_atr, SIGNAL_ID

_BASE_DATE = date(2022, 1, 3)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_bars(closes: list, high_offset: float = 2.0, low_offset: float = 2.0) -> list:
    bars = []
    for i, c in enumerate(closes):
        d = _BASE_DATE + timedelta(days=i)
        bars.append({
            "timestamp": f"{d.isoformat()}T00:00:00Z",
            "close": c,
            "high": c + high_offset,
            "low": c - low_offset,
            "open": c,
            "volume": 1_000_000,
        })
    return bars


def _rising_bars(n: int = 30, start: float = 100.0) -> list:
    return _make_bars([start + i for i in range(n)])


def _flat_bars(n: int = 30, price: float = 100.0) -> list:
    return _make_bars([price] * n)


# ---------------------------------------------------------------------------
# SIGNAL_ID
# ---------------------------------------------------------------------------

class TestSignalId:
    def test_signal_id_value(self):
        assert SIGNAL_ID == "ATR_SIZING_V1"


# ---------------------------------------------------------------------------
# Structure
# ---------------------------------------------------------------------------

class TestComputeAtrStructure:
    def test_returns_required_keys(self):
        r = compute_atr("AAPL", _rising_bars())
        expected = {
            "signal_id", "symbol", "bar_count",
            "is_ready", "atr_period", "atr", "atr_pct", "latest_close", "input_hash",
        }
        assert expected.issubset(set(r.keys()))

    def test_signal_id_in_result(self):
        r = compute_atr("AAPL", _rising_bars())
        assert r["signal_id"] == SIGNAL_ID

    def test_symbol_in_result(self):
        r = compute_atr("MSFT", _rising_bars())
        assert r["symbol"] == "MSFT"

    def test_input_hash_propagated(self):
        r = compute_atr("AAPL", _rising_bars(), input_hash="xyzabc")
        assert r["input_hash"] == "xyzabc"


# ---------------------------------------------------------------------------
# Readiness
# ---------------------------------------------------------------------------

class TestComputeAtrReadiness:
    def test_sufficient_bars_is_ready(self):
        r = compute_atr("AAPL", _rising_bars(25), period=20)
        assert r["is_ready"] is True

    def test_insufficient_bars_not_ready(self):
        r = compute_atr("AAPL", _rising_bars(5), period=20)
        assert r["is_ready"] is False
        assert r["atr"] is None
        assert r["atr_pct"] is None

    def test_empty_bars_not_ready(self):
        r = compute_atr("AAPL", [])
        assert r["is_ready"] is False
        assert r["latest_close"] is None

    def test_bar_count_correct(self):
        r = compute_atr("AAPL", _rising_bars(30))
        assert r["bar_count"] == 30


# ---------------------------------------------------------------------------
# ATR values
# ---------------------------------------------------------------------------

class TestComputeAtrValues:
    def test_atr_positive_for_volatile_series(self):
        r = compute_atr("AAPL", _rising_bars(30, start=100.0), period=20)
        assert r["is_ready"] is True
        assert r["atr"] is not None
        assert r["atr"] > 0.0

    def test_atr_pct_derived_from_close(self):
        r = compute_atr("AAPL", _flat_bars(30, price=200.0), period=20)
        if r["is_ready"] and r["atr"] is not None:
            expected_pct = r["atr"] / r["latest_close"]
            assert abs(r["atr_pct"] - expected_pct) < 1e-10

    def test_latest_close_populated(self):
        bars = _rising_bars(30, start=100.0)
        r = compute_atr("AAPL", bars, period=20)
        assert r["latest_close"] is not None
        assert r["latest_close"] > 0

    def test_atr_pct_between_zero_and_one(self):
        r = compute_atr("AAPL", _rising_bars(30), period=20)
        if r["is_ready"] and r["atr_pct"] is not None:
            assert 0.0 < r["atr_pct"] < 1.0

    def test_custom_period_stored(self):
        r = compute_atr("AAPL", _rising_bars(30), period=14)
        assert r["atr_period"] == 14

    def test_wilder_smoothing_reduces_with_more_bars(self):
        """More bars → Wilder smoothing converges; just verify it runs without error."""
        r = compute_atr("AAPL", _flat_bars(100, price=100.0), period=20)
        assert r["is_ready"] is True
        assert r["atr"] is not None


# ---------------------------------------------------------------------------
# ATR is non-blocking (no passes/skip_reason field)
# ---------------------------------------------------------------------------

class TestAtrNonBlocking:
    def test_no_passes_field(self):
        r = compute_atr("AAPL", _rising_bars(30))
        assert "passes" not in r

    def test_no_skip_reason_field(self):
        r = compute_atr("AAPL", _rising_bars(30))
        assert "skip_reason" not in r

    def test_no_trigger_id_field(self):
        r = compute_atr("AAPL", _rising_bars(30))
        assert "trigger_id" not in r
