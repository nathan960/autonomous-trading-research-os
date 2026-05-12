#!/usr/bin/env python3
"""Phase 2 data refresh — fetch Alpaca paper data and write JSON snapshots.

Usage:
    python scripts/refresh_data.py             # real Alpaca paper fetch
    python scripts/refresh_data.py --dry-run   # use mock data (no credentials needed)
    python scripts/refresh_data.py --lookback-days 420

Exit codes:
    0  all snapshots written successfully
    1  validation failure, missing credentials, or fetch error

Safety:
- Fails if TRADING_MODE is not 'paper'.
- Fails if ALPACA_PAPER is not true.
- Never prints API keys, secrets, or credential values.
- Never places orders.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import (
    LATEST_DIR,
    MEMORY_DIR,
    SNAPSHOTS_DIR,
    load_config_file,
)
from trading_os.data.data_quality import build_quality_report
from trading_os.hashing import stable_hash
from trading_os.time_utils import utc_now_iso


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True, default=str)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(path)
    print(f"  wrote {path.relative_to(_ROOT)}")


def _append_quality_log(report: dict) -> None:
    log_path = MEMORY_DIR / "DATA-QUALITY-LOG.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    if existing and not existing.endswith("\n"):
        existing += "\n"
    summary = {
        "run_id": report.get("run_id"),
        "generated_at": report.get("generated_at"),
        "status": report.get("status"),
        "issues": report.get("issues"),
        "snapshot_fetched_at": report.get("snapshot_fetched_at"),
        "snapshot_age_minutes": report.get("snapshot_age_minutes"),
        "symbols_expected": report.get("symbols_expected"),
        "symbols_with_bars": report.get("symbols_with_bars"),
        "missing_bars_count": len(report.get("missing_bars") or []),
        "insufficient_bars_count": len(report.get("insufficient_bars") or {}),
        "not_tradable_count": len(report.get("not_tradable") or []),
        "market_data_hash": report.get("market_data_hash"),
    }
    block = (
        "\n## refresh_data run\n\n"
        "```json\n"
        + json.dumps(summary, indent=2, sort_keys=True, default=str)
        + "\n```\n"
    )
    log_path.write_text(existing + block, encoding="utf-8")


def _archive_snapshot(market_snapshot: dict, fetched_at: str) -> None:
    ts = fetched_at.replace(":", "").replace("-", "").replace("Z", "")
    archive_path = SNAPSHOTS_DIR / f"{ts}_market_snapshot.json"
    _write_json(archive_path, market_snapshot)


# ---------------------------------------------------------------------------
# Mock data path (--dry-run)
# ---------------------------------------------------------------------------

def _mock_account_snapshot() -> dict:
    fetched_at = utc_now_iso()
    payload: dict[str, Any] = {
        "schema_version": "0.1.0",
        "source": "dry_run_mock",
        "fetched_at": fetched_at,
        "account": {
            "equity": "40000.00",
            "cash": "40000.00",
            "buying_power": "40000.00",
            "status": "ACTIVE",
        },
        "positions": [],
        "orders": [],
        "clock": {
            "timestamp": fetched_at,
            "is_open": True,
            "next_open": fetched_at,
            "next_close": fetched_at,
        },
        "position_count": 0,
        "open_order_count": 0,
        "source_labels": {
            "account": "dry_run_mock",
            "positions": "dry_run_mock",
            "orders": "dry_run_mock",
            "clock": "dry_run_mock",
        },
    }
    payload["data_hash"] = stable_hash(
        {k: v for k, v in payload.items() if k != "data_hash"}
    )
    return payload


def _mock_market_snapshot(symbols: list) -> dict:
    from autonomous_trading_research_os.mock_data import generate_market_snapshot

    raw = generate_market_snapshot(symbols)
    # Adapt to the Phase 2 schema.
    fetched_at = raw.get("generated_at", utc_now_iso())
    all_symbols: list = sorted(set(symbols + ["SPY", "BIL"]))
    bars = raw.get("bars", {})
    quotes = raw.get("quotes", {})
    spreads = raw.get("spreads", {})

    # Synthesise per-symbol asset metadata (mock: all tradable).
    assets = {
        sym: {
            "symbol": sym,
            "tradable": True,
            "fractionable": True,
            "status": "active",
            "exchange": "NASDAQ",
            "asset_class": "us_equity",
            "source": "dry_run_mock",
        }
        for sym in all_symbols
    }
    # latest_bars: last bar for each symbol.
    latest_bars = {sym: sb[-1] for sym, sb in bars.items() if sb}

    payload: dict[str, Any] = {
        "schema_version": "0.1.0",
        "source": "dry_run_mock",
        "data_feed": "mock",
        "fetched_at": fetched_at,
        "lookback_days": 420,
        "symbols_requested": all_symbols,
        "bar_counts": {sym: len(b) for sym, b in bars.items()},
        "assets": assets,
        "bars": bars,
        "latest_bars": latest_bars,
        "quotes": quotes,
        "spreads": spreads,
        "source_labels": {
            "bars": "dry_run_mock",
            "latest_bars": "dry_run_mock",
            "quotes": "dry_run_mock",
            "spreads": "dry_run_mock",
            "assets": "dry_run_mock",
        },
    }
    payload["data_hash"] = stable_hash(
        {k: v for k, v in payload.items() if k not in {"data_hash", "bars", "latest_bars", "quotes"}}
    )
    return payload


# ---------------------------------------------------------------------------
# Build combined market_snapshot.json (backward-compatible with Phase 1 readers)
# ---------------------------------------------------------------------------

def _build_combined_snapshot(account: dict, market: dict) -> dict:
    fetched_at = account.get("fetched_at") or market.get("fetched_at") or utc_now_iso()
    combined: dict[str, Any] = {
        "schema_version": "0.1.0",
        "run_mode": "alpaca_paper" if market.get("source") == "alpaca_paper" else "dry_run",
        "generated_at": fetched_at,
        "data_source": market.get("source", "unknown"),
        "data_feed": market.get("data_feed"),
        "account": account.get("account", {}),
        "positions": account.get("positions", []),
        "orders": account.get("orders", []),
        "clock": account.get("clock", {}),
        "bars": market.get("bars", {}),
        "latest_bars": market.get("latest_bars", {}),
        "quotes": market.get("quotes", {}),
        "spreads": market.get("spreads", {}),
        "assets": market.get("assets", {}),
        "source_labels": {
            **(account.get("source_labels") or {}),
            **(market.get("source_labels") or {}),
        },
    }
    combined["source_data_hash"] = stable_hash(
        {k: v for k, v in combined.items() if k != "source_data_hash"}
    )
    return combined


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Phase 2 Alpaca paper data refresh.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Use deterministic mock data instead of live Alpaca calls (no credentials required).",
    )
    parser.add_argument(
        "--lookback-days",
        type=int,
        default=420,
        metavar="N",
        help="Calendar days of historical bar history to fetch (default: 420).",
    )
    args = parser.parse_args()

    print(f"=== refresh_data.py  dry_run={args.dry_run} ===")

    # --- Load config ---------------------------------------------------
    try:
        universe = load_config_file("universe.json")
        strategy = load_config_file("strategy.json")
        risk_limits = load_config_file("risk_limits.json")
    except Exception as exc:
        print(f"FAIL [config]: {exc}")
        return 1

    symbols: list = list(universe.get("symbols", []))
    params = strategy.get("parameters", {})
    min_bars = int(params.get("roc_12m_period", 252)) + 1
    max_spread = float(risk_limits.get("max_quote_spread_pct", 0.02))

    run_id = f"refresh_data-{utc_now_iso().replace(':', '').replace('-', '').replace('Z', '')}"
    print(f"run_id: {run_id}")
    print(f"universe symbols: {len(symbols)}")

    # --- Fetch data ---------------------------------------------------
    try:
        if args.dry_run:
            print("Mode: dry-run mock data")
            account_snapshot = _mock_account_snapshot()
            market_snapshot = _mock_market_snapshot(symbols)
        else:
            print("Mode: Alpaca paper API")
            from trading_os.data.alpaca_client import AlpacaPaperClient
            from trading_os.data.account_state import fetch_account_state
            from trading_os.data.market_data import fetch_market_data

            client = AlpacaPaperClient()
            print(f"  data_feed: {client.data_feed}")
            account_snapshot = fetch_account_state(client)
            market_snapshot = fetch_market_data(client, symbols, lookback_days=args.lookback_days)
    except RuntimeError as exc:
        # RuntimeError covers credential and paper-mode guard failures.
        # We only print the message, never the env var values.
        print(f"FAIL [setup]: {exc}")
        return 1
    except Exception as exc:
        print(f"FAIL [fetch {type(exc).__name__}]: {exc}")
        return 1

    fetched_at = account_snapshot.get("fetched_at") or utc_now_iso()

    # --- Write individual snapshots -----------------------------------
    LATEST_DIR.mkdir(parents=True, exist_ok=True)

    _write_json(
        LATEST_DIR / "account_snapshot.json",
        {k: v for k, v in account_snapshot.items() if k not in {"positions", "orders"}},
    )
    _write_json(
        LATEST_DIR / "positions_snapshot.json",
        {
            "schema_version": "0.1.0",
            "source": account_snapshot.get("source"),
            "fetched_at": fetched_at,
            "positions": account_snapshot.get("positions", []),
            "position_count": account_snapshot.get("position_count", 0),
        },
    )
    _write_json(
        LATEST_DIR / "orders_snapshot.json",
        {
            "schema_version": "0.1.0",
            "source": account_snapshot.get("source"),
            "fetched_at": fetched_at,
            "orders": account_snapshot.get("orders", []),
            "open_order_count": account_snapshot.get("open_order_count", 0),
        },
    )

    # Combined market_snapshot.json (backward-compatible with existing pipeline).
    combined = _build_combined_snapshot(account_snapshot, market_snapshot)
    combined["run_id"] = run_id
    _write_json(LATEST_DIR / "market_snapshot.json", combined)

    # --- Data quality -------------------------------------------------
    quality_report = build_quality_report(
        market_snapshot=market_snapshot,
        account_snapshot=account_snapshot,
        universe_symbols=symbols,
        min_bars_required=min_bars,
        max_spread_pct=max_spread,
        max_snapshot_age_minutes=float(params.get("max_snapshot_age_minutes", 90.0)),
        run_id=run_id,
    )
    _write_json(LATEST_DIR / "data_quality_snapshot.json", quality_report)

    # --- Archive market snapshot -------------------------------------
    _archive_snapshot(combined, fetched_at)

    # --- Update DATA-QUALITY-LOG.md ----------------------------------
    _append_quality_log(quality_report)
    print(f"  appended memory/DATA-QUALITY-LOG.md")

    # --- Summary ------------------------------------------------------
    status = quality_report.get("status", "UNKNOWN")
    issues = quality_report.get("issues", [])
    print(f"\nStatus: {status}")
    if issues:
        print(f"Issues: {', '.join(issues)}")
    else:
        print("No data-quality issues detected.")
    print(f"PASS: refresh_data completed  run_id={run_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
