"""Fetch market data from Alpaca paper: historical bars, latest quotes/bars, and asset metadata."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

from ..hashing import stable_hash
from ..time_utils import utc_now_iso
from .alpaca_client import AlpacaPaperClient, _extract_barset, _extract_latest_map, _to_primitive

# 420 calendar days ≈ 290 trading days — enough for 252-day ROC and 200-day SMA.
DEFAULT_LOOKBACK_DAYS = 420


def _compute_spreads(quotes: dict) -> dict:
    spreads: dict[str, dict[str, Any]] = {}
    for symbol, q in quotes.items():
        if not isinstance(q, dict):
            continue
        bid = float(q.get("bid_price") or q.get("bid") or 0.0)
        ask = float(q.get("ask_price") or q.get("ask") or 0.0)
        if ask > 0 and bid > 0:
            spread: Any = max(0.0, ask - bid)
            spread_pct: Any = spread / ask
        else:
            spread = None
            spread_pct = None
        spreads[symbol] = {
            "symbol": symbol,
            "bid": bid if bid > 0 else None,
            "ask": ask if ask > 0 else None,
            "spread": spread,
            "spread_pct": spread_pct,
            "source": "derived_from_alpaca_latest_quote",
        }
    return spreads


def _latest_from_bars(bars: dict) -> dict:
    """Extract the most recent bar for each symbol from the historical bar set."""
    return {sym: sym_bars[-1] for sym, sym_bars in bars.items() if sym_bars}


def _fetch_assets(client: AlpacaPaperClient, symbols: list) -> dict:
    """Fetch tradability metadata for each symbol via a single bulk asset-list call.

    Falls back to per-symbol get_asset() for any symbols not found in the bulk list.
    Unknown symbols are recorded with tradable=False so callers can surface them.
    """
    from alpaca.trading.enums import AssetClass, AssetStatus
    from alpaca.trading.requests import GetAssetsRequest

    trading = client.trading_client()
    symbol_set = set(symbols)
    assets: dict[str, dict[str, Any]] = {}

    try:
        req = GetAssetsRequest(
            asset_class=AssetClass.US_EQUITY,
            status=AssetStatus.ACTIVE,
        )
        for raw in trading.get_all_assets(filter=req):
            entry = _to_primitive(raw)
            if not isinstance(entry, dict):
                continue
            sym = str(entry.get("symbol", ""))
            if sym not in symbol_set:
                continue
            assets[sym] = {
                "symbol": sym,
                "tradable": bool(entry.get("tradable", False)),
                "fractionable": bool(entry.get("fractionable", False)),
                "status": entry.get("status"),
                "exchange": entry.get("exchange"),
                "asset_class": entry.get("class_") or entry.get("asset_class"),
                "source": "alpaca_trading_client.get_all_assets",
            }
    except Exception:
        pass

    # Per-symbol fallback for anything the bulk call missed.
    for sym in symbol_set:
        if sym in assets:
            continue
        try:
            entry = _to_primitive(trading.get_asset(sym))
            if isinstance(entry, dict):
                assets[sym] = {
                    "symbol": sym,
                    "tradable": bool(entry.get("tradable", False)),
                    "fractionable": bool(entry.get("fractionable", False)),
                    "status": entry.get("status"),
                    "exchange": entry.get("exchange"),
                    "asset_class": entry.get("class_") or entry.get("asset_class"),
                    "source": "alpaca_trading_client.get_asset",
                }
            else:
                assets[sym] = {
                    "symbol": sym,
                    "tradable": False,
                    "error": "unexpected_response_type",
                    "source": "alpaca_trading_client.get_asset",
                }
        except Exception as exc:
            assets[sym] = {
                "symbol": sym,
                "tradable": False,
                "error": type(exc).__name__,
                "source": "alpaca_trading_client.get_asset",
            }

    # Any symbol still absent gets a placeholder.
    for sym in symbol_set:
        if sym not in assets:
            assets[sym] = {
                "symbol": sym,
                "tradable": False,
                "error": "not_found",
                "source": "alpaca_trading_client.get_all_assets",
            }

    return assets


def fetch_market_data(
    client: AlpacaPaperClient,
    symbols: list,
    lookback_days: int = DEFAULT_LOOKBACK_DAYS,
) -> dict:
    """Fetch historical bars, latest quotes, latest bars, and asset metadata.

    Always adds SPY and BIL to the symbol set as benchmark/fallback requirements.

    Returns a dict with keys:
        schema_version, source, data_feed, fetched_at, lookback_days,
        symbols_requested, bar_counts, assets,
        bars, latest_bars, quotes, spreads,
        source_labels, data_hash
    """
    from alpaca.data.enums import DataFeed
    from alpaca.data.requests import StockBarsRequest, StockLatestBarRequest, StockLatestQuoteRequest
    from alpaca.data.timeframe import TimeFrame

    fetched_at = utc_now_iso()
    all_symbols: list = sorted(set(list(symbols) + ["SPY", "BIL"]))
    feed = DataFeed.IEX if client.data_feed == "iex" else DataFeed.SIP
    data_client = client.stock_data_client()

    # ---- Historical daily bars ----------------------------------------
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=lookback_days)
    bars = _extract_barset(
        data_client.get_stock_bars(
            StockBarsRequest(
                symbol_or_symbols=all_symbols,
                timeframe=TimeFrame.Day,
                start=start,
                end=end,
                feed=feed,
            )
        )
    )

    # ---- Latest quotes --------------------------------------------------
    quotes = _extract_latest_map(
        data_client.get_stock_latest_quote(
            StockLatestQuoteRequest(symbol_or_symbols=all_symbols, feed=feed)
        )
    )

    # ---- Latest bars ----------------------------------------------------
    try:
        latest_bars = _extract_latest_map(
            data_client.get_stock_latest_bar(
                StockLatestBarRequest(symbol_or_symbols=all_symbols, feed=feed)
            )
        )
    except Exception:
        latest_bars = _latest_from_bars(bars)

    # ---- Asset tradability metadata ------------------------------------
    assets = _fetch_assets(client, all_symbols)

    # ---- Derived spreads ------------------------------------------------
    spreads = _compute_spreads(quotes)

    payload: dict[str, Any] = {
        "schema_version": "0.1.0",
        "source": "alpaca_paper",
        "data_feed": client.data_feed,
        "fetched_at": fetched_at,
        "lookback_days": lookback_days,
        "symbols_requested": all_symbols,
        "bar_counts": {sym: len(b) for sym, b in bars.items()},
        "assets": assets,
        "bars": bars,
        "latest_bars": latest_bars,
        "quotes": quotes,
        "spreads": spreads,
        "source_labels": {
            "bars": "alpaca_stock_historical_data_client.get_stock_bars",
            "latest_bars": "alpaca_stock_historical_data_client.get_stock_latest_bar",
            "quotes": "alpaca_stock_historical_data_client.get_stock_latest_quote",
            "spreads": "derived_from_alpaca_latest_quote",
            "assets": "alpaca_trading_client.get_all_assets",
        },
    }
    # Hash over stable fields — exclude bars/quotes (large, already covered by data_hash of account).
    payload["data_hash"] = stable_hash(
        {
            k: v
            for k, v in payload.items()
            if k not in {"data_hash", "bars", "latest_bars", "quotes"}
        }
    )
    return payload
