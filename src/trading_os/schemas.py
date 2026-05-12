from __future__ import annotations

from typing import Any


class SchemaError(ValueError):
    """Raised when a config or state object fails schema validation."""

    def __init__(self, context: str, errors: list) -> None:
        self.context = context
        self.errors = list(errors)
        super().__init__(f"{context}: {'; '.join(self.errors)}")


def _require(errors: list, condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def _require_bool_false(errors: list, d: dict, key: str) -> None:
    if d.get(key) is not False:
        errors.append(f"{key} must be false")


def _require_bool_true(errors: list, d: dict, key: str) -> None:
    if d.get(key) is not True:
        errors.append(f"{key} must be true")


# ---------------------------------------------------------------------------
# Strategy
# ---------------------------------------------------------------------------

def validate_strategy(d: Any) -> None:
    errors: list = []
    _require(errors, isinstance(d, dict), "must be a JSON object")
    if not isinstance(d, dict):
        raise SchemaError("strategy", errors)

    _require(errors, isinstance(d.get("strategy_id"), str) and bool(d.get("strategy_id")), "strategy_id is required")
    _require(errors, isinstance(d.get("version"), str) and bool(d.get("version")), "version is required")
    _require(errors, d.get("trading_mode") == "paper_only", "trading_mode must be 'paper_only'")

    ap = d.get("asset_policy")
    if not isinstance(ap, dict):
        errors.append("asset_policy must be a dict")
    else:
        _require_bool_true(errors, ap, "long_only")
        _require_bool_false(errors, ap, "allow_shorting")
        _require_bool_false(errors, ap, "allow_options")
        _require_bool_false(errors, ap, "allow_crypto")

    params = d.get("parameters")
    if not isinstance(params, dict):
        errors.append("parameters must be a dict")
    else:
        _require(
            errors,
            isinstance(params.get("max_holdings"), int) and params["max_holdings"] > 0,
            "parameters.max_holdings must be a positive int",
        )
        _require(
            errors,
            isinstance(params.get("max_position_weight"), (int, float))
            and 0 < float(params["max_position_weight"]) <= 1.0,
            "parameters.max_position_weight must be in (0, 1]",
        )

    gates = d.get("risk_gates")
    _require(errors, isinstance(gates, list) and len(gates) > 0, "risk_gates must be a non-empty list")

    if errors:
        raise SchemaError("strategy", errors)


# ---------------------------------------------------------------------------
# Risk limits
# ---------------------------------------------------------------------------

def validate_risk_limits(d: Any) -> None:
    errors: list = []
    _require(errors, isinstance(d, dict), "must be a JSON object")
    if not isinstance(d, dict):
        raise SchemaError("risk_limits", errors)

    _require_bool_true(errors, d, "paper_only")
    _require_bool_false(errors, d, "live_trading_allowed")

    _require(
        errors,
        isinstance(d.get("max_portfolio_gross_exposure"), (int, float))
        and 0 < float(d["max_portfolio_gross_exposure"]) <= 1.0,
        "max_portfolio_gross_exposure must be in (0, 1]",
    )
    _require(
        errors,
        isinstance(d.get("max_position_weight"), (int, float))
        and 0 < float(d["max_position_weight"]) <= 1.0,
        "max_position_weight must be in (0, 1]",
    )
    _require(
        errors,
        isinstance(d.get("max_holdings"), int) and d["max_holdings"] > 0,
        "max_holdings must be a positive int",
    )
    _require(
        errors,
        isinstance(d.get("max_names_per_sector"), int) and d["max_names_per_sector"] > 0,
        "max_names_per_sector must be a positive int",
    )

    warn = d.get("max_drawdown_warn_pct")
    block = d.get("max_drawdown_block_pct")
    _require(errors, isinstance(warn, (int, float)) and float(warn) < 0, "max_drawdown_warn_pct must be negative")
    _require(errors, isinstance(block, (int, float)) and float(block) < 0, "max_drawdown_block_pct must be negative")
    if isinstance(warn, (int, float)) and isinstance(block, (int, float)):
        _require(errors, float(block) <= float(warn), "max_drawdown_block_pct must be <= max_drawdown_warn_pct")

    _require(
        errors,
        isinstance(d.get("min_order_notional"), (int, float)) and d["min_order_notional"] > 0,
        "min_order_notional must be positive",
    )
    _require(
        errors,
        isinstance(d.get("max_quote_spread_pct"), (int, float)) and d["max_quote_spread_pct"] > 0,
        "max_quote_spread_pct must be positive",
    )
    _require(errors, isinstance(d.get("block_symbols"), list), "block_symbols must be a list")
    _require(
        errors,
        isinstance(d.get("allowed_fallbacks"), list) and len(d.get("allowed_fallbacks", [])) > 0,
        "allowed_fallbacks must be a non-empty list",
    )

    if "max_orders_per_run" in d:
        _require(
            errors,
            isinstance(d["max_orders_per_run"], int) and d["max_orders_per_run"] >= 1,
            "max_orders_per_run must be a positive int when present",
        )
    if "max_notional_per_order" in d:
        _require(
            errors,
            isinstance(d["max_notional_per_order"], (int, float))
            and float(d["max_notional_per_order"]) > 0,
            "max_notional_per_order must be positive when present",
        )
        if "min_order_notional" in d and isinstance(d.get("min_order_notional"), (int, float)):
            _require(
                errors,
                float(d["max_notional_per_order"]) >= float(d["min_order_notional"]),
                "max_notional_per_order must be >= min_order_notional",
            )

    if errors:
        raise SchemaError("risk_limits", errors)


# ---------------------------------------------------------------------------
# Execution policy
# ---------------------------------------------------------------------------

def validate_execution_policy(d: Any) -> None:
    errors: list = []
    _require(errors, isinstance(d, dict), "must be a JSON object")
    if not isinstance(d, dict):
        raise SchemaError("execution_policy", errors)

    _require(
        errors,
        isinstance(d.get("policy_version"), str) and bool(d.get("policy_version")),
        "policy_version is required",
    )
    _require_bool_true(errors, d, "paper_only")
    _require_bool_true(errors, d, "require_confirm_paper_flag")
    _require_bool_true(errors, d, "require_plan_approval")
    _require_bool_true(errors, d, "require_market_open")
    _require_bool_false(errors, d, "allow_shorting")
    _require_bool_false(errors, d, "allow_options")
    _require_bool_false(errors, d, "allow_crypto")
    _require_bool_true(errors, d, "fail_closed_on_any_gate_failure")

    if errors:
        raise SchemaError("execution_policy", errors)


# ---------------------------------------------------------------------------
# Universe
# ---------------------------------------------------------------------------

def validate_universe(d: Any) -> None:
    errors: list = []
    _require(errors, isinstance(d, dict), "must be a JSON object")
    if not isinstance(d, dict):
        raise SchemaError("universe", errors)

    _require(
        errors,
        isinstance(d.get("universe_id"), str) and bool(d.get("universe_id")),
        "universe_id is required",
    )
    _require(
        errors,
        isinstance(d.get("benchmark"), str) and bool(d.get("benchmark")),
        "benchmark is required",
    )
    symbols = d.get("symbols")
    _require(errors, isinstance(symbols, list) and len(symbols) > 0, "symbols must be a non-empty list")
    if isinstance(symbols, list):
        _require(
            errors,
            all(isinstance(s, str) and s for s in symbols),
            "all symbols must be non-empty strings",
        )
    fallbacks = d.get("fallbacks")
    _require(errors, isinstance(fallbacks, list) and len(fallbacks) > 0, "fallbacks must be a non-empty list")

    if errors:
        raise SchemaError("universe", errors)


# ---------------------------------------------------------------------------
# Sector map
# ---------------------------------------------------------------------------

def validate_sector_map(d: Any) -> None:
    errors: list = []
    if not isinstance(d, dict) or len(d) == 0:
        errors.append("sector_map must be a non-empty JSON object")
        raise SchemaError("sector_map", errors)

    for symbol, entry in d.items():
        if not isinstance(entry, dict):
            errors.append(f"sector_map[{symbol!r}] must be a dict")
            continue
        if not isinstance(entry.get("sector"), str) or not entry["sector"]:
            errors.append(f"sector_map[{symbol!r}].sector must be a non-empty string")
        if not isinstance(entry.get("sector_code"), int):
            errors.append(f"sector_map[{symbol!r}].sector_code must be an int")

    if errors:
        raise SchemaError("sector_map", errors)


# ---------------------------------------------------------------------------
# Trigger registry
# ---------------------------------------------------------------------------

def validate_trigger_registry(d: Any) -> None:
    errors: list = []
    _require(errors, isinstance(d, dict), "must be a JSON object")
    if not isinstance(d, dict):
        raise SchemaError("trigger_registry", errors)

    _require(
        errors,
        isinstance(d.get("registry_version"), str) and bool(d.get("registry_version")),
        "registry_version is required",
    )
    triggers = d.get("triggers")
    _require(errors, isinstance(triggers, list) and len(triggers) > 0, "triggers must be a non-empty list")

    if isinstance(triggers, list):
        for i, t in enumerate(triggers):
            prefix = f"triggers[{i}]"
            if not isinstance(t, dict):
                errors.append(f"{prefix} must be a dict")
                continue
            if not isinstance(t.get("id"), str) or not t["id"]:
                errors.append(f"{prefix}.id must be a non-empty string")
            if not isinstance(t.get("layer"), str) or not t["layer"]:
                errors.append(f"{prefix}.layer must be a non-empty string")
            if not isinstance(t.get("definition"), str) or not t["definition"]:
                errors.append(f"{prefix}.definition must be a non-empty string")
            if t.get("trade_direct") is not False:
                errors.append(f"{prefix}.trade_direct must be false — triggers never place orders directly")

    if errors:
        raise SchemaError("trigger_registry", errors)


# ---------------------------------------------------------------------------
# Risk state
# ---------------------------------------------------------------------------

def validate_risk_state(d: Any) -> None:
    errors: list = []
    _require(errors, isinstance(d, dict), "must be a JSON object")
    if not isinstance(d, dict):
        raise SchemaError("risk_state", errors)

    _require(
        errors,
        isinstance(d.get("schema_version"), str) and bool(d.get("schema_version")),
        "schema_version is required",
    )
    _require(
        errors,
        isinstance(d.get("updated_at"), str) and bool(d.get("updated_at")),
        "updated_at is required",
    )
    _require(
        errors,
        isinstance(d.get("last_monitor_run_id"), str) and bool(d.get("last_monitor_run_id")),
        "last_monitor_run_id is required",
    )
    _require(errors, isinstance(d.get("drawdown"), (int, float)), "drawdown must be a number")
    _require(
        errors,
        isinstance(d.get("latest_equity"), (int, float)) and d["latest_equity"] > 0,
        "latest_equity must be positive",
    )
    _require(
        errors,
        isinstance(d.get("peak_equity"), (int, float)) and d["peak_equity"] > 0,
        "peak_equity must be positive",
    )
    _require(
        errors,
        isinstance(d.get("position_count"), int) and d["position_count"] >= 0,
        "position_count must be a non-negative int",
    )

    if errors:
        raise SchemaError("risk_state", errors)
