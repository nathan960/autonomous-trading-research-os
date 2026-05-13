"""Tests for src/trading_os/research/spread_diagnostics.py"""
from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from trading_os.research.spread_diagnostics import (
    FC_FEED_LIMITATION,
    FC_MISSING_ASK,
    FC_MISSING_BID,
    FC_OFF_HOURS,
    FC_PASS,
    FC_STALE_QUOTE,
    FC_UNKNOWN,
    FC_WIDE_REAL,
    FC_ZERO_BID_OR_ASK,
    analyze_symbol,
    build_spread_diagnostics,
    classify_spread_failure,
    write_spread_diagnostics,
)


# ---------------------------------------------------------------------------
# Fixtures / helpers
# ---------------------------------------------------------------------------

SNAPSHOT_TS = "2026-05-13T21:01:05Z"
QUOTE_TS_AT_CLOSE = "2026-05-13T20:00:00Z"   # 61 min before snapshot
QUOTE_TS_FRESH = "2026-05-13T21:00:00Z"       # 1 min before snapshot
QUOTE_TS_STALE = "2026-05-13T19:00:00Z"       # 121 min before snapshot

CLOCK_CLOSED = {"is_open": False, "timestamp": SNAPSHOT_TS, "next_open": "2026-05-14T13:30:00Z"}
CLOCK_OPEN = {"is_open": True, "timestamp": SNAPSHOT_TS}

MAX_SPREAD = 0.02


def _quote(bid=200.0, ask=202.0, ts=QUOTE_TS_FRESH):
    return {"bid_price": bid, "ask_price": ask, "timestamp": ts}


def _spread_info(bid=200.0, ask=202.0):
    if bid is None or ask is None or bid == 0 or ask == 0:
        return {"bid": bid, "ask": ask, "spread": None, "spread_pct": None}
    spread = ask - bid
    mid = (ask + bid) / 2
    spread_pct = spread / mid if mid > 0 else None
    return {"bid": bid, "ask": ask, "spread": spread, "spread_pct": spread_pct}


def _market_snapshot(
    is_open=True,
    feed="iex",
    symbols=None,
    spread_overrides=None,
    quote_ts=QUOTE_TS_FRESH,
):
    symbols = symbols or ["AAPL", "MSFT"]
    spread_overrides = spread_overrides or {}
    quotes = {}
    spreads = {}
    for sym in symbols:
        if sym in spread_overrides:
            bid, ask = spread_overrides[sym]
        else:
            bid, ask = 200.0, 201.0  # 0.5% spread — passes
        quotes[sym] = {"bid_price": bid, "ask_price": ask, "timestamp": quote_ts}
        if bid and ask and bid > 0 and ask > 0:
            sp = ask - bid
            spreads[sym] = {"bid": bid, "ask": ask, "spread": sp, "spread_pct": sp / ((bid + ask) / 2)}
        else:
            spreads[sym] = {"bid": bid, "ask": ask, "spread": None, "spread_pct": None}
    return {
        "generated_at": SNAPSHOT_TS,
        "data_feed": feed,
        "clock": {"is_open": is_open, "timestamp": SNAPSHOT_TS, "next_open": "2026-05-14T13:30:00Z"},
        "quotes": quotes,
        "spreads": spreads,
    }


def _risk_limits():
    return {"max_quote_spread_pct": MAX_SPREAD}


def _sector_map():
    return {
        "AAPL": {"sector": "Technology"},
        "MSFT": {"sector": "Technology"},
        "JNJ": {"sector": "Health Care"},
    }


# ---------------------------------------------------------------------------
# TestClassifySpreadFailure
# ---------------------------------------------------------------------------

class TestClassifySpreadFailure:
    def test_pass_when_spread_within_threshold(self):
        result = classify_spread_failure(
            bid=200.0, ask=201.0, spread_pct=0.005,
            quote_ts_str=QUOTE_TS_FRESH, snapshot_ts_str=SNAPSHOT_TS,
            market_is_open=True, max_spread_pct=MAX_SPREAD, data_feed="iex",
        )
        assert result == FC_PASS

    def test_missing_bid_when_bid_is_none(self):
        result = classify_spread_failure(
            bid=None, ask=201.0, spread_pct=None,
            quote_ts_str=QUOTE_TS_FRESH, snapshot_ts_str=SNAPSHOT_TS,
            market_is_open=True, max_spread_pct=MAX_SPREAD,
        )
        assert result == FC_MISSING_BID

    def test_missing_ask_when_ask_is_none(self):
        result = classify_spread_failure(
            bid=200.0, ask=None, spread_pct=None,
            quote_ts_str=QUOTE_TS_FRESH, snapshot_ts_str=SNAPSHOT_TS,
            market_is_open=True, max_spread_pct=MAX_SPREAD,
        )
        assert result == FC_MISSING_ASK

    def test_zero_bid_or_ask_when_ask_is_zero(self):
        result = classify_spread_failure(
            bid=200.0, ask=0.0, spread_pct=None,
            quote_ts_str=QUOTE_TS_FRESH, snapshot_ts_str=SNAPSHOT_TS,
            market_is_open=False, max_spread_pct=MAX_SPREAD, data_feed="iex",
        )
        assert result == FC_ZERO_BID_OR_ASK

    def test_zero_bid_or_ask_when_bid_is_zero(self):
        result = classify_spread_failure(
            bid=0.0, ask=200.0, spread_pct=None,
            quote_ts_str=QUOTE_TS_FRESH, snapshot_ts_str=SNAPSHOT_TS,
            market_is_open=True, max_spread_pct=MAX_SPREAD,
        )
        assert result == FC_ZERO_BID_OR_ASK

    def test_unknown_when_spread_pct_none_but_nonzero_bid_ask(self):
        result = classify_spread_failure(
            bid=200.0, ask=202.0, spread_pct=None,
            quote_ts_str=QUOTE_TS_FRESH, snapshot_ts_str=SNAPSHOT_TS,
            market_is_open=True, max_spread_pct=MAX_SPREAD,
        )
        assert result == FC_UNKNOWN

    def test_off_hours_when_market_closed_and_spread_wide(self):
        result = classify_spread_failure(
            bid=200.0, ask=222.0, spread_pct=0.10,
            quote_ts_str=QUOTE_TS_AT_CLOSE, snapshot_ts_str=SNAPSHOT_TS,
            market_is_open=False, max_spread_pct=MAX_SPREAD, data_feed="iex",
        )
        assert result == FC_OFF_HOURS

    def test_stale_quote_when_market_open_but_old_quote(self):
        result = classify_spread_failure(
            bid=200.0, ask=222.0, spread_pct=0.10,
            quote_ts_str=QUOTE_TS_STALE, snapshot_ts_str=SNAPSHOT_TS,
            market_is_open=True, max_spread_pct=MAX_SPREAD, data_feed="sip",
        )
        assert result == FC_STALE_QUOTE

    def test_data_feed_limitation_when_open_fresh_iex_and_wide(self):
        result = classify_spread_failure(
            bid=200.0, ask=222.0, spread_pct=0.10,
            quote_ts_str=QUOTE_TS_FRESH, snapshot_ts_str=SNAPSHOT_TS,
            market_is_open=True, max_spread_pct=MAX_SPREAD, data_feed="iex",
        )
        assert result == FC_FEED_LIMITATION

    def test_wide_spread_real_when_open_fresh_sip_and_wide(self):
        result = classify_spread_failure(
            bid=200.0, ask=222.0, spread_pct=0.10,
            quote_ts_str=QUOTE_TS_FRESH, snapshot_ts_str=SNAPSHOT_TS,
            market_is_open=True, max_spread_pct=MAX_SPREAD, data_feed="sip",
        )
        assert result == FC_WIDE_REAL

    def test_off_hours_takes_precedence_over_stale_quote(self):
        # Market is closed AND quote is stale — off_hours wins
        result = classify_spread_failure(
            bid=200.0, ask=222.0, spread_pct=0.10,
            quote_ts_str=QUOTE_TS_STALE, snapshot_ts_str=SNAPSHOT_TS,
            market_is_open=False, max_spread_pct=MAX_SPREAD, data_feed="iex",
        )
        assert result == FC_OFF_HOURS

    def test_zero_ask_checked_before_market_status(self):
        # zero_bid_or_ask must be returned even if market is open
        result = classify_spread_failure(
            bid=200.0, ask=0.0, spread_pct=None,
            quote_ts_str=QUOTE_TS_FRESH, snapshot_ts_str=SNAPSHOT_TS,
            market_is_open=True, max_spread_pct=MAX_SPREAD,
        )
        assert result == FC_ZERO_BID_OR_ASK

    def test_missing_bid_checked_before_zero_ask(self):
        result = classify_spread_failure(
            bid=None, ask=0.0, spread_pct=None,
            quote_ts_str=QUOTE_TS_FRESH, snapshot_ts_str=SNAPSHOT_TS,
            market_is_open=True, max_spread_pct=MAX_SPREAD,
        )
        assert result == FC_MISSING_BID


# ---------------------------------------------------------------------------
# TestAnalyzeSymbol
# ---------------------------------------------------------------------------

class TestAnalyzeSymbol:
    def test_returns_all_required_fields(self):
        q = _quote(bid=200.0, ask=201.0, ts=QUOTE_TS_FRESH)
        si = _spread_info(bid=200.0, ask=201.0)
        rec = analyze_symbol(
            symbol="AAPL", quote=q, spread_info=si,
            market_clock=CLOCK_OPEN, sector="Technology",
            max_spread_pct=MAX_SPREAD, data_feed="iex",
            snapshot_ts=SNAPSHOT_TS,
        )
        for field in [
            "symbol", "sector", "bid", "ask", "spread", "spread_pct",
            "quote_timestamp", "quote_age_minutes", "quote_age_bucket",
            "market_is_open", "source_feed", "max_spread_pct",
            "spread_pass", "failure_class",
        ]:
            assert field in rec, f"missing field: {field}"

    def test_spread_pass_true_when_within_threshold(self):
        q = _quote(bid=200.0, ask=201.0)
        si = _spread_info(bid=200.0, ask=201.0)
        rec = analyze_symbol(
            symbol="AAPL", quote=q, spread_info=si,
            market_clock=CLOCK_OPEN, sector="Technology",
            max_spread_pct=MAX_SPREAD, data_feed="iex",
            snapshot_ts=SNAPSHOT_TS,
        )
        assert rec["spread_pass"] is True
        assert rec["failure_class"] == FC_PASS

    def test_off_hours_class_when_market_closed_and_wide(self):
        q = _quote(bid=200.0, ask=220.0, ts=QUOTE_TS_AT_CLOSE)
        si = {"spread_pct": 0.095, "spread": 20.0}
        rec = analyze_symbol(
            symbol="JNJ", quote=q, spread_info=si,
            market_clock=CLOCK_CLOSED, sector="Health Care",
            max_spread_pct=MAX_SPREAD, data_feed="iex",
            snapshot_ts=SNAPSHOT_TS,
        )
        assert rec["failure_class"] == FC_OFF_HOURS
        assert rec["spread_pass"] is False
        assert rec["market_is_open"] is False

    def test_zero_bid_or_ask_class(self):
        q = {"bid_price": 200.0, "ask_price": 0.0, "timestamp": QUOTE_TS_AT_CLOSE}
        si = {"spread_pct": None, "spread": None}
        rec = analyze_symbol(
            symbol="SPY", quote=q, spread_info=si,
            market_clock=CLOCK_CLOSED, sector="ETF",
            max_spread_pct=MAX_SPREAD, data_feed="iex",
            snapshot_ts=SNAPSHOT_TS,
        )
        assert rec["failure_class"] == FC_ZERO_BID_OR_ASK

    def test_quote_age_minutes_computed(self):
        q = _quote(bid=200.0, ask=201.0, ts=QUOTE_TS_AT_CLOSE)
        si = _spread_info(200.0, 201.0)
        rec = analyze_symbol(
            symbol="X", quote=q, spread_info=si,
            market_clock=CLOCK_OPEN, sector="Unknown",
            max_spread_pct=MAX_SPREAD, data_feed="iex",
            snapshot_ts=SNAPSHOT_TS,
        )
        assert rec["quote_age_minutes"] is not None
        assert 60 <= rec["quote_age_minutes"] <= 62  # ~61 min

    def test_max_spread_pct_not_mutated(self):
        original_limits = {"max_quote_spread_pct": MAX_SPREAD}
        q = _quote()
        si = _spread_info()
        rec = analyze_symbol(
            symbol="AAPL", quote=q, spread_info=si,
            market_clock=CLOCK_OPEN, sector="Technology",
            max_spread_pct=original_limits["max_quote_spread_pct"],
            data_feed="iex", snapshot_ts=SNAPSHOT_TS,
        )
        assert original_limits["max_quote_spread_pct"] == MAX_SPREAD


# ---------------------------------------------------------------------------
# TestBuildSpreadDiagnostics
# ---------------------------------------------------------------------------

class TestBuildSpreadDiagnostics:
    def _build(self, is_open=False, feed="iex", spread_overrides=None, quote_ts=QUOTE_TS_AT_CLOSE):
        ms = _market_snapshot(
            is_open=is_open, feed=feed,
            symbols=["AAPL", "MSFT", "JNJ"],
            spread_overrides=spread_overrides,
            quote_ts=quote_ts,
        )
        return build_spread_diagnostics(
            market_snapshot=ms,
            data_quality_snapshot={"data_feed": feed},
            risk_limits=_risk_limits(),
            sector_map=_sector_map(),
        )

    def test_returns_required_top_level_fields(self):
        snap = self._build()
        for field in [
            "run_id", "generated_at", "market_snapshot_ts", "market_is_open",
            "market_clock", "data_feed", "max_spread_pct", "summary",
            "findings", "recommendations", "symbols", "no_config_was_modified",
        ]:
            assert field in snap, f"missing field: {field}"

    def test_no_config_was_modified_always_true(self):
        snap = self._build()
        assert snap["no_config_was_modified"] is True

    def test_max_spread_pct_taken_from_risk_limits_not_invented(self):
        snap = self._build()
        assert snap["max_spread_pct"] == MAX_SPREAD

    def test_all_pass_when_spreads_tight_and_market_open(self):
        snap = self._build(
            is_open=True, feed="sip", quote_ts=QUOTE_TS_FRESH,
            # default bid/ask gives ~0.5% spread, well under 2%
        )
        s = snap["summary"]
        assert s["pass_count"] == s["total_symbols"]
        assert s["fail_count"] == 0

    def test_off_hours_blocks_when_market_closed_wide_spreads(self):
        snap = self._build(
            is_open=False,
            spread_overrides={"AAPL": (200.0, 222.0), "MSFT": (300.0, 333.0)},
        )
        s = snap["summary"]
        by_class = s["by_failure_class"]
        assert by_class.get(FC_OFF_HOURS, 0) == 2

    def test_zero_bid_or_ask_counted_separately(self):
        snap = self._build(
            is_open=False,
            spread_overrides={"AAPL": (200.0, 0.0), "MSFT": (300.0, 0.0)},
        )
        s = snap["summary"]
        by_class = s["by_failure_class"]
        assert by_class.get(FC_ZERO_BID_OR_ASK, 0) == 2

    def test_findings_not_empty(self):
        snap = self._build()
        assert len(snap["findings"]) > 0

    def test_recommendations_not_empty(self):
        snap = self._build()
        assert len(snap["recommendations"]) > 0

    def test_keep_threshold_recommendation_always_present(self):
        snap = self._build()
        actions = [r["action"] for r in snap["recommendations"]]
        assert "keep_threshold_unchanged" in actions

    def test_threshold_not_changed_in_recommendations(self):
        snap = self._build()
        for rec in snap["recommendations"]:
            assert "change" not in rec.get("action", "").lower() or "unchanged" in rec.get("action", "")
            detail = rec.get("detail", "")
            assert "loosen" not in detail.lower()
            assert "tighten" not in detail.lower()
            assert "adjust" not in detail.lower() or "Do not adjust" in detail

    def test_symbols_list_covers_all_universe(self):
        snap = self._build()
        symbols_in_snap = {r["symbol"] for r in snap["symbols"]}
        assert "AAPL" in symbols_in_snap
        assert "MSFT" in symbols_in_snap

    def test_summary_by_sector_present(self):
        snap = self._build()
        assert "by_sector" in snap["summary"]

    def test_summary_by_market_status_present(self):
        snap = self._build()
        assert "by_market_status" in snap["summary"]


# ---------------------------------------------------------------------------
# TestNoConfigMutation
# ---------------------------------------------------------------------------

class TestNoConfigMutation:
    def test_risk_limits_dict_not_mutated(self):
        limits = {"max_quote_spread_pct": 0.02, "extra": "value"}
        original = limits.copy()
        ms = _market_snapshot(symbols=["AAPL"])
        build_spread_diagnostics(
            market_snapshot=ms,
            data_quality_snapshot={},
            risk_limits=limits,
            sector_map=_sector_map(),
        )
        assert limits == original

    def test_sector_map_not_mutated(self):
        sm = _sector_map()
        original = {k: dict(v) for k, v in sm.items()}
        ms = _market_snapshot(symbols=["AAPL"])
        build_spread_diagnostics(
            market_snapshot=ms,
            data_quality_snapshot={},
            risk_limits=_risk_limits(),
            sector_map=sm,
        )
        for k, v in original.items():
            assert sm[k] == v

    def test_market_snapshot_not_mutated(self):
        ms = _market_snapshot(symbols=["AAPL"])
        original_keys = set(ms.keys())
        build_spread_diagnostics(
            market_snapshot=ms,
            data_quality_snapshot={},
            risk_limits=_risk_limits(),
            sector_map=_sector_map(),
        )
        assert set(ms.keys()) == original_keys

    def test_spread_threshold_value_unchanged_in_output(self):
        snap = build_spread_diagnostics(
            market_snapshot=_market_snapshot(symbols=["AAPL"]),
            data_quality_snapshot={},
            risk_limits=_risk_limits(),
            sector_map=_sector_map(),
        )
        assert snap["max_spread_pct"] == MAX_SPREAD
        for sym_rec in snap["symbols"]:
            assert sym_rec["max_spread_pct"] == MAX_SPREAD


# ---------------------------------------------------------------------------
# TestWriteSpreadDiagnostics
# ---------------------------------------------------------------------------

class TestWriteSpreadDiagnostics:
    def test_writes_latest_and_history(self, tmp_path):
        snap = build_spread_diagnostics(
            market_snapshot=_market_snapshot(symbols=["AAPL"]),
            data_quality_snapshot={},
            risk_limits=_risk_limits(),
            sector_map=_sector_map(),
        )
        latest_dir = tmp_path / "latest"
        latest_dir.mkdir()
        history_dir = tmp_path / "history" / "spread_diagnostics"
        memory_dir = tmp_path / "memory"
        memory_dir.mkdir()

        paths = write_spread_diagnostics(snap, latest_dir, history_dir, memory_dir)

        assert Path(paths["latest_path"]).exists()
        assert Path(paths["history_path"]).exists()
        assert Path(paths["dq_log_path"]).exists()

    def test_latest_json_is_valid(self, tmp_path):
        snap = build_spread_diagnostics(
            market_snapshot=_market_snapshot(symbols=["AAPL"]),
            data_quality_snapshot={},
            risk_limits=_risk_limits(),
            sector_map=_sector_map(),
        )
        latest_dir = tmp_path / "latest"
        latest_dir.mkdir()
        history_dir = tmp_path / "history" / "spread_diagnostics"
        memory_dir = tmp_path / "memory"
        memory_dir.mkdir()

        paths = write_spread_diagnostics(snap, latest_dir, history_dir, memory_dir)
        loaded = json.loads(Path(paths["latest_path"]).read_text())
        assert loaded["no_config_was_modified"] is True
        assert loaded["max_spread_pct"] == MAX_SPREAD

    def test_data_quality_log_appended(self, tmp_path):
        snap = build_spread_diagnostics(
            market_snapshot=_market_snapshot(symbols=["AAPL"]),
            data_quality_snapshot={},
            risk_limits=_risk_limits(),
            sector_map=_sector_map(),
        )
        latest_dir = tmp_path / "latest"
        latest_dir.mkdir()
        history_dir = tmp_path / "history" / "spread_diagnostics"
        memory_dir = tmp_path / "memory"
        memory_dir.mkdir()

        dq_log = memory_dir / "DATA-QUALITY-LOG.md"
        dq_log.write_text("## prior entry\n")

        paths = write_spread_diagnostics(snap, latest_dir, history_dir, memory_dir)
        content = Path(paths["dq_log_path"]).read_text()
        assert "prior entry" in content
        assert "Spread Diagnostics" in content


# ---------------------------------------------------------------------------
# TestQuoteAgeBucket (edge cases)
# ---------------------------------------------------------------------------

class TestQuoteAgeBucket:
    def test_quote_age_bucket_fresh(self):
        from trading_os.research.spread_diagnostics import _quote_age_bucket
        assert _quote_age_bucket(2.0) == "fresh_lt5m"

    def test_quote_age_bucket_recent(self):
        from trading_os.research.spread_diagnostics import _quote_age_bucket
        assert _quote_age_bucket(15.0) == "recent_5_30m"

    def test_quote_age_bucket_stale_30_60(self):
        from trading_os.research.spread_diagnostics import _quote_age_bucket
        assert _quote_age_bucket(45.0) == "stale_30_60m"

    def test_quote_age_bucket_stale_gt_60(self):
        from trading_os.research.spread_diagnostics import _quote_age_bucket
        assert _quote_age_bucket(90.0) == "stale_gt_60m"

    def test_quote_age_bucket_unknown_when_none(self):
        from trading_os.research.spread_diagnostics import _quote_age_bucket
        assert _quote_age_bucket(None) == "unknown"
