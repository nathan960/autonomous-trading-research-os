"""Research-only spread gate diagnostics for Autonomous Trading Research OS.

Classifies spread gate failures to distinguish data/timing issues from real
liquidity problems. All outputs are observations only.

SAFETY:
  - No execution path.
  - Never modifies config/strategy.json, risk_limits.json, or trigger_registry.json.
  - Never loosens or tightens the spread threshold.
  - Never approves trade plans or places orders.
  - No secrets accessed or emitted.
"""
from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from ..config import HISTORY_DIR, LATEST_DIR, MEMORY_DIR
from ..hashing import stable_hash
from ..time_utils import parse_iso_utc, utc_now_iso


# ---------------------------------------------------------------------------
# Constants — never expose or modify risk_limits values from here
# ---------------------------------------------------------------------------

STALE_QUOTE_THRESHOLD_MINUTES: float = 60.0
NEAR_CLOSE_QUOTE_THRESHOLD_MINUTES: float = 10.0
DEFAULT_MAX_SPREAD_PCT: float = 0.02  # fallback only; actual value must come from risk_limits


# ---------------------------------------------------------------------------
# Failure classification values
# ---------------------------------------------------------------------------

FC_PASS = "pass"
FC_MISSING_BID = "missing_bid"
FC_MISSING_ASK = "missing_ask"
FC_ZERO_BID_OR_ASK = "zero_bid_or_ask"
FC_STALE_QUOTE = "stale_quote"
FC_OFF_HOURS = "off_hours_quote"
FC_FEED_LIMITATION = "data_feed_limitation"
FC_WIDE_REAL = "wide_spread_real"
FC_UNKNOWN = "unknown"

_ALL_CLASSES = (
    FC_PASS,
    FC_MISSING_BID,
    FC_MISSING_ASK,
    FC_ZERO_BID_OR_ASK,
    FC_STALE_QUOTE,
    FC_OFF_HOURS,
    FC_FEED_LIMITATION,
    FC_WIDE_REAL,
    FC_UNKNOWN,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_json(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _write_json_atomic(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    tmp.replace(path)


def _safe_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _quote_age_minutes(quote_ts_str: Optional[str], snapshot_ts_str: Optional[str]) -> Optional[float]:
    if not quote_ts_str or not snapshot_ts_str:
        return None
    qt = parse_iso_utc(quote_ts_str)
    st = parse_iso_utc(snapshot_ts_str)
    if qt is None or st is None:
        return None
    delta = (st - qt).total_seconds() / 60.0
    return delta


def _quote_age_bucket(age_minutes: Optional[float]) -> str:
    if age_minutes is None:
        return "unknown"
    if age_minutes < 5:
        return "fresh_lt5m"
    if age_minutes < 30:
        return "recent_5_30m"
    if age_minutes < 60:
        return "stale_30_60m"
    return "stale_gt_60m"


# ---------------------------------------------------------------------------
# Core classification
# ---------------------------------------------------------------------------

def classify_spread_failure(
    bid: Optional[float],
    ask: Optional[float],
    spread_pct: Optional[float],
    quote_ts_str: Optional[str],
    snapshot_ts_str: Optional[str],
    market_is_open: bool,
    max_spread_pct: float,
    data_feed: str = "iex",
) -> str:
    """Classify why a symbol's spread failed (or passed) the gate.

    Returns one of the FC_* constants. Never modifies any config value.
    Pure computation — safe to call from tests or production pipelines.
    """
    # Data-quality failures (quote integrity problems)
    if bid is None:
        return FC_MISSING_BID
    if ask is None:
        return FC_MISSING_ASK
    if bid == 0.0 or ask == 0.0:
        return FC_ZERO_BID_OR_ASK
    if spread_pct is None:
        return FC_UNKNOWN

    # Gate result
    if spread_pct <= max_spread_pct:
        return FC_PASS

    # Spread is above threshold — classify why
    age_minutes = _quote_age_minutes(quote_ts_str, snapshot_ts_str)

    # Market is closed → off-hours quotes are the most likely cause
    if not market_is_open:
        return FC_OFF_HOURS

    # Market was open but quote is stale
    if age_minutes is not None and age_minutes > STALE_QUOTE_THRESHOLD_MINUTES:
        return FC_STALE_QUOTE

    # Market open, fresh quote, IEX feed — IEX-venue-only coverage
    if data_feed and data_feed.lower() == "iex":
        return FC_FEED_LIMITATION

    # Market open, fresh quote, non-IEX feed — genuine wide spread
    return FC_WIDE_REAL


# ---------------------------------------------------------------------------
# Per-symbol analysis
# ---------------------------------------------------------------------------

def analyze_symbol(
    symbol: str,
    quote: dict,
    spread_info: dict,
    market_clock: dict,
    sector: str,
    max_spread_pct: float,
    data_feed: str,
    snapshot_ts: str,
) -> dict:
    """Build a diagnostic record for one symbol. Pure computation."""
    bid = _safe_float(quote.get("bid_price"))
    ask = _safe_float(quote.get("ask_price"))
    spread_pct = _safe_float(spread_info.get("spread_pct"))
    spread = _safe_float(spread_info.get("spread"))
    quote_ts = quote.get("timestamp")
    market_is_open = bool((market_clock or {}).get("is_open"))

    age_minutes = _quote_age_minutes(quote_ts, snapshot_ts)

    failure_class = classify_spread_failure(
        bid, ask, spread_pct, quote_ts, snapshot_ts,
        market_is_open, max_spread_pct, data_feed,
    )

    return {
        "symbol": symbol,
        "sector": sector,
        "bid": bid,
        "ask": ask,
        "spread": spread,
        "spread_pct": spread_pct,
        "quote_timestamp": quote_ts,
        "quote_age_minutes": round(age_minutes, 2) if age_minutes is not None else None,
        "quote_age_bucket": _quote_age_bucket(age_minutes),
        "market_is_open": market_is_open,
        "source_feed": data_feed,
        "max_spread_pct": max_spread_pct,
        "spread_pass": failure_class == FC_PASS,
        "failure_class": failure_class,
    }


# ---------------------------------------------------------------------------
# Aggregation helpers
# ---------------------------------------------------------------------------

def _aggregate_by_failure_class(symbol_records: list) -> dict:
    counts: dict = {c: 0 for c in _ALL_CLASSES}
    for rec in symbol_records:
        fc = rec.get("failure_class", FC_UNKNOWN)
        counts[fc] = counts.get(fc, 0) + 1
    return counts


def _aggregate_by_sector(symbol_records: list) -> dict:
    sector_stats: dict = {}
    for rec in symbol_records:
        sector = rec.get("sector", "Unknown")
        if sector not in sector_stats:
            sector_stats[sector] = {"total": 0, "pass": 0, "fail": 0, "failure_classes": {}}
        s = sector_stats[sector]
        s["total"] += 1
        fc = rec.get("failure_class", FC_UNKNOWN)
        if fc == FC_PASS:
            s["pass"] += 1
        else:
            s["fail"] += 1
        s["failure_classes"][fc] = s["failure_classes"].get(fc, 0) + 1
    return sector_stats


def _aggregate_by_age_bucket(symbol_records: list) -> dict:
    buckets: dict = {}
    for rec in symbol_records:
        b = rec.get("quote_age_bucket", "unknown")
        if b not in buckets:
            buckets[b] = {"total": 0, "pass": 0, "fail": 0}
        b_stats = buckets[b]
        b_stats["total"] += 1
        if rec.get("spread_pass"):
            b_stats["pass"] += 1
        else:
            b_stats["fail"] += 1
    return buckets


def _aggregate_by_market_status(symbol_records: list) -> dict:
    stats: dict = {
        "market_open": {"total": 0, "pass": 0, "fail": 0},
        "market_closed": {"total": 0, "pass": 0, "fail": 0},
    }
    for rec in symbol_records:
        key = "market_open" if rec.get("market_is_open") else "market_closed"
        stats[key]["total"] += 1
        if rec.get("spread_pass"):
            stats[key]["pass"] += 1
        else:
            stats[key]["fail"] += 1
    return stats


def _aggregate_by_feed(symbol_records: list) -> dict:
    feeds: dict = {}
    for rec in symbol_records:
        feed = rec.get("source_feed", "unknown")
        if feed not in feeds:
            feeds[feed] = {"total": 0, "pass": 0, "fail": 0}
        feeds[feed]["total"] += 1
        if rec.get("spread_pass"):
            feeds[feed]["pass"] += 1
        else:
            feeds[feed]["fail"] += 1
    return feeds


# ---------------------------------------------------------------------------
# Findings and recommendations (operational only)
# ---------------------------------------------------------------------------

def _build_findings(symbol_records: list, market_clock: dict, data_feed: str) -> list:
    """Build factual observation list from diagnostic data."""
    findings = []
    by_class = _aggregate_by_failure_class(symbol_records)
    total = len(symbol_records)
    fail_total = sum(v for k, v in by_class.items() if k != FC_PASS)
    is_open = bool((market_clock or {}).get("is_open"))

    if total > 0:
        block_rate = fail_total / total
        findings.append(
            f"{fail_total}/{total} symbols ({block_rate:.0%}) fail the spread gate."
        )

    off_hours_n = by_class.get(FC_OFF_HOURS, 0)
    zero_ask_n = by_class.get(FC_ZERO_BID_OR_ASK, 0)
    stale_n = by_class.get(FC_STALE_QUOTE, 0)
    real_n = by_class.get(FC_WIDE_REAL, 0)
    feed_n = by_class.get(FC_FEED_LIMITATION, 0)

    if not is_open:
        ts = (market_clock or {}).get("timestamp", "")
        next_open = (market_clock or {}).get("next_open", "unknown")
        findings.append(
            f"Market is CLOSED (clock timestamp: {ts}, next open: {next_open}). "
            "Off-hours quotes are unreliable for spread gate evaluation."
        )

    if zero_ask_n > 0:
        findings.append(
            f"{zero_ask_n} symbols have ask_price=0.0 (zero_bid_or_ask). "
            "This is a known IEX behavior at/after market close — ask liquidity disappears "
            "from the IEX venue. These symbols produce spread_pct=null and are blocked."
        )

    if off_hours_n > 0:
        findings.append(
            f"{off_hours_n} symbols have computed spread_pct > threshold while market is closed. "
            "IEX closing-print bid-ask spreads typically range 8–12% and are not representative "
            "of intraday liquidity."
        )

    if data_feed.lower() == "iex":
        findings.append(
            "Data feed is IEX. IEX is an alternative trading venue with partial market coverage. "
            "Quotes reflect IEX-venue activity only, not the National Best Bid and Offer (NBBO). "
            "After-hours IEX spreads are structurally wide regardless of underlying liquidity."
        )

    if stale_n > 0:
        findings.append(
            f"{stale_n} symbols have quotes older than {STALE_QUOTE_THRESHOLD_MINUTES:.0f} minutes "
            "relative to the snapshot timestamp."
        )

    if real_n > 0:
        findings.append(
            f"{real_n} symbols show wide_spread_real: market was open, "
            "quote was fresh, spread exceeded threshold. These are genuine liquidity concerns."
        )

    if feed_n > 0:
        findings.append(
            f"{feed_n} symbols classified as data_feed_limitation: market was open but IEX "
            "quote coverage was insufficient for reliable spread measurement."
        )

    return findings


def _build_recommendations(
    symbol_records: list,
    market_clock: dict,
    data_feed: str,
    max_spread_pct: float,
) -> list:
    """Build operational recommendations. Never recommends threshold changes."""
    recs = []
    by_class = _aggregate_by_failure_class(symbol_records)
    is_open = bool((market_clock or {}).get("is_open"))
    next_open = (market_clock or {}).get("next_open", "unknown")

    off_hours_n = by_class.get(FC_OFF_HOURS, 0)
    zero_ask_n = by_class.get(FC_ZERO_BID_OR_ASK, 0)

    if not is_open and (off_hours_n + zero_ask_n) > 0:
        recs.append({
            "priority": "high",
            "action": "rerun_during_market_hours",
            "detail": (
                f"Market is closed. {off_hours_n} symbols show off_hours_quote and "
                f"{zero_ask_n} show zero_bid_or_ask — both are consistent with post-close "
                f"IEX quote behavior. Re-run diagnose_spreads.py during market hours "
                f"(next open: {next_open}) to evaluate spread gate performance with valid quotes."
            ),
        })

    if data_feed.lower() == "iex":
        recs.append({
            "priority": "medium",
            "action": "verify_alpaca_data_feed",
            "detail": (
                "ALPACA_DATA_FEED=iex. IEX quotes are venue-specific and unreliable after hours. "
                "If a SIP (Nasdaq/NYSE consolidated tape) subscription is available and has been "
                "explicitly approved, verify by checking Alpaca account data permissions. "
                "Do not switch to SIP feed without confirming subscription and approval."
            ),
        })

    if zero_ask_n > 0:
        recs.append({
            "priority": "medium",
            "action": "inspect_quote_timestamps",
            "detail": (
                f"{zero_ask_n} symbols returned ask_price=0.0. "
                "Inspect quote timestamps to confirm these are close-of-day IEX prints. "
                "If timestamps are at market close (20:00 UTC in EDT), "
                "these symbols will likely pass spread gate when re-evaluated during market hours."
            ),
        })

    # Explicit no-threshold-change note
    recs.append({
        "priority": "info",
        "action": "keep_threshold_unchanged",
        "detail": (
            f"max_quote_spread_pct={max_spread_pct} remains unchanged. "
            "Do not adjust the spread threshold based on off-hours or data-quality diagnostic results. "
            "A threshold review requires evidence of persistent wide spreads during market hours "
            "across multiple days of intraday trigger scans."
        ),
    })

    return recs


# ---------------------------------------------------------------------------
# Main build function
# ---------------------------------------------------------------------------

def build_spread_diagnostics(
    market_snapshot: dict,
    data_quality_snapshot: dict,
    risk_limits: dict,
    sector_map: dict,
) -> dict:
    """Build a full spread diagnostics snapshot. Pure computation.

    Args:
        market_snapshot: data/latest/market_snapshot.json
        data_quality_snapshot: data/latest/data_quality_snapshot.json
        risk_limits: config/risk_limits.json
        sector_map: config/sector_map.json

    Returns:
        Diagnostic snapshot dict. Does not read or write any files.
        Never modifies risk_limits or any config value.
    """
    generated_at = utc_now_iso()
    snapshot_ts = market_snapshot.get("generated_at", generated_at)
    market_clock = market_snapshot.get("clock") or {}
    quotes = market_snapshot.get("quotes") or {}
    spreads_map = market_snapshot.get("spreads") or {}
    data_feed = market_snapshot.get("data_feed") or data_quality_snapshot.get("data_feed") or "unknown"

    max_spread_pct: float = float(risk_limits.get("max_quote_spread_pct", DEFAULT_MAX_SPREAD_PCT))

    # Per-symbol records — use universe from spreads_map (matches trigger engine)
    all_symbols = sorted(set(spreads_map.keys()) | set(quotes.keys()))
    symbol_records = []
    for sym in all_symbols:
        quote = quotes.get(sym) or {}
        spread_info = spreads_map.get(sym) or {}
        sector_entry = sector_map.get(sym) or {}
        sector = sector_entry.get("sector", "Unknown")
        rec = analyze_symbol(
            symbol=sym,
            quote=quote,
            spread_info=spread_info,
            market_clock=market_clock,
            sector=sector,
            max_spread_pct=max_spread_pct,
            data_feed=data_feed,
            snapshot_ts=snapshot_ts,
        )
        symbol_records.append(rec)

    by_failure_class = _aggregate_by_failure_class(symbol_records)
    pass_count = by_failure_class.get(FC_PASS, 0)
    fail_count = sum(v for k, v in by_failure_class.items() if k != FC_PASS)
    total = len(symbol_records)

    summary = {
        "total_symbols": total,
        "pass_count": pass_count,
        "fail_count": fail_count,
        "block_rate": round(fail_count / total, 4) if total > 0 else None,
        "by_failure_class": by_failure_class,
        "by_sector": _aggregate_by_sector(symbol_records),
        "by_quote_age_bucket": _aggregate_by_age_bucket(symbol_records),
        "by_market_status": _aggregate_by_market_status(symbol_records),
        "by_feed": _aggregate_by_feed(symbol_records),
    }

    findings = _build_findings(symbol_records, market_clock, data_feed)
    recommendations = _build_recommendations(symbol_records, market_clock, data_feed, max_spread_pct)

    run_id_ts = generated_at.replace(":", "").replace("-", "")[:15]
    payload_for_hash = {
        "snapshot_ts": snapshot_ts,
        "by_failure_class": by_failure_class,
        "total_symbols": total,
    }
    run_hash = stable_hash(payload_for_hash)[:8]
    run_id = f"spread_diagnostics-{run_id_ts}-{run_hash}"

    return {
        "run_id": run_id,
        "generated_at": generated_at,
        "market_snapshot_ts": snapshot_ts,
        "market_is_open": bool(market_clock.get("is_open")),
        "market_clock": market_clock,
        "data_feed": data_feed,
        "max_spread_pct": max_spread_pct,
        "summary": summary,
        "findings": findings,
        "recommendations": recommendations,
        "symbols": symbol_records,
        "no_config_was_modified": True,
        "schema_version": "0.1.0",
    }


# ---------------------------------------------------------------------------
# Output writer
# ---------------------------------------------------------------------------

def _format_data_quality_log_entry(snapshot: dict) -> str:
    s = snapshot.get("summary") or {}
    by_class = s.get("by_failure_class") or {}
    lines = [
        f"## Spread Diagnostics — {snapshot.get('generated_at', '')}",
        "",
        f"**Run ID:** `{snapshot.get('run_id')}`  "
        f"**Market open:** {snapshot.get('market_is_open')}  "
        f"**Feed:** {snapshot.get('data_feed')}",
        "",
        f"**Total:** {s.get('total_symbols')}  **Pass:** {s.get('pass_count')}  "
        f"**Fail:** {s.get('fail_count')}  "
        f"**Block rate:** {s.get('block_rate', 0):.0%}  "
        f"**max_spread_pct:** {snapshot.get('max_spread_pct')}",
        "",
        "**Failure classes:**",
    ]
    for cls in _ALL_CLASSES:
        n = by_class.get(cls, 0)
        if n > 0:
            lines.append(f"- {cls}: {n}")
    lines.append("")
    for finding in snapshot.get("findings") or []:
        lines.append(f"- {finding}")
    lines.append("")
    for rec in snapshot.get("recommendations") or []:
        lines.append(f"- [{rec.get('priority').upper()}] {rec.get('action')}: {rec.get('detail')}")
    lines.append("")
    return "\n".join(lines)


def write_spread_diagnostics(
    snapshot: dict,
    latest_dir: Path,
    history_dir: Path,
    memory_dir: Path,
) -> dict:
    """Write snapshot to latest/, history/, and memory/. Returns written paths."""
    generated_at = snapshot.get("generated_at", utc_now_iso())
    date_str = generated_at[:10]
    run_hash = snapshot.get("run_id", "").split("-")[-1]

    latest_path = latest_dir / "spread_diagnostics.json"
    history_path = history_dir / f"spread_diagnostics_{date_str}-{run_hash}.json"
    dq_log_path = memory_dir / "DATA-QUALITY-LOG.md"

    _write_json_atomic(latest_path, snapshot)
    _write_json_atomic(history_path, snapshot)

    entry = _format_data_quality_log_entry(snapshot)
    with dq_log_path.open("a", encoding="utf-8") as f:
        f.write(entry)

    return {
        "latest_path": str(latest_path),
        "history_path": str(history_path),
        "dq_log_path": str(dq_log_path),
    }
