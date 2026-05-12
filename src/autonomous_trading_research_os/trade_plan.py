from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

from .audit import append_event, new_run_id, record_error
from .file_io import read_json, safe_float, sha256_json, utc_now_iso, write_json
from .paths import CONFIG_DIR, LATEST_DIR, ensure_repo_dirs
from .risk import all_gates_pass, evaluate_plan_risk


def _account_equity(snapshot: dict[str, Any]) -> float:
    account = snapshot.get("account", {}) if isinstance(snapshot.get("account"), dict) else {}
    return safe_float(account.get("equity") or account.get("portfolio_value") or account.get("cash"), 0.0)


def _positions_by_symbol(snapshot: dict[str, Any]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    positions = snapshot.get("positions", [])
    if not isinstance(positions, list):
        return out
    for position in positions:
        if not isinstance(position, dict):
            continue
        symbol = str(position.get("symbol") or position.get("asset_symbol") or "").upper()
        if not symbol:
            continue
        out[symbol] = position
    return out


def _latest_price(snapshot: dict[str, Any], symbol: str) -> float:
    bars = snapshot.get("bars", {}).get(symbol, []) if isinstance(snapshot.get("bars"), dict) else []
    if bars:
        return safe_float(bars[-1].get("close") or bars[-1].get("c"), 0.0)
    quote = snapshot.get("quotes", {}).get(symbol, {}) if isinstance(snapshot.get("quotes"), dict) else {}
    bid = safe_float(quote.get("bid_price") or quote.get("bid"), 0.0)
    ask = safe_float(quote.get("ask_price") or quote.get("ask"), 0.0)
    return (bid + ask) / 2.0 if bid and ask else 0.0


def _position_market_value(position: dict[str, Any]) -> float:
    return safe_float(position.get("market_value") or position.get("market_value_usd") or position.get("notional"), 0.0)


def _position_qty(position: dict[str, Any]) -> float:
    return safe_float(position.get("qty") or position.get("quantity"), 0.0)


def _build_targets(trigger_snapshot: dict[str, Any], strategy: dict[str, Any]) -> tuple[dict[str, float], str]:
    params = strategy.get("parameters", {})
    fallbacks = strategy.get("fallbacks", {})
    regime = trigger_snapshot.get("regime", {})
    risk_on = bool(regime.get("risk_on"))
    selected = trigger_snapshot.get("selected", []) if risk_on else []

    if not risk_on:
        target = fallbacks.get("risk_off_target", {"symbol": "BIL", "weight": 1.0})
        return {target["symbol"]: float(target["weight"])}, "risk_off_bil_fallback"

    if not selected:
        target = fallbacks.get("risk_on_no_candidates_target", {"symbol": "SPY", "weight": 1.0})
        return {target["symbol"]: float(target["weight"])}, "risk_on_no_candidates_spy_fallback"

    min_atr_floor = float(params.get("min_atr_pct_floor", 0.01))
    alloc = float(params.get("risk_on_equity_alloc", 0.90))
    max_weight = float(params.get("max_position_weight", 0.12))
    inv_vols: list[tuple[str, float]] = []
    for item in selected:
        atr_pct = max(float(item.get("atr_pct") or min_atr_floor), min_atr_floor)
        inv_vols.append((item["symbol"], 1.0 / atr_pct))
    raw_sum = sum(weight for _, weight in inv_vols)
    if raw_sum <= 0:
        target = fallbacks.get("risk_on_no_candidates_target", {"symbol": "SPY", "weight": 1.0})
        return {target["symbol"]: float(target["weight"])}, "risk_on_invalid_vol_spy_fallback"

    targets: dict[str, float] = {}
    stock_sum = 0.0
    for symbol, inv_vol in inv_vols:
        raw_weight = (inv_vol / raw_sum) * alloc
        weight = min(raw_weight, max_weight)
        targets[symbol] = round(weight, 6)
        stock_sum += weight
    residual = max(0.0, 1.0 - stock_sum)
    if residual > 1e-6:
        targets["BIL"] = round(residual, 6)
    return targets, "risk_on_stock_basket_inverse_atr_weighted"


def _build_orders(snapshot: dict[str, Any], targets: dict[str, float], run_id: str, min_notional: float) -> list[dict[str, Any]]:
    equity = _account_equity(snapshot)
    positions = _positions_by_symbol(snapshot)
    symbols = sorted(set(targets) | set(positions))
    orders: list[dict[str, Any]] = []
    for symbol in symbols:
        target_weight = safe_float(targets.get(symbol), 0.0)
        target_value = target_weight * equity
        current_position = positions.get(symbol, {})
        current_value = _position_market_value(current_position)
        current_qty = _position_qty(current_position)
        delta = target_value - current_value
        price = _latest_price(snapshot, symbol)
        if abs(delta) < min_notional:
            orders.append({
                "symbol": symbol,
                "action": "skip",
                "reason": "below_min_order_notional",
                "target_weight": round(target_weight, 6),
                "target_value": round(target_value, 2),
                "current_value": round(current_value, 2),
                "delta_value": round(delta, 2),
            })
            continue
        if delta > 0:
            orders.append({
                "symbol": symbol,
                "action": "submit_candidate",
                "side": "buy",
                "order_type": "market",
                "time_in_force": "day",
                "notional": round(delta, 2),
                "qty": None,
                "would_short": False,
                "target_weight": round(target_weight, 6),
                "target_value": round(target_value, 2),
                "current_value": round(current_value, 2),
                "delta_value": round(delta, 2),
                "client_order_id": f"ATR-OS-{run_id[:24]}-{symbol}-BUY",
            })
        else:
            qty_to_sell = abs(delta) / price if price > 0 else 0.0
            would_short = qty_to_sell > current_qty + 1e-6
            qty = min(qty_to_sell, max(0.0, current_qty))
            if qty <= 0:
                orders.append({
                    "symbol": symbol,
                    "action": "skip",
                    "reason": "sell_required_but_no_long_qty_available",
                    "target_weight": round(target_weight, 6),
                    "target_value": round(target_value, 2),
                    "current_value": round(current_value, 2),
                    "delta_value": round(delta, 2),
                    "would_short": would_short,
                })
            else:
                orders.append({
                    "symbol": symbol,
                    "action": "submit_candidate",
                    "side": "sell",
                    "order_type": "market",
                    "time_in_force": "day",
                    "notional": None,
                    "qty": round(qty, 6),
                    "would_short": would_short,
                    "target_weight": round(target_weight, 6),
                    "target_value": round(target_value, 2),
                    "current_value": round(current_value, 2),
                    "delta_value": round(delta, 2),
                    "client_order_id": f"ATR-OS-{run_id[:24]}-{symbol}-SELL",
                })
    return orders


def generate_trade_plan(dry_run: bool = True, approve_paper: bool = False) -> dict[str, Any]:
    ensure_repo_dirs()
    run_id = new_run_id("trade_plan")
    try:
        strategy = read_json(CONFIG_DIR / "strategy.json", default={})
        universe = read_json(CONFIG_DIR / "universe.json", default={})
        sector_map = read_json(CONFIG_DIR / "sector_map.json", default={})
        snapshot = read_json(LATEST_DIR / "market_snapshot.json", default=None)
        trigger_snapshot = read_json(LATEST_DIR / "trigger_snapshot.json", default=None)
        if snapshot is None:
            raise RuntimeError("Missing data/latest/market_snapshot.json. Run data refresh first.")
        if trigger_snapshot is None:
            raise RuntimeError("Missing data/latest/trigger_snapshot.json. Run trigger scan first.")

        params = strategy.get("parameters", {})
        targets, target_reason = _build_targets(trigger_snapshot, strategy)
        proposed_orders = _build_orders(snapshot, targets, run_id, float(params.get("min_order_notional", 25.0)))
        risk_gates = evaluate_plan_risk(targets, proposed_orders, strategy, universe, sector_map, snapshot, require_alpaca_trade_data=not dry_run)
        gates_pass = all_gates_pass(risk_gates)
        expires_at = (datetime.now(timezone.utc) + timedelta(minutes=int(params.get("plan_expiry_minutes", 360)))).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        if dry_run:
            approval_status = "DRY_RUN_ONLY"
            approval_reason = "Dry-run plan generated for compile/pipeline validation; execution must not submit orders."
        elif approve_paper and gates_pass:
            approval_status = "APPROVED_FOR_PAPER"
            approval_reason = "All deterministic gates passed and approve-paper flag was provided."
        else:
            approval_status = "BLOCKED"
            approval_reason = "Plan is not approved for paper execution. Either gates failed or approve-paper flag was not provided."

        plan: dict[str, Any] = {
            "schema_version": "0.1.0",
            "run_id": run_id,
            "generated_at": utc_now_iso(),
            "expires_at": expires_at,
            "strategy_id": strategy.get("strategy_id"),
            "strategy_version": strategy.get("version"),
            "dry_run": dry_run,
            "market_snapshot_hash": snapshot.get("source_data_hash"),
            "trade_critical_data_source": snapshot.get("data_source"),
            "trade_critical_run_mode": snapshot.get("run_mode"),
            "trigger_snapshot_hash": trigger_snapshot.get("trigger_snapshot_hash"),
            "source_run_ids": {
                "data_refresh": snapshot.get("run_id"),
                "trigger_scan": trigger_snapshot.get("run_id"),
            },
            "market_regime": trigger_snapshot.get("regime", {}),
            "target_reason": target_reason,
            "targets": targets,
            "proposed_orders": proposed_orders,
            "risk_gates": risk_gates,
            "approval": {
                "status": approval_status,
                "reason": approval_reason,
                "all_gates_pass": gates_pass,
            },
            "blocked_symbols": read_json(CONFIG_DIR / "risk_limits.json", default={}).get("block_symbols", []),
            "no_trade_reasons": [gate["id"] for gate in risk_gates if not gate.get("passed")],
            "trade_plan_hash": None,
        }
        plan["trade_plan_hash"] = sha256_json({k: v for k, v in plan.items() if k != "trade_plan_hash"})
        write_json(LATEST_DIR / "trade_plan.json", plan)
        append_event("SIGNAL-LOG.md", "Trade plan generated", {
            "run_id": run_id,
            "approval_status": approval_status,
            "target_reason": target_reason,
            "targets": targets,
            "candidate_order_count": len([o for o in proposed_orders if o.get("action") == "submit_candidate"]),
            "failed_gates": plan["no_trade_reasons"],
            "trade_plan_hash": plan["trade_plan_hash"],
        })
        return plan
    except Exception as exc:
        record_error("trade_plan", exc, {"dry_run": dry_run, "approve_paper": approve_paper})
        raise
