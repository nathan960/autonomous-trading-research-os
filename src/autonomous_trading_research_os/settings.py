from __future__ import annotations

import os
from dataclasses import dataclass


def _truthy(value: str | None) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "y", "on"}


@dataclass(frozen=True)
class RuntimeSettings:
    alpaca_api_key_present: bool
    alpaca_api_secret_present: bool
    trading_mode: str
    alpaca_paper: bool
    live_trading_confirmed: bool
    allow_paper_order_submission: bool
    alpaca_data_feed: str

    @classmethod
    def from_env(cls) -> "RuntimeSettings":
        return cls(
            alpaca_api_key_present=bool(os.getenv("ALPACA_API_KEY")),
            alpaca_api_secret_present=bool(os.getenv("ALPACA_API_SECRET")),
            trading_mode=os.getenv("TRADING_MODE", "paper").strip().lower(),
            alpaca_paper=_truthy(os.getenv("ALPACA_PAPER", "true")),
            live_trading_confirmed=_truthy(os.getenv("LIVE_TRADING_CONFIRMED", "false")),
            allow_paper_order_submission=_truthy(os.getenv("ALLOW_PAPER_ORDER_SUBMISSION", "false")),
            alpaca_data_feed=os.getenv("ALPACA_DATA_FEED", "iex").strip().lower(),
        )

    def validate_paper_only(self) -> None:
        if self.trading_mode != "paper":
            raise RuntimeError("Blocked: TRADING_MODE must be 'paper'. Live trading is not allowed in this project.")
        if not self.alpaca_paper:
            raise RuntimeError("Blocked: ALPACA_PAPER must be true.")
        if self.live_trading_confirmed:
            raise RuntimeError("Blocked: LIVE_TRADING_CONFIRMED must not be true. This project is paper-only.")

    def redacted_summary(self) -> dict[str, object]:
        return {
            "alpaca_api_key_present": self.alpaca_api_key_present,
            "alpaca_api_secret_present": self.alpaca_api_secret_present,
            "trading_mode": self.trading_mode,
            "alpaca_paper": self.alpaca_paper,
            "live_trading_confirmed": self.live_trading_confirmed,
            "allow_paper_order_submission": self.allow_paper_order_submission,
            "alpaca_data_feed": self.alpaca_data_feed,
        }
