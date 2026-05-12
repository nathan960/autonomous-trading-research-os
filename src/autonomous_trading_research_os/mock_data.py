from __future__ import annotations

import hashlib
import math
from datetime import datetime, timedelta, timezone
from typing import Any

from .file_io import sha256_json, utc_now_iso


def _seed(symbol: str) -> int:
    return int(hashlib.sha256(symbol.encode("utf-8")).hexdigest()[:8], 16)


def _weekdays(end_date: datetime, count: int) -> list[datetime]:
    days: list[datetime] = []
    cursor = end_date
    while len(days) < count:
        if cursor.weekday() < 5:
            days.append(cursor)
        cursor -= timedelta(days=1)
    return list(reversed(days))


def generate_symbol_bars(symbol: str, count: int = 320, end_date: datetime | None = None) -> list[dict[str, Any]]:
    end = end_date or datetime.now(timezone.utc)
    days = _weekdays(end, count)
    seed = _seed(symbol)
    if symbol == "BIL":
        base = 91.0
        slope = 0.00003
        amplitude = 0.001
    elif symbol == "SPY":
        base = 430.0
        slope = 0.00095
        amplitude = 0.010
    else:
        base = 40.0 + (seed % 350)
        slope = 0.00025 + ((seed % 17) / 17000.0)
        if seed % 7 == 0:
            slope = -0.00020
        amplitude = 0.012 + ((seed % 9) / 1000.0)

    bars: list[dict[str, Any]] = []
    for i, day in enumerate(days):
        wave = amplitude * math.sin((i / 17.0) + (seed % 31))
        drift = 1.0 + slope * i
        close = max(1.0, base * drift * (1.0 + wave))
        open_price = close * (1.0 - 0.002 * math.sin(i / 13.0 + seed % 11))
        high = max(open_price, close) * (1.0 + 0.004 + ((seed % 5) * 0.0004))
        low = min(open_price, close) * (1.0 - 0.004 - ((seed % 3) * 0.0005))
        volume = int(750_000 + (seed % 3_500_000) + i * 500)
        bars.append({
            "timestamp": day.replace(hour=21, minute=0, second=0, microsecond=0).isoformat().replace("+00:00", "Z"),
            "open": round(open_price, 4),
            "high": round(high, 4),
            "low": round(low, 4),
            "close": round(close, 4),
            "volume": volume,
            "source": "dry_run_mock_alpaca_bars",
        })
    return bars


def generate_market_snapshot(universe_symbols: list[str], lookback_bars: int = 320) -> dict[str, Any]:
    generated_at = utc_now_iso()
    symbols = sorted(set(universe_symbols + ["SPY", "BIL"]))
    bars = {symbol: generate_symbol_bars(symbol, lookback_bars) for symbol in symbols}
    quotes: dict[str, dict[str, Any]] = {}
    spreads: dict[str, dict[str, Any]] = {}
    for symbol, symbol_bars in bars.items():
        last_close = symbol_bars[-1]["close"]
        spread_pct = 0.0007 if symbol in {"SPY", "BIL"} else 0.001 + ((_seed(symbol) % 20) / 10000.0)
        bid = last_close * (1.0 - spread_pct / 2.0)
        ask = last_close * (1.0 + spread_pct / 2.0)
        quotes[symbol] = {
            "symbol": symbol,
            "bid_price": round(bid, 4),
            "ask_price": round(ask, 4),
            "timestamp": generated_at,
            "source": "dry_run_mock_alpaca_quote",
        }
        spreads[symbol] = {
            "symbol": symbol,
            "spread": round(ask - bid, 6),
            "spread_pct": round((ask - bid) / ask, 6) if ask > 0 else None,
            "source": "derived_from_dry_run_mock_quote",
        }

    snapshot: dict[str, Any] = {
        "schema_version": "0.1.0",
        "run_mode": "dry_run",
        "generated_at": generated_at,
        "data_source": "dry_run_mock_alpaca_compatible",
        "account": {
            "equity": "40000.00",
            "cash": "40000.00",
            "buying_power": "40000.00",
            "status": "ACTIVE",
            "source": "dry_run_mock_alpaca_account",
        },
        "positions": [],
        "orders": [],
        "clock": {
            "timestamp": generated_at,
            "is_open": True,
            "next_open": generated_at,
            "next_close": generated_at,
            "source": "dry_run_mock_alpaca_clock",
        },
        "bars": bars,
        "quotes": quotes,
        "spreads": spreads,
        "source_labels": {
            "account": "dry_run_mock_alpaca_account",
            "positions": "dry_run_mock_alpaca_positions",
            "orders": "dry_run_mock_alpaca_orders",
            "clock": "dry_run_mock_alpaca_clock",
            "bars": "dry_run_mock_alpaca_bars",
            "quotes": "dry_run_mock_alpaca_quote",
            "spreads": "derived_from_dry_run_mock_quote",
        },
    }
    snapshot["source_data_hash"] = sha256_json({k: v for k, v in snapshot.items() if k != "source_data_hash"})
    return snapshot
