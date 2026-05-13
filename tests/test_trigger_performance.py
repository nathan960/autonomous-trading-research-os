"""Tests for trigger_performance module.

Verifies:
- skip_reason mapping
- regime stats collection
- symbol trigger stats collection
- fill stats deduplication
- recommendation classification
- no execution path
- no config mutation
"""
from __future__ import annotations

import json
import re
import tempfile
from pathlib import Path

import pytest

from trading_os.research.trigger_performance import (
    MIN_FILL_SAMPLE,
    MIN_SYMBOL_SAMPLE,
    TRIGGER_CATEGORY_MAP,
    _collect_fill_stats,
    _collect_outcome_stats,
    _collect_plan_layer_stats,
    _collect_regime_stats,
    _collect_symbol_trigger_stats,
    _date_range,
    build_trigger_performance,
    classify_recommendation,
    classify_regime_recommendation,
    format_experiment_log_entry,
    skip_reason_to_trigger_id,
    write_trigger_performance,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _make_trigger_snapshot(symbols: dict | None = None) -> dict:
    if symbols is None:
        symbols = {
            "AAPL": {
                "spread": {"trigger_id": "SPREAD_GATE_V1", "spread_pct": 0.001, "passes": True},
                "trend": {"trigger_id": "STOCK_TREND_200DMA_V1", "passes": True},
                "momentum": {"trigger_id": "MOMENTUM_BLEND_6M_12M_V1", "momentum_score": 0.12, "passes": True},
                "liquidity": {"trigger_id": "LIQUIDITY_GATE_V1", "passes": True},
                "atr": {"signal_id": "ATR_SIZING_V1", "atr_pct": 0.015},
            },
            "MSFT": {
                "spread": {"trigger_id": "SPREAD_GATE_V1", "spread_pct": 0.002, "passes": False},
                "trend": {"trigger_id": "STOCK_TREND_200DMA_V1", "passes": False},
                "momentum": {"trigger_id": "MOMENTUM_BLEND_6M_12M_V1", "momentum_score": -0.05, "passes": False},
                "liquidity": {"trigger_id": "LIQUIDITY_GATE_V1", "passes": True},
                "atr": {"signal_id": "ATR_SIZING_V1", "atr_pct": 0.022},
            },
        }
    return {"symbol_results": symbols}


def _make_order_monitor(lifecycles: list, generated_at: str = "2026-05-13T21:00:00Z") -> dict:
    return {
        "generated_at": generated_at,
        "lifecycles": lifecycles,
    }


def _make_lifecycle(cid: str, status: str = "filled", checked_at: str = "2026-05-13T21:00:00Z") -> dict:
    return {
        "client_order_id": cid,
        "symbol": cid.split("-")[-1] if "-" in cid else cid,
        "side": "buy",
        "lifecycle_status": status,
        "checked_at": checked_at,
        "fill": {"fill_price": 100.0, "filled_qty": 1.0, "filled_notional": 100.0},
    }


def _make_trigger_jsonl_line(
    risk_on: bool,
    candidates: list | None = None,
    selected: list | None = None,
    excluded_count: int = 0,
    regime_skip_reason: str | None = None,
) -> str:
    entry: dict = {
        "risk_on": risk_on,
        "candidates": candidates or [],
        "selected": selected or [],
        "excluded_count": excluded_count,
        "scanned_at": "2026-05-13T16:00:00Z",
    }
    if not risk_on and regime_skip_reason:
        entry["regime_skip_reason"] = regime_skip_reason
    return json.dumps(entry)


# ---------------------------------------------------------------------------
# skip_reason_to_trigger_id
# ---------------------------------------------------------------------------

class TestSkipReasonToTriggerId:
    def test_none_returns_none(self):
        assert skip_reason_to_trigger_id(None) is None

    def test_empty_string_returns_none(self):
        assert skip_reason_to_trigger_id("") is None

    def test_close_below_200dma(self):
        assert skip_reason_to_trigger_id("close_below_200dma") == "STOCK_TREND_200DMA_V1"

    def test_spread_too_wide(self):
        assert skip_reason_to_trigger_id("spread_too_wide") == "SPREAD_GATE_V1"

    def test_roc_6m_below_min(self):
        assert skip_reason_to_trigger_id("roc_6m_below_min") == "MOMENTUM_BLEND_6M_12M_V1"

    def test_roc_12m_below_min(self):
        assert skip_reason_to_trigger_id("roc_12m_below_min") == "MOMENTUM_BLEND_6M_12M_V1"

    def test_sector_cap(self):
        assert skip_reason_to_trigger_id("sector_cap") == "SECTOR_CAP"

    def test_max_holdings_reached(self):
        assert skip_reason_to_trigger_id("max_holdings_reached") == "MAX_HOLDINGS"

    def test_capped_by_max_orders_per_run(self):
        assert skip_reason_to_trigger_id("capped_by_max_orders_per_run") == "MAX_ORDERS_PER_RUN"

    def test_max_orders_per_run_cap(self):
        assert skip_reason_to_trigger_id("max_orders_per_run_cap") == "MAX_ORDERS_PER_RUN"

    def test_insufficient_bars(self):
        assert skip_reason_to_trigger_id("insufficient_bars") == "DATA_READINESS"

    def test_not_ready(self):
        assert skip_reason_to_trigger_id("not_ready") == "DATA_READINESS"

    def test_case_insensitive(self):
        assert skip_reason_to_trigger_id("SPREAD_TOO_WIDE") == "SPREAD_GATE_V1"
        assert skip_reason_to_trigger_id("Close_Below_200DMA") == "STOCK_TREND_200DMA_V1"

    def test_substring_match(self):
        assert skip_reason_to_trigger_id("skip: close_below_200dma (symbol AAPL)") == "STOCK_TREND_200DMA_V1"

    def test_unknown_reason_returns_other(self):
        assert skip_reason_to_trigger_id("some_unknown_reason") == "OTHER"

    def test_whitespace_only_returns_none(self):
        assert skip_reason_to_trigger_id("   ") is None


# ---------------------------------------------------------------------------
# classify_recommendation
# ---------------------------------------------------------------------------

class TestClassifyRecommendation:
    def test_spread_gate_high_block_rate_is_operational_issue(self):
        label, reason = classify_recommendation("SPREAD_GATE_V1", "spread_gate", 0.60, 50, 5)
        assert label == "operational_issue"
        assert "60%" in reason

    def test_spread_gate_low_block_rate_passes(self):
        label, _ = classify_recommendation("SPREAD_GATE_V1", "spread_gate", 0.30, 50, 5)
        assert label != "operational_issue"

    def test_data_gate_high_block_rate_is_operational_issue(self):
        label, reason = classify_recommendation("DATA_STALE_GATE_V1", "data_gate", 0.50, 50, 5)
        assert label == "operational_issue"
        assert "50%" in reason

    def test_data_gate_low_block_rate_passes(self):
        label, _ = classify_recommendation("DATA_STALE_GATE_V1", "data_gate", 0.10, 50, 5)
        assert label != "operational_issue"

    def test_insufficient_observations_needs_more_data(self):
        label, reason = classify_recommendation(
            "STOCK_TREND_200DMA_V1", "stock_trend", 0.30,
            MIN_SYMBOL_SAMPLE - 1, 0
        )
        assert label == "needs_more_data"
        assert str(MIN_SYMBOL_SAMPLE) in reason

    def test_sufficient_observations_insufficient_fills(self):
        label, reason = classify_recommendation(
            "STOCK_TREND_200DMA_V1", "stock_trend", 0.30,
            MIN_SYMBOL_SAMPLE, MIN_FILL_SAMPLE - 1
        )
        assert label == "do_not_promote_yet"
        assert str(MIN_FILL_SAMPLE) in reason

    def test_sufficient_data_candidate_for_review(self):
        label, reason = classify_recommendation(
            "STOCK_TREND_200DMA_V1", "stock_trend", 0.30,
            MIN_SYMBOL_SAMPLE, MIN_FILL_SAMPLE
        )
        assert label == "candidate_for_review"
        assert "backtest" in reason.lower() or "review" in reason.lower()

    def test_none_block_rate_not_operational_issue(self):
        label, _ = classify_recommendation("SPREAD_GATE_V1", "spread_gate", None, 50, 5)
        assert label != "operational_issue"

    def test_spread_gate_boundary_50pct_not_issue(self):
        label, _ = classify_recommendation("SPREAD_GATE_V1", "spread_gate", 0.50, 50, 30)
        assert label != "operational_issue"

    def test_spread_gate_boundary_51pct_is_issue(self):
        label, _ = classify_recommendation("SPREAD_GATE_V1", "spread_gate", 0.51, 50, 30)
        assert label == "operational_issue"


# ---------------------------------------------------------------------------
# classify_regime_recommendation
# ---------------------------------------------------------------------------

class TestClassifyRegimeRecommendation:
    def test_few_sessions_keep_observing(self):
        label, reason = classify_regime_recommendation(5)
        assert label == "keep_observing"
        assert "5" in reason

    def test_sufficient_sessions_candidate_for_review(self):
        label, reason = classify_regime_recommendation(MIN_SYMBOL_SAMPLE)
        assert label == "candidate_for_review"
        assert str(MIN_SYMBOL_SAMPLE) in reason

    def test_zero_sessions(self):
        label, _ = classify_regime_recommendation(0)
        assert label == "keep_observing"


# ---------------------------------------------------------------------------
# _collect_regime_stats
# ---------------------------------------------------------------------------

class TestCollectRegimeStats:
    def _write_jsonl(self, directory: Path, date_str: str, lines: list[str]) -> None:
        triggers_dir = directory / "triggers"
        triggers_dir.mkdir(parents=True, exist_ok=True)
        (triggers_dir / f"{date_str}.jsonl").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )

    def test_empty_history_returns_zero_sessions(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = _collect_regime_stats(Path(tmp), ["2026-05-13"])
        assert result["sessions_total"] == 0
        assert result["sessions_risk_on"] == 0
        assert result["trigger_id"] == "SPY_REGIME_200DMA_V1"
        assert result["risk_on_pct"] is None

    def test_all_risk_on(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._write_jsonl(Path(tmp), "2026-05-13", [
                _make_trigger_jsonl_line(risk_on=True, candidates=["A", "B"], selected=["A"]),
                _make_trigger_jsonl_line(risk_on=True, candidates=["C"], selected=["C"]),
            ])
            result = _collect_regime_stats(Path(tmp), ["2026-05-13"])
        assert result["sessions_total"] == 2
        assert result["sessions_risk_on"] == 2
        assert result["sessions_risk_off"] == 0
        assert result["risk_on_pct"] == 1.0

    def test_mixed_risk(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._write_jsonl(Path(tmp), "2026-05-13", [
                _make_trigger_jsonl_line(risk_on=True),
                _make_trigger_jsonl_line(risk_on=False, regime_skip_reason="spy_below_200dma"),
            ])
            result = _collect_regime_stats(Path(tmp), ["2026-05-13"])
        assert result["sessions_total"] == 2
        assert result["sessions_risk_on"] == 1
        assert result["sessions_risk_off"] == 1
        assert result["risk_on_pct"] == 0.5
        assert "spy_below_200dma" in result["regime_errors"]

    def test_multi_day_aggregation(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._write_jsonl(Path(tmp), "2026-05-12", [
                _make_trigger_jsonl_line(risk_on=True),
            ])
            self._write_jsonl(Path(tmp), "2026-05-13", [
                _make_trigger_jsonl_line(risk_on=True),
                _make_trigger_jsonl_line(risk_on=False),
            ])
            result = _collect_regime_stats(Path(tmp), ["2026-05-12", "2026-05-13"])
        assert result["sessions_total"] == 3
        assert result["sessions_risk_on"] == 2

    def test_missing_date_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._write_jsonl(Path(tmp), "2026-05-13", [
                _make_trigger_jsonl_line(risk_on=True),
            ])
            result = _collect_regime_stats(Path(tmp), ["2026-05-11", "2026-05-13"])
        assert result["sessions_total"] == 1

    def test_invalid_jsonl_line_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            triggers_dir = Path(tmp) / "triggers"
            triggers_dir.mkdir()
            (triggers_dir / "2026-05-13.jsonl").write_text(
                'not json\n' + _make_trigger_jsonl_line(risk_on=True) + "\n",
                encoding="utf-8",
            )
            result = _collect_regime_stats(Path(tmp), ["2026-05-13"])
        assert result["sessions_total"] == 1

    def test_regime_errors_capped_at_10(self):
        with tempfile.TemporaryDirectory() as tmp:
            lines = [
                _make_trigger_jsonl_line(risk_on=False, regime_skip_reason=f"reason_{i}")
                for i in range(15)
            ]
            self._write_jsonl(Path(tmp), "2026-05-13", lines)
            result = _collect_regime_stats(Path(tmp), ["2026-05-13"])
        assert len(result["regime_errors"]) == 10


# ---------------------------------------------------------------------------
# _collect_symbol_trigger_stats
# ---------------------------------------------------------------------------

class TestCollectSymbolTriggerStats:
    def test_empty_snapshot_returns_empty(self):
        assert _collect_symbol_trigger_stats({}) == {}

    def test_basic_pass_fail_counts(self):
        snap = _make_trigger_snapshot()
        result = _collect_symbol_trigger_stats(snap)
        spread = result["SPREAD_GATE_V1"]
        assert spread["passed_count"] == 1
        assert spread["blocked_count"] == 1
        assert spread["observation_count"] == 2
        assert spread["block_rate"] == 0.5

    def test_trend_gate_counted(self):
        snap = _make_trigger_snapshot()
        result = _collect_symbol_trigger_stats(snap)
        assert "STOCK_TREND_200DMA_V1" in result
        trend = result["STOCK_TREND_200DMA_V1"]
        assert trend["passed_count"] == 1
        assert trend["blocked_count"] == 1

    def test_momentum_gate_counted(self):
        snap = _make_trigger_snapshot()
        result = _collect_symbol_trigger_stats(snap)
        assert "MOMENTUM_BLEND_6M_12M_V1" in result

    def test_atr_always_passes(self):
        snap = _make_trigger_snapshot()
        result = _collect_symbol_trigger_stats(snap)
        assert "ATR_SIZING_V1" in result
        atr = result["ATR_SIZING_V1"]
        assert atr["blocked_count"] == 0
        assert atr["passed_count"] == 2

    def test_avg_spread_computed(self):
        snap = _make_trigger_snapshot()
        result = _collect_symbol_trigger_stats(snap)
        spread = result["SPREAD_GATE_V1"]
        assert spread.get("avg_spread_passing") == pytest.approx(0.001, rel=1e-4)
        assert spread.get("avg_spread_blocked") == pytest.approx(0.002, rel=1e-4)

    def test_avg_momentum_score_computed(self):
        snap = _make_trigger_snapshot()
        result = _collect_symbol_trigger_stats(snap)
        mom = result["MOMENTUM_BLEND_6M_12M_V1"]
        assert mom.get("avg_momentum_score_passing") == pytest.approx(0.12, rel=1e-4)
        assert mom.get("avg_momentum_score_blocked") == pytest.approx(-0.05, rel=1e-4)

    def test_atr_pct_computed(self):
        snap = _make_trigger_snapshot()
        result = _collect_symbol_trigger_stats(snap)
        atr = result["ATR_SIZING_V1"]
        assert "avg_atr_pct" in atr

    def test_missing_sub_result_skipped(self):
        snap = {"symbol_results": {"AAPL": {"trend": {}}}}
        result = _collect_symbol_trigger_stats(snap)
        assert result == {}

    def test_100pct_block_rate_spread_gate_is_operational_issue(self):
        symbols = {
            f"SYM{i}": {
                "spread": {"trigger_id": "SPREAD_GATE_V1", "spread_pct": 0.01, "passes": False},
            }
            for i in range(10)
        }
        snap = {"symbol_results": symbols}
        result = _collect_symbol_trigger_stats(snap)
        spread = result["SPREAD_GATE_V1"]
        assert spread["recommendation"] == "operational_issue"


# ---------------------------------------------------------------------------
# _collect_plan_layer_stats
# ---------------------------------------------------------------------------

class TestCollectPlanLayerStats:
    def test_empty_plan_returns_empty(self):
        assert _collect_plan_layer_stats({}) == {}

    def test_blocked_symbols_counted(self):
        plan = {
            "blocked_symbols": [
                {"symbol": "A", "skip_reason": "close_below_200dma"},
                {"symbol": "B", "skip_reason": "spread_too_wide"},
                {"symbol": "C", "skip_reason": "close_below_200dma"},
            ]
        }
        result = _collect_plan_layer_stats(plan)
        assert result["STOCK_TREND_200DMA_V1"] == 2
        assert result["SPREAD_GATE_V1"] == 1

    def test_orders_run_capped_counted(self):
        plan = {
            "orders_run_capped_at_planning": [
                {"symbol": "A"},
                {"symbol": "B"},
            ]
        }
        result = _collect_plan_layer_stats(plan)
        assert result["MAX_ORDERS_PER_RUN"] == 2

    def test_unknown_skip_reason_mapped_to_other(self):
        plan = {
            "blocked_symbols": [
                {"symbol": "A", "skip_reason": "unknown_reason"},
            ]
        }
        result = _collect_plan_layer_stats(plan)
        assert result.get("OTHER") == 1

    def test_null_skip_reason_not_counted(self):
        plan = {
            "blocked_symbols": [
                {"symbol": "A", "skip_reason": None},
                {"symbol": "B"},
            ]
        }
        result = _collect_plan_layer_stats(plan)
        assert result == {}


# ---------------------------------------------------------------------------
# _collect_fill_stats
# ---------------------------------------------------------------------------

class TestCollectFillStats:
    def _write_monitor(self, orders_dir: Path, filename: str, lifecycles: list) -> None:
        orders_dir.mkdir(parents=True, exist_ok=True)
        data = _make_order_monitor(lifecycles)
        (orders_dir / filename).write_text(json.dumps(data), encoding="utf-8")

    def test_empty_dir_returns_zero_fills(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = _collect_fill_stats(Path(tmp) / "orders", ["2026-05-13"])
        assert result["total_fills"] == 0
        assert result["total_tracked"] == 0

    def test_basic_fill_counted(self):
        with tempfile.TemporaryDirectory() as tmp:
            orders = Path(tmp) / "orders"
            self._write_monitor(orders, "order_monitor-20260513T210000.json", [
                _make_lifecycle("CID-001", "filled"),
            ])
            result = _collect_fill_stats(orders, ["2026-05-13"])
        assert result["total_fills"] == 1
        assert result["total_tracked"] == 1

    def test_deduplication_keeps_latest(self):
        with tempfile.TemporaryDirectory() as tmp:
            orders = Path(tmp) / "orders"
            self._write_monitor(orders, "order_monitor-20260513T190000.json", [
                _make_lifecycle("CID-001", "missing", checked_at="2026-05-13T19:00:00Z"),
            ])
            self._write_monitor(orders, "order_monitor-20260513T210000.json", [
                _make_lifecycle("CID-001", "filled", checked_at="2026-05-13T21:00:00Z"),
            ])
            result = _collect_fill_stats(orders, ["2026-05-13"])
        assert result["total_fills"] == 1
        assert result["total_tracked"] == 1

    def test_deduplication_not_overwrite_if_earlier(self):
        with tempfile.TemporaryDirectory() as tmp:
            orders = Path(tmp) / "orders"
            self._write_monitor(orders, "order_monitor-20260513T210000.json", [
                _make_lifecycle("CID-001", "filled", checked_at="2026-05-13T21:00:00Z"),
            ])
            self._write_monitor(orders, "order_monitor-20260513T190000.json", [
                _make_lifecycle("CID-001", "missing", checked_at="2026-05-13T19:00:00Z"),
            ])
            result = _collect_fill_stats(orders, ["2026-05-13"])
        assert result["total_fills"] == 1

    def test_non_filled_not_counted_as_fill(self):
        with tempfile.TemporaryDirectory() as tmp:
            orders = Path(tmp) / "orders"
            self._write_monitor(orders, "order_monitor-20260513T210000.json", [
                _make_lifecycle("CID-001", "missing"),
                _make_lifecycle("CID-002", "expired"),
            ])
            result = _collect_fill_stats(orders, ["2026-05-13"])
        assert result["total_fills"] == 0
        assert result["total_tracked"] == 2

    def test_multi_day_aggregation(self):
        with tempfile.TemporaryDirectory() as tmp:
            orders = Path(tmp) / "orders"
            self._write_monitor(orders, "order_monitor-20260512T210000.json", [
                _make_lifecycle("CID-001", "filled"),
            ])
            self._write_monitor(orders, "order_monitor-20260513T210000.json", [
                _make_lifecycle("CID-002", "filled"),
            ])
            result = _collect_fill_stats(orders, ["2026-05-12", "2026-05-13"])
        assert result["total_fills"] == 2

    def test_no_client_order_id_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            orders = Path(tmp) / "orders"
            lc = _make_lifecycle("", "filled")
            lc["client_order_id"] = ""
            self._write_monitor(orders, "order_monitor-20260513T210000.json", [lc])
            result = _collect_fill_stats(orders, ["2026-05-13"])
        assert result["total_fills"] == 0


# ---------------------------------------------------------------------------
# _collect_outcome_stats
# ---------------------------------------------------------------------------

class TestCollectOutcomeStats:
    def test_empty_snapshot(self):
        result = _collect_outcome_stats({})
        assert result["total_outcomes"] == 0
        assert result["sample_status"] == "insufficient_sample"
        assert result["avg_slippage_pct"] is None
        assert result["avg_current_return_pct"] is None

    def test_fills_below_min_threshold(self):
        outcomes = [
            {
                "symbol": "AAPL",
                "slippage_pct": -0.001,
                "current_return_pct": 0.02,
                "fill_price": 150.0,
                "current_price": 153.0,
                "current_unrealized_pl": 3.0,
                "filled_at": "2026-05-13T16:00:00Z",
                "entry_or_exit": "entry",
            }
        ]
        result = _collect_outcome_stats({"outcomes": outcomes})
        assert result["total_outcomes"] == 1
        assert result["sample_status"] == "insufficient_sample"
        assert result["recommendation"] == "needs_more_data"

    def test_avg_slippage_computed(self):
        outcomes = [
            {"symbol": "A", "slippage_pct": 0.001, "current_return_pct": 0.02},
            {"symbol": "B", "slippage_pct": 0.003, "current_return_pct": 0.04},
        ]
        result = _collect_outcome_stats({"outcomes": outcomes})
        assert result["avg_slippage_pct"] == pytest.approx(0.002, rel=1e-4)
        assert result["avg_current_return_pct"] == pytest.approx(0.03, rel=1e-4)

    def test_by_symbol_populated(self):
        outcomes = [
            {"symbol": "WELL", "slippage_pct": -0.001, "current_return_pct": 0.005},
        ]
        result = _collect_outcome_stats({"outcomes": outcomes})
        assert "WELL" in result["by_symbol"]
        assert result["by_symbol"]["WELL"]["slippage_pct"] == -0.001

    def test_null_slippage_ignored_in_avg(self):
        outcomes = [
            {"symbol": "A", "slippage_pct": 0.002, "current_return_pct": None},
            {"symbol": "B", "slippage_pct": None, "current_return_pct": 0.01},
        ]
        result = _collect_outcome_stats({"outcomes": outcomes})
        assert result["avg_slippage_pct"] == pytest.approx(0.002, rel=1e-4)
        assert result["avg_current_return_pct"] == pytest.approx(0.01, rel=1e-4)


# ---------------------------------------------------------------------------
# build_trigger_performance (integration)
# ---------------------------------------------------------------------------

class TestBuildTriggerPerformance:
    def _setup_dirs(self, tmp: str) -> tuple:
        root = Path(tmp)
        latest = root / "latest"
        latest.mkdir()
        history = root / "history"
        (history / "orders").mkdir(parents=True)
        memory = root / "memory"
        memory.mkdir()
        return root, latest, history, memory

    def test_empty_inputs_returns_ok_status(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, latest, history, memory = self._setup_dirs(tmp)
            perf = build_trigger_performance(
                end_date_str="2026-05-13",
                days=7,
                latest_dir=latest,
                history_dir=history,
                memory_dir=memory,
            )
        assert perf["status"] == "ok"
        assert perf["period_end"] == "2026-05-13"
        assert perf["days"] == 7

    def test_required_fields_present(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, latest, history, memory = self._setup_dirs(tmp)
            perf = build_trigger_performance(
                end_date_str="2026-05-13",
                days=7,
                latest_dir=latest,
                history_dir=history,
                memory_dir=memory,
            )
        for key in ("run_id", "generated_at", "period_start", "period_end", "days",
                    "status", "regime", "triggers", "fill_outcomes",
                    "execution_fill_stats", "operational_issues",
                    "research_observations", "safety_note", "performance_hash"):
            assert key in perf, f"missing key: {key}"

    def test_safety_note_present(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, latest, history, memory = self._setup_dirs(tmp)
            perf = build_trigger_performance(
                end_date_str="2026-05-13",
                days=7,
                latest_dir=latest,
                history_dir=history,
                memory_dir=memory,
            )
        assert "research-only" in perf["safety_note"].lower()
        assert "no strategy changes" in perf["safety_note"].lower() or "no config" in perf["safety_note"].lower()

    def test_no_fills_produces_operational_issue(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, latest, history, memory = self._setup_dirs(tmp)
            perf = build_trigger_performance(
                end_date_str="2026-05-13",
                days=7,
                latest_dir=latest,
                history_dir=history,
                memory_dir=memory,
            )
        assert any("fills" in issue.lower() for issue in perf["operational_issues"])

    def test_trigger_snapshot_loaded(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, latest, history, memory = self._setup_dirs(tmp)
            snap = _make_trigger_snapshot()
            (latest / "trigger_snapshot.json").write_text(json.dumps(snap), encoding="utf-8")
            perf = build_trigger_performance(
                end_date_str="2026-05-13",
                days=7,
                latest_dir=latest,
                history_dir=history,
                memory_dir=memory,
            )
        assert "SPREAD_GATE_V1" in perf["triggers"]
        assert "STOCK_TREND_200DMA_V1" in perf["triggers"]

    def test_performance_hash_changes_with_different_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, latest, history, memory = self._setup_dirs(tmp)
            p1 = build_trigger_performance(
                end_date_str="2026-05-12",
                days=7,
                latest_dir=latest,
                history_dir=history,
                memory_dir=memory,
            )
            p2 = build_trigger_performance(
                end_date_str="2026-05-13",
                days=7,
                latest_dir=latest,
                history_dir=history,
                memory_dir=memory,
            )
        assert p1["performance_hash"] != p2["performance_hash"]

    def test_observations_not_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, latest, history, memory = self._setup_dirs(tmp)
            perf = build_trigger_performance(
                end_date_str="2026-05-13",
                days=7,
                latest_dir=latest,
                history_dir=history,
                memory_dir=memory,
            )
        assert len(perf["research_observations"]) > 0

    def test_no_strategy_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, latest, history, memory = self._setup_dirs(tmp)
            perf = build_trigger_performance(
                end_date_str="2026-05-13",
                days=7,
                latest_dir=latest,
                history_dir=history,
                memory_dir=memory,
            )
        for forbidden in ("approved_for_execution", "enable_live_trading", "trade_plan"):
            assert forbidden not in perf


# ---------------------------------------------------------------------------
# write_trigger_performance
# ---------------------------------------------------------------------------

class TestWriteTriggerPerformance:
    def _make_perf(self) -> dict:
        return {
            "run_id": "trigger_performance-20260513T195351-abc12345",
            "generated_at": "2026-05-13T19:53:51Z",
            "period_start": "2026-05-07",
            "period_end": "2026-05-13",
            "days": 7,
            "status": "ok",
            "regime": {"sessions_total": 2, "sessions_risk_on": 2},
            "triggers": {},
            "fill_outcomes": {"total_outcomes": 0},
            "execution_fill_stats": {"total_fills": 0, "total_tracked": 0},
            "operational_issues": [],
            "research_observations": ["Test observation."],
            "safety_note": "Research only.",
            "performance_hash": "abcdef1234567890",
        }

    def test_latest_file_written(self):
        with tempfile.TemporaryDirectory() as tmp:
            latest = Path(tmp) / "latest"
            latest.mkdir()
            tp_hist = Path(tmp) / "history" / "trigger_performance"
            memory = Path(tmp) / "memory"
            memory.mkdir()
            paths = write_trigger_performance(
                self._make_perf(),
                latest_dir=latest,
                tp_history_dir=tp_hist,
                memory_dir=memory,
            )
            assert Path(paths["latest_path"]).exists()
            data = json.loads(Path(paths["latest_path"]).read_text())
            assert data["run_id"] == "trigger_performance-20260513T195351-abc12345"

    def test_history_file_written(self):
        with tempfile.TemporaryDirectory() as tmp:
            latest = Path(tmp) / "latest"
            latest.mkdir()
            tp_hist = Path(tmp) / "history" / "trigger_performance"
            memory = Path(tmp) / "memory"
            memory.mkdir()
            paths = write_trigger_performance(
                self._make_perf(),
                latest_dir=latest,
                tp_history_dir=tp_hist,
                memory_dir=memory,
            )
            assert Path(paths["history_path"]).exists()
            assert "trigger_performance_2026-05-13" in paths["history_path"]

    def test_experiment_log_appended(self):
        with tempfile.TemporaryDirectory() as tmp:
            latest = Path(tmp) / "latest"
            latest.mkdir()
            tp_hist = Path(tmp) / "history" / "trigger_performance"
            memory = Path(tmp) / "memory"
            memory.mkdir()
            paths = write_trigger_performance(
                self._make_perf(),
                latest_dir=latest,
                tp_history_dir=tp_hist,
                memory_dir=memory,
            )
            exp_path = paths.get("experiment_log_path")
            assert exp_path is not None
            content = Path(exp_path).read_text()
            assert "Test observation." in content

    def test_idempotent_write_appends_log(self):
        perf = self._make_perf()
        with tempfile.TemporaryDirectory() as tmp:
            latest = Path(tmp) / "latest"
            latest.mkdir()
            tp_hist = Path(tmp) / "history" / "trigger_performance"
            memory = Path(tmp) / "memory"
            memory.mkdir()
            write_trigger_performance(perf, latest_dir=latest, tp_history_dir=tp_hist, memory_dir=memory)
            write_trigger_performance(perf, latest_dir=latest, tp_history_dir=tp_hist, memory_dir=memory)
            exp_log = memory / "EXPERIMENT-LOG.md"
            count = exp_log.read_text().count("trigger_performance-20260513T195351-abc12345")
        assert count == 2

    def test_no_observations_no_experiment_log(self):
        perf = self._make_perf()
        perf["research_observations"] = []
        perf["operational_issues"] = []
        with tempfile.TemporaryDirectory() as tmp:
            latest = Path(tmp) / "latest"
            latest.mkdir()
            tp_hist = Path(tmp) / "history" / "trigger_performance"
            memory = Path(tmp) / "memory"
            memory.mkdir()
            paths = write_trigger_performance(
                perf,
                latest_dir=latest,
                tp_history_dir=tp_hist,
                memory_dir=memory,
            )
            assert paths.get("experiment_log_path") is None


# ---------------------------------------------------------------------------
# format_experiment_log_entry
# ---------------------------------------------------------------------------

class TestFormatExperimentLogEntry:
    def test_none_if_no_issues_or_observations(self):
        perf = {
            "operational_issues": [],
            "research_observations": [],
            "period_end": "2026-05-13",
            "period_start": "2026-05-07",
            "days": 7,
            "run_id": "test-run",
        }
        assert format_experiment_log_entry(perf) is None

    def test_returns_string_with_observations(self):
        perf = {
            "operational_issues": [],
            "research_observations": ["Observation one."],
            "period_end": "2026-05-13",
            "period_start": "2026-05-07",
            "days": 7,
            "run_id": "test-run",
        }
        result = format_experiment_log_entry(perf)
        assert result is not None
        assert "Observation one." in result

    def test_contains_safety_reminder(self):
        perf = {
            "operational_issues": ["Some issue."],
            "research_observations": [],
            "period_end": "2026-05-13",
            "period_start": "2026-05-07",
            "days": 7,
            "run_id": "test-run",
        }
        result = format_experiment_log_entry(perf)
        assert "strategy.json" in result or "risk_limits" in result

    def test_operational_issues_use_checkbox(self):
        perf = {
            "operational_issues": ["Issue A.", "Issue B."],
            "research_observations": [],
            "period_end": "2026-05-13",
            "period_start": "2026-05-07",
            "days": 7,
            "run_id": "test-run",
        }
        result = format_experiment_log_entry(perf)
        assert "- [ ] Issue A." in result
        assert "- [ ] Issue B." in result


# ---------------------------------------------------------------------------
# No execution path
# ---------------------------------------------------------------------------

class TestNoExecutionPath:
    def test_module_does_not_import_execute_paper(self):
        import trading_os.research.trigger_performance as mod
        source = Path(mod.__file__).read_text(encoding="utf-8")
        assert not re.search(r"^\s*(import|from)\s+.*execute_paper", source, re.MULTILINE)

    def test_module_does_not_import_order_submission(self):
        import trading_os.research.trigger_performance as mod
        source = Path(mod.__file__).read_text(encoding="utf-8")
        assert "submit_order" not in source
        assert "place_order" not in source

    def test_build_does_not_write_strategy_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            latest = root / "latest"
            latest.mkdir()
            history = root / "history"
            (history / "orders").mkdir(parents=True)
            memory = root / "memory"
            memory.mkdir()
            strategy_path = root / "config" / "strategy.json"
            (root / "config").mkdir()
            strategy_path.write_text('{"original": true}')
            build_trigger_performance(
                end_date_str="2026-05-13",
                days=7,
                latest_dir=latest,
                history_dir=history,
                memory_dir=memory,
            )
            assert json.loads(strategy_path.read_text()) == {"original": True}

    def test_write_does_not_mutate_strategy_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            latest = root / "latest"
            latest.mkdir()
            tp_hist = root / "history" / "trigger_performance"
            memory = root / "memory"
            memory.mkdir()
            strategy_path = root / "config" / "strategy.json"
            (root / "config").mkdir()
            strategy_path.write_text('{"v": 1}')
            perf = {
                "run_id": "test",
                "generated_at": "2026-05-13T00:00:00Z",
                "period_start": "2026-05-07",
                "period_end": "2026-05-13",
                "days": 7,
                "status": "ok",
                "performance_hash": "abcdef12",
                "operational_issues": [],
                "research_observations": [],
            }
            write_trigger_performance(perf, latest_dir=latest, tp_history_dir=tp_hist, memory_dir=memory)
            assert json.loads(strategy_path.read_text()) == {"v": 1}

    def test_approved_for_execution_not_in_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            latest = root / "latest"
            latest.mkdir()
            history = root / "history"
            (history / "orders").mkdir(parents=True)
            memory = root / "memory"
            memory.mkdir()
            perf = build_trigger_performance(
                end_date_str="2026-05-13",
                days=7,
                latest_dir=latest,
                history_dir=history,
                memory_dir=memory,
            )
        assert "approved_for_execution" not in perf
        assert "approved_for_execution" not in json.dumps(perf)


# ---------------------------------------------------------------------------
# _date_range helper
# ---------------------------------------------------------------------------

class TestDateRange:
    def test_single_day(self):
        result = _date_range("2026-05-13", 1)
        assert result == ["2026-05-13"]

    def test_seven_days(self):
        result = _date_range("2026-05-13", 7)
        assert len(result) == 7
        assert result[0] == "2026-05-07"
        assert result[-1] == "2026-05-13"

    def test_ascending_order(self):
        result = _date_range("2026-05-13", 5)
        assert result == sorted(result)


# ---------------------------------------------------------------------------
# TRIGGER_CATEGORY_MAP coverage
# ---------------------------------------------------------------------------

class TestTriggerCategoryMap:
    def test_all_known_triggers_have_category(self):
        known = [
            "SPY_REGIME_200DMA_V1", "DATA_STALE_GATE_V1", "STOCK_TREND_200DMA_V1",
            "MOMENTUM_BLEND_6M_12M_V1", "LIQUIDITY_GATE_V1", "SPREAD_GATE_V1",
            "ATR_SIZING_V1", "SECTOR_CAP", "MAX_HOLDINGS", "MAX_ORDERS_PER_RUN",
            "DATA_READINESS", "OTHER",
        ]
        for tid in known:
            assert tid in TRIGGER_CATEGORY_MAP, f"{tid} missing from TRIGGER_CATEGORY_MAP"

    def test_each_entry_is_two_tuple(self):
        for tid, value in TRIGGER_CATEGORY_MAP.items():
            assert isinstance(value, tuple) and len(value) == 2, f"{tid}: expected 2-tuple"
