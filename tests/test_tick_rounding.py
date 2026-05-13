"""Tests for src/trading_os/tick_rounding.py and downstream usage.

Proves:
- 1078.765 (EQIX-like price) rounds to a valid 2-decimal tick.
- High-priced equities never produce 3-decimal limit prices.
- Sub-dollar prices round to 4 decimal places.
- Zero / negative / missing prices are blocked.
- position_sizer proposed_orders carry valid tick prices.
- order_builder orders_validated carry valid tick prices.
- paper_executor blocks sub-tick prices before submit_order is called.
"""
from __future__ import annotations

import sys
from decimal import Decimal
from pathlib import Path
from unittest.mock import MagicMock

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trading_os.tick_rounding import round_to_tick, validate_tick_price


# ---------------------------------------------------------------------------
# Helpers shared across test classes
# ---------------------------------------------------------------------------

def _has_at_most_n_decimal_places(value: float, n: int) -> bool:
    d = Decimal(str(value))
    sign, digits, exponent = d.as_tuple()
    decimal_places = max(0, -exponent)
    return decimal_places <= n


# ===========================================================================
# TestRoundToTick
# ===========================================================================

class TestRoundToTick:
    def test_eqix_price_rounds_to_two_decimal(self):
        result = round_to_tick(1078.765, "buy")
        assert result == Decimal("1078.77")

    def test_result_type_is_decimal(self):
        result = round_to_tick(150.0, "buy")
        assert isinstance(result, Decimal)

    def test_already_valid_price_unchanged(self):
        assert round_to_tick(150.00, "buy") == Decimal("150.00")

    def test_three_decimal_buy_rounds_up(self):
        # 100.005 → 100.01 (ROUND_HALF_UP)
        assert round_to_tick(100.005, "buy") == Decimal("100.01")

    def test_three_decimal_sell_also_rounds_half_up(self):
        # Same rule for sell — no side-specific rounding
        assert round_to_tick(100.005, "sell") == Decimal("100.01")

    def test_high_price_no_more_than_two_decimals(self):
        result = float(round_to_tick(1078.765, "buy"))
        assert _has_at_most_n_decimal_places(result, 2)

    def test_another_high_price(self):
        result = float(round_to_tick(999.999, "buy"))
        assert _has_at_most_n_decimal_places(result, 2)

    def test_sub_dollar_rounds_to_four_decimals(self):
        result = round_to_tick(0.99999, "buy")
        assert result == Decimal("1.0000")  # >= 1.00 so 2 decimals after crossing threshold

    def test_sub_dollar_stays_sub_dollar(self):
        result = round_to_tick(0.5001, "buy")
        assert result == Decimal("0.5001")
        assert _has_at_most_n_decimal_places(float(result), 4)

    def test_sub_dollar_five_decimal_rounds_to_four(self):
        result = round_to_tick(0.12345, "buy")
        assert result == Decimal("0.1235")

    def test_sub_dollar_result_no_more_than_four_decimals(self):
        result = float(round_to_tick(0.12345, "buy"))
        assert _has_at_most_n_decimal_places(result, 4)

    def test_exactly_one_dollar_uses_penny_tick(self):
        result = round_to_tick(1.005, "buy")
        assert result == Decimal("1.01")

    def test_zero_raises_value_error(self):
        with pytest.raises(ValueError, match="positive"):
            round_to_tick(0.0, "buy")

    def test_negative_raises_value_error(self):
        with pytest.raises(ValueError, match="positive"):
            round_to_tick(-10.0, "buy")

    def test_invalid_string_raises_value_error(self):
        with pytest.raises((ValueError, TypeError)):
            round_to_tick(float("nan"), "buy")

    def test_penny_boundary_399_99(self):
        result = round_to_tick(399.99, "buy")
        assert result == Decimal("399.99")

    def test_penny_boundary_400_00(self):
        result = round_to_tick(400.00, "buy")
        assert result == Decimal("400.00")


# ===========================================================================
# TestValidateTickPrice
# ===========================================================================

class TestValidateTickPrice:
    def test_valid_two_decimal_returns_none(self):
        assert validate_tick_price(150.00) is None

    def test_valid_one_decimal_returns_none(self):
        assert validate_tick_price(150.5) is None

    def test_valid_whole_number_returns_none(self):
        assert validate_tick_price(200.0) is None

    def test_three_decimal_returns_error(self):
        err = validate_tick_price(1078.765)
        assert err is not None
        assert "sub-tick" in err or "decimal" in err.lower()

    def test_error_mentions_correct_rounded_value(self):
        err = validate_tick_price(1078.765)
        assert "1078.77" in err

    def test_zero_returns_error(self):
        err = validate_tick_price(0.0)
        assert err is not None
        assert "positive" in err.lower()

    def test_negative_returns_error(self):
        err = validate_tick_price(-5.0)
        assert err is not None

    def test_valid_sub_dollar_four_decimals_returns_none(self):
        assert validate_tick_price(0.1234) is None

    def test_sub_dollar_five_decimals_returns_error(self):
        err = validate_tick_price(0.12345)
        assert err is not None
        assert "sub-tick" in err or "decimal" in err.lower()

    def test_eqix_at_valid_tick_returns_none(self):
        assert validate_tick_price(1078.77) is None

    def test_eqix_at_invalid_tick_returns_error(self):
        assert validate_tick_price(1078.765) is not None


# ===========================================================================
# TestPositionSizerTickRounding — proposed_orders have valid tick prices
# ===========================================================================

class TestPositionSizerTickRounding:
    def _compute(self, latest_close: float, **kwargs):
        from trading_os.planning.position_sizer import compute_proposed_orders
        targets = {
            "EQIX": {
                "weight": 0.09,
                "notional": 3600.0,
                "reason": "momentum",
                "latest_close": latest_close,
            }
        }
        return compute_proposed_orders(
            targets=targets,
            equity=40000.0,
            positions=[],
            min_order_notional=25.0,
            **kwargs,
        )

    def test_three_decimal_price_becomes_valid_tick(self):
        orders = self._compute(1078.765)
        assert len(orders) == 1
        lp = orders[0]["limit_price"]
        assert lp is not None
        assert validate_tick_price(lp) is None, (
            f"limit_price {lp} should be a valid tick but validate_tick_price returned error"
        )

    def test_proposed_order_limit_price_two_decimals(self):
        orders = self._compute(1078.765)
        lp = orders[0]["limit_price"]
        assert _has_at_most_n_decimal_places(lp, 2)

    def test_already_valid_price_unchanged(self):
        orders = self._compute(150.00)
        assert orders[0]["limit_price"] == pytest.approx(150.00)

    def test_zero_price_produces_skip_reason(self):
        orders = self._compute(0.0)
        assert orders[0]["skip_reason"] is not None

    def test_none_price_produces_skip_reason(self):
        from trading_os.planning.position_sizer import compute_proposed_orders
        targets = {
            "BIL": {
                "weight": 0.91,
                "notional": 36400.0,
                "reason": "risk_off",
                "latest_close": None,
            }
        }
        orders = compute_proposed_orders(
            targets=targets,
            equity=40000.0,
            positions=[],
            min_order_notional=25.0,
        )
        assert orders[0]["skip_reason"] is not None
        assert orders[0]["limit_price"] is None

    def test_sell_exit_price_is_valid_tick(self):
        from trading_os.planning.position_sizer import compute_proposed_orders
        positions = [{
            "symbol": "AAPL",
            "market_value": "3600.00",
            "current_price": "182.333",
            "avg_entry_price": "180.00",
        }]
        orders = compute_proposed_orders(
            targets={},
            equity=40000.0,
            positions=positions,
            min_order_notional=25.0,
        )
        sell_orders = [o for o in orders if o["symbol"] == "AAPL" and o["side"] == "sell"]
        assert len(sell_orders) == 1
        lp = sell_orders[0]["limit_price"]
        assert lp is not None
        assert validate_tick_price(lp) is None


# ===========================================================================
# TestOrderBuilderTickRounding — orders_validated have valid tick prices
# ===========================================================================

class TestOrderBuilderTickRounding:
    def _build_orders(self, limit_price: float, symbol: str = "EQIX"):
        from trading_os.execution.order_builder import build_execution_orders
        trade_plan = {
            "plan_id": "trade_plan-20260512T000000-abc12345",
            "proposed_orders": [{
                "symbol": symbol,
                "side": "buy",
                "order_type": "limit",
                "limit_price": limit_price,
                "notional": 3600.0,
                "target_weight": 0.09,
                "would_short": False,
                "skip_reason": None,
            }],
        }
        universe = {"symbols": [symbol]}
        risk_limits = {
            "allowed_fallbacks": ["BIL", "SPY"],
            "max_quote_spread_pct": 0.02,
            "min_order_notional": 25.0,
        }
        strategy = {
            "parameters": {"max_quote_spread_pct": 0.02, "min_order_notional": 25.0},
            "fallbacks": {
                "risk_off_target": {"symbol": "BIL"},
                "risk_on_no_candidates_target": {"symbol": "SPY"},
            },
        }
        market_snapshot = {
            "spreads": {symbol: {"symbol": symbol, "spread_pct": 0.001}},
        }
        return build_execution_orders(
            trade_plan=trade_plan,
            universe=universe,
            risk_limits=risk_limits,
            strategy=strategy,
            market_snapshot=market_snapshot,
        )

    def test_three_decimal_price_becomes_valid_tick(self):
        orders = self._build_orders(1078.765)
        assert len(orders) == 1
        lp = orders[0]["limit_price"]
        assert lp is not None
        assert validate_tick_price(lp) is None

    def test_orders_validated_no_three_decimal_prices(self):
        orders = self._build_orders(1078.765)
        for o in orders:
            if o["limit_price"] is not None:
                assert _has_at_most_n_decimal_places(o["limit_price"], 2)

    def test_valid_price_passes_through(self):
        orders = self._build_orders(150.00)
        assert orders[0]["limit_price"] == pytest.approx(150.00)
        assert orders[0]["execution_ready"] is True


# ===========================================================================
# TestPaperExecutorTickValidation — executor blocks sub-tick prices before submit
# ===========================================================================

class TestPaperExecutorTickValidation:
    def test_sub_tick_price_blocked_not_submitted(self, tmp_path):
        """An order with a sub-tick limit_price must be skipped, not submitted."""
        from trading_os.execution.paper_executor import _validate_order_paper_safe

        order = {
            "symbol": "EQIX",
            "side": "buy",
            "order_type": "limit",
            "limit_price": 1078.765,  # sub-tick
            "notional": 3600.0,
            "time_in_force": "day",
            "would_short": False,
        }
        reason = _validate_order_paper_safe(order)
        assert reason is not None
        assert "tick" in reason.lower() or "decimal" in reason.lower()

    def test_valid_tick_price_passes_validation(self):
        from trading_os.execution.paper_executor import _validate_order_paper_safe

        order = {
            "symbol": "EQIX",
            "side": "buy",
            "order_type": "limit",
            "limit_price": 1078.77,  # valid tick
            "notional": 3600.0,
            "time_in_force": "day",
            "would_short": False,
        }
        assert _validate_order_paper_safe(order) is None

    def test_submit_paper_order_applies_final_rounding(self, tmp_path):
        """submit_paper_order must round the price before calling the broker, not reject it."""
        from trading_os.execution.paper_executor import submit_paper_order

        client = MagicMock()
        response = MagicMock()
        response.id = "broker-001"
        response.status = "accepted"
        response.model_dump.return_value = {"id": "broker-001", "status": "accepted"}
        client.submit_order.return_value = response

        order = {
            "symbol": "EQIX",
            "side": "buy",
            "order_type": "limit",
            "limit_price": 1078.765,
            "notional": 3600.0,
            "time_in_force": "day",
            "would_short": False,
            "client_order_id": "TOS-20260512T000000-EQIX-BUY",
            "validation_skip_reason": None,
        }
        result = submit_paper_order(client, order, tmp_path)

        # Price submitted to broker must be a valid tick
        assert client.submit_order.called
        req_arg = client.submit_order.call_args[0][0]
        submitted_price = float(req_arg.limit_price)
        assert validate_tick_price(submitted_price) is None, (
            f"Broker received sub-tick price {submitted_price}"
        )
        assert result["limit_price"] == pytest.approx(1078.77)

    def test_submit_paper_order_broker_sees_rounded_price(self, tmp_path):
        """Prove the rounded price (not the raw float) is sent to the broker."""
        from trading_os.execution.paper_executor import submit_paper_order

        client = MagicMock()
        response = MagicMock()
        response.id = "broker-002"
        response.status = "accepted"
        response.model_dump.return_value = {"id": "broker-002", "status": "accepted"}
        client.submit_order.return_value = response

        order = {
            "symbol": "NVDA",
            "side": "buy",
            "order_type": "limit",
            "limit_price": 875.333,  # 3 decimal places
            "notional": 5000.0,
            "time_in_force": "day",
            "would_short": False,
            "client_order_id": "TOS-20260512T000000-NVDA-BUY",
            "validation_skip_reason": None,
        }
        submit_paper_order(client, order, tmp_path)

        req_arg = client.submit_order.call_args[0][0]
        submitted_price = float(req_arg.limit_price)
        assert _has_at_most_n_decimal_places(submitted_price, 2), (
            f"Broker received {submitted_price} which has more than 2 decimal places"
        )
