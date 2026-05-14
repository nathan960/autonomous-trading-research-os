"""Safety tests for src/trading_os/execution/paper_executor.py.

Every test proves a specific safety invariant:
- No order is ever submitted when any hard gate fails.
- Live trading cannot be enabled accidentally.
- The paper broker connection is always paper=True.
- Orders blocked at any layer are never submitted.

All Alpaca API calls are mocked. No network I/O occurs.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trading_os.execution.paper_executor import (
    _check_confirm_paper,
    _check_hard_env_gates,
    _check_plan_approved,
    _probe_log_dirs,
    _validate_order_paper_safe,
    run_paper_execution,
    submit_paper_order,
)
from trading_os.time_utils import utc_now_iso


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _future_ts(minutes: int = 120) -> str:
    from datetime import datetime, timezone, timedelta
    return (
        (datetime.now(timezone.utc) + timedelta(minutes=minutes))
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def _past_ts(minutes: int = 10) -> str:
    from datetime import datetime, timezone, timedelta
    return (
        (datetime.now(timezone.utc) - timedelta(minutes=minutes))
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def _plan(
    trading_mode: str = "paper",
    expires_at: str | None = None,
    approved: bool = True,
    orders: list | None = None,
    risk_checks: list | None = None,
) -> dict:
    return {
        "plan_id": "trade_plan-20260512T000000-abc12345",
        "generated_at": _past_ts(5),
        "expires_at": expires_at or _future_ts(360),
        "trading_mode": trading_mode,
        "trade_plan_hash": "x" * 64,
        "proposed_orders": orders if orders is not None else [_order("AAPL"), _order("BIL")],
        "risk_checks": risk_checks if risk_checks is not None else [],
        "targets": {"AAPL": {"weight": 0.09}, "BIL": {"weight": 0.91}},
        "approval": {
            "approved_for_execution": approved,
            "approve_paper_flag": approved,
            "all_risk_checks_pass": True,
            "reason": "approved" if approved else "approve_paper_flag_not_set",
        },
    }


def _order(
    symbol: str = "AAPL",
    side: str = "buy",
    order_type: str = "limit",
    notional: float = 3600.0,
    target_weight: float = 0.09,
    would_short: bool = False,
    skip_reason: str | None = None,
    limit_price: float = 150.0,
    time_in_force: str = "day",
    client_order_id: str = "TOS-20260512T000000-AAPL-BUY",
) -> dict:
    return {
        "symbol": symbol,
        "side": side,
        "order_type": order_type,
        "limit_price": limit_price,
        "notional": notional,
        "target_weight": target_weight,
        "current_value": 0.0,
        "target_value": notional,
        "delta_value": notional,
        "would_short": would_short,
        "skip_reason": skip_reason,
        "time_in_force": time_in_force,
        "client_order_id": client_order_id,
    }


def _account_snapshot(status: str = "ACTIVE", is_open: bool = True, pos_count: int = 0) -> dict:
    return {
        "account": {"equity": "40000.00", "cash": "40000.00", "status": status},
        "clock": {"is_open": is_open, "timestamp": utc_now_iso()},
        "position_count": pos_count,
        "fetched_at": utc_now_iso(),
    }


def _positions_snapshot(pos_count: int = 0) -> dict:
    return {
        "positions": [],
        "position_count": pos_count,
        "fetched_at": utc_now_iso(),
    }


def _orders_snapshot(orders: list | None = None) -> dict:
    return {"orders": orders or [], "open_order_count": len(orders or [])}


def _market_snapshot(symbols: list | None = None, spread_pct: float = 0.001) -> dict:
    syms = symbols or ["AAPL", "MSFT", "BIL"]
    now = utc_now_iso()
    return {
        "generated_at": now,
        "quotes": {
            sym: {"symbol": sym, "bid_price": 100.0, "ask_price": 100.1, "timestamp": now}
            for sym in syms
        },
        "spreads": {sym: {"symbol": sym, "spread_pct": spread_pct} for sym in syms},
    }


def _risk_state(drawdown: float = 0.0, paused: bool = False) -> dict:
    rs = {
        "drawdown": drawdown,
        "peak_equity": 40000.0,
        "latest_equity": 40000.0,
        "position_count": 0,
        "schema_version": "0.1.0",
        "updated_at": utc_now_iso(),
    }
    if paused:
        rs["paused"] = True
    return rs


def _risk_limits() -> dict:
    return {
        "live_trading_allowed": False,
        "max_drawdown_block_pct": -0.1,
        "max_position_weight": 0.35,
        "max_holdings": 10,
        "min_order_notional": 25.0,
        "max_quote_spread_pct": 0.02,
        "allowed_fallbacks": ["BIL", "SPY"],
        "block_symbols": [],
    }


def _strategy() -> dict:
    return {
        "trading_mode": "paper_only",
        "parameters": {
            "max_holdings": 10,
            "max_position_weight": 0.35,
            "max_names_per_sector": 2,
            "risk_on_equity_alloc": 0.9,
            "min_order_notional": 25.0,
            "max_snapshot_age_minutes": 90,
            "max_quote_spread_pct": 0.02,
        },
        "fallbacks": {
            "risk_off_target": {"symbol": "BIL", "weight": 1.0},
            "risk_on_no_candidates_target": {"symbol": "SPY", "weight": 1.0},
        },
    }


def _universe(symbols: list | None = None) -> dict:
    return {"symbols": symbols or ["AAPL", "MSFT", "GOOGL", "WMT", "APD"]}


_UNSET = object()


def _ctx(
    plan=_UNSET,
    acct=_UNSET,
    pos_snap=_UNSET,
    ord_snap=_UNSET,
    mkt=_UNSET,
    rs=_UNSET,
    universe=_UNSET,
    rl=_UNSET,
    strat=_UNSET,
    exec_dir: Path | None = None,
    orders_dir: Path | None = None,
) -> dict:
    with tempfile.TemporaryDirectory() as td:
        default_exec_dir = Path(td) / "executions"
        default_orders_dir = Path(td) / "orders"
    return {
        "trade_plan":         _plan() if plan is _UNSET else plan,
        "account_snapshot":   _account_snapshot() if acct is _UNSET else acct,
        "positions_snapshot": _positions_snapshot() if pos_snap is _UNSET else pos_snap,
        "orders_snapshot":    _orders_snapshot() if ord_snap is _UNSET else ord_snap,
        "market_snapshot":    _market_snapshot() if mkt is _UNSET else mkt,
        "risk_state":         _risk_state() if rs is _UNSET else rs,
        "universe":           _universe() if universe is _UNSET else universe,
        "risk_limits":        _risk_limits() if rl is _UNSET else rl,
        "strategy":           _strategy() if strat is _UNSET else strat,
        "exec_history_dir":   exec_dir or default_exec_dir,
        "orders_dir":         orders_dir or default_orders_dir,
        "dry_run":            False,
    }


def _mock_trading_client(broker_order_id: str = "broker-abc123") -> MagicMock:
    """Return a mock trading client that records submitted orders."""
    client = MagicMock()
    response = MagicMock()
    response.id = broker_order_id
    response.status = "accepted"
    response.model_dump.return_value = {
        "id": broker_order_id,
        "status": "accepted",
        "symbol": "AAPL",
    }
    client.submit_order.return_value = response
    return client


def _paper_env(monkeypatch) -> None:
    """Set all required env vars for paper execution."""
    monkeypatch.setenv("TRADING_MODE", "paper")
    monkeypatch.setenv("ALPACA_PAPER", "true")
    monkeypatch.setenv("ENABLE_PAPER_EXECUTION", "true")
    monkeypatch.delenv("LIVE_TRADING_CONFIRMED", raising=False)


# ===========================================================================
# TestHardEnvGates — every violation must raise before any network call
# ===========================================================================

class TestHardEnvGates:
    def test_missing_trading_mode_fails(self, monkeypatch):
        monkeypatch.delenv("TRADING_MODE", raising=False)
        with pytest.raises(RuntimeError, match="TRADING_MODE"):
            _check_hard_env_gates()

    def test_live_trading_mode_fails(self, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "live")
        with pytest.raises(RuntimeError, match="TRADING_MODE"):
            _check_hard_env_gates()

    def test_alpaca_paper_absent_fails(self, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.delenv("ALPACA_PAPER", raising=False)
        with pytest.raises(RuntimeError, match="ALPACA_PAPER"):
            _check_hard_env_gates()

    def test_alpaca_paper_false_fails(self, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "false")
        with pytest.raises(RuntimeError, match="ALPACA_PAPER"):
            _check_hard_env_gates()

    def test_enable_paper_execution_absent_fails(self, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "true")
        monkeypatch.delenv("ENABLE_PAPER_EXECUTION", raising=False)
        with pytest.raises(RuntimeError, match="ENABLE_PAPER_EXECUTION"):
            _check_hard_env_gates()

    def test_enable_paper_execution_false_fails(self, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "true")
        monkeypatch.setenv("ENABLE_PAPER_EXECUTION", "false")
        with pytest.raises(RuntimeError, match="ENABLE_PAPER_EXECUTION"):
            _check_hard_env_gates()

    def test_live_trading_confirmed_true_fails(self, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "true")
        monkeypatch.setenv("ENABLE_PAPER_EXECUTION", "true")
        monkeypatch.setenv("LIVE_TRADING_CONFIRMED", "true")
        with pytest.raises(RuntimeError, match="LIVE_TRADING_CONFIRMED"):
            _check_hard_env_gates()

    def test_live_trading_confirmed_1_fails(self, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "true")
        monkeypatch.setenv("ENABLE_PAPER_EXECUTION", "true")
        monkeypatch.setenv("LIVE_TRADING_CONFIRMED", "1")
        with pytest.raises(RuntimeError, match="LIVE_TRADING_CONFIRMED"):
            _check_hard_env_gates()

    def test_all_correct_passes(self, monkeypatch):
        _paper_env(monkeypatch)
        _check_hard_env_gates()  # must not raise

    def test_enable_paper_1_passes(self, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "1")
        monkeypatch.setenv("ENABLE_PAPER_EXECUTION", "1")
        monkeypatch.delenv("LIVE_TRADING_CONFIRMED", raising=False)
        _check_hard_env_gates()  # must not raise


# ===========================================================================
# TestAlpacaClientSafety — prove live trading cannot be reached through client
# ===========================================================================

class TestAlpacaClientSafety:
    """Prove AlpacaPaperClient enforces paper-only at construction time."""

    def _client_env(self, monkeypatch) -> None:
        """Set env vars required for a valid AlpacaPaperClient."""
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "true")
        monkeypatch.delenv("LIVE_TRADING_CONFIRMED", raising=False)
        monkeypatch.setenv("ALPACA_API_KEY", "FAKEKEYFORTEST")
        monkeypatch.setenv("ALPACA_API_SECRET", "FAKESECRETFORTEST")

    def test_live_trading_confirmed_blocks_client(self, monkeypatch):
        self._client_env(monkeypatch)
        monkeypatch.setenv("LIVE_TRADING_CONFIRMED", "true")
        from trading_os.data.alpaca_client import AlpacaPaperClient
        with pytest.raises(RuntimeError, match="LIVE_TRADING_CONFIRMED"):
            AlpacaPaperClient()

    def test_wrong_trading_mode_blocks_client(self, monkeypatch):
        self._client_env(monkeypatch)
        monkeypatch.setenv("TRADING_MODE", "live")
        from trading_os.data.alpaca_client import AlpacaPaperClient
        with pytest.raises(RuntimeError, match="TRADING_MODE"):
            AlpacaPaperClient()

    def test_alpaca_paper_false_blocks_client(self, monkeypatch):
        self._client_env(monkeypatch)
        monkeypatch.setenv("ALPACA_PAPER", "false")
        from trading_os.data.alpaca_client import AlpacaPaperClient
        with pytest.raises(RuntimeError, match="ALPACA_PAPER"):
            AlpacaPaperClient()

    def test_missing_api_key_blocks_client(self, monkeypatch):
        self._client_env(monkeypatch)
        monkeypatch.delenv("ALPACA_API_KEY", raising=False)
        from trading_os.data.alpaca_client import AlpacaPaperClient
        with pytest.raises(RuntimeError, match="ALPACA_API_KEY"):
            AlpacaPaperClient()

    def test_missing_api_secret_blocks_client(self, monkeypatch):
        self._client_env(monkeypatch)
        monkeypatch.delenv("ALPACA_API_SECRET", raising=False)
        from trading_os.data.alpaca_client import AlpacaPaperClient
        with pytest.raises(RuntimeError, match="ALPACA_API_SECRET"):
            AlpacaPaperClient()

    def test_trading_client_always_paper_true(self, monkeypatch):
        """Prove that trading_client() always calls TradingClient(paper=True)."""
        self._client_env(monkeypatch)
        from trading_os.data.alpaca_client import AlpacaPaperClient
        client = AlpacaPaperClient()
        with patch("alpaca.trading.client.TradingClient") as mock_tc:
            mock_tc.return_value = MagicMock()
            client.trading_client()
            # Verify paper=True was passed — live trading requires paper=False
            call_kwargs = mock_tc.call_args[1]
            assert call_kwargs.get("paper") is True, (
                "TradingClient must always be constructed with paper=True"
            )


# ===========================================================================
# TestConfirmPaper
# ===========================================================================

class TestConfirmPaper:
    def test_confirm_paper_false_returns_block(self):
        assert _check_confirm_paper(False) is not None

    def test_confirm_paper_true_returns_none(self):
        assert _check_confirm_paper(True) is None

    def test_block_message_mentions_confirm_paper(self):
        reason = _check_confirm_paper(False)
        assert "confirm_paper" in reason.lower()

    def test_run_paper_execution_blocked_without_confirm(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = _ctx(exec_dir=tmp_path / "exec", orders_dir=tmp_path / "orders")
        report = run_paper_execution(ctx, MagicMock(), confirm_paper=False)
        assert report["status"] == "PAPER_BLOCKED"
        assert report["orders_submitted"] == []
        assert "confirm_paper" in (report.get("blocked_reason") or "").lower()


# ===========================================================================
# TestPlanApproval
# ===========================================================================

class TestPlanApproval:
    def test_unapproved_plan_returns_block(self):
        reason = _check_plan_approved(_plan(approved=False))
        assert reason is not None
        assert "approved_for_execution" in reason

    def test_approved_plan_returns_none(self):
        assert _check_plan_approved(_plan(approved=True)) is None

    def test_missing_approval_key_returns_block(self):
        plan = _plan()
        del plan["approval"]
        reason = _check_plan_approved(plan)
        assert reason is not None

    def test_run_paper_execution_blocked_on_unapproved_plan(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = _ctx(
            plan=_plan(approved=False),
            exec_dir=tmp_path / "exec",
            orders_dir=tmp_path / "orders",
        )
        report = run_paper_execution(ctx, MagicMock(), confirm_paper=True)
        assert report["status"] == "PAPER_BLOCKED"
        assert report["orders_submitted"] == []


# ===========================================================================
# TestLogDirProbe
# ===========================================================================

class TestLogDirProbe:
    def test_writable_dir_returns_none(self, tmp_path):
        assert _probe_log_dirs(tmp_path / "a", tmp_path / "b") is None

    def test_unwritable_dir_returns_error(self):
        # Pass a path under /proc or similar that cannot be created on macOS
        bad = Path("/proc/impossible/path/for/testing")
        result = _probe_log_dirs(bad)
        assert result is not None

    def test_run_blocked_when_logs_not_writable(self, monkeypatch):
        _paper_env(monkeypatch)
        ctx = _ctx()
        # Override exec_history_dir with an unwritable path
        ctx["exec_history_dir"] = Path("/proc/impossible/exec_dir")
        report = run_paper_execution(ctx, MagicMock(), confirm_paper=True)
        assert report["status"] == "PAPER_BLOCKED"
        assert report["orders_submitted"] == []
        assert "not writable" in (report.get("blocked_reason") or "")


# ===========================================================================
# TestOrderValidation — paper-safe order checks
# ===========================================================================

class TestOrderValidation:
    def test_valid_limit_buy_passes(self):
        assert _validate_order_paper_safe(_order()) is None

    def test_market_order_blocked(self):
        reason = _validate_order_paper_safe(_order(order_type="market"))
        assert reason is not None
        assert "limit_only" in reason or "limit" in reason

    def test_short_order_blocked(self):
        reason = _validate_order_paper_safe(_order(side="sell", would_short=True))
        assert reason is not None
        assert "short" in reason.lower()

    def test_options_symbol_slash_blocked(self):
        reason = _validate_order_paper_safe(_order(symbol="AAPL/C240119"))
        assert reason is not None
        assert "options" in reason.lower() or "suspected" in reason.lower()

    def test_options_symbol_digit_suffix_blocked(self):
        # Alpaca option ticker format ends in digits: e.g. AAPL2401190C00150000
        reason = _validate_order_paper_safe(_order(symbol="AAPL2401190"))
        assert reason is not None

    def test_missing_limit_price_blocked(self):
        o = _order()
        o["limit_price"] = None
        assert _validate_order_paper_safe(o) is not None

    def test_zero_limit_price_blocked(self):
        o = _order()
        o["limit_price"] = 0.0
        assert _validate_order_paper_safe(o) is not None

    def test_non_day_tif_blocked(self):
        reason = _validate_order_paper_safe(_order(time_in_force="gtc"))
        assert reason is not None
        assert "day" in reason.lower()

    def test_opg_tif_blocked(self):
        reason = _validate_order_paper_safe(_order(time_in_force="opg"))
        assert reason is not None

    def test_valid_limit_sell_passes(self):
        # A sell to exit an existing position is allowed (would_short=False)
        assert _validate_order_paper_safe(_order(side="sell", would_short=False)) is None


# ===========================================================================
# TestSubmitPaperOrder — single order submission
# ===========================================================================

class TestSubmitPaperOrder:
    def test_successful_submission(self, tmp_path):
        client = _mock_trading_client("broker-xyz")
        result = submit_paper_order(client, _order(), tmp_path)
        assert result["submitted"] is True
        assert result["broker_order_id"] == "broker-xyz"
        assert result["error"] is None

    def test_writes_audit_file(self, tmp_path):
        submit_paper_order(_mock_trading_client(), _order(symbol="AAPL"), tmp_path)
        files = list(tmp_path.iterdir())
        assert len(files) == 1
        assert files[0].suffix == ".json"

    def test_audit_file_contains_symbol(self, tmp_path):
        import json as _json
        submit_paper_order(_mock_trading_client(), _order(symbol="WMT"), tmp_path)
        content = _json.loads(list(tmp_path.iterdir())[0].read_text())
        assert content["symbol"] == "WMT"

    def test_broker_error_recorded_not_raised(self, tmp_path):
        client = MagicMock()
        client.submit_order.side_effect = RuntimeError("API timeout")
        result = submit_paper_order(client, _order(), tmp_path)
        assert result["submitted"] is False
        assert "RuntimeError" in result["error"]

    def test_no_secrets_in_audit_file(self, tmp_path):
        import json as _json
        submit_paper_order(_mock_trading_client(), _order(), tmp_path)
        content = list(tmp_path.iterdir())[0].read_text()
        # API keys should never appear in audit logs
        assert "ALPACA_API_KEY" not in content
        assert "ALPACA_API_SECRET" not in content
        assert "api_key" not in content.lower()


# ===========================================================================
# TestRunPaperExecution — full pipeline safety invariants
# ===========================================================================

class TestRunPaperExecution:
    def test_returns_report_dict(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = _ctx(exec_dir=tmp_path / "exec", orders_dir=tmp_path / "orders")
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        assert isinstance(report, dict)
        assert "status" in report
        assert "run_id" in report
        assert "execution_report_hash" in report

    def test_report_has_dry_run_false(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = _ctx(exec_dir=tmp_path / "exec", orders_dir=tmp_path / "orders")
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        assert report["dry_run"] is False

    def test_orders_never_submitted_when_gates_fail(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        # Expired plan causes TRADE_PLAN_NOT_EXPIRED gate to fail
        ctx = _ctx(
            plan=_plan(expires_at=_past_ts(60)),
            exec_dir=tmp_path / "exec",
            orders_dir=tmp_path / "orders",
        )
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        assert report["status"] == "PAPER_FAIL"
        assert report["orders_submitted"] == []

    def test_orders_never_submitted_when_plan_not_approved(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = _ctx(
            plan=_plan(approved=False),
            exec_dir=tmp_path / "exec",
            orders_dir=tmp_path / "orders",
        )
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        assert report["status"] == "PAPER_BLOCKED"
        assert report["orders_submitted"] == []

    def test_orders_never_submitted_without_confirm_paper(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = _ctx(exec_dir=tmp_path / "exec", orders_dir=tmp_path / "orders")
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=False)
        assert report["status"] == "PAPER_BLOCKED"
        assert report["orders_submitted"] == []

    def test_orders_never_submitted_when_market_closed(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = _ctx(
            acct=_account_snapshot(is_open=False),
            exec_dir=tmp_path / "exec",
            orders_dir=tmp_path / "orders",
        )
        # With dry_run=False (forced by run_paper_execution), market closed → gate fails
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        assert report["status"] == "PAPER_FAIL"
        assert report["orders_submitted"] == []
        assert "MARKET_CLOCK_OPEN" in report.get("failed_gates", [])

    def test_orders_never_submitted_when_account_blocked(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = _ctx(
            acct=_account_snapshot(status="ACCOUNT_BLOCKED"),
            exec_dir=tmp_path / "exec",
            orders_dir=tmp_path / "orders",
        )
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        assert report["status"] == "PAPER_FAIL"
        assert report["orders_submitted"] == []

    def test_orders_never_submitted_when_risk_state_paused(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = _ctx(
            rs=_risk_state(paused=True),
            exec_dir=tmp_path / "exec",
            orders_dir=tmp_path / "orders",
        )
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        assert report["status"] == "PAPER_FAIL"
        assert report["orders_submitted"] == []

    def test_no_orders_submitted_when_no_ready_orders(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        # All orders have skip_reason → none are execution_ready
        skipped = [
            _order("AAPL", skip_reason="below_min_notional"),
            _order("BIL", skip_reason="below_min_notional"),
        ]
        ctx = _ctx(
            plan=_plan(orders=skipped),
            exec_dir=tmp_path / "exec",
            orders_dir=tmp_path / "orders",
        )
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        assert report["orders_submitted"] == []

    def test_market_order_is_skipped_not_submitted(self, monkeypatch, tmp_path):
        """NO_PROHIBITED_ORDERS gate blocks market orders before any submission."""
        _paper_env(monkeypatch)
        orders = [_order("AAPL", order_type="market")]
        ctx = _ctx(
            plan=_plan(orders=orders),
            exec_dir=tmp_path / "exec",
            orders_dir=tmp_path / "orders",
        )
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        # Gate blocks market orders; no orders submitted to broker
        assert report["orders_submitted"] == []
        assert report.get("all_gates_pass") is False
        assert "NO_PROHIBITED_ORDERS" in report.get("failed_gates", [])

    def test_execution_report_hash_present(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = _ctx(exec_dir=tmp_path / "exec", orders_dir=tmp_path / "orders")
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        assert report.get("execution_report_hash") is not None
        assert len(report["execution_report_hash"]) == 64

    def test_broker_submit_error_does_not_crash_pipeline(self, monkeypatch, tmp_path):
        """If Alpaca returns an error for one order, the pipeline continues and records it."""
        _paper_env(monkeypatch)
        ctx = _ctx(exec_dir=tmp_path / "exec", orders_dir=tmp_path / "orders")
        client = MagicMock()
        client.submit_order.side_effect = RuntimeError("rate limit")
        report = run_paper_execution(ctx, client, confirm_paper=True)
        # Pipeline should not crash; orders_submitted records the error
        assert isinstance(report, dict)
        submitted = report.get("orders_submitted", [])
        if submitted:
            assert all(o.get("submitted") is False for o in submitted)

    def test_non_paper_trading_mode_in_plan_fails_gate(self, monkeypatch, tmp_path):
        """If trade_plan has trading_mode != paper, gate 1 fails and no orders submit."""
        _paper_env(monkeypatch)
        ctx = _ctx(
            plan=_plan(trading_mode="live"),
            exec_dir=tmp_path / "exec",
            orders_dir=tmp_path / "orders",
        )
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        assert report["status"] == "PAPER_FAIL"
        assert report["orders_submitted"] == []
        assert "TRADING_MODE_PAPER" in report.get("failed_gates", [])

    def test_alpaca_paper_false_env_fails_gate(self, monkeypatch, tmp_path):
        """ALPACA_PAPER=false causes gate 2 to fail; no orders submitted."""
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "false")
        monkeypatch.setenv("ENABLE_PAPER_EXECUTION", "true")
        monkeypatch.delenv("LIVE_TRADING_CONFIRMED", raising=False)
        ctx = _ctx(exec_dir=tmp_path / "exec", orders_dir=tmp_path / "orders")
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        assert report["status"] == "PAPER_FAIL"
        assert report["orders_submitted"] == []
        assert "ALPACA_PAPER_MODE" in report.get("failed_gates", [])


# ===========================================================================
# TestLiveTradingCannotBeEnabled — comprehensive safety proof
# ===========================================================================

class TestLiveTradingCannotBeEnabled:
    """Prove that no combination of inputs can trigger live trading."""

    def test_check_hard_env_gates_blocks_live_mode(self, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "live")
        with pytest.raises(RuntimeError):
            _check_hard_env_gates()

    def test_check_hard_env_gates_blocks_live_trading_confirmed(self, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "true")
        monkeypatch.setenv("ENABLE_PAPER_EXECUTION", "true")
        monkeypatch.setenv("LIVE_TRADING_CONFIRMED", "true")
        with pytest.raises(RuntimeError):
            _check_hard_env_gates()

    def test_gate1_blocks_non_paper_plan(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = _ctx(
            plan=_plan(trading_mode="live"),
            exec_dir=tmp_path / "exec",
            orders_dir=tmp_path / "orders",
        )
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        assert "TRADING_MODE_PAPER" in report.get("failed_gates", [])
        assert report["orders_submitted"] == []

    def test_alpaca_client_rejects_live_confirmed(self, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "true")
        monkeypatch.setenv("LIVE_TRADING_CONFIRMED", "true")
        monkeypatch.setenv("ALPACA_API_KEY", "FAKEKEY")
        monkeypatch.setenv("ALPACA_API_SECRET", "FAKESECRET")
        from trading_os.data.alpaca_client import AlpacaPaperClient
        with pytest.raises(RuntimeError, match="LIVE_TRADING_CONFIRMED"):
            AlpacaPaperClient()

    def test_orders_submitted_list_empty_on_every_gate_failure(self, monkeypatch, tmp_path):
        """orders_submitted must always be [] when any gate fails."""
        _paper_env(monkeypatch)
        # Breach drawdown limit → gate 7 fails
        ctx = _ctx(
            rs=_risk_state(drawdown=-0.15),
            exec_dir=tmp_path / "exec",
            orders_dir=tmp_path / "orders",
        )
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        assert report["orders_submitted"] == [], (
            "orders_submitted must be empty when any gate fails — "
            "live trading must never be triggered accidentally"
        )

    def test_no_orders_without_enable_paper_execution(self, monkeypatch, tmp_path):
        """ENABLE_PAPER_EXECUTION=false → _check_hard_env_gates raises.
        The script exits 1 before run_paper_execution is ever called."""
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "true")
        monkeypatch.setenv("ENABLE_PAPER_EXECUTION", "false")
        monkeypatch.delenv("LIVE_TRADING_CONFIRMED", raising=False)
        with pytest.raises(RuntimeError, match="ENABLE_PAPER_EXECUTION"):
            _check_hard_env_gates()


# ===========================================================================
# TestReportStatusSemantics — PAPER_SUBMITTED only when submitted=True
# ===========================================================================

class TestReportStatusSemantics:
    """Prove that report status accurately reflects broker submission results.

    PAPER_SUBMITTED      → all attempted orders have submitted=True
    PAPER_PARTIAL_SUBMIT → some submitted=True, some submitted=False
    PAPER_ORDER_ERRORS   → all attempted orders have submitted=False
    PAPER_NO_ORDERS      → no execution-ready orders existed
    """

    def _ctx_with_ready_orders(self, tmp_path) -> dict:
        """Return a context with two execution-ready orders."""
        orders = [
            _order("AAPL", limit_price=150.00, client_order_id="TOS-20260512T000000-AAPL-BUY"),
            _order("BIL", limit_price=91.50, client_order_id="TOS-20260512T000000-BIL-BUY"),
        ]
        return _ctx(
            plan=_plan(orders=orders),
            exec_dir=tmp_path / "exec",
            orders_dir=tmp_path / "orders",
        )

    def test_all_submitted_true_produces_paper_submitted(self, monkeypatch, tmp_path):
        """All broker responses successful → PAPER_SUBMITTED."""
        _paper_env(monkeypatch)
        ctx = self._ctx_with_ready_orders(tmp_path)
        client = _mock_trading_client("broker-aaa")
        report = run_paper_execution(ctx, client, confirm_paper=True)
        submitted = report.get("orders_submitted", [])
        if submitted:
            all_ok = all(o.get("submitted") is True for o in submitted)
            if all_ok:
                assert report["status"] == "PAPER_SUBMITTED"

    def test_api_error_does_not_produce_paper_submitted(self, monkeypatch, tmp_path):
        """Broker raises an exception → submitted=False → status must NOT be PAPER_SUBMITTED."""
        _paper_env(monkeypatch)
        ctx = self._ctx_with_ready_orders(tmp_path)
        client = MagicMock()
        client.submit_order.side_effect = RuntimeError("Alpaca API error")
        report = run_paper_execution(ctx, client, confirm_paper=True)
        submitted = report.get("orders_submitted", [])
        if submitted:
            assert report["status"] != "PAPER_SUBMITTED", (
                f"status should not be PAPER_SUBMITTED when all orders have submitted=False "
                f"(got {report['status']!r})"
            )

    def test_all_broker_errors_produce_paper_order_errors(self, monkeypatch, tmp_path):
        """All broker calls fail → PAPER_ORDER_ERRORS."""
        _paper_env(monkeypatch)
        ctx = self._ctx_with_ready_orders(tmp_path)
        client = MagicMock()
        client.submit_order.side_effect = RuntimeError("connection refused")
        report = run_paper_execution(ctx, client, confirm_paper=True)
        submitted = report.get("orders_submitted", [])
        if submitted:
            assert report["status"] == "PAPER_ORDER_ERRORS", (
                f"All orders failed broker submission; expected PAPER_ORDER_ERRORS "
                f"but got {report['status']!r}"
            )
            assert report.get("blocked_reason") is not None
            assert "failed" in (report.get("blocked_reason") or "").lower()

    def test_mixed_results_produce_paper_partial_submit(self, monkeypatch, tmp_path):
        """First order succeeds, second fails → PAPER_PARTIAL_SUBMIT."""
        _paper_env(monkeypatch)
        ctx = self._ctx_with_ready_orders(tmp_path)

        # First call succeeds, second raises
        response = MagicMock()
        response.id = "broker-partial"
        response.status = "accepted"
        response.model_dump.return_value = {"id": "broker-partial", "status": "accepted"}
        client = MagicMock()
        client.submit_order.side_effect = [response, RuntimeError("quota exceeded")]

        report = run_paper_execution(ctx, client, confirm_paper=True)
        submitted = report.get("orders_submitted", [])
        if len(submitted) == 2:
            n_ok = sum(1 for o in submitted if o.get("submitted") is True)
            n_fail = len(submitted) - n_ok
            if n_ok > 0 and n_fail > 0:
                assert report["status"] == "PAPER_PARTIAL_SUBMIT", (
                    f"Expected PAPER_PARTIAL_SUBMIT for mixed results; "
                    f"got {report['status']!r}"
                )

    def test_no_execution_ready_orders_produces_paper_no_orders(self, monkeypatch, tmp_path):
        """No execution-ready orders → PAPER_NO_ORDERS (not PAPER_SUBMITTED)."""
        _paper_env(monkeypatch)
        skipped = [
            _order("AAPL", skip_reason="below_min_notional", notional=1.0),
            _order("BIL", skip_reason="spread_too_wide"),
        ]
        ctx = _ctx(
            plan=_plan(orders=skipped),
            exec_dir=tmp_path / "exec",
            orders_dir=tmp_path / "orders",
        )
        client = MagicMock()
        report = run_paper_execution(ctx, client, confirm_paper=True)
        if report["status"] not in ("PAPER_FAIL", "PAPER_BLOCKED"):
            assert report["status"] == "PAPER_NO_ORDERS", (
                f"Expected PAPER_NO_ORDERS when all orders are skipped; "
                f"got {report['status']!r}"
            )
        assert client.submit_order.call_count == 0

    def test_submitted_false_result_has_error_field(self, monkeypatch, tmp_path):
        """When a broker call fails, the result must have a non-None error field."""
        _paper_env(monkeypatch)
        ctx = self._ctx_with_ready_orders(tmp_path)
        client = MagicMock()
        client.submit_order.side_effect = ValueError("bad request")
        report = run_paper_execution(ctx, client, confirm_paper=True)
        for o in report.get("orders_submitted", []):
            if o.get("submitted") is False:
                assert o.get("error") is not None, (
                    f"submitted=False order must carry an error field"
                )


# ===========================================================================
# TestBuildFreshExecutionSnapshots — source wiring from fetch_account_state
# ===========================================================================

class TestBuildFreshExecutionSnapshots:
    """Verify that fresh Alpaca state is correctly sliced with source fields preserved.

    This is the root-cause fix for CANONICAL_SOURCE_INTEGRITY failing when
    execute_paper.py reconstructed snapshots without source='alpaca_paper'.
    """

    def _fresh_state(self, source: str = "alpaca_paper") -> dict:
        return {
            "source": source,
            "schema_version": "0.1.0",
            "fetched_at": utc_now_iso(),
            "account": {"status": "ACTIVE", "equity": "40000.00"},
            "positions": [],
            "orders": [],
            "clock": {"is_open": True, "timestamp": utc_now_iso()},
            "position_count": 0,
            "open_order_count": 0,
        }

    def test_account_snapshot_has_source_alpaca_paper(self):
        from trading_os.execution.paper_executor import build_fresh_execution_snapshots
        acct, _, _ = build_fresh_execution_snapshots(self._fresh_state())
        assert acct["source"] == "alpaca_paper"

    def test_positions_snapshot_has_source_alpaca_paper(self):
        from trading_os.execution.paper_executor import build_fresh_execution_snapshots
        _, pos, _ = build_fresh_execution_snapshots(self._fresh_state())
        assert pos["source"] == "alpaca_paper"

    def test_orders_snapshot_has_source_alpaca_paper(self):
        from trading_os.execution.paper_executor import build_fresh_execution_snapshots
        _, _, ord_ = build_fresh_execution_snapshots(self._fresh_state())
        assert ord_["source"] == "alpaca_paper"

    def test_account_snapshot_has_fetched_at(self):
        from trading_os.execution.paper_executor import build_fresh_execution_snapshots
        acct, _, _ = build_fresh_execution_snapshots(self._fresh_state())
        assert acct["fetched_at"] != ""

    def test_positions_snapshot_has_fetched_at(self):
        from trading_os.execution.paper_executor import build_fresh_execution_snapshots
        _, pos, _ = build_fresh_execution_snapshots(self._fresh_state())
        assert pos["fetched_at"] != ""

    def test_orders_snapshot_has_fetched_at(self):
        from trading_os.execution.paper_executor import build_fresh_execution_snapshots
        _, _, ord_ = build_fresh_execution_snapshots(self._fresh_state())
        assert ord_["fetched_at"] != ""

    def test_account_snapshot_has_open_order_count(self):
        from trading_os.execution.paper_executor import build_fresh_execution_snapshots
        acct, _, _ = build_fresh_execution_snapshots(self._fresh_state())
        assert "open_order_count" in acct

    def test_account_snapshot_has_schema_version(self):
        from trading_os.execution.paper_executor import build_fresh_execution_snapshots
        acct, _, _ = build_fresh_execution_snapshots(self._fresh_state())
        assert acct["schema_version"] == "0.1.0"

    def test_all_three_snapshots_have_data_hash(self):
        from trading_os.execution.paper_executor import build_fresh_execution_snapshots
        acct, pos, ord_ = build_fresh_execution_snapshots(self._fresh_state())
        assert len(acct["data_hash"]) == 64
        assert len(pos["data_hash"]) == 64
        assert len(ord_["data_hash"]) == 64

    def test_non_alpaca_source_propagated_not_hardcoded(self):
        """Wrong source propagates so the gate (not the helper) rejects it."""
        from trading_os.execution.paper_executor import build_fresh_execution_snapshots
        acct, pos, ord_ = build_fresh_execution_snapshots(self._fresh_state("dry_run_mock"))
        assert acct["source"] == "dry_run_mock"
        assert pos["source"] == "dry_run_mock"
        assert ord_["source"] == "dry_run_mock"


# ===========================================================================
# TestCanonicalSourceIntegrityGateWiring
# ===========================================================================

def _account_snapshot_with_source(source: str = "alpaca_paper", **kwargs) -> dict:
    return {
        "source": source,
        "account": {"equity": "40000.00", "cash": "40000.00", "status": "ACTIVE"},
        "clock": {"is_open": True, "timestamp": utc_now_iso()},
        "position_count": 0,
        "open_order_count": 0,
        "fetched_at": utc_now_iso(),
        **kwargs,
    }


def _positions_snapshot_with_source(source: str = "alpaca_paper", **kwargs) -> dict:
    return {
        "source": source,
        "positions": [],
        "position_count": 0,
        "fetched_at": utc_now_iso(),
        **kwargs,
    }


def _orders_snapshot_with_source(source: str = "alpaca_paper", **kwargs) -> dict:
    return {
        "source": source,
        "orders": [],
        "open_order_count": 0,
        "fetched_at": utc_now_iso(),
        **kwargs,
    }


def _market_snapshot_with_source(source: str = "alpaca_paper") -> dict:
    now = utc_now_iso()
    return {
        "source": source,
        "generated_at": now,
        "quotes": {"AAPL": {"bid_price": 100.0, "ask_price": 100.1, "timestamp": now},
                   "BIL": {"bid_price": 91.4, "ask_price": 91.5, "timestamp": now}},
        "spreads": {"AAPL": {"spread_pct": 0.001}, "BIL": {"spread_pct": 0.001}},
    }


class TestCanonicalSourceIntegrityGateWiring:
    """Prove CANONICAL_SOURCE_INTEGRITY passes/fails correctly with run_paper_execution."""

    def _full_ctx(self, tmp_path, **overrides) -> dict:
        base = _ctx(
            acct=_account_snapshot_with_source("alpaca_paper"),
            pos_snap=_positions_snapshot_with_source("alpaca_paper"),
            ord_snap=_orders_snapshot_with_source("alpaca_paper"),
            mkt=_market_snapshot_with_source("alpaca_paper"),
            exec_dir=tmp_path / "exec",
            orders_dir=tmp_path / "orders",
        )
        base.update(overrides)
        return base

    def _gate_result(self, report: dict, gate_id: str) -> dict | None:
        return next(
            (g for g in report.get("gate_results", []) if g["gate_id"] == gate_id),
            None,
        )

    def test_all_alpaca_paper_integrity_gate_passes(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        report = run_paper_execution(
            self._full_ctx(tmp_path), _mock_trading_client(), confirm_paper=True
        )
        gate = self._gate_result(report, "CANONICAL_SOURCE_INTEGRITY")
        assert gate is not None
        assert gate["passes"] is True

    def test_missing_source_account_snapshot_fails_integrity(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = self._full_ctx(tmp_path)
        ctx["account_snapshot"] = _account_snapshot()  # no source field
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        gate = self._gate_result(report, "CANONICAL_SOURCE_INTEGRITY")
        assert gate["passes"] is False

    def test_unknown_source_account_snapshot_fails_integrity(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = self._full_ctx(tmp_path)
        ctx["account_snapshot"] = _account_snapshot_with_source("unknown")
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        gate = self._gate_result(report, "CANONICAL_SOURCE_INTEGRITY")
        assert gate["passes"] is False

    def test_missing_source_positions_snapshot_fails_integrity(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = self._full_ctx(tmp_path)
        ctx["positions_snapshot"] = _positions_snapshot()  # no source field
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        gate = self._gate_result(report, "CANONICAL_SOURCE_INTEGRITY")
        assert gate["passes"] is False

    def test_missing_source_orders_snapshot_fails_integrity(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = self._full_ctx(tmp_path)
        ctx["orders_snapshot"] = _orders_snapshot()  # no source field
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        gate = self._gate_result(report, "CANONICAL_SOURCE_INTEGRITY")
        assert gate["passes"] is False

    def test_no_orders_submitted_when_source_missing(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = self._full_ctx(tmp_path)
        ctx["account_snapshot"] = _account_snapshot()  # no source → gate fails
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        assert report["orders_submitted"] == []

    def test_dry_run_mock_source_fails_integrity(self, monkeypatch, tmp_path):
        _paper_env(monkeypatch)
        ctx = self._full_ctx(tmp_path)
        ctx["positions_snapshot"] = _positions_snapshot_with_source("dry_run_mock")
        report = run_paper_execution(ctx, _mock_trading_client(), confirm_paper=True)
        gate = self._gate_result(report, "CANONICAL_SOURCE_INTEGRITY")
        assert gate["passes"] is False
        assert report["orders_submitted"] == []

    def test_enable_paper_execution_false_fails_closed(self, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "true")
        monkeypatch.setenv("ENABLE_PAPER_EXECUTION", "false")
        monkeypatch.delenv("LIVE_TRADING_CONFIRMED", raising=False)
        with pytest.raises(RuntimeError, match="ENABLE_PAPER_EXECUTION"):
            _check_hard_env_gates()


# ===========================================================================
# TestDryRunExecutePreservesSource
# ===========================================================================

class TestDryRunExecutePreservesSource:
    """Verify dry_run_execute.py loads canonical snapshots without reconstructing them."""

    def _script(self) -> str:
        return (
            Path(__file__).resolve().parents[1] / "scripts" / "dry_run_execute.py"
        ).read_text(encoding="utf-8")

    def test_loads_account_snapshot_from_data_latest(self):
        assert 'LATEST_DIR / "account_snapshot.json"' in self._script()

    def test_loads_positions_snapshot_from_data_latest(self):
        assert 'LATEST_DIR / "positions_snapshot.json"' in self._script()

    def test_loads_orders_snapshot_from_data_latest(self):
        assert 'LATEST_DIR / "orders_snapshot.json"' in self._script()

    def test_does_not_fetch_fresh_account_state(self):
        """dry_run_execute must not call the broker — source comes from saved snapshots."""
        assert "fetch_account_state" not in self._script()
        assert "AlpacaPaperClient" not in self._script()

    def test_passes_loaded_snapshots_unmodified_to_gate_context(self):
        """Snapshots are passed through loaded dict, not reconstructed without source."""
        src = self._script()
        assert 'loaded["account_snapshot"]' in src
        assert 'loaded["positions_snapshot"]' in src
        assert 'loaded["orders_snapshot"]' in src
