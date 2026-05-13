"""Tests for the research-only daily summary module.

Key invariants proven here:
- build_daily_summary returns correct structure with all required sections.
- Graceful degradation when artifact files are absent.
- write_daily_summary writes JSON and appends DAILY-SUMMARY.md.
- JSON output is valid and has summary_hash.
- Markdown contains human-readable sections.
- No execution path exists in the module.
- approved_for_execution is always read, never set.
- execute_paper is never referenced as an import or subprocess call.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from trading_os.research.daily_summary import (
    build_daily_summary,
    format_daily_summary_md,
    write_daily_summary,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture()
def dirs(tmp_path: Path):
    """Create a minimal artifact directory tree."""
    latest = tmp_path / "latest"
    history = tmp_path / "history"
    memory = tmp_path / "memory"
    latest.mkdir()
    (history / "executions").mkdir(parents=True)
    (history / "orders").mkdir(parents=True)
    (history / "alerts" / "routes").mkdir(parents=True)
    memory.mkdir()
    return {
        "tmp": tmp_path,
        "latest": latest,
        "history": history,
        "memory": memory,
        "runs": history / "runs",
    }


def _write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data), encoding="utf-8")


def _make_account_snapshot(latest: Path, equity: float = 50000.0) -> None:
    _write_json(latest / "account_snapshot.json", {
        "account": {
            "equity": str(equity),
            "cash": "48000.00",
            "buying_power": "96000.00",
            "status": "ACTIVE",
        },
        "position_count": 1,
        "fetched_at": "2026-05-13T16:00:00Z",
    })


def _make_positions_snapshot(latest: Path) -> None:
    _write_json(latest / "positions_snapshot.json", {
        "positions": [{
            "symbol": "WELL",
            "side": "long",
            "qty": "0.114",
            "market_value": "25.23",
            "unrealized_pl": "0.23",
            "unrealized_plpc": "0.009",
            "avg_entry_price": "218.80",
        }],
        "position_count": 1,
        "fetched_at": "2026-05-13T16:00:00Z",
    })


def _make_orders_snapshot(latest: Path, empty: bool = True) -> None:
    _write_json(latest / "orders_snapshot.json", {
        "orders": [] if empty else [{
            "symbol": "BLK",
            "side": "buy",
            "order_type": "limit",
            "limit_price": 368.98,
            "notional": 25.0,
            "status": "new",
            "client_order_id": "TOS-TEST-001",
        }],
        "open_order_count": 0 if empty else 1,
        "fetched_at": "2026-05-13T16:00:00Z",
    })


def _make_trigger_snapshot(latest: Path) -> None:
    _write_json(latest / "trigger_snapshot.json", {
        "candidates": ["WELL", "BLK", "AAPL"],
        "selected": ["WELL", "BLK"],
        "excluded": [{"symbol": "MSFT", "skip_reason": "close_below_200dma"}],
        "scanned_at": "2026-05-13T15:30:00Z",
        "regime": {
            "risk_on": True,
            "passed": True,
            "spy_signals": {
                "latest_close": 564.30,
                "sma": 519.61,
                "passes_200dma": True,
                "roc": 0.0987,
                "passes_6m_momentum": True,
            },
            "breadth": {
                "breadth": 0.899,
                "breadth_ok": True,
                "above_200dma_count": 71,
                "ready_count": 79,
            },
        },
    })


def _make_trade_plan(latest: Path, approved: bool = False) -> None:
    _write_json(latest / "trade_plan.json", {
        "plan_id": "trade_plan-20260513T172830-abc123",
        "trading_mode": "paper",
        "generated_at": "2026-05-13T17:28:30Z",
        "expires_at": "2099-12-31T23:59:59Z",
        "approval": {
            "approved_for_execution": approved,
            "approve_paper_flag": approved,
            "all_risk_checks_pass": True,
            "reason": "approved" if approved else "approve_paper_flag_not_set",
        },
        "proposed_orders": [{
            "symbol": "BLK",
            "side": "buy",
            "order_type": "limit",
            "limit_price": 368.98,
            "notional": 25.0,
            "time_in_force": "day",
            "would_short": False,
            "skip_reason": None,
        }],
        "blocked_symbols": [],
        "risk_checks": [
            {"check_id": "TRADING_MODE_PAPER", "passes": True},
            {"check_id": "NO_LIVE_TRADING", "passes": True},
        ],
    })


def _make_risk_state(memory: Path) -> None:
    _write_json(memory / "RISK-STATE.json", {
        "latest_equity": 99803.09,
        "peak_equity": 99803.09,
        "drawdown": 0.0,
        "position_count": 1,
        "updated_at": "2026-05-13T17:46:47Z",
    })


def _make_execution_report(latest: Path, all_pass: bool = True) -> None:
    _write_json(latest / "execution_report.json", {
        "run_id": "execution-20260513T172835-test",
        "generated_at": "2026-05-13T17:28:35Z",
        "dry_run": True,
        "all_gates_pass": all_pass,
        "failed_gates": [] if all_pass else ["RISK_STATE_NOT_PAUSED"],
        "status": "DRY_RUN_PASS" if all_pass else "DRY_RUN_GATES_FAILED",
        "orders_submitted": [],
    })


def _make_dry_run(exec_dir: Path, date_nodash: str, all_pass: bool = True, idx: int = 0) -> None:
    fname = f"execution-{date_nodash}T15{idx:02d}00-test{idx:04d}_dry_run.json"
    _write_json(exec_dir / fname, {
        "run_id": f"execution-{date_nodash}T15{idx:02d}00-test{idx:04d}",
        "dry_run": True,
        "all_gates_pass": all_pass,
        "failed_gates": [] if all_pass else ["RISK_STATE_NOT_PAUSED"],
        "status": "DRY_RUN_PASS" if all_pass else "DRY_RUN_GATES_FAILED",
    })


def _make_paper_execution(exec_dir: Path, date_nodash: str) -> None:
    fname = f"execution-{date_nodash}T160036-test_paper.json"
    _write_json(exec_dir / fname, {
        "run_id": f"execution-{date_nodash}T160036-test",
        "dry_run": False,
        "status": "PAPER_SUBMITTED",
        "plan_id": "trade_plan-test",
        "orders_submitted": [{
            "symbol": "WELL",
            "side": "buy",
            "notional": 25.0,
            "limit_price": 218.90,
            "submitted": True,
            "submitted_at": f"{date_nodash[:4]}-{date_nodash[4:6]}-{date_nodash[6:]}T16:00:36Z",
            "broker_order_id": "test-broker-id",
            "client_order_id": "TOS-test",
        }],
    })


def _make_order_monitor_report(latest: Path, tracked: int = 1) -> None:
    _write_json(latest / "order_monitor_report.json", {
        "run_id": "order_monitor-20260513T174742-test",
        "generated_at": "2026-05-13T17:47:42Z",
        "dry_run": False,
        "orders_tracked": tracked,
        "orders_filled": 0,
        "orders_missing": tracked,
        "orders_expired": 0,
        "orders_rejected": 0,
        "orders_canceled": 0,
        "orders_active": 0,
        "lifecycles": [],
    })


def _make_alert(alerts_dir: Path, alert_id: str, next_step: str, ingested_at: str) -> None:
    _write_json(alerts_dir / f"alert-{alert_id}.json", {
        "alert_id": alert_id,
        "symbol": "SPY",
        "next_step": next_step,
        "source": "tradingview",
        "trade_execution_allowed": False,
        "blocked_by_default": True,
        "ingested_at": ingested_at,
    })


def _make_route(routes_dir: Path, route_id: str, action: str, execution_called: bool = False) -> None:
    _write_json(routes_dir / f"route_{route_id}.json", {
        "route_id": route_id,
        "action_taken": action,
        "execution_called": execution_called,
        "approved_trade_plan_created": False,
        "routed_at": "2026-05-13T17:01:52Z",
    })


def _make_data_quality(latest: Path, status: str = "PASS") -> None:
    _write_json(latest / "data_quality_report.json", {
        "run_id": "dq-test",
        "status": status,
        "generated_at": "2026-05-13T17:00:00Z",
        "issues": [],
        "wide_spreads": [],
        "missing_bars": [],
        "insufficient_bars": [],
        "missing_quotes": [],
    })


# ---------------------------------------------------------------------------
# build_daily_summary — structure
# ---------------------------------------------------------------------------

class TestBuildDailySummaryStructure:
    def test_returns_dict_with_all_sections(self, dirs):
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert isinstance(summary, dict)
        for key in [
            "run_id", "date", "generated_at", "status",
            "account", "risk_state", "positions", "open_orders",
            "trigger_scan", "trade_plan", "execution_report",
            "dry_runs", "paper_executions", "order_monitor",
            "alerts", "alert_routes", "data_quality", "summary_hash",
        ]:
            assert key in summary, f"Missing key: {key}"

    def test_run_id_contains_date(self, dirs):
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert summary["run_id"] == "daily_summary-2026-05-13"

    def test_status_ok(self, dirs):
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert summary["status"] == "ok"

    def test_summary_hash_present_and_16chars(self, dirs):
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert len(summary["summary_hash"]) == 16

    def test_uses_today_when_date_not_given(self, dirs):
        from datetime import date
        summary = build_daily_summary(
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert summary["date"] == date.today().isoformat()


class TestBuildDailySummaryGracefulDegradation:
    def test_empty_dirs_returns_available_false(self, dirs):
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert summary["trigger_scan"]["available"] is False
        assert summary["trade_plan"]["available"] is False
        assert summary["execution_report"]["available"] is False
        assert summary["data_quality"]["available"] is False

    def test_empty_dirs_positions_is_empty_list(self, dirs):
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert summary["positions"] == []
        assert summary["open_orders"] == []

    def test_empty_dirs_dry_runs_count_zero(self, dirs):
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert summary["dry_runs"]["count"] == 0

    def test_empty_dirs_alerts_total_zero(self, dirs):
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert summary["alerts"]["total_count"] == 0


class TestBuildDailySummaryWithArtifacts:
    def test_reads_positions(self, dirs):
        _make_positions_snapshot(dirs["latest"])
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert len(summary["positions"]) == 1
        assert summary["positions"][0]["symbol"] == "WELL"

    def test_reads_trade_plan_not_approved(self, dirs):
        _make_trade_plan(dirs["latest"], approved=False)
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        tp = summary["trade_plan"]
        assert tp["available"] is True
        assert tp["approved_for_execution"] is False
        assert tp["proposed_orders_count"] == 1
        assert tp["proposed_orders"][0]["symbol"] == "BLK"

    def test_trade_plan_approved_flag_preserved_not_overridden(self, dirs):
        # If somehow approved=True in file, we read it faithfully (audit, not modify)
        _make_trade_plan(dirs["latest"], approved=True)
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert summary["trade_plan"]["approved_for_execution"] is True

    def test_reads_trigger_scan_regime(self, dirs):
        _make_trigger_snapshot(dirs["latest"])
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        ts = summary["trigger_scan"]
        assert ts["available"] is True
        assert ts["risk_on"] is True
        assert ts["candidates_count"] == 3
        assert ts["selected_count"] == 2
        assert ts["excluded_count"] == 1

    def test_reads_risk_state(self, dirs):
        _make_risk_state(dirs["memory"])
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        rs = summary["risk_state"]
        assert rs["drawdown"] == 0.0
        assert rs["peak_equity"] == 99803.09

    def test_counts_dry_runs_today(self, dirs):
        exec_dir = dirs["history"] / "executions"
        _make_dry_run(exec_dir, "20260513", all_pass=True, idx=0)
        _make_dry_run(exec_dir, "20260513", all_pass=False, idx=1)
        _make_dry_run(exec_dir, "20260512", all_pass=True, idx=0)  # different date
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        dr = summary["dry_runs"]
        assert dr["count"] == 2  # only today's
        assert dr["all_pass_count"] == 1
        assert dr["fail_count"] == 1
        assert "RISK_STATE_NOT_PAUSED" in dr["failing_gates"]

    def test_counts_paper_executions_today(self, dirs):
        exec_dir = dirs["history"] / "executions"
        _make_paper_execution(exec_dir, "20260513")
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        pe = summary["paper_executions"]
        assert pe["count"] == 1
        assert pe["total_orders_submitted"] == 1

    def test_alerts_count_and_today_filter(self, dirs):
        alerts_dir = dirs["history"] / "alerts"
        _make_alert(alerts_dir, "alert-001", "request_data_refresh", "2026-05-13T14:00:00Z")
        _make_alert(alerts_dir, "alert-002", "request_data_refresh", "2026-05-12T14:00:00Z")
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        al = summary["alerts"]
        assert al["total_count"] == 2
        assert al["ingested_today"] == 1
        assert al["by_next_step"]["request_data_refresh"] == 2

    def test_routes_safety_flags(self, dirs):
        routes_dir = dirs["history"] / "alerts" / "routes"
        _make_route(routes_dir, "route_20260513T170000_test_aaa", "refresh_requested")
        _make_route(routes_dir, "route_20260513T171000_test_bbb", "logged")
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        ar = summary["alert_routes"]
        assert ar["total_routes"] == 2
        assert ar["execution_called_any"] is False
        assert ar["approved_trade_plan_created_any"] is False

    def test_data_quality_status(self, dirs):
        _make_data_quality(dirs["latest"], status="PASS")
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        dq = summary["data_quality"]
        assert dq["available"] is True
        assert dq["status"] == "PASS"

    def test_order_monitor_aggregates_correctly(self, dirs):
        _make_order_monitor_report(dirs["latest"], tracked=3)
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        om = summary["order_monitor"]
        assert om["available"] is True
        assert om["orders_tracked"] == 3
        assert om["orders_missing"] == 3


# ---------------------------------------------------------------------------
# write_daily_summary
# ---------------------------------------------------------------------------

class TestWriteDailySummary:
    def test_writes_json_file(self, dirs):
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        paths = write_daily_summary(summary, dirs["runs"], dirs["memory"])
        assert Path(paths["json_path"]).exists()

    def test_json_filename_contains_date(self, dirs):
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        paths = write_daily_summary(summary, dirs["runs"], dirs["memory"])
        assert "2026-05-13" in paths["json_path"]

    def test_json_is_valid_and_has_hash(self, dirs):
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        paths = write_daily_summary(summary, dirs["runs"], dirs["memory"])
        d = json.loads(Path(paths["json_path"]).read_text(encoding="utf-8"))
        assert "summary_hash" in d
        assert len(d["summary_hash"]) == 16

    def test_appends_daily_summary_md(self, dirs):
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        write_daily_summary(summary, dirs["runs"], dirs["memory"])
        write_daily_summary(summary, dirs["runs"], dirs["memory"])  # second call appends
        content = (dirs["memory"] / "DAILY-SUMMARY.md").read_text(encoding="utf-8")
        assert content.count("## Daily Summary") == 2

    def test_creates_runs_dir_if_absent(self, tmp_path):
        runs = tmp_path / "deep" / "nested" / "runs"
        mem = tmp_path / "mem"
        mem.mkdir()
        summary = {"run_id": "x", "date": "2026-05-13", "generated_at": "t",
                   "status": "ok", "summary_hash": "abc12345"}
        paths = write_daily_summary(summary, runs, mem)
        assert Path(paths["json_path"]).exists()


# ---------------------------------------------------------------------------
# format_daily_summary_md
# ---------------------------------------------------------------------------

class TestFormatDailySummaryMd:
    def _make_full_summary(self, dirs):
        _make_account_snapshot(dirs["latest"])
        _make_risk_state(dirs["memory"])
        _make_positions_snapshot(dirs["latest"])
        _make_orders_snapshot(dirs["latest"])
        _make_trigger_snapshot(dirs["latest"])
        _make_trade_plan(dirs["latest"], approved=False)
        _make_execution_report(dirs["latest"])
        _make_data_quality(dirs["latest"])
        return build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )

    def test_contains_date_header(self, dirs):
        summary = self._make_full_summary(dirs)
        md = format_daily_summary_md(summary)
        assert "2026-05-13" in md

    def test_contains_account_section(self, dirs):
        summary = self._make_full_summary(dirs)
        md = format_daily_summary_md(summary)
        assert "Account" in md

    def test_contains_positions_section(self, dirs):
        summary = self._make_full_summary(dirs)
        md = format_daily_summary_md(summary)
        assert "Positions" in md
        assert "WELL" in md

    def test_contains_trigger_regime(self, dirs):
        summary = self._make_full_summary(dirs)
        md = format_daily_summary_md(summary)
        assert "RISK_ON" in md

    def test_approved_for_execution_shown_as_no(self, dirs):
        summary = self._make_full_summary(dirs)
        md = format_daily_summary_md(summary)
        assert "NO" in md  # approved_for_execution=False shown as NO

    def test_approved_for_execution_bold_yes_when_true(self, dirs):
        _make_trade_plan(dirs["latest"], approved=True)
        summary = build_daily_summary(
            date_str="2026-05-13",
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        md = format_daily_summary_md(summary)
        assert "**YES**" in md

    def test_separator_present(self, dirs):
        summary = self._make_full_summary(dirs)
        md = format_daily_summary_md(summary)
        assert "---" in md


# ---------------------------------------------------------------------------
# Safety — no execution path
# ---------------------------------------------------------------------------

class TestDailySummaryNoExecutionPath:
    def test_module_does_not_import_execute_paper(self):
        import trading_os.research.daily_summary as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        assert not re.search(r'^\s*(import|from)\s+.*execute_paper', src, re.MULTILINE)
        assert not re.search(r'subprocess\.[^(]+\([^)]*execute_paper', src)

    def test_module_does_not_call_subprocess(self):
        import trading_os.research.daily_summary as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        assert "subprocess" not in src

    def test_module_never_sets_approved_for_execution(self):
        import trading_os.research.daily_summary as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        # Should never assign approved_for_execution = True
        assert not re.search(r'approved_for_execution\s*=\s*True', src)

    def test_module_never_modifies_strategy_or_risk_limits(self):
        import trading_os.research.daily_summary as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        assert "strategy.json" not in src
        assert "risk_limits.json" not in src

    def test_cli_script_does_not_call_execute_paper(self):
        script = Path(__file__).parents[1] / "scripts" / "daily_summary.py"
        src = script.read_text(encoding="utf-8")
        assert "execute_paper" not in src
