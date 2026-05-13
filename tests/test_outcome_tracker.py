"""Tests for src/trading_os/research/outcome_tracker.py.

Safety invariants proved:
- Filled order creates an outcome record with correct fields.
- Duplicate monitor reports do not duplicate outcome records.
- Pending windows remain pending when checked immediately after fill.
- Unrealized P/L is attached when a matching position exists.
- Missing position is handled safely (no KeyError / no crash).
- Side=sell produces entry_or_exit="exit".
- No execution functions are called by this module.
- config/strategy.json and risk_limits.json are never written.
- execute_paper is never imported or referenced.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

import pytest

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.research.outcome_tracker import (
    _compute_outcome_windows,
    _compute_slippage,
    _get_current_price,
    _get_position,
    build_outcome_record,
    build_outcome_snapshot,
    load_existing_outcomes,
    write_outcome_snapshot,
)


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------

def _lifecycle(
    client_order_id: str = "TOS-20260513T160035-WELL-BUY",
    broker_order_id: str = "broker-abc123",
    symbol: str = "WELL",
    side: str = "buy",
    limit_price: float = 218.9,
    lifecycle_status: str = "filled",
    fill_price: float = 218.808,
    filled_qty: float = 0.11425542,
    filled_notional: float = 25.0,
    filled_at: str = "2026-05-13T16:00:36Z",
    plan_id: str = "trade_plan-20260513T160035-0460e121",
    run_id: str = "execution-20260513T160036-b4ad22c3",
    trade_plan_hash: str = "abc123",
    trigger_snapshot_hash: str | None = None,
) -> dict:
    return {
        "client_order_id": client_order_id,
        "broker_order_id": broker_order_id,
        "symbol": symbol,
        "side": side,
        "limit_price": limit_price,
        "lifecycle_status": lifecycle_status,
        "notional": filled_notional,
        "submitted_at": filled_at,
        "fill": {
            "fill_price": fill_price,
            "filled_qty": filled_qty,
            "filled_notional": filled_notional,
            "filled_at": filled_at,
            "plan_id": plan_id,
            "run_id": run_id,
            "trade_plan_hash": trade_plan_hash,
            "trigger_snapshot_hash": trigger_snapshot_hash,
            "position_confirmed": True,
        },
    }


def _position(
    symbol: str = "WELL",
    qty: float = 0.11425542,
    current_price: float = 220.85,
    market_value: float = 25.23,
    unrealized_pl: float = 0.23,
    unrealized_plpc: float = 0.00933,
) -> dict:
    return {
        "symbol": symbol,
        "qty": str(qty),
        "current_price": str(current_price),
        "market_value": str(market_value),
        "unrealized_pl": str(unrealized_pl),
        "unrealized_plpc": str(unrealized_plpc),
        "side": "long",
    }


def _market_snapshot(prices: dict | None = None) -> dict:
    """Build a minimal market_snapshot. prices = {symbol: close_price}."""
    prices = prices or {
        "WELL": 220.85,
        "SPY": 743.265,
        "BIL": 91.495,
    }
    latest_bars = {
        sym: {"close": price, "symbol": sym, "timestamp": "2026-05-13T19:32:00Z"}
        for sym, price in prices.items()
    }
    return {"latest_bars": latest_bars, "quotes": {}}


def _monitor_report(lifecycles: list, generated_at: str = "2026-05-13T19:32:15Z") -> dict:
    return {
        "run_id": "order_monitor-test",
        "generated_at": generated_at,
        "orders_filled": sum(1 for lc in lifecycles if lc.get("lifecycle_status") == "filled"),
        "orders_missing": 0,
        "orders_tracked": len(lifecycles),
        "lifecycles": lifecycles,
        "safety": {
            "submit_order_called": False,
            "cancel_order_called": False,
            "replace_order_called": False,
        },
    }


def _write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data), encoding="utf-8")


# ---------------------------------------------------------------------------
# _get_current_price
# ---------------------------------------------------------------------------

class TestGetCurrentPrice:
    def test_returns_close_from_latest_bars(self):
        ms = _market_snapshot({"WELL": 220.85})
        assert _get_current_price("WELL", ms) == 220.85

    def test_returns_none_when_symbol_missing(self):
        assert _get_current_price("UNKNOWN", _market_snapshot()) is None

    def test_falls_back_to_quote_mid(self):
        ms = {"latest_bars": {}, "quotes": {"AAPL": {"bid_price": 200.0, "ask_price": 202.0}}}
        assert _get_current_price("AAPL", ms) == 201.0

    def test_empty_snapshot_returns_none(self):
        assert _get_current_price("WELL", {}) is None


# ---------------------------------------------------------------------------
# _compute_slippage
# ---------------------------------------------------------------------------

class TestComputeSlippage:
    def test_negative_slippage_for_buy_below_limit(self):
        slip, pct = _compute_slippage(218.808, 218.9)
        assert slip is not None and slip < 0
        assert pct is not None and pct < 0

    def test_zero_slippage_exact_fill(self):
        slip, pct = _compute_slippage(100.0, 100.0)
        assert slip == 0.0

    def test_none_when_fill_price_missing(self):
        assert _compute_slippage(None, 100.0) == (None, None)

    def test_none_when_limit_price_missing(self):
        assert _compute_slippage(100.0, None) == (None, None)

    def test_none_when_limit_zero(self):
        assert _compute_slippage(100.0, 0.0) == (None, None)


# ---------------------------------------------------------------------------
# _compute_outcome_windows
# ---------------------------------------------------------------------------

class TestComputeOutcomeWindows:
    def test_all_pending_when_just_filled(self):
        windows = _compute_outcome_windows(
            "2026-05-13T16:00:36Z", "2026-05-13T19:32:15Z"
        )
        assert all(v["status"] == "pending" for v in windows.values())

    def test_same_day_elapsed_next_calendar_day(self):
        windows = _compute_outcome_windows(
            "2026-05-13T16:00:00Z", "2026-05-14T12:00:00Z"
        )
        assert windows["same_day"]["status"] == "elapsed"
        # 1-day window still pending (< 1.3 days elapsed)
        assert windows["1_trading_day"]["status"] == "pending"

    def test_1d_elapsed_after_2_calendar_days(self):
        windows = _compute_outcome_windows(
            "2026-05-13T16:00:00Z", "2026-05-15T20:00:00Z"
        )
        assert windows["1_trading_day"]["status"] == "elapsed"
        assert windows["5_trading_days"]["status"] == "pending"

    def test_5d_elapsed_after_8_calendar_days(self):
        windows = _compute_outcome_windows(
            "2026-05-13T16:00:00Z", "2026-05-21T20:00:00Z"
        )
        assert windows["5_trading_days"]["status"] == "elapsed"
        assert windows["20_trading_days"]["status"] == "pending"

    def test_all_elapsed_after_100_days(self):
        windows = _compute_outcome_windows(
            "2026-01-01T16:00:00Z", "2026-04-20T16:00:00Z"
        )
        assert all(v["status"] == "elapsed" for v in windows.values())

    def test_missing_timestamps_all_pending(self):
        windows = _compute_outcome_windows("", "")
        assert all(v["status"] == "pending" for v in windows.values())

    def test_window_keys_present(self):
        windows = _compute_outcome_windows(
            "2026-05-13T16:00:00Z", "2026-05-13T19:00:00Z"
        )
        for key in ("same_day", "1_trading_day", "5_trading_days", "20_trading_days", "63_trading_days"):
            assert key in windows


# ---------------------------------------------------------------------------
# build_outcome_record
# ---------------------------------------------------------------------------

class TestBuildOutcomeRecord:
    CHECKED_AT = "2026-05-13T19:32:15Z"

    def test_creates_record_for_filled_order(self):
        lc = _lifecycle()
        record = build_outcome_record(lc, [], _market_snapshot(), self.CHECKED_AT)
        assert record["client_order_id"] == "TOS-20260513T160035-WELL-BUY"
        assert record["symbol"] == "WELL"
        assert record["lifecycle_status"] == "filled"

    def test_buy_is_entry(self):
        record = build_outcome_record(_lifecycle(side="buy"), [], _market_snapshot(), self.CHECKED_AT)
        assert record["entry_or_exit"] == "entry"

    def test_sell_is_exit(self):
        record = build_outcome_record(_lifecycle(side="sell"), [], _market_snapshot(), self.CHECKED_AT)
        assert record["entry_or_exit"] == "exit"

    def test_fill_fields_populated(self):
        record = build_outcome_record(_lifecycle(), [], _market_snapshot(), self.CHECKED_AT)
        assert record["fill_price"] == 218.808
        assert record["filled_qty"] == pytest.approx(0.11425542)
        assert record["filled_notional"] == 25.0
        assert record["filled_at"] == "2026-05-13T16:00:36Z"

    def test_plan_refs_populated(self):
        record = build_outcome_record(_lifecycle(), [], _market_snapshot(), self.CHECKED_AT)
        assert record["plan_id"] == "trade_plan-20260513T160035-0460e121"
        assert record["run_id"] == "execution-20260513T160036-b4ad22c3"
        assert record["trade_plan_hash"] == "abc123"

    def test_slippage_computed(self):
        record = build_outcome_record(_lifecycle(fill_price=218.808, limit_price=218.9), [], _market_snapshot(), self.CHECKED_AT)
        assert record["slippage_vs_limit"] is not None
        assert record["slippage_vs_limit"] < 0

    def test_unrealized_return_computed(self):
        ms = _market_snapshot({"WELL": 220.85, "SPY": 743.0, "BIL": 91.5})
        record = build_outcome_record(_lifecycle(fill_price=218.808), [], ms, self.CHECKED_AT)
        assert record["current_return_pct"] is not None
        assert record["current_return_pct"] > 0

    def test_position_data_attached_when_present(self):
        positions = [_position(symbol="WELL", current_price=220.85, unrealized_pl=0.23)]
        record = build_outcome_record(_lifecycle(), positions, _market_snapshot(), self.CHECKED_AT)
        assert record["current_price"] is not None
        assert record["current_unrealized_pl"] is not None
        assert record["current_position_qty"] is not None
        assert record["current_market_value"] is not None
        assert record["current_unrealized_pl_pct"] is not None

    def test_missing_position_handled_safely(self):
        record = build_outcome_record(_lifecycle(symbol="AAPL"), [], _market_snapshot(), self.CHECKED_AT)
        assert record["current_position_qty"] is None
        assert record["current_unrealized_pl"] is None
        assert record["current_market_value"] is None

    def test_current_price_falls_back_to_market_snapshot(self):
        ms = _market_snapshot({"WELL": 220.85, "SPY": 743.0, "BIL": 91.5})
        record = build_outcome_record(_lifecycle(), [], ms, self.CHECKED_AT)
        assert record["current_price"] == 220.85

    def test_spy_and_bil_benchmarks_populated(self):
        ms = _market_snapshot({"WELL": 220.85, "SPY": 743.265, "BIL": 91.495})
        record = build_outcome_record(_lifecycle(), [], ms, self.CHECKED_AT)
        assert record["spy_price_at_check"] == 743.265
        assert record["bil_price_at_check"] == 91.495

    def test_benchmark_none_when_not_in_snapshot(self):
        ms = _market_snapshot({"WELL": 220.85})
        record = build_outcome_record(_lifecycle(), [], ms, self.CHECKED_AT)
        assert record["spy_price_at_check"] is None
        assert record["bil_price_at_check"] is None

    def test_outcome_windows_all_pending_same_day(self):
        record = build_outcome_record(_lifecycle(), [], _market_snapshot(), self.CHECKED_AT)
        windows = record["outcome_windows"]
        assert all(v["status"] == "pending" for v in windows.values())

    def test_first_seen_at_preserved(self):
        first = "2026-05-13T16:00:00Z"
        record = build_outcome_record(_lifecycle(), [], _market_snapshot(), self.CHECKED_AT, first_seen_at=first)
        assert record["first_seen_at"] == first

    def test_first_seen_at_defaults_to_checked_at(self):
        record = build_outcome_record(_lifecycle(), [], _market_snapshot(), self.CHECKED_AT)
        assert record["first_seen_at"] == self.CHECKED_AT

    def test_no_crash_on_empty_market_snapshot(self):
        record = build_outcome_record(_lifecycle(), [], {}, self.CHECKED_AT)
        assert record["current_price"] is None
        assert record["spy_price_at_check"] is None


# ---------------------------------------------------------------------------
# build_outcome_snapshot
# ---------------------------------------------------------------------------

class TestBuildOutcomeSnapshot:
    CHECKED_AT = "2026-05-13T19:32:15Z"

    def _snap(self, lifecycles, positions=None, prices=None, existing=None, generated_at=None):
        report = _monitor_report(lifecycles, generated_at=generated_at or self.CHECKED_AT)
        positions_snap = {"positions": positions or []}
        ms = _market_snapshot(prices or {"WELL": 220.85, "SPY": 743.0, "BIL": 91.5})
        return build_outcome_snapshot(report, positions_snap, ms, existing_outcomes=existing)

    def test_filled_order_creates_record(self):
        snap = self._snap([_lifecycle()])
        assert snap["outcomes_count"] == 1
        assert snap["outcomes"][0]["symbol"] == "WELL"

    def test_missing_lifecycle_excluded(self):
        lc = _lifecycle()
        lc["lifecycle_status"] = "missing"
        lc["fill"] = None
        snap = self._snap([lc])
        assert snap["outcomes_count"] == 0

    def test_active_lifecycle_excluded(self):
        lc = _lifecycle()
        lc["lifecycle_status"] = "new"
        snap = self._snap([lc])
        assert snap["outcomes_count"] == 0

    def test_partially_filled_included(self):
        lc = _lifecycle()
        lc["lifecycle_status"] = "partially_filled"
        snap = self._snap([lc])
        assert snap["outcomes_count"] == 1

    def test_duplicate_monitor_reports_do_not_duplicate_records(self):
        lc = _lifecycle()
        report1 = _monitor_report([lc], generated_at="2026-05-13T17:00:00Z")
        report2 = _monitor_report([lc], generated_at="2026-05-13T19:00:00Z")
        positions_snap = {"positions": []}
        ms = _market_snapshot()

        snap1 = build_outcome_snapshot(report1, positions_snap, ms)
        existing = {r["client_order_id"]: r for r in snap1["outcomes"]}
        snap2 = build_outcome_snapshot(report2, positions_snap, ms, existing_outcomes=existing)
        assert snap2["outcomes_count"] == 1

    def test_newer_checked_at_replaces_older(self):
        lc = _lifecycle()
        report_old = _monitor_report([lc], generated_at="2026-05-13T17:00:00Z")
        report_new = _monitor_report([lc], generated_at="2026-05-13T19:00:00Z")
        positions_snap = {"positions": []}
        ms = _market_snapshot()

        snap_old = build_outcome_snapshot(report_old, positions_snap, ms)
        existing = {r["client_order_id"]: r for r in snap_old["outcomes"]}
        snap_new = build_outcome_snapshot(report_new, positions_snap, ms, existing_outcomes=existing)
        assert snap_new["outcomes"][0]["checked_at"] == "2026-05-13T19:00:00Z"

    def test_multiple_unique_orders(self):
        lc1 = _lifecycle(client_order_id="TOS-WELL", symbol="WELL")
        lc2 = _lifecycle(client_order_id="TOS-JNJ", symbol="JNJ")
        snap = self._snap([lc1, lc2])
        assert snap["outcomes_count"] == 2
        symbols = {o["symbol"] for o in snap["outcomes"]}
        assert symbols == {"WELL", "JNJ"}

    def test_snapshot_has_required_fields(self):
        snap = self._snap([_lifecycle()])
        for key in ("run_id", "generated_at", "outcomes_count", "outcomes", "snapshot_hash"):
            assert key in snap

    def test_snapshot_hash_16_chars(self):
        snap = self._snap([_lifecycle()])
        assert len(snap["snapshot_hash"]) == 16

    def test_existing_outcomes_preserved_when_not_in_new_report(self):
        existing_record = build_outcome_record(
            _lifecycle(client_order_id="TOS-OLD", symbol="KO"),
            [],
            _market_snapshot(),
            "2026-05-12T19:00:00Z",
        )
        existing = {"TOS-OLD": existing_record}
        snap = self._snap([_lifecycle()], existing=existing)
        assert snap["outcomes_count"] == 2
        symbols = {o["symbol"] for o in snap["outcomes"]}
        assert "KO" in symbols and "WELL" in symbols

    def test_first_seen_at_preserved_across_updates(self):
        lc = _lifecycle()
        first_snap = self._snap([lc], generated_at="2026-05-13T17:00:00Z")
        original_first_seen = first_snap["outcomes"][0]["first_seen_at"]

        existing = {r["client_order_id"]: r for r in first_snap["outcomes"]}
        second_snap = self._snap([lc], existing=existing, generated_at="2026-05-13T19:00:00Z")
        assert second_snap["outcomes"][0]["first_seen_at"] == original_first_seen

    def test_unrealized_pl_attached_when_position_exists(self):
        pos = _position(symbol="WELL", unrealized_pl=0.23, unrealized_plpc=0.00933)
        snap = self._snap([_lifecycle()], positions=[pos])
        assert snap["outcomes"][0]["current_unrealized_pl"] == pytest.approx(0.23, abs=0.01)

    def test_missing_position_does_not_crash(self):
        snap = self._snap([_lifecycle(symbol="AAPL")], positions=[])
        assert snap["outcomes"][0]["current_unrealized_pl"] is None

    def test_empty_monitor_report_produces_empty_snapshot(self):
        snap = self._snap([])
        assert snap["outcomes_count"] == 0


# ---------------------------------------------------------------------------
# load_existing_outcomes
# ---------------------------------------------------------------------------

class TestLoadExistingOutcomes:
    def test_empty_when_file_absent(self, tmp_path):
        result = load_existing_outcomes(tmp_path)
        assert result == {}

    def test_empty_when_file_malformed(self, tmp_path):
        (tmp_path / "outcome_snapshot.json").write_text("not json", encoding="utf-8")
        result = load_existing_outcomes(tmp_path)
        assert result == {}

    def test_loads_keyed_by_client_order_id(self, tmp_path):
        snap = {
            "outcomes": [
                {"client_order_id": "TOS-WELL", "symbol": "WELL"},
                {"client_order_id": "TOS-JNJ", "symbol": "JNJ"},
            ]
        }
        (tmp_path / "outcome_snapshot.json").write_text(json.dumps(snap), encoding="utf-8")
        result = load_existing_outcomes(tmp_path)
        assert "TOS-WELL" in result
        assert "TOS-JNJ" in result
        assert result["TOS-WELL"]["symbol"] == "WELL"

    def test_skips_records_without_client_order_id(self, tmp_path):
        snap = {"outcomes": [{"symbol": "WELL"}]}  # no client_order_id
        (tmp_path / "outcome_snapshot.json").write_text(json.dumps(snap), encoding="utf-8")
        result = load_existing_outcomes(tmp_path)
        assert result == {}


# ---------------------------------------------------------------------------
# write_outcome_snapshot
# ---------------------------------------------------------------------------

class TestWriteOutcomeSnapshot:
    def _build_snap(self) -> dict:
        lc = _lifecycle()
        report = _monitor_report([lc])
        positions_snap = {"positions": [_position()]}
        ms = _market_snapshot()
        return build_outcome_snapshot(report, positions_snap, ms)

    def test_writes_latest_outcome_snapshot(self, tmp_path):
        snap = self._build_snap()
        latest = tmp_path / "latest"
        latest.mkdir()
        outcomes_dir = tmp_path / "outcomes"
        mem = tmp_path / "memory"
        mem.mkdir()
        (mem / "TRADE-LOG.md").write_text("# Trade Log\n", encoding="utf-8")
        paths = write_outcome_snapshot(snap, latest, outcomes_dir, mem)
        assert Path(paths["latest_path"]).exists()
        assert "outcome_snapshot.json" in paths["latest_path"]

    def test_writes_history_outcome_file(self, tmp_path):
        snap = self._build_snap()
        latest = tmp_path / "latest"
        latest.mkdir()
        outcomes_dir = tmp_path / "outcomes"
        mem = tmp_path / "memory"
        mem.mkdir()
        (mem / "TRADE-LOG.md").write_text("# Trade Log\n", encoding="utf-8")
        paths = write_outcome_snapshot(snap, latest, outcomes_dir, mem)
        assert Path(paths["history_path"]).exists()
        assert "outcome_" in Path(paths["history_path"]).name

    def test_appends_to_trade_log(self, tmp_path):
        snap = self._build_snap()
        latest = tmp_path / "latest"
        latest.mkdir()
        outcomes_dir = tmp_path / "outcomes"
        mem = tmp_path / "memory"
        mem.mkdir()
        (mem / "TRADE-LOG.md").write_text("# Trade Log\n", encoding="utf-8")
        write_outcome_snapshot(snap, latest, outcomes_dir, mem)
        content = (mem / "TRADE-LOG.md").read_text(encoding="utf-8")
        assert "Outcome Tracker" in content
        assert "WELL" in content

    def test_appends_to_experiment_log_when_returns_present(self, tmp_path):
        snap = self._build_snap()
        latest = tmp_path / "latest"
        latest.mkdir()
        outcomes_dir = tmp_path / "outcomes"
        mem = tmp_path / "memory"
        mem.mkdir()
        (mem / "TRADE-LOG.md").write_text("# Trade Log\n", encoding="utf-8")
        (mem / "EXPERIMENT-LOG.md").write_text("# Experiment Log\n", encoding="utf-8")
        paths = write_outcome_snapshot(snap, latest, outcomes_dir, mem)
        if paths.get("experiment_log_path"):
            content = Path(paths["experiment_log_path"]).read_text(encoding="utf-8")
            assert "Outcome Observations" in content

    def test_creates_outcomes_dir_if_absent(self, tmp_path):
        snap = self._build_snap()
        latest = tmp_path / "latest"
        latest.mkdir()
        outcomes_dir = tmp_path / "deep" / "outcomes"
        mem = tmp_path / "memory"
        mem.mkdir()
        (mem / "TRADE-LOG.md").write_text("# Trade Log\n", encoding="utf-8")
        paths = write_outcome_snapshot(snap, latest, outcomes_dir, mem)
        assert Path(paths["history_path"]).exists()

    def test_written_json_is_valid(self, tmp_path):
        snap = self._build_snap()
        latest = tmp_path / "latest"
        latest.mkdir()
        outcomes_dir = tmp_path / "outcomes"
        mem = tmp_path / "memory"
        mem.mkdir()
        (mem / "TRADE-LOG.md").write_text("# Trade Log\n", encoding="utf-8")
        paths = write_outcome_snapshot(snap, latest, outcomes_dir, mem)
        data = json.loads(Path(paths["latest_path"]).read_text(encoding="utf-8"))
        assert data["outcomes_count"] == 1
        assert data["outcomes"][0]["symbol"] == "WELL"


# ---------------------------------------------------------------------------
# Safety — no execution path
# ---------------------------------------------------------------------------

class TestOutcomeTrackerNoExecutionPath:
    def test_module_does_not_import_execute_paper(self):
        import trading_os.research.outcome_tracker as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        assert not re.search(r'^\s*(import|from)\s+.*execute_paper', src, re.MULTILINE)
        assert not re.search(r'subprocess\.[^(]+\([^)]*execute_paper', src)

    def test_module_does_not_call_subprocess(self):
        import trading_os.research.outcome_tracker as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        assert "subprocess" not in src

    def test_module_never_writes_strategy_or_risk_limits(self):
        import trading_os.research.outcome_tracker as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        assert not re.search(r'strategy\.json.*write|write.*strategy\.json', src)
        assert not re.search(r'risk_limits\.json.*write|write.*risk_limits\.json', src)

    def test_module_never_sets_approved_for_execution(self):
        import trading_os.research.outcome_tracker as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        assert not re.search(r'approved_for_execution\s*=\s*True', src)

    def test_module_never_calls_submit_cancel_replace(self):
        import trading_os.research.outcome_tracker as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        for forbidden in ("submit_order(", "cancel_order(", "replace_order("):
            assert forbidden not in src, f"module must not call {forbidden!r}"

    def test_script_does_not_call_execute_paper(self):
        script = Path(__file__).parents[1] / "scripts" / "track_outcomes.py"
        src = script.read_text(encoding="utf-8")
        assert "execute_paper" not in src

    def test_script_never_sets_approved_for_execution(self):
        script = Path(__file__).parents[1] / "scripts" / "track_outcomes.py"
        src = script.read_text(encoding="utf-8")
        assert not re.search(r'approved_for_execution\s*=\s*True', src)
