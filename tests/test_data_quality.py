"""Tests for trading_os.data.data_quality — pure functions, no Alpaca credentials."""
from __future__ import annotations

import pytest

from trading_os.data.data_quality import (
    assess_asset_tradability,
    assess_bar_coverage,
    assess_quote_coverage,
    assess_snapshot_freshness,
    assess_spread_quality,
    build_quality_report,
)
from trading_os.time_utils import utc_now_iso


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _make_bars(symbols: list, count: int = 260) -> dict:
    """Create a bars dict with `count` placeholder bars per symbol."""
    bar = {"timestamp": "2026-01-01T21:00:00Z", "open": 100.0, "high": 101.0, "low": 99.0, "close": 100.0, "volume": 1_000_000}
    return {sym: [bar] * count for sym in symbols}


def _make_quotes(symbols: list, bid: float = 99.9, ask: float = 100.1) -> dict:
    return {sym: {"bid_price": bid, "ask_price": ask, "symbol": sym} for sym in symbols}


def _make_spreads(symbols: list, spread_pct: float = 0.001) -> dict:
    return {sym: {"symbol": sym, "spread_pct": spread_pct} for sym in symbols}


def _make_assets(symbols: list, tradable: bool = True) -> dict:
    return {sym: {"symbol": sym, "tradable": tradable, "fractionable": True, "status": "active"} for sym in symbols}


SYMS = ["AAPL", "MSFT", "SPY", "BIL"]


# ---------------------------------------------------------------------------
# assess_bar_coverage
# ---------------------------------------------------------------------------

class TestAssessBarCoverage:
    def test_clean_returns_empty(self) -> None:
        bars = _make_bars(SYMS, 260)
        missing, insufficient = assess_bar_coverage(bars, SYMS, min_bars_required=253)
        assert missing == []
        assert insufficient == {}

    def test_missing_symbol_detected(self) -> None:
        bars = _make_bars(["AAPL", "SPY", "BIL"], 260)
        missing, _ = assess_bar_coverage(bars, SYMS, min_bars_required=253)
        assert "MSFT" in missing

    def test_empty_bar_list_is_missing(self) -> None:
        bars = {**_make_bars(SYMS, 260), "AAPL": []}
        missing, _ = assess_bar_coverage(bars, SYMS, min_bars_required=253)
        assert "AAPL" in missing

    def test_insufficient_bars_detected(self) -> None:
        bars = {**_make_bars(SYMS, 260), "MSFT": [{}] * 100}
        _, insufficient = assess_bar_coverage(bars, SYMS, min_bars_required=253)
        assert "MSFT" in insufficient
        assert insufficient["MSFT"] == 100

    def test_exactly_min_bars_is_sufficient(self) -> None:
        bars = _make_bars(SYMS, 253)
        _, insufficient = assess_bar_coverage(bars, SYMS, min_bars_required=253)
        assert insufficient == {}

    def test_one_fewer_than_min_is_insufficient(self) -> None:
        bars = _make_bars(SYMS, 252)
        _, insufficient = assess_bar_coverage(bars, SYMS, min_bars_required=253)
        assert all(sym in insufficient for sym in SYMS)

    def test_empty_universe_returns_empty(self) -> None:
        missing, insufficient = assess_bar_coverage({}, [], min_bars_required=253)
        assert missing == [] and insufficient == {}

    def test_missing_symbol_not_in_insufficient(self) -> None:
        # A completely missing symbol should appear in missing, not insufficient.
        bars = _make_bars(["SPY", "BIL"], 260)
        missing, insufficient = assess_bar_coverage(bars, ["AAPL", "SPY", "BIL"], 253)
        assert "AAPL" in missing
        assert "AAPL" not in insufficient


# ---------------------------------------------------------------------------
# assess_quote_coverage
# ---------------------------------------------------------------------------

class TestAssessQuoteCoverage:
    def test_clean_returns_empty(self) -> None:
        quotes = _make_quotes(SYMS)
        assert assess_quote_coverage(quotes, SYMS) == []

    def test_missing_symbol_detected(self) -> None:
        quotes = _make_quotes(["AAPL", "SPY", "BIL"])
        missing = assess_quote_coverage(quotes, SYMS)
        assert "MSFT" in missing

    def test_non_dict_quote_is_missing(self) -> None:
        quotes = {**_make_quotes(SYMS), "AAPL": "bad_value"}
        missing = assess_quote_coverage(quotes, SYMS)
        assert "AAPL" in missing

    def test_empty_universe_returns_empty(self) -> None:
        assert assess_quote_coverage({}, []) == []


# ---------------------------------------------------------------------------
# assess_spread_quality
# ---------------------------------------------------------------------------

class TestAssessSpreadQuality:
    def test_tight_spreads_pass(self) -> None:
        spreads = _make_spreads(SYMS, spread_pct=0.001)
        assert assess_spread_quality(spreads, max_spread_pct=0.02) == {}

    def test_wide_spread_detected(self) -> None:
        spreads = {**_make_spreads(SYMS, 0.001), "AAPL": {"spread_pct": 0.05}}
        wide = assess_spread_quality(spreads, max_spread_pct=0.02)
        assert "AAPL" in wide

    def test_exactly_at_limit_does_not_flag(self) -> None:
        spreads = {"AAPL": {"spread_pct": 0.02}}
        assert assess_spread_quality(spreads, max_spread_pct=0.02) == {}

    def test_just_above_limit_flags(self) -> None:
        spreads = {"AAPL": {"spread_pct": 0.0201}}
        wide = assess_spread_quality(spreads, max_spread_pct=0.02)
        assert "AAPL" in wide

    def test_none_spread_pct_ignored(self) -> None:
        spreads = {"AAPL": {"spread_pct": None}}
        assert assess_spread_quality(spreads, max_spread_pct=0.02) == {}

    def test_non_dict_entry_ignored(self) -> None:
        spreads = {"AAPL": "bad"}
        assert assess_spread_quality(spreads, max_spread_pct=0.02) == {}

    def test_empty_spreads_pass(self) -> None:
        assert assess_spread_quality({}, max_spread_pct=0.02) == {}


# ---------------------------------------------------------------------------
# assess_snapshot_freshness
# ---------------------------------------------------------------------------

class TestAssessSnapshotFreshness:
    def test_just_fetched_is_very_fresh(self) -> None:
        age = assess_snapshot_freshness(utc_now_iso(), max_age_minutes=90.0)
        assert age is not None
        assert 0.0 <= age < 1.0

    def test_invalid_timestamp_returns_none(self) -> None:
        assert assess_snapshot_freshness("not-a-timestamp") is None
        assert assess_snapshot_freshness("") is None

    def test_old_timestamp_has_large_age(self) -> None:
        age = assess_snapshot_freshness("2020-01-01T00:00:00Z")
        assert age is not None
        assert age > 100_000  # many minutes in the past


# ---------------------------------------------------------------------------
# assess_asset_tradability
# ---------------------------------------------------------------------------

class TestAssessAssetTradability:
    def test_all_tradable_returns_empty(self) -> None:
        assets = _make_assets(SYMS, tradable=True)
        assert assess_asset_tradability(assets, SYMS) == []

    def test_non_tradable_detected(self) -> None:
        assets = {**_make_assets(SYMS, tradable=True), "AAPL": {"symbol": "AAPL", "tradable": False}}
        not_tradable = assess_asset_tradability(assets, SYMS)
        assert "AAPL" in not_tradable

    def test_error_entry_flagged(self) -> None:
        assets = {**_make_assets(SYMS, tradable=True), "AAPL": {"symbol": "AAPL", "tradable": True, "error": "fetch_failed"}}
        not_tradable = assess_asset_tradability(assets, SYMS)
        assert "AAPL" in not_tradable

    def test_missing_entry_flagged(self) -> None:
        assets = _make_assets(["MSFT", "SPY", "BIL"], tradable=True)
        not_tradable = assess_asset_tradability(assets, SYMS)
        assert "AAPL" in not_tradable

    def test_empty_universe_returns_empty(self) -> None:
        assert assess_asset_tradability({}, []) == []


# ---------------------------------------------------------------------------
# build_quality_report (integration)
# ---------------------------------------------------------------------------

class TestBuildQualityReport:
    def _market(self, syms: list = None, bar_count: int = 260) -> dict:
        syms = syms or SYMS
        bars = _make_bars(syms, bar_count)
        quotes = _make_quotes(syms)
        spreads = _make_spreads(syms, 0.001)
        assets = _make_assets(syms)
        return {
            "schema_version": "0.1.0",
            "source": "alpaca_paper",
            "data_feed": "iex",
            "fetched_at": utc_now_iso(),
            "bars": bars,
            "latest_bars": {sym: bars[sym][-1] for sym in syms},
            "quotes": quotes,
            "spreads": spreads,
            "assets": assets,
            "bar_counts": {sym: len(bars[sym]) for sym in syms},
            "source_labels": {},
            "data_hash": "abc123",
        }

    def _account(self) -> dict:
        return {
            "schema_version": "0.1.0",
            "source": "alpaca_paper",
            "fetched_at": utc_now_iso(),
            "account": {"equity": "40000.00"},
            "positions": [],
            "orders": [],
            "position_count": 0,
            "open_order_count": 0,
            "data_hash": "def456",
        }

    def test_clean_data_passes(self) -> None:
        report = build_quality_report(
            self._market(),
            self._account(),
            SYMS,
            min_bars_required=253,
            max_spread_pct=0.02,
            max_snapshot_age_minutes=90.0,
            run_id="test-001",
        )
        assert report["status"] == "PASS"
        assert report["issues"] == []

    def test_missing_bar_triggers_issue(self) -> None:
        market = self._market()
        del market["bars"]["AAPL"]
        market["bar_counts"].pop("AAPL", None)
        report = build_quality_report(market, self._account(), SYMS)
        assert "missing_bars" in report["issues"]
        assert "AAPL" in report["missing_bars"]

    def test_insufficient_bars_triggers_issue(self) -> None:
        market = self._market(bar_count=100)
        report = build_quality_report(
            market, self._account(), SYMS, min_bars_required=253
        )
        assert "insufficient_bars" in report["issues"]

    def test_missing_quote_triggers_issue(self) -> None:
        market = self._market()
        del market["quotes"]["AAPL"]
        report = build_quality_report(market, self._account(), SYMS)
        assert "missing_quotes" in report["issues"]
        assert "AAPL" in report["missing_quotes"]

    def test_wide_spread_triggers_issue(self) -> None:
        market = self._market()
        market["spreads"]["AAPL"] = {"spread_pct": 0.10}
        report = build_quality_report(
            market, self._account(), SYMS, max_spread_pct=0.02
        )
        assert "wide_spreads" in report["issues"]

    def test_stale_snapshot_triggers_issue(self) -> None:
        market = self._market()
        market["fetched_at"] = "2020-01-01T00:00:00Z"
        report = build_quality_report(
            market, self._account(), SYMS, max_snapshot_age_minutes=90.0
        )
        assert "stale_or_unparseable_snapshot" in report["issues"]

    def test_missing_data_hash_triggers_issue(self) -> None:
        market = self._market()
        del market["data_hash"]
        report = build_quality_report(market, self._account(), SYMS)
        assert "missing_data_hash" in report["issues"]

    def test_non_tradable_triggers_issue(self) -> None:
        market = self._market()
        market["assets"]["AAPL"] = {"symbol": "AAPL", "tradable": False}
        report = build_quality_report(market, self._account(), SYMS)
        assert "non_tradable_symbols" in report["issues"]
        assert "AAPL" in report["not_tradable"]

    def test_report_has_data_hash(self) -> None:
        report = build_quality_report(self._market(), self._account(), SYMS)
        assert isinstance(report.get("data_hash"), str)
        assert len(report["data_hash"]) == 64

    def test_run_id_propagated(self) -> None:
        report = build_quality_report(
            self._market(), self._account(), SYMS, run_id="my-run-id"
        )
        assert report["run_id"] == "my-run-id"

    def test_multiple_issues_collected(self) -> None:
        market = self._market(bar_count=100)
        del market["quotes"]["AAPL"]
        market["spreads"]["MSFT"] = {"spread_pct": 0.99}
        report = build_quality_report(
            market, self._account(), SYMS, min_bars_required=253, max_spread_pct=0.02
        )
        assert len(report["issues"]) >= 3

    def test_benchmark_and_fallback_always_checked(self) -> None:
        # Universe list doesn't include SPY/BIL explicitly — they should still be checked.
        market = self._market(syms=["AAPL", "MSFT"])
        # SPY and BIL will be in expected_symbols; market has them too.
        report = build_quality_report(market, self._account(), ["AAPL", "MSFT"])
        # Should still check SPY and BIL coverage.
        assert report["symbols_expected"] == 4  # AAPL, MSFT, BIL, SPY
