from __future__ import annotations

import pytest

from trading_os.schemas import (
    SchemaError,
    validate_execution_policy,
    validate_risk_limits,
    validate_risk_state,
    validate_sector_map,
    validate_strategy,
    validate_trigger_registry,
    validate_universe,
)

# ---------------------------------------------------------------------------
# Canonical valid fixtures
# ---------------------------------------------------------------------------

VALID_STRATEGY = {
    "strategy_id": "test_strategy_v1",
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
    },
    "risk_gates": ["NO_LIVE_TRADING"],
}

VALID_RISK_LIMITS = {
    "paper_only": True,
    "live_trading_allowed": False,
    "max_portfolio_gross_exposure": 1.0,
    "max_position_weight": 0.12,
    "max_holdings": 10,
    "max_names_per_sector": 2,
    "max_drawdown_warn_pct": -0.05,
    "max_drawdown_block_pct": -0.10,
    "min_order_notional": 25.0,
    "max_quote_spread_pct": 0.02,
    "block_symbols": [],
    "allowed_fallbacks": ["BIL", "SPY"],
}

VALID_EXECUTION_POLICY = {
    "policy_version": "0.1.0",
    "paper_only": True,
    "require_confirm_paper_flag": True,
    "require_plan_approval": True,
    "require_market_open": True,
    "allow_shorting": False,
    "allow_options": False,
    "allow_crypto": False,
    "fail_closed_on_any_gate_failure": True,
}

VALID_UNIVERSE = {
    "universe_id": "test_universe_v1",
    "benchmark": "SPY",
    "symbols": ["AAPL", "MSFT"],
    "fallbacks": ["BIL", "SPY"],
}

VALID_SECTOR_MAP = {
    "AAPL": {"sector": "Technology", "sector_code": 101},
    "MSFT": {"sector": "Technology", "sector_code": 101},
}

VALID_TRIGGER_REGISTRY = {
    "registry_version": "0.1.0",
    "triggers": [
        {
            "id": "TEST_TRIGGER",
            "layer": "trigger_scan",
            "definition": "Close > 200-day SMA",
            "trade_direct": False,
        }
    ],
}

VALID_RISK_STATE = {
    "schema_version": "0.1.0",
    "updated_at": "2026-05-12T15:33:05Z",
    "last_monitor_run_id": "position_monitor-20260512T153305-abc12345",
    "drawdown": 0.0,
    "latest_equity": 40000.0,
    "peak_equity": 40000.0,
    "position_count": 0,
}


# ---------------------------------------------------------------------------
# Strategy
# ---------------------------------------------------------------------------

class TestValidateStrategy:
    def test_valid_passes(self) -> None:
        validate_strategy(VALID_STRATEGY)

    def test_live_mode_rejected(self) -> None:
        d = {**VALID_STRATEGY, "trading_mode": "live"}
        with pytest.raises(SchemaError) as exc_info:
            validate_strategy(d)
        assert "paper_only" in str(exc_info.value)

    def test_missing_strategy_id_rejected(self) -> None:
        d = {k: v for k, v in VALID_STRATEGY.items() if k != "strategy_id"}
        with pytest.raises(SchemaError):
            validate_strategy(d)

    def test_shorting_rejected(self) -> None:
        ap = {**VALID_STRATEGY["asset_policy"], "allow_shorting": True}
        with pytest.raises(SchemaError):
            validate_strategy({**VALID_STRATEGY, "asset_policy": ap})

    def test_options_rejected(self) -> None:
        ap = {**VALID_STRATEGY["asset_policy"], "allow_options": True}
        with pytest.raises(SchemaError):
            validate_strategy({**VALID_STRATEGY, "asset_policy": ap})

    def test_crypto_rejected(self) -> None:
        ap = {**VALID_STRATEGY["asset_policy"], "allow_crypto": True}
        with pytest.raises(SchemaError):
            validate_strategy({**VALID_STRATEGY, "asset_policy": ap})

    def test_short_only_rejected(self) -> None:
        ap = {**VALID_STRATEGY["asset_policy"], "long_only": False}
        with pytest.raises(SchemaError):
            validate_strategy({**VALID_STRATEGY, "asset_policy": ap})

    def test_empty_risk_gates_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_strategy({**VALID_STRATEGY, "risk_gates": []})

    def test_zero_max_holdings_rejected(self) -> None:
        params = {**VALID_STRATEGY["parameters"], "max_holdings": 0}
        with pytest.raises(SchemaError):
            validate_strategy({**VALID_STRATEGY, "parameters": params})

    def test_overweight_position_rejected(self) -> None:
        params = {**VALID_STRATEGY["parameters"], "max_position_weight": 1.5}
        with pytest.raises(SchemaError):
            validate_strategy({**VALID_STRATEGY, "parameters": params})

    def test_error_contains_context(self) -> None:
        with pytest.raises(SchemaError) as exc_info:
            validate_strategy({**VALID_STRATEGY, "trading_mode": "live"})
        assert exc_info.value.context == "strategy"
        assert len(exc_info.value.errors) >= 1


# ---------------------------------------------------------------------------
# Risk limits
# ---------------------------------------------------------------------------

class TestValidateRiskLimits:
    def test_valid_passes(self) -> None:
        validate_risk_limits(VALID_RISK_LIMITS)

    def test_paper_only_false_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_risk_limits({**VALID_RISK_LIMITS, "paper_only": False})

    def test_live_trading_allowed_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_risk_limits({**VALID_RISK_LIMITS, "live_trading_allowed": True})

    def test_block_pct_must_be_negative(self) -> None:
        with pytest.raises(SchemaError):
            validate_risk_limits({**VALID_RISK_LIMITS, "max_drawdown_block_pct": 0.1})

    def test_warn_pct_must_be_negative(self) -> None:
        with pytest.raises(SchemaError):
            validate_risk_limits({**VALID_RISK_LIMITS, "max_drawdown_warn_pct": 0.0})

    def test_block_must_be_lte_warn(self) -> None:
        # block less severe than warn — invalid ordering
        with pytest.raises(SchemaError):
            validate_risk_limits({
                **VALID_RISK_LIMITS,
                "max_drawdown_warn_pct": -0.10,
                "max_drawdown_block_pct": -0.05,
            })

    def test_exposure_above_one_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_risk_limits({**VALID_RISK_LIMITS, "max_portfolio_gross_exposure": 1.1})

    def test_empty_fallbacks_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_risk_limits({**VALID_RISK_LIMITS, "allowed_fallbacks": []})


# ---------------------------------------------------------------------------
# Execution policy
# ---------------------------------------------------------------------------

class TestValidateExecutionPolicy:
    def test_valid_passes(self) -> None:
        validate_execution_policy(VALID_EXECUTION_POLICY)

    def test_paper_only_false_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_execution_policy({**VALID_EXECUTION_POLICY, "paper_only": False})

    def test_shorting_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_execution_policy({**VALID_EXECUTION_POLICY, "allow_shorting": True})

    def test_options_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_execution_policy({**VALID_EXECUTION_POLICY, "allow_options": True})

    def test_crypto_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_execution_policy({**VALID_EXECUTION_POLICY, "allow_crypto": True})

    def test_fail_open_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_execution_policy({**VALID_EXECUTION_POLICY, "fail_closed_on_any_gate_failure": False})

    def test_missing_plan_approval_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_execution_policy({**VALID_EXECUTION_POLICY, "require_plan_approval": False})

    def test_missing_version_rejected(self) -> None:
        d = {k: v for k, v in VALID_EXECUTION_POLICY.items() if k != "policy_version"}
        with pytest.raises(SchemaError):
            validate_execution_policy(d)


# ---------------------------------------------------------------------------
# Universe
# ---------------------------------------------------------------------------

class TestValidateUniverse:
    def test_valid_passes(self) -> None:
        validate_universe(VALID_UNIVERSE)

    def test_empty_symbols_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_universe({**VALID_UNIVERSE, "symbols": []})

    def test_missing_benchmark_rejected(self) -> None:
        d = {k: v for k, v in VALID_UNIVERSE.items() if k != "benchmark"}
        with pytest.raises(SchemaError):
            validate_universe(d)

    def test_missing_universe_id_rejected(self) -> None:
        d = {k: v for k, v in VALID_UNIVERSE.items() if k != "universe_id"}
        with pytest.raises(SchemaError):
            validate_universe(d)

    def test_empty_fallbacks_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_universe({**VALID_UNIVERSE, "fallbacks": []})

    def test_non_string_symbol_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_universe({**VALID_UNIVERSE, "symbols": ["AAPL", 123]})


# ---------------------------------------------------------------------------
# Sector map
# ---------------------------------------------------------------------------

class TestValidateSectorMap:
    def test_valid_passes(self) -> None:
        validate_sector_map(VALID_SECTOR_MAP)

    def test_empty_dict_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_sector_map({})

    def test_non_dict_entry_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_sector_map({"AAPL": "Technology"})

    def test_missing_sector_code_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_sector_map({"AAPL": {"sector": "Technology"}})

    def test_string_sector_code_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_sector_map({"AAPL": {"sector": "Technology", "sector_code": "101"}})

    def test_empty_sector_name_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_sector_map({"AAPL": {"sector": "", "sector_code": 101}})


# ---------------------------------------------------------------------------
# Trigger registry
# ---------------------------------------------------------------------------

class TestValidateTriggerRegistry:
    def test_valid_passes(self) -> None:
        validate_trigger_registry(VALID_TRIGGER_REGISTRY)

    def test_trade_direct_true_rejected(self) -> None:
        bad_trigger = {**VALID_TRIGGER_REGISTRY["triggers"][0], "trade_direct": True}
        with pytest.raises(SchemaError):
            validate_trigger_registry({**VALID_TRIGGER_REGISTRY, "triggers": [bad_trigger]})

    def test_empty_triggers_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_trigger_registry({**VALID_TRIGGER_REGISTRY, "triggers": []})

    def test_missing_version_rejected(self) -> None:
        d = {k: v for k, v in VALID_TRIGGER_REGISTRY.items() if k != "registry_version"}
        with pytest.raises(SchemaError):
            validate_trigger_registry(d)

    def test_trigger_missing_id_rejected(self) -> None:
        bad = {k: v for k, v in VALID_TRIGGER_REGISTRY["triggers"][0].items() if k != "id"}
        with pytest.raises(SchemaError):
            validate_trigger_registry({**VALID_TRIGGER_REGISTRY, "triggers": [bad]})

    def test_trigger_missing_definition_rejected(self) -> None:
        bad = {k: v for k, v in VALID_TRIGGER_REGISTRY["triggers"][0].items() if k != "definition"}
        with pytest.raises(SchemaError):
            validate_trigger_registry({**VALID_TRIGGER_REGISTRY, "triggers": [bad]})


# ---------------------------------------------------------------------------
# Risk state
# ---------------------------------------------------------------------------

class TestValidateRiskState:
    def test_valid_passes(self) -> None:
        validate_risk_state(VALID_RISK_STATE)

    def test_zero_equity_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_risk_state({**VALID_RISK_STATE, "latest_equity": 0.0})

    def test_negative_equity_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_risk_state({**VALID_RISK_STATE, "latest_equity": -1.0})

    def test_negative_position_count_rejected(self) -> None:
        with pytest.raises(SchemaError):
            validate_risk_state({**VALID_RISK_STATE, "position_count": -1})

    def test_missing_run_id_rejected(self) -> None:
        d = {k: v for k, v in VALID_RISK_STATE.items() if k != "last_monitor_run_id"}
        with pytest.raises(SchemaError):
            validate_risk_state(d)

    def test_missing_schema_version_rejected(self) -> None:
        d = {k: v for k, v in VALID_RISK_STATE.items() if k != "schema_version"}
        with pytest.raises(SchemaError):
            validate_risk_state(d)

    def test_missing_updated_at_rejected(self) -> None:
        d = {k: v for k, v in VALID_RISK_STATE.items() if k != "updated_at"}
        with pytest.raises(SchemaError):
            validate_risk_state(d)

    def test_error_context_set(self) -> None:
        with pytest.raises(SchemaError) as exc_info:
            validate_risk_state({**VALID_RISK_STATE, "latest_equity": 0.0})
        assert exc_info.value.context == "risk_state"
