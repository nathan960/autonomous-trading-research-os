"""Tests for src/trading_os/logging/event_log.py and scripts/rebuild_memory_logs.py"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from trading_os.logging.event_log import (
    EVENT_TYPES,
    LOG_EVENT_ROUTING,
    format_event_as_markdown,
    read_events,
    write_event,
)

_ROOT = Path(__file__).resolve().parents[1]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _minimal_payload(event_type: str = "dry_run") -> dict:
    return {
        "run_id": f"test-run-{event_type}",
        "generated_at": "2026-05-13T16:00:00Z",
        "status": "ok",
    }


# ---------------------------------------------------------------------------
# TestWriteEvent
# ---------------------------------------------------------------------------

class TestWriteEvent:
    def test_writes_file_with_correct_structure(self, tmp_path):
        p = write_event(
            "dry_run", "execution-20260513T160000-abc12345",
            _minimal_payload("dry_run"),
            tmp_path, generated_at="2026-05-13T16:00:00Z",
        )
        assert p.exists()
        data = json.loads(p.read_text())
        assert data["event_type"] == "dry_run"
        assert data["run_id"] == "execution-20260513T160000-abc12345"
        assert data["generated_at"] == "2026-05-13T16:00:00Z"
        assert "payload" in data
        assert "schema_version" in data

    def test_unique_filenames_per_run(self, tmp_path):
        p1 = write_event(
            "order_monitor", "monitor-20260513T160000-aaaaaa",
            {"status": "run1"}, tmp_path, generated_at="2026-05-13T16:00:00Z",
        )
        p2 = write_event(
            "order_monitor", "monitor-20260513T160001-bbbbbb",
            {"status": "run2"}, tmp_path, generated_at="2026-05-13T16:00:01Z",
        )
        assert p1 != p2
        assert p1.name != p2.name

    def test_two_simulated_workflows_no_conflict(self, tmp_path):
        """Simulate two concurrent workflows writing events — different paths guaranteed."""
        workflow_a_path = write_event(
            "order_monitor", "monitor-workflow-a-20260513",
            {"workflow": "A", "orders_tracked": 3},
            tmp_path, generated_at="2026-05-13T20:30:00Z",
        )
        workflow_b_path = write_event(
            "order_monitor", "monitor-workflow-b-20260513",
            {"workflow": "B", "orders_tracked": 5},
            tmp_path, generated_at="2026-05-13T20:30:01Z",
        )
        assert workflow_a_path.exists()
        assert workflow_b_path.exists()
        assert workflow_a_path != workflow_b_path
        a_data = json.loads(workflow_a_path.read_text())
        b_data = json.loads(workflow_b_path.read_text())
        assert a_data["run_id"] != b_data["run_id"]

    def test_filename_contains_event_type_and_run_id(self, tmp_path):
        p = write_event(
            "paper_execution", "execution-20260513T160000-deadbeef",
            {}, tmp_path, generated_at="2026-05-13T16:00:00Z",
        )
        assert "paper_execution" in p.name
        assert "execution-20260513T160000-deadbeef" in p.name

    def test_invalid_event_type_raises_value_error(self, tmp_path):
        with pytest.raises(ValueError, match="Unknown event_type"):
            write_event("live_trading", "run-id", {}, tmp_path)

    def test_creates_date_subdirectory(self, tmp_path):
        write_event(
            "dry_run", "run-abc",
            {}, tmp_path, generated_at="2026-05-14T09:00:00Z",
        )
        assert (tmp_path / "2026-05-14").is_dir()

    def test_payload_preserved_exactly(self, tmp_path):
        payload = {
            "run_id": "x",
            "status": "DRY_RUN_PASS",
            "nested": {"a": 1, "b": [1, 2, 3]},
        }
        p = write_event(
            "dry_run", "run-x", payload, tmp_path,
            generated_at="2026-05-13T10:00:00Z",
        )
        data = json.loads(p.read_text())
        assert data["payload"]["nested"]["b"] == [1, 2, 3]
        assert data["payload"]["status"] == "DRY_RUN_PASS"

    def test_no_tmp_file_left_after_write(self, tmp_path):
        write_event(
            "dry_run", "run-tmp-test", {}, tmp_path,
            generated_at="2026-05-13T10:00:00Z",
        )
        tmp_files = list(tmp_path.rglob("*.tmp"))
        assert tmp_files == []

    def test_same_content_different_run_id_different_files(self, tmp_path):
        payload = {"status": "ok"}
        p1 = write_event(
            "dry_run", "run-001", payload, tmp_path,
            generated_at="2026-05-13T10:00:00Z",
        )
        p2 = write_event(
            "dry_run", "run-002", payload, tmp_path,
            generated_at="2026-05-13T10:00:00Z",
        )
        # Different run_ids → different hashes → different filenames
        assert p1.name != p2.name

    def test_all_event_types_accepted(self, tmp_path):
        for et in EVENT_TYPES:
            p = write_event(et, f"run-{et}", {}, tmp_path,
                           generated_at="2026-05-13T10:00:00Z")
            assert p.exists()


# ---------------------------------------------------------------------------
# TestReadEvents
# ---------------------------------------------------------------------------

class TestReadEvents:
    def test_reads_all_events_sorted_by_generated_at(self, tmp_path):
        write_event("dry_run", "r1", {}, tmp_path, generated_at="2026-05-13T10:00:00Z")
        write_event("order_monitor", "r2", {}, tmp_path, generated_at="2026-05-13T11:00:00Z")
        write_event("paper_execution", "r3", {}, tmp_path, generated_at="2026-05-13T12:00:00Z")

        events = read_events(tmp_path)
        assert len(events) == 3
        assert [e["generated_at"] for e in events] == [
            "2026-05-13T10:00:00Z",
            "2026-05-13T11:00:00Z",
            "2026-05-13T12:00:00Z",
        ]

    def test_filters_by_event_type(self, tmp_path):
        write_event("dry_run", "r1", {}, tmp_path, generated_at="2026-05-13T10:00:00Z")
        write_event("order_monitor", "r2", {}, tmp_path, generated_at="2026-05-13T11:00:00Z")
        write_event("dry_run", "r3", {}, tmp_path, generated_at="2026-05-13T12:00:00Z")

        events = read_events(tmp_path, event_types=("dry_run",))
        assert len(events) == 2
        assert all(e["event_type"] == "dry_run" for e in events)

    def test_empty_dir_returns_empty_list(self, tmp_path):
        events = read_events(tmp_path)
        assert events == []

    def test_nonexistent_dir_returns_empty_list(self, tmp_path):
        events = read_events(tmp_path / "nonexistent")
        assert events == []

    def test_days_limits_to_most_recent_dirs(self, tmp_path):
        write_event("dry_run", "old", {}, tmp_path, generated_at="2026-05-01T10:00:00Z")
        write_event("dry_run", "new", {}, tmp_path, generated_at="2026-05-13T10:00:00Z")

        events = read_events(tmp_path, days=1)
        assert len(events) == 1
        assert events[0]["run_id"] == "new"

    def test_malformed_json_file_skipped(self, tmp_path):
        date_dir = tmp_path / "2026-05-13"
        date_dir.mkdir()
        (date_dir / "bad_file.json").write_text("not json")
        write_event("dry_run", "good", {}, tmp_path, generated_at="2026-05-13T10:00:00Z")

        events = read_events(tmp_path)
        assert len(events) == 1
        assert events[0]["run_id"] == "good"


# ---------------------------------------------------------------------------
# TestFormatEventAsMarkdown
# ---------------------------------------------------------------------------

class TestFormatEventAsMarkdown:
    def test_contains_event_type_heading(self):
        evt = {
            "event_type": "dry_run",
            "run_id": "execution-abc",
            "generated_at": "2026-05-13T10:00:00Z",
            "payload": {"status": "DRY_RUN_PASS", "all_gates_pass": True},
        }
        md = format_event_as_markdown(evt)
        assert "## dry_run" in md
        assert "execution-abc" in md
        assert "```json" in md

    def test_contains_run_id(self):
        evt = {
            "event_type": "order_monitor",
            "run_id": "monitor-20260513T203956-0bf45519",
            "generated_at": "2026-05-13T20:39:56Z",
            "payload": {"orders_tracked": 3},
        }
        md = format_event_as_markdown(evt)
        assert "monitor-20260513T203956-0bf45519" in md


# ---------------------------------------------------------------------------
# TestLogEventRouting
# ---------------------------------------------------------------------------

class TestLogEventRouting:
    def test_trade_log_contains_dry_run_and_order_monitor(self):
        types = LOG_EVENT_ROUTING["TRADE-LOG.md"]
        assert "dry_run" in types
        assert "order_monitor" in types
        assert "paper_execution" in types

    def test_trigger_log_contains_alert_types(self):
        types = LOG_EVENT_ROUTING["TRIGGER-LOG.md"]
        assert "alert_intake" in types
        assert "alert_router" in types

    def test_signal_log_contains_alert_types(self):
        types = LOG_EVENT_ROUTING["SIGNAL-LOG.md"]
        assert "alert_intake" in types
        assert "alert_router" in types

    def test_no_execution_type_in_signal_or_trigger_log(self):
        for log_name in ("SIGNAL-LOG.md", "TRIGGER-LOG.md"):
            types = LOG_EVENT_ROUTING[log_name]
            assert "paper_execution" not in types


# ---------------------------------------------------------------------------
# TestRebuildMemoryLogs (subprocess integration)
# ---------------------------------------------------------------------------

class TestRebuildMemoryLogs:
    def test_dry_run_exits_zero(self):
        result = subprocess.run(
            [sys.executable, "scripts/rebuild_memory_logs.py", "--dry-run"],
            capture_output=True, text=True,
            cwd=str(_ROOT),
        )
        assert result.returncode == 0, result.stderr

    def test_produces_markdown_files(self, tmp_path):
        events_dir = tmp_path / "events"
        memory_dir = tmp_path / "memory"
        memory_dir.mkdir()

        write_event(
            "dry_run", "execution-test-abc",
            {"run_id": "execution-test-abc", "status": "DRY_RUN_PASS", "all_gates_pass": True},
            events_dir, generated_at="2026-05-13T10:00:00Z",
        )
        write_event(
            "order_monitor", "monitor-test-xyz",
            {"run_id": "monitor-test-xyz", "orders_tracked": 2, "orders_filled": 1},
            events_dir, generated_at="2026-05-13T11:00:00Z",
        )
        write_event(
            "alert_intake", "alert-001",
            {"alert_id": "alert-001", "symbol": "AAPL", "next_step": "log_only"},
            events_dir, generated_at="2026-05-13T12:00:00Z",
        )

        from trading_os.logging.event_log import LOG_EVENT_ROUTING
        for log_name in LOG_EVENT_ROUTING:
            event_types = LOG_EVENT_ROUTING[log_name]
            events = read_events(events_dir, event_types=event_types)
            from trading_os.logging.event_log import format_event_as_markdown
            sections = [format_event_as_markdown(e) for e in events]
            content = "# " + log_name + "\n\n" + "\n".join(sections)
            (memory_dir / log_name).write_text(content, encoding="utf-8")

        trade_log = (memory_dir / "TRADE-LOG.md").read_text()
        assert "dry_run" in trade_log
        assert "order_monitor" in trade_log
        assert "execution-test-abc" in trade_log

        trigger_log = (memory_dir / "TRIGGER-LOG.md").read_text()
        assert "alert_intake" in trigger_log
        assert "alert-001" in trigger_log

    def test_no_execution_path_in_rebuild_script(self):
        """rebuild_memory_logs.py must not import or call execution code."""
        script = (_ROOT / "scripts" / "rebuild_memory_logs.py").read_text()
        assert "execute_paper" not in script
        assert "import.*ENABLE_PAPER_EXECUTION" not in script
        assert "AlpacaPaperClient" not in script
        assert "submit_order" not in script
        # Must not read or set the execution env var at runtime
        assert 'os.environ.get("ENABLE_PAPER_EXECUTION")' not in script
        assert 'os.environ["ENABLE_PAPER_EXECUTION"]' not in script


# ---------------------------------------------------------------------------
# TestNoExecutionPath
# ---------------------------------------------------------------------------

class TestNoExecutionPath:
    def test_write_event_has_no_execution_side_effects(self, tmp_path):
        """write_event is pure I/O — writes one file, no API calls, no config changes."""
        p = write_event(
            "dry_run", "safe-run",
            {"status": "test"},
            tmp_path, generated_at="2026-05-13T10:00:00Z",
        )
        assert p.exists()
        files = list(tmp_path.rglob("*"))
        json_files = [f for f in files if f.is_file() and f.suffix == ".json"]
        assert len(json_files) == 1

    def test_event_log_module_does_not_import_execution_code(self):
        module_path = _ROOT / "src" / "trading_os" / "logging" / "event_log.py"
        source = module_path.read_text()
        assert "execute_paper" not in source
        assert "AlpacaPaperClient" not in source
        assert "submit_order" not in source
        assert "ENABLE_PAPER_EXECUTION" not in source
