from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .audit import append_event, new_run_id, record_error
from .file_io import parse_iso_datetime, read_json, safe_float, utc_now_iso, write_json
from .paths import CONFIG_DIR, LATEST_DIR, ensure_repo_dirs


def run_data_quality_review() -> dict[str, Any]:
    ensure_repo_dirs()
    run_id = new_run_id("data_quality")
    try:
        strategy = read_json(CONFIG_DIR / "strategy.json", default={})
        universe = read_json(CONFIG_DIR / "universe.json", default={})
        snapshot = read_json(LATEST_DIR / "market_snapshot.json", default={})
        params = strategy.get("parameters", {})
        expected_symbols = sorted(set(universe.get("symbols", []) + universe.get("fallbacks", []) + [universe.get("benchmark", "SPY")]))
        bars = snapshot.get("bars", {}) if isinstance(snapshot.get("bars"), dict) else {}
        quotes = snapshot.get("quotes", {}) if isinstance(snapshot.get("quotes"), dict) else {}
        spreads = snapshot.get("spreads", {}) if isinstance(snapshot.get("spreads"), dict) else {}

        missing_bars = [symbol for symbol in expected_symbols if symbol not in bars or not bars.get(symbol)]
        missing_quotes = [symbol for symbol in expected_symbols if symbol not in quotes]
        min_bars_needed = int(params.get("roc_12m_period", 252)) + 1
        insufficient_bars = {symbol: len(items) for symbol, items in bars.items() if symbol in expected_symbols and len(items) < min_bars_needed}
        max_spread_pct = safe_float(params.get("max_quote_spread_pct"), 0.02)
        wide_spreads = {symbol: item.get("spread_pct") for symbol, item in spreads.items() if safe_float(item.get("spread_pct"), 0.0) > max_spread_pct}

        generated_at = parse_iso_datetime(str(snapshot.get("generated_at") or ""))
        age_minutes = None if generated_at is None else (datetime.now(timezone.utc) - generated_at).total_seconds() / 60.0
        max_age = safe_float(params.get("max_snapshot_age_minutes"), 90.0)
        issues: list[str] = []
        if missing_bars:
            issues.append("missing_bars")
        if missing_quotes:
            issues.append("missing_quotes")
        if insufficient_bars:
            issues.append("insufficient_bars")
        if wide_spreads:
            issues.append("wide_spreads")
        if age_minutes is None or age_minutes > max_age:
            issues.append("stale_snapshot")
        if not snapshot.get("source_data_hash"):
            issues.append("missing_source_data_hash")

        report: dict[str, Any] = {
            "schema_version": "0.1.0",
            "run_id": run_id,
            "generated_at": utc_now_iso(),
            "snapshot_generated_at": snapshot.get("generated_at"),
            "snapshot_age_minutes": age_minutes,
            "status": "PASS" if not issues else "ATTENTION_REQUIRED",
            "issues": issues,
            "missing_bars": missing_bars,
            "missing_quotes": missing_quotes,
            "insufficient_bars": insufficient_bars,
            "wide_spreads": wide_spreads,
            "source_labels": snapshot.get("source_labels", {}),
            "source_data_hash": snapshot.get("source_data_hash"),
        }
        write_json(LATEST_DIR / "data_quality_report.json", report)
        append_event("DATA-QUALITY-LOG.md", "Data quality review completed", report)
        return report
    except Exception as exc:
        record_error("data_quality", exc)
        raise
