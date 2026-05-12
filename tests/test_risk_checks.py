"""Tests for src/trading_os/planning/risk_checks.py"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trading_os.planning.risk_checks import all_checks_pass, run_risk_checks


# ---------------------------------------------------------------------------
# Fixtures / helpers
# ---------------------------------------------------------------------------

def _strategy(
    trading_mode: str = "paper_only",
    max_holdings: int = 10,
    max_pos_weight: float = 0.12,
    max_names_per_sector: int = 2,
    min_order_notional: float = 25.0,
    equity_alloc: float = 0.9,
) -> dict:
    return {
        "trading_mode": trading_mode,
        "parameters": {
            "max_holdings": max_holdings,
            "max_position_weight": max_pos_weight,
            "max_names_per_sector": max_names_per_sector,
            "min_order_notional": min_order_notional,
            "risk_on_equity_alloc": equity_alloc,
        },
        "fallbacks": {
            "risk_off_target": {"symbol": "BIL", "weight": 1.0},
            "risk_on_no_candidates_target": {"symbol": "SPY", "weight": 1.0},
        },
    }


def _risk_limits(live_trading: bool = False, allowed_fallbacks: list | None = None, block_symbols: list | None = None) -> dict:
    return {
        "live_trading_allowed": live_trading,
        "allowed_fallbacks": allowed_fallbacks or ["BIL", "SPY"],
        "block_symbols": block_symbols or [],
    }


def _execution_policy(paper_only: bool = True, allow_options: bool = False, allow_crypto: bool = False, allow_shorting: bool = False) -> dict:
    return {
        "paper_only": paper_only,
        "allow_options": allow_options,
        "allow_crypto": allow_crypto,
        "allow_shorting": allow_shorting,
    }


def _targets(symbols: list, weight: float = 0.09, include_bil: bool = True) -> dict:
    result = {sym: {"weight": weight, "notional": weight * 40000} for sym in symbols}
    if include_bil:
        result["BIL"] = {"weight": round(1.0 - weight * len(symbols), 8), "notional": 0}
    return result


def _order(symbol: str, notional: float = 3600.0, would_short: bool = False, skip_reason: str | None = None) -> dict:
    return {
        "symbol": symbol,
        "side": "buy" if not would_short else "sell",
        "order_type": "limit",
        "limit_price": 100.0,
        "notional": notional,
        "target_weight": 0.09,
        "current_value": 0.0,
        "target_value": notional,
        "delta_value": notional,
        "would_short": would_short,
        "skip_reason": skip_reason,
    }


def _sector_map(symbols: list, sector_code: int = 101) -> dict:
    return {sym: {"sector": "Technology", "sector_code": sector_code} for sym in symbols}


def _run(
    symbols: list | None = None,
    orders: list | None = None,
    strat: dict | None = None,
    rl: dict | None = None,
    ep: dict | None = None,
    sector_map: dict | None = None,
    tsh: str = "abc123",
    dh: str = "def456",
) -> list:
    syms = symbols or ["AAPL", "MSFT"]
    return run_risk_checks(
        targets=_targets(syms),
        proposed_orders=orders if orders is not None else [_order(s) for s in syms],
        strategy=strat or _strategy(),
        risk_limits=rl or _risk_limits(),
        execution_policy=ep or _execution_policy(),
        trigger_snapshot_hash=tsh,
        data_hash=dh,
        sector_map=sector_map or _sector_map(syms),
    )


# ---------------------------------------------------------------------------
# all_checks_pass
# ---------------------------------------------------------------------------

class TestAllChecksPass:
    def test_all_pass_returns_true(self):
        checks = [{"check_id": "X", "passes": True, "detail": None}] * 5
        assert all_checks_pass(checks) is True

    def test_one_fail_returns_false(self):
        checks = [
            {"check_id": "X", "passes": True, "detail": None},
            {"check_id": "Y", "passes": False, "detail": "oops"},
        ]
        assert all_checks_pass(checks) is False

    def test_empty_list_returns_true(self):
        assert all_checks_pass([]) is True


# ---------------------------------------------------------------------------
# run_risk_checks: return structure
# ---------------------------------------------------------------------------

class TestRunRiskChecksStructure:
    def test_returns_list(self):
        assert isinstance(_run(), list)

    def test_each_check_has_required_keys(self):
        for check in _run():
            assert "check_id" in check
            assert "passes" in check
            assert "detail" in check

    def test_check_ids_are_strings(self):
        for check in _run():
            assert isinstance(check["check_id"], str)

    def test_passes_are_bool(self):
        for check in _run():
            assert isinstance(check["passes"], bool)

    def test_detail_none_when_passes(self):
        checks = _run()
        for c in checks:
            if c["passes"]:
                assert c["detail"] is None


# ---------------------------------------------------------------------------
# run_risk_checks: fundamental mode gates
# ---------------------------------------------------------------------------

class TestFundamentalModeGates:
    def test_paper_only_strategy_passes(self):
        checks = {c["check_id"]: c for c in _run(strat=_strategy(trading_mode="paper_only"))}
        assert checks["TRADING_MODE_PAPER"]["passes"] is True

    def test_live_strategy_fails_trading_mode(self):
        checks = {c["check_id"]: c for c in _run(strat=_strategy(trading_mode="live"))}
        assert checks["TRADING_MODE_PAPER"]["passes"] is False

    def test_no_live_trading_passes_when_false(self):
        checks = {c["check_id"]: c for c in _run(rl=_risk_limits(live_trading=False))}
        assert checks["NO_LIVE_TRADING"]["passes"] is True

    def test_no_live_trading_fails_when_true(self):
        checks = {c["check_id"]: c for c in _run(rl=_risk_limits(live_trading=True))}
        assert checks["NO_LIVE_TRADING"]["passes"] is False

    def test_paper_only_policy_passes(self):
        checks = {c["check_id"]: c for c in _run(ep=_execution_policy(paper_only=True))}
        assert checks["PAPER_ONLY_POLICY"]["passes"] is True

    def test_non_paper_policy_fails(self):
        checks = {c["check_id"]: c for c in _run(ep=_execution_policy(paper_only=False))}
        assert checks["PAPER_ONLY_POLICY"]["passes"] is False


# ---------------------------------------------------------------------------
# Data provenance
# ---------------------------------------------------------------------------

class TestDataProvenance:
    def test_data_hash_present_passes(self):
        checks = {c["check_id"]: c for c in _run(dh="somehash")}
        assert checks["DATA_HASH_PRESENT"]["passes"] is True

    def test_data_hash_empty_fails(self):
        checks = {c["check_id"]: c for c in _run(dh="")}
        assert checks["DATA_HASH_PRESENT"]["passes"] is False

    def test_trigger_hash_present_passes(self):
        checks = {c["check_id"]: c for c in _run(tsh="somehash")}
        assert checks["TRIGGER_SNAPSHOT_PRESENT"]["passes"] is True

    def test_trigger_hash_empty_fails(self):
        checks = {c["check_id"]: c for c in _run(tsh="")}
        assert checks["TRIGGER_SNAPSHOT_PRESENT"]["passes"] is False


# ---------------------------------------------------------------------------
# Asset class / instrument policy
# ---------------------------------------------------------------------------

class TestAssetClassPolicy:
    def test_no_options_passes_when_disabled(self):
        checks = {c["check_id"]: c for c in _run(ep=_execution_policy(allow_options=False))}
        assert checks["NO_OPTIONS"]["passes"] is True

    def test_no_options_fails_when_enabled(self):
        checks = {c["check_id"]: c for c in _run(ep=_execution_policy(allow_options=True))}
        assert checks["NO_OPTIONS"]["passes"] is False

    def test_no_crypto_passes_when_disabled(self):
        checks = {c["check_id"]: c for c in _run(ep=_execution_policy(allow_crypto=False))}
        assert checks["NO_CRYPTO"]["passes"] is True

    def test_no_crypto_fails_when_enabled(self):
        checks = {c["check_id"]: c for c in _run(ep=_execution_policy(allow_crypto=True))}
        assert checks["NO_CRYPTO"]["passes"] is False

    def test_no_shorting_passes_when_disabled(self):
        checks = {c["check_id"]: c for c in _run(ep=_execution_policy(allow_shorting=False))}
        assert checks["NO_SHORTING"]["passes"] is True

    def test_no_shorting_fails_when_enabled(self):
        checks = {c["check_id"]: c for c in _run(ep=_execution_policy(allow_shorting=True))}
        assert checks["NO_SHORTING"]["passes"] is False


# ---------------------------------------------------------------------------
# Short-sell detection
# ---------------------------------------------------------------------------

class TestShortSellDetection:
    def test_no_short_sells_passes_with_clean_orders(self):
        syms = ["AAPL", "MSFT"]
        orders = [_order(s, would_short=False) for s in syms]
        checks = {c["check_id"]: c for c in _run(symbols=syms, orders=orders)}
        assert checks["NO_SHORT_SELLS_IN_ORDERS"]["passes"] is True

    def test_short_sell_detected_fails(self):
        syms = ["AAPL"]
        orders = [_order("AAPL", would_short=True)]
        checks = {c["check_id"]: c for c in _run(symbols=syms, orders=orders)}
        assert checks["NO_SHORT_SELLS_IN_ORDERS"]["passes"] is False


# ---------------------------------------------------------------------------
# Holdings limits
# ---------------------------------------------------------------------------

class TestHoldingsLimits:
    def test_within_max_holdings_passes(self):
        syms = ["AAPL", "MSFT", "GOOGL"]
        checks = {c["check_id"]: c for c in _run(symbols=syms, strat=_strategy(max_holdings=10))}
        assert checks["MAX_HOLDINGS"]["passes"] is True

    def test_exceeds_max_holdings_fails(self):
        syms = [f"SYM{i}" for i in range(5)]
        checks = {c["check_id"]: c for c in _run(symbols=syms, strat=_strategy(max_holdings=3))}
        assert checks["MAX_HOLDINGS"]["passes"] is False


# ---------------------------------------------------------------------------
# Weight limits
# ---------------------------------------------------------------------------

class TestWeightLimits:
    def test_within_max_position_weight_passes(self):
        # BIL is a fallback symbol and exempt; AAPL at 0.10 is within 0.12 cap
        targets = {"AAPL": {"weight": 0.10, "notional": 4000}, "BIL": {"weight": 0.90, "notional": 36000}}
        checks = {c["check_id"]: c for c in run_risk_checks(
            targets=targets, proposed_orders=[], strategy=_strategy(max_pos_weight=0.12),
            risk_limits=_risk_limits(), execution_policy=_execution_policy(),
            trigger_snapshot_hash="x", data_hash="y", sector_map={"AAPL": {"sector_code": 101}}
        )}
        assert checks["MAX_POSITION_WEIGHT"]["passes"] is True

    def test_exceeds_max_position_weight_fails(self):
        # AAPL at 0.20 exceeds 0.12 (not a fallback symbol)
        targets = {"AAPL": {"weight": 0.20, "notional": 8000}, "BIL": {"weight": 0.80, "notional": 32000}}
        checks = {c["check_id"]: c for c in run_risk_checks(
            targets=targets, proposed_orders=[], strategy=_strategy(max_pos_weight=0.12),
            risk_limits=_risk_limits(), execution_policy=_execution_policy(),
            trigger_snapshot_hash="x", data_hash="y", sector_map={"AAPL": {"sector_code": 101}}
        )}
        assert checks["MAX_POSITION_WEIGHT"]["passes"] is False

    def test_total_weight_at_1_passes(self):
        targets = {"AAPL": {"weight": 0.5, "notional": 20000}, "BIL": {"weight": 0.5, "notional": 20000}}
        checks = {c["check_id"]: c for c in run_risk_checks(
            targets=targets, proposed_orders=[], strategy=_strategy(),
            risk_limits=_risk_limits(), execution_policy=_execution_policy(),
            trigger_snapshot_hash="x", data_hash="y", sector_map={}
        )}
        assert checks["TOTAL_WEIGHT_LIMIT"]["passes"] is True

    def test_total_weight_above_1_01_fails(self):
        targets = {"AAPL": {"weight": 0.6, "notional": 24000}, "MSFT": {"weight": 0.6, "notional": 24000}}
        checks = {c["check_id"]: c for c in run_risk_checks(
            targets=targets, proposed_orders=[], strategy=_strategy(),
            risk_limits=_risk_limits(), execution_policy=_execution_policy(),
            trigger_snapshot_hash="x", data_hash="y", sector_map={"AAPL": {"sector_code": 1}, "MSFT": {"sector_code": 2}}
        )}
        assert checks["TOTAL_WEIGHT_LIMIT"]["passes"] is False


# ---------------------------------------------------------------------------
# Sector caps
# ---------------------------------------------------------------------------

class TestSectorCaps:
    def test_sector_within_cap_passes(self):
        syms = ["AAPL", "MSFT"]
        checks = {c["check_id"]: c for c in _run(symbols=syms, strat=_strategy(max_names_per_sector=2), sector_map=_sector_map(syms, 101))}
        assert checks["SECTOR_CAPS_OK"]["passes"] is True

    def test_sector_exceeds_cap_fails(self):
        syms = ["AAPL", "MSFT", "GOOGL"]
        all_same_sector = {sym: {"sector": "Tech", "sector_code": 101} for sym in syms}
        checks = {c["check_id"]: c for c in _run(symbols=syms, strat=_strategy(max_names_per_sector=2), sector_map=all_same_sector)}
        assert checks["SECTOR_CAPS_OK"]["passes"] is False


# ---------------------------------------------------------------------------
# Blocked symbols
# ---------------------------------------------------------------------------

class TestBlockedSymbols:
    def test_no_blocked_passes_when_empty_blocklist(self):
        checks = {c["check_id"]: c for c in _run(rl=_risk_limits(block_symbols=[]))}
        assert checks["NO_BLOCKED_SYMBOLS_IN_TARGETS"]["passes"] is True

    def test_blocked_symbol_in_targets_fails(self):
        syms = ["AAPL", "MSFT"]
        checks = {c["check_id"]: c for c in _run(symbols=syms, rl=_risk_limits(block_symbols=["AAPL"]))}
        assert checks["NO_BLOCKED_SYMBOLS_IN_TARGETS"]["passes"] is False


# ---------------------------------------------------------------------------
# Min order notional
# ---------------------------------------------------------------------------

class TestMinOrderNotional:
    def test_orders_above_min_passes(self):
        syms = ["AAPL"]
        orders = [_order("AAPL", notional=3600.0)]
        checks = {c["check_id"]: c for c in _run(symbols=syms, orders=orders, strat=_strategy(min_order_notional=25.0))}
        assert checks["MIN_ORDER_NOTIONAL"]["passes"] is True

    def test_order_below_min_fails(self):
        # An actionable order (skip_reason=None) with tiny notional
        orders = [{"symbol": "AAPL", "notional": 10.0, "would_short": False, "skip_reason": None}]
        targets = {"AAPL": {"weight": 0.09, "notional": 10.0}}
        checks = {c["check_id"]: c for c in run_risk_checks(
            targets=targets, proposed_orders=orders, strategy=_strategy(min_order_notional=25.0),
            risk_limits=_risk_limits(), execution_policy=_execution_policy(),
            trigger_snapshot_hash="x", data_hash="y", sector_map=_sector_map(["AAPL"])
        )}
        assert checks["MIN_ORDER_NOTIONAL"]["passes"] is False


# ---------------------------------------------------------------------------
# Happy path: all checks pass
# ---------------------------------------------------------------------------

class TestHappyPath:
    def test_clean_setup_all_checks_pass(self):
        syms = ["AAPL", "MSFT", "GOOGL"]
        orders = [_order(s, notional=3000) for s in syms]
        # Distinct sectors to avoid sector-cap failure
        sector_map = {
            "AAPL": {"sector": "Technology", "sector_code": 101},
            "MSFT": {"sector": "Technology", "sector_code": 101},
            "GOOGL": {"sector": "Communication", "sector_code": 102},
        }
        checks = _run(symbols=syms, orders=orders, sector_map=sector_map)
        assert all_checks_pass(checks) is True, [c for c in checks if not c["passes"]]
