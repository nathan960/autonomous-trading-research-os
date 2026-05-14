"""Tests verifying that paper-execution.yml is correctly deprecated.

Ensures:
- The workflow exists (historical reference preserved).
- It fails immediately via a deprecation block step.
- It contains no execution scripts — no orders can be submitted from it.
- It points users to manual-paper-cycle.yml.
- execute_paper.py is not called from this workflow.
- ENABLE_PAPER_EXECUTION is never set to true.
"""
from __future__ import annotations

from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_WORKFLOW = _ROOT / ".github" / "workflows" / "paper-execution.yml"
_REPLACEMENT = _ROOT / ".github" / "workflows" / "manual-paper-cycle.yml"


def _text() -> str:
    return _WORKFLOW.read_text(encoding="utf-8")


class TestDeprecatedWorkflowExists:
    def test_file_preserved_for_history(self):
        assert _WORKFLOW.exists(), (
            "paper-execution.yml must be kept for historical reference"
        )

    def test_replacement_workflow_exists(self):
        assert _REPLACEMENT.exists(), (
            "manual-paper-cycle.yml must exist as the replacement"
        )

    def test_workflow_name_unchanged(self):
        assert "Paper Execution" in _text()

    def test_workflow_dispatch_trigger_kept(self):
        assert "workflow_dispatch" in _text()

    def test_no_schedule_trigger(self):
        assert "cron:" not in _text()


class TestDeprecationBlock:
    def test_deprecation_step_present(self):
        src = _text()
        assert "Deprecation block" in src or "deprecated" in src.lower()

    def test_workflow_exits_with_failure(self):
        assert "exit 1" in _text()

    def test_points_to_replacement_workflow(self):
        src = _text()
        assert "manual-paper-cycle" in src or "Manual Paper Cycle" in src

    def test_deprecation_message_mentions_execution_path(self):
        src = _text().lower()
        assert "paper_execution" in src or "paper execution" in src

    def test_error_annotation_present(self):
        assert "::error::" in _text()


class TestNoExecutionPath:
    def test_execute_paper_not_called(self):
        lines = [
            ln for ln in _text().splitlines()
            if not ln.lstrip().startswith("#")
            and "execute_paper" in ln
            and "python" in ln
        ]
        assert lines == [], (
            f"execute_paper.py must not be invoked in deprecated workflow: {lines}"
        )

    def test_no_scripts_run(self):
        """No python scripts should be invoked — only the deprecation block."""
        run_lines = [
            ln for ln in _text().splitlines()
            if not ln.lstrip().startswith("#")
            and ln.strip().startswith("python ")
        ]
        assert run_lines == [], (
            f"No python scripts should run in deprecated workflow: {run_lines}"
        )

    def test_enable_paper_execution_never_true(self):
        src = _text()
        assert 'ENABLE_PAPER_EXECUTION: "true"' not in src
        assert "ENABLE_PAPER_EXECUTION=true" not in src

    def test_enable_paper_execution_is_false(self):
        assert 'ENABLE_PAPER_EXECUTION: "false"' in _text()

    def test_live_trading_confirmed_never_true(self):
        assert 'LIVE_TRADING_CONFIRMED: "true"' not in _text()
        assert "LIVE_TRADING_CONFIRMED=true" not in _text()

    def test_confirm_paper_flag_not_present(self):
        lines = [
            ln for ln in _text().splitlines()
            if not ln.lstrip().startswith("#")
            and "--confirm-paper" in ln
        ]
        assert lines == [], (
            "--confirm-paper must not appear in deprecated workflow"
        )

    def test_no_approve_paper_flag(self):
        lines = [
            ln for ln in _text().splitlines()
            if not ln.lstrip().startswith("#")
            and "python" in ln
            and "--approve-paper" in ln
        ]
        assert lines == [], (
            "--approve-paper must not be passed to any script in deprecated workflow"
        )
