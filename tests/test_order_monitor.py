"""Tests for src/trading_os/monitoring/order_monitor.py.

Safety invariants proved:
- Submitted pending_new order is tracked and status preserved.
- Filled order produces fill reconciliation data.
- Rejected order is logged as rejected, not successful.
- Missing broker order creates a warning in the report.
- Monitor never submits, cancels, or replaces orders (source inspection).
- Stale day order (active, market closed) is flagged.
- Fill links back to plan_id, run_id, trade_plan_hash, trigger_snapshot_hash.
- Safety block is always present with all False values.
- Dry-run mode uses stored data and produces a valid report.

Fetch lookup tests (TestFetchBrokerOrdersLookupPaths):
- Order found via bulk open orders list.
- Order found via bulk closed orders list.
- Order found via direct broker_order_id fallback (get_order_by_id).
- Order found via direct client_order_id fallback (get_order_by_client_id).
- Truly missing order remains missing with warning.
- fetch_log counts are accurate and contain no secrets.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

import pytest

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.monitoring.order_monitor import (
    ACTIVE_STATUSES,
    TERMINAL_STATUSES,
    _normalize_status,
    append_trade_log,
    build_order_lifecycle,
    build_plan_refs_index,
    is_stale_order,
    load_submitted_audits,
    reconcile_fill,
    run_order_monitor,
)
from trading_os.time_utils import utc_now_iso


# ---------------------------------------------------------------------------
# Fixtures / builders
# ---------------------------------------------------------------------------

def _audit(
    client_order_id: str = "TOS-20260513T160035-WELL-BUY",
    broker_order_id: str = "broker-abc123",
    symbol: str = "WELL",
    side: str = "buy",
    notional: float = 25.0,
    limit_price: float = 218.90,
    submitted: bool = True,
    time_in_force: str = "day",
) -> dict:
    return {
        "client_order_id": client_order_id,
        "broker_order_id": broker_order_id,
        "symbol": symbol,
        "side": side,
        "notional": notional,
        "limit_price": limit_price,
        "submitted_at": utc_now_iso(),
        "submitted": submitted,
        "broker_status": "pending_new",
        "error": None,
        "time_in_force": time_in_force,
    }


def _broker_order(
    broker_id: str = "broker-abc123",
    client_id: str = "TOS-20260513T160035-WELL-BUY",
    symbol: str = "WELL",
    status: str = "pending_new",
    filled_avg_price: float | None = None,
    filled_qty: float | None = None,
    filled_at: str | None = None,
) -> dict:
    return {
        "id": broker_id,
        "client_order_id": client_id,
        "symbol": symbol,
        "status": status,
        "filled_avg_price": filled_avg_price,
        "filled_qty": str(filled_qty) if filled_qty is not None else None,
        "filled_at": filled_at,
        "side": "buy",
        "order_type": "limit",
        "time_in_force": "day",
    }


def _broker_lookup(orders: list) -> dict:
    by_broker: dict = {}
    by_client: dict = {}
    for o in orders:
        bid = o.get("id")
        cid = o.get("client_order_id")
        if bid:
            by_broker[str(bid)] = o
        if cid:
            by_client[str(cid)] = o
    return {"by_broker_id": by_broker, "by_client_id": by_client}


def _open_clock() -> dict:
    return {"is_open": True, "timestamp": utc_now_iso()}


def _closed_clock() -> dict:
    return {"is_open": False, "timestamp": utc_now_iso()}


def _write_audit(tmp_path: Path, audit: dict) -> Path:
    """Write a per-order audit file to tmp_path and return the path."""
    path = tmp_path / f"{audit['client_order_id']}.json"
    path.write_text(json.dumps(audit) + "\n", encoding="utf-8")
    return path


def _write_exec_report(executions_dir: Path, report: dict) -> None:
    executions_dir.mkdir(parents=True, exist_ok=True)
    run_id = report["run_id"]
    path = executions_dir / f"{run_id}_paper.json"
    path.write_text(json.dumps(report) + "\n", encoding="utf-8")


# ===========================================================================
# TestBuildOrderLifecycle — core lifecycle computation
# ===========================================================================

class TestBuildOrderLifecycle:
    def test_pending_new_order_tracked(self):
        order = _broker_order(status="pending_new")
        lookup = _broker_lookup([order])
        lc = build_order_lifecycle(
            audit=_audit(),
            broker_lookup=lookup,
            plan_refs=None,
            trigger_snapshot_hash=None,
            positions=[],
            clock=_open_clock(),
            checked_at=utc_now_iso(),
        )
        assert lc["lifecycle_status"] == "pending_new"
        assert lc["client_order_id"] == "TOS-20260513T160035-WELL-BUY"
        assert lc["symbol"] == "WELL"
        assert lc["fill"] is None
        assert lc["warning"] is None

    def test_filled_order_has_fill_data(self):
        order = _broker_order(
            status="filled",
            filled_avg_price=219.50,
            filled_qty=0.113,
            filled_at="2026-05-13T16:30:00Z",
        )
        lookup = _broker_lookup([order])
        positions = [{"symbol": "WELL", "qty": "0.113", "market_value": "24.80"}]
        lc = build_order_lifecycle(
            audit=_audit(),
            broker_lookup=lookup,
            plan_refs=None,
            trigger_snapshot_hash=None,
            positions=positions,
            clock=_open_clock(),
            checked_at=utc_now_iso(),
        )
        assert lc["lifecycle_status"] == "filled"
        fill = lc["fill"]
        assert fill is not None
        assert fill["fill_price"] == pytest.approx(219.50)
        assert fill["filled_qty"] == pytest.approx(0.113)
        assert fill["filled_at"] == "2026-05-13T16:30:00Z"

    def test_filled_order_position_confirmed_when_present(self):
        order = _broker_order(
            status="filled", filled_avg_price=219.50, filled_qty=0.113
        )
        lookup = _broker_lookup([order])
        positions = [{"symbol": "WELL", "qty": "0.113", "market_value": "24.80"}]
        lc = build_order_lifecycle(
            audit=_audit(),
            broker_lookup=lookup,
            plan_refs=None,
            trigger_snapshot_hash=None,
            positions=positions,
            clock=_open_clock(),
            checked_at=utc_now_iso(),
        )
        assert lc["fill"]["position_confirmed"] is True

    def test_filled_order_position_not_confirmed_when_absent(self):
        order = _broker_order(
            status="filled", filled_avg_price=219.50, filled_qty=0.113
        )
        lookup = _broker_lookup([order])
        lc = build_order_lifecycle(
            audit=_audit(),
            broker_lookup=lookup,
            plan_refs=None,
            trigger_snapshot_hash=None,
            positions=[],  # no positions
            clock=_open_clock(),
            checked_at=utc_now_iso(),
        )
        assert lc["fill"]["position_confirmed"] is False

    def test_rejected_order_logged_as_rejected(self):
        order = _broker_order(status="rejected")
        lookup = _broker_lookup([order])
        lc = build_order_lifecycle(
            audit=_audit(),
            broker_lookup=lookup,
            plan_refs=None,
            trigger_snapshot_hash=None,
            positions=[],
            clock=_open_clock(),
            checked_at=utc_now_iso(),
        )
        assert lc["lifecycle_status"] == "rejected"
        assert lc["fill"] is None

    def test_rejected_order_not_treated_as_success(self):
        order = _broker_order(status="rejected")
        lookup = _broker_lookup([order])
        lc = build_order_lifecycle(
            audit=_audit(),
            broker_lookup=lookup,
            plan_refs=None,
            trigger_snapshot_hash=None,
            positions=[],
            clock=_open_clock(),
            checked_at=utc_now_iso(),
        )
        assert lc["lifecycle_status"] != "filled"
        assert lc["lifecycle_status"] != "pending_new"

    def test_missing_broker_order_creates_warning(self):
        # Empty broker lookup — order not found
        lc = build_order_lifecycle(
            audit=_audit(),
            broker_lookup={"by_broker_id": {}, "by_client_id": {}},
            plan_refs=None,
            trigger_snapshot_hash=None,
            positions=[],
            clock=_open_clock(),
            checked_at=utc_now_iso(),
        )
        assert lc["lifecycle_status"] == "missing"
        assert lc["warning"] is not None
        assert "not found" in lc["warning"].lower() or "missing" in lc["warning"].lower()

    def test_missing_broker_order_not_treated_as_success(self):
        lc = build_order_lifecycle(
            audit=_audit(),
            broker_lookup={"by_broker_id": {}, "by_client_id": {}},
            plan_refs=None,
            trigger_snapshot_hash=None,
            positions=[],
            clock=_open_clock(),
            checked_at=utc_now_iso(),
        )
        assert lc["lifecycle_status"] not in ("filled", "pending_new", "new")

    def test_canceled_order_tracked(self):
        order = _broker_order(status="canceled")
        lookup = _broker_lookup([order])
        lc = build_order_lifecycle(
            audit=_audit(),
            broker_lookup=lookup,
            plan_refs=None,
            trigger_snapshot_hash=None,
            positions=[],
            clock=_open_clock(),
            checked_at=utc_now_iso(),
        )
        assert lc["lifecycle_status"] == "canceled"
        assert lc["fill"] is None

    def test_fallback_to_client_id_lookup(self):
        """Order found by client_order_id when broker_order_id lookup fails."""
        order = _broker_order(
            broker_id="broker-xyz",
            client_id="TOS-20260513T160035-WELL-BUY",
            status="new",
        )
        # Only in by_client_id, not by_broker_id
        lookup = {
            "by_broker_id": {},
            "by_client_id": {"TOS-20260513T160035-WELL-BUY": order},
        }
        lc = build_order_lifecycle(
            audit=_audit(broker_order_id="broker-different"),
            broker_lookup=lookup,
            plan_refs=None,
            trigger_snapshot_hash=None,
            positions=[],
            clock=_open_clock(),
            checked_at=utc_now_iso(),
        )
        assert lc["lifecycle_status"] == "new"
        assert lc["warning"] is None


# ===========================================================================
# TestFillReconciliation — plan linkage
# ===========================================================================

class TestFillReconciliation:
    def _filled_order(self) -> dict:
        return _broker_order(
            status="filled",
            filled_avg_price=219.50,
            filled_qty=0.113,
            filled_at="2026-05-13T16:30:00Z",
        )

    def test_fill_links_plan_id(self):
        plan_refs = {
            "plan_id": "trade_plan-20260513T160035-abcdef12",
            "run_id": "execution-20260513T160035-12345678",
            "trade_plan_hash": "a" * 64,
        }
        fill = reconcile_fill(
            broker_order=self._filled_order(),
            positions=[{"symbol": "WELL", "qty": "0.113"}],
            plan_refs=plan_refs,
            trigger_snapshot_hash="b" * 64,
        )
        assert fill["plan_id"] == plan_refs["plan_id"]

    def test_fill_links_run_id(self):
        plan_refs = {
            "plan_id": "trade_plan-20260513T160035-abcdef12",
            "run_id": "execution-20260513T160035-12345678",
            "trade_plan_hash": "a" * 64,
        }
        fill = reconcile_fill(
            broker_order=self._filled_order(),
            positions=[{"symbol": "WELL", "qty": "0.113"}],
            plan_refs=plan_refs,
            trigger_snapshot_hash=None,
        )
        assert fill["run_id"] == plan_refs["run_id"]

    def test_fill_links_trade_plan_hash(self):
        plan_refs = {
            "plan_id": "trade_plan-20260513T160035-abcdef12",
            "run_id": "execution-20260513T160035-12345678",
            "trade_plan_hash": "a" * 64,
        }
        fill = reconcile_fill(
            broker_order=self._filled_order(),
            positions=[],
            plan_refs=plan_refs,
            trigger_snapshot_hash=None,
        )
        assert fill["trade_plan_hash"] == "a" * 64

    def test_fill_links_trigger_snapshot_hash(self):
        plan_refs = {
            "plan_id": "trade_plan-20260513T160035-abcdef12",
            "run_id": "execution-20260513T160035-12345678",
            "trade_plan_hash": "a" * 64,
        }
        fill = reconcile_fill(
            broker_order=self._filled_order(),
            positions=[],
            plan_refs=plan_refs,
            trigger_snapshot_hash="c" * 64,
        )
        assert fill["trigger_snapshot_hash"] == "c" * 64

    def test_fill_with_no_plan_refs_has_null_ids(self):
        fill = reconcile_fill(
            broker_order=self._filled_order(),
            positions=[],
            plan_refs=None,
            trigger_snapshot_hash=None,
        )
        assert fill["plan_id"] is None
        assert fill["run_id"] is None
        assert fill["trade_plan_hash"] is None

    def test_fill_notional_computed(self):
        order = _broker_order(
            status="filled", filled_avg_price=219.50, filled_qty=0.113
        )
        fill = reconcile_fill(
            broker_order=order,
            positions=[],
            plan_refs=None,
            trigger_snapshot_hash=None,
        )
        assert fill["filled_notional"] == pytest.approx(219.50 * 0.113, abs=0.01)


# ===========================================================================
# TestStaleOrderDetection
# ===========================================================================

class TestStaleOrderDetection:
    def test_active_order_market_closed_is_stale(self):
        assert is_stale_order("new", _closed_clock(), "day") is True

    def test_active_order_market_open_not_stale(self):
        assert is_stale_order("new", _open_clock(), "day") is False

    def test_terminal_order_not_stale(self):
        assert is_stale_order("filled", _closed_clock(), "day") is False

    def test_missing_order_not_stale(self):
        assert is_stale_order("missing", _closed_clock(), "day") is False

    def test_gtc_order_not_stale_even_when_market_closed(self):
        assert is_stale_order("new", _closed_clock(), "gtc") is False

    def test_pending_new_market_closed_is_stale(self):
        assert is_stale_order("pending_new", _closed_clock(), "day") is True

    def test_stale_warning_appears_in_lifecycle(self):
        order = _broker_order(status="new")
        lookup = _broker_lookup([order])
        lc = build_order_lifecycle(
            audit=_audit(time_in_force="day"),
            broker_lookup=lookup,
            plan_refs=None,
            trigger_snapshot_hash=None,
            positions=[],
            clock=_closed_clock(),
            checked_at=utc_now_iso(),
        )
        assert lc["stale_warning"] is not None
        assert "stale" in lc["stale_warning"].lower() or "active" in lc["stale_warning"].lower()

    def test_stale_warning_appears_in_report(self, tmp_path):
        order = _broker_order(status="new")
        audit = _audit(time_in_force="day")
        _write_audit(tmp_path, audit)
        report = run_order_monitor(
            broker_lookup=_broker_lookup([order]),
            orders_dir=tmp_path,
            executions_dir=tmp_path / "executions",
            positions=[],
            clock=_closed_clock(),
        )
        assert len(report["stale_orders"]) > 0


# ===========================================================================
# TestPlanRefsIndex
# ===========================================================================

class TestPlanRefsIndex:
    def test_finds_plan_refs_for_client_order_id(self, tmp_path):
        exec_report = {
            "run_id": "execution-20260513T160035-12345678",
            "plan_id": "trade_plan-20260513T160035-abcdef12",
            "trade_plan_hash": "a" * 64,
            "orders_submitted": [
                {"client_order_id": "TOS-20260513T160035-WELL-BUY", "submitted": True},
            ],
        }
        _write_exec_report(tmp_path, exec_report)
        index = build_plan_refs_index(tmp_path)
        refs = index.get("TOS-20260513T160035-WELL-BUY")
        assert refs is not None
        assert refs["plan_id"] == exec_report["plan_id"]
        assert refs["run_id"] == exec_report["run_id"]
        assert refs["trade_plan_hash"] == exec_report["trade_plan_hash"]

    def test_returns_empty_for_missing_executions_dir(self, tmp_path):
        index = build_plan_refs_index(tmp_path / "nonexistent")
        assert index == {}

    def test_multiple_execution_reports_indexed(self, tmp_path):
        for i in range(3):
            _write_exec_report(tmp_path, {
                "run_id": f"execution-00000000T00000{i}-{'x' * 8}",
                "plan_id": f"trade_plan-00000000T00000{i}-{'y' * 8}",
                "trade_plan_hash": str(i) * 64,
                "orders_submitted": [
                    {"client_order_id": f"TOS-ORDER-{i}", "submitted": True},
                ],
            })
        index = build_plan_refs_index(tmp_path)
        assert len(index) == 3


# ===========================================================================
# TestLoadSubmittedAudits
# ===========================================================================

class TestLoadSubmittedAudits:
    def test_loads_submitted_audits(self, tmp_path):
        _write_audit(tmp_path, _audit(submitted=True))
        entries = load_submitted_audits(tmp_path)
        assert len(entries) == 1

    def test_skips_non_submitted_audits(self, tmp_path):
        audit = _audit(submitted=False)
        _write_audit(tmp_path, audit)
        entries = load_submitted_audits(tmp_path)
        assert len(entries) == 0

    def test_skips_monitor_report_files(self, tmp_path):
        # Write a monitor report file — should be ignored
        report_path = tmp_path / "order_monitor_run123.json"
        report_path.write_text(json.dumps({"orders_tracked": 1}) + "\n")
        entries = load_submitted_audits(tmp_path)
        assert len(entries) == 0

    def test_empty_orders_dir(self, tmp_path):
        entries = load_submitted_audits(tmp_path)
        assert entries == []

    def test_nonexistent_orders_dir(self, tmp_path):
        entries = load_submitted_audits(tmp_path / "nonexistent")
        assert entries == []


# ===========================================================================
# TestRunOrderMonitor — full pipeline
# ===========================================================================

class TestRunOrderMonitor:
    def test_returns_report_dict(self, tmp_path):
        report = run_order_monitor(
            broker_lookup={"by_broker_id": {}, "by_client_id": {}},
            orders_dir=tmp_path,
            executions_dir=tmp_path / "executions",
            positions=[],
            clock=_open_clock(),
        )
        assert isinstance(report, dict)
        assert "run_id" in report
        assert "report_hash" in report

    def test_report_has_safety_block(self, tmp_path):
        report = run_order_monitor(
            broker_lookup={"by_broker_id": {}, "by_client_id": {}},
            orders_dir=tmp_path,
            executions_dir=tmp_path / "executions",
            positions=[],
            clock=_open_clock(),
        )
        safety = report.get("safety", {})
        assert safety.get("submit_order_called") is False
        assert safety.get("cancel_order_called") is False
        assert safety.get("replace_order_called") is False

    def test_zero_orders_when_no_audit_files(self, tmp_path):
        report = run_order_monitor(
            broker_lookup={"by_broker_id": {}, "by_client_id": {}},
            orders_dir=tmp_path,
            executions_dir=tmp_path / "executions",
            positions=[],
            clock=_open_clock(),
        )
        assert report["orders_tracked"] == 0
        assert report["lifecycles"] == []

    def test_pending_new_order_tracked_in_report(self, tmp_path):
        order = _broker_order(status="pending_new")
        audit = _audit()
        _write_audit(tmp_path, audit)
        report = run_order_monitor(
            broker_lookup=_broker_lookup([order]),
            orders_dir=tmp_path,
            executions_dir=tmp_path / "executions",
            positions=[],
            clock=_open_clock(),
        )
        assert report["orders_tracked"] == 1
        assert report["orders_active"] == 1
        lc = report["lifecycles"][0]
        assert lc["lifecycle_status"] == "pending_new"
        assert lc["symbol"] == "WELL"

    def test_filled_order_increments_filled_count(self, tmp_path):
        order = _broker_order(
            status="filled", filled_avg_price=219.50, filled_qty=0.113
        )
        _write_audit(tmp_path, _audit())
        report = run_order_monitor(
            broker_lookup=_broker_lookup([order]),
            orders_dir=tmp_path,
            executions_dir=tmp_path / "executions",
            positions=[{"symbol": "WELL", "qty": "0.113"}],
            clock=_open_clock(),
        )
        assert report["orders_filled"] == 1
        assert report["lifecycles"][0]["fill"] is not None

    def test_rejected_order_counted_correctly(self, tmp_path):
        order = _broker_order(status="rejected")
        _write_audit(tmp_path, _audit())
        report = run_order_monitor(
            broker_lookup=_broker_lookup([order]),
            orders_dir=tmp_path,
            executions_dir=tmp_path / "executions",
            positions=[],
            clock=_open_clock(),
        )
        assert report["orders_rejected"] == 1
        assert report["orders_filled"] == 0
        assert report["lifecycles"][0]["lifecycle_status"] == "rejected"

    def test_missing_broker_order_counted_as_missing(self, tmp_path):
        _write_audit(tmp_path, _audit())
        report = run_order_monitor(
            broker_lookup={"by_broker_id": {}, "by_client_id": {}},
            orders_dir=tmp_path,
            executions_dir=tmp_path / "executions",
            positions=[],
            clock=_open_clock(),
        )
        assert report["orders_missing"] == 1
        assert len(report["warnings"]) >= 1

    def test_audit_file_updated_with_lifecycle_status(self, tmp_path):
        order = _broker_order(status="filled", filled_avg_price=219.50, filled_qty=0.113)
        audit = _audit()
        audit_path = _write_audit(tmp_path, audit)
        run_order_monitor(
            broker_lookup=_broker_lookup([order]),
            orders_dir=tmp_path,
            executions_dir=tmp_path / "executions",
            positions=[{"symbol": "WELL", "qty": "0.113"}],
            clock=_open_clock(),
        )
        updated = json.loads(audit_path.read_text())
        assert updated.get("lifecycle_status") == "filled"
        assert updated.get("lifecycle_checked_at") is not None

    def test_report_hash_present_and_64_chars(self, tmp_path):
        report = run_order_monitor(
            broker_lookup={"by_broker_id": {}, "by_client_id": {}},
            orders_dir=tmp_path,
            executions_dir=tmp_path / "executions",
            positions=[],
            clock=_open_clock(),
        )
        h = report.get("report_hash")
        assert h is not None
        assert len(h) == 64

    def test_dry_run_noted_in_report(self, tmp_path):
        report = run_order_monitor(
            broker_lookup={"by_broker_id": {}, "by_client_id": {}},
            orders_dir=tmp_path,
            executions_dir=tmp_path / "executions",
            positions=[],
            clock=_open_clock(),
            dry_run=True,
        )
        assert report["dry_run"] is True
        assert report["source"] == "stored_snapshot"

    def test_fill_includes_plan_refs_from_execution_report(self, tmp_path):
        exec_dir = tmp_path / "executions"
        exec_dir.mkdir()
        _write_exec_report(exec_dir, {
            "run_id": "execution-20260513T160035-12345678",
            "plan_id": "trade_plan-20260513T160035-abcdef12",
            "trade_plan_hash": "a" * 64,
            "orders_submitted": [
                {"client_order_id": "TOS-20260513T160035-WELL-BUY", "submitted": True},
            ],
        })
        order = _broker_order(
            status="filled", filled_avg_price=219.50, filled_qty=0.113
        )
        _write_audit(tmp_path, _audit())
        report = run_order_monitor(
            broker_lookup=_broker_lookup([order]),
            orders_dir=tmp_path,
            executions_dir=exec_dir,
            positions=[{"symbol": "WELL", "qty": "0.113"}],
            clock=_open_clock(),
        )
        fill = report["lifecycles"][0]["fill"]
        assert fill["plan_id"] == "trade_plan-20260513T160035-abcdef12"
        assert fill["run_id"] == "execution-20260513T160035-12345678"
        assert fill["trade_plan_hash"] == "a" * 64


# ===========================================================================
# TestAppendTradeLog
# ===========================================================================

class TestAppendTradeLog:
    def test_trade_log_appended(self, tmp_path):
        log_path = tmp_path / "TRADE-LOG.md"
        report = {
            "run_id": "order_monitor-test",
            "generated_at": utc_now_iso(),
            "dry_run": False,
            "source": "alpaca_paper",
            "orders_tracked": 1,
            "orders_filled": 0,
            "orders_active": 1,
            "orders_missing": 0,
            "orders_rejected": 0,
            "stale_orders": [],
            "warnings": [],
            "lifecycles": [],
        }
        append_trade_log(report, log_path)
        content = log_path.read_text()
        assert "order_monitor" in content
        assert "orders_tracked" in content

    def test_trade_log_contains_lifecycle_status(self, tmp_path):
        log_path = tmp_path / "TRADE-LOG.md"
        report = {
            "run_id": "order_monitor-test",
            "generated_at": utc_now_iso(),
            "dry_run": False,
            "source": "alpaca_paper",
            "orders_tracked": 1,
            "orders_filled": 0,
            "orders_active": 1,
            "orders_missing": 0,
            "orders_rejected": 0,
            "stale_orders": [],
            "warnings": [],
            "lifecycles": [{
                "client_order_id": "TOS-20260513T160035-WELL-BUY",
                "symbol": "WELL",
                "side": "buy",
                "notional": 25.0,
                "lifecycle_status": "pending_new",
                "fill": None,
            }],
        }
        append_trade_log(report, log_path)
        content = log_path.read_text()
        assert "pending_new" in content
        assert "WELL" in content

    def test_trade_log_appends_not_overwrites(self, tmp_path):
        log_path = tmp_path / "TRADE-LOG.md"
        log_path.write_text("## existing entry\n\nprevious content\n")
        report = {
            "run_id": "order_monitor-test",
            "generated_at": utc_now_iso(),
            "dry_run": True,
            "source": "stored_snapshot",
            "orders_tracked": 0,
            "orders_filled": 0,
            "orders_active": 0,
            "orders_missing": 0,
            "orders_rejected": 0,
            "stale_orders": [],
            "warnings": [],
            "lifecycles": [],
        }
        append_trade_log(report, log_path)
        content = log_path.read_text()
        assert "existing entry" in content
        assert "previous content" in content


# ===========================================================================
# TestMonitorNeverSubmitsCancelsReplaces — source inspection
# ===========================================================================

class TestMonitorNeverSubmitsCancelsReplaces:
    """Prove by source inspection that the module never mutates broker state."""

    @classmethod
    def _src(cls) -> str:
        import trading_os.monitoring.order_monitor as mod
        return Path(mod.__file__).read_text(encoding="utf-8")

    def test_no_submit_order_call(self):
        src = self._src()
        assert not re.search(r"\bsubmit_order\s*\(", src), (
            "order_monitor.py must never call submit_order"
        )

    def test_no_cancel_order_call(self):
        src = self._src()
        assert not re.search(r"\bcancel_order\s*\(", src), (
            "order_monitor.py must never call cancel_order"
        )

    def test_no_replace_order_call(self):
        src = self._src()
        assert not re.search(r"\breplace_order\s*\(", src), (
            "order_monitor.py must never call replace_order"
        )

    def test_no_paper_executor_import(self):
        src = self._src()
        assert not re.search(
            r"^\s*(import|from)\s+.*paper_executor", src, re.MULTILINE
        ), "order_monitor.py must not import paper_executor"

    def test_no_approved_for_execution_true(self):
        src = self._src()
        assert not re.search(r'"approved_for_execution"\s*:\s*True', src), (
            "order_monitor.py must never set approved_for_execution=True"
        )

    def test_safety_block_always_false(self, tmp_path):
        report = run_order_monitor(
            broker_lookup={"by_broker_id": {}, "by_client_id": {}},
            orders_dir=tmp_path,
            executions_dir=tmp_path / "executions",
            positions=[],
            clock=_open_clock(),
        )
        safety = report["safety"]
        assert safety["submit_order_called"] is False
        assert safety["cancel_order_called"] is False
        assert safety["replace_order_called"] is False


# ===========================================================================
# TestFetchBrokerOrdersLookupPaths — all four lookup strategies
#
# fetch_broker_orders uses a real trading_client, so we mock it here.
# Each test exercises exactly one lookup path.
# ===========================================================================

from unittest.mock import MagicMock, call


def _mock_order_primitive(
    broker_id: str = "broker-abc123",
    client_id: str = "TOS-20260513T160035-WELL-BUY",
    symbol: str = "WELL",
    status: str = "pending_new",
) -> dict:
    return {
        "id": broker_id,
        "client_order_id": client_id,
        "symbol": symbol,
        "status": status,
        "side": "buy",
        "order_type": "limit",
        "time_in_force": "day",
    }


def _make_sdk_order(primitive: dict) -> MagicMock:
    """Return a mock Alpaca SDK Order that model_dump() returns the primitive."""
    obj = MagicMock()
    obj.model_dump.return_value = primitive
    return obj


class TestFetchBrokerOrdersLookupPaths:
    """Mock the TradingClient to exercise each lookup path in isolation."""

    def _import_fn(self):
        from trading_os.monitoring.order_monitor import fetch_broker_orders
        return fetch_broker_orders

    def _client(
        self,
        open_orders=None,
        closed_orders=None,
        by_id_order=None,
        by_client_id_order=None,
        by_id_raises=False,
        by_client_id_raises=False,
    ) -> MagicMock:
        """Build a mock TradingClient with controlled return values."""
        client = MagicMock()

        def _get_orders(filter=None):
            status = getattr(filter, "status", None)
            status_val = status.value if hasattr(status, "value") else str(status)
            if status_val == "open":
                return [_make_sdk_order(o) for o in (open_orders or [])]
            else:
                return [_make_sdk_order(o) for o in (closed_orders or [])]

        client.get_orders.side_effect = _get_orders

        if by_id_raises:
            client.get_order_by_id.side_effect = Exception("order not found")
        elif by_id_order:
            client.get_order_by_id.return_value = _make_sdk_order(by_id_order)
        else:
            client.get_order_by_id.side_effect = Exception("order not found")

        if by_client_id_raises:
            client.get_order_by_client_id.side_effect = Exception("order not found")
        elif by_client_id_order:
            client.get_order_by_client_id.return_value = _make_sdk_order(by_client_id_order)
        else:
            client.get_order_by_client_id.side_effect = Exception("order not found")

        return client

    def test_order_found_in_open_orders_bulk(self):
        fn = self._import_fn()
        prim = _mock_order_primitive(status="new")
        client = self._client(open_orders=[prim])
        result = fn(client, known_broker_ids=["broker-abc123"])
        assert "broker-abc123" in result["by_broker_id"]
        assert result["by_broker_id"]["broker-abc123"]["status"] == "new"
        assert result["fetch_log"]["open_count"] == 1

    def test_order_found_in_closed_orders_bulk(self):
        fn = self._import_fn()
        prim = _mock_order_primitive(status="filled")
        client = self._client(closed_orders=[prim])
        result = fn(client, known_broker_ids=["broker-abc123"])
        assert "broker-abc123" in result["by_broker_id"]
        assert result["by_broker_id"]["broker-abc123"]["status"] == "filled"
        assert result["fetch_log"]["closed_count"] == 1

    def test_order_found_by_direct_broker_id_fallback(self):
        """Not in bulk; found via get_order_by_id."""
        fn = self._import_fn()
        prim = _mock_order_primitive(status="expired")
        # Bulk returns nothing; direct lookup succeeds
        client = self._client(by_id_order=prim)
        result = fn(
            client,
            known_broker_ids=["broker-abc123"],
            known_client_ids=["TOS-20260513T160035-WELL-BUY"],
        )
        assert "broker-abc123" in result["by_broker_id"]
        assert result["by_broker_id"]["broker-abc123"]["status"] == "expired"
        assert result["fetch_log"]["direct_broker_id_hits"] == 1
        # No client_id lookup needed — client_id was indexed via broker_id hit
        assert result["fetch_log"]["direct_client_id_lookups"] == 0

    def test_order_found_by_direct_client_id_fallback(self):
        """Not in bulk, broker_id lookup fails; found via get_order_by_client_id."""
        fn = self._import_fn()
        prim = _mock_order_primitive(status="canceled")
        # Bulk empty, broker_id lookup raises, client_id lookup succeeds
        client = self._client(by_id_raises=True, by_client_id_order=prim)
        result = fn(
            client,
            known_broker_ids=["broker-abc123"],
            known_client_ids=["TOS-20260513T160035-WELL-BUY"],
        )
        assert "TOS-20260513T160035-WELL-BUY" in result["by_client_id"]
        assert result["by_client_id"]["TOS-20260513T160035-WELL-BUY"]["status"] == "canceled"
        assert result["fetch_log"]["direct_client_id_hits"] == 1

    def test_truly_missing_order_not_in_result(self):
        """All three layers fail — order is absent from all lookup results."""
        fn = self._import_fn()
        # Bulk empty, both direct lookups raise
        client = self._client(by_id_raises=True, by_client_id_raises=True)
        result = fn(
            client,
            known_broker_ids=["broker-abc123"],
            known_client_ids=["TOS-20260513T160035-WELL-BUY"],
        )
        assert "broker-abc123" not in result["by_broker_id"]
        assert "TOS-20260513T160035-WELL-BUY" not in result["by_client_id"]
        assert result["fetch_log"]["direct_broker_id_errors"] == 1
        assert result["fetch_log"]["direct_client_id_errors"] == 1

    def test_truly_missing_order_shows_warning_in_lifecycle(self):
        """When all lookups fail, build_order_lifecycle produces a warning."""
        lc = build_order_lifecycle(
            audit=_audit(),
            broker_lookup={"by_broker_id": {}, "by_client_id": {}},
            plan_refs=None,
            trigger_snapshot_hash=None,
            positions=[],
            clock=_open_clock(),
            checked_at=utc_now_iso(),
        )
        assert lc["lifecycle_status"] == "missing"
        assert lc["warning"] is not None

    def test_fetch_log_contains_no_secrets(self):
        """fetch_log must never contain API keys, secrets, or credentials."""
        fn = self._import_fn()
        prim = _mock_order_primitive()
        client = self._client(open_orders=[prim])
        result = fn(client, known_broker_ids=["broker-abc123"])
        fetch_log_str = str(result["fetch_log"])
        for forbidden in ("api_key", "secret", "password", "token", "credential"):
            assert forbidden.lower() not in fetch_log_str.lower(), (
                f"fetch_log must not contain {forbidden!r}"
            )

    def test_closed_orders_request_uses_after_date(self):
        """Prove the closed orders request includes an `after` datetime (7-day window)."""
        fn = self._import_fn()
        client = self._client()
        fn(client)
        # Find the closed-orders call
        closed_call = None
        for c in client.get_orders.call_args_list:
            filt = c.kwargs.get("filter") or (c.args[0] if c.args else None)
            if filt and hasattr(filt, "status"):
                status_val = filt.status.value if hasattr(filt.status, "value") else str(filt.status)
                if status_val == "closed":
                    closed_call = filt
                    break
        assert closed_call is not None, "A closed-orders request must be made"
        assert closed_call.after is not None, (
            "closed orders request must include `after` date to enforce 7-day lookback window"
        )

    def test_no_direct_lookup_when_already_in_bulk(self):
        """If an order is found in bulk, direct lookup is not called."""
        fn = self._import_fn()
        prim = _mock_order_primitive(status="new")
        client = self._client(open_orders=[prim])
        fn(client, known_broker_ids=["broker-abc123"])
        # get_order_by_id should not have been called since it was in open orders
        assert client.get_order_by_id.call_count == 0


# ---------------------------------------------------------------------------
# TestStatusNormalization — _normalize_status and lifecycle counter correctness
# ---------------------------------------------------------------------------

class _StrEnum(str):
    """Minimal str-subclass that mimics Alpaca SDK str-enum behaviour."""
    def __new__(cls, value, name=None):
        obj = super().__new__(cls, value)
        obj._name_ = name or value.upper()
        obj.value = value
        return obj

    def __str__(self):
        return f"{type(self).__name__}.{self._name_}"


class TestStatusNormalization:
    """Prove _normalize_status handles plain strings, str-enums, and aliases."""

    # --- _normalize_status unit tests ---

    def test_plain_string_filled(self):
        assert _normalize_status("filled") == "filled"

    def test_plain_string_partially_filled(self):
        assert _normalize_status("partially_filled") == "partially_filled"

    def test_plain_string_canceled(self):
        assert _normalize_status("canceled") == "canceled"

    def test_british_cancelled_aliased(self):
        assert _normalize_status("cancelled") == "canceled"

    def test_plain_string_active_statuses(self):
        for s in ("new", "pending_new", "accepted", "pending_cancel", "pending_replace"):
            assert _normalize_status(s) == s, f"expected {s!r} to pass through"

    def test_plain_string_expired(self):
        assert _normalize_status("expired") == "expired"

    def test_plain_string_rejected(self):
        assert _normalize_status("rejected") == "rejected"

    def test_none_returns_unknown(self):
        assert _normalize_status(None) == "unknown"

    def test_unrecognised_string(self):
        assert _normalize_status("totally_made_up") == "totally_made_up"

    def test_str_enum_filled(self):
        """str-enum member with value 'filled' must normalise to 'filled', not 'classname.FILLED'."""
        enum_member = _StrEnum("filled", "FILLED")
        assert _normalize_status(enum_member) == "filled"

    def test_str_enum_partially_filled(self):
        enum_member = _StrEnum("partially_filled", "PARTIALLY_FILLED")
        assert _normalize_status(enum_member) == "partially_filled"

    def test_str_enum_canceled(self):
        enum_member = _StrEnum("canceled", "CANCELED")
        assert _normalize_status(enum_member) == "canceled"

    def test_str_enum_cancelled_aliased(self):
        enum_member = _StrEnum("cancelled", "CANCELLED")
        assert _normalize_status(enum_member) == "canceled"

    def test_str_enum_new(self):
        enum_member = _StrEnum("new", "NEW")
        assert _normalize_status(enum_member) == "new"

    def test_str_enum_rejected(self):
        enum_member = _StrEnum("rejected", "REJECTED")
        assert _normalize_status(enum_member) == "rejected"

    # --- lifecycle classification via build_order_lifecycle ---

    def _lc(self, status, broker_id="broker-abc123"):
        """Helper: build lifecycle for a single order with given broker status."""
        audit = _audit(broker_order_id=broker_id)
        order = _broker_order(broker_id=broker_id, status=status)
        lookup = _broker_lookup([order])
        clock = {"is_open": True}
        return build_order_lifecycle(
            audit=audit,
            broker_lookup=lookup,
            plan_refs=None,
            trigger_snapshot_hash=None,
            positions=[],
            clock=clock,
            checked_at=utc_now_iso(),
        )

    def test_plain_filled_produces_lifecycle_filled(self):
        lc = self._lc("filled")
        assert lc["lifecycle_status"] == "filled"

    def test_str_enum_filled_produces_lifecycle_filled(self):
        """Regression: Alpaca SDK str-enum must not produce lifecycle=unknown."""
        lc = self._lc(_StrEnum("filled", "FILLED"))
        assert lc["lifecycle_status"] == "filled"

    def test_str_enum_filled_has_fill_block(self):
        """When lifecycle=filled, fill block must be present (not None)."""
        lc = self._lc(_StrEnum("filled", "FILLED"))
        assert lc["fill"] is not None, "fill block must be present for filled orders"

    def test_str_enum_partially_filled_lifecycle(self):
        lc = self._lc(_StrEnum("partially_filled", "PARTIALLY_FILLED"))
        assert lc["lifecycle_status"] == "partially_filled"
        assert lc["fill"] is not None

    def test_str_enum_canceled_lifecycle(self):
        lc = self._lc(_StrEnum("canceled", "CANCELED"))
        assert lc["lifecycle_status"] == "canceled"

    def test_str_enum_cancelled_lifecycle(self):
        """British spelling str-enum must map to lifecycle_status='canceled'."""
        lc = self._lc(_StrEnum("cancelled", "CANCELLED"))
        assert lc["lifecycle_status"] == "canceled"

    def test_str_enum_new_is_active(self):
        lc = self._lc(_StrEnum("new", "NEW"))
        assert lc["lifecycle_status"] == "new"

    def test_str_enum_pending_new_is_active(self):
        lc = self._lc(_StrEnum("pending_new", "PENDING_NEW"))
        assert lc["lifecycle_status"] == "pending_new"

    def test_str_enum_accepted_is_active(self):
        lc = self._lc(_StrEnum("accepted", "ACCEPTED"))
        assert lc["lifecycle_status"] == "accepted"

    def test_str_enum_rejected_lifecycle(self):
        lc = self._lc(_StrEnum("rejected", "REJECTED"))
        assert lc["lifecycle_status"] == "rejected"

    def test_str_enum_expired_lifecycle(self):
        lc = self._lc(_StrEnum("expired", "EXPIRED"))
        assert lc["lifecycle_status"] == "expired"

    def test_unknown_status_produces_unknown_lifecycle(self):
        import warnings
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            lc = self._lc("totally_bogus_status_xyz")
        assert lc["lifecycle_status"] == "unknown"
        assert any("unrecognised" in str(warning.message).lower() for warning in w), (
            "expected a RuntimeWarning about unrecognised status"
        )

    # --- orders_filled counter ---

    def _run_monitor(self, status, tmp_path):
        """Helper: write one audit file and run monitor with given broker status."""
        orders_dir = tmp_path / "orders"
        orders_dir.mkdir(parents=True)
        executions_dir = tmp_path / "executions"
        executions_dir.mkdir(parents=True)

        audit = _audit(client_order_id="TOS-test", broker_order_id="broker-001")
        audit_path = orders_dir / "TOS-test.json"
        audit_path.write_text(json.dumps(audit), encoding="utf-8")

        order = _broker_order(broker_id="broker-001", client_id="TOS-test", status=status)
        lookup = _broker_lookup([order])
        clock = {"is_open": True}

        return run_order_monitor(
            broker_lookup=lookup,
            orders_dir=orders_dir,
            executions_dir=executions_dir,
            positions=[],
            clock=clock,
        )

    def test_orders_filled_counter_increments(self, tmp_path):
        report = self._run_monitor("filled", tmp_path)
        assert report["orders_filled"] == 1, (
            f"expected orders_filled=1 for filled order, got {report['orders_filled']}"
        )

    def test_orders_filled_counter_with_str_enum(self, tmp_path):
        """Regression: str-enum filled must increment orders_filled, not leave it at 0."""
        report = self._run_monitor(_StrEnum("filled", "FILLED"), tmp_path)
        assert report["orders_filled"] == 1, (
            f"expected orders_filled=1 for str-enum filled order, got {report['orders_filled']}"
        )

    def test_orders_partially_filled_counter(self, tmp_path):
        report = self._run_monitor("partially_filled", tmp_path)
        assert report["orders_partially_filled"] == 1

    def test_orders_filled_zero_for_active(self, tmp_path):
        report = self._run_monitor("new", tmp_path)
        assert report["orders_filled"] == 0

    # --- safety block ---

    def test_safety_block_never_submits(self, tmp_path):
        report = self._run_monitor("filled", tmp_path)
        sb = report.get("safety", {})
        assert sb.get("submit_order_called") is False
        assert sb.get("cancel_order_called") is False
        assert sb.get("replace_order_called") is False

    def test_safety_block_present_for_unknown_status(self, tmp_path):
        import warnings
        with warnings.catch_warnings(record=True):
            warnings.simplefilter("always")
            report = self._run_monitor("bogus_status_xyz", tmp_path)
        sb = report.get("safety", {})
        assert sb.get("submit_order_called") is False
        assert sb.get("cancel_order_called") is False
        assert sb.get("replace_order_called") is False
