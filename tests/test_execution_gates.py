"""Tests for src/trading_os/execution/execution_gates.py and order_builder.py"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trading_os.execution.execution_gates import (
    all_gates_pass,
    gate_account_not_blocked,
    gate_alpaca_paper_mode,
    gate_execution_log_writable,
    gate_market_clock_open,
    gate_no_duplicate_open_orders,
    gate_no_prohibited_orders,
    gate_plan_exists,
    gate_plan_not_expired,
    gate_positions_match_snapshot,
    gate_quote_freshness,
    gate_risk_limits_respected,
    gate_risk_state_not_paused,
    gate_spread_not_too_wide,
    gate_symbols_tradable,
    gate_trading_mode_paper,
    gate_universe_membership,
    run_all_gates,
)
from trading_os.execution.order_builder import build_execution_order, build_execution_orders
from trading_os.time_utils import utc_now_iso


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _future_ts(minutes: int = 120) -> str:
    from datetime import datetime, timezone, timedelta
    return (datetime.now(timezone.utc) + timedelta(minutes=minutes)).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _past_ts(minutes: int = 10) -> str:
    from datetime import datetime, timezone, timedelta
    return (datetime.now(timezone.utc) - timedelta(minutes=minutes)).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _plan(
    trading_mode: str = "paper",
    expires_at: str | None = None,
    orders: list | None = None,
    risk_checks: list | None = None,
    targets: dict | None = None,
) -> dict:
    return {
        "plan_id": "trade_plan-20260512T000000-abc12345",
        "generated_at": _past_ts(5),
        "expires_at": expires_at or _future_ts(360),
        "trading_mode": trading_mode,
        "trade_plan_hash": "x" * 64,
        "proposed_orders": orders if orders is not None else [_order("AAPL"), _order("BIL")],
        "risk_checks": risk_checks if risk_checks is not None else [],
        "targets": targets or {"AAPL": {"weight": 0.09}, "BIL": {"weight": 0.91}},
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
    }


def _account_snapshot(status: str = "ACTIVE", is_open: bool = True, pos_count: int = 0) -> dict:
    return {
        "account": {"equity": "40000.00", "cash": "40000.00", "status": status},
        "clock": {"is_open": is_open, "timestamp": utc_now_iso()},
        "position_count": pos_count,
        "fetched_at": utc_now_iso(),
    }


def _positions_snapshot(pos_count: int = 0, age_minutes: int = 5) -> dict:
    return {
        "positions": [],
        "position_count": pos_count,
        "fetched_at": _past_ts(age_minutes),
    }


def _orders_snapshot(orders: list | None = None) -> dict:
    return {"orders": orders or [], "open_order_count": len(orders or [])}


def _market_snapshot(symbols: list | None = None, spread_pct: float = 0.001) -> dict:
    syms = symbols or ["AAPL", "MSFT", "BIL"]
    now = utc_now_iso()
    return {
        "generated_at": now,
        "quotes": {sym: {"symbol": sym, "bid_price": 100.0, "ask_price": 100.1, "timestamp": now} for sym in syms},
        "spreads": {sym: {"symbol": sym, "spread_pct": spread_pct} for sym in syms},
    }


def _risk_state(drawdown: float = 0.0, paused: bool = False) -> dict:
    rs = {
        "drawdown": drawdown,
        "peak_equity": 40000.0,
        "latest_equity": 40000.0 * (1 + drawdown),
        "position_count": 0,
        "schema_version": "0.1.0",
        "updated_at": utc_now_iso(),
    }
    if paused:
        rs["paused"] = True
    return rs


def _risk_limits(max_drawdown_block: float = -0.1, block_syms: list | None = None) -> dict:
    return {
        "live_trading_allowed": False,
        "max_drawdown_block_pct": max_drawdown_block,
        "max_position_weight": 0.12,
        "max_holdings": 10,
        "min_order_notional": 25.0,
        "max_quote_spread_pct": 0.02,
        "allowed_fallbacks": ["BIL", "SPY"],
        "block_symbols": block_syms or [],
    }


def _strategy(equity_alloc: float = 0.9, max_pos_weight: float = 0.35) -> dict:
    return {
        "trading_mode": "paper_only",
        "parameters": {
            "max_holdings": 10,
            "max_position_weight": max_pos_weight,
            "max_names_per_sector": 2,
            "risk_on_equity_alloc": equity_alloc,
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
    dry_run: bool = True,
) -> dict:
    with tempfile.TemporaryDirectory() as td:
        default_exec_dir = Path(td) / "executions"
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
        "dry_run":            dry_run,
    }


# ===========================================================================
# all_gates_pass
# ===========================================================================

class TestAllGatesPass:
    def test_all_pass_returns_true(self):
        gates = [{"gate_id": "X", "passes": True, "detail": None}] * 5
        assert all_gates_pass(gates) is True

    def test_one_fail_returns_false(self):
        gates = [{"gate_id": "X", "passes": True, "detail": None},
                 {"gate_id": "Y", "passes": False, "detail": "oops"}]
        assert all_gates_pass(gates) is False

    def test_empty_returns_true(self):
        assert all_gates_pass([]) is True


# ===========================================================================
# Individual gate tests
# ===========================================================================

class TestGateTradingModePaper:
    def test_paper_mode_passes(self):
        r = gate_trading_mode_paper(_ctx(plan=_plan(trading_mode="paper")))
        assert r["passes"] is True

    def test_non_paper_fails(self):
        r = gate_trading_mode_paper(_ctx(plan=_plan(trading_mode="live")))
        assert r["passes"] is False

    def test_gate_id(self):
        assert gate_trading_mode_paper(_ctx())["gate_id"] == "TRADING_MODE_PAPER"


class TestGateAlpacaPaperMode:
    def test_passes_in_dry_run_without_env(self, monkeypatch):
        monkeypatch.delenv("ALPACA_PAPER", raising=False)
        r = gate_alpaca_paper_mode(_ctx(dry_run=True))
        assert r["passes"] is True

    def test_passes_when_env_true(self, monkeypatch):
        monkeypatch.setenv("ALPACA_PAPER", "true")
        r = gate_alpaca_paper_mode(_ctx())
        assert r["passes"] is True

    def test_fails_when_env_explicitly_false_live_mode(self, monkeypatch):
        monkeypatch.setenv("ALPACA_PAPER", "false")
        r = gate_alpaca_paper_mode(_ctx(dry_run=False))
        assert r["passes"] is False

    def test_gate_id(self):
        assert gate_alpaca_paper_mode(_ctx())["gate_id"] == "ALPACA_PAPER_MODE"


class TestGatePlanExists:
    def test_valid_plan_passes(self):
        assert gate_plan_exists(_ctx())["passes"] is True

    def test_empty_plan_fails(self):
        r = gate_plan_exists(_ctx(plan={}))
        assert r["passes"] is False

    def test_missing_fields_fails(self):
        r = gate_plan_exists(_ctx(plan={"plan_id": "x"}))
        assert r["passes"] is False

    def test_gate_id(self):
        assert gate_plan_exists(_ctx())["gate_id"] == "TRADE_PLAN_EXISTS"


class TestGatePlanNotExpired:
    def test_future_expiry_passes(self):
        plan = _plan(expires_at=_future_ts(120))
        assert gate_plan_not_expired(_ctx(plan=plan))["passes"] is True

    def test_past_expiry_fails(self):
        plan = _plan(expires_at=_past_ts(60))
        r = gate_plan_not_expired(_ctx(plan=plan))
        assert r["passes"] is False

    def test_missing_expiry_fails(self):
        plan = dict(_plan())
        plan["expires_at"] = ""
        r = gate_plan_not_expired(_ctx(plan=plan))
        assert r["passes"] is False

    def test_gate_id(self):
        assert gate_plan_not_expired(_ctx())["gate_id"] == "TRADE_PLAN_NOT_EXPIRED"


class TestGateMarketClockOpen:
    def test_open_market_passes(self):
        r = gate_market_clock_open(_ctx(acct=_account_snapshot(is_open=True)))
        assert r["passes"] is True

    def test_closed_market_passes_in_dry_run(self):
        r = gate_market_clock_open(_ctx(acct=_account_snapshot(is_open=False), dry_run=True))
        assert r["passes"] is True
        assert r["detail"] is not None  # informational note

    def test_closed_market_fails_in_live_mode(self):
        ctx = _ctx(acct=_account_snapshot(is_open=False), dry_run=False)
        r = gate_market_clock_open(ctx)
        assert r["passes"] is False

    def test_gate_id(self):
        assert gate_market_clock_open(_ctx())["gate_id"] == "MARKET_CLOCK_OPEN"


class TestGateAccountNotBlocked:
    def test_active_passes(self):
        assert gate_account_not_blocked(_ctx(acct=_account_snapshot(status="ACTIVE")))["passes"] is True

    def test_blocked_fails(self):
        r = gate_account_not_blocked(_ctx(acct=_account_snapshot(status="ACCOUNT_BLOCKED")))
        assert r["passes"] is False

    def test_papered_active_passes(self):
        assert gate_account_not_blocked(_ctx())["passes"] is True

    def test_gate_id(self):
        assert gate_account_not_blocked(_ctx())["gate_id"] == "ACCOUNT_NOT_BLOCKED"


class TestGateRiskStateNotPaused:
    def test_normal_state_passes(self):
        assert gate_risk_state_not_paused(_ctx(rs=_risk_state(drawdown=0.0)))["passes"] is True

    def test_paused_fails(self):
        r = gate_risk_state_not_paused(_ctx(rs=_risk_state(paused=True)))
        assert r["passes"] is False

    def test_drawdown_at_block_threshold_fails(self):
        # drawdown=-0.10 is AT the block threshold (-0.10), so <=, should fail
        r = gate_risk_state_not_paused(_ctx(rs=_risk_state(drawdown=-0.10), rl=_risk_limits(max_drawdown_block=-0.10)))
        assert r["passes"] is False

    def test_drawdown_within_limit_passes(self):
        r = gate_risk_state_not_paused(_ctx(rs=_risk_state(drawdown=-0.05), rl=_risk_limits(max_drawdown_block=-0.10)))
        assert r["passes"] is True

    def test_gate_id(self):
        assert gate_risk_state_not_paused(_ctx())["gate_id"] == "RISK_STATE_NOT_PAUSED"


class TestGatePositionsMatchSnapshot:
    def test_fresh_snapshot_passes(self):
        r = gate_positions_match_snapshot(_ctx(pos_snap=_positions_snapshot(age_minutes=5)))
        assert r["passes"] is True

    def test_stale_snapshot_fails(self):
        r = gate_positions_match_snapshot(_ctx(pos_snap=_positions_snapshot(age_minutes=200)))
        assert r["passes"] is False

    def test_missing_fetched_at_fails(self):
        snap = {"positions": [], "position_count": 0}
        r = gate_positions_match_snapshot(_ctx(pos_snap=snap))
        assert r["passes"] is False

    def test_count_mismatch_fails(self):
        pos_snap = _positions_snapshot(pos_count=3, age_minutes=5)
        acct = _account_snapshot(pos_count=1)
        r = gate_positions_match_snapshot(_ctx(acct=acct, pos_snap=pos_snap))
        assert r["passes"] is False

    def test_gate_id(self):
        assert gate_positions_match_snapshot(_ctx())["gate_id"] == "POSITIONS_MATCH_SNAPSHOT"


class TestGateNoDuplicateOpenOrders:
    def test_no_open_orders_passes(self):
        r = gate_no_duplicate_open_orders(_ctx(ord_snap=_orders_snapshot([])))
        assert r["passes"] is True

    def test_open_order_for_unrelated_symbol_passes(self):
        open_orders = [{"symbol": "GOOGL", "status": "open"}]
        r = gate_no_duplicate_open_orders(_ctx(ord_snap=_orders_snapshot(open_orders)))
        assert r["passes"] is True

    def test_open_order_for_proposed_symbol_fails(self):
        # AAPL is in default proposed orders
        open_orders = [{"symbol": "AAPL", "status": "open"}]
        r = gate_no_duplicate_open_orders(_ctx(ord_snap=_orders_snapshot(open_orders)))
        assert r["passes"] is False

    def test_gate_id(self):
        assert gate_no_duplicate_open_orders(_ctx())["gate_id"] == "NO_DUPLICATE_OPEN_ORDERS"


class TestGateUniverseMembership:
    def test_all_in_universe_passes(self):
        plan = _plan(orders=[_order("AAPL"), _order("BIL")])
        universe = _universe(["AAPL", "MSFT"])
        r = gate_universe_membership(_ctx(plan=plan, universe=universe))
        assert r["passes"] is True  # BIL is in allowed_fallbacks

    def test_outsider_symbol_fails(self):
        plan = _plan(orders=[_order("FAKE")])
        r = gate_universe_membership(_ctx(plan=plan))
        assert r["passes"] is False

    def test_fallback_symbols_allowed(self):
        plan = _plan(orders=[_order("SPY")])
        r = gate_universe_membership(_ctx(plan=plan))
        assert r["passes"] is True

    def test_gate_id(self):
        assert gate_universe_membership(_ctx())["gate_id"] == "UNIVERSE_MEMBERSHIP"


class TestGateSymbolsTradable:
    def test_universe_symbols_pass(self):
        plan = _plan(orders=[_order("AAPL")])
        r = gate_symbols_tradable(_ctx(plan=plan, universe=_universe(["AAPL"])))
        assert r["passes"] is True

    def test_non_universe_symbol_fails(self):
        plan = _plan(orders=[_order("DOGE")])
        r = gate_symbols_tradable(_ctx(plan=plan, universe=_universe(["AAPL"])))
        assert r["passes"] is False

    def test_gate_id(self):
        assert gate_symbols_tradable(_ctx())["gate_id"] == "SYMBOLS_TRADABLE"


class TestGateQuoteFreshness:
    def test_fresh_quotes_pass(self):
        mkt = _market_snapshot(["AAPL", "BIL"])
        plan = _plan(orders=[_order("AAPL"), _order("BIL")])
        r = gate_quote_freshness(_ctx(plan=plan, mkt=mkt))
        assert r["passes"] is True

    def test_missing_quote_fails(self):
        mkt = _market_snapshot(["MSFT"])  # no AAPL quote
        plan = _plan(orders=[_order("AAPL")])
        r = gate_quote_freshness(_ctx(plan=plan, mkt=mkt))
        assert r["passes"] is False

    def test_stale_quote_fails(self):
        old_ts = _past_ts(200)
        mkt = {
            "generated_at": old_ts,
            "quotes": {"AAPL": {"timestamp": old_ts, "bid_price": 100, "ask_price": 100.1}},
            "spreads": {},
        }
        plan = _plan(orders=[_order("AAPL")])
        r = gate_quote_freshness(_ctx(plan=plan, mkt=mkt))
        assert r["passes"] is False

    def test_gate_id(self):
        assert gate_quote_freshness(_ctx())["gate_id"] == "QUOTE_FRESHNESS"


class TestGateSpreadNotTooWide:
    def test_narrow_spread_passes(self):
        mkt = _market_snapshot(["AAPL", "BIL"], spread_pct=0.001)
        plan = _plan(orders=[_order("AAPL"), _order("BIL")])
        r = gate_spread_not_too_wide(_ctx(plan=plan, mkt=mkt))
        assert r["passes"] is True

    def test_wide_spread_fails(self):
        mkt = _market_snapshot(["AAPL", "BIL"], spread_pct=0.10)
        plan = _plan(orders=[_order("AAPL"), _order("BIL")])
        r = gate_spread_not_too_wide(_ctx(plan=plan, mkt=mkt))
        assert r["passes"] is False

    def test_no_spread_data_passes(self):
        mkt = {"quotes": {}, "spreads": {}}
        plan = _plan(orders=[_order("AAPL")])
        r = gate_spread_not_too_wide(_ctx(plan=plan, mkt=mkt))
        assert r["passes"] is True  # no data → cannot block

    def test_gate_id(self):
        assert gate_spread_not_too_wide(_ctx())["gate_id"] == "SPREAD_NOT_TOO_WIDE"


class TestGateRiskLimitsRespected:
    def test_passing_risk_checks_passes(self):
        plan = _plan(risk_checks=[{"check_id": "X", "passes": True}])
        r = gate_risk_limits_respected(_ctx(plan=plan))
        assert r["passes"] is True

    def test_failed_plan_risk_check_fails(self):
        plan = _plan(risk_checks=[{"check_id": "TRADING_MODE_PAPER", "passes": False}])
        r = gate_risk_limits_respected(_ctx(plan=plan))
        assert r["passes"] is False

    def test_overweight_order_fails(self):
        orders = [_order("AAPL", target_weight=0.50)]  # well above 0.12 cap
        plan = _plan(orders=orders, risk_checks=[])
        strat = _strategy(max_pos_weight=0.12)
        r = gate_risk_limits_respected(_ctx(plan=plan, strat=strat))
        assert r["passes"] is False

    def test_gate_id(self):
        assert gate_risk_limits_respected(_ctx())["gate_id"] == "RISK_LIMITS_RESPECTED"


class TestGateNoProhibitedOrders:
    def test_clean_buy_orders_pass(self):
        orders = [_order("AAPL", side="buy"), _order("BIL", side="buy")]
        r = gate_no_prohibited_orders(_ctx(plan=_plan(orders=orders)))
        assert r["passes"] is True

    def test_short_sell_fails(self):
        orders = [_order("AAPL", side="sell", would_short=True)]
        r = gate_no_prohibited_orders(_ctx(plan=_plan(orders=orders)))
        assert r["passes"] is False

    def test_valid_sell_to_exit_passes(self):
        # would_short=False, side=sell → legitimate exit
        orders = [_order("AAPL", side="sell", would_short=False)]
        r = gate_no_prohibited_orders(_ctx(plan=_plan(orders=orders)))
        assert r["passes"] is True

    def test_invalid_order_type_fails(self):
        orders = [_order("AAPL", order_type="stop_loss")]
        r = gate_no_prohibited_orders(_ctx(plan=_plan(orders=orders)))
        assert r["passes"] is False

    def test_extended_hours_tif_fails(self):
        orders = [_order("AAPL", time_in_force="opg")]
        r = gate_no_prohibited_orders(_ctx(plan=_plan(orders=orders)))
        assert r["passes"] is False

    def test_skipped_orders_are_ignored(self):
        orders = [_order("AAPL", skip_reason="below_min_notional", would_short=True)]
        r = gate_no_prohibited_orders(_ctx(plan=_plan(orders=orders)))
        assert r["passes"] is True  # skipped order not checked

    def test_gate_id(self):
        assert gate_no_prohibited_orders(_ctx())["gate_id"] == "NO_PROHIBITED_ORDERS"


class TestGateExecutionLogWritable:
    def test_writable_tmpdir_passes(self):
        with tempfile.TemporaryDirectory() as td:
            exec_dir = Path(td) / "executions"
            r = gate_execution_log_writable({"exec_history_dir": exec_dir})
            assert r["passes"] is True
            assert exec_dir.exists()

    def test_none_dir_fails(self):
        r = gate_execution_log_writable({"exec_history_dir": None})
        assert r["passes"] is False

    def test_gate_id(self):
        with tempfile.TemporaryDirectory() as td:
            r = gate_execution_log_writable({"exec_history_dir": Path(td) / "x"})
            assert r["gate_id"] == "EXECUTION_LOG_WRITABLE"


# ===========================================================================
# run_all_gates
# ===========================================================================

class TestRunAllGates:
    def test_returns_16_results(self):
        with tempfile.TemporaryDirectory() as td:
            ctx = _ctx(exec_dir=Path(td) / "exec")
            results = run_all_gates(ctx)
            assert len(results) == 16

    def test_each_result_has_required_keys(self):
        with tempfile.TemporaryDirectory() as td:
            ctx = _ctx(exec_dir=Path(td) / "exec")
            for r in run_all_gates(ctx):
                assert "gate_id" in r
                assert "passes" in r
                assert "detail" in r

    def test_clean_ctx_all_pass(self, monkeypatch):
        monkeypatch.delenv("ALPACA_PAPER", raising=False)
        monkeypatch.delenv("TRADING_MODE", raising=False)
        with tempfile.TemporaryDirectory() as td:
            ctx = _ctx(exec_dir=Path(td) / "exec")
            results = run_all_gates(ctx)
            failed = [r["gate_id"] for r in results if not r["passes"]]
            assert failed == [], f"Unexpected gate failures: {failed}"

    def test_never_raises_on_bad_context(self):
        results = run_all_gates({})
        assert isinstance(results, list)
        assert len(results) == 16

    def test_gate_ids_are_unique(self):
        with tempfile.TemporaryDirectory() as td:
            ctx = _ctx(exec_dir=Path(td) / "exec")
            results = run_all_gates(ctx)
            ids = [r["gate_id"] for r in results]
            assert len(ids) == len(set(ids))


# ===========================================================================
# order_builder
# ===========================================================================

class TestBuildExecutionOrder:
    def _base(self, symbol: str = "AAPL", **kw) -> dict:
        return build_execution_order(
            proposed=_order(symbol, **kw),
            plan_id="trade_plan-20260512T000000-abc12345",
            universe_symbols={"AAPL", "MSFT"},
            fallback_symbols={"BIL", "SPY"},
            max_spread_pct=0.02,
            spreads={"AAPL": {"spread_pct": 0.001}},
            min_order_notional=25.0,
        )

    def test_valid_order_execution_ready(self):
        o = self._base()
        assert o["execution_ready"] is True
        assert o["validation_skip_reason"] is None

    def test_client_order_id_has_symbol(self):
        o = self._base("AAPL", side="buy")
        assert "AAPL" in o["client_order_id"]
        assert "BUY" in o["client_order_id"]

    def test_non_universe_symbol_not_ready(self):
        o = build_execution_order(
            proposed=_order("FAKE"),
            plan_id="trade_plan-20260512T000000-abc12345",
            universe_symbols={"AAPL"},
            fallback_symbols={"BIL"},
            max_spread_pct=0.02,
            spreads={},
            min_order_notional=25.0,
        )
        assert o["execution_ready"] is False
        assert "not_in_universe" in (o["validation_skip_reason"] or "")

    def test_would_short_not_ready(self):
        o = self._base(would_short=True)
        assert o["execution_ready"] is False

    def test_below_min_notional_not_ready(self):
        o = self._base(notional=5.0)
        assert o["execution_ready"] is False

    def test_wide_spread_not_ready(self):
        o = build_execution_order(
            proposed=_order("AAPL"),
            plan_id="trade_plan-20260512T000000-abc12345",
            universe_symbols={"AAPL"},
            fallback_symbols={"BIL"},
            max_spread_pct=0.01,
            spreads={"AAPL": {"spread_pct": 0.05}},
            min_order_notional=25.0,
        )
        assert o["execution_ready"] is False

    def test_already_skipped_order_stays_not_ready(self):
        o = self._base(skip_reason="below_min_notional")
        assert o["execution_ready"] is False


class TestBuildExecutionOrders:
    def _build(self, orders: list | None = None) -> list:
        plan = _plan(orders=orders or [_order("AAPL"), _order("BIL")])
        return build_execution_orders(
            trade_plan=plan,
            universe=_universe(["AAPL"]),
            risk_limits=_risk_limits(),
            strategy=_strategy(),
            market_snapshot=_market_snapshot(["AAPL", "BIL"]),
        )

    def test_returns_list(self):
        assert isinstance(self._build(), list)

    def test_each_order_has_client_order_id(self):
        for o in self._build():
            assert "client_order_id" in o

    def test_each_order_has_execution_ready(self):
        for o in self._build():
            assert "execution_ready" in o

    def test_count_matches_proposed_orders(self):
        orders = [_order("AAPL"), _order("MSFT")]
        built = self._build(orders=orders)
        assert len(built) == 2
