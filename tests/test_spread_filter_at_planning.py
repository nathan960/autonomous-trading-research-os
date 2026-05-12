"""Tests: spread filtering at trade-plan generation time.

Requirements verified:
- Symbols whose bid-ask spread exceeds max_quote_spread_pct are removed from
  proposed_orders and added to blocked_symbols at planning time.
- Wide-spread symbols appear in spread_blocked_at_planning with a clear reason.
- no_trade_reasons contains a summary ONLY when spread blocking empties
  proposed_orders entirely; otherwise it contains a non_blocking entry.
- When some valid orders remain the plan is still approvable.
- risk_checks includes SPREAD_OK_AT_PLANNING and it passes after filtering.
- The execution-gate SPREAD_NOT_TOO_WIDE still re-validates (tested separately).
- All proposed_orders are limit orders (no market orders introduced).
- _filter_wide_spread_orders pure logic is covered directly.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.planning.trade_plan_builder import (
    _filter_wide_spread_orders,
    build_trade_plan,
)
from trading_os.planning.risk_checks import run_risk_checks


# ---------------------------------------------------------------------------
# Fixtures / builders
# ---------------------------------------------------------------------------

def _strategy(max_spread: float = 0.02) -> dict:
    return {
        "strategy_id": "test",
        "version": "0.1.0",
        "trading_mode": "paper_only",
        "asset_policy": {
            "long_only": True,
            "allow_shorting": False,
            "allow_options": False,
            "allow_crypto": False,
        },
        "parameters": {
            "max_holdings": 10,
            "max_position_weight": 0.12,
            "max_names_per_sector": 2,
            "min_order_notional": 25.0,
            "plan_expiry_minutes": 360,
            "max_quote_spread_pct": max_spread,
            "atr_lookback": 14,
            "breadth_threshold": 0.3,
            "max_atr_weight": 0.12,
            "regime_ema_fast": 50,
            "regime_ema_slow": 200,
        },
        "fallbacks": {
            "risk_off_target": {"symbol": "BIL", "weight": 1.0},
            "risk_on_no_candidates_target": {"symbol": "SPY", "weight": 1.0},
        },
    }


def _risk_limits(max_spread: float = 0.02) -> dict:
    return {
        "paper_only": True,
        "live_trading_allowed": False,
        "max_portfolio_gross_exposure": 1.0,
        "max_position_weight": 0.12,
        "max_holdings": 10,
        "max_names_per_sector": 2,
        "max_drawdown_warn_pct": -0.05,
        "max_drawdown_block_pct": -0.1,
        "min_order_notional": 25.0,
        "max_quote_spread_pct": max_spread,
        "block_symbols": [],
        "allowed_fallbacks": ["BIL", "SPY"],
    }


def _execution_policy() -> dict:
    return {
        "paper_only": True,
        "allow_options": False,
        "allow_crypto": False,
        "allow_shorting": False,
    }


def _sector_map(*symbols: str) -> dict:
    return {s: {"sector_code": "10"} for s in symbols}


def _spreads(*pairs: tuple) -> dict:
    """Build spreads dict: _spreads(("AAPL", 0.001), ("AMD", 0.05))"""
    return {sym: {"symbol": sym, "spread_pct": pct} for sym, pct in pairs}


def _bars(symbol: str, close: float = 100.0) -> list:
    return [{"t": "2026-05-01T00:00:00Z", "o": close, "h": close, "l": close, "c": close, "v": 1000}]


def _market_snapshot(spreads_data: dict, symbols: list | None = None) -> dict:
    syms = symbols or list(spreads_data.keys())
    bars = {s: _bars(s, 100.0) for s in syms}
    return {
        "schema_version": "0.1.0",
        "generated_at": "2026-05-12T14:00:00Z",
        "run_mode": "dry_run",
        "source_data_hash": "abc123",
        "bars": bars,
        "latest_bars": {},
        "quotes": {},
        "spreads": spreads_data,
        "assets": {},
        "account": {"equity": "40000.0", "cash": "40000.0", "buying_power": "40000.0", "status": "ACTIVE"},
        "positions": [],
        "orders": [],
        "clock": {"is_open": True},
    }


def _account_snapshot(equity: float = 40000.0) -> dict:
    return {
        "account": {
            "equity": str(equity),
            "cash": str(equity),
            "buying_power": str(equity),
            "status": "ACTIVE",
        },
        "position_count": 0,
        "fetched_at": "2026-05-12T14:00:00Z",
        "clock": {"is_open": True},
    }


def _trigger_snapshot(selected: list) -> dict:
    results = {
        sym: {
            "symbol": sym,
            "trigger_fired": True,
            "latest_close": 100.0,
            "atr": {"atr": 2.0, "atr_pct": 0.02, "latest_close": 100.0},
            "signal_score": 1.0,
        }
        for sym in selected
    }
    return {
        "scanned_at": "2026-05-12T14:00:00Z",
        "regime": {"risk_on": True},
        "selected": selected,
        "excluded": [],
        "symbol_results": results,
        "trigger_snapshot_hash": "def456",
        "data_stale_gate": {"passes": True},
    }


def _build_plan(
    selected: list,
    spread_map: dict,
    max_spread: float = 0.02,
    approve_paper: bool = False,
    equity: float = 40000.0,
) -> dict:
    all_symbols = selected
    return build_trade_plan(
        market_snapshot=_market_snapshot(spread_map, symbols=all_symbols),
        trigger_snapshot=_trigger_snapshot(selected),
        account_snapshot=_account_snapshot(equity),
        positions=[],
        strategy=_strategy(max_spread),
        risk_limits=_risk_limits(max_spread),
        execution_policy=_execution_policy(),
        sector_map=_sector_map(*all_symbols),
        approve_paper=approve_paper,
    )


# ---------------------------------------------------------------------------
# Unit tests: _filter_wide_spread_orders
# ---------------------------------------------------------------------------

class TestFilterWideSpreadOrders:
    def _order(self, symbol: str) -> dict:
        return {
            "symbol": symbol,
            "side": "buy",
            "order_type": "limit",
            "limit_price": 100.0,
            "notional": 500.0,
            "skip_reason": None,
        }

    def test_no_spreads_data_passes_all(self):
        orders = [self._order("AAPL"), self._order("AMD")]
        ok, blocked = _filter_wide_spread_orders(orders, spreads={}, max_spread=0.02)
        assert len(ok) == 2
        assert len(blocked) == 0

    def test_missing_spread_entry_passes(self):
        orders = [self._order("AAPL")]
        spreads = {"AMD": {"spread_pct": 0.001}}
        ok, blocked = _filter_wide_spread_orders(orders, spreads=spreads, max_spread=0.02)
        assert len(ok) == 1
        assert len(blocked) == 0

    def test_null_spread_pct_passes(self):
        orders = [self._order("AAPL")]
        spreads = {"AAPL": {"spread_pct": None}}
        ok, blocked = _filter_wide_spread_orders(orders, spreads=spreads, max_spread=0.02)
        assert len(ok) == 1

    def test_spread_at_threshold_passes(self):
        orders = [self._order("AAPL")]
        spreads = {"AAPL": {"spread_pct": 0.02}}
        ok, blocked = _filter_wide_spread_orders(orders, spreads=spreads, max_spread=0.02)
        assert len(ok) == 1
        assert len(blocked) == 0

    def test_spread_just_above_threshold_blocks(self):
        orders = [self._order("AMD")]
        spreads = {"AMD": {"spread_pct": 0.0201}}
        ok, blocked = _filter_wide_spread_orders(orders, spreads=spreads, max_spread=0.02)
        assert len(ok) == 0
        assert len(blocked) == 1
        assert blocked[0]["symbol"] == "AMD"
        assert "spread_too_wide" in blocked[0]["skip_reason"]

    def test_skip_reason_format(self):
        orders = [self._order("PEP")]
        spreads = {"PEP": {"spread_pct": 0.0500}}
        _, blocked = _filter_wide_spread_orders(orders, spreads=spreads, max_spread=0.02)
        assert blocked[0]["skip_reason"] == "spread_too_wide(0.0500>0.02)"

    def test_mixed_ok_and_blocked(self):
        orders = [self._order("AAPL"), self._order("AMD"), self._order("SPY")]
        spreads = {
            "AAPL": {"spread_pct": 0.001},
            "AMD": {"spread_pct": 0.05},
            "SPY": {"spread_pct": 0.003},
        }
        ok, blocked = _filter_wide_spread_orders(orders, spreads=spreads, max_spread=0.02)
        ok_syms = [o["symbol"] for o in ok]
        blocked_syms = [o["symbol"] for o in blocked]
        assert "AAPL" in ok_syms
        assert "SPY" in ok_syms
        assert "AMD" in blocked_syms

    def test_blocked_orders_remain_limit_type(self):
        orders = [self._order("AMD")]
        spreads = {"AMD": {"spread_pct": 0.10}}
        _, blocked = _filter_wide_spread_orders(orders, spreads=spreads, max_spread=0.02)
        assert blocked[0]["order_type"] == "limit"

    def test_no_market_orders_introduced(self):
        orders = [self._order(s) for s in ["AAPL", "AMD", "PEP", "KO"]]
        spreads = {s: {"spread_pct": 0.10} for s in ["AAPL", "AMD", "PEP", "KO"]}
        ok, blocked = _filter_wide_spread_orders(orders, spreads=spreads, max_spread=0.02)
        for o in ok + blocked:
            assert o["order_type"] != "market"


# ---------------------------------------------------------------------------
# Integration tests: build_trade_plan spread filtering
# ---------------------------------------------------------------------------

class TestBuildTradePlanSpreadFilter:
    def test_wide_spread_symbol_not_in_proposed_orders(self):
        selected = ["AAPL", "AMD"]
        spreads = {
            "AAPL": {"spread_pct": 0.001},
            "AMD": {"spread_pct": 0.05},  # wide
        }
        plan = _build_plan(selected, spreads)
        proposed_syms = [o["symbol"] for o in plan["proposed_orders"]]
        assert "AMD" not in proposed_syms

    def test_wide_spread_symbol_in_blocked_symbols(self):
        selected = ["AAPL", "AMD"]
        spreads = {
            "AAPL": {"spread_pct": 0.001},
            "AMD": {"spread_pct": 0.05},
        }
        plan = _build_plan(selected, spreads)
        blocked_syms = [
            b["symbol"] if isinstance(b, dict) else b
            for b in plan["blocked_symbols"]
        ]
        assert "AMD" in blocked_syms

    def test_blocked_entry_has_spread_skip_reason(self):
        selected = ["AAPL", "AMD"]
        spreads = {
            "AAPL": {"spread_pct": 0.001},
            "AMD": {"spread_pct": 0.05},
        }
        plan = _build_plan(selected, spreads)
        blocked_entries = [
            b for b in plan["blocked_symbols"]
            if isinstance(b, dict) and b.get("symbol") == "AMD"
        ]
        assert blocked_entries
        assert "spread_too_wide" in blocked_entries[0]["skip_reason"]

    def test_spread_blocked_at_planning_field_present(self):
        selected = ["AAPL", "AMD"]
        spreads = {
            "AAPL": {"spread_pct": 0.001},
            "AMD": {"spread_pct": 0.05},
        }
        plan = _build_plan(selected, spreads)
        assert "spread_blocked_at_planning" in plan
        syms = [e["symbol"] for e in plan["spread_blocked_at_planning"]]
        assert "AMD" in syms

    def test_spread_blocked_at_planning_empty_when_all_ok(self):
        selected = ["AAPL", "SPY"]
        spreads = {
            "AAPL": {"spread_pct": 0.001},
            "SPY": {"spread_pct": 0.001},
        }
        plan = _build_plan(selected, spreads)
        assert plan["spread_blocked_at_planning"] == []

    def test_valid_symbol_still_in_proposed_orders(self):
        selected = ["AAPL", "AMD"]
        spreads = {
            "AAPL": {"spread_pct": 0.001},
            "AMD": {"spread_pct": 0.05},
        }
        plan = _build_plan(selected, spreads)
        proposed_syms = [o["symbol"] for o in plan["proposed_orders"]]
        assert "AAPL" in proposed_syms

    def test_all_proposed_orders_are_limit_orders(self):
        selected = ["AAPL", "AMD", "SPY"]
        spreads = {
            "AAPL": {"spread_pct": 0.001},
            "AMD": {"spread_pct": 0.05},
            "SPY": {"spread_pct": 0.002},
        }
        plan = _build_plan(selected, spreads)
        for o in plan["proposed_orders"]:
            assert o["order_type"] != "market", f"Market order found: {o}"

    def test_no_trade_reason_non_blocking_when_some_orders_remain(self):
        selected = ["AAPL", "AMD"]
        spreads = {
            "AAPL": {"spread_pct": 0.001},
            "AMD": {"spread_pct": 0.05},
        }
        plan = _build_plan(selected, spreads)
        # AMD is spread-blocked but AAPL is still valid — should be non_blocking
        spread_reasons = [r for r in plan["no_trade_reasons"] if "spread" in r]
        assert spread_reasons
        assert all("non_blocking" in r for r in spread_reasons)

    def test_plan_approvable_when_some_orders_remain(self):
        selected = ["AAPL", "AMD"]
        spreads = {
            "AAPL": {"spread_pct": 0.001},
            "AMD": {"spread_pct": 0.05},
        }
        plan = _build_plan(selected, spreads, approve_paper=True)
        # AAPL should still be actionable, plan should be approvable
        assert plan["proposed_orders"], "Expected at least one proposed order"
        assert plan["approval"]["approved_for_execution"] is True

    def test_no_trade_reason_blocking_when_all_spread_blocked(self):
        selected = ["AAPL", "AMD"]
        spreads = {
            "AAPL": {"spread_pct": 0.10},
            "AMD": {"spread_pct": 0.05},
        }
        plan = _build_plan(selected, spreads)
        assert plan["proposed_orders"] == []
        blocking_reasons = [
            r for r in plan["no_trade_reasons"]
            if "spread_blocked_all_orders" in r
        ]
        assert blocking_reasons

    def test_plan_not_approvable_when_all_spread_blocked(self):
        selected = ["AAPL", "AMD"]
        spreads = {
            "AAPL": {"spread_pct": 0.10},
            "AMD": {"spread_pct": 0.05},
        }
        plan = _build_plan(selected, spreads, approve_paper=True)
        assert plan["approval"]["approved_for_execution"] is False

    def test_multiple_wide_spread_symbols_all_blocked(self):
        selected = ["AAPL", "AMD", "PEP", "KO", "SPY"]
        spreads = {
            "AAPL": {"spread_pct": 0.001},
            "AMD": {"spread_pct": 0.08},
            "PEP": {"spread_pct": 0.06},
            "KO": {"spread_pct": 0.001},
            "SPY": {"spread_pct": 0.001},
        }
        plan = _build_plan(selected, spreads)
        proposed_syms = {o["symbol"] for o in plan["proposed_orders"]}
        assert "AMD" not in proposed_syms
        assert "PEP" not in proposed_syms
        assert "AAPL" in proposed_syms or "KO" in proposed_syms or "SPY" in proposed_syms


# ---------------------------------------------------------------------------
# SPREAD_OK_AT_PLANNING risk check
# ---------------------------------------------------------------------------

class TestSpreadOkAtPlanningRiskCheck:
    def _base_checks_kwargs(self, proposed: list, spreads: dict, max_spread: float = 0.02) -> dict:
        return dict(
            targets={"AAPL": {"weight": 0.1, "notional": 4000.0}},
            proposed_orders=proposed,
            strategy=_strategy(max_spread),
            risk_limits=_risk_limits(max_spread),
            execution_policy=_execution_policy(),
            trigger_snapshot_hash="abc",
            data_hash="def",
            sector_map=_sector_map("AAPL"),
            spreads=spreads,
            max_quote_spread=max_spread,
        )

    def _order(self, symbol: str) -> dict:
        return {
            "symbol": symbol,
            "side": "buy",
            "order_type": "limit",
            "limit_price": 100.0,
            "notional": 500.0,
            "skip_reason": None,
        }

    def test_spread_ok_check_present_when_spreads_provided(self):
        checks = run_risk_checks(**self._base_checks_kwargs(
            proposed=[self._order("AAPL")],
            spreads={"AAPL": {"spread_pct": 0.001}},
        ))
        check_ids = [c["check_id"] for c in checks]
        assert "SPREAD_OK_AT_PLANNING" in check_ids

    def test_spread_ok_check_absent_when_no_spreads(self):
        checks = run_risk_checks(
            targets={},
            proposed_orders=[],
            strategy=_strategy(),
            risk_limits=_risk_limits(),
            execution_policy=_execution_policy(),
            trigger_snapshot_hash="abc",
            data_hash="def",
            sector_map={},
        )
        check_ids = [c["check_id"] for c in checks]
        assert "SPREAD_OK_AT_PLANNING" not in check_ids

    def test_passes_when_all_spreads_ok(self):
        checks = run_risk_checks(**self._base_checks_kwargs(
            proposed=[self._order("AAPL")],
            spreads={"AAPL": {"spread_pct": 0.001}},
        ))
        spread_check = next(c for c in checks if c["check_id"] == "SPREAD_OK_AT_PLANNING")
        assert spread_check["passes"] is True

    def test_fails_when_wide_spread_in_proposed(self):
        checks = run_risk_checks(**self._base_checks_kwargs(
            proposed=[self._order("AMD")],
            spreads={"AMD": {"spread_pct": 0.10}},
        ))
        spread_check = next(c for c in checks if c["check_id"] == "SPREAD_OK_AT_PLANNING")
        assert spread_check["passes"] is False
        assert "AMD" in spread_check["detail"]

    def test_passes_when_proposed_orders_empty(self):
        checks = run_risk_checks(**self._base_checks_kwargs(
            proposed=[],
            spreads={"AMD": {"spread_pct": 0.10}},
        ))
        spread_check = next(c for c in checks if c["check_id"] == "SPREAD_OK_AT_PLANNING")
        assert spread_check["passes"] is True

    def test_passes_in_full_plan_after_filtering(self):
        selected = ["AAPL", "AMD"]
        spreads = {
            "AAPL": {"spread_pct": 0.001},
            "AMD": {"spread_pct": 0.05},
        }
        plan = _build_plan(selected, spreads)
        risk_checks = {c["check_id"]: c for c in plan["risk_checks"]}
        assert "SPREAD_OK_AT_PLANNING" in risk_checks
        assert risk_checks["SPREAD_OK_AT_PLANNING"]["passes"] is True
