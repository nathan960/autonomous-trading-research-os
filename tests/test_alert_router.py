"""Tests for the research-only alert router.

Key invariants proven here:
- Router rejects alerts where trade_execution_allowed is not exactly False.
- Router rejects alerts where blocked_by_default is not exactly True.
- log_only → logs, no artifact written.
- request_alert_review → writes review record.
- request_data_refresh → writes refresh record.
- request_trade_plan_unapproved → writes plan-request record, no --approve-paper in any command.
- Safety block in every result has execute_paper_called=False, approve_paper_passed=False.
- Source inspection: alert_router.py never imports execute_paper, never calls approve_paper.
- External alerts cannot trigger execution (proven by source + result inspection).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from trading_os.research.alert_router import (
    ALLOWED_NEXT_STEPS,
    SUGGESTED_PIPELINE_COMMANDS,
    AlertRouterError,
    route_alert,
    validate_alert_safety,
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


def _route(tmp_path: Path, alert: dict) -> dict:
    return route_alert(
        alert=alert,
        alerts_dir=tmp_path / "alerts",
        trigger_log_path=tmp_path / "TRIGGER-LOG.md",
        signal_log_path=tmp_path / "SIGNAL-LOG.md",
    )


# ---------------------------------------------------------------------------
# validate_alert_safety
# ---------------------------------------------------------------------------

class TestValidateAlertSafety:
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
        # Must be the boolean False, not the string "false"
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
        # Must be the boolean True, not the string "true"
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
        # Docstrings may mention the string; check for actual Python call syntax.
        src = self._src()
        assert not re.search(r"\bapprove_paper\s*=\s*True\b\s*[,)]", src)

    def test_no_approved_for_execution_true(self) -> None:
        src = self._src()
        # Dict literal: "approved_for_execution": True
        assert not re.search(r'"approved_for_execution"\s*:\s*True', src)
        # Keyword arg: approved_for_execution=True,  or  approved_for_execution=True)
        assert not re.search(r"\bapproved_for_execution\s*=\s*True\b\s*[,)]", src)

    def test_no_subprocess_call_in_module(self) -> None:
        # The pure module must not import subprocess — the CLI script does that.
        src = self._src()
        assert not re.search(r"^\s*(import|from)\s+subprocess\b", src, re.MULTILINE)

    def test_suggested_commands_have_no_approve_paper(self) -> None:
        for cmd in SUGGESTED_PIPELINE_COMMANDS:
            assert "--approve-paper" not in cmd

    def test_suggested_commands_have_no_execute_paper(self) -> None:
        for cmd in SUGGESTED_PIPELINE_COMMANDS:
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


# ---------------------------------------------------------------------------
# log_only
# ---------------------------------------------------------------------------

class TestRouteLogOnly:
    def test_log_only_accepted(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="log_only"))
        assert result["action_taken"] == "logged"

    def test_log_only_no_artifact(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="log_only"))
        assert result["artifact_path"] is None

    def test_log_only_no_artifact_file(self, tmp_path: Path) -> None:
        alerts_dir = tmp_path / "alerts"
        _route(tmp_path, _make_alert(next_step="log_only"))
        # No files under alerts subdir (no review/refresh/plan subdirs)
        if alerts_dir.exists():
            nested = list(alerts_dir.rglob("*.json"))
            assert nested == []

    def test_log_only_no_suggested_commands(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="log_only"))
        assert result["suggested_commands"] == []

    def test_log_only_trigger_log_appended(self, tmp_path: Path) -> None:
        log = tmp_path / "TRIGGER-LOG.md"
        _route(tmp_path, _make_alert(next_step="log_only"))
        assert log.exists()
        assert "Alert routed" in log.read_text()

    def test_log_only_signal_log_not_touched(self, tmp_path: Path) -> None:
        sig = tmp_path / "SIGNAL-LOG.md"
        _route(tmp_path, _make_alert(next_step="log_only"))
        assert not sig.exists()


# ---------------------------------------------------------------------------
# request_alert_review
# ---------------------------------------------------------------------------

class TestRouteAlertReview:
    def test_review_action_taken(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_alert_review"))
        assert result["action_taken"] == "review_requested"

    def test_review_artifact_written(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_alert_review"))
        assert result["artifact_path"] is not None
        assert Path(result["artifact_path"]).exists()

    def test_review_artifact_valid_json(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_alert_review"))
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["alert_id"] == "test-router-001"

    def test_review_artifact_has_forced_flags(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_alert_review"))
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["trade_execution_allowed"] is False
        assert parsed["blocked_by_default"] is True

    def test_review_artifact_in_review_requests_subdir(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_alert_review"))
        assert "review-requests" in result["artifact_path"]

    def test_review_no_suggested_commands(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_alert_review"))
        assert result["suggested_commands"] == []

    def test_review_trigger_log_appended(self, tmp_path: Path) -> None:
        log = tmp_path / "TRIGGER-LOG.md"
        _route(tmp_path, _make_alert(next_step="request_alert_review"))
        assert "Alert routed" in log.read_text()


# ---------------------------------------------------------------------------
# request_data_refresh
# ---------------------------------------------------------------------------

class TestRouteDataRefresh:
    def test_refresh_action_taken(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        assert result["action_taken"] == "refresh_requested"

    def test_refresh_artifact_written(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        assert result["artifact_path"] is not None
        assert Path(result["artifact_path"]).exists()

    def test_refresh_artifact_valid_json(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["alert_id"] == "test-router-001"

    def test_refresh_artifact_has_forced_flags(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["trade_execution_allowed"] is False
        assert parsed["blocked_by_default"] is True

    def test_refresh_artifact_in_refresh_requests_subdir(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        assert "refresh-requests" in result["artifact_path"]

    def test_refresh_no_suggested_commands(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        assert result["suggested_commands"] == []

    def test_refresh_trigger_log_appended(self, tmp_path: Path) -> None:
        log = tmp_path / "TRIGGER-LOG.md"
        _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        assert "Alert routed" in log.read_text()

    def test_refresh_signal_log_not_touched(self, tmp_path: Path) -> None:
        sig = tmp_path / "SIGNAL-LOG.md"
        _route(tmp_path, _make_alert(next_step="request_data_refresh"))
        assert not sig.exists()


# ---------------------------------------------------------------------------
# request_trade_plan_unapproved
# ---------------------------------------------------------------------------

class TestRouteTradeplanUnapproved:
    def test_plan_action_taken(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        assert result["action_taken"] == "plan_requested"

    def test_plan_artifact_written(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        assert result["artifact_path"] is not None
        assert Path(result["artifact_path"]).exists()

    def test_plan_artifact_approved_for_execution_false(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["approved_for_execution"] is False

    def test_plan_artifact_has_forced_flags(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        assert parsed["trade_execution_allowed"] is False
        assert parsed["blocked_by_default"] is True

    def test_plan_artifact_in_plan_requests_subdir(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        assert "plan-requests" in result["artifact_path"]

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

    def test_plan_artifact_suggested_commands_no_approve_paper(self, tmp_path: Path) -> None:
        result = _route(tmp_path, _make_alert(next_step="request_trade_plan_unapproved"))
        parsed = json.loads(Path(result["artifact_path"]).read_text())
        for cmd in parsed["suggested_commands"]:
            assert "--approve-paper" not in cmd

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
        assert "APPROVED" not in content.upper().replace("UNAPPROVED", "")


# ---------------------------------------------------------------------------
# Execution cannot be triggered via external alert
# ---------------------------------------------------------------------------

class TestNoExecutionPath:
    def test_execution_rejected_via_trade_execution_true(self, tmp_path: Path) -> None:
        """An alert claiming trade_execution_allowed=True must be rejected."""
        with pytest.raises(AlertRouterError, match="trade_execution_allowed must be false"):
            _route(tmp_path, _make_alert(trade_execution_allowed=True))

    def test_execution_rejected_no_artifact_written(self, tmp_path: Path) -> None:
        """No artifact is written when a rejected alert is attempted."""
        alerts_dir = tmp_path / "alerts"
        try:
            _route(tmp_path, _make_alert(trade_execution_allowed=True))
        except AlertRouterError:
            pass
        assert not alerts_dir.exists() or list(alerts_dir.rglob("*.json")) == []

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

    def test_no_artifact_has_approved_for_execution_true(self, tmp_path: Path) -> None:
        for i, ns in enumerate(sorted(ALLOWED_NEXT_STEPS)):
            alert = _make_alert(next_step=ns, alert_id=f"art-test-{i}")
            result = _route(tmp_path, alert)
            if result.get("artifact_path"):
                parsed = json.loads(Path(result["artifact_path"]).read_text())
                assert parsed.get("approved_for_execution") is not True
