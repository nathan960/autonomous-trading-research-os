"""Orchestrate allocator, position_sizer, and risk_checks into a trade plan.

The plan is always written — including no-trade plans when gates fail.
No orders are ever submitted here. Phase 4 output only.

Required trade_plan fields:
    plan_id, generated_at, expires_at, trading_mode, strategy_hash, data_hash,
    trigger_snapshot_hash, account_snapshot, market_clock, regime, targets,
    proposed_orders, blocked_symbols, risk_checks, no_trade_reasons,
    approval.approved_for_execution
"""
from __future__ import annotations

import uuid
from typing import Any, Optional

from ..hashing import stable_hash
from ..signals._indicators import closes, sorted_bars
from ..time_utils import utc_now_iso, parse_iso_utc
from .allocator import compute_targets
from .churn_guard import filter_churn_blocked
from .position_sizer import compute_proposed_orders
from .risk_checks import all_checks_pass, run_risk_checks

_PLAN_ID_PREFIX = "trade_plan"


def _plan_id(generated_at: str) -> str:
    ts = generated_at.replace(":", "").replace("-", "").replace("Z", "")[:15]
    uid = uuid.uuid4().hex[:8]
    return f"{_PLAN_ID_PREFIX}-{ts}-{uid}"


def _expires_at(generated_at: str, expiry_minutes: float) -> str:
    from datetime import timedelta
    dt = parse_iso_utc(generated_at)
    if dt is None:
        return generated_at
    expires = dt + timedelta(minutes=expiry_minutes)
    return expires.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _account_equity(account_snapshot: dict) -> float:
    """Extract portfolio equity as float from account snapshot."""
    acct = account_snapshot.get("account", {})
    try:
        return float(acct.get("equity") or 0)
    except (TypeError, ValueError):
        return 0.0


def _latest_close_from_bars(bars_map: dict, symbol: str) -> Optional[float]:
    """Look up the latest close price for a symbol from market snapshot bars."""
    bars = bars_map.get(symbol, [])
    ordered = sorted_bars(bars)
    cl = closes(ordered)
    return cl[-1] if cl else None


def _enrich_targets_with_prices(targets: dict, bars_map: dict) -> dict:
    """Fill in missing latest_close values from market snapshot bars."""
    enriched = {}
    for sym, tgt in targets.items():
        entry = dict(tgt)
        if entry.get("latest_close") is None:
            price = _latest_close_from_bars(bars_map, sym)
            if price is not None:
                entry["latest_close"] = price
        enriched[sym] = entry
    return enriched


def _filter_wide_spread_orders(
    orders: list,
    spreads: dict,
    max_spread: float,
) -> tuple:
    """Split orders into (spread_ok, spread_blocked) using market snapshot spreads.

    Spread-blocked orders have skip_reason set to spread_too_wide(...).
    Orders with no spread data in the snapshot are allowed through — execution
    gate SPREAD_NOT_TOO_WIDE will catch them if data arrives by then.
    """
    ok: list = []
    blocked: list = []
    for o in orders:
        sym = o["symbol"]
        sp = spreads.get(sym, {})
        pct = sp.get("spread_pct")
        if pct is not None and pct > max_spread:
            bo = dict(o)
            bo["skip_reason"] = f"spread_too_wide({pct:.4f}>{max_spread})"
            blocked.append(bo)
        else:
            ok.append(o)
    return ok, blocked


def _filter_open_order_symbols(
    orders: list,
    open_orders: list,
) -> tuple:
    """Split orders into (no_conflict, open_order_blocked).

    Any symbol that already has an open order is blocked at planning time with
    skip_reason 'duplicate_open_order'.  The execution gate
    NO_DUPLICATE_OPEN_ORDERS is the independent last line of defense.

    Each blocked entry carries _open_order_info with the available audit
    fields (client_order_id, side, status, submitted_at) for blocked_symbols.
    """
    open_by_symbol: dict = {}
    for oo in open_orders:
        sym = oo.get("symbol")
        if sym and sym not in open_by_symbol:
            open_by_symbol[sym] = oo
    ok: list = []
    blocked: list = []
    for o in orders:
        sym = o["symbol"]
        if sym in open_by_symbol:
            oo = open_by_symbol[sym]
            bo = dict(o)
            bo["skip_reason"] = "duplicate_open_order"
            bo["_open_order_info"] = {
                k: oo.get(k)
                for k in ("client_order_id", "side", "status", "submitted_at")
                if oo.get(k) is not None
            }
            blocked.append(bo)
        else:
            ok.append(o)
    return ok, blocked


def build_trade_plan(
    market_snapshot: dict,
    trigger_snapshot: dict,
    account_snapshot: dict,
    positions: list,
    strategy: dict,
    risk_limits: dict,
    execution_policy: dict,
    sector_map: dict,
    approve_paper: bool = False,
    orders_snapshot: Optional[dict] = None,
    monitor_report: Optional[dict] = None,
) -> dict:
    """Build and return a complete trade plan dict.

    Args:
        market_snapshot:    loaded data/latest/market_snapshot.json
        trigger_snapshot:   loaded data/latest/trigger_snapshot.json
        account_snapshot:   loaded data/latest/account_snapshot.json
        positions:          list from data/latest/positions_snapshot.json ["positions"]
        strategy:           loaded config/strategy.json
        risk_limits:        loaded config/risk_limits.json
        execution_policy:   loaded config/execution_policy.json
        sector_map:         loaded config/sector_map.json
        approve_paper:      set True only with --approve-paper CLI flag
        orders_snapshot:    loaded data/latest/orders_snapshot.json (optional)

    Returns:
        trade_plan dict (always returned, even on gate failure).
    """
    generated_at = utc_now_iso()
    params = strategy.get("parameters", {})
    expiry_minutes: float = float(params.get("plan_expiry_minutes", 360))
    min_order_notional: float = float(params.get("min_order_notional", 25.0))
    max_quote_spread: float = float(
        params.get("max_quote_spread_pct")
        or risk_limits.get("max_quote_spread_pct", 0.02)
    )

    equity = _account_equity(account_snapshot)
    bars_map: dict = market_snapshot.get("bars", {})
    spreads: dict = market_snapshot.get("spreads", {})

    regime: Any = trigger_snapshot.get("regime") or {}
    risk_on: bool = bool(regime.get("risk_on", False))
    selected: list = trigger_snapshot.get("selected", [])
    symbol_results: dict = trigger_snapshot.get("symbol_results", {})
    trigger_snapshot_hash: str = trigger_snapshot.get("trigger_snapshot_hash", "")
    data_hash: str = (
        market_snapshot.get("source_data_hash")
        or market_snapshot.get("data_hash")
        or ""
    )
    strategy_hash: str = stable_hash(strategy)

    # ── Determine no_trade_reasons from gate states ──────────────────────────
    no_trade_reasons: list = []
    stale_gate = trigger_snapshot.get("data_stale_gate") or {}
    if not stale_gate.get("passes", True):
        no_trade_reasons.append(f"data_stale_gate_failed: {stale_gate.get('skip_reason')}")

    # ── Allocate targets ─────────────────────────────────────────────────────
    targets = compute_targets(
        selected=selected,
        symbol_results=symbol_results,
        strategy=strategy,
        risk_on=risk_on,
        equity=equity,
    )

    # Enrich fallback symbols (BIL, SPY) with latest_close from market bars
    targets = _enrich_targets_with_prices(targets, bars_map)

    # ── Compute proposed orders ──────────────────────────────────────────────
    all_orders = compute_proposed_orders(
        targets=targets,
        equity=equity,
        positions=positions,
        min_order_notional=min_order_notional,
    )
    sizer_ok = [o for o in all_orders if o.get("skip_reason") is None]
    sizer_blocked = [o for o in all_orders if o.get("skip_reason") is not None]

    # ── Spread filter at planning time ───────────────────────────────────────
    # Remove any sizer-ok order whose symbol has spread > max_quote_spread_pct
    # in the current market snapshot. These are moved to blocked_symbols with a
    # clear reason. The execution gate SPREAD_NOT_TOO_WIDE re-validates at run
    # time so that any spread widening after planning is also caught.
    proposed_orders, spread_blocked = _filter_wide_spread_orders(
        sizer_ok, spreads, max_quote_spread
    )

    # ── blocked_symbols: trigger excluded + sizer-blocked + spread-blocked ──
    blocked_symbols: list = list(trigger_snapshot.get("excluded", []))
    for o in sizer_blocked:
        blocked_symbols.append({"symbol": o["symbol"], "skip_reason": o["skip_reason"]})
    for o in spread_blocked:
        blocked_symbols.append({"symbol": o["symbol"], "skip_reason": o["skip_reason"]})

    # ── Open-order filter at planning time ───────────────────────────────────
    # Prevents the execution gate NO_DUPLICATE_OPEN_ORDERS from blocking an
    # otherwise-valid plan. Inserted after spread filter so the priority sort
    # and max_orders_per_run cap operate only on non-conflicting candidates —
    # this lets the next eligible symbol fill the slot automatically.
    _open_orders: list = []
    if orders_snapshot:
        raw = orders_snapshot.get("orders", [])
        _open_orders = [o for o in raw if isinstance(o, dict)]

    proposed_orders, open_order_blocked = _filter_open_order_symbols(
        proposed_orders, _open_orders
    )

    def _open_order_blocked_entry(o: dict) -> dict:
        entry: dict = {"symbol": o["symbol"], "skip_reason": "duplicate_open_order"}
        entry.update(o.get("_open_order_info", {}))
        return entry

    for o in open_order_blocked:
        blocked_symbols.append(_open_order_blocked_entry(o))

    open_order_blocked_summary: list = [
        _open_order_blocked_entry(o) for o in open_order_blocked
    ]

    # ── Read per-run caps from risk_limits ──────────────────────────────────
    max_orders_per_run: Optional[int] = (
        int(risk_limits["max_orders_per_run"])
        if risk_limits.get("max_orders_per_run") is not None
        else None
    )
    max_notional_per_order: Optional[float] = (
        float(risk_limits["max_notional_per_order"])
        if risk_limits.get("max_notional_per_order") is not None
        else None
    )

    # ── Churn / cooldown filter ──────────────────────────────────────────────
    # Prevents repeated same-symbol trades and daily over-trading.
    # Runs after open-order filter so the remaining candidates are already clean.
    _lifecycles: list = []
    if monitor_report:
        _lifecycles = [
            lc for lc in monitor_report.get("lifecycles", [])
            if isinstance(lc, dict)
        ]

    proposed_orders, churn_blocked = filter_churn_blocked(
        proposed_orders, _lifecycles, risk_limits, generated_at
    )

    churn_blocked_summary: list = []
    for o in churn_blocked:
        blocked_symbols.append({"symbol": o["symbol"], "skip_reason": o.get("skip_reason", "")})
        churn_blocked_summary.append({"symbol": o["symbol"], "skip_reason": o.get("skip_reason", "")})

    # ── Deterministic priority sort ──────────────────────────────────────────
    # Sell exits sort before buys (reduce risk first).
    # Within buys: highest momentum_score → lowest ATR% → alphabetical.
    def _priority_key(o: dict) -> tuple:
        sym = o["symbol"]
        side = o.get("side", "buy")
        res = symbol_results.get(sym, {})
        score = float(res.get("momentum_score") or 0.0)
        atr_data = res.get("atr") or {}
        atr = float(atr_data.get("atr_pct") or 1.0) if isinstance(atr_data, dict) else 1.0
        side_rank = 0 if side == "sell" else 1
        return (side_rank, -score, atr, sym)

    proposed_orders.sort(key=_priority_key)

    # ── max_orders_per_run cap ───────────────────────────────────────────────
    # Dequeued orders are moved to blocked_symbols; plan remains approvable when
    # at least one order survives the cap.
    orders_run_capped: list = []
    if max_orders_per_run is not None and len(proposed_orders) > max_orders_per_run:
        orders_run_capped = proposed_orders[max_orders_per_run:]
        proposed_orders = proposed_orders[:max_orders_per_run]
        for o in orders_run_capped:
            blocked_symbols.append({
                "symbol": o["symbol"],
                "skip_reason": f"capped_by_max_orders_per_run({max_orders_per_run})",
            })
        dequeued_syms = [o["symbol"] for o in orders_run_capped]
        tag = (
            f"max_orders_per_run_cap({max_orders_per_run})"
            f"_dequeued(non_blocking): {dequeued_syms}"
        )
        no_trade_reasons.append(tag)

    # ── max_notional_per_order cap ───────────────────────────────────────────
    # Cap each proposed order's notional in-place. Orders whose capped notional
    # falls below min_order_notional are moved to blocked_symbols.
    notional_recapped: list = []
    if max_notional_per_order is not None:
        kept: list = []
        for o in proposed_orders:
            o = dict(o)
            if o.get("notional", 0) > max_notional_per_order:
                o["notional"] = round(max_notional_per_order, 2)
                o["capped_by_max_notional_per_order"] = True
            else:
                o["capped_by_max_notional_per_order"] = False
            if o["notional"] < min_order_notional:
                o["skip_reason"] = (
                    f"below_min_notional_after_cap"
                    f"({o['notional']:.2f}<{min_order_notional})"
                )
                blocked_symbols.append({
                    "symbol": o["symbol"],
                    "skip_reason": o["skip_reason"],
                })
                notional_recapped.append(o)
            else:
                kept.append(o)
        proposed_orders = kept

    # ── Risk checks ──────────────────────────────────────────────────────────
    risk_checks = run_risk_checks(
        targets=targets,
        proposed_orders=proposed_orders,
        strategy=strategy,
        risk_limits=risk_limits,
        execution_policy=execution_policy,
        trigger_snapshot_hash=trigger_snapshot_hash,
        data_hash=data_hash,
        sector_map=sector_map,
        spreads=spreads,
        max_quote_spread=max_quote_spread,
        max_orders_per_run=max_orders_per_run,
        max_notional_per_order=max_notional_per_order,
    )
    gates_pass = all_checks_pass(risk_checks)

    # ── Collect additional no-trade reasons from failed checks ───────────────
    failed_checks = [c for c in risk_checks if not c["passes"]]
    for fc in failed_checks:
        no_trade_reasons.append(f"risk_check_failed:{fc['check_id']}")

    # Summarise spread-blocked symbols for auditability.
    # They are always visible in blocked_symbols and spread_blocked_at_planning.
    # Only added to no_trade_reasons when they are the sole reason proposed_orders
    # is empty (so they do not block approval when other valid orders remain).
    spread_blocked_summary: list = [
        {"symbol": o["symbol"], "skip_reason": o["skip_reason"]}
        for o in spread_blocked
    ]
    if spread_blocked_summary and not proposed_orders:
        syms = [o["symbol"] for o in spread_blocked]
        no_trade_reasons.append(f"spread_blocked_all_orders: {syms}")
    elif spread_blocked_summary:
        # Some orders remain — record as informational, not a plan blocker.
        syms = [o["symbol"] for o in spread_blocked]
        no_trade_reasons.append(f"spread_blocked_at_planning(non_blocking): {syms}")

    # Summarise open-order-blocked symbols for auditability.
    if open_order_blocked_summary and not proposed_orders:
        syms = [o["symbol"] for o in open_order_blocked_summary]
        no_trade_reasons.append(f"open_order_blocked_at_planning: {syms}")
    elif open_order_blocked_summary:
        syms = [o["symbol"] for o in open_order_blocked_summary]
        no_trade_reasons.append(f"open_order_blocked_at_planning(non_blocking): {syms}")

    # Summarise churn-blocked symbols for auditability.
    if churn_blocked_summary and not proposed_orders:
        syms = [o["symbol"] for o in churn_blocked_summary]
        no_trade_reasons.append(f"churn_blocked_all_orders: {syms}")
    elif churn_blocked_summary:
        syms = [o["symbol"] for o in churn_blocked_summary]
        no_trade_reasons.append(f"churn_blocked_at_planning(non_blocking): {syms}")

    if not proposed_orders and not no_trade_reasons:
        no_trade_reasons.append("no_actionable_orders")

    # ── Approval ─────────────────────────────────────────────────────────────
    # Informational no_trade_reasons (non_blocking prefix) document exclusions
    # but do not block execution approval when actionable orders remain.
    blocking_reasons = [
        r for r in no_trade_reasons
        if "(non_blocking)" not in r
    ]
    approved_for_execution = gates_pass and approve_paper and not blocking_reasons
    if approved_for_execution:
        approval_reason = "all_risk_checks_pass_and_paper_flag_set"
    elif not gates_pass:
        approval_reason = f"risk_checks_failed: {[c['check_id'] for c in failed_checks]}"
    elif not approve_paper:
        approval_reason = "approve_paper_flag_not_set"
    else:
        approval_reason = "; ".join(no_trade_reasons) or "unknown"

    # ── Account summary for the plan ─────────────────────────────────────────
    acct = account_snapshot.get("account", {})
    account_summary = {
        "equity": acct.get("equity"),
        "cash": acct.get("cash"),
        "buying_power": acct.get("buying_power"),
        "status": acct.get("status"),
        "position_count": account_snapshot.get("position_count", len(positions)),
        "fetched_at": account_snapshot.get("fetched_at"),
    }

    market_clock = account_snapshot.get("clock", {})

    # ── Assemble plan ─────────────────────────────────────────────────────────
    plan_id = _plan_id(generated_at)
    plan: dict = {
        "plan_id": plan_id,
        "generated_at": generated_at,
        "expires_at": _expires_at(generated_at, expiry_minutes),
        "trading_mode": "paper",
        "strategy_hash": strategy_hash,
        "data_hash": data_hash,
        "trigger_snapshot_hash": trigger_snapshot_hash,
        "account_snapshot": account_summary,
        "market_clock": market_clock,
        "regime": regime,
        "targets": targets,
        "proposed_orders": proposed_orders,
        "blocked_symbols": blocked_symbols,
        "spread_blocked_at_planning": spread_blocked_summary,
        "open_order_blocked_at_planning": open_order_blocked_summary,
        "churn_blocked_at_planning": churn_blocked_summary,
        "orders_run_capped_at_planning": [
            {"symbol": o["symbol"], "skip_reason": o.get("skip_reason", "")}
            for o in orders_run_capped
        ],
        "risk_checks": risk_checks,
        "no_trade_reasons": no_trade_reasons,
        "approval": {
            "approved_for_execution": approved_for_execution,
            "all_risk_checks_pass": gates_pass,
            "approve_paper_flag": approve_paper,
            "reason": approval_reason,
        },
    }
    plan["trade_plan_hash"] = stable_hash(
        {k: v for k, v in plan.items() if k != "trade_plan_hash"}
    )
    return plan
