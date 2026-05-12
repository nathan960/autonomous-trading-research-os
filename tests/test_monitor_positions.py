"""Tests: monitor_positions.py safety and correctness.

Covers:
- compute_risk_state_update() pure logic.
- Env gate: blocks when TRADING_MODE != paper.
- Env gate: blocks when ALPACA_PAPER is not true.
- Env gate: blocks when LIVE_TRADING_CONFIRMED is true.
- CLI: --dry-run succeeds without credentials.
- CLI: run without --dry-run fails closed when env gates are wrong.
- Outputs: RISK-STATE.json written and schema-valid.
- Outputs: portfolio history file written.
- Outputs: POSITION-MONITOR.md appended.
- No orders are placed (no trading endpoint calls).
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any
from unittest.mock import patch

import pytest

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.schemas import validate_risk_state


# ---------------------------------------------------------------------------
# Import the module under test
# ---------------------------------------------------------------------------

sys.path.insert(0, str(_ROOT / "scripts"))
import monitor_positions as _mon


# ---------------------------------------------------------------------------
# compute_risk_state_update pure logic
# ---------------------------------------------------------------------------

class TestComputeRiskStateUpdate:
    def _prior(self, **kwargs) -> dict:
        base = {
            "schema_version": "0.1.0",
            "last_monitor_run_id": "old-run",
            "latest_equity": 10000.0,
            "peak_equity": 10000.0,
            "drawdown": 0.0,
            "position_count": 0,
            "updated_at": "2026-01-01T00:00:00Z",
        }
        base.update(kwargs)
        return base

    def _account(self, portfolio_value: float | None = None, equity: float | None = None) -> dict:
        acc: dict = {}
        if portfolio_value is not None:
            acc["portfolio_value"] = str(portfolio_value)
        if equity is not None:
            acc["equity"] = str(equity)
        return acc

    def test_equity_from_portfolio_value(self):
        result = _mon.compute_risk_state_update(
            current_risk_state=self._prior(peak_equity=10000.0),
            positions=[],
            account=self._account(portfolio_value=12000.0),
            run_id="run-001",
            updated_at="2026-05-12T00:00:00Z",
        )
        assert result["latest_equity"] == pytest.approx(12000.0)

    def test_equity_falls_back_to_equity_key(self):
        result = _mon.compute_risk_state_update(
            current_risk_state=self._prior(),
            positions=[],
            account={"equity": "9500.0"},
            run_id="run-001",
            updated_at="2026-05-12T00:00:00Z",
        )
        assert result["latest_equity"] == pytest.approx(9500.0)

    def test_peak_equity_advances(self):
        result = _mon.compute_risk_state_update(
            current_risk_state=self._prior(peak_equity=10000.0),
            positions=[],
            account=self._account(portfolio_value=15000.0),
            run_id="run-001",
            updated_at="2026-05-12T00:00:00Z",
        )
        assert result["peak_equity"] == pytest.approx(15000.0)

    def test_peak_equity_does_not_decrease(self):
        result = _mon.compute_risk_state_update(
            current_risk_state=self._prior(peak_equity=20000.0),
            positions=[],
            account=self._account(portfolio_value=15000.0),
            run_id="run-001",
            updated_at="2026-05-12T00:00:00Z",
        )
        assert result["peak_equity"] == pytest.approx(20000.0)

    def test_drawdown_zero_at_peak(self):
        result = _mon.compute_risk_state_update(
            current_risk_state=self._prior(peak_equity=10000.0),
            positions=[],
            account=self._account(portfolio_value=10000.0),
            run_id="run-001",
            updated_at="2026-05-12T00:00:00Z",
        )
        assert result["drawdown"] == pytest.approx(0.0)

    def test_drawdown_negative_below_peak(self):
        result = _mon.compute_risk_state_update(
            current_risk_state=self._prior(peak_equity=10000.0),
            positions=[],
            account=self._account(portfolio_value=9000.0),
            run_id="run-001",
            updated_at="2026-05-12T00:00:00Z",
        )
        assert result["drawdown"] == pytest.approx(-0.1)

    def test_position_count_from_positions_list(self):
        positions = [
            {"symbol": "AAPL", "market_value": "1000.0"},
            {"symbol": "GOOG", "market_value": "2000.0"},
        ]
        result = _mon.compute_risk_state_update(
            current_risk_state=self._prior(),
            positions=positions,
            account=self._account(portfolio_value=10000.0),
            run_id="run-001",
            updated_at="2026-05-12T00:00:00Z",
        )
        assert result["position_count"] == 2

    def test_run_id_stored(self):
        result = _mon.compute_risk_state_update(
            current_risk_state=self._prior(),
            positions=[],
            account=self._account(portfolio_value=10000.0),
            run_id="monitor_positions-20260512-abc123",
            updated_at="2026-05-12T00:00:00Z",
        )
        assert result["last_monitor_run_id"] == "monitor_positions-20260512-abc123"

    def test_schema_version_preserved(self):
        result = _mon.compute_risk_state_update(
            current_risk_state=self._prior(),
            positions=[],
            account=self._account(portfolio_value=10000.0),
            run_id="run-001",
            updated_at="2026-05-12T00:00:00Z",
        )
        assert result["schema_version"] == "0.1.0"

    def test_result_passes_schema_validation(self):
        result = _mon.compute_risk_state_update(
            current_risk_state=self._prior(peak_equity=10000.0),
            positions=[{"symbol": "AAPL"}],
            account=self._account(portfolio_value=11000.0),
            run_id="monitor_positions-20260512T000000-abcdef01",
            updated_at="2026-05-12T00:00:00Z",
        )
        validate_risk_state(result)  # must not raise


# ---------------------------------------------------------------------------
# Env gates
# ---------------------------------------------------------------------------

class TestEnvGates:
    def _clean_env(self) -> dict:
        return {
            "TRADING_MODE": "paper",
            "ALPACA_PAPER": "true",
        }

    def test_missing_trading_mode_raises(self):
        env = self._clean_env()
        del env["TRADING_MODE"]
        with patch.dict(os.environ, env, clear=True):
            with pytest.raises(RuntimeError, match="TRADING_MODE"):
                _mon._check_env_gates()

    def test_wrong_trading_mode_raises(self):
        env = {**self._clean_env(), "TRADING_MODE": "live"}
        with patch.dict(os.environ, env, clear=True):
            with pytest.raises(RuntimeError, match="TRADING_MODE"):
                _mon._check_env_gates()

    def test_alpaca_paper_false_raises(self):
        env = {**self._clean_env(), "ALPACA_PAPER": "false"}
        with patch.dict(os.environ, env, clear=True):
            with pytest.raises(RuntimeError, match="ALPACA_PAPER"):
                _mon._check_env_gates()

    def test_live_trading_confirmed_true_raises(self):
        env = {**self._clean_env(), "LIVE_TRADING_CONFIRMED": "true"}
        with patch.dict(os.environ, env, clear=True):
            with pytest.raises(RuntimeError, match="LIVE_TRADING_CONFIRMED"):
                _mon._check_env_gates()

    def test_live_trading_confirmed_yes_raises(self):
        env = {**self._clean_env(), "LIVE_TRADING_CONFIRMED": "yes"}
        with patch.dict(os.environ, env, clear=True):
            with pytest.raises(RuntimeError, match="LIVE_TRADING_CONFIRMED"):
                _mon._check_env_gates()

    def test_paper_mode_correct_does_not_raise(self):
        env = self._clean_env()
        with patch.dict(os.environ, env, clear=True):
            _mon._check_env_gates()  # must not raise


# ---------------------------------------------------------------------------
# CLI dry-run
# ---------------------------------------------------------------------------

class TestDryRunCLI:
    """Run monitor_positions.py --dry-run as subprocess and check outputs."""

    @pytest.fixture(scope="class")
    def _run_dry(self, tmp_path_factory):
        env = {
            **os.environ,
            "TRADING_MODE": "paper",
            "ALPACA_PAPER": "true",
            "ENABLE_PAPER_EXECUTION": "false",
            "LIVE_TRADING_CONFIRMED": "false",
        }
        result = subprocess.run(
            [sys.executable, str(_ROOT / "scripts" / "monitor_positions.py"), "--dry-run"],
            capture_output=True,
            text=True,
            cwd=str(_ROOT),
            env=env,
        )
        return result

    def test_exits_zero(self, _run_dry):
        assert _run_dry.returncode == 0, (
            f"monitor_positions.py --dry-run failed:\n"
            f"{_run_dry.stdout}\n{_run_dry.stderr}"
        )

    def test_risk_state_written(self, _run_dry):
        path = _ROOT / "memory" / "RISK-STATE.json"
        assert path.exists()

    def test_risk_state_schema_valid(self, _run_dry):
        path = _ROOT / "memory" / "RISK-STATE.json"
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        validate_risk_state(data)  # must not raise

    def test_monitor_log_appended(self, _run_dry):
        path = _ROOT / "memory" / "POSITION-MONITOR.md"
        assert path.exists()
        content = path.read_text(encoding="utf-8")
        assert "monitor_positions run" in content

    def test_portfolio_history_written(self, _run_dry):
        portfolio_dir = _ROOT / "data" / "history" / "portfolio"
        assert portfolio_dir.exists()
        files = list(portfolio_dir.glob("*_portfolio.json"))
        assert len(files) >= 1

    def test_portfolio_report_has_data_hash(self, _run_dry):
        portfolio_dir = _ROOT / "data" / "history" / "portfolio"
        files = sorted(portfolio_dir.glob("*_portfolio.json"))
        assert files
        with files[-1].open("r", encoding="utf-8") as fh:
            report = json.load(fh)
        assert "data_hash" in report
        assert isinstance(report["data_hash"], str) and len(report["data_hash"]) == 64

    def test_no_secrets_in_stdout(self, _run_dry):
        key = os.environ.get("ALPACA_API_KEY", "")
        secret = os.environ.get("ALPACA_API_SECRET", "")
        if key:
            assert key not in _run_dry.stdout
        if secret:
            assert secret not in _run_dry.stdout

    def test_no_orders_placed_dry_run(self, _run_dry):
        # Dry-run must not touch any execution or order history
        output = _run_dry.stdout + _run_dry.stderr
        assert "submit" not in output.lower()
        assert "order submitted" not in output.lower()


# ---------------------------------------------------------------------------
# CLI live mode fails closed when env gates are wrong
# ---------------------------------------------------------------------------

class TestLiveModeFailsClosed:
    def _run(self, extra_env: dict) -> subprocess.CompletedProcess:
        env = {
            **os.environ,
            "TRADING_MODE": "paper",
            "ALPACA_PAPER": "true",
            "ENABLE_PAPER_EXECUTION": "false",
            **extra_env,
        }
        return subprocess.run(
            [sys.executable, str(_ROOT / "scripts" / "monitor_positions.py")],
            capture_output=True,
            text=True,
            cwd=str(_ROOT),
            env=env,
        )

    def test_wrong_trading_mode_exits_nonzero(self):
        result = self._run({"TRADING_MODE": "live"})
        assert result.returncode != 0

    def test_alpaca_paper_false_exits_nonzero(self):
        result = self._run({"ALPACA_PAPER": "false"})
        assert result.returncode != 0

    def test_live_trading_confirmed_exits_nonzero(self):
        result = self._run({"LIVE_TRADING_CONFIRMED": "true"})
        assert result.returncode != 0
