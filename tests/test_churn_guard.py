"""Tests for Paper Ops v2 hardening:
- churn_guard.py (cooldown and daily order-count controls)
- trade plan history archiving (generate_trade_plan.py)
- lineage recovery from archived trade plan history
- execution gate gate_daily_order_limits
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

import pytest

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.planning.churn_guard import (
    _date_str,
    _minutes_since,
    check_daily_symbol_limit,
    check_daily_total_limit,
    check_roundtrip_cooldown,
    check_symbol_cooldown,
    filter_churn_blocked,
    get_orders_today,
    get_recent_orders,
    get_symbol_orders_today,
)
from trading_os.research.lineage import (
    LINEAGE_STATUS_COMPLETE,
    LINEAGE_STATUS_PARTIAL_NO_HASH,
    build_lineage_record,
    build_lineage_snapshot,
    load_trade_plan_history,
    recover_trigger_snapshot_hash,
)
from trading_os.execution.execution_gates import gate_daily_order_limits


# ---------------------------------------------------------------------------
# Fixtures / helpers
# ---------------------------------------------------------------------------

_TODAY = "2026-05-14"
_NOW = "2026-05-14T16:00:00Z"
_YESTERDAY = "2026-05-13"


def _lifecycle(symbol: str, side: str, submitted_at: str, lifecycle_status: str = "filled") -> dict:
    return {
        "symbol": symbol,
        "side": side,
        "submitted_at": submitted_at,
        "lifecycle_status": lifecycle_status,
        "client_order_id": f"TOS-{submitted_at.replace(':', '').replace('-', '')}-{symbol}-{side.upper()}",
    }


def _risk_limits(**overrides) -> dict:
    base = {
        "same_symbol_buy_cooldown_minutes": 240,
        "same_symbol_sell_cooldown_minutes": 240,
        "same_symbol_roundtrip_cooldown_days": 1,
        "max_orders_per_symbol_per_day": 1,
        "max_total_paper_orders_per_day": 3,
    }
    base.update(overrides)
    return base


def _order(symbol: str, side: str = "buy") -> dict:
    return {"symbol": symbol, "side": side, "notional": 25.0}


# ---------------------------------------------------------------------------
# 1. Cooldown: recent same-symbol buy blocks new buy
# ---------------------------------------------------------------------------

class TestSameSymbolBuyCooldown:
    def test_buy_within_cooldown_is_blocked(self):
        # BUY submitted 60 min ago; cooldown=240 min
        lc = _lifecycle("EQIX", "buy", "2026-05-14T15:00:00Z")
        result = check_symbol_cooldown([lc], "EQIX", "buy", _NOW, _risk_limits())
        assert result["passes"] is False
        assert "recent_same_symbol_buy" in result["skip_reason"]
        assert "EQIX" in result["skip_reason"]

    def test_buy_outside_cooldown_passes(self):
        # BUY submitted 300 min ago (> 240 min cooldown)
        lc = _lifecycle("EQIX", "buy", "2026-05-14T11:00:00Z")
        result = check_symbol_cooldown([lc], "EQIX", "buy", _NOW, _risk_limits())
        assert result["passes"] is True

    def test_buy_cooldown_zero_always_passes(self):
        lc = _lifecycle("EQIX", "buy", "2026-05-14T15:59:00Z")
        result = check_symbol_cooldown([lc], "EQIX", "buy", _NOW,
                                       _risk_limits(same_symbol_buy_cooldown_minutes=0))
        assert result["passes"] is True

    def test_sell_cooldown_does_not_block_buy(self):
        # There's a sell in cooldown window; checking a new BUY should not trigger sell cooldown
        lc = _lifecycle("EQIX", "sell", "2026-05-14T15:00:00Z")
        result = check_symbol_cooldown([lc], "EQIX", "buy", _NOW, _risk_limits())
        assert result["passes"] is True

    def test_different_symbol_does_not_block(self):
        lc = _lifecycle("JNJ", "buy", "2026-05-14T15:00:00Z")
        result = check_symbol_cooldown([lc], "EQIX", "buy", _NOW, _risk_limits())
        assert result["passes"] is True

    def test_sell_within_cooldown_blocked(self):
        lc = _lifecycle("EQIX", "sell", "2026-05-14T15:00:00Z")
        result = check_symbol_cooldown([lc], "EQIX", "sell", _NOW, _risk_limits())
        assert result["passes"] is False
        assert "recent_same_symbol_sell" in result["skip_reason"]


# ---------------------------------------------------------------------------
# 2. Same-day roundtrip block
# ---------------------------------------------------------------------------

class TestRoundtripCooldown:
    def test_buy_and_sell_today_blocks_new_order(self):
        lcb = _lifecycle("EQIX", "buy", f"{_TODAY}T14:00:00Z")
        lcs = _lifecycle("EQIX", "sell", f"{_TODAY}T15:00:00Z")
        result = check_roundtrip_cooldown([lcb, lcs], "EQIX", _TODAY, _risk_limits())
        assert result["passes"] is False
        assert "same_day_roundtrip_block" in result["skip_reason"]

    def test_buy_only_today_does_not_block(self):
        lcb = _lifecycle("EQIX", "buy", f"{_TODAY}T14:00:00Z")
        result = check_roundtrip_cooldown([lcb], "EQIX", _TODAY, _risk_limits())
        assert result["passes"] is True

    def test_roundtrip_cooldown_zero_always_passes(self):
        lcb = _lifecycle("EQIX", "buy", f"{_TODAY}T14:00:00Z")
        lcs = _lifecycle("EQIX", "sell", f"{_TODAY}T15:00:00Z")
        result = check_roundtrip_cooldown(
            [lcb, lcs], "EQIX", _TODAY,
            _risk_limits(same_symbol_roundtrip_cooldown_days=0)
        )
        assert result["passes"] is True

    def test_buy_and_sell_different_days_does_not_block(self):
        lcb = _lifecycle("EQIX", "buy", f"{_YESTERDAY}T14:00:00Z")
        lcs = _lifecycle("EQIX", "sell", f"{_TODAY}T15:00:00Z")
        result = check_roundtrip_cooldown([lcb, lcs], "EQIX", _TODAY, _risk_limits())
        # Only sell today — no buy today — so no roundtrip
        assert result["passes"] is True


# ---------------------------------------------------------------------------
# 3. max_orders_per_symbol_per_day enforced
# ---------------------------------------------------------------------------

class TestDailySymbolLimit:
    def test_symbol_at_limit_is_blocked(self):
        lc = _lifecycle("EQIX", "buy", f"{_TODAY}T14:00:00Z")
        result = check_daily_symbol_limit([lc], "EQIX", _TODAY, _risk_limits())
        assert result["passes"] is False
        assert "max_orders_per_symbol_per_day" in result["skip_reason"]
        assert "EQIX" in result["skip_reason"]

    def test_symbol_below_limit_passes(self):
        result = check_daily_symbol_limit([], "EQIX", _TODAY, _risk_limits())
        assert result["passes"] is True

    def test_symbol_different_day_not_counted(self):
        lc = _lifecycle("EQIX", "buy", f"{_YESTERDAY}T14:00:00Z")
        result = check_daily_symbol_limit([lc], "EQIX", _TODAY, _risk_limits())
        assert result["passes"] is True

    def test_limit_none_always_passes(self):
        lc = _lifecycle("EQIX", "buy", f"{_TODAY}T14:00:00Z")
        result = check_daily_symbol_limit([lc], "EQIX", _TODAY,
                                          _risk_limits(max_orders_per_symbol_per_day=None))
        assert result["passes"] is True


# ---------------------------------------------------------------------------
# 4. max_total_paper_orders_per_day enforced
# ---------------------------------------------------------------------------

class TestDailyTotalLimit:
    def test_total_at_limit_blocks_all(self):
        lcs = [_lifecycle(f"S{i}", "buy", f"{_TODAY}T1{i}:00:00Z") for i in range(3)]
        result = check_daily_total_limit(lcs, _TODAY, _risk_limits())
        assert result["passes"] is False
        assert "max_total_orders_per_day" in result["skip_reason"]

    def test_total_below_limit_passes(self):
        lcs = [_lifecycle("EQIX", "buy", f"{_TODAY}T14:00:00Z")]
        result = check_daily_total_limit(lcs, _TODAY, _risk_limits())
        assert result["passes"] is True

    def test_total_limit_none_always_passes(self):
        lcs = [_lifecycle(f"S{i}", "buy", f"{_TODAY}T1{i}:00:00Z") for i in range(5)]
        result = check_daily_total_limit(lcs, _TODAY,
                                         _risk_limits(max_total_paper_orders_per_day=None))
        assert result["passes"] is True


# ---------------------------------------------------------------------------
# 5. filter_churn_blocked composite
# ---------------------------------------------------------------------------

class TestFilterChurnBlocked:
    def test_cooldown_blocks_order(self):
        lc = _lifecycle("EQIX", "buy", "2026-05-14T15:00:00Z")
        orders = [_order("EQIX", "buy")]
        ok, blocked = filter_churn_blocked(orders, [lc], _risk_limits(), _NOW)
        assert len(ok) == 0
        assert len(blocked) == 1
        assert "recent_same_symbol_buy" in blocked[0]["skip_reason"]

    def test_unaffected_symbol_passes(self):
        lc = _lifecycle("EQIX", "buy", "2026-05-14T15:00:00Z")
        orders = [_order("JNJ", "buy")]
        ok, blocked = filter_churn_blocked(orders, [lc], _risk_limits(), _NOW)
        assert len(ok) == 1
        assert len(blocked) == 0

    def test_daily_total_blocks_all_remaining(self):
        lcs = [_lifecycle(f"S{i}", "buy", f"{_TODAY}T1{i}:00:00Z") for i in range(3)]
        orders = [_order("WELL", "buy"), _order("WMT", "buy")]
        ok, blocked = filter_churn_blocked(orders, lcs, _risk_limits(), _NOW)
        assert len(ok) == 0
        assert len(blocked) == 2
        for b in blocked:
            assert "max_total_orders_per_day" in b["skip_reason"]

    def test_empty_lifecycles_no_blocks(self):
        orders = [_order("EQIX", "buy"), _order("JNJ", "buy")]
        ok, blocked = filter_churn_blocked(orders, [], _risk_limits(), _NOW)
        assert len(ok) == 2
        assert len(blocked) == 0


# ---------------------------------------------------------------------------
# 6. Execution gate gate_daily_order_limits
# ---------------------------------------------------------------------------

class TestGateDailyOrderLimits:
    def test_gate_passes_when_no_monitor_report(self):
        ctx = {
            "order_monitor_report": {},
            "risk_limits": _risk_limits(),
            "trade_plan": {"proposed_orders": []},
        }
        result = gate_daily_order_limits(ctx)
        assert result["passes"] is True
        assert result["gate_id"] == "DAILY_ORDER_LIMITS"

    def test_gate_fails_when_total_limit_exceeded(self):
        lcs = [{"symbol": f"S{i}", "side": "buy", "submitted_at": f"{_TODAY}T1{i}:00:00Z"}
               for i in range(3)]
        ctx = {
            "order_monitor_report": {"lifecycles": lcs},
            "risk_limits": _risk_limits(),
            "trade_plan": {"proposed_orders": [{"symbol": "WELL", "side": "buy"}]},
        }
        result = gate_daily_order_limits(ctx)
        assert result["passes"] is False
        assert "max_total_orders_per_day" in result["detail"]

    def test_gate_fails_when_symbol_limit_exceeded(self):
        lcs = [{"symbol": "EQIX", "side": "buy", "submitted_at": f"{_TODAY}T14:00:00Z"}]
        ctx = {
            "order_monitor_report": {"lifecycles": lcs},
            "risk_limits": _risk_limits(),
            "trade_plan": {"proposed_orders": [{"symbol": "EQIX", "side": "buy"}]},
        }
        result = gate_daily_order_limits(ctx)
        assert result["passes"] is False
        assert "max_orders_per_symbol_per_day" in result["detail"]

    def test_gate_passes_when_different_symbol_proposed(self):
        lcs = [{"symbol": "EQIX", "side": "buy", "submitted_at": f"{_TODAY}T14:00:00Z"}]
        ctx = {
            "order_monitor_report": {"lifecycles": lcs},
            "risk_limits": _risk_limits(),
            "trade_plan": {"proposed_orders": [{"symbol": "JNJ", "side": "buy"}]},
        }
        result = gate_daily_order_limits(ctx)
        assert result["passes"] is True

    def test_gate_skips_orders_with_skip_reason(self):
        # Symbol with daily limit hit but order has skip_reason — gate should not count it
        lcs = [{"symbol": "EQIX", "side": "buy", "submitted_at": f"{_TODAY}T14:00:00Z"}]
        ctx = {
            "order_monitor_report": {"lifecycles": lcs},
            "risk_limits": _risk_limits(),
            "trade_plan": {"proposed_orders": [
                {"symbol": "EQIX", "side": "buy", "skip_reason": "duplicate_open_order"}
            ]},
        }
        result = gate_daily_order_limits(ctx)
        assert result["passes"] is True


# ---------------------------------------------------------------------------
# 7. Lineage: trigger_snapshot_hash recovered from archived trade plan
# ---------------------------------------------------------------------------

class TestLineageFromTradePlanHistory:
    def _make_lifecycle(self, plan_id: str, symbol: str = "EQIX") -> dict:
        return {
            "client_order_id": f"TOS-20260514-{symbol}-BUY",
            "symbol": symbol,
            "side": "buy",
            "lifecycle_status": "filled",
            "broker_order_id": "fake-broker-id",
            "broker_status": "filled",
            "limit_price": 100.0,
            "submitted_at": f"{_TODAY}T14:00:00Z",
            "fill": {
                "plan_id": plan_id,
                "trade_plan_hash": "abc123",
                "run_id": "execution-fake-run",
                "fill_price": 99.5,
                "filled_qty": 0.25,
                "filled_notional": 25.0,
                "filled_at": f"{_TODAY}T14:05:00Z",
                "trigger_snapshot_hash": None,
            },
        }

    def test_recover_from_trade_plan_history(self):
        plan_id = "trade_plan-20260514T140000-abc12345"
        expected_hash = "deadbeef" * 8

        history = {
            plan_id: {
                "plan_id": plan_id,
                "trigger_snapshot_hash": expected_hash,
                "targets": {"EQIX": {"weight": 0.05, "notional": 25.0}},
            }
        }

        h, source, entry = recover_trigger_snapshot_hash(
            plan_id=plan_id,
            symbol="EQIX",
            executed_at_str=f"{_TODAY}T14:05:00Z",
            current_trade_plan={},
            trigger_history_lines=[],
            trade_plan_history=history,
        )

        assert h == expected_hash
        assert source == "from_trade_plan_history"
        assert entry is None

    def test_lineage_status_complete_from_history(self):
        plan_id = "trade_plan-20260514T140000-abc12345"
        expected_hash = "deadbeef" * 8

        history = {
            plan_id: {
                "plan_id": plan_id,
                "trigger_snapshot_hash": expected_hash,
                "targets": {"EQIX": {"weight": 0.05, "notional": 25.0}},
            }
        }

        lifecycle = self._make_lifecycle(plan_id)
        monitor_report = {
            "lifecycles": [lifecycle],
            "orders_tracked": 1,
        }

        snapshot = build_lineage_snapshot(
            monitor_report=monitor_report,
            execution_index={},
            current_trade_plan={},
            trigger_history_lines=[],
            trigger_snapshot={},
            outcome_snapshot={},
            trade_plan_history=history,
        )

        assert snapshot["lineage_count"] == 1
        record = snapshot["lineage_records"][0]
        assert record["lineage_status"] == LINEAGE_STATUS_COMPLETE
        assert record["trigger_snapshot_hash"] == expected_hash

    def test_lineage_partial_without_history(self):
        plan_id = "trade_plan-20260514T140000-abc12345"

        lifecycle = self._make_lifecycle(plan_id)
        monitor_report = {
            "lifecycles": [lifecycle],
            "orders_tracked": 1,
        }

        snapshot = build_lineage_snapshot(
            monitor_report=monitor_report,
            execution_index={},
            current_trade_plan={},
            trigger_history_lines=[],
            trigger_snapshot={},
            outcome_snapshot={},
            trade_plan_history={},
        )

        record = snapshot["lineage_records"][0]
        assert record["lineage_status"] == LINEAGE_STATUS_PARTIAL_NO_HASH
        assert record["trigger_snapshot_hash"] is None

    def test_target_data_recovered_from_history(self):
        plan_id = "trade_plan-20260514T140000-abc12345"

        history = {
            plan_id: {
                "plan_id": plan_id,
                "trigger_snapshot_hash": "abc123",
                "targets": {
                    "EQIX": {"weight": 0.07, "notional": 30.0, "reason": "momentum"},
                },
            }
        }

        lifecycle = self._make_lifecycle(plan_id)
        monitor_report = {"lifecycles": [lifecycle], "orders_tracked": 1}

        snapshot = build_lineage_snapshot(
            monitor_report=monitor_report,
            execution_index={},
            current_trade_plan={},
            trigger_history_lines=[],
            trigger_snapshot={},
            outcome_snapshot={},
            trade_plan_history=history,
        )

        record = snapshot["lineage_records"][0]
        assert record["target_weight"] == pytest.approx(0.07)
        assert record["target_notional"] == pytest.approx(30.0)
        assert record["target_reason"] == "momentum"


# ---------------------------------------------------------------------------
# 8. Trade plan archiving (integration test for generate_trade_plan.py)
# ---------------------------------------------------------------------------

class TestTradePlanArchiving:
    def _load_script(self, tmp_path: Path) -> Any:
        spec = importlib.util.spec_from_file_location(
            f"generate_trade_plan_{id(tmp_path)}",
            _ROOT / "scripts" / "generate_trade_plan.py",
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def test_trade_plan_written_to_history(self, tmp_path: Path):
        latest_dir = tmp_path / "latest"
        history_dir = tmp_path / "history"
        latest_dir.mkdir(parents=True)

        # Minimal stub data that will produce a valid no-trade plan
        market_snapshot = {
            "generated_at": _NOW,
            "source_data_hash": "abc",
            "bars": {},
            "quotes": {},
            "spreads": {},
        }
        trigger_snapshot = {
            "scanned_at": _NOW,
            "trigger_snapshot_hash": "deadeef1234",
            "regime": {"risk_on": True},
            "selected": [],
            "candidates": [],
            "excluded": [],
            "symbol_results": {},
            "data_stale_gate": {"passes": True},
        }
        account_snapshot = {
            "fetched_at": _NOW,
            "source": "alpaca_paper",
            "account": {"equity": 10000, "cash": 10000, "buying_power": 10000, "status": "ACTIVE"},
            "clock": {"is_open": False},
            "position_count": 0,
            "open_order_count": 0,
        }

        (latest_dir / "market_snapshot.json").write_text(
            json.dumps(market_snapshot) + "\n"
        )
        (latest_dir / "trigger_snapshot.json").write_text(
            json.dumps(trigger_snapshot) + "\n"
        )
        (latest_dir / "account_snapshot.json").write_text(
            json.dumps(account_snapshot) + "\n"
        )

        mod = self._load_script(tmp_path)
        # Redirect paths so _write_json path.relative_to(_ROOT) doesn't fail
        mod._ROOT = tmp_path
        mod.LATEST_DIR = latest_dir
        mod.HISTORY_DIR = history_dir

        from trading_os.config import load_config_file
        import unittest.mock as mock
        with mock.patch.object(mod, "load_config_file", side_effect=load_config_file):
            rc = mod.main(approve_paper=False)

        assert rc == 0

        # Latest should exist
        assert (latest_dir / "trade_plan.json").exists()

        # History trade_plans dir should have exactly one file
        history_plans = list((history_dir / "trade_plans").glob("*.json"))
        assert len(history_plans) == 1

        # The archived plan should have a plan_id
        archived = json.loads(history_plans[0].read_text())
        assert archived.get("plan_id") is not None
        assert archived.get("trading_mode") == "paper"
