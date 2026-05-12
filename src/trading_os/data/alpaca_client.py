"""Thin Alpaca paper-trading client.

Validates paper-only settings at construction. All SDK imports are lazy so that
compile checks, dry runs, and unit tests do not require credentials or network.
Secrets (API key and secret) are read from environment variables only and are
never printed, logged, or returned.
"""
from __future__ import annotations

import os
from datetime import datetime, timezone
from typing import Any


# ---------------------------------------------------------------------------
# SDK-object → primitive conversion helpers
# ---------------------------------------------------------------------------

def _to_primitive(value: Any) -> Any:
    """Recursively convert Alpaca SDK objects to JSON-serialisable primitives."""
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, datetime):
        return (
            value.astimezone(timezone.utc)
            .replace(microsecond=0)
            .isoformat()
            .replace("+00:00", "Z")
        )
    if isinstance(value, (list, tuple)):
        return [_to_primitive(item) for item in value]
    if isinstance(value, dict):
        return {str(k): _to_primitive(v) for k, v in value.items()}
    if hasattr(value, "model_dump"):
        return _to_primitive(value.model_dump())
    if hasattr(value, "dict"):
        return _to_primitive(value.dict())
    if hasattr(value, "__dict__"):
        return _to_primitive(
            {k: v for k, v in vars(value).items() if not k.startswith("_")}
        )
    return str(value)


def _extract_barset(barset: Any) -> dict:
    """Convert an Alpaca barset response to {symbol: [bar, ...]}."""
    if hasattr(barset, "data"):
        data = getattr(barset, "data")
        return {
            str(sym): [_to_primitive(bar) for bar in bars]
            for sym, bars in data.items()
        }
    if hasattr(barset, "df"):
        try:
            df = getattr(barset, "df")
            reset = df.reset_index()
            out: dict = {}
            for _, row in reset.iterrows():
                item = row.to_dict()
                sym = str(item.pop("symbol"))
                out.setdefault(sym, []).append(_to_primitive(item))
            return out
        except Exception:
            pass
    primitive = _to_primitive(barset)
    if isinstance(primitive, dict):
        return {
            str(k): v if isinstance(v, list) else [v]
            for k, v in primitive.items()
        }
    raise RuntimeError("Cannot extract Alpaca barset into {symbol: [bar]} mapping")


def _extract_latest_map(response: Any) -> dict:
    """Convert an Alpaca latest-quote or latest-bar response to {symbol: item}."""
    primitive = _to_primitive(response)
    if isinstance(primitive, dict):
        return {str(k): v for k, v in primitive.items() if isinstance(v, dict)}
    return {}


# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------

class AlpacaPaperClient:
    """Paper-only Alpaca client with upfront safety validation.

    Construction fails if:
    - TRADING_MODE is not 'paper'
    - ALPACA_PAPER is not truthy
    - LIVE_TRADING_CONFIRMED is truthy
    - ALPACA_API_KEY or ALPACA_API_SECRET are absent
    """

    def __init__(self) -> None:
        mode = os.getenv("TRADING_MODE", "paper").strip().lower()
        if mode != "paper":
            raise RuntimeError(
                f"Blocked: TRADING_MODE must be 'paper' (got {mode!r}). "
                "Live trading is not permitted in this system."
            )

        paper_raw = os.getenv("ALPACA_PAPER", "true").strip().lower()
        if paper_raw not in {"1", "true", "yes", "y", "on"}:
            raise RuntimeError("Blocked: ALPACA_PAPER must be true.")

        live_raw = os.getenv("LIVE_TRADING_CONFIRMED", "false").strip().lower()
        if live_raw in {"1", "true", "yes", "y", "on"}:
            raise RuntimeError(
                "Blocked: LIVE_TRADING_CONFIRMED must not be true. "
                "This system is paper-only."
            )

        key = os.environ.get("ALPACA_API_KEY", "").strip()
        secret = os.environ.get("ALPACA_API_SECRET", "").strip()
        if not key:
            raise RuntimeError(
                "ALPACA_API_KEY is not set. "
                "Export it in your shell environment (never write it to .env for cloud use)."
            )
        if not secret:
            raise RuntimeError(
                "ALPACA_API_SECRET is not set. "
                "Export it in your shell environment (never write it to .env for cloud use)."
            )

        # Hold references privately; never expose via __repr__, logs, or return values.
        self.__key = key
        self.__secret = secret
        self.data_feed: str = os.getenv("ALPACA_DATA_FEED", "iex").strip().lower()

    def trading_client(self) -> Any:
        from alpaca.trading.client import TradingClient
        return TradingClient(self.__key, self.__secret, paper=True)

    def stock_data_client(self) -> Any:
        from alpaca.data.historical import StockHistoricalDataClient
        return StockHistoricalDataClient(self.__key, self.__secret)
