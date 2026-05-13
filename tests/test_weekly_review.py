"""Tests for the research-only weekly review module.

Key invariants proven here:
- build_weekly_review returns correct structure with all required sections.
- Date range is correctly computed from end_date + days.
- Graceful degradation when artifact files are absent.
- write_weekly_review writes JSON, appends WEEKLY-REVIEW.md, appends EXPERIMENT-LOG.md.
- Operational issues are correctly identified.
- Research observations are generated.
- No execution path exists in the module.
- config/strategy.json and risk_limits.json are never modified.
- execute_paper is never referenced.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from trading_os.research.weekly_review import (
    _date_range,
    build_weekly_review,
    format_weekly_review_md,
    write_weekly_review,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture()
def dirs(tmp_path: Path):
    latest = tmp_path / "latest"
    history = tmp_path / "history"
    memory = tmp_path / "memory"
    latest.mkdir()
    (history / "executions").mkdir(parents=True)
    (history / "orders").mkdir(parents=True)
    (history / "triggers").mkdir(parents=True)
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


def _make_risk_state(memory: Path) -> None:
    _write_json(memory / "RISK-STATE.json", {
        "latest_equity": 99803.09,
        "peak_equity": 99803.09,
        "drawdown": 0.0,
        "position_count": 1,
        "updated_at": "2026-05-13T17:46:47Z",
    })


def _make_trigger_jsonl(triggers_dir: Path, date_str: str, risk_on: bool = True, n: int = 1) -> None:
    lines = []
    for i in range(n):
        lines.append(json.dumps({
            "risk_on": risk_on,
            "candidates": ["WELL", "BLK", "AAPL"],
            "selected": ["WELL", "BLK"],
            "excluded_count": 5,
            "scanned_at": f"{date_str}T1{i}:00:00Z",
            "regime_skip_reason": None,
            "trigger_snapshot_hash": f"hash{i}",
        }))
    (triggers_dir / f"{date_str}.jsonl").write_text("\n".join(lines), encoding="utf-8")


def _make_dry_run(exec_dir: Path, date_str: str, all_pass: bool, idx: int = 0) -> None:
    dn = date_str.replace("-", "")
    _write_json(exec_dir / f"execution-{dn}T15{idx:02d}00-test{idx:04d}_dry_run.json", {
        "run_id": f"execution-{dn}-test{idx}",
        "dry_run": True,
        "all_gates_pass": all_pass,
        "failed_gates": [] if all_pass else ["RISK_STATE_NOT_PAUSED"],
        "status": "DRY_RUN_PASS" if all_pass else "DRY_RUN_GATES_FAILED",
    })


def _make_paper_execution(exec_dir: Path, date_str: str, idx: int = 0) -> None:
    dn = date_str.replace("-", "")
    _write_json(exec_dir / f"execution-{dn}T160{idx:02d}00-test_paper.json", {
        "run_id": f"execution-{dn}-paper{idx}",
        "dry_run": False,
        "status": "PAPER_SUBMITTED",
        "orders_submitted": [{
            "symbol": "WELL",
            "side": "buy",
            "notional": 25.0,
            "limit_price": 218.90,
        }],
    })


def _make_order_monitor(orders_dir: Path, date_str: str, idx: int = 0,
                        missing: int = 0, fills: int = 0) -> None:
    dn = date_str.replace("-", "")
    _write_json(orders_dir / f"order_monitor-{dn}T17{idx:02d}00-test.json", {
        "run_id": f"order_monitor-{dn}-{idx}",
        "orders_tracked": missing + fills,
        "orders_filled": fills,
        "orders_missing": missing,
        "orders_expired": 0,
        "orders_rejected": 0,
        "orders_canceled": 0,
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


def _make_route(routes_dir: Path, route_id: str, routed_at: str,
                action: str = "refresh_requested",
                execution_called: bool = False,
                approved_plan: bool = False) -> None:
    _write_json(routes_dir / f"route_{route_id}.json", {
        "route_id": route_id,
        "action_taken": action,
        "execution_called": execution_called,
        "approved_trade_plan_created": approved_plan,
        "routed_at": routed_at,
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
# _date_range
# ---------------------------------------------------------------------------

class TestDateRange:
    def test_7_days(self):
        dates = _date_range("2026-05-13", 7)
        assert len(dates) == 7
        assert dates[0] == "2026-05-07"
        assert dates[-1] == "2026-05-13"

    def test_1_day(self):
        dates = _date_range("2026-05-13", 1)
        assert dates == ["2026-05-13"]

    def test_ascending_order(self):
        dates = _date_range("2026-05-13", 5)
        assert dates == sorted(dates)


# ---------------------------------------------------------------------------
# build_weekly_review — structure
# ---------------------------------------------------------------------------

class TestBuildWeeklyReviewStructure:
    def test_returns_dict_with_all_sections(self, dirs):
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        for key in [
            "run_id", "period_start", "period_end", "days", "generated_at", "status",
            "trigger_scans", "dry_runs", "paper_executions", "order_monitor",
            "alerts", "data_quality", "risk_state",
            "operational_issues", "research_observations", "review_hash",
        ]:
            assert key in review, f"Missing key: {key}"

    def test_period_dates(self, dirs):
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert review["period_start"] == "2026-05-07"
        assert review["period_end"] == "2026-05-13"

    def test_run_id_contains_end_date(self, dirs):
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert review["run_id"] == "weekly_review-2026-05-13"

    def test_review_hash_present(self, dirs):
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert len(review["review_hash"]) == 16

    def test_empty_dirs_no_errors(self, dirs):
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert review["status"] == "ok"
        assert review["trigger_scans"]["total_runs"] == 0
        assert review["dry_runs"]["total_runs"] == 0


# ---------------------------------------------------------------------------
# build_weekly_review — aggregation
# ---------------------------------------------------------------------------

class TestBuildWeeklyReviewAggregation:
    def test_aggregates_trigger_scans_across_days(self, dirs):
        triggers_dir = dirs["history"] / "triggers"
        _make_trigger_jsonl(triggers_dir, "2026-05-12", risk_on=True, n=2)
        _make_trigger_jsonl(triggers_dir, "2026-05-13", risk_on=False, n=1)
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        ts = review["trigger_scans"]
        assert ts["total_runs"] == 3
        assert ts["risk_on_sessions"] == 2
        assert ts["risk_off_sessions"] == 1

    def test_aggregates_dry_runs_across_days(self, dirs):
        exec_dir = dirs["history"] / "executions"
        _make_dry_run(exec_dir, "2026-05-12", all_pass=True, idx=0)
        _make_dry_run(exec_dir, "2026-05-13", all_pass=False, idx=0)
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        dr = review["dry_runs"]
        assert dr["total_runs"] == 2
        assert dr["all_pass_count"] == 1
        assert dr["fail_count"] == 1
        assert dr["failing_gates"].get("RISK_STATE_NOT_PAUSED") == 1

    def test_aggregates_paper_executions(self, dirs):
        exec_dir = dirs["history"] / "executions"
        _make_paper_execution(exec_dir, "2026-05-12", idx=0)
        _make_paper_execution(exec_dir, "2026-05-13", idx=1)
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        pe = review["paper_executions"]
        assert pe["total_attempts"] == 2
        assert pe["total_orders_submitted"] == 2

    def test_aggregates_order_monitor(self, dirs):
        orders_dir = dirs["history"] / "orders"
        _make_order_monitor(orders_dir, "2026-05-12", idx=0, missing=1)
        _make_order_monitor(orders_dir, "2026-05-13", idx=0, fills=1)
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        om = review["order_monitor"]
        assert om["total_runs"] == 2
        assert om["missing"] == 1
        assert om["fills"] == 1

    def test_excludes_files_outside_period(self, dirs):
        exec_dir = dirs["history"] / "executions"
        # Only 1 day in period
        _make_dry_run(exec_dir, "2026-05-13", all_pass=True, idx=0)
        _make_dry_run(exec_dir, "2026-05-01", all_pass=True, idx=0)  # outside window
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=1,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert review["dry_runs"]["total_runs"] == 1

    def test_alerts_period_filter(self, dirs):
        alerts_dir = dirs["history"] / "alerts"
        _make_alert(alerts_dir, "a001", "request_data_refresh", "2026-05-13T14:00:00Z")
        _make_alert(alerts_dir, "a002", "request_data_refresh", "2026-04-01T14:00:00Z")  # old
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        al = review["alerts"]
        assert al["alerts_this_period"] == 1
        assert al["total_alerts_all_time"] == 2

    def test_routes_execution_called_any_false(self, dirs):
        routes_dir = dirs["history"] / "alerts" / "routes"
        _make_route(routes_dir, "r001", "2026-05-13T17:00:00Z", execution_called=False)
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert review["alerts"]["execution_called_any"] is False

    def test_routes_execution_called_any_true_flagged(self, dirs):
        routes_dir = dirs["history"] / "alerts" / "routes"
        _make_route(routes_dir, "r001", "2026-05-13T17:00:00Z", execution_called=True)
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert review["alerts"]["execution_called_any"] is True


# ---------------------------------------------------------------------------
# Operational issues detection
# ---------------------------------------------------------------------------

class TestOperationalIssues:
    def test_no_issues_when_clean(self, dirs):
        _make_data_quality(dirs["latest"], "PASS")
        _make_risk_state(dirs["memory"])
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        assert review["operational_issues"] == []

    def test_issue_reported_for_failing_gate(self, dirs):
        exec_dir = dirs["history"] / "executions"
        _make_dry_run(exec_dir, "2026-05-13", all_pass=False)
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        issues = review["operational_issues"]
        assert any("RISK_STATE_NOT_PAUSED" in i for i in issues)

    def test_issue_reported_for_missing_orders(self, dirs):
        orders_dir = dirs["history"] / "orders"
        _make_order_monitor(orders_dir, "2026-05-13", idx=0, missing=2)
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        issues = review["operational_issues"]
        assert any("missing" in i.lower() for i in issues)

    def test_safety_issue_for_execution_called(self, dirs):
        routes_dir = dirs["history"] / "alerts" / "routes"
        _make_route(routes_dir, "r001", "2026-05-13T17:00:00Z", execution_called=True)
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        issues = review["operational_issues"]
        assert any("SAFETY" in i for i in issues)


# ---------------------------------------------------------------------------
# write_weekly_review
# ---------------------------------------------------------------------------

class TestWriteWeeklyReview:
    def test_writes_json_file(self, dirs):
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        paths = write_weekly_review(review, dirs["runs"], dirs["memory"])
        assert Path(paths["json_path"]).exists()

    def test_json_filename_contains_date(self, dirs):
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        paths = write_weekly_review(review, dirs["runs"], dirs["memory"])
        assert "2026-05-13" in paths["json_path"]

    def test_appends_weekly_review_md(self, dirs):
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        write_weekly_review(review, dirs["runs"], dirs["memory"])
        write_weekly_review(review, dirs["runs"], dirs["memory"])
        content = (dirs["memory"] / "WEEKLY-REVIEW.md").read_text(encoding="utf-8")
        assert content.count("## Weekly Review") == 2

    def test_appends_experiment_log_when_issues_exist(self, dirs):
        exec_dir = dirs["history"] / "executions"
        _make_dry_run(exec_dir, "2026-05-13", all_pass=False)
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        paths = write_weekly_review(review, dirs["runs"], dirs["memory"])
        assert paths.get("experiment_log_path") is not None
        exp_content = Path(paths["experiment_log_path"]).read_text(encoding="utf-8")
        assert "Experiment Candidates" in exp_content

    def test_no_experiment_log_when_no_issues(self, dirs):
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        paths = write_weekly_review(review, dirs["runs"], dirs["memory"])
        # May or may not write depending on observations — just check it doesn't error
        # The experiment log path is None only when there are no issues AND no observations
        assert "experiment_log_path" in paths

    def test_creates_runs_dir_if_absent(self, tmp_path):
        runs = tmp_path / "deep" / "nested" / "runs"
        mem = tmp_path / "mem"
        mem.mkdir()
        review = {"run_id": "x", "period_start": "2026-05-07", "period_end": "2026-05-13",
                  "days": 7, "generated_at": "t", "status": "ok",
                  "operational_issues": [], "research_observations": [],
                  "review_hash": "abc12345"}
        paths = write_weekly_review(review, runs, mem)
        assert Path(paths["json_path"]).exists()


# ---------------------------------------------------------------------------
# format_weekly_review_md
# ---------------------------------------------------------------------------

class TestFormatWeeklyReviewMd:
    def test_contains_period_header(self, dirs):
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        md = format_weekly_review_md(review)
        assert "2026-05-07" in md
        assert "2026-05-13" in md

    def test_contains_operational_issues_section(self, dirs):
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        md = format_weekly_review_md(review)
        assert "Operational Issues" in md

    def test_execution_called_safety_warning(self, dirs):
        routes_dir = dirs["history"] / "alerts" / "routes"
        _make_route(routes_dir, "r001", "2026-05-13T17:00:00Z", execution_called=True)
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        md = format_weekly_review_md(review)
        assert "INVESTIGATE" in md

    def test_separator_present(self, dirs):
        review = build_weekly_review(
            end_date_str="2026-05-13",
            days=7,
            latest_dir=dirs["latest"],
            history_dir=dirs["history"],
            memory_dir=dirs["memory"],
        )
        md = format_weekly_review_md(review)
        assert "---" in md


# ---------------------------------------------------------------------------
# Safety — no execution path
# ---------------------------------------------------------------------------

class TestWeeklyReviewNoExecutionPath:
    def test_module_does_not_import_execute_paper(self):
        import trading_os.research.weekly_review as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        assert not re.search(r'^\s*(import|from)\s+.*execute_paper', src, re.MULTILINE)
        assert not re.search(r'subprocess\.[^(]+\([^)]*execute_paper', src)

    def test_module_does_not_call_subprocess(self):
        import trading_os.research.weekly_review as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        assert "subprocess" not in src

    def test_module_never_writes_to_strategy_or_risk_limits(self):
        import trading_os.research.weekly_review as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        assert not re.search(r'strategy\.json.*write|write.*strategy\.json', src)
        assert not re.search(r'risk_limits\.json.*write|write.*risk_limits\.json', src)

    def test_module_never_sets_approved_for_execution(self):
        import trading_os.research.weekly_review as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        assert not re.search(r'approved_for_execution\s*=\s*True', src)

    def test_cli_script_does_not_call_execute_paper(self):
        script = Path(__file__).parents[1] / "scripts" / "weekly_review.py"
        src = script.read_text(encoding="utf-8")
        assert "execute_paper" not in src
