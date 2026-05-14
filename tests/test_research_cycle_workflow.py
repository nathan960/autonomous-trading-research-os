"""Tests for .github/workflows/research-cycle.yml.

Verifies the safety invariants and structural requirements of the
Research Cycle workflow without executing any scripts or network calls.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_WORKFLOW = _ROOT / ".github" / "workflows" / "research-cycle.yml"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _workflow_text() -> str:
    return _WORKFLOW.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Existence and structure
# ---------------------------------------------------------------------------

class TestWorkflowExists:
    def test_file_exists(self):
        assert _WORKFLOW.exists(), "research-cycle.yml must exist"

    def test_file_is_nonempty(self):
        assert len(_workflow_text()) > 100

    def test_valid_yaml(self):
        try:
            import yaml
        except ImportError:
            pytest.skip("pyyaml not installed")
        doc = yaml.safe_load(_workflow_text())
        assert isinstance(doc, dict)
        assert "jobs" in doc

    def test_workflow_name(self):
        assert "Research Cycle" in _workflow_text()

    def test_has_workflow_dispatch_trigger(self):
        assert "workflow_dispatch" in _workflow_text()

    def test_has_schedule_trigger(self):
        assert "schedule" in _workflow_text()
        assert "cron" in _workflow_text()

    def test_permissions_contents_write(self):
        src = _workflow_text()
        assert "permissions" in src
        assert "contents: write" in src

    def test_concurrency_group_trading_os_main(self):
        src = _workflow_text()
        assert "trading-os-main" in src
        assert "cancel-in-progress: false" in src


# ---------------------------------------------------------------------------
# Safety invariants — hardcoded env vars
# ---------------------------------------------------------------------------

class TestSafetyEnvVars:
    def test_enable_paper_execution_is_false(self):
        src = _workflow_text()
        assert 'ENABLE_PAPER_EXECUTION: "false"' in src

    def test_live_trading_confirmed_is_false(self):
        src = _workflow_text()
        assert 'LIVE_TRADING_CONFIRMED: "false"' in src

    def test_trading_mode_is_paper(self):
        src = _workflow_text()
        assert "TRADING_MODE: paper" in src

    def test_alpaca_paper_is_true(self):
        src = _workflow_text()
        assert 'ALPACA_PAPER: "true"' in src

    def test_data_feed_uses_var_with_iex_default(self):
        src = _workflow_text()
        assert "ALPACA_DATA_FEED" in src
        assert "iex" in src


# ---------------------------------------------------------------------------
# No execution path
# ---------------------------------------------------------------------------

class TestNoExecutionPath:
    def test_execute_paper_never_called(self):
        # Strip comment lines before checking — the header comment names the file
        # for documentation; the invariant is that no `run:` step invokes it.
        run_lines = [
            line for line in _workflow_text().splitlines()
            if not line.lstrip().startswith("#") and "execute_paper" in line
        ]
        assert run_lines == [], (
            f"execute_paper.py must not appear outside comments: {run_lines}"
        )

    def test_approve_paper_never_passed(self):
        # Same: only check non-comment lines for --approve-paper
        run_lines = [
            line for line in _workflow_text().splitlines()
            if not line.lstrip().startswith("#") and "--approve-paper" in line
        ]
        assert run_lines == [], (
            f"--approve-paper must not appear outside comments: {run_lines}"
        )

    def test_enable_paper_execution_never_set_true(self):
        src = _workflow_text()
        assert 'ENABLE_PAPER_EXECUTION: "true"' not in src
        assert "ENABLE_PAPER_EXECUTION=true" not in src
        assert "ENABLE_PAPER_EXECUTION: true" not in src

    def test_live_trading_confirmed_never_set_true(self):
        src = _workflow_text()
        assert 'LIVE_TRADING_CONFIRMED: "true"' not in src
        assert "LIVE_TRADING_CONFIRMED=true" not in src

    def test_no_confirm_paper_flag(self):
        assert "--confirm-paper" not in _workflow_text()


# ---------------------------------------------------------------------------
# Safety preflight step
# ---------------------------------------------------------------------------

class TestSafetyPreflight:
    def test_preflight_step_present(self):
        assert "Safety preflight" in _workflow_text()

    def test_preflight_checks_enable_paper_execution(self):
        src = _workflow_text()
        assert "ENABLE_PAPER_EXECUTION" in src
        # Must fail (exit 1) if somehow set to true
        assert "exit 1" in src

    def test_preflight_checks_live_trading_confirmed(self):
        assert "LIVE_TRADING_CONFIRMED" in _workflow_text()

    def test_preflight_checks_trading_mode(self):
        assert "TRADING_MODE" in _workflow_text()


# ---------------------------------------------------------------------------
# Required pipeline steps
# ---------------------------------------------------------------------------

class TestRequiredSteps:
    def test_refresh_data_step(self):
        assert "refresh_data.py" in _workflow_text()

    def test_monitor_positions_step(self):
        assert "monitor_positions.py" in _workflow_text()

    def test_monitor_orders_step(self):
        assert "monitor_orders.py" in _workflow_text()

    def test_scan_triggers_step(self):
        assert "scan_triggers.py" in _workflow_text()

    def test_generate_trade_plan_step(self):
        assert "generate_trade_plan.py" in _workflow_text()

    def test_dry_run_execute_step(self):
        assert "dry_run_execute.py" in _workflow_text()

    def test_track_outcomes_step(self):
        assert "track_outcomes.py" in _workflow_text()

    def test_build_lineage_step(self):
        assert "build_lineage.py" in _workflow_text()

    def test_score_triggers_step(self):
        assert "score_triggers.py" in _workflow_text()

    def test_daily_summary_step(self):
        assert "daily_summary.py" in _workflow_text()

    def test_validate_all_step(self):
        assert "validate_all.py" in _workflow_text()


# ---------------------------------------------------------------------------
# Commit pattern — two-step conflict-resistant
# ---------------------------------------------------------------------------

class TestCommitPattern:
    def test_event_files_committed_first(self):
        src = _workflow_text()
        assert "data/history/events/" in src
        # Event commit step must appear before the main artifact commit
        event_pos = src.index("data/history/events/")
        artifact_pos = src.index("git add -A data memory")
        assert event_pos < artifact_pos, (
            "event files commit step must appear before the main artifact commit"
        )

    def test_uses_autostash_on_rebase(self):
        assert "--autostash" in _workflow_text()

    def test_sandbox_excluded_from_commit(self):
        src = _workflow_text()
        assert "data/sandbox" in src or "sandbox" in src
        assert "restore --staged" in src

    def test_rebase_conflict_handled_gracefully(self):
        src = _workflow_text()
        assert "rebase --abort" in src
        assert "rebuild_memory_logs.py" in src

    def test_always_runs_commit_step(self):
        src = _workflow_text()
        assert "if: always()" in src

    def test_uses_github_actions_bot_identity(self):
        src = _workflow_text()
        assert "github-actions[bot]" in src
        assert "41898282+github-actions[bot]@users.noreply.github.com" in src

    def test_commit_message_includes_run_id(self):
        assert "github.run_id" in _workflow_text()


# ---------------------------------------------------------------------------
# Alpaca credentials wired from secrets
# ---------------------------------------------------------------------------

class TestCredentials:
    def test_api_key_from_secret(self):
        assert "secrets.ALPACA_API_KEY" in _workflow_text()

    def test_api_secret_from_secret(self):
        assert "secrets.ALPACA_API_SECRET" in _workflow_text()

    def test_no_hardcoded_credentials(self):
        src = _workflow_text().lower()
        assert "api_key:" not in src.replace("alpaca_api_key", "")
        assert "secret:" not in src.replace("alpaca_api_secret", "")
