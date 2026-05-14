"""Tests for src/trading_os/monitoring/system_status.py.

Covers all check functions, build_system_status(), status-tier transitions,
readiness flags, and graceful handling of missing/empty snapshots.

Safety invariants verified:
- safe_for_scheduled_paper_execution is always False (system policy).
- No execution code is imported or called.
- No order submission path is reachable from this module.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest
from datetime import datetime, timezone, timedelta

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))


def _utcnow() -> str:
    """Return current UTC time as ISO 8601 string."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _utc_future(days: int = 30) -> str:
    dt = datetime.now(timezone.utc) + timedelta(days=days)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

from trading_os.monitoring.system_status import (
    HARD_BLOCK_GATES,
    NON_CRITICAL_GATES,
    RISK_STATE_STALE_MINUTES,
    STATUS_GREEN,
    STATUS_RED,
    STATUS_YELLOW,
    build_system_status,
    check_data_quality,
    check_dry_run_gates,
    check_execution_policy,
    check_order_safety,
    check_risk_state,
    check_source_integrity,
    check_trade_plan,
    format_status_markdown,
)


# ---------------------------------------------------------------------------
# Fixtures / builders
# ---------------------------------------------------------------------------

def _alpaca_snap(source: str = "alpaca_paper") -> dict:
    return {
        "source": source,
        "schema_version": "0.1.0",
        "fetched_at": _utcnow(),
        "data_hash": "a" * 64,
    }


def _account_snap(source: str = "alpaca_paper") -> dict:
    snap = _alpaca_snap(source)
    snap.update({
        "account": {"equity": "10000.00", "cash": "5000.00", "buying_power": "5000.00"},
        "clock": {"is_open": True},
        "position_count": 1,
        "open_order_count": 0,
    })
    return snap


def _positions_snap(source: str = "alpaca_paper") -> dict:
    snap = _alpaca_snap(source)
    snap.update({
        "positions": [
            {
                "symbol": "AAPL",
                "qty": "5",
                "market_value": "800.00",
                "unrealized_pl": "50.00",
                "avg_entry_price": "150.00",
                "current_price": "160.00",
            }
        ],
        "position_count": 1,
    })
    return snap


def _orders_snap(source: str = "alpaca_paper", orders: list | None = None) -> dict:
    snap = _alpaca_snap(source)
    snap.update({
        "orders": orders if orders is not None else [],
        "open_order_count": len(orders) if orders is not None else 0,
    })
    return snap


def _market_snap(source: str = "alpaca_paper") -> dict:
    snap = _alpaca_snap(source)
    snap["market"] = {"is_open": True}
    return snap


def _fresh_risk_state() -> dict:
    return {
        "paused": False,
        "drawdown": -0.01,
        "updated_at": _utcnow(),
        "peak_equity": 10000.0,
        "latest_equity": 9900.0,
    }


def _risk_limits() -> dict:
    return {
        "live_trading_allowed": False,
        "max_drawdown_warn_pct": -0.05,
        "max_drawdown_block_pct": -0.10,
        "max_position_pct": 0.10,
    }


def _execution_policy() -> dict:
    return {
        "paper_only": True,
        "allow_shorting": False,
        "allow_options": False,
        "allow_crypto": False,
        "plan_max_age_minutes": 360,
    }


def _gates_pass() -> dict:
    return {
        "all_gates_pass": True,
        "failed_gates": [],
        "status": "pass",
        "generated_at": _utcnow(),
    }


def _gates_fail_hard() -> dict:
    return {
        "all_gates_pass": False,
        "failed_gates": ["CANONICAL_SOURCE_INTEGRITY"],
        "status": "fail",
        "generated_at": _utcnow(),
    }


def _gates_fail_soft() -> dict:
    return {
        "all_gates_pass": False,
        "failed_gates": ["MARKET_CLOCK_OPEN"],
        "status": "partial",
        "generated_at": _utcnow(),
    }


def _trade_plan(approved: bool = True, order_type: str = "limit") -> dict:
    return {
        "plan_id": "plan-001",
        "generated_at": _utcnow(),
        "expires_at": _utc_future(30),
        "trading_mode": "paper",
        "approval": {"approved_for_execution": approved},
        "proposed_orders": [
            {
                "symbol": "AAPL",
                "side": "buy",
                "order_type": order_type,
                "limit_price": 155.00,
                "notional": 500.00,
                "skip_reason": None,
            }
        ],
    }


def _full_snapshots(
    account_source: str = "alpaca_paper",
    position_source: str = "alpaca_paper",
    orders_source: str = "alpaca_paper",
    market_source: str = "alpaca_paper",
    approved_plan: bool = True,
    open_orders: list | None = None,
) -> dict:
    return {
        "account_snapshot":     _account_snap(account_source),
        "positions_snapshot":   _positions_snap(position_source),
        "orders_snapshot":      _orders_snap(orders_source, open_orders),
        "market_snapshot":      _market_snap(market_source),
        "data_quality_snapshot": {"status": "ok"},
        "trigger_snapshot":     {"candidates": []},
        "trade_plan":           _trade_plan(approved=approved_plan),
        "execution_report":     _gates_pass(),
        "order_monitor_report": {},
        "outcome_snapshot":     {},
        "lineage_snapshot":     {},
        "trigger_performance":  {},
    }


def _full_configs(
    risk_state: dict | None = None,
    risk_limits: dict | None = None,
    execution_policy: dict | None = None,
) -> dict:
    return {
        "risk_limits":      risk_limits or _risk_limits(),
        "execution_policy": execution_policy or _execution_policy(),
        "strategy":         {},
        "risk_state":       risk_state or _fresh_risk_state(),
    }


# ---------------------------------------------------------------------------
# check_source_integrity
# ---------------------------------------------------------------------------

class TestCheckSourceIntegrity:
    def test_all_alpaca_paper_passes(self):
        result = check_source_integrity(
            _account_snap(), _positions_snap(), _orders_snap(), _market_snap()
        )
        assert result["passes"] is True
        assert result["failed"] == []

    def test_mock_account_fails(self):
        result = check_source_integrity(
            _account_snap("mock"), _positions_snap(), _orders_snap(), _market_snap()
        )
        assert result["passes"] is False
        assert len(result["failed"]) > 0

    def test_unknown_source_fails(self):
        result = check_source_integrity(
            _account_snap("unknown"), _positions_snap(), _orders_snap(), _market_snap()
        )
        assert result["passes"] is False

    def test_missing_source_field_fails(self):
        acct = _account_snap()
        del acct["source"]
        result = check_source_integrity(
            acct, _positions_snap(), _orders_snap(), _market_snap()
        )
        assert result["passes"] is False

    def test_empty_snapshots_fail(self):
        result = check_source_integrity({}, {}, {}, {})
        assert result["passes"] is False

    def test_checked_count(self):
        result = check_source_integrity(
            _account_snap(), _positions_snap(), _orders_snap(), _market_snap()
        )
        assert len(result["checked"]) >= 4


# ---------------------------------------------------------------------------
# check_risk_state
# ---------------------------------------------------------------------------

class TestCheckRiskState:
    def test_fresh_healthy_passes(self):
        result = check_risk_state(_fresh_risk_state(), _risk_limits())
        assert result["passes"] is True
        assert result["paused"] is False
        assert result["stale"] is False
        assert result["drawdown_blocked"] is False

    def test_paused_fails(self):
        rs = _fresh_risk_state()
        rs["paused"] = True
        result = check_risk_state(rs, _risk_limits())
        assert result["passes"] is False
        assert result["paused"] is True

    def test_empty_state_is_stale(self):
        result = check_risk_state({}, _risk_limits())
        assert result["stale"] is True
        assert result["passes"] is False

    def test_drawdown_at_warn_threshold(self):
        rs = _fresh_risk_state()
        rs["drawdown"] = -0.05
        result = check_risk_state(rs, _risk_limits())
        assert result["drawdown_warn"] is True
        assert result["drawdown_blocked"] is False

    def test_drawdown_at_block_threshold(self):
        rs = _fresh_risk_state()
        rs["drawdown"] = -0.10
        result = check_risk_state(rs, _risk_limits())
        assert result["drawdown_blocked"] is True
        assert result["passes"] is False

    def test_drawdown_below_block_threshold(self):
        rs = _fresh_risk_state()
        rs["drawdown"] = -0.15
        result = check_risk_state(rs, _risk_limits())
        assert result["drawdown_blocked"] is True
        assert result["passes"] is False

    def test_stale_minutes_none_when_no_timestamp(self):
        result = check_risk_state({}, _risk_limits())
        assert result["stale_minutes"] is None


# ---------------------------------------------------------------------------
# check_data_quality
# ---------------------------------------------------------------------------

class TestCheckDataQuality:
    def test_ok_status_passes(self):
        result = check_data_quality({"status": "ok"})
        assert result["passes"] is True

    def test_warning_status_passes(self):
        result = check_data_quality({"status": "WARNING"})
        assert result["passes"] is True

    def test_error_status_fails(self):
        result = check_data_quality({"status": "ERROR"})
        assert result["passes"] is False

    def test_critical_status_fails(self):
        result = check_data_quality({"status": "CRITICAL"})
        assert result["passes"] is False

    def test_empty_snapshot_passes_with_unknown_status(self):
        result = check_data_quality({})
        assert result["status"] == "unknown"
        assert result["passes"] is True

    def test_wide_spread_count(self):
        snap = {"status": "ok", "wide_spreads": {"AAPL": 0.03, "MSFT": 0.04}}
        result = check_data_quality(snap)
        assert result["wide_spread_count"] == 2
        assert "AAPL" in result["wide_spread_symbols"]


# ---------------------------------------------------------------------------
# check_dry_run_gates
# ---------------------------------------------------------------------------

class TestCheckDryRunGates:
    def test_all_pass(self):
        result = check_dry_run_gates(_gates_pass())
        assert result["passes"] is True
        assert result["hard_failures"] == []
        assert result["has_hard_failures"] is False

    def test_hard_gate_failure(self):
        result = check_dry_run_gates(_gates_fail_hard())
        assert result["passes"] is False
        assert "CANONICAL_SOURCE_INTEGRITY" in result["hard_failures"]
        assert result["has_hard_failures"] is True

    def test_soft_gate_failure(self):
        result = check_dry_run_gates(_gates_fail_soft())
        assert result["passes"] is False
        assert "MARKET_CLOCK_OPEN" in result["soft_failures"]
        assert result["has_hard_failures"] is False

    def test_empty_report_fails(self):
        result = check_dry_run_gates({})
        assert result["passes"] is False

    def test_non_critical_gates_classified_as_soft(self):
        for gate in NON_CRITICAL_GATES:
            report = {"all_gates_pass": False, "failed_gates": [gate]}
            result = check_dry_run_gates(report)
            assert gate in result["soft_failures"]

    def test_hard_block_gates_classified_as_hard(self):
        for gate in HARD_BLOCK_GATES:
            report = {"all_gates_pass": False, "failed_gates": [gate]}
            result = check_dry_run_gates(report)
            assert gate in result["hard_failures"]


# ---------------------------------------------------------------------------
# check_trade_plan
# ---------------------------------------------------------------------------

class TestCheckTradePlan:
    def test_valid_plan_passes(self):
        result = check_trade_plan(_trade_plan(), _execution_policy())
        assert result["passes"] is True
        assert result["missing"] is False
        assert result["non_limit_orders"] == []

    def test_empty_plan_fails_gracefully(self):
        result = check_trade_plan({}, _execution_policy())
        assert result["passes"] is False
        assert result["missing"] is True
        assert result["proposed_order_count"] == 0

    def test_non_limit_order_detected(self):
        result = check_trade_plan(_trade_plan(order_type="market"), _execution_policy())
        assert "AAPL" in result["non_limit_orders"]

    def test_skipped_orders_excluded_from_non_limit_check(self):
        plan = _trade_plan(order_type="market")
        plan["proposed_orders"][0]["skip_reason"] = "RISK_CAP"
        result = check_trade_plan(plan, _execution_policy())
        assert result["non_limit_orders"] == []

    def test_expired_plan_fails(self):
        plan = _trade_plan()
        plan["expires_at"] = "2000-01-01T00:00:00Z"  # clearly in the past
        result = check_trade_plan(plan, _execution_policy())
        assert result["is_expired"] is True
        assert result["passes"] is False

    def test_approved_for_execution_reflected(self):
        assert check_trade_plan(_trade_plan(approved=True), _execution_policy())["is_approved"] is True
        assert check_trade_plan(_trade_plan(approved=False), _execution_policy())["is_approved"] is False


# ---------------------------------------------------------------------------
# check_order_safety
# ---------------------------------------------------------------------------

class TestCheckOrderSafety:
    def test_no_conflicts(self):
        result = check_order_safety(_orders_snap(), _trade_plan())
        assert result["passes"] is True
        assert result["has_duplicates"] is False

    def test_conflict_detected(self):
        open_orders = [{"symbol": "AAPL", "status": "new"}]
        result = check_order_safety(_orders_snap(orders=open_orders), _trade_plan())
        assert result["has_duplicates"] is True
        assert "AAPL" in result["conflict_symbols"]
        assert result["passes"] is False

    def test_skipped_planned_order_ignored(self):
        plan = _trade_plan()
        plan["proposed_orders"][0]["skip_reason"] = "RISK_CAP"
        open_orders = [{"symbol": "AAPL"}]
        result = check_order_safety(_orders_snap(orders=open_orders), plan)
        assert result["passes"] is True

    def test_empty_plan_no_conflicts(self):
        open_orders = [{"symbol": "AAPL"}]
        result = check_order_safety(_orders_snap(orders=open_orders), {})
        assert result["passes"] is True


# ---------------------------------------------------------------------------
# check_execution_policy
# ---------------------------------------------------------------------------

class TestCheckExecutionPolicy:
    def test_safe_policy_passes(self):
        result = check_execution_policy(_risk_limits(), _execution_policy())
        assert result["passes"] is True
        assert result["violations"] == []

    def test_live_trading_allowed_fails(self):
        rl = _risk_limits()
        rl["live_trading_allowed"] = True
        result = check_execution_policy(rl, _execution_policy())
        assert result["passes"] is False
        assert any("live_trading_allowed" in v for v in result["violations"])

    def test_allow_shorting_fails(self):
        ep = _execution_policy()
        ep["allow_shorting"] = True
        result = check_execution_policy(_risk_limits(), ep)
        assert result["passes"] is False

    def test_allow_options_fails(self):
        ep = _execution_policy()
        ep["allow_options"] = True
        result = check_execution_policy(_risk_limits(), ep)
        assert result["passes"] is False

    def test_allow_crypto_fails(self):
        ep = _execution_policy()
        ep["allow_crypto"] = True
        result = check_execution_policy(_risk_limits(), ep)
        assert result["passes"] is False

    def test_paper_only_false_fails(self):
        ep = _execution_policy()
        ep["paper_only"] = False
        result = check_execution_policy(_risk_limits(), ep)
        assert result["passes"] is False


# ---------------------------------------------------------------------------
# build_system_status — overall status tiers
# ---------------------------------------------------------------------------

class TestBuildSystemStatusGreenYellowRed:
    def test_green_when_all_checks_pass(self):
        status = build_system_status(_full_snapshots(), _full_configs())
        assert status["overall_status"] == STATUS_GREEN

    def test_red_when_source_integrity_fails(self):
        status = build_system_status(
            _full_snapshots(account_source="mock"),
            _full_configs(),
        )
        assert status["overall_status"] == STATUS_RED

    def test_red_when_drawdown_blocked(self):
        rs = _fresh_risk_state()
        rs["drawdown"] = -0.15
        status = build_system_status(_full_snapshots(), _full_configs(risk_state=rs))
        assert status["overall_status"] == STATUS_RED

    def test_red_when_hard_gate_fails(self):
        snaps = _full_snapshots()
        snaps["execution_report"] = _gates_fail_hard()
        status = build_system_status(snaps, _full_configs())
        assert status["overall_status"] == STATUS_RED

    def test_yellow_when_only_soft_gate_fails(self):
        snaps = _full_snapshots()
        snaps["execution_report"] = _gates_fail_soft()
        status = build_system_status(snaps, _full_configs())
        assert status["overall_status"] == STATUS_YELLOW

    def test_yellow_when_risk_state_stale(self):
        rs = {"paused": False, "drawdown": 0.0, "updated_at": "2020-01-01T00:00:00Z"}
        status = build_system_status(_full_snapshots(), _full_configs(risk_state=rs))
        assert status["overall_status"] in (STATUS_YELLOW, STATUS_RED)

    def test_yellow_when_trade_plan_missing(self):
        snaps = _full_snapshots()
        snaps["trade_plan"] = {}
        status = build_system_status(snaps, _full_configs())
        assert status["overall_status"] in (STATUS_YELLOW, STATUS_RED)

    def test_red_when_duplicate_open_orders(self):
        open_orders = [{"symbol": "AAPL", "status": "new"}]
        status = build_system_status(
            _full_snapshots(open_orders=open_orders),
            _full_configs(),
        )
        assert status["overall_status"] == STATUS_RED

    def test_red_when_policy_violations(self):
        rl = _risk_limits()
        rl["live_trading_allowed"] = True
        status = build_system_status(_full_snapshots(), _full_configs(risk_limits=rl))
        assert status["overall_status"] == STATUS_RED


# ---------------------------------------------------------------------------
# build_system_status — safe_for_scheduled_paper_execution always False
# ---------------------------------------------------------------------------

class TestScheduledPaperExecutionAlwaysFalse:
    def test_always_false_on_green_with_approved_plan(self):
        status = build_system_status(_full_snapshots(approved_plan=True), _full_configs())
        assert status["overall_status"] == STATUS_GREEN
        assert status["safe_for_scheduled_paper_execution"] is False

    def test_always_false_on_yellow(self):
        rs = {"paused": False, "drawdown": 0.0, "updated_at": "2020-01-01T00:00:00Z"}
        status = build_system_status(_full_snapshots(), _full_configs(risk_state=rs))
        assert status["safe_for_scheduled_paper_execution"] is False

    def test_always_false_on_red(self):
        status = build_system_status(
            _full_snapshots(account_source="mock"),
            _full_configs(),
        )
        assert status["safe_for_scheduled_paper_execution"] is False

    def test_always_false_with_all_empty_snapshots(self):
        status = build_system_status({}, _full_configs())
        assert status["safe_for_scheduled_paper_execution"] is False


# ---------------------------------------------------------------------------
# build_system_status — safe_for_manual_paper_execution
# ---------------------------------------------------------------------------

class TestSafeForManualPaperExecution:
    def test_true_only_on_green_with_approved_plan_and_gates(self):
        status = build_system_status(_full_snapshots(approved_plan=True), _full_configs())
        assert status["overall_status"] == STATUS_GREEN
        assert status["safe_for_manual_paper_execution"] is True

    def test_false_when_plan_not_approved(self):
        status = build_system_status(_full_snapshots(approved_plan=False), _full_configs())
        assert status["safe_for_manual_paper_execution"] is False

    def test_false_when_gates_fail(self):
        snaps = _full_snapshots()
        snaps["execution_report"] = _gates_fail_hard()
        status = build_system_status(snaps, _full_configs())
        assert status["safe_for_manual_paper_execution"] is False

    def test_false_when_red_status(self):
        status = build_system_status(
            _full_snapshots(account_source="mock"),
            _full_configs(),
        )
        assert status["safe_for_manual_paper_execution"] is False

    def test_false_when_drawdown_blocked(self):
        rs = _fresh_risk_state()
        rs["drawdown"] = -0.15
        status = build_system_status(_full_snapshots(), _full_configs(risk_state=rs))
        assert status["safe_for_manual_paper_execution"] is False

    def test_false_when_duplicate_orders(self):
        open_orders = [{"symbol": "AAPL", "status": "new"}]
        status = build_system_status(
            _full_snapshots(open_orders=open_orders),
            _full_configs(),
        )
        assert status["safe_for_manual_paper_execution"] is False


# ---------------------------------------------------------------------------
# build_system_status — safe_for_research_cycle
# ---------------------------------------------------------------------------

class TestSafeForResearchCycle:
    def test_true_on_green(self):
        status = build_system_status(_full_snapshots(), _full_configs())
        assert status["safe_for_research_cycle"] is True

    def test_true_on_yellow_if_source_and_policy_ok(self):
        snaps = _full_snapshots()
        snaps["execution_report"] = _gates_fail_soft()
        status = build_system_status(snaps, _full_configs())
        assert status["overall_status"] == STATUS_YELLOW
        assert status["safe_for_research_cycle"] is True

    def test_false_on_red(self):
        status = build_system_status(
            _full_snapshots(account_source="mock"),
            _full_configs(),
        )
        assert status["safe_for_research_cycle"] is False

    def test_false_when_policy_violations(self):
        rl = _risk_limits()
        rl["live_trading_allowed"] = True
        status = build_system_status(_full_snapshots(), _full_configs(risk_limits=rl))
        assert status["safe_for_research_cycle"] is False


# ---------------------------------------------------------------------------
# build_system_status — missing / empty snapshots degrade gracefully
# ---------------------------------------------------------------------------

class TestMissingSnapshotsGracefulness:
    def test_empty_snapshots_does_not_raise(self):
        status = build_system_status({}, _full_configs())
        assert "overall_status" in status

    def test_missing_account_snapshot_produces_status(self):
        snaps = _full_snapshots()
        snaps.pop("account_snapshot")
        status = build_system_status(snaps, _full_configs())
        assert "overall_status" in status

    def test_missing_execution_report_defaults_to_fail(self):
        snaps = _full_snapshots()
        snaps["execution_report"] = {}
        status = build_system_status(snaps, _full_configs())
        assert status["dry_run_all_gates_pass"] is False

    def test_missing_trade_plan_produces_warning(self):
        snaps = _full_snapshots()
        snaps["trade_plan"] = {}
        status = build_system_status(snaps, _full_configs())
        warnings = status.get("warnings", [])
        actions = status.get("required_operator_actions", [])
        combined = " ".join(warnings + actions).lower()
        assert "trade plan" in combined or "research cycle" in combined

    def test_all_empty_snapshots_does_not_raise(self):
        empty_snaps = {k: {} for k in [
            "account_snapshot", "positions_snapshot", "orders_snapshot",
            "market_snapshot", "data_quality_snapshot", "trigger_snapshot",
            "trade_plan", "execution_report", "order_monitor_report",
            "outcome_snapshot", "lineage_snapshot", "trigger_performance",
        ]}
        status = build_system_status(empty_snaps, _full_configs())
        assert isinstance(status, dict)
        assert "overall_status" in status


# ---------------------------------------------------------------------------
# build_system_status — required output fields
# ---------------------------------------------------------------------------

class TestRequiredOutputFields:
    def _status(self) -> dict:
        return build_system_status(_full_snapshots(), _full_configs())

    def test_has_schema_version(self):
        assert "schema_version" in self._status()

    def test_has_generated_at(self):
        assert "generated_at" in self._status()

    def test_has_overall_status(self):
        assert self._status()["overall_status"] in (STATUS_GREEN, STATUS_YELLOW, STATUS_RED)

    def test_has_safe_for_research_cycle(self):
        assert isinstance(self._status()["safe_for_research_cycle"], bool)

    def test_has_safe_for_manual_paper_execution(self):
        assert isinstance(self._status()["safe_for_manual_paper_execution"], bool)

    def test_has_safe_for_scheduled_paper_execution(self):
        assert self._status()["safe_for_scheduled_paper_execution"] is False

    def test_has_blocking_issues_list(self):
        assert isinstance(self._status()["blocking_issues"], list)

    def test_has_warnings_list(self):
        assert isinstance(self._status()["warnings"], list)

    def test_has_required_operator_actions_list(self):
        assert isinstance(self._status()["required_operator_actions"], list)

    def test_has_dry_run_all_gates_pass(self):
        assert isinstance(self._status()["dry_run_all_gates_pass"], bool)

    def test_has_failed_gates_list(self):
        assert isinstance(self._status()["failed_gates"], list)

    def test_has_source_integrity_status(self):
        assert self._status()["source_integrity_status"] in ("ok", "failed")

    def test_has_risk_state_block(self):
        rs = self._status()["risk_state"]
        assert "drawdown" in rs
        assert "paused" in rs
        assert "stale" in rs

    def test_has_status_hash(self):
        h = self._status()["status_hash"]
        assert isinstance(h, str) and len(h) > 0

    def test_has_latest_plan_id(self):
        assert "latest_plan_id" in self._status()

    def test_has_proposed_orders(self):
        assert isinstance(self._status()["proposed_orders"], list)


# ---------------------------------------------------------------------------
# format_status_markdown
# ---------------------------------------------------------------------------

class TestFormatStatusMarkdown:
    def _build(self) -> dict:
        return build_system_status(_full_snapshots(), _full_configs())

    def test_returns_string(self):
        assert isinstance(format_status_markdown(self._build()), str)

    def test_contains_overall_status(self):
        md = format_status_markdown(self._build())
        assert "GREEN" in md or "YELLOW" in md or "RED" in md

    def test_contains_scheduled_no_policy_note(self):
        md = format_status_markdown(self._build())
        assert "NO (policy)" in md or "Scheduled" in md

    def test_contains_separator(self):
        md = format_status_markdown(self._build())
        assert "---" in md

    def test_blocking_issues_shown(self):
        status = build_system_status(
            _full_snapshots(account_source="mock"),
            _full_configs(),
        )
        md = format_status_markdown(status)
        assert "Blocking Issues" in md or "blocking" in md.lower()

    def test_empty_status_does_not_raise(self):
        md = format_status_markdown({})
        assert isinstance(md, str)


# ---------------------------------------------------------------------------
# No execution path reachable
# ---------------------------------------------------------------------------

class TestNoExecutionPath:
    def test_execute_paper_not_importable_from_module(self):
        """system_status module must not import any execution path."""
        import importlib
        module = importlib.import_module("trading_os.monitoring.system_status")
        assert not hasattr(module, "execute_paper")
        assert not hasattr(module, "submit_order")
        assert not hasattr(module, "place_order")

    def test_build_system_status_returns_dict_not_order(self):
        status = build_system_status(_full_snapshots(), _full_configs())
        assert isinstance(status, dict)
        # must not contain order-submission artifacts
        assert "order_id" not in status
        assert "submitted_orders" not in status

    def test_enable_paper_execution_never_set(self):
        import inspect
        import trading_os.monitoring.system_status as mod
        src = inspect.getsource(mod)
        assert "ENABLE_PAPER_EXECUTION" not in src
        assert "execute_paper" not in src
