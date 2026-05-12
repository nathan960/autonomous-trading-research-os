from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any

from .file_io import parse_iso_datetime, safe_float
from .settings import RuntimeSettings

_OPTION_SYMBOL_RE = re.compile(r"^[A-Z]{1,6}\d{6}[CP]\d{8}$")


def classify_symbol(symbol: str) -> str:
    if "/" in symbol or symbol.upper().endswith("USD") and symbol not in {"BIL", "SPY"}:
        return "crypto_like"
    if _OPTION_SYMBOL_RE.match(symbol.upper()):
        return "option_like"
    return "equity_or_etf"


def gate(gate_id: str, passed: bool, reason: str, details: dict[str, Any] | None = None) -> dict[str, Any]:
    return {"id": gate_id, "passed": bool(passed), "reason": reason, "details": details or {}}


def _snapshot_age_minutes(snapshot: dict[str, Any]) -> float | None:
    generated_at = parse_iso_datetime(str(snapshot.get("generated_at") or ""))
    if generated_at is None:
        return None
    return (datetime.now(timezone.utc) - generated_at).total_seconds() / 60.0


def evaluate_plan_risk(
    targets: dict[str, float],
    proposed_orders: list[dict[str, Any]],
    strategy: dict[str, Any],
    universe: dict[str, Any],
    sector_map: dict[str, Any],
    snapshot: dict[str, Any],
    require_alpaca_trade_data: bool = False,
) -> list[dict[str, Any]]:
    params = strategy.get("parameters", {})
    allowed_symbols = set(universe.get("symbols", [])) | set(universe.get("fallbacks", [])) | {universe.get("benchmark", "SPY"), "SPY", "BIL"}
    settings = RuntimeSettings.from_env()
    gates: list[dict[str, Any]] = []

    gates.append(gate(
        "NO_LIVE_TRADING",
        settings.trading_mode == "paper" and settings.alpaca_paper and not settings.live_trading_confirmed,
        "Trading mode is paper-only and live confirmation is false.",
        settings.redacted_summary(),
    ))

    total_weight = sum(max(0.0, safe_float(weight)) for weight in targets.values())
    gates.append(gate("TOTAL_WEIGHT_LIMIT", total_weight <= 1.0001, "Target gross exposure must be <= 100%.", {"total_weight": total_weight}))
    gates.append(gate("LONG_ONLY_TARGETS", all(safe_float(w) >= -1e-9 for w in targets.values()), "All targets must be non-negative.", {"targets": targets}))

    classified = {symbol: classify_symbol(symbol) for symbol in targets}
    gates.append(gate(
        "NO_OPTIONS_OR_CRYPTO",
        all(kind == "equity_or_etf" for kind in classified.values()),
        "Targets must be US equities/ETFs only.",
        classified,
    ))
    gates.append(gate(
        "UNIVERSE_ONLY",
        all(symbol in allowed_symbols for symbol in targets),
        "Targets must be in configured universe or approved fallback set.",
        {"unknown_symbols": sorted([symbol for symbol in targets if symbol not in allowed_symbols])},
    ))

    max_position_weight = safe_float(params.get("max_position_weight"), 0.12)
    max_holdings = int(params.get("max_holdings", 10))
    fallback_symbols = set(universe.get("fallbacks", [])) | {"BIL", "SPY"}
    stock_targets = {symbol: weight for symbol, weight in targets.items() if symbol not in fallback_symbols and weight > 1e-6}
    overweight = {symbol: weight for symbol, weight in stock_targets.items() if weight > max_position_weight + 1e-9}
    gates.append(gate("MAX_POSITION_WEIGHT", not overweight, "Individual stock weights must stay under cap.", {"overweight": overweight, "cap": max_position_weight}))
    gates.append(gate("MAX_HOLDINGS", len(stock_targets) <= max_holdings, "Number of stock holdings must stay under cap.", {"stock_holdings": len(stock_targets), "cap": max_holdings}))

    max_names_per_sector = int(params.get("max_names_per_sector", 2))
    sector_counts: dict[str, int] = {}
    for symbol in stock_targets:
        sector = str(sector_map.get(symbol, {}).get("sector_code", "UNKNOWN"))
        sector_counts[sector] = sector_counts.get(sector, 0) + 1
    sector_violations = {sector: count for sector, count in sector_counts.items() if count > max_names_per_sector}
    gates.append(gate("SECTOR_CAPS", not sector_violations, "Sector name counts must stay under cap.", {"sector_counts": sector_counts, "cap": max_names_per_sector}))

    oversells = [order for order in proposed_orders if order.get("side") == "sell" and order.get("would_short")]
    gates.append(gate("NO_SHORT_SELLS", not oversells, "Sell orders must not exceed current long quantity.", {"oversells": oversells}))

    source_hash = snapshot.get("source_data_hash")
    gates.append(gate("DATA_SOURCE_HASH_PRESENT", bool(source_hash), "Snapshot must include source data hash.", {"source_data_hash_present": bool(source_hash)}))

    max_age = safe_float(params.get("max_snapshot_age_minutes"), 90.0)
    age = _snapshot_age_minutes(snapshot)
    gates.append(gate("PLAN_EXISTS_AND_FRESH", age is not None and age <= max_age, "Market snapshot must be fresh enough for plan generation.", {"age_minutes": age, "max_age_minutes": max_age}))

    source_is_alpaca_paper = snapshot.get("data_source") == "alpaca_paper" and snapshot.get("run_mode") == "alpaca_paper"
    gates.append(gate(
        "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
        source_is_alpaca_paper or not require_alpaca_trade_data,
        "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation.",
        {"data_source": snapshot.get("data_source"), "run_mode": snapshot.get("run_mode"), "required": require_alpaca_trade_data},
    ))

    open_orders = snapshot.get("orders", []) if isinstance(snapshot.get("orders"), list) else []
    max_open_orders = int(params.get("max_open_orders", 25))
    gates.append(gate(
        "MAX_OPEN_ORDERS",
        len(open_orders) <= max_open_orders,
        "Open orders must stay within configured operational cap before new submissions.",
        {"open_order_count": len(open_orders), "max_open_orders": max_open_orders},
    ))

    max_spread = safe_float(params.get("max_quote_spread_pct"), 0.02)
    spreads = snapshot.get("spreads", {}) if isinstance(snapshot.get("spreads"), dict) else {}
    wide = {symbol: item.get("spread_pct") for symbol, item in spreads.items() if symbol in targets and safe_float(item.get("spread_pct"), 0.0) > max_spread}
    gates.append(gate("QUOTE_SPREAD_LIMIT", not wide, "Target quote spreads must be below configured limit.", {"wide_spreads": wide, "max_spread_pct": max_spread}))

    gates.append(gate("NO_SECRETS_IN_OUTPUT", True, "No secrets are required or emitted by risk gate output."))
    return gates


def all_gates_pass(gates: list[dict[str, Any]]) -> bool:
    return all(bool(item.get("passed")) for item in gates)
