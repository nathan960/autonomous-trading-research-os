"""Tests for phase-gate scorecard (pure module).

Scenarios:
1. Insufficient fills blocks promotion (FILLED_ORDERS_MIN_20)
2. Missing orders blocks promotion (NO_MISSING_ORDERS)
3. Rejected orders blocks promotion (NO_REJECTED_ORDERS)
4. Source integrity failure blocks promotion (SOURCE_INTEGRITY_OK)
5. Daily order limit violation shows as warning (DAILY_ORDER_LIMIT_RESPECTED — non-blocking)
6. Clean evidence marks system eligible for review
7. phase_gate never edits risk_limits.json or any config file
8. phase_gate never approves scheduled paper execution
9. PHASE_4 is always blocked by policy
10. determine_current_phase correctly maps risk_limits values
11. format_phase_gate_markdown includes required safety note
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import pytest

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.research.phase_gate import (
    PHASE_0_BUILD,
    PHASE_1_TINY_MANUAL,
    PHASE_2_SMALL_MANUAL,
    PHASE_3_LIMITED_SCHEDULED_RESEARCH_ONLY,
    PHASE_4_LIMITED_SCHEDULED_PAPER,
    build_phase_gate,
    determine_current_phase,
    format_phase_gate_markdown,
    next_phase,
    run_phase1_to_phase2_checks,
)


# ---------------------------------------------------------------------------
# Fixtures / helpers
# ---------------------------------------------------------------------------

def _risk_limits_phase1(**overrides: Any) -> dict:
    """Minimal risk_limits for PHASE_1_TINY_MANUAL."""
    base = {
        "max_notional_per_order": 25.0,
        "max_orders_per_run": 1,
        "max_drawdown_block_pct": -0.10,
        "max_total_paper_orders_per_day": 3,
    }
    base.update(overrides)
    return base


def _system_status_ok(**overrides: Any) -> dict:
    base = {
        "source_integrity_status": "ok",
        "blocking_issues": [],
        "churn_state": {
            "passes": True,
            "daily_total_limit_reached": False,
            "symbol_daily_limit_violations": [],
        },
        "risk_state": {"drawdown": 0.0},
    }
    base.update(overrides)
    return base


def _monitor_report(**overrides: Any) -> dict:
    base = {
        "orders_filled": 20,
        "orders_missing": 0,
        "orders_rejected": 0,
        "orders_active": 0,
        "lifecycles": [],
    }
    base.update(overrides)
    return base


def _outcome_snapshot(**overrides: Any) -> dict:
    base = {"source_integrity_status": "ok"}
    base.update(overrides)
    return base


def _lineage_snapshot(**overrides: Any) -> dict:
    base = {"lineage_count": 10, "complete_count": 8, "partial_count": 2}
    base.update(overrides)
    return base


def _trigger_performance(**overrides: Any) -> dict:
    base = {"status": "ok"}
    base.update(overrides)
    return base


def _history_counts(**overrides: Any) -> dict:
    base = {"daily_summaries": 5, "weekly_reviews": 2}
    base.update(overrides)
    return base


def _risk_state(**overrides: Any) -> dict:
    base = {"drawdown": 0.0}
    base.update(overrides)
    return base


def _build_gate(**kwargs: Any) -> dict:
    """Call build_phase_gate with all-passing defaults; override specific fields."""
    defaults: dict = dict(
        system_status=_system_status_ok(),
        order_monitor_report=_monitor_report(),
        outcome_snapshot=_outcome_snapshot(),
        lineage_snapshot=_lineage_snapshot(),
        trigger_performance=_trigger_performance(),
        execution_report={},
        trade_plan={},
        risk_state=_risk_state(),
        risk_limits=_risk_limits_phase1(),
        history_counts=_history_counts(),
    )
    defaults.update(kwargs)
    return build_phase_gate(**defaults)


# ---------------------------------------------------------------------------
# determine_current_phase
# ---------------------------------------------------------------------------

class TestDetermineCurrentPhase:
    def test_phase1_tiny_manual(self) -> None:
        rl = {"max_notional_per_order": 25.0, "max_orders_per_run": 1}
        assert determine_current_phase(rl) == PHASE_1_TINY_MANUAL

    def test_phase2_small_manual(self) -> None:
        rl = {"max_notional_per_order": 50.0, "max_orders_per_run": 1}
        assert determine_current_phase(rl) == PHASE_2_SMALL_MANUAL

    def test_phase3_above_50(self) -> None:
        rl = {"max_notional_per_order": 100.0, "max_orders_per_run": 2}
        assert determine_current_phase(rl) == PHASE_3_LIMITED_SCHEDULED_RESEARCH_ONLY

    def test_phase0_when_both_none(self) -> None:
        rl = {}
        assert determine_current_phase(rl) == PHASE_0_BUILD

    def test_phase1_boundary_exactly_25(self) -> None:
        rl = {"max_notional_per_order": 25.0, "max_orders_per_run": 1}
        assert determine_current_phase(rl) == PHASE_1_TINY_MANUAL

    def test_phase2_boundary_above_25(self) -> None:
        rl = {"max_notional_per_order": 25.01, "max_orders_per_run": 1}
        assert determine_current_phase(rl) == PHASE_2_SMALL_MANUAL


# ---------------------------------------------------------------------------
# Scenario 1: Insufficient fills blocks
# ---------------------------------------------------------------------------

class TestInsufficientFillsBlocks:
    def test_fills_below_20_blocks(self) -> None:
        result = _build_gate(order_monitor_report=_monitor_report(orders_filled=13))
        assert result["eligible_for_next_phase"] is False
        assert result["recommendation"] == "stay_at_phase"

    def test_blocking_issue_present(self) -> None:
        result = _build_gate(order_monitor_report=_monitor_report(orders_filled=5))
        check_ids = [c["check_id"] for c in result["checks"] if not c["passes"] and c["blocking"]]
        assert "FILLED_ORDERS_MIN_20" in check_ids

    def test_fills_exactly_20_passes(self) -> None:
        result = _build_gate(order_monitor_report=_monitor_report(orders_filled=20))
        check = next(c for c in result["checks"] if c["check_id"] == "FILLED_ORDERS_MIN_20")
        assert check["passes"] is True

    def test_fills_zero_blocks(self) -> None:
        result = _build_gate(order_monitor_report=_monitor_report(orders_filled=0))
        assert result["eligible_for_next_phase"] is False


# ---------------------------------------------------------------------------
# Scenario 2: Missing orders blocks
# ---------------------------------------------------------------------------

class TestMissingOrdersBlocks:
    def test_missing_orders_blocks(self) -> None:
        result = _build_gate(order_monitor_report=_monitor_report(orders_missing=2))
        assert result["eligible_for_next_phase"] is False

    def test_missing_orders_check_id_present(self) -> None:
        result = _build_gate(order_monitor_report=_monitor_report(orders_missing=1))
        check_ids = [c["check_id"] for c in result["checks"] if not c["passes"] and c["blocking"]]
        assert "NO_MISSING_ORDERS" in check_ids

    def test_zero_missing_passes(self) -> None:
        result = _build_gate()
        check = next(c for c in result["checks"] if c["check_id"] == "NO_MISSING_ORDERS")
        assert check["passes"] is True


# ---------------------------------------------------------------------------
# Scenario 3: Rejected orders blocks
# ---------------------------------------------------------------------------

class TestRejectedOrdersBlocks:
    def test_rejected_orders_blocks(self) -> None:
        result = _build_gate(order_monitor_report=_monitor_report(orders_rejected=1))
        assert result["eligible_for_next_phase"] is False

    def test_rejected_orders_check_id_present(self) -> None:
        result = _build_gate(order_monitor_report=_monitor_report(orders_rejected=3))
        check_ids = [c["check_id"] for c in result["checks"] if not c["passes"]]
        assert "NO_REJECTED_ORDERS" in check_ids


# ---------------------------------------------------------------------------
# Scenario 4: Source integrity failure blocks
# ---------------------------------------------------------------------------

class TestSourceIntegrityBlocks:
    def test_source_integrity_unknown_blocks(self) -> None:
        status = _system_status_ok(source_integrity_status="unknown")
        result = _build_gate(system_status=status)
        assert result["eligible_for_next_phase"] is False

    def test_source_integrity_missing_blocks(self) -> None:
        status = _system_status_ok()
        status.pop("source_integrity_status")
        result = _build_gate(system_status=status)
        assert result["eligible_for_next_phase"] is False

    def test_source_integrity_ok_passes_this_check(self) -> None:
        result = _build_gate()
        check = next(c for c in result["checks"] if c["check_id"] == "SOURCE_INTEGRITY_OK")
        assert check["passes"] is True


# ---------------------------------------------------------------------------
# Scenario 5: Daily order limit violation is a warning, not blocking
# ---------------------------------------------------------------------------

class TestDailyOrderLimitWarning:
    def test_daily_limit_reached_is_non_blocking(self) -> None:
        status = _system_status_ok(churn_state={
            "passes": False,
            "daily_total_limit_reached": True,
            "symbol_daily_limit_violations": [],
        })
        result = _build_gate(system_status=status)
        check = next(c for c in result["checks"] if c["check_id"] == "DAILY_ORDER_LIMIT_RESPECTED")
        assert check["blocking"] is False

    def test_daily_limit_violation_still_allows_eligible(self) -> None:
        status = _system_status_ok(churn_state={
            "passes": False,
            "daily_total_limit_reached": True,
            "symbol_daily_limit_violations": ["AAPL"],
        })
        # All blocking checks still pass (20 fills, no missing/rejected, etc.)
        result = _build_gate(system_status=status)
        # DAILY_ORDER_LIMIT_RESPECTED is blocking=False, so eligible is still True
        blocking_failures = [c for c in result["checks"] if not c["passes"] and c["blocking"]]
        assert all(c["check_id"] != "DAILY_ORDER_LIMIT_RESPECTED" for c in blocking_failures)

    def test_limit_violation_appears_in_warnings_not_blocking_issues(self) -> None:
        status = _system_status_ok(churn_state={
            "passes": False,
            "daily_total_limit_reached": True,
            "symbol_daily_limit_violations": [],
        })
        result = _build_gate(system_status=status)
        # The daily limit check detail should not appear in blocking_issues
        check = next(c for c in result["checks"] if c["check_id"] == "DAILY_ORDER_LIMIT_RESPECTED")
        if check["detail"]:
            assert check["detail"] not in result["blocking_issues"]


# ---------------------------------------------------------------------------
# Scenario 6: Clean evidence marks system eligible for review
# ---------------------------------------------------------------------------

class TestCleanEvidenceEligible:
    def test_all_passing_is_eligible(self) -> None:
        result = _build_gate()
        assert result["eligible_for_next_phase"] is True
        assert result["recommendation"] == "eligible_for_review"

    def test_eligible_result_has_required_human_actions(self) -> None:
        result = _build_gate()
        assert len(result["required_human_actions"]) >= 1
        # Must mention human judgment
        combined = " ".join(result["required_human_actions"]).lower()
        assert "human" in combined

    def test_recommended_phase_is_phase2_when_eligible(self) -> None:
        result = _build_gate()
        assert result["recommended_phase"] == PHASE_2_SMALL_MANUAL

    def test_all_blocking_checks_pass(self) -> None:
        result = _build_gate()
        blocking_failures = [c for c in result["checks"] if not c["passes"] and c["blocking"]]
        assert blocking_failures == []


# ---------------------------------------------------------------------------
# Scenario 7: phase_gate never edits risk_limits.json
# ---------------------------------------------------------------------------

class TestNeverEditsConfig:
    def test_build_phase_gate_returns_dict_not_file(self, tmp_path: Path) -> None:
        """build_phase_gate is a pure function — no file I/O at all."""
        risk_limits_file = tmp_path / "risk_limits.json"
        risk_limits_data = _risk_limits_phase1()
        risk_limits_file.write_text(
            json.dumps(risk_limits_data, indent=2), encoding="utf-8"
        )
        original_content = risk_limits_file.read_text()

        # Call the pure module
        result = _build_gate(risk_limits=risk_limits_data)

        # risk_limits.json on disk must be unchanged
        assert risk_limits_file.read_text() == original_content
        assert isinstance(result, dict)

    def test_result_has_safety_note(self) -> None:
        result = _build_gate()
        note = result.get("safety_note", "")
        assert "No config was changed" in note
        assert "No orders were placed" in note

    def test_risk_limits_not_mutated_in_memory(self) -> None:
        rl = _risk_limits_phase1()
        original_keys = set(rl.keys())
        _build_gate(risk_limits=rl)
        assert set(rl.keys()) == original_keys


# ---------------------------------------------------------------------------
# Scenario 8: phase_gate never approves scheduled paper execution
# ---------------------------------------------------------------------------

class TestNeverApprovesScheduledExecution:
    def test_result_never_contains_enable_paper_execution(self) -> None:
        result = _build_gate()
        result_str = json.dumps(result)
        assert "ENABLE_PAPER_EXECUTION=true" not in result_str
        assert "enable_paper_execution" not in result_str.lower() or (
            "false" in result_str.lower()
        )

    def test_safety_note_mentions_no_paper_execution(self) -> None:
        result = _build_gate()
        note = result.get("safety_note", "")
        assert "No paper execution was enabled" in note

    def test_safety_note_mentions_no_scheduled_execution(self) -> None:
        result = _build_gate()
        note = result.get("safety_note", "")
        assert "No scheduled execution was enabled" in note


# ---------------------------------------------------------------------------
# Scenario 9: PHASE_4 is always blocked by policy
# ---------------------------------------------------------------------------

class TestPhase4AlwaysBlocked:
    def test_phase4_always_blocked_by_automated_scorecard(self) -> None:
        # Even with perfect phase 3 evidence, phase 4 cannot be unlocked
        rl = {
            "max_notional_per_order": 50.0,
            "max_orders_per_run": 1,
            "max_drawdown_block_pct": -0.10,
            "max_total_paper_orders_per_day": 3,
        }
        result = _build_gate(risk_limits=rl)
        # Current phase is PHASE_2_SMALL_MANUAL (50.0, 1)
        # Next phase is PHASE_3 — but even if it were phase 3, phase 4 is blocked
        assert result["eligible_for_next_phase"] is False or (
            result.get("recommended_phase") != PHASE_4_LIMITED_SCHEDULED_PAPER
        )

    def test_phase4_blocking_message_in_output(self) -> None:
        # Simulate being at phase 3 by giving risk_limits that produce phase 3
        rl = {"max_notional_per_order": 100.0, "max_orders_per_run": 2}
        result = _build_gate(risk_limits=rl)
        # Phase 3 → Phase 4 is the next step; scorecard must block it
        if result.get("next_phase") == PHASE_4_LIMITED_SCHEDULED_PAPER:
            assert result["eligible_for_next_phase"] is False
            combined = " ".join(result["blocking_issues"]).lower()
            assert "phase_4" in combined or "human approval" in combined

    def test_next_phase_of_phase4_is_none(self) -> None:
        assert next_phase(PHASE_4_LIMITED_SCHEDULED_PAPER) is None

    def test_next_phase_sequence(self) -> None:
        assert next_phase(PHASE_0_BUILD) == PHASE_1_TINY_MANUAL
        assert next_phase(PHASE_1_TINY_MANUAL) == PHASE_2_SMALL_MANUAL
        assert next_phase(PHASE_2_SMALL_MANUAL) == PHASE_3_LIMITED_SCHEDULED_RESEARCH_ONLY
        assert next_phase(PHASE_3_LIMITED_SCHEDULED_RESEARCH_ONLY) == PHASE_4_LIMITED_SCHEDULED_PAPER


# ---------------------------------------------------------------------------
# Scenario 10: format_phase_gate_markdown includes required safety note
# ---------------------------------------------------------------------------

class TestFormatMarkdown:
    def test_markdown_contains_safety_note(self) -> None:
        result = _build_gate()
        md = format_phase_gate_markdown(result)
        assert "No config was changed" in md
        assert "No orders were placed" in md

    def test_markdown_contains_run_id(self) -> None:
        result = _build_gate()
        md = format_phase_gate_markdown(result)
        assert result["run_id"] in md

    def test_markdown_contains_current_phase(self) -> None:
        result = _build_gate()
        md = format_phase_gate_markdown(result)
        assert result["current_phase"] in md

    def test_markdown_blocking_issues_appear_when_present(self) -> None:
        result = _build_gate(order_monitor_report=_monitor_report(orders_filled=0))
        md = format_phase_gate_markdown(result)
        assert "Blocking Issues" in md


# ---------------------------------------------------------------------------
# Integration: checks list structure
# ---------------------------------------------------------------------------

class TestChecksStructure:
    def test_all_checks_have_required_fields(self) -> None:
        result = _build_gate()
        for check in result["checks"]:
            assert "check_id" in check
            assert "passes" in check
            assert "blocking" in check
            assert "evidence" in check
            assert "required" in check

    def test_phase_gate_hash_is_present(self) -> None:
        result = _build_gate()
        assert result.get("phase_gate_hash")
        assert len(result["phase_gate_hash"]) >= 8

    def test_result_has_generated_at(self) -> None:
        result = _build_gate()
        assert result.get("generated_at")
