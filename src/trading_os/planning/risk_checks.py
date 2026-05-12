"""Deterministic risk checks for a trade plan draft.

Pure function — no I/O, no side effects. Each check returns a dict with:
    check_id    str   unique identifier
    passes      bool  True = gate passes, False = gate blocks
    detail      str|None  human-readable reason (None when passing)

The caller decides what to do with failures. No check raises an exception.
"""
from __future__ import annotations

from typing import Any, Optional


def _check(check_id: str, passes: bool, detail: Optional[str] = None) -> dict:
    return {"check_id": check_id, "passes": passes, "detail": None if passes else detail}


def run_risk_checks(
    targets: dict,
    proposed_orders: list,
    strategy: dict,
    risk_limits: dict,
    execution_policy: dict,
    trigger_snapshot_hash: str,
    data_hash: str,
    sector_map: dict,
    spreads: Optional[dict] = None,
    max_quote_spread: Optional[float] = None,
) -> list:
    """Run all pre-plan risk checks and return a list of check result dicts.

    Args:
        targets:                 allocator output {symbol → target record}
        proposed_orders:         position_sizer output (actionable orders only)
        strategy:                loaded config/strategy.json
        risk_limits:             loaded config/risk_limits.json
        execution_policy:        loaded config/execution_policy.json
        trigger_snapshot_hash:   hash from trigger_snapshot
        data_hash:               hash from market_snapshot
        sector_map:              loaded config/sector_map.json
        spreads:                 market_snapshot["spreads"] for planning-time check
        max_quote_spread:        override threshold (falls back to risk_limits value)

    Returns:
        List of check dicts ordered from most fundamental to most specific.
    """
    checks: list = []
    params = strategy.get("parameters", {})
    max_holdings: int = int(params.get("max_holdings", 10))
    max_pos_weight: float = float(params.get("max_position_weight", 0.12))
    max_names_per_sector: int = int(params.get("max_names_per_sector", 2))
    min_order_notional: float = float(params.get("min_order_notional", 25.0))
    fallback_symbols: set = {
        strategy.get("fallbacks", {}).get("risk_off_target", {}).get("symbol", "BIL"),
        strategy.get("fallbacks", {}).get("risk_on_no_candidates_target", {}).get("symbol", "SPY"),
        *(risk_limits.get("allowed_fallbacks") or []),
    }

    # ── Fundamental mode checks ──────────────────────────────────────────────
    checks.append(_check(
        "TRADING_MODE_PAPER",
        strategy.get("trading_mode") == "paper_only",
        "strategy.trading_mode must be paper_only",
    ))
    checks.append(_check(
        "NO_LIVE_TRADING",
        risk_limits.get("live_trading_allowed") is False,
        "risk_limits.live_trading_allowed must be false",
    ))
    checks.append(_check(
        "PAPER_ONLY_POLICY",
        execution_policy.get("paper_only") is True,
        "execution_policy.paper_only must be true",
    ))

    # ── Data provenance ──────────────────────────────────────────────────────
    checks.append(_check(
        "DATA_HASH_PRESENT",
        bool(data_hash),
        "data_hash is empty — market snapshot may be missing",
    ))
    checks.append(_check(
        "TRIGGER_SNAPSHOT_PRESENT",
        bool(trigger_snapshot_hash),
        "trigger_snapshot_hash is empty — trigger scan may not have run",
    ))

    # ── Asset class / instrument policy ─────────────────────────────────────
    checks.append(_check(
        "NO_OPTIONS",
        execution_policy.get("allow_options") is False,
        "execution_policy.allow_options must be false",
    ))
    checks.append(_check(
        "NO_CRYPTO",
        execution_policy.get("allow_crypto") is False,
        "execution_policy.allow_crypto must be false",
    ))
    checks.append(_check(
        "NO_SHORTING",
        execution_policy.get("allow_shorting") is False,
        "execution_policy.allow_shorting must be false",
    ))

    # ── Order-level short-sell check ─────────────────────────────────────────
    short_orders = [o for o in proposed_orders if o.get("would_short")]
    checks.append(_check(
        "NO_SHORT_SELLS_IN_ORDERS",
        len(short_orders) == 0,
        f"would_short orders detected: {[o['symbol'] for o in short_orders]}",
    ))

    # ── Holdings limits ──────────────────────────────────────────────────────
    equity_targets = [s for s in targets if s not in fallback_symbols]
    checks.append(_check(
        "MAX_HOLDINGS",
        len(equity_targets) <= max_holdings,
        f"equity holdings={len(equity_targets)} exceeds max={max_holdings}",
    ))

    # ── Weight limits ────────────────────────────────────────────────────────
    # Fallback symbols (BIL, SPY) can exceed max_position_weight — they represent
    # cash allocation, not concentrated equity exposure.
    overweight = {
        s: w["weight"]
        for s, w in targets.items()
        if s not in fallback_symbols and w["weight"] > max_pos_weight + 1e-6
    }
    checks.append(_check(
        "MAX_POSITION_WEIGHT",
        len(overweight) == 0,
        f"overweight equity symbols: {overweight}",
    ))

    total_weight = sum(t["weight"] for t in targets.values())
    checks.append(_check(
        "TOTAL_WEIGHT_LIMIT",
        total_weight <= 1.01,
        f"total_weight={total_weight:.4f} exceeds 1.01",
    ))

    # ── Sector concentration ─────────────────────────────────────────────────
    sector_counts: dict = {}
    for sym in equity_targets:
        info = sector_map.get(sym, {})
        code = str(info.get("sector_code") or "UNKNOWN")
        sector_counts[code] = sector_counts.get(code, 0) + 1
    over_sector = {c: n for c, n in sector_counts.items() if n > max_names_per_sector}
    checks.append(_check(
        "SECTOR_CAPS_OK",
        len(over_sector) == 0,
        f"sector over-concentration: {over_sector} (max={max_names_per_sector})",
    ))

    # ── Blocked symbols check ────────────────────────────────────────────────
    blocked_list: list = risk_limits.get("block_symbols") or []
    blocked_in_targets = [s for s in targets if s in blocked_list]
    checks.append(_check(
        "NO_BLOCKED_SYMBOLS_IN_TARGETS",
        len(blocked_in_targets) == 0,
        f"blocked symbols in targets: {blocked_in_targets}",
    ))

    # ── Minimum order notional ───────────────────────────────────────────────
    tiny_orders = [
        o for o in proposed_orders
        if o.get("skip_reason") is None and o.get("notional", 0) < min_order_notional
    ]
    checks.append(_check(
        "MIN_ORDER_NOTIONAL",
        len(tiny_orders) == 0,
        f"orders below min_notional({min_order_notional}): {[o['symbol'] for o in tiny_orders]}",
    ))

    # ── Spread check at planning time ────────────────────────────────────────
    # Verifies that no proposed_order has a spread exceeding the threshold in
    # the market snapshot used for planning. This confirms the spread filter in
    # trade_plan_builder worked correctly. The execution-time gate
    # SPREAD_NOT_TOO_WIDE re-validates with fresh data before any order submission.
    if spreads is not None:
        _max_spread: float = float(
            max_quote_spread
            if max_quote_spread is not None
            else risk_limits.get("max_quote_spread_pct", 0.02)
        )
        wide_in_proposed: list = []
        for o in proposed_orders:
            sym = o["symbol"]
            sp = spreads.get(sym, {})
            pct = sp.get("spread_pct")
            if pct is not None and pct > _max_spread:
                wide_in_proposed.append(f"{sym}({pct:.4f}>{_max_spread})")
        checks.append(_check(
            "SPREAD_OK_AT_PLANNING",
            len(wide_in_proposed) == 0,
            f"proposed orders with wide spread (should have been filtered): {wide_in_proposed}",
        ))

    return checks


def all_checks_pass(checks: list) -> bool:
    """Return True only if every check in the list passes."""
    return all(c["passes"] for c in checks)
