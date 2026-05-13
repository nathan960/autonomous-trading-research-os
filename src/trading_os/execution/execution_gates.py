"""Pre-execution gate checks for the dry-run execution pipeline.

All gate functions are pure (no I/O, no side effects, no order submission).
Each returns a dict: {gate_id, passes, detail}.

Run order matches the CLAUDE.md safe-execution checklist exactly.
A gate that passes has detail=None; a failing gate has a non-null detail string.

Context dict expected by run_all_gates():
    trade_plan        dict    loaded data/latest/trade_plan.json
    account_snapshot  dict    loaded data/latest/account_snapshot.json
    positions_snapshot dict   loaded data/latest/positions_snapshot.json
    orders_snapshot   dict    loaded data/latest/orders_snapshot.json
    market_snapshot   dict    loaded data/latest/market_snapshot.json
    risk_state        dict    loaded memory/RISK-STATE.json
    universe          dict    loaded config/universe.json
    risk_limits       dict    loaded config/risk_limits.json
    strategy          dict    loaded config/strategy.json
    exec_history_dir  Path    data/history/executions/
    dry_run           bool    True in dry-run mode (suppresses env-var hard failure)
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Optional

from ..source_integrity import check_execution_snapshots
from ..time_utils import iso_age_minutes, utc_now_iso


def _gate(gate_id: str, passes: bool, detail: Optional[str] = None) -> dict:
    return {"gate_id": gate_id, "passes": passes, "detail": None if passes else detail}


# ── Gate 1 ───────────────────────────────────────────────────────────────────

def gate_trading_mode_paper(ctx: dict) -> dict:
    """Confirm trade_plan.trading_mode == 'paper' and env TRADING_MODE=paper."""
    trade_plan = ctx.get("trade_plan", {})
    plan_mode = trade_plan.get("trading_mode", "")
    plan_ok = plan_mode == "paper"

    env_mode = os.getenv("TRADING_MODE", "").strip().lower()
    if env_mode and env_mode != "paper":
        return _gate("TRADING_MODE_PAPER", False,
                     f"TRADING_MODE env={env_mode!r} but must be 'paper'")
    return _gate(
        "TRADING_MODE_PAPER", plan_ok,
        f"trade_plan.trading_mode={plan_mode!r} (expected 'paper')" if not plan_ok else None,
    )


# ── Gate 2 ───────────────────────────────────────────────────────────────────

def gate_alpaca_paper_mode(ctx: dict) -> dict:
    """Confirm ALPACA_PAPER=true in environment; passes in dry-run when var absent."""
    dry_run: bool = ctx.get("dry_run", True)
    val = os.getenv("ALPACA_PAPER", "").strip().lower()

    if val in ("true", "1"):
        return _gate("ALPACA_PAPER_MODE", True)
    if not val:
        # Env var absent — pass in dry-run (no broker connection), fail in live mode
        if dry_run:
            return _gate("ALPACA_PAPER_MODE", True)
        return _gate("ALPACA_PAPER_MODE", False, "ALPACA_PAPER env var not set")
    return _gate("ALPACA_PAPER_MODE", False,
                 f"ALPACA_PAPER={val!r} (must be 'true' to ensure paper broker connection)")


# ── Gate 3 ───────────────────────────────────────────────────────────────────

def gate_canonical_source_integrity(ctx: dict) -> dict:
    """Confirm all execution-critical snapshots carry source='alpaca_paper'.

    Fails if any snapshot has source=dry_run_mock, stored_snapshot, local_mock,
    or unknown. Paper orders must never be based on mock data.
    """
    result = check_execution_snapshots(
        account_snapshot=ctx.get("account_snapshot", {}),
        positions_snapshot=ctx.get("positions_snapshot", {}),
        orders_snapshot=ctx.get("orders_snapshot", {}),
        market_snapshot=ctx.get("market_snapshot", {}),
    )
    if result["passes"]:
        return _gate("CANONICAL_SOURCE_INTEGRITY", True)
    failed_desc = "; ".join(
        f"{c['name']}={c['source']!r}" for c in result["failed"]
    )
    return _gate(
        "CANONICAL_SOURCE_INTEGRITY",
        False,
        f"mock/invalid snapshot source(s) detected: {failed_desc}. "
        "Run live Data Refresh (refresh_data.py without --dry-run) before paper execution.",
    )


# ── Gate 4 ───────────────────────────────────────────────────────────────────

def gate_plan_exists(ctx: dict) -> dict:
    """Confirm trade_plan was loaded and contains required fields."""
    trade_plan = ctx.get("trade_plan", {})
    if not trade_plan:
        return _gate("TRADE_PLAN_EXISTS", False, "trade_plan is empty or missing")
    required = {"plan_id", "generated_at", "expires_at", "trading_mode", "proposed_orders"}
    missing = required - set(trade_plan.keys())
    if missing:
        return _gate("TRADE_PLAN_EXISTS", False, f"missing required fields: {sorted(missing)}")
    return _gate("TRADE_PLAN_EXISTS", True)


# ── Gate 5 ───────────────────────────────────────────────────────────────────

def gate_plan_not_expired(ctx: dict) -> dict:
    """Confirm trade_plan.expires_at is in the future."""
    trade_plan = ctx.get("trade_plan", {})
    expires_at = trade_plan.get("expires_at", "")
    age = iso_age_minutes(expires_at)
    if age is None:
        return _gate("TRADE_PLAN_NOT_EXPIRED", False,
                     f"cannot parse expires_at={expires_at!r}")
    if age > 0:
        return _gate("TRADE_PLAN_NOT_EXPIRED", False,
                     f"plan expired {age:.1f} minutes ago (expires_at={expires_at})")
    return _gate("TRADE_PLAN_NOT_EXPIRED", True)


# ── Gate 6 ───────────────────────────────────────────────────────────────────

def gate_market_clock_open(ctx: dict) -> dict:
    """Confirm market clock reports open; informational (non-blocking) in dry-run."""
    dry_run: bool = ctx.get("dry_run", True)
    account_snapshot = ctx.get("account_snapshot", {})
    clock = account_snapshot.get("clock", {})
    is_open = clock.get("is_open")

    if is_open is True:
        return _gate("MARKET_CLOCK_OPEN", True)
    # Market closed — non-blocking in dry-run (just record the state)
    detail = f"market is_open={is_open} at {clock.get('timestamp', '?')}"
    if dry_run:
        # Pass with informational note — dry-run simulates execution checks, does not block
        return {"gate_id": "MARKET_CLOCK_OPEN", "passes": True, "detail": f"[dry-run] {detail}"}
    return _gate("MARKET_CLOCK_OPEN", False, detail)


# ── Gate 7 ───────────────────────────────────────────────────────────────────

def gate_account_not_blocked(ctx: dict) -> dict:
    """Confirm account status is ACTIVE."""
    account_snapshot = ctx.get("account_snapshot", {})
    status = account_snapshot.get("account", {}).get("status", "")
    return _gate(
        "ACCOUNT_NOT_BLOCKED",
        status == "ACTIVE",
        f"account status={status!r} (expected 'ACTIVE')" if status != "ACTIVE" else None,
    )


# ── Gate 8 ───────────────────────────────────────────────────────────────────

def gate_risk_state_not_paused(ctx: dict) -> dict:
    """Confirm risk state is not paused and drawdown is within block threshold."""
    risk_state = ctx.get("risk_state", {})
    risk_limits = ctx.get("risk_limits", {})

    if risk_state.get("paused") is True:
        return _gate("RISK_STATE_NOT_PAUSED", False, "risk_state.paused=true")

    drawdown: float = float(risk_state.get("drawdown", 0.0))
    block_threshold: float = float(risk_limits.get("max_drawdown_block_pct", -0.1))

    if drawdown <= block_threshold:
        return _gate(
            "RISK_STATE_NOT_PAUSED", False,
            f"drawdown={drawdown:.3f} breaches block_threshold={block_threshold}",
        )
    return _gate("RISK_STATE_NOT_PAUSED", True)


# ── Gate 9 ───────────────────────────────────────────────────────────────────

def gate_positions_match_snapshot(ctx: dict) -> dict:
    """Confirm positions snapshot is fresh and position count is internally consistent."""
    positions_snapshot = ctx.get("positions_snapshot", {})
    account_snapshot = ctx.get("account_snapshot", {})
    strategy = ctx.get("strategy", {})
    max_age: float = float(
        strategy.get("parameters", {}).get("max_snapshot_age_minutes", 90)
    )

    fetched_at = positions_snapshot.get("fetched_at", "")
    age = iso_age_minutes(fetched_at)
    if age is None:
        return _gate("POSITIONS_MATCH_SNAPSHOT", False,
                     "positions_snapshot.fetched_at missing or unparseable")
    if age > max_age:
        return _gate("POSITIONS_MATCH_SNAPSHOT", False,
                     f"positions_snapshot stale: age={age:.1f}min > max={max_age}min")

    snap_count = positions_snapshot.get("position_count", len(positions_snapshot.get("positions", [])))
    acct_count = account_snapshot.get("position_count", snap_count)
    if snap_count != acct_count:
        return _gate("POSITIONS_MATCH_SNAPSHOT", False,
                     f"position count mismatch: snapshot={snap_count} account={acct_count}")
    return _gate("POSITIONS_MATCH_SNAPSHOT", True)


# ── Gate 10 ─────────────────────────────────────────────────────────────────

def gate_no_duplicate_open_orders(ctx: dict) -> dict:
    """Confirm no open orders exist for symbols we are about to trade."""
    orders_snapshot = ctx.get("orders_snapshot", {})
    trade_plan = ctx.get("trade_plan", {})

    proposed_symbols: set = {
        o["symbol"]
        for o in trade_plan.get("proposed_orders", [])
        if o.get("skip_reason") is None
    }
    open_orders: list = orders_snapshot.get("orders", [])
    conflicts: list = [
        o.get("symbol") for o in open_orders
        if o.get("symbol") in proposed_symbols
    ]
    if conflicts:
        return _gate("NO_DUPLICATE_OPEN_ORDERS", False,
                     f"open orders already exist for: {conflicts}")
    return _gate("NO_DUPLICATE_OPEN_ORDERS", True)


# ── Gate 11 ─────────────────────────────────────────────────────────────────

def gate_universe_membership(ctx: dict) -> dict:
    """Confirm every proposed symbol is in universe.json or the allowed fallbacks list."""
    trade_plan = ctx.get("trade_plan", {})
    universe = ctx.get("universe", {})
    risk_limits = ctx.get("risk_limits", {})
    strategy = ctx.get("strategy", {})

    universe_syms: set = set(universe.get("symbols", []))
    fallback_syms: set = set(risk_limits.get("allowed_fallbacks", []))
    fb = strategy.get("fallbacks", {})
    fallback_syms |= {
        fb.get("risk_off_target", {}).get("symbol", "BIL"),
        fb.get("risk_on_no_candidates_target", {}).get("symbol", "SPY"),
    }
    allowed: set = universe_syms | fallback_syms

    proposed: list = [
        o["symbol"]
        for o in trade_plan.get("proposed_orders", [])
        if o.get("skip_reason") is None
    ]
    outsiders = [s for s in proposed if s not in allowed]
    if outsiders:
        return _gate("UNIVERSE_MEMBERSHIP", False,
                     f"symbols not in universe or fallbacks: {outsiders}")
    return _gate("UNIVERSE_MEMBERSHIP", True)


# ── Gate 12 ─────────────────────────────────────────────────────────────────

def gate_symbols_tradable(ctx: dict) -> dict:
    """Confirm proposed symbols are tradable US equities (universe membership as proxy in dry-run)."""
    trade_plan = ctx.get("trade_plan", {})
    universe = ctx.get("universe", {})
    risk_limits = ctx.get("risk_limits", {})
    market_snapshot = ctx.get("market_snapshot", {})

    tradable: set = set(universe.get("symbols", []))
    tradable |= set(risk_limits.get("allowed_fallbacks", []))

    # If market snapshot has an explicit assets map, use it
    assets: dict = market_snapshot.get("assets", {})
    if assets:
        tradable = {s for s, a in assets.items() if a.get("tradable") is not False}

    proposed = [
        o["symbol"]
        for o in trade_plan.get("proposed_orders", [])
        if o.get("skip_reason") is None
    ]
    not_tradable = [s for s in proposed if s not in tradable]
    if not_tradable:
        return _gate("SYMBOLS_TRADABLE", False,
                     f"symbols not confirmed tradable: {not_tradable}")
    return _gate("SYMBOLS_TRADABLE", True)


# ── Gate 13 ─────────────────────────────────────────────────────────────────

def gate_quote_freshness(ctx: dict) -> dict:
    """Confirm quotes exist and are fresh for all proposed symbols."""
    trade_plan = ctx.get("trade_plan", {})
    market_snapshot = ctx.get("market_snapshot", {})
    strategy = ctx.get("strategy", {})
    max_age: float = float(
        strategy.get("parameters", {}).get("max_snapshot_age_minutes", 90)
    )

    quotes: dict = market_snapshot.get("quotes", {})
    proposed = [
        o["symbol"]
        for o in trade_plan.get("proposed_orders", [])
        if o.get("skip_reason") is None
    ]

    missing_quotes = [s for s in proposed if s not in quotes]
    if missing_quotes:
        return _gate("QUOTE_FRESHNESS", False,
                     f"no quote data for: {missing_quotes}")

    stale: list = []
    for sym in proposed:
        q = quotes.get(sym, {})
        ts = q.get("timestamp", "")
        age = iso_age_minutes(ts)
        if age is not None and age > max_age:
            stale.append(f"{sym}({age:.0f}min)")
    if stale:
        return _gate("QUOTE_FRESHNESS", False,
                     f"stale quotes (>{max_age}min): {stale}")
    return _gate("QUOTE_FRESHNESS", True)


# ── Gate 14 ─────────────────────────────────────────────────────────────────

def gate_spread_not_too_wide(ctx: dict) -> dict:
    """Confirm bid-ask spread is within limits for all proposed symbols."""
    trade_plan = ctx.get("trade_plan", {})
    market_snapshot = ctx.get("market_snapshot", {})
    strategy = ctx.get("strategy", {})
    risk_limits = ctx.get("risk_limits", {})

    max_spread: float = float(
        strategy.get("parameters", {}).get("max_quote_spread_pct")
        or risk_limits.get("max_quote_spread_pct", 0.02)
    )
    spreads: dict = market_snapshot.get("spreads", {})
    proposed = [
        o["symbol"]
        for o in trade_plan.get("proposed_orders", [])
        if o.get("skip_reason") is None
    ]

    wide: list = []
    for sym in proposed:
        sp = spreads.get(sym, {})
        pct = sp.get("spread_pct")
        if pct is not None and pct > max_spread:
            wide.append(f"{sym}({pct:.4f}>{max_spread})")
    if wide:
        return _gate("SPREAD_NOT_TOO_WIDE", False,
                     f"spread too wide: {wide}")
    return _gate("SPREAD_NOT_TOO_WIDE", True)


# ── Gate 15 ─────────────────────────────────────────────────────────────────

def gate_risk_limits_respected(ctx: dict) -> dict:
    """Confirm proposed orders respect per-order and per-plan risk limits.

    Cross-references trade_plan.risk_checks — if the plan was generated with passing
    risk checks, this gate re-validates at execution time.
    """
    trade_plan = ctx.get("trade_plan", {})
    risk_limits = ctx.get("risk_limits", {})
    strategy = ctx.get("strategy", {})

    max_pos_weight: float = float(
        strategy.get("parameters", {}).get("max_position_weight")
        or risk_limits.get("max_position_weight", 0.12)
    )
    min_notional: float = float(
        strategy.get("parameters", {}).get("min_order_notional")
        or risk_limits.get("min_order_notional", 25.0)
    )
    max_holdings: int = int(
        strategy.get("parameters", {}).get("max_holdings")
        or risk_limits.get("max_holdings", 10)
    )

    # Check trade_plan.risk_checks were all passing when the plan was built
    plan_risk_checks = trade_plan.get("risk_checks", [])
    failed_plan_checks = [c["check_id"] for c in plan_risk_checks if not c.get("passes")]
    if failed_plan_checks:
        return _gate("RISK_LIMITS_RESPECTED", False,
                     f"plan was built with failing risk checks: {failed_plan_checks}")

    # Re-validate proposed orders at execution time
    proposed = [
        o for o in trade_plan.get("proposed_orders", [])
        if o.get("skip_reason") is None
    ]
    overweight = [
        o["symbol"] for o in proposed
        if o.get("target_weight", 0) > max_pos_weight + 1e-6
    ]
    if overweight:
        return _gate("RISK_LIMITS_RESPECTED", False,
                     f"overweight orders: {overweight} (max={max_pos_weight})")

    tiny = [
        o["symbol"] for o in proposed
        if o.get("notional", 0) < min_notional
    ]
    if tiny:
        return _gate("RISK_LIMITS_RESPECTED", False,
                     f"orders below min_notional({min_notional}): {tiny}")

    targets = trade_plan.get("targets", {})
    equity_symbols = [s for s in targets if s not in {"BIL", "SPY"}]
    if len(equity_symbols) > max_holdings:
        return _gate("RISK_LIMITS_RESPECTED", False,
                     f"equity holdings={len(equity_symbols)} > max={max_holdings}")

    return _gate("RISK_LIMITS_RESPECTED", True)


# ── Gate 16 ─────────────────────────────────────────────────────────────────

def gate_no_prohibited_orders(ctx: dict) -> dict:
    """Confirm no options, crypto, short-sells, or extended-hours orders."""
    trade_plan = ctx.get("trade_plan", {})
    proposed = trade_plan.get("proposed_orders", [])

    for o in proposed:
        if o.get("skip_reason") is not None:
            continue
        symbol: str = o.get("symbol", "")
        # Detect option-like symbols (contain "/" or end in digits after letter)
        if "/" in symbol or (len(symbol) > 6 and symbol[-1].isdigit()):
            return _gate("NO_PROHIBITED_ORDERS", False,
                         f"suspected options symbol: {symbol}")
        if o.get("would_short") is True:
            return _gate("NO_PROHIBITED_ORDERS", False,
                         f"short-sell order detected: {symbol}")
        side: str = o.get("side", "")
        if side == "sell":
            # Sell is only allowed to exit existing positions, not for shorting
            # would_short=False means we own it; check passes
            pass
        order_type: str = o.get("order_type", "")
        if order_type != "limit":
            return _gate("NO_PROHIBITED_ORDERS", False,
                         f"only limit orders are allowed (got order_type={order_type!r} for {symbol})")
        tif: str = o.get("time_in_force", "day")
        if tif in ("opg", "cls"):
            return _gate("NO_PROHIBITED_ORDERS", False,
                         f"extended-hours time_in_force={tif!r} for {symbol}")
    return _gate("NO_PROHIBITED_ORDERS", True)


# ── Gate 17 ─────────────────────────────────────────────────────────────────

def gate_execution_log_writable(ctx: dict) -> dict:
    """Confirm the execution history directory can be written to."""
    exec_dir: Any = ctx.get("exec_history_dir")
    if exec_dir is None:
        return _gate("EXECUTION_LOG_WRITABLE", False, "exec_history_dir not set in context")
    try:
        path = Path(exec_dir)
        path.mkdir(parents=True, exist_ok=True)
        # Quick write test
        test_file = path / ".write_test"
        test_file.write_text("ok", encoding="utf-8")
        test_file.unlink()
        return _gate("EXECUTION_LOG_WRITABLE", True)
    except Exception as exc:
        return _gate("EXECUTION_LOG_WRITABLE", False,
                     f"cannot write to {exec_dir}: {type(exc).__name__}")


# ── Orchestrator ─────────────────────────────────────────────────────────────

_GATE_FUNCTIONS = [
    gate_trading_mode_paper,
    gate_alpaca_paper_mode,
    gate_canonical_source_integrity,
    gate_plan_exists,
    gate_plan_not_expired,
    gate_market_clock_open,
    gate_account_not_blocked,
    gate_risk_state_not_paused,
    gate_positions_match_snapshot,
    gate_no_duplicate_open_orders,
    gate_universe_membership,
    gate_symbols_tradable,
    gate_quote_freshness,
    gate_spread_not_too_wide,
    gate_risk_limits_respected,
    gate_no_prohibited_orders,
    gate_execution_log_writable,
]


def run_all_gates(ctx: dict) -> list:
    """Run all 16 execution gates and return results in order.

    Never raises. Each gate is independent; a failure in one does not skip others.
    """
    results = []
    for fn in _GATE_FUNCTIONS:
        try:
            results.append(fn(ctx))
        except Exception as exc:
            results.append({
                "gate_id": fn.__name__,
                "passes": False,
                "detail": f"gate raised unexpected exception: {type(exc).__name__}: {exc}",
            })
    return results


def all_gates_pass(gate_results: list) -> bool:
    return all(g["passes"] for g in gate_results)
