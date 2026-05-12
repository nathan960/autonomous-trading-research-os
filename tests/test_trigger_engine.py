"""Tests for src/trading_os/signals/trigger_engine.py"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trading_os.signals.trigger_engine import run_trigger_scan
from trading_os.time_utils import utc_now_iso


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_bars(closes: list, n_override: int = 0) -> list:
    series = closes if not n_override else closes[:n_override]
    return [
        {
            "timestamp": f"2023-{(i // 28) + 1:02d}-{(i % 28) + 1:02d}T00:00:00Z",
            "close": c,
            "high": c + 2.0,
            "low": c - 2.0,
            "open": c,
            "volume": 2_000_000,
        }
        for i, c in enumerate(series)
    ]


def _rising_closes(n: int = 320, start: float = 100.0, step: float = 0.4) -> list:
    return [start + i * step for i in range(n)]


def _falling_closes(n: int = 320, start: float = 300.0, step: float = 0.4) -> list:
    return [start - i * step for i in range(n)]


def _make_strategy(
    max_snapshot_age: float = 1440.0,
    breadth_threshold: float = 0.55,
    max_spread_pct: float = 0.02,
    max_holdings: int = 5,
    max_names_per_sector: int = 2,
) -> dict:
    return {
        "asset_policy": {"benchmark_symbol": "SPY"},
        "parameters": {
            "max_snapshot_age_minutes": max_snapshot_age,
            "breadth_threshold": breadth_threshold,
            "max_quote_spread_pct": max_spread_pct,
            "sma_period": 200,
            "roc_6m_period": 126,
            "roc_12m_period": 252,
            "min_momentum_6m": 0.0,
            "min_momentum_12m": 0.0,
            "atr_period": 20,
            "max_holdings": max_holdings,
            "max_names_per_sector": max_names_per_sector,
        },
    }


def _make_universe(symbols: list) -> dict:
    return {"symbols": symbols}


def _make_sector_map(symbols: list, sector_code: int = 101) -> dict:
    return {sym: {"sector": "Technology", "sector_code": sector_code} for sym in symbols}


def _make_snapshot(
    symbols: list,
    spy_closes: list | None = None,
    stock_closes: list | None = None,
    generated_at: str | None = None,
    spread_pct_override: float | None = None,
) -> dict:
    now = generated_at or utc_now_iso()
    spy = spy_closes or _rising_closes()
    stock = stock_closes or _rising_closes()

    bars: dict = {"SPY": _make_bars(spy)}
    for sym in symbols:
        if sym != "SPY":
            bars[sym] = _make_bars(stock)

    spreads: dict = {}
    for sym in symbols + ["SPY"]:
        spreads[sym] = {
            "symbol": sym,
            "spread_pct": spread_pct_override if spread_pct_override is not None else 0.001,
        }

    return {"generated_at": now, "bars": bars, "spreads": spreads}


# ---------------------------------------------------------------------------
# DATA_STALE_GATE_V1
# ---------------------------------------------------------------------------

class TestDataStaleGate:
    def test_fresh_snapshot_passes(self):
        symbols = ["AAPL", "MSFT"]
        snapshot = _make_snapshot(symbols)
        strategy = _make_strategy(max_snapshot_age=1440.0)
        result = run_trigger_scan(snapshot, strategy, _make_universe(symbols), _make_sector_map(symbols))
        assert result["data_stale_gate"]["passes"] is True

    def test_stale_snapshot_blocks_all(self):
        symbols = ["AAPL", "MSFT"]
        old_ts = "2020-01-01T00:00:00Z"
        snapshot = _make_snapshot(symbols, generated_at=old_ts)
        strategy = _make_strategy(max_snapshot_age=90.0)
        result = run_trigger_scan(snapshot, strategy, _make_universe(symbols), _make_sector_map(symbols))
        assert result["data_stale_gate"]["passes"] is False
        assert result["selected"] == []
        assert result["regime"] is None
        # All symbols should appear in excluded
        excluded_syms = {e["symbol"] for e in result["excluded"]}
        for sym in symbols:
            assert sym in excluded_syms

    def test_stale_skip_reason_present(self):
        symbols = ["AAPL"]
        snapshot = _make_snapshot(symbols, generated_at="2020-01-01T00:00:00Z")
        strategy = _make_strategy(max_snapshot_age=90.0)
        result = run_trigger_scan(snapshot, strategy, _make_universe(symbols), _make_sector_map(symbols))
        excluded = result["excluded"]
        assert all(e["skip_reason"] is not None for e in excluded)

    def test_missing_timestamp_blocks_all(self):
        symbols = ["AAPL"]
        snapshot = {"bars": {"AAPL": _make_bars(_rising_closes()), "SPY": _make_bars(_rising_closes())}, "spreads": {}}
        strategy = _make_strategy(max_snapshot_age=90.0)
        result = run_trigger_scan(snapshot, strategy, _make_universe(symbols), _make_sector_map(symbols))
        assert result["data_stale_gate"]["passes"] is False


# ---------------------------------------------------------------------------
# Regime
# ---------------------------------------------------------------------------

class TestRegime:
    def test_risk_on_with_uptrend_spy_and_high_breadth(self):
        symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]
        snapshot = _make_snapshot(symbols)
        strategy = _make_strategy(breadth_threshold=0.1)
        result = run_trigger_scan(snapshot, strategy, _make_universe(symbols), _make_sector_map(symbols))
        assert result["regime"]["risk_on"] is True

    def test_risk_off_with_downtrend_spy(self):
        symbols = ["AAPL", "MSFT"]
        snapshot = _make_snapshot(symbols, spy_closes=_falling_closes())
        strategy = _make_strategy()
        result = run_trigger_scan(snapshot, strategy, _make_universe(symbols), _make_sector_map(symbols))
        assert result["regime"]["risk_on"] is False
        assert result["selected"] == []

    def test_risk_off_selected_empty(self):
        symbols = ["AAPL", "MSFT"]
        snapshot = _make_snapshot(symbols, spy_closes=_falling_closes())
        result = run_trigger_scan(
            snapshot,
            _make_strategy(),
            _make_universe(symbols),
            _make_sector_map(symbols),
        )
        assert result["selected"] == []

    def test_risk_off_candidates_have_regime_risk_off_skip_reason(self):
        symbols = ["AAPL", "MSFT"]
        snapshot = _make_snapshot(symbols, spy_closes=_falling_closes())
        result = run_trigger_scan(
            snapshot,
            _make_strategy(breadth_threshold=0.1),
            _make_universe(symbols),
            _make_sector_map(symbols),
        )
        # candidates that would have passed per-symbol should be in excluded with regime_risk_off
        regime_excluded = [e for e in result["excluded"] if e.get("skip_reason") == "regime_risk_off"]
        # If any candidates passed per-symbol filters, they should be in regime_excluded
        if result["candidates"]:
            assert len(regime_excluded) > 0


# ---------------------------------------------------------------------------
# Per-symbol gates
# ---------------------------------------------------------------------------

class TestPerSymbolGates:
    def test_wide_spread_excluded(self):
        symbols = ["AAPL", "MSFT"]
        snapshot = _make_snapshot(symbols, spread_pct_override=0.10)
        strategy = _make_strategy(max_spread_pct=0.02, breadth_threshold=0.1)
        result = run_trigger_scan(snapshot, strategy, _make_universe(symbols), _make_sector_map(symbols))
        # All symbols fail spread gate
        excluded_reasons = {e["skip_reason"] for e in result["excluded"]}
        assert any("spread_too_wide" in (r or "") for r in excluded_reasons)

    def test_insufficient_bars_excluded(self):
        symbols = ["AAPL"]
        snapshot = _make_snapshot(symbols, stock_closes=_rising_closes(50))
        strategy = _make_strategy(breadth_threshold=0.0)
        result = run_trigger_scan(snapshot, strategy, _make_universe(symbols), _make_sector_map(symbols))
        assert "AAPL" not in result["selected"]
        aapl_excluded = [e for e in result["excluded"] if e["symbol"] == "AAPL"]
        assert len(aapl_excluded) >= 1
        assert aapl_excluded[0]["skip_reason"] is not None

    def test_symbol_results_populated_for_all_non_benchmark(self):
        symbols = ["AAPL", "MSFT", "GOOGL"]
        snapshot = _make_snapshot(symbols)
        strategy = _make_strategy(breadth_threshold=0.1)
        result = run_trigger_scan(snapshot, strategy, _make_universe(symbols), _make_sector_map(symbols))
        for sym in symbols:
            if sym != "SPY":
                assert sym in result["symbol_results"]

    def test_benchmark_not_in_symbol_results(self):
        symbols = ["AAPL", "MSFT"]
        snapshot = _make_snapshot(symbols)
        strategy = _make_strategy(breadth_threshold=0.1)
        result = run_trigger_scan(snapshot, strategy, _make_universe(symbols), _make_sector_map(symbols))
        assert "SPY" not in result["symbol_results"]


# ---------------------------------------------------------------------------
# input_hash on every result
# ---------------------------------------------------------------------------

class TestInputHash:
    def test_every_symbol_result_has_input_hash(self):
        symbols = ["AAPL", "MSFT"]
        snapshot = _make_snapshot(symbols)
        strategy = _make_strategy(breadth_threshold=0.1)
        result = run_trigger_scan(snapshot, strategy, _make_universe(symbols), _make_sector_map(symbols))
        for sym, res in result["symbol_results"].items():
            assert res.get("input_hash"), f"{sym} missing input_hash"
            assert len(res["input_hash"]) == 64  # sha256 hex

    def test_candidates_have_input_hash(self):
        symbols = ["AAPL", "MSFT"]
        snapshot = _make_snapshot(symbols)
        strategy = _make_strategy(breadth_threshold=0.1)
        result = run_trigger_scan(snapshot, strategy, _make_universe(symbols), _make_sector_map(symbols))
        # candidates list is just symbols; check via symbol_results
        for sym in result["candidates"]:
            assert result["symbol_results"][sym].get("input_hash")


# ---------------------------------------------------------------------------
# Sector caps
# ---------------------------------------------------------------------------

class TestSectorCaps:
    def test_sector_cap_respected(self):
        symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]
        # All same sector, cap=2
        sector_map = {sym: {"sector": "Technology", "sector_code": 101} for sym in symbols}
        snapshot = _make_snapshot(symbols)
        strategy = _make_strategy(max_holdings=10, max_names_per_sector=2, breadth_threshold=0.1)
        result = run_trigger_scan(snapshot, strategy, _make_universe(symbols), sector_map)
        if result["regime"]["risk_on"]:
            assert len(result["selected"]) <= 2

    def test_max_holdings_respected(self):
        symbols = [f"SYM{i}" for i in range(10)]
        sector_map = {sym: {"sector": "X", "sector_code": i} for i, sym in enumerate(symbols)}
        snapshot = _make_snapshot(symbols)
        strategy = _make_strategy(max_holdings=3, max_names_per_sector=10, breadth_threshold=0.1)
        result = run_trigger_scan(snapshot, strategy, _make_universe(symbols), sector_map)
        if result["regime"]["risk_on"]:
            assert len(result["selected"]) <= 3


# ---------------------------------------------------------------------------
# Every skipped symbol has a skip_reason
# ---------------------------------------------------------------------------

class TestSkipReasons:
    def test_all_excluded_have_skip_reason(self):
        symbols = ["AAPL", "MSFT", "GOOGL"]
        snapshot = _make_snapshot(symbols)
        strategy = _make_strategy(breadth_threshold=0.1, max_holdings=1, max_names_per_sector=1)
        result = run_trigger_scan(snapshot, strategy, _make_universe(symbols), _make_sector_map(symbols))
        for entry in result["excluded"]:
            assert entry.get("skip_reason") is not None, f"{entry.get('symbol')} has null skip_reason"

    def test_stale_gate_excluded_all_have_reason(self):
        symbols = ["AAPL", "MSFT"]
        snapshot = _make_snapshot(symbols, generated_at="2020-01-01T00:00:00Z")
        result = run_trigger_scan(
            snapshot,
            _make_strategy(max_snapshot_age=90.0),
            _make_universe(symbols),
            _make_sector_map(symbols),
        )
        for e in result["excluded"]:
            assert e["skip_reason"] is not None


# ---------------------------------------------------------------------------
# Snapshot integrity
# ---------------------------------------------------------------------------

class TestSnapshotIntegrity:
    def test_trigger_snapshot_hash_present(self):
        symbols = ["AAPL", "MSFT"]
        result = run_trigger_scan(
            _make_snapshot(symbols),
            _make_strategy(breadth_threshold=0.1),
            _make_universe(symbols),
            _make_sector_map(symbols),
        )
        assert "trigger_snapshot_hash" in result
        assert len(result["trigger_snapshot_hash"]) == 64

    def test_scanned_at_present(self):
        symbols = ["AAPL"]
        result = run_trigger_scan(
            _make_snapshot(symbols),
            _make_strategy(breadth_threshold=0.1),
            _make_universe(symbols),
            _make_sector_map(symbols),
        )
        assert result.get("scanned_at")

    def test_required_top_level_keys(self):
        symbols = ["AAPL", "MSFT"]
        result = run_trigger_scan(
            _make_snapshot(symbols),
            _make_strategy(breadth_threshold=0.1),
            _make_universe(symbols),
            _make_sector_map(symbols),
        )
        required = {
            "scanned_at", "data_stale_gate", "regime",
            "symbol_results", "candidates", "selected",
            "excluded", "sector_counts", "trigger_snapshot_hash",
        }
        assert required.issubset(set(result.keys()))

    def test_selected_is_subset_of_candidates(self):
        symbols = ["AAPL", "MSFT", "GOOGL"]
        result = run_trigger_scan(
            _make_snapshot(symbols),
            _make_strategy(breadth_threshold=0.1),
            _make_universe(symbols),
            _make_sector_map(symbols),
        )
        assert set(result["selected"]).issubset(set(result["candidates"]))
