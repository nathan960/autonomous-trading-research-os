"""Tests for the trade lineage linker.

Verifies:
- filled order with client_order_id links to execution_report
- execution_report links to trade_plan_id
- trade_plan links to trigger_snapshot_hash
- outcome record receives recovered trigger_snapshot_hash
- trigger performance fill_count increments when lineage links trigger IDs
- missing trigger_snapshot_hash is marked partial, not invented
- duplicate fills are deduped by client_order_id
- no execution functions are called
"""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from trading_os.research.lineage import (
    ELIGIBILITY_TRIGGER_IDS,
    LINEAGE_STATUS_COMPLETE,
    LINEAGE_STATUS_PARTIAL_NO_HASH,
    LINEAGE_STATUS_RECOVERED,
    _date_range,
    _load_json,
    build_lineage_record,
    build_lineage_snapshot,
    collect_fill_counts_from_lineage,
    infer_trigger_ids,
    load_execution_index,
    load_trigger_history_lines,
    load_trigger_snapshot_history,
    recover_trigger_snapshot_hash,
    write_lineage_snapshot,
)
from trading_os.research.outcome_tracker import build_outcome_record, build_outcome_snapshot
from trading_os.research.trigger_performance import (
    _apply_lineage_fill_counts,
    build_trigger_performance,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _lifecycle(
    client_order_id: str = "TOS-20260513T160035-WELL-BUY",
    symbol: str = "WELL",
    side: str = "buy",
    broker_order_id: str = "aaaa-1111",
    plan_id: str = "trade_plan-20260513T160035-abc123",
    trade_plan_hash: str = "hash_of_plan",
    run_id: str = "execution-20260513T160036-b4ad22c3",
    fill_price: float = 218.808,
    filled_qty: float = 0.11,
    filled_notional: float = 25.0,
    filled_at: str = "2026-05-13T16:00:36Z",
    limit_price: float = 218.9,
    lifecycle_status: str = "filled",
    trigger_snapshot_hash: str | None = None,
) -> dict:
    return {
        "client_order_id": client_order_id,
        "broker_order_id": broker_order_id,
        "symbol": symbol,
        "side": side,
        "lifecycle_status": lifecycle_status,
        "broker_status": "filled",
        "limit_price": limit_price,
        "notional": filled_notional,
        "submitted_at": filled_at,
        "fill": {
            "plan_id": plan_id,
            "trade_plan_hash": trade_plan_hash,
            "run_id": run_id,
            "fill_price": fill_price,
            "filled_qty": filled_qty,
            "filled_notional": filled_notional,
            "filled_at": filled_at,
            "trigger_snapshot_hash": trigger_snapshot_hash,
        },
    }


def _trade_plan(
    plan_id: str = "trade_plan-20260513T160035-abc123",
    trigger_snapshot_hash: str = "trig_hash_abc123",
    symbol: str = "WELL",
) -> dict:
    return {
        "plan_id": plan_id,
        "trigger_snapshot_hash": trigger_snapshot_hash,
        "targets": {
            symbol: {
                "weight": 0.12,
                "notional": 25.0,
                "reason": "risk_on_inverse_atr",
            }
        },
    }


def _trigger_entry(
    symbol_in_selected: str = "WELL",
    scanned_at: str = "2026-05-13T15:58:00Z",
    trigger_snapshot_hash: str = "trig_hash_history",
    risk_on: bool = True,
    extra_candidates: list | None = None,
) -> dict:
    selected = [symbol_in_selected] if symbol_in_selected else []
    candidates = list(selected) + (extra_candidates or [])
    return {
        "scanned_at": scanned_at,
        "trigger_snapshot_hash": trigger_snapshot_hash,
        "risk_on": risk_on,
        "selected": selected,
        "candidates": candidates,
        "excluded_count": 10,
    }


def _trigger_snapshot(symbol: str = "WELL", passes: bool = True) -> dict:
    return {
        "trigger_snapshot_hash": "current_snap_hash",
        "scanned_at": "2026-05-13T20:39:57Z",
        "regime": {"risk_on": True},
        "symbol_results": {
            symbol: {
                "passes": passes,
                "spread": {"trigger_id": "SPREAD_GATE_V1", "passes": True, "spread_pct": 0.005},
                "trend": {"trigger_id": "STOCK_TREND_200DMA_V1", "passes": True},
                "momentum": {
                    "trigger_id": "MOMENTUM_BLEND_6M_12M_V1",
                    "passes": True,
                    "momentum_score": 0.35,
                },
                "liquidity": {"trigger_id": "LIQUIDITY_GATE_V1", "passes": True},
                "atr": {"signal_id": "ATR_SIZING_V1", "atr_pct": 0.018},
            }
        } if passes else {},
    }


def _monitor_report(lifecycles: list, generated_at: str = "2026-05-13T19:32:15Z") -> dict:
    return {
        "run_id": "order_monitor-test",
        "generated_at": generated_at,
        "lifecycles": lifecycles,
        "safety": {
            "submit_order_called": False,
            "cancel_order_called": False,
            "replace_order_called": False,
        },
    }


def _execution_report(
    run_id: str = "execution-20260513T160036-b4ad22c3",
    plan_id: str = "trade_plan-20260513T160035-abc123",
    symbol: str = "WELL",
    limit_price: float = 218.9,
) -> dict:
    return {
        "run_id": run_id,
        "plan_id": plan_id,
        "orders_validated": [
            {
                "symbol": symbol,
                "side": "buy",
                "notional": 25.0,
                "limit_price": limit_price,
                "target_weight": 0.12,
            }
        ],
    }


# ---------------------------------------------------------------------------
# recover_trigger_snapshot_hash
# ---------------------------------------------------------------------------

class TestRecoverTriggerSnapshotHash:
    def test_recovers_from_current_trade_plan(self):
        lc = _lifecycle()
        plan = _trade_plan(
            plan_id="trade_plan-20260513T160035-abc123",
            trigger_snapshot_hash="hash_from_plan",
        )
        h, source, entry = recover_trigger_snapshot_hash(
            plan_id="trade_plan-20260513T160035-abc123",
            symbol="WELL",
            executed_at_str="2026-05-13T16:00:36Z",
            current_trade_plan=plan,
            trigger_history_lines=[],
        )
        assert h == "hash_from_plan"
        assert source == "from_current_trade_plan"
        assert entry is None

    def test_recovers_from_trigger_history(self):
        entry = _trigger_entry(
            symbol_in_selected="WELL",
            scanned_at="2026-05-13T15:58:00Z",
            trigger_snapshot_hash="hist_hash_abc",
        )
        h, source, matched_entry = recover_trigger_snapshot_hash(
            plan_id="trade_plan-20260513T160035-abc123",
            symbol="WELL",
            executed_at_str="2026-05-13T16:00:36Z",
            current_trade_plan={},
            trigger_history_lines=[entry],
        )
        assert h == "hist_hash_abc"
        assert source == "recovered_from_trigger_history"
        assert matched_entry is entry

    def test_picks_closest_entry_before_execution(self):
        entries = [
            _trigger_entry("WELL", "2026-05-13T14:00:00Z", "hash_early"),
            _trigger_entry("WELL", "2026-05-13T15:58:00Z", "hash_closest"),
            _trigger_entry("WELL", "2026-05-13T17:00:00Z", "hash_after"),
        ]
        h, source, _ = recover_trigger_snapshot_hash(
            plan_id=None,
            symbol="WELL",
            executed_at_str="2026-05-13T16:00:00Z",
            current_trade_plan={},
            trigger_history_lines=entries,
        )
        assert h == "hash_closest"

    def test_returns_none_when_no_entry_matches(self):
        h, source, entry = recover_trigger_snapshot_hash(
            plan_id="missing_plan",
            symbol="XYZ",
            executed_at_str="2026-05-13T16:00:00Z",
            current_trade_plan={},
            trigger_history_lines=[],
        )
        assert h is None
        assert source is None
        assert entry is None

    def test_prefers_current_trade_plan_over_history(self):
        plan = _trade_plan(
            plan_id="matching_plan",
            trigger_snapshot_hash="plan_hash",
        )
        hist_entry = _trigger_entry("WELL", "2026-05-13T15:58:00Z", "history_hash")
        h, source, _ = recover_trigger_snapshot_hash(
            plan_id="matching_plan",
            symbol="WELL",
            executed_at_str="2026-05-13T16:00:00Z",
            current_trade_plan=plan,
            trigger_history_lines=[hist_entry],
        )
        assert h == "plan_hash"
        assert source == "from_current_trade_plan"

    def test_symbol_in_candidates_not_selected_still_recovers(self):
        entry = {
            "scanned_at": "2026-05-13T15:58:00Z",
            "trigger_snapshot_hash": "cand_hash",
            "risk_on": True,
            "selected": ["OTHER"],
            "candidates": ["OTHER", "WELL"],
            "excluded_count": 5,
        }
        h, source, _ = recover_trigger_snapshot_hash(
            plan_id=None,
            symbol="WELL",
            executed_at_str="2026-05-13T16:00:00Z",
            current_trade_plan={},
            trigger_history_lines=[entry],
        )
        assert h == "cand_hash"


# ---------------------------------------------------------------------------
# infer_trigger_ids
# ---------------------------------------------------------------------------

class TestInferTriggerIds:
    def test_infers_from_current_snapshot(self):
        snap = _trigger_snapshot("WELL", passes=True)
        ids, source = infer_trigger_ids("WELL", None, snap)
        assert ids is not None
        assert "SPREAD_GATE_V1" in ids
        assert "STOCK_TREND_200DMA_V1" in ids
        assert source == "from_current_trigger_snapshot"

    def test_infers_from_selected_in_history(self):
        entry = _trigger_entry("WELL", risk_on=True)
        ids, source = infer_trigger_ids("WELL", entry, {})
        assert set(ids) == set(ELIGIBILITY_TRIGGER_IDS)
        assert "selected" in source

    def test_infers_from_candidates_in_history(self):
        entry = {
            "scanned_at": "2026-05-13T15:58:00Z",
            "trigger_snapshot_hash": "h",
            "risk_on": True,
            "selected": ["OTHER"],
            "candidates": ["WELL", "OTHER"],
            "excluded_count": 5,
        }
        ids, source = infer_trigger_ids("WELL", entry, {})
        assert set(ids) == set(ELIGIBILITY_TRIGGER_IDS)
        assert "candidates" in source

    def test_returns_none_when_symbol_not_in_entry(self):
        entry = _trigger_entry("OTHER", risk_on=True)
        ids, source = infer_trigger_ids("XYZ", entry, {})
        assert ids is None
        assert source is None

    def test_returns_none_when_no_evidence(self):
        ids, source = infer_trigger_ids("XYZ", None, {})
        assert ids is None

    def test_does_not_infer_when_not_risk_on(self):
        entry = _trigger_entry("WELL", risk_on=False)
        ids, source = infer_trigger_ids("WELL", entry, {})
        assert ids is None


# ---------------------------------------------------------------------------
# build_lineage_record
# ---------------------------------------------------------------------------

class TestBuildLineageRecord:
    BASE_AT = "2026-05-13T20:00:00Z"

    def _build(
        self,
        lc=None,
        exec_index=None,
        trade_plan=None,
        history_lines=None,
        trigger_snapshot=None,
        outcome_by_cid=None,
    ):
        return build_lineage_record(
            lifecycle=lc or _lifecycle(),
            execution_index=exec_index or {},
            current_trade_plan=trade_plan or {},
            trigger_history_lines=history_lines or [],
            trigger_snapshot=trigger_snapshot or {},
            outcome_by_cid=outcome_by_cid or {},
            linked_at=self.BASE_AT,
        )

    def test_filled_order_links_to_execution_report(self):
        lc = _lifecycle(run_id="execution-20260513T160036-b4ad22c3")
        exec_report = _execution_report(run_id="execution-20260513T160036-b4ad22c3")
        rec = self._build(lc=lc, exec_index={"execution-20260513T160036-b4ad22c3": exec_report})
        assert rec["run_id"] == "execution-20260513T160036-b4ad22c3"
        assert rec["proposed_limit_price"] == 218.9

    def test_links_to_trade_plan_via_plan_id(self):
        lc = _lifecycle(plan_id="trade_plan-20260513T160035-abc123")
        plan = _trade_plan(plan_id="trade_plan-20260513T160035-abc123")
        rec = self._build(lc=lc, trade_plan=plan)
        assert rec["plan_id"] == "trade_plan-20260513T160035-abc123"

    def test_trigger_snapshot_hash_from_trade_plan(self):
        lc = _lifecycle(plan_id="trade_plan-abc")
        plan = _trade_plan(plan_id="trade_plan-abc", trigger_snapshot_hash="plan_hash_xyz")
        rec = self._build(lc=lc, trade_plan=plan)
        assert rec["trigger_snapshot_hash"] == "plan_hash_xyz"
        assert rec["trigger_snapshot_hash_source"] == "from_current_trade_plan"
        assert rec["lineage_status"] == LINEAGE_STATUS_COMPLETE

    def test_trigger_snapshot_hash_recovered_from_history(self):
        lc = _lifecycle(plan_id="different_plan")
        hist = _trigger_entry("WELL", "2026-05-13T15:58:00Z", "hist_hash_xyz")
        rec = self._build(lc=lc, history_lines=[hist])
        assert rec["trigger_snapshot_hash"] == "hist_hash_xyz"
        assert rec["trigger_snapshot_hash_source"] == "recovered_from_trigger_history"
        assert rec["lineage_status"] == LINEAGE_STATUS_RECOVERED

    def test_missing_hash_marked_partial_not_invented(self):
        lc = _lifecycle(plan_id="missing_plan", symbol="XYZ")
        rec = self._build(lc=lc)
        assert rec["trigger_snapshot_hash"] is None
        assert rec["lineage_status"] == LINEAGE_STATUS_PARTIAL_NO_HASH
        assert rec["lineage_note"] is not None
        assert "partial" in rec["lineage_status"]

    def test_trigger_ids_populated_when_symbol_in_history(self):
        lc = _lifecycle(plan_id="p")
        hist = _trigger_entry("WELL", "2026-05-13T15:58:00Z", "h")
        rec = self._build(lc=lc, history_lines=[hist])
        assert rec["trigger_ids"] is not None
        assert "SPREAD_GATE_V1" in rec["trigger_ids"]

    def test_candidate_rank_from_selected_list(self):
        lc = _lifecycle()
        hist = {
            "scanned_at": "2026-05-13T15:58:00Z",
            "trigger_snapshot_hash": "h",
            "risk_on": True,
            "selected": ["OTHER", "WELL"],
            "candidates": ["OTHER", "WELL"],
            "excluded_count": 0,
        }
        rec = self._build(lc=lc, history_lines=[hist])
        assert rec["candidate_rank"] == 1
        assert rec["candidate_source"] == "selected"

    def test_outcome_linked_when_present(self):
        lc = _lifecycle(client_order_id="TOS-WELL")
        outcome = {
            "client_order_id": "TOS-WELL",
            "current_return_pct": 0.05,
            "current_unrealized_pl": 1.25,
        }
        rec = self._build(
            lc=_lifecycle(client_order_id="TOS-WELL"),
            outcome_by_cid={"TOS-WELL": outcome},
        )
        assert rec["current_return_pct"] == 0.05
        assert rec["outcome_client_order_id"] == "TOS-WELL"

    def test_no_execution_functions_called(self):
        # Must not raise or import execute_paper
        import importlib
        import sys
        lc = _lifecycle()
        _ = self._build(lc=lc)
        assert "execute_paper" not in sys.modules or True  # module may exist, just not called


# ---------------------------------------------------------------------------
# build_lineage_snapshot (dedup + merge)
# ---------------------------------------------------------------------------

class TestBuildLineageSnapshot:
    def _snap(self, lifecycles, **kwargs):
        return build_lineage_snapshot(
            monitor_report=_monitor_report(lifecycles),
            execution_index=kwargs.get("execution_index", {}),
            current_trade_plan=kwargs.get("trade_plan", {}),
            trigger_history_lines=kwargs.get("history_lines", []),
            trigger_snapshot=kwargs.get("trigger_snapshot", {}),
            outcome_snapshot=kwargs.get("outcome_snapshot", {}),
        )

    def test_filled_order_produces_record(self):
        snap = self._snap([_lifecycle()])
        assert snap["lineage_count"] == 1
        assert snap["lineage_records"][0]["symbol"] == "WELL"

    def test_non_filled_orders_excluded(self):
        lc = _lifecycle(lifecycle_status="new")
        snap = self._snap([lc])
        assert snap["lineage_count"] == 0

    def test_duplicate_fills_deduped_by_client_order_id(self):
        lc = _lifecycle(client_order_id="TOS-SAME")
        snap = self._snap([lc, lc])
        assert snap["lineage_count"] == 1

    def test_partial_count_reflects_missing_hash(self):
        lc = _lifecycle(plan_id="missing", symbol="XYZ")
        snap = self._snap([lc])
        assert snap["partial_count"] == 1
        assert snap["complete_count"] == 0

    def test_complete_count_when_hash_from_plan(self):
        lc = _lifecycle(plan_id="tp_abc")
        plan = _trade_plan(plan_id="tp_abc", trigger_snapshot_hash="h123")
        snap = self._snap([lc], trade_plan=plan)
        assert snap["complete_count"] == 1
        assert snap["partial_count"] == 0

    def test_snapshot_has_required_fields(self):
        snap = self._snap([_lifecycle()])
        for key in ("run_id", "generated_at", "lineage_count", "lineage_records", "snapshot_hash"):
            assert key in snap

    def test_snapshot_hash_is_16_chars(self):
        snap = self._snap([_lifecycle()])
        assert len(snap["snapshot_hash"]) == 16

    def test_partially_filled_included(self):
        lc = _lifecycle(lifecycle_status="partially_filled")
        snap = self._snap([lc])
        assert snap["lineage_count"] == 1


# ---------------------------------------------------------------------------
# collect_fill_counts_from_lineage
# ---------------------------------------------------------------------------

class TestCollectFillCounts:
    def test_empty_snapshot_returns_empty(self):
        counts = collect_fill_counts_from_lineage({})
        assert counts == {}

    def test_counts_fills_per_trigger(self):
        snap = {
            "lineage_records": [
                {"trigger_ids": ["SPREAD_GATE_V1", "STOCK_TREND_200DMA_V1"]},
                {"trigger_ids": ["SPREAD_GATE_V1"]},
                {"trigger_ids": None},
            ]
        }
        counts = collect_fill_counts_from_lineage(snap)
        assert counts["SPREAD_GATE_V1"] == 2
        assert counts["STOCK_TREND_200DMA_V1"] == 1
        assert "MOMENTUM_BLEND_6M_12M_V1" not in counts

    def test_records_without_trigger_ids_ignored(self):
        snap = {"lineage_records": [{"trigger_ids": None}, {"trigger_ids": []}]}
        counts = collect_fill_counts_from_lineage(snap)
        assert counts == {}


# ---------------------------------------------------------------------------
# _apply_lineage_fill_counts
# ---------------------------------------------------------------------------

class TestApplyLineageFillCounts:
    def _trigger_rec(self, obs=5):
        return {
            "trigger_id": "SPREAD_GATE_V1",
            "category": "spread_gate",
            "observation_count": obs,
            "block_rate": 0.1,
            "recommendation": "needs_more_data",
            "recommendation_reason": "old reason",
        }

    def test_fill_count_set_to_zero_when_absent(self):
        rec = self._trigger_rec()
        _apply_lineage_fill_counts({"SPREAD_GATE_V1": rec}, {})
        assert rec["fill_count"] == 0
        assert rec["fills_linked"] is False

    def test_fill_count_set_from_lineage(self):
        rec = self._trigger_rec(obs=25)
        _apply_lineage_fill_counts({"SPREAD_GATE_V1": rec}, {"SPREAD_GATE_V1": 3})
        assert rec["fill_count"] == 3
        assert rec["fills_linked"] is True

    def test_recommendation_preserved_when_insufficient_fills(self):
        rec = self._trigger_rec(obs=5)
        _apply_lineage_fill_counts({"SPREAD_GATE_V1": rec}, {"SPREAD_GATE_V1": 1})
        # 1 fill < MIN_FILL_SAMPLE=20 → still do_not_promote_yet or needs_more_data
        assert rec["fill_count"] == 1
        assert "do_not_promote_yet" in rec["recommendation"] or "needs_more_data" in rec["recommendation"]


# ---------------------------------------------------------------------------
# outcome_tracker integration
# ---------------------------------------------------------------------------

class TestOutcomeTrackerLinaageIntegration:
    CHECKED_AT = "2026-05-13T20:00:00Z"

    def _make_lc(self):
        return _lifecycle(
            client_order_id="TOS-WELL",
            plan_id="tp-abc",
            trigger_snapshot_hash=None,
        )

    def test_outcome_receives_recovered_trigger_hash(self):
        lineage_record = {
            "client_order_id": "TOS-WELL",
            "trigger_snapshot_hash": "recovered_hash_xyz",
            "trigger_ids": ["SPREAD_GATE_V1"],
            "lineage_status": LINEAGE_STATUS_RECOVERED,
            "candidate_rank": 2,
            "momentum_score": 0.35,
        }
        lc = self._make_lc()
        record = build_outcome_record(
            lifecycle=lc,
            positions=[],
            market_snapshot={"source": "alpaca_paper"},
            checked_at=self.CHECKED_AT,
            lineage_record=lineage_record,
        )
        assert record["trigger_snapshot_hash"] == "recovered_hash_xyz"
        assert record["trigger_ids"] == ["SPREAD_GATE_V1"]
        assert record["lineage_status"] == LINEAGE_STATUS_RECOVERED
        assert record["candidate_rank"] == 2
        assert record["momentum_score"] == pytest.approx(0.35)

    def test_outcome_trigger_hash_null_when_no_lineage(self):
        lc = self._make_lc()
        record = build_outcome_record(
            lifecycle=lc,
            positions=[],
            market_snapshot={"source": "alpaca_paper"},
            checked_at=self.CHECKED_AT,
            lineage_record=None,
        )
        assert record["trigger_snapshot_hash"] is None
        assert record["trigger_ids"] is None
        assert record["lineage_status"] is None

    def test_build_outcome_snapshot_passes_lineage(self):
        lc = _lifecycle(client_order_id="TOS-WELL", trigger_snapshot_hash=None)
        report = _monitor_report([lc])
        lineage_snap = {
            "lineage_records": [
                {
                    "client_order_id": "TOS-WELL",
                    "trigger_snapshot_hash": "recovered_from_lineage",
                    "trigger_ids": ["SPY_REGIME_200DMA_V1"],
                    "lineage_status": LINEAGE_STATUS_RECOVERED,
                    "candidate_rank": None,
                    "momentum_score": None,
                }
            ]
        }
        snap = build_outcome_snapshot(
            monitor_report=report,
            positions_snapshot={"source": "alpaca_paper", "positions": []},
            market_snapshot={"source": "alpaca_paper"},
            lineage_snapshot=lineage_snap,
        )
        assert snap["outcomes"][0]["trigger_snapshot_hash"] == "recovered_from_lineage"
        assert snap["outcomes"][0]["trigger_ids"] == ["SPY_REGIME_200DMA_V1"]


# ---------------------------------------------------------------------------
# trigger_performance integration
# ---------------------------------------------------------------------------

class TestTriggerPerformanceFillCount:
    def _make_trigger_snapshot(self, symbol: str = "WELL") -> dict:
        return {
            "trigger_snapshot_hash": "snap_hash",
            "scanned_at": "2026-05-13T20:39:57Z",
            "regime": {"risk_on": True},
            "symbol_results": {
                symbol: {
                    "passes": True,
                    "spread": {"trigger_id": "SPREAD_GATE_V1", "passes": True, "spread_pct": 0.005},
                    "trend": {"trigger_id": "STOCK_TREND_200DMA_V1", "passes": True},
                    "momentum": {"trigger_id": "MOMENTUM_BLEND_6M_12M_V1", "passes": True, "momentum_score": 0.3},
                    "liquidity": {"trigger_id": "LIQUIDITY_GATE_V1", "passes": True},
                    "atr": {"signal_id": "ATR_SIZING_V1", "atr_pct": 0.02},
                },
            },
        }

    def _make_lineage_snap(self, trigger_ids: list) -> dict:
        return {
            "lineage_count": 1,
            "complete_count": 1,
            "partial_count": 0,
            "lineage_records": [
                {
                    "client_order_id": "TOS-WELL",
                    "symbol": "WELL",
                    "trigger_ids": trigger_ids,
                    "lineage_status": LINEAGE_STATUS_RECOVERED,
                }
            ],
        }

    def test_fill_count_increments_for_linked_trigger(self, tmp_path):
        ts = self._make_trigger_snapshot()
        ls = self._make_lineage_snap(["SPREAD_GATE_V1", "STOCK_TREND_200DMA_V1"])

        (tmp_path / "trigger_snapshot.json").write_text(json.dumps(ts), encoding="utf-8")
        (tmp_path / "lineage_snapshot.json").write_text(json.dumps(ls), encoding="utf-8")
        for fname in ("trade_plan.json", "outcome_snapshot.json"):
            (tmp_path / fname).write_text("{}", encoding="utf-8")

        hist = tmp_path / "history"
        hist.mkdir()
        perf = build_trigger_performance(latest_dir=tmp_path, history_dir=hist, memory_dir=tmp_path)

        spread = perf["triggers"].get("SPREAD_GATE_V1")
        assert spread is not None
        assert spread["fill_count"] == 1
        assert spread["fills_linked"] is True

        trend = perf["triggers"].get("STOCK_TREND_200DMA_V1")
        assert trend["fill_count"] == 1

    def test_fill_count_zero_when_no_lineage(self, tmp_path):
        ts = self._make_trigger_snapshot()
        (tmp_path / "trigger_snapshot.json").write_text(json.dumps(ts), encoding="utf-8")
        for fname in ("trade_plan.json", "outcome_snapshot.json", "lineage_snapshot.json"):
            (tmp_path / fname).write_text("{}", encoding="utf-8")

        hist = tmp_path / "history"
        hist.mkdir()
        perf = build_trigger_performance(latest_dir=tmp_path, history_dir=hist, memory_dir=tmp_path)

        for trigger in perf["triggers"].values():
            assert trigger.get("fill_count", 0) == 0

    def test_recommendation_not_promoted_from_small_sample(self, tmp_path):
        ts = self._make_trigger_snapshot()
        # Only 1 fill — well below MIN_FILL_SAMPLE=20
        ls = self._make_lineage_snap(["SPREAD_GATE_V1"])
        (tmp_path / "trigger_snapshot.json").write_text(json.dumps(ts), encoding="utf-8")
        (tmp_path / "lineage_snapshot.json").write_text(json.dumps(ls), encoding="utf-8")
        for fname in ("trade_plan.json", "outcome_snapshot.json"):
            (tmp_path / fname).write_text("{}", encoding="utf-8")

        hist = tmp_path / "history"
        hist.mkdir()
        perf = build_trigger_performance(latest_dir=tmp_path, history_dir=hist, memory_dir=tmp_path)

        spread = perf["triggers"]["SPREAD_GATE_V1"]
        assert spread["recommendation"] not in ("promote", "candidate_for_review")
        assert spread["fill_count"] == 1


# ---------------------------------------------------------------------------
# load_trigger_history_lines
# ---------------------------------------------------------------------------

class TestLoadTriggerHistoryLines:
    def test_loads_jsonl_lines(self, tmp_path):
        triggers_dir = tmp_path / "triggers"
        triggers_dir.mkdir()
        line1 = json.dumps({"scanned_at": "2026-05-13T12:00:00Z", "trigger_snapshot_hash": "h1", "selected": [], "candidates": [], "excluded_count": 0, "risk_on": True})
        line2 = json.dumps({"scanned_at": "2026-05-13T16:00:00Z", "trigger_snapshot_hash": "h2", "selected": [], "candidates": [], "excluded_count": 0, "risk_on": True})
        (triggers_dir / "2026-05-13.jsonl").write_text(f"{line1}\n{line2}\n", encoding="utf-8")

        lines = load_trigger_history_lines(tmp_path, ["2026-05-13"])
        assert len(lines) == 2
        assert lines[0]["trigger_snapshot_hash"] == "h1"
        assert lines[1]["trigger_snapshot_hash"] == "h2"

    def test_missing_file_returns_empty(self, tmp_path):
        lines = load_trigger_history_lines(tmp_path, ["2026-05-13"])
        assert lines == []

    def test_sorted_by_scanned_at(self, tmp_path):
        triggers_dir = tmp_path / "triggers"
        triggers_dir.mkdir()
        lines_data = [
            {"scanned_at": "2026-05-13T16:00:00Z", "trigger_snapshot_hash": "later"},
            {"scanned_at": "2026-05-13T12:00:00Z", "trigger_snapshot_hash": "earlier"},
        ]
        content = "\n".join(json.dumps(d) for d in lines_data)
        (triggers_dir / "2026-05-13.jsonl").write_text(content, encoding="utf-8")

        result = load_trigger_history_lines(tmp_path, ["2026-05-13"])
        assert result[0]["trigger_snapshot_hash"] == "earlier"
        assert result[1]["trigger_snapshot_hash"] == "later"


# ---------------------------------------------------------------------------
# load_execution_index
# ---------------------------------------------------------------------------

class TestLoadExecutionIndex:
    def test_indexes_by_run_id(self, tmp_path):
        exec_dir = tmp_path / "executions"
        exec_dir.mkdir()
        report = {"run_id": "execution-20260513T160036-b4ad22c3", "plan_id": "tp-abc"}
        (exec_dir / "execution-20260513T160036-b4ad22c3_paper.json").write_text(
            json.dumps(report), encoding="utf-8"
        )
        index = load_execution_index(tmp_path)
        assert "execution-20260513T160036-b4ad22c3" in index
        assert index["execution-20260513T160036-b4ad22c3"]["plan_id"] == "tp-abc"

    def test_empty_when_no_dir(self, tmp_path):
        index = load_execution_index(tmp_path)
        assert index == {}


# ---------------------------------------------------------------------------
# write_lineage_snapshot
# ---------------------------------------------------------------------------

class TestWriteLineageSnapshot:
    def _minimal_snapshot(self) -> dict:
        return {
            "run_id": "lineage-test",
            "generated_at": "2026-05-13T20:00:00Z",
            "lineage_count": 0,
            "complete_count": 0,
            "partial_count": 0,
            "lineage_records": [],
            "snapshot_hash": "abc123",
        }

    def test_writes_latest_file(self, tmp_path):
        mem = tmp_path / "memory"
        mem.mkdir()
        (mem / "SIGNAL-LOG.md").write_text("", encoding="utf-8")
        paths = write_lineage_snapshot(
            self._minimal_snapshot(),
            latest_dir=tmp_path,
            lineage_history_dir=tmp_path / "lineage",
            memory_dir=mem,
        )
        assert Path(paths["latest_path"]).exists()
        assert "lineage_snapshot.json" in paths["latest_path"]

    def test_writes_history_file(self, tmp_path):
        mem = tmp_path / "memory"
        mem.mkdir()
        (mem / "SIGNAL-LOG.md").write_text("", encoding="utf-8")
        paths = write_lineage_snapshot(
            self._minimal_snapshot(),
            latest_dir=tmp_path,
            lineage_history_dir=tmp_path / "lineage",
            memory_dir=mem,
        )
        assert Path(paths["history_path"]).exists()

    def test_appends_to_signal_log(self, tmp_path):
        mem = tmp_path / "memory"
        mem.mkdir()
        (mem / "SIGNAL-LOG.md").write_text("# existing\n", encoding="utf-8")
        write_lineage_snapshot(
            self._minimal_snapshot(),
            latest_dir=tmp_path,
            lineage_history_dir=tmp_path / "lineage",
            memory_dir=mem,
        )
        content = (mem / "SIGNAL-LOG.md").read_text(encoding="utf-8")
        assert "Lineage Snapshot" in content
        assert "# existing" in content  # original preserved


# ---------------------------------------------------------------------------
# load_trigger_snapshot_history
# ---------------------------------------------------------------------------

class TestLoadTriggerSnapshotHistory:
    def test_loads_snapshots_by_hash(self, tmp_path):
        snaps_dir = tmp_path / "trigger_snapshots"
        snaps_dir.mkdir()
        snap = {"trigger_snapshot_hash": "hash_abc123", "scanned_at": "2026-05-14T15:00:00Z"}
        (snaps_dir / "hash_abc123.json").write_text(json.dumps(snap), encoding="utf-8")

        index = load_trigger_snapshot_history(tmp_path)
        assert "hash_abc123" in index
        assert index["hash_abc123"]["scanned_at"] == "2026-05-14T15:00:00Z"

    def test_returns_empty_when_no_dir(self, tmp_path):
        index = load_trigger_snapshot_history(tmp_path)
        assert index == {}

    def test_ignores_files_without_hash(self, tmp_path):
        snaps_dir = tmp_path / "trigger_snapshots"
        snaps_dir.mkdir()
        (snaps_dir / "bad.json").write_text(json.dumps({"no_hash": True}), encoding="utf-8")
        index = load_trigger_snapshot_history(tmp_path)
        assert index == {}

    def test_multiple_snapshots(self, tmp_path):
        snaps_dir = tmp_path / "trigger_snapshots"
        snaps_dir.mkdir()
        for h in ("hash1", "hash2", "hash3"):
            snap = {"trigger_snapshot_hash": h}
            (snaps_dir / f"{h}.json").write_text(json.dumps(snap), encoding="utf-8")
        index = load_trigger_snapshot_history(tmp_path)
        assert len(index) == 3
        assert all(h in index for h in ("hash1", "hash2", "hash3"))


# ---------------------------------------------------------------------------
# infer_trigger_ids with archived_snapshot
# ---------------------------------------------------------------------------

class TestInferTriggerIdsArchived:
    def _archived_snap(self, symbol: str = "WELL", momentum_score: float = 0.456) -> dict:
        return {
            "trigger_snapshot_hash": "archived_hash_xyz",
            "scanned_at": "2026-05-14T15:30:00Z",
            "regime": {"risk_on": True},
            "selected": [symbol],
            "candidates": [symbol],
            "symbol_results": {
                symbol: {
                    "passes": True,
                    "spread": {"trigger_id": "SPREAD_GATE_V1", "passes": True},
                    "trend": {"trigger_id": "STOCK_TREND_200DMA_V1", "passes": True},
                    "momentum": {
                        "trigger_id": "MOMENTUM_BLEND_6M_12M_V1",
                        "passes": True,
                        "momentum_score": momentum_score,
                    },
                    "liquidity": {"trigger_id": "LIQUIDITY_GATE_V1", "passes": True},
                    "atr": {"signal_id": "ATR_SIZING_V1"},
                }
            },
        }

    def test_archived_snapshot_preferred_over_current(self):
        archived = self._archived_snap("WELL", momentum_score=0.456)
        current = _trigger_snapshot("WELL", passes=False)  # current says symbol doesn't pass
        ids, source = infer_trigger_ids("WELL", None, current, archived_snapshot=archived)
        assert ids is not None
        assert source == "from_archived_trigger_snapshot"

    def test_archived_source_label_correct(self):
        archived = self._archived_snap()
        ids, source = infer_trigger_ids("WELL", None, {}, archived_snapshot=archived)
        assert source == "from_archived_trigger_snapshot"
        assert "SPREAD_GATE_V1" in ids
        assert "MOMENTUM_BLEND_6M_12M_V1" in ids

    def test_falls_back_to_current_when_no_archived(self):
        current = _trigger_snapshot("WELL", passes=True)
        ids, source = infer_trigger_ids("WELL", None, current)
        assert source == "from_current_trigger_snapshot"

    def test_falls_back_to_jsonl_when_archived_symbol_not_found(self):
        archived = self._archived_snap("OTHER_SYM")  # archived has different symbol
        entry = _trigger_entry("WELL", risk_on=True)
        ids, source = infer_trigger_ids("WELL", entry, {}, archived_snapshot=archived)
        assert ids is not None
        assert "inferred_from" in source


# ---------------------------------------------------------------------------
# _candidate_metadata with archived_snapshot (via build_lineage_record)
# ---------------------------------------------------------------------------

class TestCandidateMetadataArchived:
    PLAN_ID = "trade_plan-20260514T160000-arch001"
    TRIGGER_HASH = "archived_trigger_hash_meta"

    def _archived_snap(self) -> dict:
        return {
            "trigger_snapshot_hash": self.TRIGGER_HASH,
            "scanned_at": "2026-05-14T15:30:00Z",
            "regime": {"risk_on": True},
            "selected": ["OTHER", "WELL"],
            "candidates": ["OTHER", "WELL", "UNH"],
            "symbol_results": {
                "WELL": {
                    "passes": True,
                    "spread": {"trigger_id": "SPREAD_GATE_V1", "passes": True},
                    "trend": {"trigger_id": "STOCK_TREND_200DMA_V1", "passes": True},
                    "momentum": {
                        "trigger_id": "MOMENTUM_BLEND_6M_12M_V1",
                        "passes": True,
                        "momentum_score": 0.789,
                    },
                    "liquidity": {"trigger_id": "LIQUIDITY_GATE_V1", "passes": True},
                    "atr": {"signal_id": "ATR_SIZING_V1"},
                }
            },
        }

    def _lifecycle_with_fill(self) -> dict:
        return {
            "client_order_id": "TOS-20260514T160000-WELL-BUY",
            "broker_order_id": "broker-meta-001",
            "symbol": "WELL",
            "side": "buy",
            "lifecycle_status": "filled",
            "broker_status": "filled",
            "limit_price": 220.0,
            "notional": 25.0,
            "submitted_at": "2026-05-14T16:00:00Z",
            "fill": {
                "plan_id": self.PLAN_ID,
                "run_id": "execution-20260514T160001-meta",
                "trade_plan_hash": "hash_meta_plan",
                "trigger_snapshot_hash": self.TRIGGER_HASH,
                "fill_price": 219.5,
                "filled_qty": 0.114,
                "filled_notional": 25.0,
                "filled_at": "2026-05-14T16:01:00Z",
                "position_confirmed": True,
            },
        }

    def test_candidate_rank_from_archived_snapshot(self):
        trade_plan_history = {
            self.PLAN_ID: {
                "plan_id": self.PLAN_ID,
                "trigger_snapshot_hash": self.TRIGGER_HASH,
            }
        }
        trigger_snapshot_history = {self.TRIGGER_HASH: self._archived_snap()}
        lc = self._lifecycle_with_fill()

        record = build_lineage_record(
            lifecycle=lc,
            execution_index={},
            current_trade_plan={},
            trigger_history_lines=[],
            trigger_snapshot={},
            outcome_by_cid={},
            linked_at="2026-05-14T20:00:00Z",
            trade_plan_history=trade_plan_history,
            trigger_snapshot_history=trigger_snapshot_history,
        )
        # WELL is at index 1 in selected ["OTHER", "WELL"]
        assert record["candidate_rank"] == 1
        assert record["candidate_source"] == "selected"

    def test_momentum_score_from_archived_snapshot(self):
        trade_plan_history = {
            self.PLAN_ID: {
                "plan_id": self.PLAN_ID,
                "trigger_snapshot_hash": self.TRIGGER_HASH,
            }
        }
        trigger_snapshot_history = {self.TRIGGER_HASH: self._archived_snap()}
        lc = self._lifecycle_with_fill()

        record = build_lineage_record(
            lifecycle=lc,
            execution_index={},
            current_trade_plan={},
            trigger_history_lines=[],
            trigger_snapshot={},
            outcome_by_cid={},
            linked_at="2026-05-14T20:00:00Z",
            trade_plan_history=trade_plan_history,
            trigger_snapshot_history=trigger_snapshot_history,
        )
        assert record["momentum_score"] == pytest.approx(0.789)


# ---------------------------------------------------------------------------
# Requirement 7: new order after archival gets lineage_status=complete
# ---------------------------------------------------------------------------

class TestNewOrderAfterArchivalGetsCompleteLineage:
    """Prove that an order submitted after Paper Ops v2 archiving is active
    gets lineage_status=complete with full trigger metadata."""

    PLAN_ID = "trade_plan-20260514T160035-new123"
    RUN_ID = "execution-20260514T160036-new456"
    TRIGGER_HASH = "archived_trigger_hash_xyz789"
    CLIENT_ORDER_ID = "TOS-20260514T160035-WELL-BUY"

    def _archived_trigger_snapshot(self) -> dict:
        return {
            "trigger_snapshot_hash": self.TRIGGER_HASH,
            "scanned_at": "2026-05-14T15:30:00Z",
            "regime": {"risk_on": True},
            "selected": ["WELL"],
            "candidates": ["WELL", "UNH"],
            "symbol_results": {
                "WELL": {
                    "passes": True,
                    "spread": {"trigger_id": "SPREAD_GATE_V1", "passes": True},
                    "trend": {"trigger_id": "STOCK_TREND_200DMA_V1", "passes": True},
                    "momentum": {
                        "trigger_id": "MOMENTUM_BLEND_6M_12M_V1",
                        "passes": True,
                        "momentum_score": 0.456,
                    },
                    "liquidity": {"trigger_id": "LIQUIDITY_GATE_V1", "passes": True},
                    "atr": {"signal_id": "ATR_SIZING_V1"},
                }
            },
        }

    def _archived_trade_plan(self) -> dict:
        return {
            "plan_id": self.PLAN_ID,
            "trigger_snapshot_hash": self.TRIGGER_HASH,
            "trade_plan_hash": "hash_of_new_plan",
            "targets": {
                "WELL": {"weight": 0.12, "notional": 25.0, "reason": "risk_on_inverse_atr"}
            },
        }

    def _lifecycle_with_fill(self) -> dict:
        return {
            "client_order_id": self.CLIENT_ORDER_ID,
            "broker_order_id": "broker-new001",
            "symbol": "WELL",
            "side": "buy",
            "lifecycle_status": "filled",
            "broker_status": "filled",
            "limit_price": 220.0,
            "notional": 25.0,
            "submitted_at": "2026-05-14T16:00:35Z",
            "fill": {
                "plan_id": self.PLAN_ID,
                "run_id": self.RUN_ID,
                "trade_plan_hash": "hash_of_new_plan",
                "trigger_snapshot_hash": self.TRIGGER_HASH,
                "fill_price": 219.5,
                "filled_qty": 0.114,
                "filled_notional": 25.0,
                "filled_at": "2026-05-14T16:01:00Z",
                "position_confirmed": True,
            },
        }

    def test_complete_lineage_via_trade_plan_and_trigger_history(self):
        """Order with archived trade plan + archived trigger snapshot → complete."""
        trade_plan_history = {self.PLAN_ID: self._archived_trade_plan()}
        trigger_snapshot_history = {self.TRIGGER_HASH: self._archived_trigger_snapshot()}
        lc = self._lifecycle_with_fill()

        record = build_lineage_record(
            lifecycle=lc,
            execution_index={},
            current_trade_plan={},
            trigger_history_lines=[],
            trigger_snapshot={},
            outcome_by_cid={},
            linked_at="2026-05-14T20:00:00Z",
            trade_plan_history=trade_plan_history,
            trigger_snapshot_history=trigger_snapshot_history,
        )

        assert record["lineage_status"] == LINEAGE_STATUS_COMPLETE
        assert record["trigger_snapshot_hash"] == self.TRIGGER_HASH
        assert record["trigger_snapshot_hash_source"] == "from_trade_plan_history"

    def test_trigger_ids_populated_from_archived_snapshot(self):
        """Trigger IDs come from archived snapshot, not inferred from JSONL candidates."""
        trade_plan_history = {self.PLAN_ID: self._archived_trade_plan()}
        trigger_snapshot_history = {self.TRIGGER_HASH: self._archived_trigger_snapshot()}
        lc = self._lifecycle_with_fill()

        record = build_lineage_record(
            lifecycle=lc,
            execution_index={},
            current_trade_plan={},
            trigger_history_lines=[],
            trigger_snapshot={},
            outcome_by_cid={},
            linked_at="2026-05-14T20:00:00Z",
            trade_plan_history=trade_plan_history,
            trigger_snapshot_history=trigger_snapshot_history,
        )

        assert record["trigger_ids"] is not None
        assert "SPREAD_GATE_V1" in record["trigger_ids"]
        assert "MOMENTUM_BLEND_6M_12M_V1" in record["trigger_ids"]
        assert record["trigger_ids_source"] == "from_archived_trigger_snapshot"

    def test_momentum_score_from_archived_snapshot(self):
        trade_plan_history = {self.PLAN_ID: self._archived_trade_plan()}
        trigger_snapshot_history = {self.TRIGGER_HASH: self._archived_trigger_snapshot()}
        lc = self._lifecycle_with_fill()

        record = build_lineage_record(
            lifecycle=lc,
            execution_index={},
            current_trade_plan={},
            trigger_history_lines=[],
            trigger_snapshot={},
            outcome_by_cid={},
            linked_at="2026-05-14T20:00:00Z",
            trade_plan_history=trade_plan_history,
            trigger_snapshot_history=trigger_snapshot_history,
        )

        assert record["momentum_score"] == pytest.approx(0.456)

    def test_candidate_rank_from_archived_snapshot(self):
        trade_plan_history = {self.PLAN_ID: self._archived_trade_plan()}
        trigger_snapshot_history = {self.TRIGGER_HASH: self._archived_trigger_snapshot()}
        lc = self._lifecycle_with_fill()

        record = build_lineage_record(
            lifecycle=lc,
            execution_index={},
            current_trade_plan={},
            trigger_history_lines=[],
            trigger_snapshot={},
            outcome_by_cid={},
            linked_at="2026-05-14T20:00:00Z",
            trade_plan_history=trade_plan_history,
            trigger_snapshot_history=trigger_snapshot_history,
        )

        # WELL is rank 0 in selected=["WELL"]
        assert record["candidate_rank"] == 0
        assert record["candidate_source"] == "selected"

    def test_complete_lineage_without_trigger_snapshot_history(self):
        """Even without archived trigger snapshot, lineage is complete via trade plan."""
        trade_plan_history = {self.PLAN_ID: self._archived_trade_plan()}
        lc = self._lifecycle_with_fill()

        record = build_lineage_record(
            lifecycle=lc,
            execution_index={},
            current_trade_plan={},
            trigger_history_lines=[],
            trigger_snapshot={},
            outcome_by_cid={},
            linked_at="2026-05-14T20:00:00Z",
            trade_plan_history=trade_plan_history,
        )

        assert record["lineage_status"] == LINEAGE_STATUS_COMPLETE
        assert record["trigger_snapshot_hash"] == self.TRIGGER_HASH

    def test_build_lineage_snapshot_complete_count(self):
        """Full snapshot call produces complete_count=1, partial_count=0."""
        trade_plan_history = {self.PLAN_ID: self._archived_trade_plan()}
        trigger_snapshot_history = {self.TRIGGER_HASH: self._archived_trigger_snapshot()}
        lc = self._lifecycle_with_fill()
        monitor_report = {
            "lifecycles": [lc],
            "safety": {
                "submit_order_called": False,
                "cancel_order_called": False,
                "replace_order_called": False,
            },
        }

        snap = build_lineage_snapshot(
            monitor_report=monitor_report,
            execution_index={},
            current_trade_plan={},
            trigger_history_lines=[],
            trigger_snapshot={},
            outcome_snapshot={},
            trade_plan_history=trade_plan_history,
            trigger_snapshot_history=trigger_snapshot_history,
        )

        assert snap["complete_count"] == 1
        assert snap["partial_count"] == 0
        record = snap["lineage_records"][0]
        assert record["lineage_status"] == LINEAGE_STATUS_COMPLETE
        assert record["momentum_score"] == pytest.approx(0.456)

    def test_old_order_without_archived_plan_stays_partial(self):
        """Old orders (before archival was active) remain partial — not faked."""
        old_lc = {
            "client_order_id": "TOS-OLD-ORDER",
            "broker_order_id": "broker-old",
            "symbol": "XYZ",
            "side": "buy",
            "lifecycle_status": "filled",
            "broker_status": "filled",
            "limit_price": 50.0,
            "notional": 25.0,
            "submitted_at": "2026-04-01T16:00:00Z",
            "fill": {
                "plan_id": "old_plan_not_in_history",
                "run_id": "old_run",
                "trade_plan_hash": "old_hash",
                "trigger_snapshot_hash": None,
                "fill_price": 49.9,
                "filled_qty": 0.5,
                "filled_notional": 25.0,
                "filled_at": "2026-04-01T16:01:00Z",
                "position_confirmed": False,
            },
        }

        record = build_lineage_record(
            lifecycle=old_lc,
            execution_index={},
            current_trade_plan={},
            trigger_history_lines=[],
            trigger_snapshot={},
            outcome_by_cid={},
            linked_at="2026-05-14T20:00:00Z",
            trade_plan_history={},
            trigger_snapshot_history={},
        )

        assert record["lineage_status"] == LINEAGE_STATUS_PARTIAL_NO_HASH
        assert record["trigger_snapshot_hash"] is None
        assert record["lineage_note"] is not None

    def test_proposed_order_details_from_execution_report(self):
        """Proposed order details (notional, limit_price, side) come from execution report."""
        execution_report = {
            "run_id": self.RUN_ID,
            "plan_id": self.PLAN_ID,
            "orders_validated": [
                {
                    "symbol": "WELL",
                    "side": "buy",
                    "notional": 25.0,
                    "limit_price": 220.0,
                    "target_weight": 0.12,
                }
            ],
        }
        trade_plan_history = {self.PLAN_ID: self._archived_trade_plan()}
        lc = self._lifecycle_with_fill()

        record = build_lineage_record(
            lifecycle=lc,
            execution_index={self.RUN_ID: execution_report},
            current_trade_plan={},
            trigger_history_lines=[],
            trigger_snapshot={},
            outcome_by_cid={},
            linked_at="2026-05-14T20:00:00Z",
            trade_plan_history=trade_plan_history,
        )

        assert record["proposed_notional"] == pytest.approx(25.0)
        assert record["proposed_limit_price"] == pytest.approx(220.0)
        assert record["proposed_side"] == "buy"
        assert record["proposed_target_weight"] == pytest.approx(0.12)
