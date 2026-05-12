"""Pure data-quality assessment functions.

No Alpaca dependency. All functions take plain dicts/lists and return plain dicts.
Suitable for unit testing without credentials or network.
"""
from __future__ import annotations

from typing import Any, Optional

from ..hashing import stable_hash
from ..time_utils import iso_age_minutes, utc_now_iso


# ---------------------------------------------------------------------------
# Individual assessors
# ---------------------------------------------------------------------------

def assess_bar_coverage(
    bars: dict,
    symbols: list,
    min_bars_required: int = 253,
) -> tuple:
    """Return (missing_symbols, insufficient_bar_counts).

    missing_symbols: symbols that have no bars at all.
    insufficient_bar_counts: {symbol: actual_count} for symbols with fewer bars
        than min_bars_required but at least one bar.
    """
    missing: list = [s for s in symbols if s not in bars or not bars[s]]
    insufficient: dict = {
        s: len(bars[s])
        for s in symbols
        if s in bars and bars[s] and len(bars[s]) < min_bars_required
    }
    return missing, insufficient


def assess_quote_coverage(quotes: dict, symbols: list) -> list:
    """Return list of symbols that have no latest quote."""
    return [s for s in symbols if s not in quotes or not isinstance(quotes[s], dict)]


def assess_spread_quality(spreads: dict, max_spread_pct: float = 0.02) -> dict:
    """Return {symbol: spread_pct} for symbols whose spread exceeds max_spread_pct."""
    wide: dict[str, Any] = {}
    for symbol, info in spreads.items():
        if not isinstance(info, dict):
            continue
        spread_pct = info.get("spread_pct")
        if spread_pct is not None:
            try:
                if float(spread_pct) > max_spread_pct:
                    wide[symbol] = spread_pct
            except (TypeError, ValueError):
                pass
    return wide


def assess_snapshot_freshness(
    fetched_at: str,
    max_age_minutes: float = 90.0,
) -> Optional[float]:
    """Return age in minutes since fetched_at, or None if the timestamp is unparseable."""
    return iso_age_minutes(fetched_at)


def assess_asset_tradability(assets: dict, symbols: list) -> list:
    """Return list of symbols that are marked non-tradable or had a fetch error."""
    not_tradable: list = []
    for sym in symbols:
        entry = assets.get(sym)
        if not isinstance(entry, dict):
            not_tradable.append(sym)
            continue
        if not entry.get("tradable", False) or "error" in entry:
            not_tradable.append(sym)
    return not_tradable


# ---------------------------------------------------------------------------
# Full report builder
# ---------------------------------------------------------------------------

def build_quality_report(
    market_snapshot: dict,
    account_snapshot: dict,
    universe_symbols: list,
    min_bars_required: int = 253,
    max_spread_pct: float = 0.02,
    max_snapshot_age_minutes: float = 90.0,
    run_id: str = "",
) -> dict:
    """Assemble a full data-quality report from market and account snapshots.

    Returns a dict suitable for writing to data_quality_snapshot.json and
    appending to memory/DATA-QUALITY-LOG.md.
    """
    generated_at = utc_now_iso()

    bars = market_snapshot.get("bars", {})
    quotes = market_snapshot.get("quotes", {})
    spreads = market_snapshot.get("spreads", {})
    assets = market_snapshot.get("assets", {})
    fetched_at = str(market_snapshot.get("fetched_at") or "")

    # All expected symbols: universe + benchmark/fallbacks always included.
    expected_symbols: list = sorted(set(universe_symbols + ["SPY", "BIL"]))

    missing_bars, insufficient_bars = assess_bar_coverage(
        bars, expected_symbols, min_bars_required
    )
    missing_quotes = assess_quote_coverage(quotes, expected_symbols)
    wide_spreads = assess_spread_quality(spreads, max_spread_pct)
    age_minutes = assess_snapshot_freshness(fetched_at, max_snapshot_age_minutes)
    not_tradable = assess_asset_tradability(assets, expected_symbols)

    issues: list = []
    if missing_bars:
        issues.append("missing_bars")
    if missing_quotes:
        issues.append("missing_quotes")
    if insufficient_bars:
        issues.append("insufficient_bars")
    if wide_spreads:
        issues.append("wide_spreads")
    if age_minutes is None or age_minutes > max_snapshot_age_minutes:
        issues.append("stale_or_unparseable_snapshot")
    if not market_snapshot.get("data_hash"):
        issues.append("missing_data_hash")
    if not_tradable:
        issues.append("non_tradable_symbols")

    report: dict[str, Any] = {
        "schema_version": "0.1.0",
        "run_id": run_id,
        "generated_at": generated_at,
        "status": "PASS" if not issues else "ATTENTION_REQUIRED",
        "issues": issues,
        "snapshot_fetched_at": fetched_at,
        "snapshot_age_minutes": age_minutes,
        "snapshot_source": market_snapshot.get("source"),
        "data_feed": market_snapshot.get("data_feed"),
        "symbols_expected": len(expected_symbols),
        "symbols_with_bars": len(bars),
        "bar_counts": market_snapshot.get("bar_counts", {}),
        "missing_bars": missing_bars,
        "insufficient_bars": insufficient_bars,
        "missing_quotes": missing_quotes,
        "wide_spreads": wide_spreads,
        "not_tradable": not_tradable,
        "position_count": account_snapshot.get("position_count", 0),
        "open_order_count": account_snapshot.get("open_order_count", 0),
        "source_labels": market_snapshot.get("source_labels", {}),
        "market_data_hash": market_snapshot.get("data_hash"),
        "account_data_hash": account_snapshot.get("data_hash"),
    }
    report["data_hash"] = stable_hash(
        {k: v for k, v in report.items() if k != "data_hash"}
    )
    return report
