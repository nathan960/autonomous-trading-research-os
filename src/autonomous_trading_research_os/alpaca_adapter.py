from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from typing import Any

from .file_io import sha256_json, utc_now_iso
from .settings import RuntimeSettings


def _to_primitive(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, (datetime,)):
        return value.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    if isinstance(value, list):
        return [_to_primitive(item) for item in value]
    if isinstance(value, tuple):
        return [_to_primitive(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _to_primitive(item) for key, item in value.items()}
    if hasattr(value, "model_dump"):
        return _to_primitive(value.model_dump())
    if hasattr(value, "dict"):
        return _to_primitive(value.dict())
    if hasattr(value, "__dict__"):
        return _to_primitive({key: item for key, item in vars(value).items() if not key.startswith("_")})
    return str(value)


def _extract_barset(barset: Any) -> dict[str, list[dict[str, Any]]]:
    if hasattr(barset, "data"):
        data = getattr(barset, "data")
        return {str(symbol): [_to_primitive(bar) for bar in bars] for symbol, bars in data.items()}
    if hasattr(barset, "df"):
        df = getattr(barset, "df")
        try:
            reset = df.reset_index()
            out: dict[str, list[dict[str, Any]]] = {}
            for _, row in reset.iterrows():
                item = row.to_dict()
                symbol = str(item.pop("symbol"))
                out.setdefault(symbol, []).append(_to_primitive(item))
            return out
        except Exception:
            pass
    primitive = _to_primitive(barset)
    if isinstance(primitive, dict):
        return {str(k): v if isinstance(v, list) else [v] for k, v in primitive.items()}
    raise RuntimeError("Unable to extract Alpaca barset into a symbol->bars mapping")


def _extract_quotes(quotes: Any) -> dict[str, dict[str, Any]]:
    primitive = _to_primitive(quotes)
    if isinstance(primitive, dict):
        return {str(k): v for k, v in primitive.items() if isinstance(v, dict)}
    raise RuntimeError("Unable to extract Alpaca latest quotes")


class AlpacaAdapter:
    """Thin Alpaca paper-trading adapter.

    Imports alpaca-py lazily so compile checks and dry runs do not require credentials or network.
    """

    def __init__(self, settings: RuntimeSettings | None = None) -> None:
        self.settings = settings or RuntimeSettings.from_env()
        self.settings.validate_paper_only()
        if not (self.settings.alpaca_api_key_present and self.settings.alpaca_api_secret_present):
            raise RuntimeError("Alpaca API key/secret are required for non-dry-run Alpaca calls.")
        self.api_key = os.environ["ALPACA_API_KEY"]
        self.api_secret = os.environ["ALPACA_API_SECRET"]

    def trading_client(self) -> Any:
        from alpaca.trading.client import TradingClient

        return TradingClient(self.api_key, self.api_secret, paper=True)

    def stock_data_client(self) -> Any:
        from alpaca.data.historical import StockHistoricalDataClient

        return StockHistoricalDataClient(self.api_key, self.api_secret)

    def refresh_snapshot(self, universe_symbols: list[str], lookback_days: int = 420) -> dict[str, Any]:
        from alpaca.data.enums import DataFeed
        from alpaca.data.requests import StockBarsRequest, StockLatestQuoteRequest
        from alpaca.data.timeframe import TimeFrame
        from alpaca.trading.requests import GetOrdersRequest

        generated_at = utc_now_iso()
        symbols = sorted(set(universe_symbols + ["SPY", "BIL"]))
        trading_client = self.trading_client()
        data_client = self.stock_data_client()

        account = _to_primitive(trading_client.get_account())
        positions = _to_primitive(trading_client.get_all_positions())
        orders = _to_primitive(trading_client.get_orders(filter=GetOrdersRequest(status="open")))
        clock = _to_primitive(trading_client.get_clock())

        end = datetime.now(timezone.utc)
        start = end - timedelta(days=lookback_days)
        feed = DataFeed.IEX if self.settings.alpaca_data_feed == "iex" else DataFeed.SIP
        bars_request = StockBarsRequest(symbol_or_symbols=symbols, timeframe=TimeFrame.Day, start=start, end=end, feed=feed)
        bars = _extract_barset(data_client.get_stock_bars(bars_request))

        quote_request = StockLatestQuoteRequest(symbol_or_symbols=symbols, feed=feed)
        quotes = _extract_quotes(data_client.get_stock_latest_quote(quote_request))
        spreads: dict[str, dict[str, Any]] = {}
        for symbol, quote in quotes.items():
            bid = float(quote.get("bid_price") or quote.get("bid") or 0.0)
            ask = float(quote.get("ask_price") or quote.get("ask") or 0.0)
            spread = max(0.0, ask - bid) if ask and bid else None
            spreads[symbol] = {
                "symbol": symbol,
                "spread": spread,
                "spread_pct": (spread / ask) if spread is not None and ask else None,
                "source": "derived_from_alpaca_latest_quote",
            }

        snapshot: dict[str, Any] = {
            "schema_version": "0.1.0",
            "run_mode": "alpaca_paper",
            "generated_at": generated_at,
            "data_source": "alpaca_paper",
            "account": account,
            "positions": positions,
            "orders": orders,
            "clock": clock,
            "bars": bars,
            "quotes": quotes,
            "spreads": spreads,
            "source_labels": {
                "account": "alpaca_trading_client.get_account",
                "positions": "alpaca_trading_client.get_all_positions",
                "orders": "alpaca_trading_client.get_orders(open)",
                "clock": "alpaca_trading_client.get_clock",
                "bars": "alpaca_stock_historical_data_client.get_stock_bars",
                "quotes": "alpaca_stock_historical_data_client.get_stock_latest_quote",
                "spreads": "derived_from_alpaca_latest_quote",
            },
        }
        snapshot["source_data_hash"] = sha256_json({k: v for k, v in snapshot.items() if k != "source_data_hash"})
        return snapshot

    def submit_market_order(self, order: dict[str, Any]) -> dict[str, Any]:
        from alpaca.trading.enums import OrderSide, TimeInForce
        from alpaca.trading.requests import MarketOrderRequest

        side = str(order["side"]).lower()
        if side not in {"buy", "sell"}:
            raise RuntimeError(f"Unsupported side: {side}")
        kwargs: dict[str, Any] = {
            "symbol": order["symbol"],
            "side": OrderSide.BUY if side == "buy" else OrderSide.SELL,
            "time_in_force": TimeInForce.DAY,
            "client_order_id": order.get("client_order_id"),
        }
        if side == "buy":
            kwargs["notional"] = str(order["notional"])
        else:
            kwargs["qty"] = str(order["qty"])
        request = MarketOrderRequest(**{k: v for k, v in kwargs.items() if v is not None})
        submitted = self.trading_client().submit_order(request)
        return _to_primitive(submitted)
