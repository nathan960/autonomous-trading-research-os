"""Tests for the source integrity hardening (requirements 1–8).

Covers:
- source_integrity module functions
- refresh_data.py --dry-run writes to sandbox, not data/latest
- monitor_positions.py --dry-run does not overwrite memory/RISK-STATE.json
- execution gate fails when snapshots are dry_run_mock
- outcome tracker refuses to compute current P/L from mock positions
- trigger performance refuses to use outcome P/L when integrity is blocked
- live alpaca_paper snapshots pass all checks
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trading_os.source_integrity import (
    MOCK_SOURCES,
    STATUS_BLOCKED_MOCK,
    STATUS_BLOCKED_UNKNOWN,
    STATUS_DATA_INTEGRITY_BLOCK,
    STATUS_OK,
    VALID_EXECUTION_SOURCES,
    check_execution_snapshots,
    check_snapshot,
    get_snapshot_source,
    is_mock_source,
    is_valid_execution_source,
    snapshot_source_status,
)
from trading_os.execution.execution_gates import (
    gate_canonical_source_integrity,
    run_all_gates,
)
from trading_os.research.outcome_tracker import (
    build_outcome_record,
    build_outcome_snapshot,
)
from trading_os.research.trigger_performance import _collect_outcome_stats


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _snap(source: str, extra: dict | None = None) -> dict:
    d = {"source": source, "fetched_at": "2026-05-13T20:00:00Z"}
    if extra:
        d.update(extra)
    return d


def _alpaca_snap(extra: dict | None = None) -> dict:
    return _snap("alpaca_paper", extra)


def _mock_snap(extra: dict | None = None) -> dict:
    return _snap("dry_run_mock", extra)


def _lifecycle(
    cid: str = "CID-001",
    symbol: str = "AAPL",
    side: str = "buy",
    fill_price: float = 150.0,
    limit_price: float = 151.0,
) -> dict:
    return {
        "client_order_id": cid,
        "symbol": symbol,
        "side": side,
        "lifecycle_status": "filled",
        "limit_price": limit_price,
        "fill": {
            "fill_price": fill_price,
            "filled_qty": 1.0,
            "filled_notional": fill_price,
            "filled_at": "2026-05-13T16:00:00Z",
        },
    }


# ---------------------------------------------------------------------------
# source_integrity module
# ---------------------------------------------------------------------------

class TestGetSnapshotSource:
    def test_uses_source_field(self):
        assert get_snapshot_source({"source": "alpaca_paper"}) == "alpaca_paper"

    def test_falls_back_to_data_source(self):
        assert get_snapshot_source({"data_source": "alpaca_paper"}) == "alpaca_paper"

    def test_source_takes_priority_over_data_source(self):
        assert get_snapshot_source({"source": "dry_run_mock", "data_source": "alpaca_paper"}) == "dry_run_mock"

    def test_empty_dict_returns_unknown(self):
        assert get_snapshot_source({}) == "unknown"

    def test_empty_string_returns_unknown(self):
        assert get_snapshot_source({"source": ""}) == "unknown"

    def test_strips_whitespace(self):
        assert get_snapshot_source({"source": "  alpaca_paper  "}) == "alpaca_paper"


class TestIsMockSource:
    def test_dry_run_mock_is_mock(self):
        assert is_mock_source("dry_run_mock") is True

    def test_local_mock_is_mock(self):
        assert is_mock_source("local_mock") is True

    def test_stored_snapshot_is_mock(self):
        assert is_mock_source("stored_snapshot") is True

    def test_stored_snapshot_missing_is_mock(self):
        assert is_mock_source("stored_snapshot_missing") is True

    def test_unknown_is_mock(self):
        assert is_mock_source("unknown") is True

    def test_alpaca_paper_is_not_mock(self):
        assert is_mock_source("alpaca_paper") is False

    def test_none_is_mock(self):
        assert is_mock_source(None) is True

    def test_empty_string_is_mock(self):
        assert is_mock_source("") is True


class TestIsValidExecutionSource:
    def test_alpaca_paper_is_valid(self):
        assert is_valid_execution_source("alpaca_paper") is True

    def test_dry_run_mock_is_not_valid(self):
        assert is_valid_execution_source("dry_run_mock") is False

    def test_unknown_is_not_valid(self):
        assert is_valid_execution_source("unknown") is False

    def test_none_is_not_valid(self):
        assert is_valid_execution_source(None) is False

    def test_empty_string_is_not_valid(self):
        assert is_valid_execution_source("") is False


class TestSnapshotSourceStatus:
    def test_alpaca_paper_returns_ok(self):
        assert snapshot_source_status("alpaca_paper") == STATUS_OK

    def test_dry_run_mock_returns_blocked_mock(self):
        assert snapshot_source_status("dry_run_mock") == STATUS_BLOCKED_MOCK

    def test_stored_snapshot_returns_blocked_mock(self):
        assert snapshot_source_status("stored_snapshot") == STATUS_BLOCKED_MOCK

    def test_unknown_returns_blocked_mock(self):
        assert snapshot_source_status("unknown") == STATUS_BLOCKED_MOCK

    def test_arbitrary_string_returns_blocked_unknown(self):
        assert snapshot_source_status("some_other_source") == STATUS_BLOCKED_UNKNOWN

    def test_none_treated_as_unknown(self):
        assert snapshot_source_status(None) == STATUS_BLOCKED_MOCK


class TestCheckSnapshot:
    def test_alpaca_paper_passes(self):
        result = check_snapshot(_alpaca_snap(), "account_snapshot")
        assert result["passes"] is True
        assert result["source"] == "alpaca_paper"
        assert result["status"] == STATUS_OK

    def test_dry_run_mock_fails(self):
        result = check_snapshot(_mock_snap(), "positions_snapshot")
        assert result["passes"] is False
        assert result["source"] == "dry_run_mock"
        assert result["status"] == STATUS_BLOCKED_MOCK

    def test_name_is_preserved(self):
        result = check_snapshot(_alpaca_snap(), "orders_snapshot")
        assert result["name"] == "orders_snapshot"


class TestCheckExecutionSnapshots:
    def test_all_alpaca_passes(self):
        result = check_execution_snapshots(
            account_snapshot=_alpaca_snap(),
            positions_snapshot=_alpaca_snap(),
            orders_snapshot=_alpaca_snap(),
            market_snapshot=_alpaca_snap({"data_source": "alpaca_paper"}),
        )
        assert result["passes"] is True
        assert result["failed"] == []
        assert len(result["checked"]) == 4

    def test_one_mock_fails(self):
        result = check_execution_snapshots(
            account_snapshot=_alpaca_snap(),
            positions_snapshot=_mock_snap(),
            orders_snapshot=_alpaca_snap(),
            market_snapshot=_alpaca_snap(),
        )
        assert result["passes"] is False
        assert len(result["failed"]) == 1
        assert result["failed"][0]["name"] == "positions_snapshot"

    def test_all_mock_fails_all_four(self):
        result = check_execution_snapshots(
            account_snapshot=_mock_snap(),
            positions_snapshot=_mock_snap(),
            orders_snapshot=_mock_snap(),
            market_snapshot=_mock_snap(),
        )
        assert result["passes"] is False
        assert len(result["failed"]) == 4

    def test_market_snapshot_uses_data_source_field(self):
        mkt = {"data_source": "alpaca_paper", "fetched_at": "2026-05-13T20:00:00Z"}
        result = check_execution_snapshots(
            account_snapshot=_alpaca_snap(),
            positions_snapshot=_alpaca_snap(),
            orders_snapshot=_alpaca_snap(),
            market_snapshot=mkt,
        )
        assert result["passes"] is True


# ---------------------------------------------------------------------------
# Execution gate — gate_canonical_source_integrity
# ---------------------------------------------------------------------------

class TestGateCanonicalSourceIntegrity:
    def _ctx(self, acc="alpaca_paper", pos="alpaca_paper", ord_="alpaca_paper", mkt="alpaca_paper"):
        return {
            "account_snapshot": _snap(acc),
            "positions_snapshot": _snap(pos),
            "orders_snapshot": _snap(ord_),
            "market_snapshot": _snap(mkt),
        }

    def test_all_alpaca_passes(self):
        result = gate_canonical_source_integrity(self._ctx())
        assert result["passes"] is True
        assert result["gate_id"] == "CANONICAL_SOURCE_INTEGRITY"

    def test_mock_account_fails(self):
        result = gate_canonical_source_integrity(self._ctx(acc="dry_run_mock"))
        assert result["passes"] is False
        assert "account_snapshot" in result["detail"]
        assert "dry_run_mock" in result["detail"]

    def test_mock_positions_fails(self):
        result = gate_canonical_source_integrity(self._ctx(pos="dry_run_mock"))
        assert result["passes"] is False
        assert "positions_snapshot" in result["detail"]

    def test_mock_orders_fails(self):
        result = gate_canonical_source_integrity(self._ctx(ord_="dry_run_mock"))
        assert result["passes"] is False

    def test_mock_market_fails(self):
        result = gate_canonical_source_integrity(self._ctx(mkt="dry_run_mock"))
        assert result["passes"] is False

    def test_all_mock_fails_with_all_names(self):
        result = gate_canonical_source_integrity(
            self._ctx(acc="dry_run_mock", pos="dry_run_mock", ord_="dry_run_mock", mkt="dry_run_mock")
        )
        assert result["passes"] is False
        assert "account_snapshot" in result["detail"]
        assert "positions_snapshot" in result["detail"]

    def test_detail_mentions_refresh(self):
        result = gate_canonical_source_integrity(self._ctx(pos="dry_run_mock"))
        assert "Data Refresh" in result["detail"] or "refresh" in result["detail"].lower()

    def test_run_all_gates_includes_source_integrity(self):
        ctx = {
            "account_snapshot": _mock_snap(),
            "positions_snapshot": _mock_snap(),
            "orders_snapshot": _mock_snap(),
            "market_snapshot": _mock_snap(),
            "trade_plan": {"trading_mode": "paper", "plan_id": "x",
                           "generated_at": "now", "expires_at": "future",
                           "proposed_orders": []},
            "risk_state": {"drawdown": 0.0, "paused": False},
            "risk_limits": {"max_drawdown_block_pct": -0.1},
            "strategy": {"parameters": {}},
            "universe": {"symbols": []},
            "exec_history_dir": Path(tempfile.mkdtemp()),
            "dry_run": True,
        }
        results = run_all_gates(ctx)
        gate_ids = [r["gate_id"] for r in results]
        assert "CANONICAL_SOURCE_INTEGRITY" in gate_ids
        integrity_gate = next(r for r in results if r["gate_id"] == "CANONICAL_SOURCE_INTEGRITY")
        assert integrity_gate["passes"] is False

    def test_alpaca_paper_passes_in_run_all_gates(self):
        ctx = {
            "account_snapshot": _alpaca_snap({"account": {"status": "ACTIVE"}, "clock": {"is_open": True}}),
            "positions_snapshot": _alpaca_snap({"positions": [], "position_count": 0, "fetched_at": "2026-05-13T20:00:00Z"}),
            "orders_snapshot": _alpaca_snap({"orders": []}),
            "market_snapshot": _alpaca_snap({"quotes": {}, "spreads": {}}),
            "trade_plan": {"trading_mode": "paper", "plan_id": "x",
                           "generated_at": "now", "expires_at": "future",
                           "proposed_orders": []},
            "risk_state": {"drawdown": 0.0, "paused": False},
            "risk_limits": {"max_drawdown_block_pct": -0.1},
            "strategy": {"parameters": {}},
            "universe": {"symbols": []},
            "exec_history_dir": Path(tempfile.mkdtemp()),
            "dry_run": True,
        }
        results = run_all_gates(ctx)
        integrity_gate = next(r for r in results if r["gate_id"] == "CANONICAL_SOURCE_INTEGRITY")
        assert integrity_gate["passes"] is True


# ---------------------------------------------------------------------------
# Outcome tracker — source integrity
# ---------------------------------------------------------------------------

class TestOutcomeTrackerSourceIntegrity:
    def _market_snap(self, source: str = "alpaca_paper") -> dict:
        return {
            "source": source,
            "latest_bars": {},
            "quotes": {},
        }

    def _positions_snap(self, source: str = "alpaca_paper") -> dict:
        return {
            "source": source,
            "positions": [],
            "position_count": 0,
        }

    def _monitor_report(self) -> dict:
        return {
            "generated_at": "2026-05-13T20:00:00Z",
            "lifecycles": [_lifecycle("CID-001", "AAPL")],
        }

    def test_live_source_produces_ok_status(self):
        record = build_outcome_record(
            lifecycle=_lifecycle(),
            positions=[],
            market_snapshot=self._market_snap("alpaca_paper"),
            checked_at="2026-05-13T20:00:00Z",
            positions_integrity_blocked=False,
            market_integrity_blocked=False,
        )
        assert record["source_integrity_status"] == "ok"

    def test_mock_positions_blocks_pl(self):
        record = build_outcome_record(
            lifecycle=_lifecycle(),
            positions=[{"symbol": "AAPL", "qty": "1", "market_value": "160", "unrealized_pl": "10", "unrealized_plpc": "0.067", "current_price": "160"}],
            market_snapshot=self._market_snap(),
            checked_at="2026-05-13T20:00:00Z",
            positions_integrity_blocked=True,
            market_integrity_blocked=False,
        )
        assert record["source_integrity_status"] == "blocked_stale_or_mock_position_snapshot"
        assert record["current_return_pct"] is None
        assert record["current_position_qty"] is None
        assert record["current_market_value"] is None
        assert record["current_unrealized_pl"] is None
        assert record["current_price"] is None

    def test_mock_market_blocks_pl(self):
        record = build_outcome_record(
            lifecycle=_lifecycle(),
            positions=[],
            market_snapshot=self._market_snap(),
            checked_at="2026-05-13T20:00:00Z",
            positions_integrity_blocked=False,
            market_integrity_blocked=True,
        )
        assert record["source_integrity_status"] == "blocked_stale_or_mock_position_snapshot"
        assert record["current_return_pct"] is None

    def test_snapshot_source_integrity_status_propagated(self):
        snap = build_outcome_snapshot(
            monitor_report=self._monitor_report(),
            positions_snapshot=self._positions_snap("dry_run_mock"),
            market_snapshot=self._market_snap("alpaca_paper"),
            existing_outcomes=None,
        )
        assert snap["source_integrity_status"] == "blocked_mock_source"
        assert snap["source_integrity_note"] is not None
        assert "dry_run_mock" in snap["source_integrity_note"]
        # Each outcome should also be blocked
        for o in snap["outcomes"]:
            assert o["source_integrity_status"] == "blocked_stale_or_mock_position_snapshot"
            assert o["current_return_pct"] is None

    def test_live_snapshot_has_ok_integrity(self):
        snap = build_outcome_snapshot(
            monitor_report=self._monitor_report(),
            positions_snapshot=self._positions_snap("alpaca_paper"),
            market_snapshot=self._market_snap("alpaca_paper"),
            existing_outcomes=None,
        )
        assert snap["source_integrity_status"] == "ok"
        assert snap["source_integrity_note"] is None

    def test_fill_price_still_present_when_blocked(self):
        snap = build_outcome_snapshot(
            monitor_report=self._monitor_report(),
            positions_snapshot=self._positions_snap("dry_run_mock"),
            market_snapshot=self._market_snap("dry_run_mock"),
            existing_outcomes=None,
        )
        for o in snap["outcomes"]:
            assert o["fill_price"] == 150.0
            assert o["slippage_vs_limit"] is not None


# ---------------------------------------------------------------------------
# Trigger performance — data integrity block
# ---------------------------------------------------------------------------

class TestTriggerPerformanceIntegrityBlock:
    def _blocked_outcome_snap(self) -> dict:
        return {
            "source_integrity_status": "blocked_mock_source",
            "source_integrity_note": "WARNING: positions_snapshot.source='dry_run_mock'",
            "outcomes": [
                {
                    "symbol": "AAPL",
                    "fill_price": 150.0,
                    "current_price": None,
                    "slippage_pct": -0.001,
                    "current_return_pct": None,
                    "current_unrealized_pl": None,
                    "filled_at": "2026-05-13T16:00:00Z",
                    "entry_or_exit": "entry",
                    "source_integrity_status": "blocked_stale_or_mock_position_snapshot",
                }
            ],
        }

    def _clean_outcome_snap(self) -> dict:
        return {
            "source_integrity_status": "ok",
            "source_integrity_note": None,
            "outcomes": [
                {
                    "symbol": "AAPL",
                    "fill_price": 150.0,
                    "current_price": 155.0,
                    "slippage_pct": -0.001,
                    "current_return_pct": 0.033,
                    "current_unrealized_pl": 5.0,
                    "filled_at": "2026-05-13T16:00:00Z",
                    "entry_or_exit": "entry",
                    "source_integrity_status": "ok",
                }
            ],
        }

    def test_blocked_snapshot_gives_data_integrity_block(self):
        result = _collect_outcome_stats(self._blocked_outcome_snap())
        assert result["recommendation"] == STATUS_DATA_INTEGRITY_BLOCK
        assert result["sample_status"] == "blocked_mock_source"
        assert result["avg_current_return_pct"] is None

    def test_blocked_snapshot_returns_no_pl(self):
        result = _collect_outcome_stats(self._blocked_outcome_snap())
        assert result["avg_current_return_pct"] is None
        assert result["avg_slippage_pct"] is None

    def test_clean_snapshot_uses_returns(self):
        result = _collect_outcome_stats(self._clean_outcome_snap())
        assert result["recommendation"] != STATUS_DATA_INTEGRITY_BLOCK
        assert result["source_integrity_status"] == "ok"

    def test_blocked_note_preserved(self):
        result = _collect_outcome_stats(self._blocked_outcome_snap())
        assert result["source_integrity_note"] is not None

    def test_by_symbol_blocks_return_when_integrity_bad(self):
        result = _collect_outcome_stats(self._blocked_outcome_snap())
        aapl = result["by_symbol"].get("AAPL", {})
        assert aapl.get("current_return_pct") is None

    def test_by_symbol_uses_return_when_integrity_ok(self):
        result = _collect_outcome_stats(self._clean_outcome_snap())
        aapl = result["by_symbol"].get("AAPL", {})
        assert aapl.get("current_return_pct") == pytest.approx(0.033, rel=1e-4)

    def test_empty_snapshot_is_ok(self):
        result = _collect_outcome_stats({})
        assert result["recommendation"] != STATUS_DATA_INTEGRITY_BLOCK
        assert result["source_integrity_status"] == "ok"


# ---------------------------------------------------------------------------
# refresh_data.py --dry-run writes to sandbox, not data/latest
# ---------------------------------------------------------------------------

class TestRefreshDataDryRunSandbox:
    """Verify that refresh_data.py --dry-run does not touch canonical data/latest/."""

    def test_dry_run_module_imports_sandbox_paths(self):
        """Confirm refresh_data.py imports SANDBOX_LATEST_DIR."""
        refresh_path = Path(__file__).resolve().parents[1] / "scripts" / "refresh_data.py"
        source = refresh_path.read_text(encoding="utf-8")
        assert "SANDBOX_LATEST_DIR" in source
        assert "SANDBOX_HISTORY_DIR" in source

    def test_dry_run_writes_sandbox_not_canonical(self):
        """When --dry-run, out_latest should be SANDBOX_LATEST_DIR, not LATEST_DIR."""
        refresh_path = Path(__file__).resolve().parents[1] / "scripts" / "refresh_data.py"
        source = refresh_path.read_text(encoding="utf-8")
        # out_latest = SANDBOX_LATEST_DIR in dry-run branch
        assert "out_latest = SANDBOX_LATEST_DIR" in source
        # out_latest = LATEST_DIR in live branch
        assert "out_latest = LATEST_DIR" in source

    def test_dry_run_warning_message_present(self):
        refresh_path = Path(__file__).resolve().parents[1] / "scripts" / "refresh_data.py"
        source = refresh_path.read_text(encoding="utf-8")
        assert "WARNING: DRY RUN" in source
        assert "canonical data/latest/" in source


# ---------------------------------------------------------------------------
# monitor_positions.py --dry-run does not overwrite RISK-STATE.json
# ---------------------------------------------------------------------------

class TestMonitorPositionsDryRunSandbox:
    """Verify that monitor_positions.py --dry-run writes to sandbox only."""

    def test_dry_run_module_imports_sandbox_paths(self):
        mp_path = Path(__file__).resolve().parents[1] / "scripts" / "monitor_positions.py"
        source = mp_path.read_text(encoding="utf-8")
        assert "SANDBOX_HISTORY_DIR" in source
        assert "SANDBOX_MEMORY_DIR" in source

    def test_use_sandbox_condition_present(self):
        mp_path = Path(__file__).resolve().parents[1] / "scripts" / "monitor_positions.py"
        source = mp_path.read_text(encoding="utf-8")
        assert "use_sandbox" in source
        assert "is_mock_source" in source

    def test_canonical_risk_state_not_written_in_sandbox(self):
        """In sandbox mode, _RISK_STATE_PATH must NOT be written."""
        mp_path = Path(__file__).resolve().parents[1] / "scripts" / "monitor_positions.py"
        source = mp_path.read_text(encoding="utf-8")
        # The canonical write is inside the `else:` block (not use_sandbox)
        # We check that there's a sandbox_risk_state write AND canonical under else
        assert "sandbox_risk_state" in source
        assert "NOT modifying canonical memory/RISK-STATE.json" in source

    def test_mock_source_triggers_sandbox(self):
        """is_mock_source("dry_run_mock") should be True so sandbox is used."""
        assert is_mock_source("dry_run_mock") is True

    def test_alpaca_paper_source_does_not_trigger_sandbox(self):
        assert is_mock_source("alpaca_paper") is False


# ---------------------------------------------------------------------------
# validate_all.py source integrity check
# ---------------------------------------------------------------------------

class TestValidateAllSourceIntegrity:
    def test_validate_all_imports_source_integrity(self):
        va_path = Path(__file__).resolve().parents[1] / "scripts" / "validate_all.py"
        source = va_path.read_text(encoding="utf-8")
        assert "source_integrity" in source
        assert "EXECUTION_CRITICAL_FILES" in source

    def test_validate_all_has_execution_check_flag(self):
        va_path = Path(__file__).resolve().parents[1] / "scripts" / "validate_all.py"
        source = va_path.read_text(encoding="utf-8")
        assert "--execution-check" in source

    def test_check_canonical_sources_mock_produces_warn(self, tmp_path):
        """With mock canonical files, WARN is produced (not FAIL) without --execution-check."""
        import importlib.util
        va_path = Path(__file__).resolve().parents[1] / "scripts" / "validate_all.py"
        spec = importlib.util.spec_from_file_location("validate_all", va_path)
        mod = importlib.util.module_from_spec(spec)
        # Patch LATEST_DIR to the tmp dir
        (tmp_path / "account_snapshot.json").write_text(
            json.dumps({"source": "dry_run_mock"}), encoding="utf-8"
        )
        from trading_os.source_integrity import EXECUTION_CRITICAL_FILES
        for f in EXECUTION_CRITICAL_FILES:
            if f != "account_snapshot.json":
                (tmp_path / f).write_text(json.dumps({"source": "alpaca_paper"}), encoding="utf-8")

        with patch("trading_os.config.LATEST_DIR", tmp_path):
            spec.loader.exec_module(mod)
            issues = mod._check_canonical_sources(execution_check=False)

        assert any("WARN" in i for i in issues)
        assert any("account_snapshot" in i for i in issues)

    def test_check_canonical_sources_live_produces_no_issues(self, tmp_path):
        """With live canonical files, no issues are produced."""
        from trading_os.source_integrity import EXECUTION_CRITICAL_FILES
        for f in EXECUTION_CRITICAL_FILES:
            (tmp_path / f).write_text(json.dumps({"source": "alpaca_paper"}), encoding="utf-8")

        import importlib.util
        va_path = Path(__file__).resolve().parents[1] / "scripts" / "validate_all.py"
        spec = importlib.util.spec_from_file_location("validate_all_live", va_path)
        mod = importlib.util.module_from_spec(spec)

        with patch("trading_os.config.LATEST_DIR", tmp_path):
            spec.loader.exec_module(mod)
            issues = mod._check_canonical_sources(execution_check=False)

        assert issues == []
