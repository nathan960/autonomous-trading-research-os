"""Tests for trading_os.planning: allocator, position_sizer, and trade_plan_builder."""
from __future__ import annotations

import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trading_os.planning.allocator import compute_targets, _iterative_cap
from trading_os.planning.position_sizer import compute_proposed_orders, _position_value
from trading_os.planning.trade_plan_builder import build_trade_plan
from trading_os.time_utils import utc_now_iso

# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

_BASE_DATE = date(2020, 1, 2)

def _make_bars(closes: list) -> list:
    return [
        {
            "timestamp": f"{(_BASE_DATE + timedelta(days=i)).isoformat()}T00:00:00Z",
            "close": c, "high": c + 2, "low": c - 2, "open": c, "volume": 1_000_000,
        }
        for i, c in enumerate(closes)
    ]


def _rising_closes(n: int = 320) -> list:
    return [100.0 + i * 0.4 for i in range(n)]


def _strategy(
    equity_alloc: float = 0.9,
    max_pos_weight: float = 0.35,   # generous cap so 3-symbol tests don't all hit the cap
    min_atr_floor: float = 0.01,
    max_holdings: int = 10,
    max_names_per_sector: int = 2,
    expiry_minutes: float = 360,
) -> dict:
    return {
        "trading_mode": "paper_only",
        "asset_policy": {"benchmark_symbol": "SPY"},
        "parameters": {
            "max_holdings": max_holdings,
            "max_position_weight": max_pos_weight,
            "max_names_per_sector": max_names_per_sector,
            "risk_on_equity_alloc": equity_alloc,
            "min_atr_pct_floor": min_atr_floor,
            "sma_period": 200,
            "roc_6m_period": 126,
            "roc_12m_period": 252,
            "min_momentum_6m": 0.0,
            "min_momentum_12m": 0.0,
            "atr_period": 20,
            "max_snapshot_age_minutes": 90,
            "max_quote_spread_pct": 0.02,
            "plan_expiry_minutes": expiry_minutes,
            "min_order_notional": 25.0,
        },
        "fallbacks": {
            "risk_off_target": {"symbol": "BIL", "weight": 1.0},
            "risk_on_no_candidates_target": {"symbol": "SPY", "weight": 1.0},
            "risk_on_no_candidates_reason": "no_candidates_ready",
        },
    }


def _risk_limits() -> dict:
    return {
        "live_trading_allowed": False,
        "max_holdings": 10,
        "max_position_weight": 0.12,
        "max_names_per_sector": 2,
        "min_order_notional": 25.0,
        "max_quote_spread_pct": 0.02,
        "allowed_fallbacks": ["BIL", "SPY"],
        "block_symbols": [],
    }


def _execution_policy() -> dict:
    return {
        "paper_only": True,
        "allow_options": False,
        "allow_crypto": False,
        "allow_shorting": False,
    }


def _sector_map(symbols: list) -> dict:
    codes = {"AAPL": 101, "MSFT": 101, "GOOGL": 102, "AMZN": 103, "META": 102}
    return {sym: {"sector": "Tech", "sector_code": codes.get(sym, 199)} for sym in symbols}


def _sym_result(atr_pct: float = 0.02, latest_close: float = 150.0) -> dict:
    return {"atr": {"atr_pct": atr_pct, "latest_close": latest_close, "is_ready": True}}


def _symbol_results(symbols: list) -> dict:
    return {sym: _sym_result(atr_pct=0.02 + i * 0.001, latest_close=100.0 + i * 10) for i, sym in enumerate(symbols)}


def _market_snapshot(symbols: list) -> dict:
    bars: dict = {}
    for sym in symbols + ["SPY", "BIL"]:
        bars[sym] = _make_bars(_rising_closes())
    return {
        "generated_at": utc_now_iso(),
        "bars": bars,
        "spreads": {sym: {"spread_pct": 0.001} for sym in symbols},
        "source_data_hash": "testhash123",
    }


def _account_snapshot(equity: float = 40000.0) -> dict:
    return {
        "account": {"equity": str(equity), "cash": str(equity), "buying_power": str(equity), "status": "ACTIVE"},
        "clock": {"is_open": True, "timestamp": utc_now_iso()},
        "fetched_at": utc_now_iso(),
        "position_count": 0,
    }


def _trigger_snapshot(selected: list, risk_on: bool = True) -> dict:
    now = utc_now_iso()
    return {
        "scanned_at": now,
        "data_stale_gate": {"passes": True, "age_minutes": 5.0},
        "regime": {"risk_on": risk_on, "skip_reason": None, "trigger_id": "SPY_REGIME_200DMA_V1"},
        "selected": selected,
        "symbol_results": _symbol_results(selected),
        "candidates": selected,
        "excluded": [],
        "sector_counts": {},
        "trigger_snapshot_hash": "snapshothashabc123",
    }


# ===========================================================================
# allocator
# ===========================================================================

class TestIterativeCap:
    def test_no_cap_needed(self):
        w = {"A": 0.08, "B": 0.07}
        result = _iterative_cap(w, 0.12)
        assert abs(result["A"] - 0.08) < 1e-9
        assert abs(result["B"] - 0.07) < 1e-9

    def test_single_symbol_capped(self):
        w = {"A": 0.20}
        result = _iterative_cap(w, 0.12)
        assert result["A"] <= 0.12 + 1e-9

    def test_excess_redistributed(self):
        w = {"A": 0.20, "B": 0.05}
        result = _iterative_cap(w, 0.12)
        assert result["A"] <= 0.12 + 1e-9
        assert result["B"] >= 0.05  # received some excess

    def test_all_capped_no_overflow(self):
        w = {"A": 0.20, "B": 0.20, "C": 0.20}
        result = _iterative_cap(w, 0.12)
        for v in result.values():
            assert v <= 0.12 + 1e-9


class TestComputeTargets:
    def test_risk_off_returns_bil(self):
        t = compute_targets([], {}, _strategy(), risk_on=False, equity=40000)
        assert "BIL" in t
        assert t["BIL"]["weight"] == 1.0
        assert t["BIL"]["reason"] == "regime_risk_off"

    def test_risk_off_bil_notional_equals_equity(self):
        equity = 40000.0
        t = compute_targets([], {}, _strategy(), risk_on=False, equity=equity)
        assert abs(t["BIL"]["notional"] - equity) < 0.01

    def test_risk_on_no_candidates_returns_spy(self):
        t = compute_targets([], {}, _strategy(), risk_on=True, equity=40000)
        assert "SPY" in t
        assert t["SPY"]["reason"] == "no_candidates_ready"

    def test_risk_on_with_candidates_returns_targets(self):
        selected = ["AAPL", "MSFT"]
        sym_results = _symbol_results(selected)
        t = compute_targets(selected, sym_results, _strategy(), risk_on=True, equity=40000)
        assert "AAPL" in t
        assert "MSFT" in t

    def test_risk_on_equity_targets_sum_to_equity_alloc_when_no_capping(self):
        # 10 symbols with equal ATR → each gets 0.9/10=0.09, below max 0.12 → no capping
        selected = [f"SYM{i}" for i in range(10)]
        sym_results = {sym: _sym_result(atr_pct=0.02, latest_close=100.0) for sym in selected}
        equity_alloc = 0.9
        t = compute_targets(selected, sym_results, _strategy(equity_alloc=equity_alloc, max_pos_weight=0.12), risk_on=True, equity=40000)
        equity_weight = sum(v["weight"] for k, v in t.items() if k not in ("BIL", "SPY"))
        assert abs(equity_weight - equity_alloc) < 0.01

    def test_risk_on_equity_targets_capped_when_few_symbols(self):
        # 3 symbols: inverse ATR gives 0.3 each, exceeds max 0.12 → all capped → equity < alloc
        selected = ["AAPL", "MSFT", "GOOGL"]
        sym_results = _symbol_results(selected)
        equity_alloc = 0.9
        t = compute_targets(selected, sym_results, _strategy(equity_alloc=equity_alloc, max_pos_weight=0.12), risk_on=True, equity=40000)
        equity_weight = sum(v["weight"] for k, v in t.items() if k not in ("BIL", "SPY"))
        # With 3 symbols capped at 0.12, equity portion is 0.36; rest goes to BIL
        assert equity_weight <= equity_alloc + 1e-6
        total = sum(v["weight"] for v in t.values())
        assert abs(total - 1.0) < 1e-6  # total including BIL must be 1.0

    def test_total_weights_sum_to_one(self):
        selected = ["AAPL", "MSFT"]
        sym_results = _symbol_results(selected)
        t = compute_targets(selected, sym_results, _strategy(), risk_on=True, equity=40000)
        total = sum(v["weight"] for v in t.values())
        assert abs(total - 1.0) < 1e-6

    def test_no_weight_exceeds_max_position_weight(self):
        selected = ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]
        sym_results = _symbol_results(selected)
        max_w = 0.12
        t = compute_targets(selected, sym_results, _strategy(max_pos_weight=max_w), risk_on=True, equity=40000)
        for sym, entry in t.items():
            if sym not in ("BIL", "SPY"):
                assert entry["weight"] <= max_w + 1e-6, f"{sym} weight {entry['weight']} > {max_w}"

    def test_reason_is_risk_on_inverse_atr(self):
        selected = ["AAPL", "MSFT"]
        t = compute_targets(selected, _symbol_results(selected), _strategy(), risk_on=True, equity=40000)
        for sym in selected:
            assert t[sym]["reason"] == "risk_on_inverse_atr"

    def test_bil_in_targets_for_cash_remainder(self):
        selected = ["AAPL", "MSFT"]
        t = compute_targets(selected, _symbol_results(selected), _strategy(equity_alloc=0.9), risk_on=True, equity=40000)
        assert "BIL" in t
        assert t["BIL"]["reason"] == "cash_allocation"

    def test_missing_atr_uses_floor(self):
        selected = ["AAPL"]
        sym_results = {"AAPL": {"atr": {"atr_pct": None, "latest_close": 100.0, "is_ready": False}}}
        t = compute_targets(selected, sym_results, _strategy(min_atr_floor=0.01), risk_on=True, equity=40000)
        assert "AAPL" in t
        assert t["AAPL"]["weight"] > 0

    def test_notional_equals_weight_times_equity(self):
        selected = ["AAPL", "MSFT"]
        equity = 50000.0
        t = compute_targets(selected, _symbol_results(selected), _strategy(), risk_on=True, equity=equity)
        for sym, entry in t.items():
            expected = round(entry["weight"] * equity, 2)
            assert abs(entry["notional"] - expected) < 0.01, f"{sym}"


# ===========================================================================
# position_sizer
# ===========================================================================

class TestPositionValue:
    def test_returns_zero_for_missing_symbol(self):
        assert _position_value([], "AAPL") == 0.0

    def test_returns_value_for_held_symbol(self):
        positions = [{"symbol": "AAPL", "market_value": "5000.00"}]
        assert abs(_position_value(positions, "AAPL") - 5000.0) < 0.01

    def test_handles_string_market_value(self):
        positions = [{"symbol": "MSFT", "market_value": "3500.50"}]
        assert abs(_position_value(positions, "MSFT") - 3500.50) < 0.01


class TestComputeProposedOrders:
    def _targets(self, syms: list, weight: float = 0.09) -> dict:
        return {sym: {"weight": weight, "notional": weight * 40000, "latest_close": 100.0} for sym in syms}

    def test_returns_buy_for_new_position(self):
        t = self._targets(["AAPL"])
        orders = compute_proposed_orders(t, 40000, [], 25.0)
        buy = next(o for o in orders if o["symbol"] == "AAPL")
        assert buy["side"] == "buy"

    def test_returns_sell_for_exit(self):
        t = {}  # not targeting AAPL
        positions = [{"symbol": "AAPL", "market_value": "5000.00"}]
        orders = compute_proposed_orders(t, 40000, positions, 25.0)
        sell = next((o for o in orders if o["symbol"] == "AAPL"), None)
        assert sell is not None
        assert sell["side"] == "sell"

    def test_would_short_flagged_when_no_position(self):
        # Target weight 0 but symbol not in positions → would_short
        t = {"AAPL": {"weight": -0.01, "notional": -400.0, "latest_close": 100.0}}
        orders = compute_proposed_orders(t, 40000, [], 25.0)
        aapl = next(o for o in orders if o["symbol"] == "AAPL")
        # delta is negative, current_value is 0 → would_short
        if aapl["delta_value"] < 0 and aapl["current_value"] == 0:
            assert aapl["would_short"] is True
            assert aapl["skip_reason"] is not None

    def test_below_min_notional_gets_skip_reason(self):
        t = {"AAPL": {"weight": 0.0001, "notional": 4.0, "latest_close": 100.0}}
        orders = compute_proposed_orders(t, 40000, [], 25.0)
        aapl = next(o for o in orders if o["symbol"] == "AAPL")
        assert aapl["skip_reason"] is not None
        assert "below_min_notional" in aapl["skip_reason"]

    def test_actionable_orders_have_null_skip_reason(self):
        t = self._targets(["AAPL", "MSFT"])
        orders = compute_proposed_orders(t, 40000, [], 25.0)
        for o in orders:
            assert o["skip_reason"] is None

    def test_limit_order_when_price_available(self):
        t = {"AAPL": {"weight": 0.09, "notional": 3600, "latest_close": 150.0}}
        orders = compute_proposed_orders(t, 40000, [], 25.0)
        aapl = next(o for o in orders if o["symbol"] == "AAPL")
        assert aapl["order_type"] == "limit"
        assert aapl["limit_price"] == 150.0

    def test_blocked_when_no_price(self):
        t = {"BIL": {"weight": 0.1, "notional": 4000, "latest_close": None}}
        orders = compute_proposed_orders(t, 40000, [], 25.0)
        bil = next(o for o in orders if o["symbol"] == "BIL")
        assert bil["order_type"] == "limit"
        assert bil["limit_price"] is None
        assert bil["skip_reason"] == "no_limit_price_source"

    def test_order_has_required_fields(self):
        t = self._targets(["AAPL"])
        orders = compute_proposed_orders(t, 40000, [], 25.0)
        required = {"symbol", "side", "order_type", "limit_price", "notional",
                    "target_weight", "current_value", "target_value",
                    "delta_value", "would_short", "skip_reason"}
        for o in orders:
            assert required.issubset(set(o.keys()))

    def test_no_orders_when_already_at_target(self):
        t = {"AAPL": {"weight": 0.09, "notional": 3600, "latest_close": 150.0}}
        positions = [{"symbol": "AAPL", "market_value": "3600.00"}]
        orders = compute_proposed_orders(t, 40000, positions, 25.0)
        aapl = next((o for o in orders if o["symbol"] == "AAPL"), None)
        # delta ≈ 0 → below min notional → skipped
        if aapl:
            assert aapl["skip_reason"] is not None


# ===========================================================================
# trade_plan_builder
# ===========================================================================

class TestBuildTradePlan:
    def _build(self, selected: list = None, risk_on: bool = True, equity: float = 40000.0, approve_paper: bool = False) -> dict:
        syms = selected if selected is not None else ["AAPL", "MSFT", "GOOGL"]
        ms = _market_snapshot(syms)
        ts = _trigger_snapshot(syms, risk_on=risk_on)
        acct = _account_snapshot(equity)
        return build_trade_plan(
            market_snapshot=ms,
            trigger_snapshot=ts,
            account_snapshot=acct,
            positions=[],
            strategy=_strategy(),
            risk_limits=_risk_limits(),
            execution_policy=_execution_policy(),
            sector_map=_sector_map(syms),
            approve_paper=approve_paper,
        )

    # ── Required fields ──────────────────────────────────────────────────────
    def test_required_top_level_keys(self):
        plan = self._build()
        required = {
            "plan_id", "generated_at", "expires_at", "trading_mode",
            "strategy_hash", "data_hash", "trigger_snapshot_hash",
            "account_snapshot", "market_clock", "regime",
            "targets", "proposed_orders", "blocked_symbols",
            "risk_checks", "no_trade_reasons", "approval", "trade_plan_hash",
        }
        assert required.issubset(set(plan.keys()))

    def test_trading_mode_is_paper(self):
        assert self._build()["trading_mode"] == "paper"

    def test_approval_has_approved_for_execution(self):
        plan = self._build()
        assert "approved_for_execution" in plan["approval"]

    def test_approved_for_execution_false_without_flag(self):
        plan = self._build(approve_paper=False)
        assert plan["approval"]["approved_for_execution"] is False

    def test_approved_for_execution_true_with_flag_and_clean_plan(self):
        plan = self._build(approve_paper=True)
        assert plan["approval"]["approved_for_execution"] is True

    # ── Plan ID and hashes ───────────────────────────────────────────────────
    def test_plan_id_has_prefix(self):
        assert self._build()["plan_id"].startswith("trade_plan-")

    def test_strategy_hash_is_sha256(self):
        plan = self._build()
        assert len(plan["strategy_hash"]) == 64

    def test_trade_plan_hash_is_sha256(self):
        plan = self._build()
        assert len(plan["trade_plan_hash"]) == 64

    def test_trigger_snapshot_hash_propagated(self):
        plan = self._build()
        assert plan["trigger_snapshot_hash"] == "snapshothashabc123"

    # ── Targets ──────────────────────────────────────────────────────────────
    def test_risk_off_targets_bil(self):
        plan = self._build(selected=[], risk_on=False)
        assert "BIL" in plan["targets"]
        assert plan["targets"]["BIL"]["reason"] == "regime_risk_off"

    def test_risk_on_targets_include_selected(self):
        plan = self._build(selected=["AAPL", "MSFT"])
        assert "AAPL" in plan["targets"]
        assert "MSFT" in plan["targets"]

    def test_risk_on_targets_include_bil_remainder(self):
        plan = self._build(selected=["AAPL", "MSFT"])
        assert "BIL" in plan["targets"]

    # ── Orders ───────────────────────────────────────────────────────────────
    def test_proposed_orders_present(self):
        plan = self._build()
        assert isinstance(plan["proposed_orders"], list)

    def test_proposed_orders_have_no_skip_reason(self):
        plan = self._build()
        for o in plan["proposed_orders"]:
            assert o.get("skip_reason") is None

    def test_proposed_orders_no_short_sells(self):
        plan = self._build()
        for o in plan["proposed_orders"]:
            assert o.get("would_short") is False

    # ── Risk checks ──────────────────────────────────────────────────────────
    def test_risk_checks_present(self):
        plan = self._build()
        assert isinstance(plan["risk_checks"], list)
        assert len(plan["risk_checks"]) > 0

    def test_all_risk_checks_pass_clean_plan(self):
        plan = self._build()
        failed = [c["check_id"] for c in plan["risk_checks"] if not c["passes"]]
        assert failed == [], f"Failed checks: {failed}"

    # ── Account snapshot ─────────────────────────────────────────────────────
    def test_account_snapshot_in_plan(self):
        plan = self._build(equity=50000.0)
        acct = plan["account_snapshot"]
        assert acct.get("equity") is not None

    # ── No-trade plan ────────────────────────────────────────────────────────
    def test_stale_data_creates_no_trade_plan(self):
        syms = ["AAPL"]
        ms = _market_snapshot(syms)
        # Trigger snapshot with failed stale gate
        ts = _trigger_snapshot(syms, risk_on=True)
        ts["data_stale_gate"] = {"passes": False, "skip_reason": "snapshot_stale(...)"}
        ts["selected"] = []
        acct = _account_snapshot()
        plan = build_trade_plan(
            market_snapshot=ms, trigger_snapshot=ts, account_snapshot=acct,
            positions=[], strategy=_strategy(), risk_limits=_risk_limits(),
            execution_policy=_execution_policy(), sector_map=_sector_map(syms),
        )
        assert len(plan["no_trade_reasons"]) > 0
        assert plan["approval"]["approved_for_execution"] is False

    def test_no_trade_plan_is_still_valid_plan(self):
        syms = ["AAPL"]
        ms = _market_snapshot(syms)
        ts = _trigger_snapshot(syms, risk_on=True)
        ts["data_stale_gate"] = {"passes": False, "skip_reason": "stale"}
        ts["selected"] = []
        plan = build_trade_plan(
            market_snapshot=ms, trigger_snapshot=ts,
            account_snapshot=_account_snapshot(), positions=[],
            strategy=_strategy(), risk_limits=_risk_limits(),
            execution_policy=_execution_policy(), sector_map=_sector_map(syms),
        )
        required = {"plan_id", "generated_at", "expires_at", "trading_mode", "approval"}
        assert required.issubset(set(plan.keys()))

    # ── Blocked symbols ──────────────────────────────────────────────────────
    def test_blocked_symbols_is_list(self):
        plan = self._build()
        assert isinstance(plan["blocked_symbols"], list)

    def test_trigger_excluded_appear_in_blocked(self):
        syms = ["AAPL", "MSFT"]
        ms = _market_snapshot(syms)
        ts = _trigger_snapshot(syms[:1], risk_on=True)
        ts["excluded"] = [{"symbol": "MSFT", "skip_reason": "trend_filter_failed"}]
        plan = build_trade_plan(
            market_snapshot=ms, trigger_snapshot=ts,
            account_snapshot=_account_snapshot(), positions=[],
            strategy=_strategy(), risk_limits=_risk_limits(),
            execution_policy=_execution_policy(), sector_map=_sector_map(syms),
        )
        blocked_syms = {b["symbol"] for b in plan["blocked_symbols"]}
        assert "MSFT" in blocked_syms
