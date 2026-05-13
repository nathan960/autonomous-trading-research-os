"""Research-only trigger performance scoring for Autonomous Trading Research OS.

Aggregates trigger scan history, execution records, and trade outcomes to
produce per-trigger performance statistics. All outputs are observations only.

SAFETY:
  - No execution path.
  - Never modifies config/strategy.json, risk_limits.json, or trigger_registry.json.
  - Never approves trade plans.
  - Never places, cancels, or replaces orders.
  - No promotion decisions — all recommendations are research-only.
"""
from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Optional

from ..config import HISTORY_DIR, LATEST_DIR, MEMORY_DIR
from ..hashing import stable_hash
from ..source_integrity import STATUS_DATA_INTEGRITY_BLOCK
from ..time_utils import utc_now_iso


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Minimum fills needed before any P/L conclusion is valid.
MIN_FILL_SAMPLE: int = 20
# Minimum symbol observations needed before trigger stats are reliable.
MIN_SYMBOL_SAMPLE: int = 20

TRIGGER_CATEGORY_MAP: dict = {
    "SPY_REGIME_200DMA_V1": ("market_regime", "SPY above 200-day SMA and 6m momentum positive"),
    "DATA_STALE_GATE_V1": ("data_gate", "Data freshness check"),
    "STOCK_TREND_200DMA_V1": ("stock_trend", "Stock latest close above 200-day SMA"),
    "MOMENTUM_BLEND_6M_12M_V1": ("momentum", "6-month and 12-month ROC momentum blend"),
    "LIQUIDITY_GATE_V1": ("liquidity", "Minimum 20-day average volume"),
    "SPREAD_GATE_V1": ("spread_gate", "Bid-ask spread percentage limit"),
    "ATR_SIZING_V1": ("sizing", "Inverse ATR% position sizing (not a gate)"),
    "SECTOR_CAP": ("plan_layer", "Sector concentration cap"),
    "MAX_HOLDINGS": ("plan_layer", "Maximum total holdings cap"),
    "MAX_ORDERS_PER_RUN": ("plan_layer", "Orders-per-run cap"),
    "DATA_READINESS": ("data_gate", "Insufficient price history for signal computation"),
    "OTHER": ("unknown", "Unclassified block reason"),
}

# Skip-reason string fragments → canonical trigger_id.
_SKIP_PATTERNS: list = [
    ("close_below_200dma", "STOCK_TREND_200DMA_V1"),
    ("spread_too_wide", "SPREAD_GATE_V1"),
    ("roc_6m_below_min", "MOMENTUM_BLEND_6M_12M_V1"),
    ("roc_12m_below_min", "MOMENTUM_BLEND_6M_12M_V1"),
    ("sector_cap", "SECTOR_CAP"),
    ("max_holdings_reached", "MAX_HOLDINGS"),
    ("capped_by_max_orders_per_run", "MAX_ORDERS_PER_RUN"),
    ("max_orders_per_run_cap", "MAX_ORDERS_PER_RUN"),
    ("insufficient_bars", "DATA_READINESS"),
    ("not_ready", "DATA_READINESS"),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_json(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _find_history_files(directory: Path, glob: str) -> list:
    if not directory.is_dir():
        return []
    return sorted(directory.glob(glob))


def _write_json_atomic(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True, default=str)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(path)


def _safe_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _date_range(end_date_str: str, days: int) -> list:
    end = date.fromisoformat(end_date_str)
    return [(end - timedelta(days=i)).isoformat() for i in range(days - 1, -1, -1)]


def skip_reason_to_trigger_id(skip_reason: Optional[str]) -> Optional[str]:
    """Map a skip_reason string to a canonical trigger_id, or None if empty."""
    if not skip_reason:
        return None
    sr = skip_reason.strip().lower()
    if not sr:
        return None
    for fragment, trigger_id in _SKIP_PATTERNS:
        if fragment in sr:
            return trigger_id
    return "OTHER"


def _trigger_category(trigger_id: str) -> tuple:
    return TRIGGER_CATEGORY_MAP.get(trigger_id, ("unknown", trigger_id))


def _avg(values: list) -> Optional[float]:
    floats = [v for v in values if v is not None]
    if not floats:
        return None
    return round(sum(floats) / len(floats), 6)


# ---------------------------------------------------------------------------
# Recommendation engine
# ---------------------------------------------------------------------------

def classify_recommendation(
    trigger_id: str,
    category: str,
    block_rate: Optional[float],
    observation_count: int,
    fill_count: int,
) -> tuple:
    """Return (recommendation_label, reason_string). Never mutates strategy."""

    # Operational issues: high block rate on gates
    if category == "spread_gate" and block_rate is not None and block_rate > 0.50:
        return (
            "operational_issue",
            f"Spread gate blocking {block_rate:.0%} of candidates — "
            "review spread threshold or data freshness.",
        )
    if category == "data_gate" and block_rate is not None and block_rate > 0.30:
        return (
            "operational_issue",
            f"Data gate blocking {block_rate:.0%} of candidates — "
            "check data pipeline health.",
        )

    # Not enough symbol observations to trust the stats
    if observation_count < MIN_SYMBOL_SAMPLE:
        return (
            "needs_more_data",
            f"Only {observation_count} symbol observations — "
            f"need {MIN_SYMBOL_SAMPLE}+ for reliable statistics.",
        )

    # Not enough fills to draw P/L conclusions
    if fill_count < MIN_FILL_SAMPLE:
        return (
            "do_not_promote_yet",
            f"Only {fill_count} fills linked to this trigger — "
            f"need {MIN_FILL_SAMPLE}+ before any strategy conclusion.",
        )

    # Sufficient data but no special flags
    return (
        "candidate_for_review",
        f"{fill_count} fills observed — sufficient for exploratory review. "
        "Requires backtest and peer review before any config change.",
    )


def classify_regime_recommendation(sessions: int) -> tuple:
    if sessions < MIN_SYMBOL_SAMPLE:
        return (
            "keep_observing",
            f"Only {sessions} session(s) — accumulating data.",
        )
    return (
        "candidate_for_review",
        f"{sessions} sessions logged. Regime stability observable. "
        "Do not change strategy from this alone.",
    )


# ---------------------------------------------------------------------------
# Collectors
# ---------------------------------------------------------------------------

def _collect_regime_stats(history_dir: Path, dates: list) -> dict:
    """Aggregate session-level regime stats from JSONL trigger history."""
    total_sessions = 0
    risk_on = 0
    risk_off = 0
    candidate_counts: list = []
    selected_counts: list = []
    excluded_counts: list = []
    regime_errors: list = []

    for date_str in dates:
        trigger_file = history_dir / "triggers" / f"{date_str}.jsonl"
        if not trigger_file.exists():
            continue
        for line in trigger_file.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
            except Exception:
                continue
            total_sessions += 1
            if entry.get("risk_on"):
                risk_on += 1
            else:
                risk_off += 1
                reason = entry.get("regime_skip_reason")
                if reason:
                    regime_errors.append(reason)
            cands = entry.get("candidates", [])
            sels = entry.get("selected", [])
            candidate_counts.append(len(cands))
            selected_counts.append(len(sels))
            excluded_counts.append(entry.get("excluded_count", 0))

    label, reason = classify_regime_recommendation(total_sessions)
    return {
        "trigger_id": "SPY_REGIME_200DMA_V1",
        "category": "market_regime",
        "description": TRIGGER_CATEGORY_MAP["SPY_REGIME_200DMA_V1"][1],
        "sessions_total": total_sessions,
        "sessions_risk_on": risk_on,
        "sessions_risk_off": risk_off,
        "risk_on_pct": round(risk_on / total_sessions, 4) if total_sessions else None,
        "avg_candidates_per_session": _avg(candidate_counts),
        "avg_selected_per_session": _avg(selected_counts),
        "avg_excluded_per_session": _avg(excluded_counts),
        "regime_errors": regime_errors[:10],
        "recommendation": label,
        "recommendation_reason": reason,
    }


def _collect_symbol_trigger_stats(trigger_snapshot: dict) -> dict:
    """Per-trigger pass/fail stats from the latest trigger_snapshot."""
    symbol_results = trigger_snapshot.get("symbol_results", {})
    if not symbol_results:
        return {}

    # Accumulators per trigger_id
    accum: dict = {}

    def _get(tid: str) -> dict:
        if tid not in accum:
            accum[tid] = {
                "passed": 0, "blocked": 0,
                "spreads_passing": [], "spreads_blocked": [],
                "momentum_scores_passing": [], "momentum_scores_blocked": [],
                "atr_pcts": [],
            }
        return accum[tid]

    for symbol, result in symbol_results.items():
        # Spread gate
        spread = result.get("spread", {})
        if spread:
            tid = spread.get("trigger_id", "SPREAD_GATE_V1")
            sp = _safe_float(spread.get("spread_pct"))
            if spread.get("passes"):
                _get(tid)["passed"] += 1
                if sp is not None:
                    _get(tid)["spreads_passing"].append(sp)
            else:
                _get(tid)["blocked"] += 1
                if sp is not None:
                    _get(tid)["spreads_blocked"].append(sp)

        # Trend gate
        trend = result.get("trend", {})
        if trend:
            tid = trend.get("trigger_id", "STOCK_TREND_200DMA_V1")
            if trend.get("passes"):
                _get(tid)["passed"] += 1
            else:
                _get(tid)["blocked"] += 1

        # Momentum gate
        mom = result.get("momentum", {})
        if mom:
            tid = mom.get("trigger_id", "MOMENTUM_BLEND_6M_12M_V1")
            score = _safe_float(mom.get("momentum_score"))
            if mom.get("passes"):
                _get(tid)["passed"] += 1
                if score is not None:
                    _get(tid)["momentum_scores_passing"].append(score)
            else:
                _get(tid)["blocked"] += 1
                if score is not None:
                    _get(tid)["momentum_scores_blocked"].append(score)

        # Liquidity gate
        liq = result.get("liquidity", {})
        if liq:
            tid = liq.get("trigger_id", "LIQUIDITY_GATE_V1")
            if liq.get("passes"):
                _get(tid)["passed"] += 1
            else:
                _get(tid)["blocked"] += 1

        # ATR sizing (informational, not a gate)
        atr = result.get("atr", {})
        if atr:
            tid = atr.get("signal_id", "ATR_SIZING_V1")
            atr_pct = _safe_float(atr.get("atr_pct"))
            if atr_pct is not None:
                _get(tid)["atr_pcts"].append(atr_pct)
            _get(tid)["passed"] += 1  # ATR always passes (sizing, not gate)

    results: dict = {}
    for tid, data in accum.items():
        obs = data["passed"] + data["blocked"]
        block_rate = data["blocked"] / obs if obs > 0 else None
        cat, desc = _trigger_category(tid)

        extra: dict = {}
        if data["spreads_passing"] or data["spreads_blocked"]:
            extra["avg_spread_passing"] = _avg(data["spreads_passing"])
            extra["avg_spread_blocked"] = _avg(data["spreads_blocked"])
        if data["momentum_scores_passing"] or data["momentum_scores_blocked"]:
            extra["avg_momentum_score_passing"] = _avg(data["momentum_scores_passing"])
            extra["avg_momentum_score_blocked"] = _avg(data["momentum_scores_blocked"])
        if data["atr_pcts"]:
            extra["avg_atr_pct"] = _avg(data["atr_pcts"])

        label, reason = classify_recommendation(
            tid, cat, block_rate, obs, fill_count=0
        )
        results[tid] = {
            "trigger_id": tid,
            "category": cat,
            "description": desc,
            "observation_count": obs,
            "passed_count": data["passed"],
            "blocked_count": data["blocked"],
            "block_rate": round(block_rate, 4) if block_rate is not None else None,
            "recommendation": label,
            "recommendation_reason": reason,
            **extra,
        }
    return results


def _collect_plan_layer_stats(trade_plan: dict) -> dict:
    """Collect plan-layer block counts from a trade_plan dict."""
    accum: dict = {}

    def _inc(tid: str) -> None:
        accum[tid] = accum.get(tid, 0) + 1

    for item in trade_plan.get("blocked_symbols", []):
        tid = skip_reason_to_trigger_id(item.get("skip_reason"))
        if tid:
            _inc(tid)

    for item in trade_plan.get("orders_run_capped_at_planning", []):
        _inc("MAX_ORDERS_PER_RUN")

    return accum


def _collect_fill_stats(orders_dir: Path, dates: list) -> dict:
    """Deduplicated fill records from order monitor history."""
    latest_by_order: dict = {}

    for date_str in dates:
        dn = date_str.replace("-", "")
        for f in _find_history_files(orders_dir, f"order_monitor-{dn}T*.json"):
            report = _load_json(f, {})
            if not report:
                continue
            for lc in report.get("lifecycles", []):
                cid = lc.get("client_order_id")
                if not cid:
                    continue
                existing = latest_by_order.get(cid)
                if existing is None or (lc.get("checked_at") or "") >= (existing.get("checked_at") or ""):
                    latest_by_order[cid] = lc

    fills = [lc for lc in latest_by_order.values() if lc.get("lifecycle_status") == "filled"]
    return {
        "total_fills": len(fills),
        "total_tracked": len(latest_by_order),
        "fill_records": fills,
    }


def _collect_outcome_stats(outcome_snapshot: dict) -> dict:
    """Aggregate P/L and slippage from outcome snapshot.

    If the outcome snapshot carries source_integrity_status != 'ok', P/L values
    are blocked and recommendations are marked as data_integrity_block.
    """
    # Check snapshot-level source integrity set by outcome_tracker
    snapshot_integrity = outcome_snapshot.get("source_integrity_status", "ok")
    integrity_blocked = snapshot_integrity != "ok"
    integrity_note = outcome_snapshot.get("source_integrity_note")

    outcomes = outcome_snapshot.get("outcomes", [])

    # Only use returns/slippage from outcomes with clean integrity
    clean_outcomes = [
        o for o in outcomes
        if (o.get("source_integrity_status") or "ok") == "ok"
    ] if not integrity_blocked else []

    slippages = [_safe_float(o.get("slippage_pct")) for o in clean_outcomes if o.get("slippage_pct") is not None]
    returns = [_safe_float(o.get("current_return_pct")) for o in clean_outcomes if o.get("current_return_pct") is not None]

    by_symbol: dict = {}
    for o in outcomes:
        sym = o.get("symbol", "?")
        o_integrity = o.get("source_integrity_status", "ok")
        by_symbol[sym] = {
            "symbol": sym,
            "fill_price": o.get("fill_price"),
            "current_price": o.get("current_price") if o_integrity == "ok" else None,
            "slippage_pct": o.get("slippage_pct"),
            "current_return_pct": o.get("current_return_pct") if o_integrity == "ok" else None,
            "current_unrealized_pl": o.get("current_unrealized_pl") if o_integrity == "ok" else None,
            "filled_at": o.get("filled_at"),
            "entry_or_exit": o.get("entry_or_exit"),
            "source_integrity_status": o_integrity,
        }

    n = len(outcomes)

    if integrity_blocked:
        label = "blocked_mock_source"
        rec = STATUS_DATA_INTEGRITY_BLOCK
        rec_reason = (
            f"P/L scoring blocked — outcome snapshot source_integrity_status="
            f"{snapshot_integrity!r}. "
            + (integrity_note or "Run live Data Refresh to restore canonical snapshots.")
        )
    elif n < MIN_FILL_SAMPLE:
        label = "insufficient_sample"
        rec = "needs_more_data"
        rec_reason = (
            f"Only {n} filled order(s) — need {MIN_FILL_SAMPLE}+ for any P/L conclusions. "
            "Do not change strategy from this sample."
        )
    else:
        label = "sufficient"
        rec = "keep_observing"
        rec_reason = f"{n} fills. Outcome data available for review."

    return {
        "total_outcomes": n,
        "avg_slippage_pct": _avg(slippages) if not integrity_blocked else None,
        "avg_current_return_pct": _avg(returns) if not integrity_blocked else None,
        "by_symbol": by_symbol,
        "sample_status": label,
        "source_integrity_status": snapshot_integrity,
        "source_integrity_note": integrity_note,
        "recommendation": rec,
        "recommendation_reason": rec_reason,
    }


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build_trigger_performance(
    end_date_str: Optional[str] = None,
    days: int = 7,
    latest_dir: Optional[Path] = None,
    history_dir: Optional[Path] = None,
    memory_dir: Optional[Path] = None,
) -> dict:
    """Build a trigger performance report. No I/O side effects."""
    if end_date_str is None:
        end_date_str = date.today().isoformat()
    latest_dir = Path(latest_dir) if latest_dir is not None else LATEST_DIR
    history_dir = Path(history_dir) if history_dir is not None else HISTORY_DIR
    memory_dir = Path(memory_dir) if memory_dir is not None else MEMORY_DIR

    dates = _date_range(end_date_str, days)
    period_start = dates[0]

    trigger_snapshot = _load_json(latest_dir / "trigger_snapshot.json", {})
    trade_plan = _load_json(latest_dir / "trade_plan.json", {})
    outcome_snapshot = _load_json(latest_dir / "outcome_snapshot.json", {})

    orders_dir = history_dir / "orders"

    regime = _collect_regime_stats(history_dir, dates)
    symbol_triggers = _collect_symbol_trigger_stats(trigger_snapshot)
    plan_layer_blocks = _collect_plan_layer_stats(trade_plan)
    fill_stats = _collect_fill_stats(orders_dir, dates)
    outcome_stats = _collect_outcome_stats(outcome_snapshot)

    # Attach plan-layer block counts as simple trigger records
    plan_layer_records: dict = {}
    for tid, block_count in plan_layer_blocks.items():
        cat, desc = _trigger_category(tid)
        label, reason = classify_recommendation(tid, cat, None, block_count, 0)
        plan_layer_records[tid] = {
            "trigger_id": tid,
            "category": cat,
            "description": desc,
            "observation_count": block_count,
            "passed_count": 0,
            "blocked_count": block_count,
            "block_rate": None,
            "recommendation": label,
            "recommendation_reason": reason,
        }

    # Merge: plan_layer_records provides entries for plan-only constraints
    # (SECTOR_CAP, MAX_HOLDINGS, MAX_ORDERS_PER_RUN); symbol_triggers has the
    # richer per-symbol stats and must win for any trigger in both.
    all_triggers = {**plan_layer_records, **symbol_triggers}

    # Collect operational issues
    issues: list = []
    for tid, rec in all_triggers.items():
        if rec.get("recommendation") == "operational_issue":
            issues.append(
                f"Trigger {tid!r} ({rec.get('category')}): {rec.get('recommendation_reason')}"
            )
    if fill_stats["total_fills"] == 0:
        issues.append("No fills recorded this period — verify execution pipeline is active.")

    # Research observations (facts only, no strategy conclusions)
    observations = _generate_observations(regime, all_triggers, fill_stats, outcome_stats)

    now = utc_now_iso()
    run_id = (
        f"trigger_performance-"
        f"{now.replace(':', '').replace('-', '').replace('Z', '')[:15]}"
        f"-{stable_hash({'ts': now})[:8]}"
    )

    perf: dict = {
        "run_id": run_id,
        "generated_at": now,
        "period_start": period_start,
        "period_end": end_date_str,
        "days": days,
        "status": "ok",
        "regime": regime,
        "triggers": all_triggers,
        "fill_outcomes": outcome_stats,
        "execution_fill_stats": {
            "total_fills": fill_stats["total_fills"],
            "total_tracked": fill_stats["total_tracked"],
        },
        "operational_issues": issues,
        "research_observations": observations,
        "safety_note": (
            "All recommendations are research-only observations. "
            "No config files were read for modification. "
            "No strategy changes are implied or permitted from this output."
        ),
    }
    perf["performance_hash"] = stable_hash(
        {k: v for k, v in perf.items() if k != "performance_hash"}
    )[:16]
    return perf


def _generate_observations(
    regime: dict,
    triggers: dict,
    fill_stats: dict,
    outcome_stats: dict,
) -> list:
    obs: list = []

    sessions = regime.get("sessions_total", 0)
    if sessions > 0:
        risk_on_pct = regime.get("risk_on_pct")
        risk_on_str = f"{risk_on_pct:.0%}" if risk_on_pct is not None else "?"
        obs.append(
            f"Regime: {sessions} session(s) scanned, "
            f"{regime.get('sessions_risk_on', 0)} risk-on "
            f"({risk_on_str})."
        )

    spread = triggers.get("SPREAD_GATE_V1", {})
    if spread.get("observation_count", 0) > 0:
        spread_rate = spread.get("block_rate") or 0
        spread_avg_blocked = spread.get("avg_spread_blocked")
        obs.append(
            f"Spread gate: {spread.get('blocked_count', 0)}/{spread.get('observation_count', 0)} "
            f"symbols blocked ({spread_rate:.0%}). "
            f"Avg spread (blocked): {spread_avg_blocked:.3%}"
            if spread_avg_blocked is not None
            else f"Spread gate: {spread.get('blocked_count', 0)}/{spread.get('observation_count', 0)} blocked."
        )

    trend = triggers.get("STOCK_TREND_200DMA_V1", {})
    if trend.get("observation_count", 0) > 0:
        trend_rate = trend.get("block_rate") or 0
        obs.append(
            f"Trend gate (200 DMA): {trend.get('blocked_count', 0)}/{trend.get('observation_count', 0)} "
            f"symbols below 200 DMA ({trend_rate:.0%} block rate)."
        )

    n = fill_stats.get("total_fills", 0)
    obs.append(
        f"Fill count this period: {n}. "
        + (
            f"Need {MIN_FILL_SAMPLE - n} more fills before P/L analysis is meaningful."
            if n < MIN_FILL_SAMPLE
            else "Sufficient fills for exploratory P/L review."
        )
    )

    outcome_integrity = outcome_stats.get("source_integrity_status", "ok")
    if outcome_integrity != "ok":
        obs.append(
            f"P/L DATA BLOCKED: outcome_snapshot source_integrity_status={outcome_integrity!r}. "
            "Current returns are not reported. Run live Data Refresh to restore canonical snapshots."
        )
    else:
        avg_ret = outcome_stats.get("avg_current_return_pct")
        if avg_ret is not None:
            obs.append(
                f"Average current return across {outcome_stats.get('total_outcomes', 0)} "
                f"tracked outcome(s): {avg_ret:+.3%}. "
                "Window pending — no conclusions yet."
            )

    obs.append(
        "IMPORTANT: With only a few paper fills, no trigger should be promoted or "
        "demoted. These observations require 20+ fills and a comparison backtest."
    )
    return obs


# ---------------------------------------------------------------------------
# Format outputs
# ---------------------------------------------------------------------------

def format_experiment_log_entry(perf: dict) -> Optional[str]:
    """Format an EXPERIMENT-LOG.md entry. Returns None if nothing to report."""
    issues = perf.get("operational_issues", [])
    obs = perf.get("research_observations", [])
    if not issues and not obs:
        return None

    lines = [
        f"## Trigger Performance Observations — {perf.get('period_end')}",
        "",
        f"*From trigger_performance run `{perf.get('run_id')}`*",
        f"*Period: {perf.get('period_start')} to {perf.get('period_end')} ({perf.get('days')} days)*",
        "",
    ]
    if issues:
        lines.append("**Operational issues:**")
        for issue in issues:
            lines.append(f"- [ ] {issue}")
        lines.append("")
    if obs:
        lines.append("**Observations (research only — no strategy conclusions):**")
        for o in obs:
            lines.append(f"- {o}")
        lines.append("")
    lines += [
        "**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json",
        "based on this report alone. Any experiment requires a candidate PR with:",
        "- Hypothesis, supporting evidence, success criteria, and rollback plan.",
        "",
        "---",
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Write
# ---------------------------------------------------------------------------

def write_trigger_performance(
    perf: dict,
    latest_dir: Optional[Path] = None,
    tp_history_dir: Optional[Path] = None,
    memory_dir: Optional[Path] = None,
) -> dict:
    """Write trigger performance outputs. Returns paths dict."""
    latest_dir = Path(latest_dir) if latest_dir is not None else LATEST_DIR
    tp_history_dir = (
        Path(tp_history_dir)
        if tp_history_dir is not None
        else HISTORY_DIR / "trigger_performance"
    )
    memory_dir = Path(memory_dir) if memory_dir is not None else MEMORY_DIR

    latest_path = latest_dir / "trigger_performance.json"
    _write_json_atomic(latest_path, perf)

    end_date = perf.get("period_end", "unknown")
    hash8 = (perf.get("performance_hash") or "00000000")[:8]
    history_path = tp_history_dir / f"trigger_performance_{end_date}-{hash8}.json"
    _write_json_atomic(history_path, perf)

    exp_entry = format_experiment_log_entry(perf)
    exp_path = memory_dir / "EXPERIMENT-LOG.md"
    if exp_entry:
        with exp_path.open("a", encoding="utf-8") as fh:
            fh.write(exp_entry)

    return {
        "latest_path": str(latest_path),
        "history_path": str(history_path),
        "experiment_log_path": str(exp_path) if exp_entry else None,
    }
