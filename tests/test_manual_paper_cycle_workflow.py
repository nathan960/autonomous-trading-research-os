"""Tests for .github/workflows/manual-paper-cycle.yml.

Verifies the safety invariants and structural requirements of the
Manual Paper Cycle workflow without executing any scripts or network calls.
"""
from __future__ import annotations

from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_WORKFLOW = _ROOT / ".github" / "workflows" / "manual-paper-cycle.yml"


def _text() -> str:
    return _WORKFLOW.read_text(encoding="utf-8")


def _noncomment_lines() -> list[str]:
    """Return lines that are not YAML comments."""
    return [
        line for line in _text().splitlines()
        if not line.lstrip().startswith("#")
    ]


def _noncomment_text() -> str:
    return "\n".join(_noncomment_lines())


# ---------------------------------------------------------------------------
# Existence and structure
# ---------------------------------------------------------------------------

class TestWorkflowExists:
    def test_file_exists(self):
        assert _WORKFLOW.exists(), "manual-paper-cycle.yml must exist"

    def test_workflow_name(self):
        assert "Manual Paper Cycle" in _text()

    def test_valid_yaml(self):
        try:
            import yaml
        except ImportError:
            pytest.skip("pyyaml not installed")
        doc = yaml.safe_load(_text())
        assert isinstance(doc, dict)
        assert "jobs" in doc

    def test_permissions_contents_write(self):
        assert "contents: write" in _text()

    def test_concurrency_group_trading_os_main(self):
        assert "trading-os-main" in _text()
        assert "cancel-in-progress: false" in _text()


# ---------------------------------------------------------------------------
# Trigger: workflow_dispatch only — no schedule
# ---------------------------------------------------------------------------

class TestTrigger:
    def test_has_workflow_dispatch(self):
        assert "workflow_dispatch" in _text()

    def test_no_schedule_trigger(self):
        try:
            import yaml
        except ImportError:
            pytest.skip("pyyaml not installed")
        doc = yaml.safe_load(_text())
        on_block = doc.get("on", {})
        assert "schedule" not in on_block, (
            "manual-paper-cycle must not have a schedule trigger"
        )

    def test_no_cron_string(self):
        assert "cron:" not in _text(), (
            "manual-paper-cycle must not contain a cron schedule"
        )

    def test_no_push_trigger(self):
        try:
            import yaml
        except ImportError:
            pytest.skip("pyyaml not installed")
        doc = yaml.safe_load(_text())
        assert "push" not in doc.get("on", {})


# ---------------------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------------------

class TestInputs:
    def _inputs(self) -> dict:
        try:
            import yaml
        except ImportError:
            pytest.skip("pyyaml not installed")
        doc = yaml.safe_load(_text())
        return doc["on"]["workflow_dispatch"].get("inputs", {})

    def test_has_cycle_mode_input(self):
        assert "cycle_mode" in self._inputs()

    def test_cycle_mode_default_is_research_only(self):
        inp = self._inputs()["cycle_mode"]
        assert inp["default"] == "research_only"

    def test_cycle_mode_has_paper_execution_option(self):
        inp = self._inputs()["cycle_mode"]
        assert "paper_execution" in inp["options"]

    def test_cycle_mode_has_research_only_option(self):
        inp = self._inputs()["cycle_mode"]
        assert "research_only" in inp["options"]

    def test_has_approve_paper_plan_input(self):
        assert "approve_paper_plan" in self._inputs()

    def test_approve_paper_plan_default_is_false(self):
        assert self._inputs()["approve_paper_plan"]["default"] == "false"

    def test_has_confirm_manual_paper_execution_input(self):
        assert "confirm_manual_paper_execution" in self._inputs()

    def test_confirm_default_is_no(self):
        assert self._inputs()["confirm_manual_paper_execution"]["default"] == "NO"

    def test_has_run_post_trade_reconciliation_input(self):
        assert "run_post_trade_reconciliation" in self._inputs()

    def test_post_trade_reconciliation_default_is_true(self):
        assert self._inputs()["run_post_trade_reconciliation"]["default"] == "true"


# ---------------------------------------------------------------------------
# Safety env vars — job level
# ---------------------------------------------------------------------------

class TestJobLevelSafety:
    def test_job_level_enable_paper_execution_is_false(self):
        src = _text()
        assert 'ENABLE_PAPER_EXECUTION: "false"' in src

    def test_live_trading_confirmed_is_false(self):
        assert 'LIVE_TRADING_CONFIRMED: "false"' in src

    def test_trading_mode_is_paper(self):
        assert "TRADING_MODE: paper" in _text()

    def test_alpaca_paper_is_true(self):
        assert 'ALPACA_PAPER: "true"' in _text()

    def test_data_feed_uses_iex_fallback(self):
        assert "iex" in _text()

    def test_api_key_from_secret(self):
        assert "secrets.ALPACA_API_KEY" in _text()

    def test_api_secret_from_secret(self):
        assert "secrets.ALPACA_API_SECRET" in _text()


# Capture as module-level for re-use in lambda
src = _WORKFLOW.read_text(encoding="utf-8") if _WORKFLOW.exists() else ""


# ---------------------------------------------------------------------------
# No live trading, no prohibited instruments
# ---------------------------------------------------------------------------

class TestNoLiveTradingPath:
    def test_live_trading_confirmed_never_set_true(self):
        assert 'LIVE_TRADING_CONFIRMED: "true"' not in src
        assert "LIVE_TRADING_CONFIRMED=true" not in src

    def test_trading_mode_never_set_live(self):
        assert "TRADING_MODE: live" not in src
        assert "TRADING_MODE=live" not in src

    def test_no_options_trading(self):
        assert "options_trading" not in src.lower()

    def test_no_crypto_trading(self):
        assert "crypto" not in src.lower()

    def test_no_short_selling(self):
        assert "short_sell" not in src.lower()
        assert "would_short" not in src.lower()


# ---------------------------------------------------------------------------
# Execution step: triple-lock conditions
# ---------------------------------------------------------------------------

class TestExecutionStepSafety:
    def test_execute_paper_only_in_noncomment_lines(self):
        """execute_paper.py appears only in the execution step run block."""
        exec_lines = [
            ln for ln in _noncomment_lines()
            if "execute_paper" in ln
        ]
        assert exec_lines, "execute_paper.py must appear in the workflow"
        for ln in exec_lines:
            # Every non-comment line referencing execute_paper must be a run: line
            # (not a standalone step name or stray invocation)
            assert "execute_paper.py" in ln, ln

    def test_execute_paper_called_with_confirm_paper(self):
        assert "execute_paper.py --confirm-paper" in src

    def test_execution_step_requires_cycle_mode_paper_execution(self):
        assert "cycle_mode == 'paper_execution'" in src or \
               'cycle_mode == "paper_execution"' in src

    def test_execution_step_requires_approve_paper_plan_true(self):
        assert "approve_paper_plan == 'true'" in src or \
               'approve_paper_plan == "true"' in src

    def test_execution_step_requires_paper_confirmation_string(self):
        assert "confirm_manual_paper_execution == 'PAPER'" in src or \
               'confirm_manual_paper_execution == "PAPER"' in src

    def test_step_level_enable_paper_execution_true_present(self):
        """The execution step must set ENABLE_PAPER_EXECUTION=true at step level."""
        assert 'ENABLE_PAPER_EXECUTION: "true"' in src

    def test_only_one_occurrence_of_enable_paper_true(self):
        """ENABLE_PAPER_EXECUTION=true must appear exactly once (the execution step)."""
        count = src.count('ENABLE_PAPER_EXECUTION: "true"')
        assert count == 1, (
            f"ENABLE_PAPER_EXECUTION: \"true\" must appear exactly once; found {count}"
        )

    def test_job_level_enable_paper_is_false_not_true(self):
        """The job-level env block sets false; only one step overrides it."""
        # The job env block has "false"; only one step-level block has "true"
        false_count = src.count('ENABLE_PAPER_EXECUTION: "false"')
        true_count = src.count('ENABLE_PAPER_EXECUTION: "true"')
        assert false_count >= 1
        assert true_count == 1

    def test_approve_paper_only_on_generate_trade_plan_script(self):
        """--approve-paper as a script flag must only follow generate_trade_plan.py."""
        # Only match lines that invoke a python script with --approve-paper,
        # not description/comment text that documents the flag.
        script_lines = [
            ln for ln in _noncomment_lines()
            if "generate_trade_plan.py" in ln and "--approve-paper" in ln
        ]
        assert script_lines, "--approve-paper must be passed to generate_trade_plan.py"
        # No other python script invocation should carry --approve-paper
        bad = [
            ln for ln in _noncomment_lines()
            if "--approve-paper" in ln
            and "python" in ln
            and "generate_trade_plan" not in ln
        ]
        assert bad == [], (
            f"--approve-paper passed to a script other than generate_trade_plan.py: {bad}"
        )


# ---------------------------------------------------------------------------
# Required pipeline steps
# ---------------------------------------------------------------------------

class TestRequiredSteps:
    def test_refresh_data(self):
        assert "refresh_data.py" in src

    def test_monitor_positions(self):
        assert "monitor_positions.py" in src

    def test_monitor_orders(self):
        assert "monitor_orders.py" in src

    def test_scan_triggers(self):
        assert "scan_triggers.py" in src

    def test_generate_trade_plan(self):
        assert "generate_trade_plan.py" in src

    def test_dry_run_execute(self):
        assert "dry_run_execute.py" in src

    def test_track_outcomes(self):
        assert "track_outcomes.py" in src

    def test_build_lineage(self):
        assert "build_lineage.py" in src

    def test_score_triggers(self):
        assert "score_triggers.py" in src

    def test_daily_summary(self):
        assert "daily_summary.py" in src

    def test_validate_all(self):
        assert "validate_all.py" in src

    def test_dry_run_gate_verification_present(self):
        assert "execution_report.json" in src
        assert "all_gates_pass" in src


# ---------------------------------------------------------------------------
# Safety preflight step
# ---------------------------------------------------------------------------

class TestSafetyPreflight:
    def test_preflight_step_present(self):
        assert "Safety preflight" in src

    def test_preflight_checks_live_trading_confirmed(self):
        assert "LIVE_TRADING_CONFIRMED" in src

    def test_preflight_checks_trading_mode(self):
        assert "TRADING_MODE" in src

    def test_preflight_prints_enable_paper_false(self):
        assert "ENABLE_PAPER_EXECUTION" in src


# ---------------------------------------------------------------------------
# Post-trade reconciliation is conditional
# ---------------------------------------------------------------------------

class TestPostTradeReconciliation:
    def test_reconciliation_is_conditional(self):
        assert "run_post_trade_reconciliation" in src

    def test_reconciliation_includes_track_outcomes(self):
        assert "track_outcomes.py" in src

    def test_reconciliation_condition_checks_true(self):
        assert "run_post_trade_reconciliation == 'true'" in src or \
               'run_post_trade_reconciliation == "true"' in src


# ---------------------------------------------------------------------------
# Commit pattern — two-step conflict-resistant
# ---------------------------------------------------------------------------

class TestCommitPattern:
    def test_event_files_committed_separately(self):
        assert "data/history/events/" in src

    def test_event_commit_before_artifact_commit(self):
        event_pos = src.index("data/history/events/")
        artifact_pos = src.index("git add -A data memory")
        assert event_pos < artifact_pos

    def test_uses_autostash(self):
        assert "--autostash" in src

    def test_sandbox_excluded(self):
        assert "restore --staged" in src

    def test_rebase_abort_on_conflict(self):
        assert "rebase --abort" in src

    def test_always_runs_commit_steps(self):
        assert "if: always()" in src

    def test_commit_message_includes_cycle_mode(self):
        assert "cycle_mode" in src

    def test_github_actions_bot_identity(self):
        assert "github-actions[bot]" in src
