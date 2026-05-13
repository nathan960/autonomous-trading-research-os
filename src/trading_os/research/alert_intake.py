"""Research-only external alert intake.

Safe intake path for TradingView and other external scanners.
NO execution path — never calls execute_paper.py, never generates
approved trade plans, never places orders.

Every ingested alert has:
  trade_execution_allowed = False  (forced, never overridden by caller)
  blocked_by_default = True        (forced, never overridden by caller)

Allowed next_steps:
  log_only | request_data_refresh | request_alert_review | request_trade_plan_unapproved

Pure functions — no I/O except in process_alert() which writes the alert file
and appends to the trigger log.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Optional

from ..hashing import stable_hash
from ..time_utils import utc_now_iso

ALLOWED_NEXT_STEPS: frozenset = frozenset({
    "log_only",
    "request_data_refresh",
    "request_alert_review",
    "request_trade_plan_unapproved",
})

PROHIBITED_ASSET_CLASSES: frozenset = frozenset({
    "crypto",
    "options",
    "futures",
    "forex",
})

# Forex pairs and crypto pairs use separators
_SYMBOL_SEPARATOR_PATTERN = re.compile(r"[/\-]")

# OCC standard option symbol: 1-6 alpha + 6 digits + C/P + 8 digits
_OCC_OPTION_PATTERN = re.compile(r"^[A-Z]{1,6}\d{6}[CP]\d{8}$")

# Well-known crypto tickers that look like plain equity symbols
_KNOWN_CRYPTO_TICKERS: frozenset = frozenset({
    "BTC", "ETH", "BNB", "SOL", "ADA", "DOGE", "XRP", "DOT", "AVAX",
    "MATIC", "LINK", "UNI", "ATOM", "LTC", "BCH", "ALGO", "FIL", "XLM",
    "VET", "SAND", "MANA", "AXS", "CRO", "FTM", "NEAR", "HBAR", "ICP",
    "TRX", "ETC", "SHIB", "APE",
})

# Characters allowed in normalized file key
_SAFE_KEY_PATTERN = re.compile(r"[^A-Za-z0-9_\-]")


class AlertIntakeError(ValueError):
    """Raised when an alert fails schema validation or is rejected as a duplicate."""

    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(reason)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _is_crypto_symbol(symbol: str) -> bool:
    """Return True if the symbol looks like a crypto asset."""
    if _SYMBOL_SEPARATOR_PATTERN.search(symbol):
        return True
    return symbol.upper() in _KNOWN_CRYPTO_TICKERS


def _is_options_symbol(symbol: str) -> bool:
    """Return True if the symbol matches the OCC option contract format."""
    return bool(_OCC_OPTION_PATTERN.match(symbol.upper()))


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def validate_alert_schema(payload: Any) -> None:
    """Validate the external alert payload schema.

    Checks required fields, allowed next_steps, and prohibited asset classes.
    Does NOT write anything — pure validation only.

    Raises:
        AlertIntakeError  with a human-readable reason on any failure.
    """
    if not isinstance(payload, dict):
        raise AlertIntakeError("payload must be a JSON object")

    symbol = payload.get("symbol")
    if not isinstance(symbol, str) or not symbol.strip():
        raise AlertIntakeError("symbol is required and must be a non-empty string")

    next_step = payload.get("next_step")
    if not isinstance(next_step, str):
        raise AlertIntakeError("next_step is required")
    if next_step not in ALLOWED_NEXT_STEPS:
        raise AlertIntakeError(
            f"next_step={next_step!r} is not in the allowed set; "
            f"permitted values: {sorted(ALLOWED_NEXT_STEPS)}"
        )

    asset_class = payload.get("asset_class")
    if asset_class is not None:
        if not isinstance(asset_class, str):
            raise AlertIntakeError("asset_class must be a string when present")
        if asset_class.lower() in PROHIBITED_ASSET_CLASSES:
            raise AlertIntakeError(
                f"asset_class={asset_class!r} is prohibited; "
                "crypto, options, futures, and forex are not supported"
            )

    if _is_crypto_symbol(symbol):
        raise AlertIntakeError(
            f"symbol={symbol!r} appears to be a crypto asset; crypto is not supported"
        )
    if _is_options_symbol(symbol):
        raise AlertIntakeError(
            f"symbol={symbol!r} matches an options contract format; options are not supported"
        )

    alert_id = payload.get("alert_id")
    if alert_id is not None and not (isinstance(alert_id, str) and alert_id.strip()):
        raise AlertIntakeError("alert_id must be a non-empty string when present")


def process_alert(
    payload: Any,
    alerts_dir: Path,
    trigger_log_path: Path,
) -> dict:
    """Validate, force safety flags, deduplicate, persist, and log an external alert.

    Safety invariants enforced unconditionally:
      - trade_execution_allowed is always False in the persisted record.
      - blocked_by_default is always True in the persisted record.
      - Never calls execute_paper.py or build_trade_plan with approve=True.
      - Never generates an approved trade plan.

    Args:
        payload:           Parsed JSON from the incoming alert (any type; validated here).
        alerts_dir:        Directory to write alert JSON files (created if absent).
        trigger_log_path:  Path to memory/TRIGGER-LOG.md for append-only log entry.

    Returns:
        The normalized alert record that was written.

    Raises:
        AlertIntakeError:  If validation fails or the alert is a duplicate.
    """
    validate_alert_schema(payload)

    raw_hash = stable_hash(payload)

    alert_id: Optional[str] = payload.get("alert_id")
    file_key: str = alert_id if alert_id else raw_hash
    safe_key: str = _SAFE_KEY_PATTERN.sub("_", file_key)
    out_path: Path = alerts_dir / f"alert-{safe_key}.json"

    if out_path.exists():
        raise AlertIntakeError(
            f"duplicate alert — a record already exists for key {file_key!r}"
        )

    ingested_at = utc_now_iso()

    # Build record, stripping any caller-supplied execution flags then forcing them.
    record: dict = {
        k: v
        for k, v in payload.items()
        if k not in ("trade_execution_allowed", "blocked_by_default")
    }
    record["alert_id"] = file_key
    record["raw_payload_hash"] = raw_hash
    record["ingested_at"] = ingested_at
    record["trade_execution_allowed"] = False   # invariant — never True
    record["blocked_by_default"] = True         # invariant — never False

    alerts_dir.mkdir(parents=True, exist_ok=True)
    text = json.dumps(record, indent=2, sort_keys=True, default=str)
    tmp = out_path.with_suffix(".json.tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(out_path)

    _append_trigger_log(record, trigger_log_path)

    return record


def _append_trigger_log(record: dict, log_path: Path) -> None:
    """Append a one-block summary of the ingested alert to TRIGGER-LOG.md."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    if existing and not existing.endswith("\n"):
        existing += "\n"

    summary = {
        "ingested_at": record.get("ingested_at"),
        "alert_id": record.get("alert_id"),
        "source": record.get("source"),
        "symbol": record.get("symbol"),
        "next_step": record.get("next_step"),
        "trade_execution_allowed": record.get("trade_execution_allowed"),
        "blocked_by_default": record.get("blocked_by_default"),
        "raw_payload_hash": record.get("raw_payload_hash"),
    }
    block = (
        "\n## External alert ingested\n\n"
        "```json\n"
        + json.dumps(summary, indent=2, sort_keys=True, default=str)
        + "\n```\n"
    )
    log_path.write_text(existing + block, encoding="utf-8")
