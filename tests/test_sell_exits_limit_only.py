"""Tests: all proposed orders from position_sizer must be limit orders only.

Covers:
- Full-exit sells (positions not in targets) use limit orders when price available.
- Full-exit sells are blocked (skip_reason set) when no price source exists.
- Target-adjustment sells use limit orders.
- Target-adjustment sells are blocked when no latest_close.
- No order_type == "market" ever appears in compute_proposed_orders output.
"""
from __future__ import annotations

import pytest

from trading_os.planning.position_sizer import compute_proposed_orders


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _pos(symbol: str, market_value: float, current_price: float = 0.0, avg_entry_price: float = 0.0) -> dict:
    p: dict = {"symbol": symbol, "market_value": str(market_value)}
    if current_price:
        p["current_price"] = str(current_price)
    if avg_entry_price:
        p["avg_entry_price"] = str(avg_entry_price)
    return p


def _tgt(symbol: str, weight: float, notional: float, latest_close: float | None = 10.0) -> dict:
    t: dict = {"weight": weight, "notional": notional}
    if latest_close is not None:
        t["latest_close"] = latest_close
    return t


def _no_market_orders(orders: list) -> None:
    for o in orders:
        assert o["order_type"] != "market", (
            f"Found market order for {o['symbol']}: {o}"
        )


# ---------------------------------------------------------------------------
# Full-exit sell orders (positions not in targets)
# ---------------------------------------------------------------------------

class TestFullExitSellLimitOnly:
    def test_full_exit_uses_current_price(self):
        positions = [_pos("AMD", 1000.0, current_price=120.50)]
        orders = compute_proposed_orders(targets={}, equity=5000.0, positions=positions)
        assert len(orders) == 1
        o = orders[0]
        assert o["symbol"] == "AMD"
        assert o["side"] == "sell"
        assert o["order_type"] == "limit"
        assert o["limit_price"] == pytest.approx(120.50)
        assert o["skip_reason"] is None

    def test_full_exit_falls_back_to_avg_entry(self):
        positions = [_pos("NVDA", 500.0, avg_entry_price=450.0)]
        orders = compute_proposed_orders(targets={}, equity=5000.0, positions=positions)
        o = orders[0]
        assert o["order_type"] == "limit"
        assert o["limit_price"] == pytest.approx(450.0)
        assert o["skip_reason"] is None

    def test_full_exit_prefers_current_price_over_avg_entry(self):
        positions = [_pos("MSFT", 800.0, current_price=400.0, avg_entry_price=350.0)]
        orders = compute_proposed_orders(targets={}, equity=5000.0, positions=positions)
        o = orders[0]
        assert o["limit_price"] == pytest.approx(400.0)

    def test_full_exit_blocked_when_no_price_source(self):
        positions = [{"symbol": "KO", "market_value": "600.0"}]
        orders = compute_proposed_orders(targets={}, equity=5000.0, positions=positions)
        o = orders[0]
        assert o["order_type"] == "limit"
        assert o["limit_price"] is None
        assert o["skip_reason"] == "no_limit_price_source"

    def test_full_exit_blocked_when_price_is_zero(self):
        positions = [_pos("MRK", 300.0, current_price=0.0, avg_entry_price=0.0)]
        orders = compute_proposed_orders(targets={}, equity=5000.0, positions=positions)
        o = orders[0]
        assert o["limit_price"] is None
        assert o["skip_reason"] == "no_limit_price_source"

    def test_full_exit_blocked_when_price_is_negative(self):
        positions = [{"symbol": "PEP", "market_value": "400.0", "current_price": "-5.0"}]
        orders = compute_proposed_orders(targets={}, equity=5000.0, positions=positions)
        o = orders[0]
        assert o["limit_price"] is None
        assert o["skip_reason"] == "no_limit_price_source"

    def test_multiple_full_exits_each_get_correct_limit(self):
        positions = [
            _pos("AAPL", 1000.0, current_price=190.0),
            _pos("GOOG", 2000.0, current_price=170.0),
            {"symbol": "META", "market_value": "500.0"},  # no price
        ]
        orders = compute_proposed_orders(targets={}, equity=10000.0, positions=positions)
        by_sym = {o["symbol"]: o for o in orders}

        assert by_sym["AAPL"]["order_type"] == "limit"
        assert by_sym["AAPL"]["limit_price"] == pytest.approx(190.0)
        assert by_sym["AAPL"]["skip_reason"] is None

        assert by_sym["GOOG"]["order_type"] == "limit"
        assert by_sym["GOOG"]["limit_price"] == pytest.approx(170.0)

        assert by_sym["META"]["order_type"] == "limit"
        assert by_sym["META"]["limit_price"] is None
        assert by_sym["META"]["skip_reason"] == "no_limit_price_source"

    def test_zero_value_position_skipped(self):
        positions = [{"symbol": "XYZ", "market_value": "0.0", "current_price": "100.0"}]
        orders = compute_proposed_orders(targets={}, equity=5000.0, positions=positions)
        assert len(orders) == 0


# ---------------------------------------------------------------------------
# Target-adjustment sells (in targets but trimming position)
# ---------------------------------------------------------------------------

class TestTargetAdjustSellLimitOnly:
    def test_partial_sell_uses_latest_close(self):
        positions = [_pos("SPY", 2000.0)]
        targets = {"SPY": _tgt("SPY", weight=0.1, notional=1000.0, latest_close=450.0)}
        orders = compute_proposed_orders(
            targets=targets, equity=10000.0, positions=positions
        )
        o = orders[0]
        assert o["side"] == "sell"
        assert o["order_type"] == "limit"
        assert o["limit_price"] == pytest.approx(450.0)
        assert o["skip_reason"] is None

    def test_partial_sell_blocked_when_no_latest_close(self):
        positions = [_pos("SPY", 2000.0)]
        targets = {"SPY": _tgt("SPY", weight=0.1, notional=1000.0, latest_close=None)}
        orders = compute_proposed_orders(
            targets=targets, equity=10000.0, positions=positions
        )
        o = orders[0]
        assert o["order_type"] == "limit"
        assert o["limit_price"] is None
        assert o["skip_reason"] == "no_limit_price_source"


# ---------------------------------------------------------------------------
# Buy orders (must also be limit-only)
# ---------------------------------------------------------------------------

class TestBuyOrdersLimitOnly:
    def test_buy_order_with_latest_close_is_limit(self):
        targets = {"AAPL": _tgt("AAPL", weight=0.2, notional=2000.0, latest_close=185.0)}
        orders = compute_proposed_orders(targets=targets, equity=10000.0, positions=[])
        o = orders[0]
        assert o["side"] == "buy"
        assert o["order_type"] == "limit"
        assert o["limit_price"] == pytest.approx(185.0)
        assert o["skip_reason"] is None

    def test_buy_order_without_latest_close_is_blocked(self):
        targets = {"AAPL": _tgt("AAPL", weight=0.2, notional=2000.0, latest_close=None)}
        orders = compute_proposed_orders(targets=targets, equity=10000.0, positions=[])
        o = orders[0]
        assert o["order_type"] == "limit"
        assert o["limit_price"] is None
        assert o["skip_reason"] == "no_limit_price_source"


# ---------------------------------------------------------------------------
# Global invariant: no market orders ever
# ---------------------------------------------------------------------------

class TestNoMarketOrdersEver:
    def test_empty_targets_and_positions(self):
        orders = compute_proposed_orders(targets={}, equity=0.0, positions=[])
        _no_market_orders(orders)

    def test_mixed_scenario_no_market_orders(self):
        positions = [
            _pos("AMD", 1000.0, current_price=150.0),
            _pos("NVDA", 500.0),  # no price
            _pos("KO", 300.0, avg_entry_price=60.0),
        ]
        targets = {
            "AAPL": _tgt("AAPL", 0.2, 2000.0, latest_close=190.0),
            "META": _tgt("META", 0.1, 1000.0, latest_close=None),
            "KO": _tgt("KO", 0.05, 500.0, latest_close=62.0),
        }
        orders = compute_proposed_orders(
            targets=targets, equity=10000.0, positions=positions
        )
        _no_market_orders(orders)

    def test_actionable_orders_have_limit_price(self):
        positions = [_pos("SPY", 500.0, current_price=450.0)]
        targets = {"SPY": _tgt("SPY", 0.2, 2000.0, latest_close=451.0)}
        orders = compute_proposed_orders(
            targets=targets, equity=10000.0, positions=positions
        )
        for o in orders:
            if o["skip_reason"] is None:
                assert o["limit_price"] is not None, (
                    f"Actionable order {o['symbol']} has no limit_price"
                )
                assert o["order_type"] == "limit"
