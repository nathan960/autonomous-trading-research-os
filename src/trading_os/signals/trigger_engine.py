"""Trigger engine: orchestrate all signal evaluations into a trigger snapshot.

Layer: Trigger Scan (layer 2)

Flow:
  1. DATA_STALE_GATE_V1  — fail-closed if snapshot is too old
  2. Trend filter on all universe symbols (needed for breadth)
  3. SPY regime (SPY_REGIME_200DMA_V1)
  4. Per-symbol: SPREAD_GATE_V1, LIQUIDITY_GATE_V1, MOMENTUM_BLEND_6M_12M_V1, ATR_SIZING_V1
  5. Rank by momentum_score, apply sector caps
  6. Return trigger_snapshot dict with trigger_snapshot_hash
"""
from __future__ import annotations

from typing import Any, Optional

from ..hashing import stable_hash
from ..time_utils import iso_age_minutes, utc_now_iso
from .atr import compute_atr
from .liquidity import compute_liquidity
from .momentum import compute_momentum
from .regime import compute_spy_signals, evaluate_breadth, evaluate_regime
from .sector_caps import apply_sector_caps
from .trend import compute_trend
from ._indicators import closes, sorted_bars

DATA_STALE_GATE_ID = "DATA_STALE_GATE_V1"
SPREAD_GATE_ID = "SPREAD_GATE_V1"


def _symbol_input_hash(symbol: str, bars: list) -> str:
    """Stable hash of key bar metadata for trigger auditability."""
    ordered = sorted_bars(bars)
    bar_count = len(ordered)
    latest_ts: Optional[str] = None
    latest_close: Optional[float] = None
    if ordered:
        last = ordered[-1]
        latest_ts = str(last.get("timestamp") or last.get("t") or last.get("date") or "")
        cl = last.get("close") or last.get("c")
        try:
            latest_close = float(cl)
        except (TypeError, ValueError):
            pass
    return stable_hash({
        "symbol": symbol,
        "bar_count": bar_count,
        "latest_timestamp": latest_ts,
        "latest_close": latest_close,
    })


def _check_data_stale(
    market_snapshot: dict,
    max_age_minutes: float,
) -> dict:
    """Return DATA_STALE_GATE_V1 result."""
    ts = market_snapshot.get("generated_at") or market_snapshot.get("fetched_at") or ""
    age: Optional[float] = iso_age_minutes(ts) if ts else None
    if age is None:
        passes = False
        skip_reason: Any = "snapshot_timestamp_missing"
    elif age > max_age_minutes:
        passes = False
        skip_reason = f"snapshot_stale(age_minutes={age:.1f}>max={max_age_minutes})"
    else:
        passes = True
        skip_reason = None
    return {
        "trigger_id": DATA_STALE_GATE_ID,
        "snapshot_timestamp": ts,
        "age_minutes": age,
        "max_age_minutes": max_age_minutes,
        "passes": passes,
        "skip_reason": skip_reason,
    }


def _check_spread(
    symbol: str,
    spreads: dict,
    max_spread_pct: float,
) -> dict:
    """Return SPREAD_GATE_V1 result for one symbol."""
    spread_info = spreads.get(symbol, {})
    spread_pct: Optional[float] = spread_info.get("spread_pct")
    if spread_pct is None:
        passes = True
        skip_reason: Any = None
    else:
        passes = bool(spread_pct <= max_spread_pct)
        skip_reason = (
            None
            if passes
            else f"spread_too_wide({spread_pct:.4f}>{max_spread_pct})"
        )
    return {
        "trigger_id": SPREAD_GATE_ID,
        "symbol": symbol,
        "spread_pct": spread_pct,
        "max_spread_pct": max_spread_pct,
        "passes": passes,
        "skip_reason": skip_reason,
    }


def run_trigger_scan(
    market_snapshot: dict,
    strategy: dict,
    universe: dict,
    sector_map: dict,
) -> dict:
    """Run the full trigger scan and return a trigger_snapshot dict.

    Args:
        market_snapshot:  loaded data/latest/market_snapshot.json
        strategy:         loaded config/strategy.json
        universe:         loaded config/universe.json
        sector_map:       loaded config/sector_map.json (symbol → {sector, sector_code})

    Returns:
        trigger_snapshot dict, always including trigger_snapshot_hash.
    """
    scanned_at = utc_now_iso()
    params = strategy.get("parameters", {})
    max_snapshot_age: float = float(params.get("max_snapshot_age_minutes", 90))
    max_spread_pct: float = float(params.get("max_quote_spread_pct", 0.02))
    sma_period: int = int(params.get("sma_period", 200))
    roc_6m_period: int = int(params.get("roc_6m_period", 126))
    roc_12m_period: int = int(params.get("roc_12m_period", 252))
    min_momentum_6m: float = float(params.get("min_momentum_6m", 0.0))
    min_momentum_12m: float = float(params.get("min_momentum_12m", 0.0))
    atr_period: int = int(params.get("atr_period", 20))
    breadth_threshold: float = float(params.get("breadth_threshold", 0.55))
    max_holdings: int = int(params.get("max_holdings", 10))
    max_names_per_sector: int = int(params.get("max_names_per_sector", 2))

    symbols: list = universe.get("symbols", [])
    benchmark: str = strategy.get("asset_policy", {}).get("benchmark_symbol", "SPY")
    bars_map: dict = market_snapshot.get("bars", {})
    spreads_map: dict = market_snapshot.get("spreads", {})

    # ── Step 1: data freshness gate ──────────────────────────────────────────
    stale_gate = _check_data_stale(market_snapshot, max_snapshot_age)

    if not stale_gate["passes"]:
        all_skipped = [
            {"symbol": sym, "skip_reason": "data_stale_gate_failed"}
            for sym in symbols
        ]
        snapshot: dict = {
            "scanned_at": scanned_at,
            "data_stale_gate": stale_gate,
            "regime": None,
            "symbol_results": {},
            "candidates": [],
            "selected": [],
            "excluded": all_skipped,
            "sector_counts": {},
        }
        snapshot["trigger_snapshot_hash"] = stable_hash(snapshot)
        return snapshot

    # ── Step 2: trend for all universe symbols (needed for breadth) ──────────
    trend_results: dict = {}
    for sym in symbols:
        bars = bars_map.get(sym, [])
        ih = _symbol_input_hash(sym, bars)
        trend_results[sym] = compute_trend(sym, bars, sma_period=sma_period, input_hash=ih)

    # Breadth uses non-benchmark symbols
    breadth_inputs = [v for k, v in trend_results.items() if k != benchmark]
    breadth_result = evaluate_breadth(breadth_inputs, breadth_threshold=breadth_threshold)

    # ── Step 3: SPY regime ───────────────────────────────────────────────────
    spy_bars = bars_map.get(benchmark, [])
    spy_input_hash = _symbol_input_hash(benchmark, spy_bars)
    spy_signals = compute_spy_signals(spy_bars, sma_period=sma_period, roc_period=roc_6m_period)
    regime = evaluate_regime(spy_signals, breadth_result, input_hash=spy_input_hash)

    # ── Step 4: per-symbol signal evaluation ────────────────────────────────
    symbol_results: dict = {}
    candidates: list = []
    excluded: list = []

    for sym in symbols:
        if sym == benchmark:
            continue
        bars = bars_map.get(sym, [])
        input_hash = trend_results[sym]["input_hash"]

        spread = _check_spread(sym, spreads_map, max_spread_pct)
        liquidity = compute_liquidity(sym, bars, input_hash=input_hash)
        momentum = compute_momentum(
            sym, bars,
            roc_6m_period=roc_6m_period,
            roc_12m_period=roc_12m_period,
            min_momentum_6m=min_momentum_6m,
            min_momentum_12m=min_momentum_12m,
            input_hash=input_hash,
        )
        atr = compute_atr(sym, bars, period=atr_period, input_hash=input_hash)
        trend = trend_results[sym]

        # Determine per-symbol pass/skip
        skip_reason: Any = None
        if not trend["passes"]:
            skip_reason = trend["skip_reason"] or "trend_filter_failed"
        elif not spread["passes"]:
            skip_reason = spread["skip_reason"] or "spread_gate_failed"
        elif not liquidity["passes"]:
            skip_reason = liquidity["skip_reason"] or "liquidity_gate_failed"
        elif not momentum["passes"]:
            skip_reason = momentum["skip_reason"] or "momentum_filter_failed"

        passes = skip_reason is None

        result: dict = {
            "symbol": sym,
            "input_hash": input_hash,
            "passes": passes,
            "skip_reason": skip_reason,
            "trend": trend,
            "spread": spread,
            "liquidity": liquidity,
            "momentum": momentum,
            "atr": atr,
        }
        symbol_results[sym] = result

        if passes:
            candidates.append({
                "symbol": sym,
                "momentum_score": momentum.get("momentum_score"),
                "atr_pct": atr.get("atr_pct"),
                "input_hash": input_hash,
            })
        else:
            excluded.append({"symbol": sym, "skip_reason": skip_reason})

    # ── Step 5: rank by momentum_score, apply sector caps ───────────────────
    ranked = sorted(
        candidates,
        key=lambda c: (c.get("momentum_score") or 0.0),
        reverse=True,
    )

    if not regime["risk_on"]:
        # Regime is risk_off: selected is empty, all candidates move to excluded
        for c in ranked:
            excluded.append({"symbol": c["symbol"], "skip_reason": "regime_risk_off"})
        selected: list = []
        sector_counts: dict = {}
    else:
        selected, sector_counts, cap_excluded = apply_sector_caps(
            ranked, sector_map,
            max_names_per_sector=max_names_per_sector,
            max_holdings=max_holdings,
        )
        excluded.extend(cap_excluded)

    # ── Step 6: assemble snapshot ────────────────────────────────────────────
    snapshot = {
        "scanned_at": scanned_at,
        "data_stale_gate": stale_gate,
        "regime": regime,
        "symbol_results": symbol_results,
        "candidates": [c["symbol"] for c in ranked],
        "selected": [s["symbol"] for s in selected],
        "excluded": excluded,
        "sector_counts": sector_counts,
    }
    snapshot["trigger_snapshot_hash"] = stable_hash(snapshot)
    return snapshot
