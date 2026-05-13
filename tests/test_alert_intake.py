"""Tests for the research-only external alert intake layer.

Key invariants proven here:
- Valid alerts are accepted and persisted.
- trade_execution_allowed is ALWAYS False in the output record, regardless of input.
- blocked_by_default is ALWAYS True in the output record, regardless of input.
- Duplicate alert_id is rejected.
- Duplicate payload hash (same content, no alert_id) is rejected.
- Crypto and options symbols are rejected.
- Invalid next_step values are rejected.
- No execution path exists — execute_paper.py is never imported or called.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

from trading_os.research.alert_intake import (
    ALLOWED_NEXT_STEPS,
    AlertIntakeError,
    process_alert,
    validate_alert_schema,
)

# ---------------------------------------------------------------------------
# Fixtures and helpers
# ---------------------------------------------------------------------------

VALID_PAYLOAD: dict = {
    "symbol": "AAPL",
    "next_step": "log_only",
    "source": "tradingview",
    "description": "Close crossed above 200-day SMA",
    "price": 185.50,
    "triggered_at": "2026-05-12T15:00:00Z",
}


def _process(tmp_path: Path, payload: dict) -> dict:
    alerts_dir = tmp_path / "alerts"
    log_path = tmp_path / "TRIGGER-LOG.md"
    return process_alert(payload, alerts_dir, log_path)


# ---------------------------------------------------------------------------
# validate_alert_schema
# ---------------------------------------------------------------------------

class TestValidateAlertSchema:
    def test_valid_passes(self) -> None:
        validate_alert_schema(VALID_PAYLOAD)

    def test_non_dict_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="JSON object"):
            validate_alert_schema("not a dict")

    def test_list_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="JSON object"):
            validate_alert_schema([VALID_PAYLOAD])

    def test_missing_symbol_rejected(self) -> None:
        d = {k: v for k, v in VALID_PAYLOAD.items() if k != "symbol"}
        with pytest.raises(AlertIntakeError, match="symbol"):
            validate_alert_schema(d)

    def test_empty_symbol_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="symbol"):
            validate_alert_schema({**VALID_PAYLOAD, "symbol": ""})

    def test_whitespace_symbol_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="symbol"):
            validate_alert_schema({**VALID_PAYLOAD, "symbol": "   "})

    def test_numeric_symbol_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="symbol"):
            validate_alert_schema({**VALID_PAYLOAD, "symbol": 123})

    def test_missing_next_step_rejected(self) -> None:
        d = {k: v for k, v in VALID_PAYLOAD.items() if k != "next_step"}
        with pytest.raises(AlertIntakeError, match="next_step"):
            validate_alert_schema(d)

    def test_invalid_next_step_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="not in the allowed set"):
            validate_alert_schema({**VALID_PAYLOAD, "next_step": "place_order"})

    def test_execute_next_step_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="not in the allowed set"):
            validate_alert_schema({**VALID_PAYLOAD, "next_step": "execute_now"})

    def test_all_allowed_next_steps_pass(self) -> None:
        for ns in ALLOWED_NEXT_STEPS:
            validate_alert_schema({**VALID_PAYLOAD, "next_step": ns})

    def test_crypto_asset_class_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="prohibited"):
            validate_alert_schema({**VALID_PAYLOAD, "asset_class": "crypto"})

    def test_options_asset_class_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="prohibited"):
            validate_alert_schema({**VALID_PAYLOAD, "asset_class": "options"})

    def test_futures_asset_class_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="prohibited"):
            validate_alert_schema({**VALID_PAYLOAD, "asset_class": "futures"})

    def test_forex_asset_class_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="prohibited"):
            validate_alert_schema({**VALID_PAYLOAD, "asset_class": "forex"})

    def test_us_equity_asset_class_passes(self) -> None:
        validate_alert_schema({**VALID_PAYLOAD, "asset_class": "us_equity"})

    def test_crypto_symbol_btc_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="crypto"):
            validate_alert_schema({**VALID_PAYLOAD, "symbol": "BTC"})

    def test_crypto_symbol_eth_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="crypto"):
            validate_alert_schema({**VALID_PAYLOAD, "symbol": "ETH"})

    def test_crypto_pair_with_separator_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="crypto"):
            validate_alert_schema({**VALID_PAYLOAD, "symbol": "BTC-USD"})

    def test_crypto_slash_pair_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="crypto"):
            validate_alert_schema({**VALID_PAYLOAD, "symbol": "ETH/USD"})

    def test_options_occ_symbol_rejected(self) -> None:
        # OCC format: AAPL230120C00150000
        with pytest.raises(AlertIntakeError, match="options"):
            validate_alert_schema({**VALID_PAYLOAD, "symbol": "AAPL230120C00150000"})

    def test_options_put_symbol_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="options"):
            validate_alert_schema({**VALID_PAYLOAD, "symbol": "MSFT240119P00250000"})

    def test_numeric_asset_class_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="asset_class"):
            validate_alert_schema({**VALID_PAYLOAD, "asset_class": 42})

    def test_empty_alert_id_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="alert_id"):
            validate_alert_schema({**VALID_PAYLOAD, "alert_id": ""})

    def test_numeric_alert_id_rejected(self) -> None:
        with pytest.raises(AlertIntakeError, match="alert_id"):
            validate_alert_schema({**VALID_PAYLOAD, "alert_id": 12345})

    def test_string_alert_id_passes(self) -> None:
        validate_alert_schema({**VALID_PAYLOAD, "alert_id": "tv-abc-123"})


# ---------------------------------------------------------------------------
# process_alert — safety invariants
# ---------------------------------------------------------------------------

class TestProcessAlertSafetyInvariants:
    def test_trade_execution_allowed_always_false(self, tmp_path: Path) -> None:
        """Caller passes true — must be forced to false."""
        payload = {**VALID_PAYLOAD, "trade_execution_allowed": True}
        record = _process(tmp_path, payload)
        assert record["trade_execution_allowed"] is False

    def test_blocked_by_default_always_true(self, tmp_path: Path) -> None:
        """Caller passes false — must be forced to true."""
        payload = {**VALID_PAYLOAD, "blocked_by_default": False}
        record = _process(tmp_path, payload)
        assert record["blocked_by_default"] is True

    def test_both_flags_forced_simultaneously(self, tmp_path: Path) -> None:
        payload = {
            **VALID_PAYLOAD,
            "trade_execution_allowed": True,
            "blocked_by_default": False,
        }
        record = _process(tmp_path, payload)
        assert record["trade_execution_allowed"] is False
        assert record["blocked_by_default"] is True

    def test_flags_absent_in_input_still_forced(self, tmp_path: Path) -> None:
        """Even if caller omits the flags, they must be present and forced in output."""
        payload = {k: v for k, v in VALID_PAYLOAD.items()
                   if k not in ("trade_execution_allowed", "blocked_by_default")}
        record = _process(tmp_path, payload)
        assert record["trade_execution_allowed"] is False
        assert record["blocked_by_default"] is True

    def test_no_execute_paper_import(self) -> None:
        """execute_paper must never be imported by the alert intake module."""
        import re
        import trading_os.research.alert_intake as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        # Comments and docstrings may mention execute_paper.py; actual imports must not.
        assert not re.search(r"^\s*(import|from)\s+.*execute_paper", src, re.MULTILINE)

    def test_no_build_trade_plan_call(self) -> None:
        """alert_intake must never import or call build_trade_plan."""
        import re
        import trading_os.research.alert_intake as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        assert not re.search(r"^\s*(import|from)\s+.*build_trade_plan", src, re.MULTILINE)
        assert not re.search(r"\bbuild_trade_plan\s*\(", src)

    def test_no_approved_for_execution(self) -> None:
        """alert_intake must never set approved_for_execution=True."""
        import trading_os.research.alert_intake as mod
        src = Path(mod.__file__).read_text(encoding="utf-8")
        assert "approved_for_execution" not in src


# ---------------------------------------------------------------------------
# process_alert — valid flow
# ---------------------------------------------------------------------------

class TestProcessAlertValidFlow:
    def test_valid_alert_accepted(self, tmp_path: Path) -> None:
        record = _process(tmp_path, VALID_PAYLOAD)
        assert record["symbol"] == "AAPL"
        assert record["next_step"] == "log_only"

    def test_alert_file_written(self, tmp_path: Path) -> None:
        record = _process(tmp_path, VALID_PAYLOAD)
        alerts_dir = tmp_path / "alerts"
        alert_id = record["alert_id"]
        assert (alerts_dir / f"alert-{alert_id}.json").exists()

    def test_written_file_is_valid_json(self, tmp_path: Path) -> None:
        record = _process(tmp_path, VALID_PAYLOAD)
        alerts_dir = tmp_path / "alerts"
        alert_id = record["alert_id"]
        path = alerts_dir / f"alert-{alert_id}.json"
        parsed = json.loads(path.read_text(encoding="utf-8"))
        assert parsed["symbol"] == "AAPL"

    def test_written_file_has_forced_flags(self, tmp_path: Path) -> None:
        payload = {**VALID_PAYLOAD, "trade_execution_allowed": True, "blocked_by_default": False}
        record = _process(tmp_path, payload)
        alerts_dir = tmp_path / "alerts"
        path = alerts_dir / f"alert-{record['alert_id']}.json"
        parsed = json.loads(path.read_text(encoding="utf-8"))
        assert parsed["trade_execution_allowed"] is False
        assert parsed["blocked_by_default"] is True

    def test_raw_payload_hash_present(self, tmp_path: Path) -> None:
        record = _process(tmp_path, VALID_PAYLOAD)
        assert isinstance(record["raw_payload_hash"], str)
        assert len(record["raw_payload_hash"]) == 64  # sha256 hex

    def test_ingested_at_present(self, tmp_path: Path) -> None:
        record = _process(tmp_path, VALID_PAYLOAD)
        assert isinstance(record["ingested_at"], str)
        assert "T" in record["ingested_at"]

    def test_explicit_alert_id_preserved(self, tmp_path: Path) -> None:
        payload = {**VALID_PAYLOAD, "alert_id": "tv-test-001"}
        record = _process(tmp_path, payload)
        assert record["alert_id"] == "tv-test-001"

    def test_alert_id_generated_when_absent(self, tmp_path: Path) -> None:
        payload = {k: v for k, v in VALID_PAYLOAD.items() if k != "alert_id"}
        record = _process(tmp_path, payload)
        assert isinstance(record["alert_id"], str)
        assert len(record["alert_id"]) > 0

    def test_trigger_log_appended(self, tmp_path: Path) -> None:
        log_path = tmp_path / "TRIGGER-LOG.md"
        process_alert(VALID_PAYLOAD, tmp_path / "alerts", log_path)
        content = log_path.read_text(encoding="utf-8")
        assert "External alert ingested" in content
        assert "AAPL" in content

    def test_trigger_log_contains_forced_flags(self, tmp_path: Path) -> None:
        log_path = tmp_path / "TRIGGER-LOG.md"
        payload = {**VALID_PAYLOAD, "trade_execution_allowed": True}
        process_alert(payload, tmp_path / "alerts", log_path)
        content = log_path.read_text(encoding="utf-8")
        assert "false" in content.lower()

    def test_trigger_log_appends_multiple(self, tmp_path: Path) -> None:
        log_path = tmp_path / "TRIGGER-LOG.md"
        alerts_dir = tmp_path / "alerts"
        process_alert({**VALID_PAYLOAD, "alert_id": "a1"}, alerts_dir, log_path)
        process_alert(
            {"symbol": "MSFT", "next_step": "request_alert_review", "alert_id": "a2"},
            alerts_dir,
            log_path,
        )
        content = log_path.read_text(encoding="utf-8")
        assert content.count("External alert ingested") == 2

    def test_all_allowed_next_steps_accepted(self, tmp_path: Path) -> None:
        for i, ns in enumerate(sorted(ALLOWED_NEXT_STEPS)):
            payload = {**VALID_PAYLOAD, "alert_id": f"test-ns-{i}", "next_step": ns}
            record = _process(tmp_path, payload)
            assert record["next_step"] == ns


# ---------------------------------------------------------------------------
# process_alert — deduplication
# ---------------------------------------------------------------------------

class TestProcessAlertDeduplication:
    def test_duplicate_alert_id_rejected(self, tmp_path: Path) -> None:
        payload = {**VALID_PAYLOAD, "alert_id": "dup-001"}
        _process(tmp_path, payload)
        with pytest.raises(AlertIntakeError, match="duplicate"):
            _process(tmp_path, {**payload, "description": "second attempt"})

    def test_duplicate_payload_hash_rejected(self, tmp_path: Path) -> None:
        payload = {k: v for k, v in VALID_PAYLOAD.items() if k != "alert_id"}
        _process(tmp_path, payload)
        with pytest.raises(AlertIntakeError, match="duplicate"):
            _process(tmp_path, payload)

    def test_different_payloads_both_accepted(self, tmp_path: Path) -> None:
        p1 = {**VALID_PAYLOAD, "alert_id": "uniq-001"}
        p2 = {**VALID_PAYLOAD, "alert_id": "uniq-002", "symbol": "MSFT"}
        r1 = _process(tmp_path, p1)
        r2 = _process(tmp_path, p2)
        assert r1["alert_id"] != r2["alert_id"]


# ---------------------------------------------------------------------------
# process_alert — rejected inputs
# ---------------------------------------------------------------------------

class TestProcessAlertRejectedInputs:
    def test_non_dict_rejected(self, tmp_path: Path) -> None:
        with pytest.raises(AlertIntakeError):
            _process(tmp_path, "not a dict")

    def test_missing_symbol_rejected(self, tmp_path: Path) -> None:
        d = {k: v for k, v in VALID_PAYLOAD.items() if k != "symbol"}
        with pytest.raises(AlertIntakeError, match="symbol"):
            _process(tmp_path, d)

    def test_invalid_next_step_rejected(self, tmp_path: Path) -> None:
        with pytest.raises(AlertIntakeError, match="not in the allowed set"):
            _process(tmp_path, {**VALID_PAYLOAD, "next_step": "buy_now"})

    def test_crypto_symbol_rejected(self, tmp_path: Path) -> None:
        with pytest.raises(AlertIntakeError, match="crypto"):
            _process(tmp_path, {**VALID_PAYLOAD, "symbol": "BTC"})

    def test_crypto_pair_rejected(self, tmp_path: Path) -> None:
        with pytest.raises(AlertIntakeError, match="crypto"):
            _process(tmp_path, {**VALID_PAYLOAD, "symbol": "ETH-USD"})

    def test_options_symbol_rejected(self, tmp_path: Path) -> None:
        with pytest.raises(AlertIntakeError, match="options"):
            _process(tmp_path, {**VALID_PAYLOAD, "symbol": "AAPL230120C00150000"})

    def test_crypto_asset_class_rejected(self, tmp_path: Path) -> None:
        with pytest.raises(AlertIntakeError, match="prohibited"):
            _process(tmp_path, {**VALID_PAYLOAD, "asset_class": "crypto"})

    def test_options_asset_class_rejected(self, tmp_path: Path) -> None:
        with pytest.raises(AlertIntakeError, match="prohibited"):
            _process(tmp_path, {**VALID_PAYLOAD, "asset_class": "options"})

    def test_no_alert_file_written_on_rejection(self, tmp_path: Path) -> None:
        alerts_dir = tmp_path / "alerts"
        try:
            _process(tmp_path, {**VALID_PAYLOAD, "symbol": "BTC"})
        except AlertIntakeError:
            pass
        # No file should have been written
        if alerts_dir.exists():
            assert list(alerts_dir.glob("*.json")) == []

    def test_no_log_written_on_rejection(self, tmp_path: Path) -> None:
        log_path = tmp_path / "TRIGGER-LOG.md"
        try:
            process_alert(
                {**VALID_PAYLOAD, "symbol": "ETH"},
                tmp_path / "alerts",
                log_path,
            )
        except AlertIntakeError:
            pass
        assert not log_path.exists()
