"""Target weight allocator: inverse-ATR position sizing with sector caps.

Pure function — no I/O, no side effects. The allocator takes the already-filtered
selected list from the trigger snapshot and returns target weights for each symbol.

Risk-off  → 100% BIL (cash-like fallback).
Risk-on, no candidates  → 100% SPY (provisional fallback).
Risk-on, with candidates → inverse-ATR, capped at max_position_weight, remainder to BIL.
"""
from __future__ import annotations

from typing import Any, Optional


def _iterative_cap(weights: dict, max_weight: float) -> dict:
    """Cap any weight above max_weight and redistribute excess to uncapped peers.

    Iterates until stable (no symbol exceeds max_weight) or no uncapped peers remain.
    Excess that cannot be redistributed stays implicitly as cash (not returned).
    """
    weights = dict(weights)
    for _ in range(len(weights) + 2):
        over = {s: w for s, w in weights.items() if w > max_weight + 1e-9}
        if not over:
            break
        excess = sum(w - max_weight for w in over.values())
        for s in over:
            weights[s] = max_weight
        under = {s: w for s, w in weights.items() if w < max_weight - 1e-9}
        if not under:
            break
        under_total = sum(under.values())
        if under_total <= 0:
            break
        for s in under:
            add = excess * (weights[s] / under_total)
            weights[s] = min(weights[s] + add, max_weight)
    return weights


def compute_targets(
    selected: list,
    symbol_results: dict,
    strategy: dict,
    risk_on: bool,
    equity: float,
) -> dict:
    """Compute target allocations from the trigger scan result.

    Args:
        selected:        symbol list from trigger_snapshot["selected"]
        symbol_results:  trigger_snapshot["symbol_results"]
        strategy:        loaded config/strategy.json
        risk_on:         trigger_snapshot["regime"]["risk_on"]
        equity:          total portfolio equity (float)

    Returns:
        Dict mapping symbol → target record:
            weight       float  portfolio weight (0–1)
            notional     float  equity * weight
            reason       str    allocation rationale
            atr_pct      float|None   effective ATR% used for sizing
            latest_close float|None   last close price for limit-order price
    """
    params = strategy.get("parameters", {})
    fallbacks = strategy.get("fallbacks", {})
    equity_alloc: float = float(params.get("risk_on_equity_alloc", 0.9))
    max_pos_weight: float = float(params.get("max_position_weight", 0.12))
    min_atr_floor: float = float(params.get("min_atr_pct_floor", 0.01))

    def _fb_entry(sym: str, weight: float, reason: str) -> dict:
        return {
            "weight": round(weight, 8),
            "notional": round(weight * equity, 2),
            "reason": reason,
            "atr_pct": None,
            "latest_close": None,
        }

    # ── Risk-off: target BIL ─────────────────────────────────────────────────
    if not risk_on:
        fb = fallbacks.get("risk_off_target", {"symbol": "BIL", "weight": 1.0})
        return {fb["symbol"]: _fb_entry(fb["symbol"], float(fb["weight"]), "regime_risk_off")}

    # ── Risk-on, no candidates: provisional fallback ─────────────────────────
    if not selected:
        fb = fallbacks.get("risk_on_no_candidates_target", {"symbol": "SPY", "weight": 1.0})
        reason = fallbacks.get("risk_on_no_candidates_reason", "no_candidates_ready")
        return {fb["symbol"]: _fb_entry(fb["symbol"], float(fb["weight"]), reason)}

    # ── Risk-on with candidates: inverse-ATR sizing ──────────────────────────
    atr_info: dict = {}
    for sym in selected:
        res = symbol_results.get(sym, {})
        atr_data = res.get("atr", {})
        raw_atr = atr_data.get("atr_pct")
        effective_atr = max(raw_atr if raw_atr is not None else 0.0, min_atr_floor)
        atr_info[sym] = {
            "effective_atr": effective_atr,
            "raw_atr_pct": raw_atr,
            "latest_close": atr_data.get("latest_close"),
        }

    inv_atr = {sym: 1.0 / atr_info[sym]["effective_atr"] for sym in selected}
    total_inv = sum(inv_atr.values())

    if total_inv <= 0:
        raw_weights = {sym: equity_alloc / len(selected) for sym in selected}
    else:
        raw_weights = {sym: inv_atr[sym] / total_inv * equity_alloc for sym in selected}

    weights = _iterative_cap(raw_weights, max_pos_weight)

    targets: dict = {}
    for sym in selected:
        w = weights[sym]
        targets[sym] = {
            "weight": round(w, 8),
            "notional": round(w * equity, 2),
            "reason": "risk_on_inverse_atr",
            "atr_pct": atr_info[sym]["raw_atr_pct"],
            "latest_close": atr_info[sym]["latest_close"],
        }

    # ── Cash/BIL remainder ───────────────────────────────────────────────────
    cash_weight = max(0.0, 1.0 - sum(weights.values()))
    bil_sym: str = fallbacks.get("risk_off_target", {}).get("symbol", "BIL")
    if cash_weight > 1e-6:
        targets[bil_sym] = {
            "weight": round(cash_weight, 8),
            "notional": round(cash_weight * equity, 2),
            "reason": "cash_allocation",
            "atr_pct": None,
            "latest_close": None,
        }

    return targets
