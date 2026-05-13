"""Tests for the research-only alert router.

Key invariants proven here:
- Router rejects alerts where trade_execution_allowed is not exactly False.
- Router rejects alerts where blocked_by_default is not exactly True.
- Router rejects alerts with execution intent fields (execute, execute_paper,
  submit_order, order, approved_for_execution=true).
- Router rejects crypto or options symbols.
- Router rejects disallowed asset_class values.
- validate_route_mode rejects incompatible route_mode for a given next_step.
- log_only → writes route record, logs to TRIGGER-LOG and SIGNAL-LOG.
- request_alert_review → writes route record; suggested_commands is empty.
- request_data_refresh → writes route record; suggested scripts are refresh commands.
- request_trade_plan_unapproved → writes route record; no --approve-paper.
- Safety checks block in every result has execute_paper_called=False.
- Source inspection: alert_router.py never imports execute_paper, never calls approve_paper.
- External alerts cannot trigger execution (proven by source + result inspection).
- check_trade_plan_not_approved raises AlertRouterError when plan is approved.
- scripts_for_route returns correct scripts per route_mode and next_step.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from trading_os.research.alert_router import (
    ALLOWED_NEXT_STEPS,
    ALLOWED_ROUTE_MODES,
    SUGGESTED_PIPELINE_COMMANDS,
    SUGGESTED_REFRESH_COMMANDS,
    AlertRouterError,
    check_trade_plan_not_approved,
    route_alert,
    scripts_for_route,
    validate_alert_safety,
    validate_route_mode,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

SAFE_ALERT: dict = {
    "alert_id": "test-router-001",
    "symbol": "AAPL",
    "next_step": "log_only",
    "source": "test",
    "trade_execution_allowed": False,
    "blocked_by_default": True,
    "ingested_at": "2026-05-13T12:00:00Z",
    "raw_payload_hash": "abc123",
}


def _make_alert(**overrides) -> dict:
    return {**SAFE_ALERT, **overrides}


def _route(tmp_path: Path, alert: dict, route_mode: str = "record_only") -> dict:
    return route_alert(
        alert=alert,
        alerts_dir=tmp_path / "alerts",
        trigger_log_path=tmp_path / "TRIGGER-LOG.md",
        signal_log_path=tmp_path / "SIGNAL-LOG.md",
        research_context_path=tmp_path / "RESEARCH-CONTEXT.md",
        route_mode=route_mode,
    )


# ---------------------------------------------------------------------------
# validate_alert_safety — flag checks
# ---------------------------------------------------------------------------

class TestValidateAlertSafetyFlags:
    def test_valid_alert_passes(self) -> None:
        validate_alert_safety(SAFE_ALERT)

    def test_non_dict_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="JSON object"):
            validate_alert_safety("not a dict")

    def test_trade_execution_allowed_true_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="trade_execution_allowed must be false"):
            validate_alert_safety(_make_alert(trade_execution_allowed=True))

    def test_trade_execution_allowed_none_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="trade_execution_allowed must be false"):
            validate_alert_safety(_make_alert(trade_execution_allowed=None))

    def test_trade_execution_allowed_missing_rejected(self) -> None:
        a = {k: v for k, v in SAFE_ALERT.items() if k != "trade_execution_allowed"}
        with pytest.raises(AlertRouterError, match="trade_execution_allowed must be false"):
            validate_alert_safety(a)

    def test_trade_execution_allowed_string_false_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="trade_execution_allowed must be false"):
            validate_alert_safety(_make_alert(trade_execution_allowed="false"))

    def test_blocked_by_default_false_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="blocked_by_default must be true"):
            validate_alert_safety(_make_alert(blocked_by_default=False))

    def test_blocked_by_default_none_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="blocked_by_default must be true"):
            validate_alert_safety(_make_alert(blocked_by_default=None))

    def test_blocked_by_default_missing_rejected(self) -> None:
        a = {k: v for k, v in SAFE_ALERT.items() if k != "blocked_by_default"}
        with pytest.raises(AlertRouterError, match="blocked_by_default must be true"):
            validate_alert_safety(a)

    def test_blocked_by_default_string_true_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="blocked_by_default must be true"):
            validate_alert_safety(_make_alert(blocked_by_default="true"))

    def test_invalid_next_step_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="next_step"):
            validate_alert_safety(_make_alert(next_step="execute_now"))

    def test_missing_next_step_rejected(self) -> None:
        a = {k: v for k, v in SAFE_ALERT.items() if k != "next_step"}
        with pytest.raises(AlertRouterError, match="next_step"):
            validate_alert_safety(a)

    def test_all_allowed_next_steps_pass(self) -> None:
        for ns in ALLOWED_NEXT_STEPS:
            validate_alert_safety(_make_alert(next_step=ns))


# ---------------------------------------------------------------------------
# validate_alert_safety — execution intent field rejection
# ---------------------------------------------------------------------------

class TestValidateAlertSafetyExecutionIntent:
    def test_execute_field_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="execution intent field"):
            validate_alert_safety(_make_alert(execute=True))

    def test_execute_paper_field_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="execution intent field"):
            validate_alert_safety(_make_alert(execute_paper=True))

    def test_submit_order_field_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="execution intent field"):
            validate_alert_safety(_make_alert(submit_order=True))

    def test_order_field_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="execution intent field"):
            validate_alert_safety(_make_alert(order={"symbol": "AAPL"}))

    def test_approved_for_execution_true_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="approved_for_execution=true"):
            validate_alert_safety(_make_alert(approved_for_execution=True))

    def test_approved_for_execution_false_passes(self) -> None:
        # False is fine — the field is only prohibited when True
        validate_alert_safety(_make_alert(approved_for_execution=False))

    def test_execute_string_value_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="execution intent field"):
            validate_alert_safety(_make_alert(execute="yes"))


# ---------------------------------------------------------------------------
# validate_alert_safety — asset class and symbol checks
# ---------------------------------------------------------------------------

class TestValidateAlertSafetyAssetSymbol:
    def test_us_equity_asset_class_passes(self) -> None:
        validate_alert_safety(_make_alert(asset_class="us_equity"))

    def test_etf_asset_class_passes(self) -> None:
        validate_alert_safety(_make_alert(asset_class="etf"))

    def test_cash_like_etf_asset_class_passes(self) -> None:
        validate_alert_safety(_make_alert(asset_class="cash_like_etf"))

    def test_asset_class_absent_passes(self) -> None:
        a = {k: v for k, v in SAFE_ALERT.items() if k != "asset_class"}
        validate_alert_safety(a)

    def test_crypto_asset_class_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="asset_class"):
            validate_alert_safety(_make_alert(asset_class="crypto"))

    def test_options_asset_class_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="asset_class"):
            validate_alert_safety(_make_alert(asset_class="options"))

    def test_futures_asset_class_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="asset_class"):
            validate_alert_safety(_make_alert(asset_class="futures"))

    def test_crypto_symbol_btc_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="crypto"):
            validate_alert_safety(_make_alert(symbol="BTC"))

    def test_crypto_symbol_eth_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="crypto"):
            validate_alert_safety(_make_alert(symbol="ETH"))

    def test_crypto_symbol_with_slash_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="crypto"):
            validate_alert_safety(_make_alert(symbol="BTC/USD"))

    def test_options_symbol_occ_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="options"):
            validate_alert_safety(_make_alert(symbol="AAPL230120C00150000"))

    def test_normal_equity_symbol_passes(self) -> None:
        validate_alert_safety(_make_alert(symbol="MSFT"))
        validate_alert_safety(_make_alert(symbol="SPY"))
        validate_alert_safety(_make_alert(symbol="WELL"))


# ---------------------------------------------------------------------------
# validate_route_mode
# ---------------------------------------------------------------------------

class TestValidateRouteMode:
    def test_record_only_valid_for_all_next_steps(self) -> None:
        for ns in ALLOWED_NEXT_STEPS:
            validate_route_mode(ns, "record_only")  # must not raise

    def test_run_refresh_valid_for_data_refresh(self) -> None:
        validate_route_mode("request_data_refresh", "run_refresh")

    def test_run_refresh_valid_for_unapproved_plan(self) -> None:
        validate_route_mode("request_trade_plan_unapproved", "run_refresh")

    def test_run_unapproved_plan_valid_for_unapproved_plan(self) -> None:
        validate_route_mode("request_trade_plan_unapproved", "run_unapproved_plan")

    def test_run_refresh_rejected_for_log_only(self) -> None:
        with pytest.raises(AlertRouterError, match="not compatible"):
            validate_route_mode("log_only", "run_refresh")

    def test_run_refresh_rejected_for_alert_review(self) -> None:
        with pytest.raises(AlertRouterError, match="not compatible"):
            validate_route_mode("request_alert_review", "run_refresh")

    def test_run_unapproved_plan_rejected_for_log_only(self) -> None:
        with pytest.raises(AlertRouterError, match="not compatible"):
            validate_route_mode("log_only", "run_unapproved_plan")

    def test_run_unapproved_plan_rejected_for_alert_review(self) -> None:
        with pytest.raises(AlertRouterError, match="not compatible"):
            validate_route_mode("request_alert_review", "run_unapproved_plan")

    def test_run_unapproved_plan_rejected_for_data_refresh(self) -> None:
        with pytest.raises(AlertRouterError, match="not compatible"):
            validate_route_mode("request_data_refresh", "run_unapproved_plan")

    def test_invalid_route_mode_rejected(self) -> None:
        with pytest.raises(AlertRouterError, match="not valid"):
            validate_route_mode("log_only", "execute_now")

    def test_all_allowed_route_modes_present(self) -> None:
        assert "record_only" in ALLOWED_ROUTE_MODES
        assert "run_refresh" in ALLOWED_ROUTE_MODES
        assert "run_unapproved_plan" in ALLOWED_ROUTE_MODES


# ---------------------------------------------------------------------------
# scripts_for_route
# ---------------------------------------------------------------------------

class TestScriptsForRoute:
    def test_record_only_returns_empty_for_all_next_steps(self) -> None:
        for ns in ALLOWED_NEXT_STEPS:
            assert scripts_for_route(ns, "record_only") == []

    def test_run_refresh_returns_refresh_commands_for_data_refresh(self) -> None:
        scripts = scripts_for_route("request_data_refresh", "run_refresh")
        assert any("refresh_data" in s for s in scripts)
        assert any("monitor_positions" in s for s in scripts)

    def test_run_refresh_returns_refresh_commands_for_unapproved_plan(self) -> None:
        scripts = scripts_for_route("request_trade_plan_unapproved", "run_refresh")
        assert any("refresh_data" in s for s in scripts)
        assert any("monitor_positions" in s for s in scripts)

    def test_run_unapproved_plan_returns_full_pipeline(self) -> None:
        scripts = scripts_for_route("request_trade_plan_unapproved", "run_unapproved_plan")
        assert any("refresh_data" in s for s in scripts)
        assert any("monitor_positions" in s for s in scripts)
        assert any("scan_triggers" in s for s in scripts)
        assert any("generate_trade_plan" in s for s in scripts)

    def test_run_unapproved_plan_no_execute_paper(self) -> None:
        scripts = scripts_for_route("request_trade_plan_unapproved", "run_unapproved_plan")
        for s in scripts:
            assert "execute_paper" not in s

    def test_run_unapproved_plan_no_approve_paper(self) -> None:
        scripts = scripts_for_route("request_trade_plan_unapproved", "run_unapproved_plan")
        for s in scripts:
            assert "--approve-paper" not in s

    def test_run_refresh_no_execute_paper(self) -> None:
        scripts = scripts_for_route("request_data_refresh", "run_refresh")
        for s in scripts:
            assert "execute_paper" not in s

    def test_run_refresh_returns_empty_for_log_only(self) -> None:
        # run_refresh is incompatible with log_only, but scripts_for_route
        # returns [] for unrecognised combos rather than raising
        assert scripts_for_route("log_only", "run_refresh") == []

    def test_run_refresh_returns_only_refresh_not_scan_or_plan(self) -> None:
        scripts = scripts_for_route("request_data_refresh", "run_refresh")
        for s in scripts:
            assert "scan_triggers" not in s
            assert "generate_trade_plan" not in s


# ---------------------------------------------------------------------------
# check_trade_plan_not_approved
# ---------------------------------------------------------------------------

class TestCheckTradePlanNotApproved:
    def test_absent_file_is_safe(self, tmp_path: Path) -> None:
        check_trade_plan_not_approved(tmp_path / "trade_plan.json")  # must not raise

    def test_unapproved_plan_passes(self, tmp_path: Path) -> None:
        plan = {"approval": {"approved_for_execution": False}}
        p = tmp_path / "trade_plan.json"
        p.write_text(json.dumps(plan))
        check_trade_plan_not_approved(p)  # must not raise

    def test_approved_plan_raises(self, tmp_path: Path) -> None:
        plan = {"approval": {"approved_for_execution": True}}
        p = tmp_path / "trade_plan.json"
        p.write_text(json.dumps(plan))
        with pytest.raises(AlertRouterError, match="approved_for_execution=True"):
            check_trade_plan_not_approved(p)

    def test_missing_approval_key_is_safe(self, tmp_path: Path) -> None:
        plan = {"orders": []}
        p = tmp_path / "trade_plan.json"
        p.write_text(json.dumps(plan))
        check_trade_plan_not_approved(p)  # must not raise

    def test_null_approval_is_safe(self, tmp_path: Path) -> None:
        plan = {"approval": None}
        p = tmp_path / "trade_plan.json"
        p.write_text(json.dumps(plan))
        check_trade_plan_not_approved(p)  # must not raise


# ---------------------------------------------------------------------------
# Safety invariants — source inspection
# ---------------------------------------------------------------------------

class TestRouterSourceSafety:
    def _src(self) -> str:
        import trading_os.research.alert_router as mod
        return Path(mod.__file__).read_text(encoding="utf-8")

    def test_no_execute_paper_import(self) -> None:
        src = self._src()
        assert not re.search(r"^\s*(import|from)\s+.*execute_paper", src, re.MULTILINE)

    def test_no_paper_executor_import(self) -> None:
        src = self._src()
        assert not re.search(r"^\s*(import|from)\s+.*paper_executor", src, re.MULTILINE)

    def test_no_approve_paper_true_call(self) -> None:
        src = self._src()
        assert not re.search(r"\bapprove_paper\s*=\s*True\b\s*[,)]", src)

    def test_no_approved_for_execution_true_literal(self) -> None:
        src = self._src()
        # Reject: "approved_for_execution": True  or  approved_for_execution=True,
        assert not re.search(r'"approved_for_execution"\s*:\s*True', src)
        assert not re.search(r"\bapproved_for_execution\s*=\s*True\b\s*[,)]", src)

    def test_no_subprocess_call_in_module(self) -> None:
        src = self._src()
        assert not re.search(r"^\s*(import|from)\s+subprocess\b", src, re.MULTILINE)

    def test_suggested_commands_have_no_approve_paper(self) -> None:
        for cmd in SUGGESTED_PIPELINE_COMMANDS:
            assert "--approve-paper" not in cmd

    def test_suggested_commands_have_no_execute_paper(self) -> None:
        for cmd in SUGGESTED_PIPELINE_COMMANDS:
            assert "execute_paper" not in cmd

    def test_suggested_refresh_commands_have_no_execute_paper(self) -> None:
        for cmd in SUGGESTED_REFRESH_COMMANDS:
            assert "execute_paper" not in cmd


# ---------------------------------------------------------------------------
# route_alert — safety block invariants
# ---------------------------------------------------------------------------

class TestRouteAlertSafetyBlock:
    def test_safety_block_always_present(self, tmp_path: Path) -> None:
        result = _route(tmp_path, SAFE_ALERT)
        assert "safety" in result

    def test_safety_execute_paper_never_called(self, tmp_path: Path) -> None:
        result = _route(tmp_path, SAFE_ALERT)
        assert result["safety"]["execute_paper_called"] is False

    def test_safety_approve_paper_never_passed(self, tmp_path: Path) -> None:
        result = _route(tmp_path, SAFE_ALERT)
        assert result["safety"]["approve_paper_passed"] is False

    def test_safety_trade_execution_allowed_false(self, tmp_path: Path) -> None:
        result = _route(tmp_path, SAFE_ALERT)
        assert result["safety"]["trade_execution_allowed"] is False

    def test_safety_blocked_by_default_true(self, tmp_path: Path) -> None:
        result = _route(tmp_path, SAFE_ALERT)
        assert result["safety"]["blocked_by_default"] is True

    def test_rejected_alert_does_not_route(self, tmp_path: Path) -> None:
        with pytest.raises(AlertRouterError):
            _route(tmp_path, _make_alert(trade_execution_allowed=True))

    def test_route_record_has_approved_trade_plan_created_false(self, tmp_path: Path) -> None:
        result = _route(tmp_path, SAFE_ALERT)
        assert result["approved_trade_plan_created"] is False

    def test_route_record_has_execution_called_false(self, tmp_path: Path) -> None:
        result = _route(tmp_path, SAFE_ALERT)
        assert result["execution_called"] is False


# ---------------------------------------------------------------------------
# log_only
# ---------------------------------------------------------------------------

class TestRouteLogOnly:
    def test_log_only_accepted(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="log_only"))
        assert result["action_taken"] == "logged"

    def test_log_only_writes_route_record(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="log_only"))
        assert result["artifact_path"] is not None
        assert Path(result["artifact_path"]).exists()

    def test_log_only_route_record_in_routes_subdir(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="log_only"))
        assert "routes" in result["artifact_path"]

    def test_log_only_route_record_valid_json(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="log_only"))
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["alert_id"] == "test-router-001"
        assert parsed["next_step"] == "log_only"

    def test_log_only_route_record_never_approved(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="log_only"))
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["approved_trade_plan_created"] is False
        assert parsed["execution_called"] is False

    def test_log_only_no_suggested_scripts(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="log_only"))
        assert result["suggested_commands"] == []

    def test_log_only_no_scripts_run(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="log_only"))
        assert result["scripts_run"] == []

    def test_log_only_trigger_log_appended(self, tmp_path: Path) -> None:
        log = tmp_path / "TRIGGER-LOG.md"
        _route(tmp_path, _make_alert(next_step="log_only"))
        assert log.exists()
        assert "Alert routed" in log.read_text()

    def test_log_only_signal_log_appended(self, tmp_path: Path) -> None:
        sig = tmp_path / "SIGNAL-LOG.md"
        _route(tmp_path, _make_alert(next_step="log_only"))
        assert sig.exists()
        assert "log_only" in sig.read_text()

    def test_log_only_signal_log_has_no_execution_claims(self, tmp_path: Path) -> None:
        sig = tmp_path / "SIGNAL-LOG.md"
        _route(tmp_path, _make_alert(next_step="log_only"))
        content = sig.read_text()
        assert "approved_for_execution=True" not in content
        assert "execute_paper" not in content

    def test_log_only_research_context_not_written(self, tmp_path: Path) -> None:
        ctx = tmp_path / "RESEARCH-CONTEXT.md"
        _route(tmp_path, _make_alert(next_step="log_only"))
        assert not ctx.exists()

    def test_log_only_only_record_only_mode_allowed(self, tmp_path: Path) -> None:
        with pytest.raises(AlertRouterError, match="not compatible"):
            _route(tmp_path, _make_alert(next_step="log_only"), route_mode="run_refresh")


# ---------------------------------------------------------------------------
# request_alert_review
# ---------------------------------------------------------------------------

class TestRouteAlertReview:
    def test_review_action_taken(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_alert_review"))
        assert result["action_taken"] == "review_requested"

    def test_review_route_record_written(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_alert_review"))
        assert result["artifact_path"] is not None
        assert Path(result["artifact_path"]).exists()

    def test_review_route_record_valid_json(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_alert_review"))
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["alert_id"] == "test-router-001"

    def test_review_route_record_in_routes_subdir(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_alert_review"))
        assert "routes" in result["artifact_path"]

    def test_review_route_record_never_approved(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_alert_review"))
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["approved_trade_plan_created"] is False
        assert parsed["execution_called"] is False

    def test_review_no_suggested_scripts(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_alert_review"))
        assert result["suggested_commands"] == []

    def test_review_trigger_log_appended(self, tmp_path: Path) -> None:
        log = tmp_path / "TRIGGER-LOG.md"
        _route(tmp_path, _make_alert(next_step="request_alert_review"))
        assert "Alert routed" in log.read_text()

    def test_review_signal_log_appended(self, tmp_path: Path) -> None:
        sig = tmp_path / "SIGNAL-LOG.md"
        _route(tmp_path, _make_alert(next_step="request_alert_review"))
        assert sig.exists()

    def test_review_research_context_appended(self, tmp_path: Path) -> None:
        ctx = tmp_path / "RESEARCH-CONTEXT.md"
        _route(tmp_path, _make_alert(next_step="request_alert_review"))
        assert ctx.exists()
        content = ctx.read_text()
        assert "Review needed" in content
        assert "AAPL" in content

    def test_review_research_context_has_no_execution_claims(self, tmp_path: Path) -> None:
        ctx = tmp_path / "RESEARCH-CONTEXT.md"
        _route(tmp_path, _make_alert(next_step="request_alert_review"))
        content = ctx.read_text()
        assert "approved_for_execution" not in content
        assert "execute_paper" not in content

    def test_review_only_record_only_mode_allowed(self, tmp_path: Path) -> None:
        with pytest.raises(AlertRouterError, match="not compatible"):
            _route(
                tmp_path,
                _make_alert(next_step="request_alert_review"),
                route_mode="run_refresh",
            )


# ---------------------------------------------------------------------------
# request_data_refresh
# ---------------------------------------------------------------------------

class TestRouteDataRefresh:
    def test_refresh_action_taken(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        assert result["action_taken"] == "refresh_requested"

    def test_refresh_route_record_written(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        assert result["artifact_path"] is not None
        assert Path(result["artifact_path"]).exists()

    def test_refresh_route_record_valid_json(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["alert_id"] == "test-router-001"

    def test_refresh_route_record_in_routes_subdir(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        assert "routes" in result["artifact_path"]

    def test_refresh_route_record_never_approved(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["approved_trade_plan_created"] is False

    def test_refresh_record_only_no_suggested_scripts(self, tmp_path: Path) -> None:
        # record_only: CLI won't run anything; suggested_scripts for refresh returns empty
        # (scripts_for_route handles execution; route_alert uses _full_suggestions_for)
        result = _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        assert result["scripts_run"] == []

    def test_refresh_trigger_log_appended(self, tmp_path: Path) -> None:
        log = tmp_path / "TRIGGER-LOG.md"
        _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        assert "Alert routed" in log.read_text()

    def test_refresh_signal_log_not_touched(self, tmp_path: Path) -> None:
        sig = tmp_path / "SIGNAL-LOG.md"
        _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        assert not sig.exists()

    def test_refresh_record_only_accepted(self, tmp_path: Path) -> None:
        _route(tmp_path, _make_alert(next_step="request_data_refresh"), route_mode="record_only")

    def test_refresh_run_refresh_accepted(self, tmp_path: Path) -> None:
        # Should not raise (route_mode is compatible)
        _route(tmp_path, _make_alert(next_step="request_data_refresh"), route_mode="run_refresh")

    def test_refresh_run_unapproved_plan_rejected(self, tmp_path: Path) -> None:
        with pytest.raises(AlertRouterError, match="not compatible"):
            _route(
                tmp_path,
                _make_alert(next_step="request_data_refresh"),
                route_mode="run_unapproved_plan",
            )

    def test_refresh_scripts_for_route_record_only_empty(self) -> None:
        assert scripts_for_route("request_data_refresh", "record_only") == []

    def test_refresh_scripts_for_route_run_refresh_has_refresh(self) -> None:
        scripts = scripts_for_route("request_data_refresh", "run_refresh")
        assert any("refresh_data" in s for s in scripts)
        assert any("monitor_positions" in s for s in scripts)
        assert not any("execute_paper" in s for s in scripts)


# ---------------------------------------------------------------------------
# request_trade_plan_unapproved
# ---------------------------------------------------------------------------

class TestRouteTradePlanUnapproved:
    def test_plan_action_taken(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        assert result["action_taken"] == "plan_requested"

    def test_plan_route_record_written(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        assert result["artifact_path"] is not None
        assert Path(result["artifact_path"]).exists()

    def test_plan_route_record_in_routes_subdir(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        assert "routes" in result["artifact_path"]

    def test_plan_route_record_approved_trade_plan_false(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["approved_trade_plan_created"] is False
        assert parsed["execution_called"] is False

    def test_plan_suggested_commands_present(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        assert len(result["suggested_commands"]) > 0

    def test_plan_suggested_commands_no_approve_paper(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        for cmd in result["suggested_commands"]:
            assert "--approve-paper" not in cmd

    def test_plan_suggested_commands_no_execute_paper(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        for cmd in result["suggested_commands"]:
            assert "execute_paper" not in cmd

    def test_plan_trigger_log_appended(self, tmp_path: Path) -> None:
        log = tmp_path / "TRIGGER-LOG.md"
        _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        assert "Alert routed" in log.read_text()

    def test_plan_signal_log_appended(self, tmp_path: Path) -> None:
        sig = tmp_path / "SIGNAL-LOG.md"
        _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        assert sig.exists()
        content = sig.read_text()
        assert "UNAPPROVED" in content
        assert "AAPL" in content

    def test_plan_signal_log_not_approved(self, tmp_path: Path) -> None:
        sig = tmp_path / "SIGNAL-LOG.md"
        _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        content = sig.read_text()
        assert "approved_for_execution=True" not in content

    def test_plan_record_only_accepted(self, tmp_path: Path) -> None:
        _route(
            tmp_path,
            _make_alert(next_step="request_trade_plan_unapproved"),
            route_mode="record_only",
        )

    def test_plan_run_refresh_accepted(self, tmp_path: Path) -> None:
        _route(
            tmp_path,
            _make_alert(next_step="request_trade_plan_unapproved"),
            route_mode="run_refresh",
        )

    def test_plan_run_unapproved_plan_accepted(self, tmp_path: Path) -> None:
        _route(
            tmp_path,
            _make_alert(next_step="request_trade_plan_unapproved"),
            route_mode="run_unapproved_plan",
        )

    def test_plan_scripts_for_run_unapproved_plan_includes_all_steps(self) -> None:
        scripts = scripts_for_route("request_trade_plan_unapproved", "run_unapproved_plan")
        script_names = " ".join(scripts)
        assert "refresh_data" in script_names
        assert "monitor_positions" in script_names
        assert "scan_triggers" in script_names
        assert "generate_trade_plan" in script_names
        assert "execute_paper" not in script_names
        assert "--approve-paper" not in script_names


# ---------------------------------------------------------------------------
# route_alert — route record full schema
# ---------------------------------------------------------------------------

class TestRouteRecordSchema:
    def test_route_record_has_route_id(self, tmp_path: Path) -> None:
        result = _route(tmp_path, SAFE_ALERT)
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert "route_id" in parsed
        assert parsed["route_id"].startswith("route_")

    def test_route_record_has_required_fields(self, tmp_path: Path) -> None:
        result = _route(tmp_path, SAFE_ALERT)
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        required = [
            "route_id", "routed_at", "alert_id", "symbol", "next_step",
            "route_mode", "action_taken", "scripts_run", "safety_checks",
            "blocked", "block_reason", "generated_files", "trade_execution_allowed",
            "approved_trade_plan_created", "execution_called",
        ]
        for field in required:
            assert field in parsed, f"missing field: {field}"

    def test_route_record_trade_execution_allowed_false(self, tmp_path: Path) -> None:
        result = _route(tmp_path, SAFE_ALERT)
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["trade_execution_allowed"] is False

    def test_route_record_not_blocked(self, tmp_path: Path) -> None:
        result = _route(tmp_path, SAFE_ALERT)
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["blocked"] is False
        assert parsed["block_reason"] is None

    def test_route_record_scripts_run_empty_at_creation(self, tmp_path: Path) -> None:
        result = _route(tmp_path, SAFE_ALERT)
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["scripts_run"] == []

    def test_route_result_has_route_record_path(self, tmp_path: Path) -> None:
        result = _route(tmp_path, SAFE_ALERT)
        assert "route_record_path" in result
        assert Path(result["route_record_path"]).exists()


# ---------------------------------------------------------------------------
# Execution cannot be triggered via external alert
# ---------------------------------------------------------------------------

class TestNoExecutionPath:
    def test_execution_rejected_via_trade_execution_true(self, tmp_path: Path) -> None:
        with pytest.raises(AlertRouterError, match="trade_execution_allowed must be false"):
            _route(tmp_path, _make_alert(trade_execution_allowed=True))

    def test_execution_rejected_via_execute_paper_field(self, tmp_path: Path) -> None:
        with pytest.raises(AlertRouterError, match="execution intent field"):
            _route(tmp_path, _make_alert(execute_paper=True))

    def test_execution_rejected_via_submit_order_field(self, tmp_path: Path) -> None:
        with pytest.raises(AlertRouterError, match="execution intent field"):
            _route(tmp_path, _make_alert(submit_order=True))

    def test_no_route_record_written_when_rejected(self, tmp_path: Path) -> None:
        routes_dir = tmp_path / "alerts" / "routes"
        try:
            _route(tmp_path, _make_alert(trade_execution_allowed=True))
        except AlertRouterError:
            pass
        assert not routes_dir.exists() or list(routes_dir.glob("*.json")) == []

    def test_all_results_have_execute_paper_false(self, tmp_path: Path) -> None:
        for i, ns in enumerate(sorted(ALLOWED_NEXT_STEPS)):
            alert = _make_alert(next_step=ns, alert_id=f"exec-test-{i}")
            result = _route(tmp_path, alert)
            assert result["safety"]["execute_paper_called"] is False

    def test_all_results_have_approve_paper_false(self, tmp_path: Path) -> None:
        for i, ns in enumerate(sorted(ALLOWED_NEXT_STEPS)):
            alert = _make_alert(next_step=ns, alert_id=f"ap-test-{i}")
            result = _route(tmp_path, alert)
            assert result["safety"]["approve_paper_passed"] is False

    def test_no_route_record_has_approved_trade_plan_true(self, tmp_path: Path) -> None:
        for i, ns in enumerate(sorted(ALLOWED_NEXT_STEPS)):
            alert = _make_alert(next_step=ns, alert_id=f"art-test-{i}")
            result = _route(tmp_path, alert)
            parsed = json.loads(Path(result["artifact_path"]).read_text())
            assert parsed.get("approved_trade_plan_created") is not True

    def test_no_test_path_triggers_execute_paper(self) -> None:
        """Source inspection: no test in this file uses subprocess to invoke execute_paper."""
        src = Path(__file__).read_text(encoding="utf-8")
        # No subprocess call targets execute_paper
        assert not re.search(r'subprocess\.[^(]+\([^)]*execute_paper', src)
        # The module under test must not import execute_paper
        import trading_os.research.alert_router as mod
        mod_src = Path(mod.__file__).read_text(encoding="utf-8")
        assert not re.search(r"^\s*(import|from)\s+.*execute_paper", mod_src, re.MULTILINE)
