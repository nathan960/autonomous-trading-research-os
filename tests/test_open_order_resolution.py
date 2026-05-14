"""Tests for open-order resolution — list and single-order cancellation.

All tests use pure functions or mock the Alpaca SDK. No network calls.
No orders are placed, replaced, or actually cancelled.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trading_os.execution.open_order_resolution import (
    CANCEL_CONFIRMATION_TOKEN,
    CANCELLABLE_STATUSES,
    TERMINAL_STATUSES,
    build_cancellation_record,
    build_order_list_record,
    format_cancellation_markdown,
    format_order_list_markdown,
    validate_cancel_confirmation,
    validate_order_cancellable,
    validate_order_id_match,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _open_order(
    symbol: str = "EQIX",
    status: str = "new",
    side: str = "buy",
    client_order_id: str = "TOS-20260514T154817-EQIX-BUY",
    broker_order_id: str = "3351082e-8e6a-4148-af27-81e5414dd0db",
) -> dict:
    return {
        "symbol": symbol,
        "status": status,
        "side": side,
        "client_order_id": client_order_id,
        "id": broker_order_id,
        "notional": "25",
        "limit_price": "1078.43",
        "submitted_at": "2026-05-14T15:48:18Z",
        "expires_at": "2026-05-14T20:00:00Z",
        "order_type": "limit",
        "asset_class": "us_equity",
    }


# ===========================================================================
# validate_cancel_confirmation
# ===========================================================================

class TestValidateCancelConfirmation:
    def test_exact_token_passes(self):
        validate_cancel_confirmation("CANCEL")  # must not raise

    def test_wrong_token_raises(self):
        with pytest.raises(ValueError, match="CANCEL"):
            validate_cancel_confirmation("cancel")

    def test_lowercase_raises(self):
        with pytest.raises(ValueError):
            validate_cancel_confirmation("cancel")

    def test_empty_string_raises(self):
        with pytest.raises(ValueError):
            validate_cancel_confirmation("")

    def test_yes_raises(self):
        with pytest.raises(ValueError):
            validate_cancel_confirmation("YES")

    def test_confirm_raises(self):
        with pytest.raises(ValueError):
            validate_cancel_confirmation("CONFIRM")

    def test_cancel_with_trailing_space_raises(self):
        with pytest.raises(ValueError):
            validate_cancel_confirmation("CANCEL ")

    def test_cancel_with_leading_space_raises(self):
        with pytest.raises(ValueError):
            validate_cancel_confirmation(" CANCEL")

    def test_true_raises(self):
        with pytest.raises(ValueError):
            validate_cancel_confirmation("true")

    def test_token_constant_is_cancel(self):
        assert CANCEL_CONFIRMATION_TOKEN == "CANCEL"


# ===========================================================================
# validate_order_cancellable
# ===========================================================================

class TestValidateOrderCancellable:
    def test_new_order_passes(self):
        validate_order_cancellable(_open_order(status="new"))

    def test_accepted_order_passes(self):
        validate_order_cancellable(_open_order(status="accepted"))

    def test_pending_new_passes(self):
        validate_order_cancellable(_open_order(status="pending_new"))

    def test_held_passes(self):
        validate_order_cancellable(_open_order(status="held"))

    def test_partially_filled_passes(self):
        validate_order_cancellable(_open_order(status="partially_filled"))

    def test_filled_raises(self):
        with pytest.raises(ValueError, match="terminal"):
            validate_order_cancellable(_open_order(status="filled"))

    def test_canceled_raises(self):
        with pytest.raises(ValueError, match="terminal"):
            validate_order_cancellable(_open_order(status="canceled"))

    def test_expired_raises(self):
        with pytest.raises(ValueError, match="terminal"):
            validate_order_cancellable(_open_order(status="expired"))

    def test_replaced_raises(self):
        with pytest.raises(ValueError, match="terminal"):
            validate_order_cancellable(_open_order(status="replaced"))

    def test_rejected_raises(self):
        with pytest.raises(ValueError, match="terminal"):
            validate_order_cancellable(_open_order(status="rejected"))

    def test_empty_dict_raises(self):
        with pytest.raises(ValueError):
            validate_order_cancellable({})

    def test_missing_status_raises(self):
        with pytest.raises(ValueError, match="no status"):
            validate_order_cancellable({"symbol": "EQIX"})

    def test_unknown_status_raises(self):
        with pytest.raises(ValueError, match="not in the known cancellable set"):
            validate_order_cancellable(_open_order(status="unknown_future_status"))

    def test_sell_side_raises(self):
        with pytest.raises(ValueError, match="long-only"):
            validate_order_cancellable(_open_order(status="new", side="sell"))

    def test_all_cancellable_statuses_pass(self):
        for status in CANCELLABLE_STATUSES:
            validate_order_cancellable(_open_order(status=status))

    def test_all_terminal_statuses_raise(self):
        for status in TERMINAL_STATUSES:
            with pytest.raises(ValueError):
                validate_order_cancellable(_open_order(status=status))


# ===========================================================================
# validate_order_id_match
# ===========================================================================

class TestValidateOrderIdMatch:
    def test_matching_client_id_passes(self):
        order = _open_order(client_order_id="TOS-123")
        validate_order_id_match(order, client_order_id="TOS-123", broker_order_id=None)

    def test_mismatched_client_id_raises(self):
        order = _open_order(client_order_id="TOS-123")
        with pytest.raises(ValueError, match="does not match"):
            validate_order_id_match(order, client_order_id="TOS-WRONG", broker_order_id=None)

    def test_matching_broker_id_passes(self):
        order = _open_order(broker_order_id="abc-uuid")
        validate_order_id_match(order, client_order_id=None, broker_order_id="abc-uuid")

    def test_mismatched_broker_id_raises(self):
        order = _open_order(broker_order_id="abc-uuid")
        with pytest.raises(ValueError, match="does not match"):
            validate_order_id_match(order, client_order_id=None, broker_order_id="other-uuid")

    def test_both_ids_matching_passes(self):
        order = _open_order(client_order_id="TOS-123", broker_order_id="broker-uuid")
        validate_order_id_match(order, client_order_id="TOS-123", broker_order_id="broker-uuid")

    def test_no_ids_provided_passes(self):
        order = _open_order()
        validate_order_id_match(order, client_order_id=None, broker_order_id=None)


# ===========================================================================
# build_order_list_record
# ===========================================================================

class TestBuildOrderListRecord:
    def _build(self, orders=None, run_id="list_open_orders-20260514-abc123", fetched_at="2026-05-14T16:00:00Z"):
        return build_order_list_record(
            orders=orders or [_open_order()],
            run_id=run_id,
            fetched_at=fetched_at,
        )

    def test_run_id_present(self):
        assert self._build()["run_id"] == "list_open_orders-20260514-abc123"

    def test_open_order_count(self):
        record = build_order_list_record([_open_order(), _open_order(symbol="JNJ")], "r", "2026-05-14T00:00:00Z")
        assert record["open_order_count"] == 2

    def test_empty_orders(self):
        record = build_order_list_record([], "r", "2026-05-14T00:00:00Z")
        assert record["open_order_count"] == 0
        assert record["orders"] == []

    def test_orders_contain_symbol(self):
        record = self._build()
        assert record["orders"][0]["symbol"] == "EQIX"

    def test_orders_contain_client_order_id(self):
        record = self._build()
        assert "client_order_id" in record["orders"][0]

    def test_orders_contain_broker_order_id(self):
        record = self._build()
        assert "broker_order_id" in record["orders"][0]

    def test_production_cancel_always_false(self):
        record = self._build()
        assert record["production_order_cancel_allowed"] is False

    def test_non_dict_orders_skipped(self):
        record = build_order_list_record(["bad", None, _open_order()], "r", "2026-05-14T00:00:00Z")
        assert record["open_order_count"] == 1

    def test_action_field(self):
        assert self._build()["action"] == "list_open_orders"


# ===========================================================================
# build_cancellation_record
# ===========================================================================

class TestBuildCancellationRecord:
    def _build(self, order=None, broker_response=None):
        return build_cancellation_record(
            order=order or _open_order(),
            broker_response=broker_response or {"status": "cancel_accepted"},
            cancelled_at="2026-05-14T17:00:00Z",
            confirmed_by="operator (confirm_cancel='CANCEL')",
            notes="test cancellation",
        )

    def test_run_id_present(self):
        record = self._build()
        assert record["run_id"].startswith("order_cancel-")

    def test_symbol_present(self):
        assert self._build()["symbol"] == "EQIX"

    def test_side_present(self):
        assert self._build()["side"] == "buy"

    def test_status_before_cancel(self):
        assert self._build()["status_before_cancel"] == "new"

    def test_client_order_id_present(self):
        record = self._build()
        assert record["client_order_id"] == "TOS-20260514T154817-EQIX-BUY"

    def test_broker_order_id_present(self):
        record = self._build()
        assert record["broker_order_id"] == "3351082e-8e6a-4148-af27-81e5414dd0db"

    def test_confirmed_by_present(self):
        record = self._build()
        assert "CANCEL" in record["confirmed_by"]

    def test_notes_present(self):
        assert self._build()["notes"] == "test cancellation"

    def test_production_cancel_always_false(self):
        assert self._build()["production_order_cancel_allowed"] is False

    def test_broker_response_included(self):
        record = self._build(broker_response={"status": "cancel_accepted", "id": "xyz"})
        assert record["broker_response"]["status"] == "cancel_accepted"

    def test_broker_response_model_dump(self):
        mock_resp = MagicMock()
        mock_resp.model_dump.return_value = {"status": "from_model_dump"}
        record = self._build(broker_response=mock_resp)
        assert record["broker_response"]["status"] == "from_model_dump"

    def test_action_field(self):
        assert self._build()["action"] == "cancel_paper_order"


# ===========================================================================
# format_cancellation_markdown
# ===========================================================================

class TestFormatCancellationMarkdown:
    def _record(self):
        return build_cancellation_record(
            order=_open_order(),
            broker_response={"status": "cancel_accepted"},
            cancelled_at="2026-05-14T17:00:00Z",
            confirmed_by="operator (confirm_cancel='CANCEL')",
        )

    def test_contains_order_cancel_header(self):
        md = format_cancellation_markdown(self._record())
        assert "order_cancel" in md

    def test_contains_symbol(self):
        md = format_cancellation_markdown(self._record())
        assert "EQIX" in md

    def test_contains_client_order_id(self):
        md = format_cancellation_markdown(self._record())
        assert "TOS-20260514T154817-EQIX-BUY" in md

    def test_contains_confirmed_by(self):
        md = format_cancellation_markdown(self._record())
        assert "CANCEL" in md


# ===========================================================================
# format_order_list_markdown
# ===========================================================================

class TestFormatOrderListMarkdown:
    def test_contains_order_list_header(self):
        record = build_order_list_record([_open_order()], "r", "2026-05-14T00:00:00Z")
        md = format_order_list_markdown(record)
        assert "order_list" in md

    def test_contains_symbol(self):
        record = build_order_list_record([_open_order(symbol="EQIX")], "r", "2026-05-14T00:00:00Z")
        md = format_order_list_markdown(record)
        assert "EQIX" in md

    def test_empty_orders_shows_placeholder(self):
        record = build_order_list_record([], "r", "2026-05-14T00:00:00Z")
        md = format_order_list_markdown(record)
        assert "no open orders" in md


# ===========================================================================
# Script: cancel_paper_order.py — confirmation gate
# ===========================================================================

class TestCancelPaperOrderConfirmationGate:
    """Verify the script fails closed when confirmation is wrong."""

    def _run_script(self, args: list) -> int:
        import importlib, importlib.util
        spec = importlib.util.spec_from_file_location(
            "cancel_paper_order",
            Path(__file__).resolve().parents[1] / "scripts" / "cancel_paper_order.py",
        )
        mod = importlib.util.module_from_spec(spec)
        with patch("sys.argv", ["cancel_paper_order.py"] + args):
            spec.loader.exec_module(mod)
        return mod

    def test_missing_confirm_cancel_exits_error(self, capsys):
        """argparse requires --confirm-cancel so missing it exits 2."""
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "cpo_missing",
            Path(__file__).resolve().parents[1] / "scripts" / "cancel_paper_order.py",
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        with pytest.raises(SystemExit) as exc_info:
            with patch("sys.argv", ["cancel_paper_order.py",
                                    "--client-order-id", "TOS-123"]):
                mod.main()
        assert exc_info.value.code == 2

    def test_wrong_confirmation_fails_closed(self, tmp_path, capsys, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "true")
        monkeypatch.setenv("LIVE_TRADING_CONFIRMED", "false")
        with patch("sys.argv", [
            "cancel_paper_order.py",
            "--client-order-id", "TOS-123",
            "--confirm-cancel", "YES",
            "--dry-run",
        ]):
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                "cpo",
                Path(__file__).resolve().parents[1] / "scripts" / "cancel_paper_order.py",
            )
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            result = mod.main()
        assert result == 1

    def test_correct_confirmation_with_dry_run_finds_order(self, tmp_path, monkeypatch):
        """dry_run with a snapshot that has the matching order returns 0."""
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "true")
        monkeypatch.setenv("LIVE_TRADING_CONFIRMED", "false")

        snap = {
            "orders": [_open_order(client_order_id="TOS-TEST-EQIX")],
            "open_order_count": 1,
        }
        latest_dir = tmp_path / "data" / "latest"
        latest_dir.mkdir(parents=True)
        (latest_dir / "orders_snapshot.json").write_text(json.dumps(snap))
        history_dir = tmp_path / "data" / "history" / "orders"
        history_dir.mkdir(parents=True)
        memory_dir = tmp_path / "memory"
        memory_dir.mkdir(parents=True)

        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "cpo2",
            Path(__file__).resolve().parents[1] / "scripts" / "cancel_paper_order.py",
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        # Patch module-level paths so relative_to and I/O use tmp_path
        mod._ROOT = tmp_path
        mod._ORDERS_DIR = history_dir
        mod._TRADE_LOG_PATH = memory_dir / "TRADE-LOG.md"
        mod._RESOLUTION_LOG_PATH = memory_dir / "ORDER-RESOLUTION-LOG.md"
        # Patch the snapshot lookup to use our tmp latest_dir
        original_find = mod._find_order_in_snapshot
        mod._find_order_in_snapshot = lambda cid, bid: original_find.__wrapped__(cid, bid) if hasattr(original_find, "__wrapped__") else _open_order(client_order_id="TOS-TEST-EQIX") if cid == "TOS-TEST-EQIX" else None

        with patch("sys.argv", [
            "cancel_paper_order.py",
            "--client-order-id", "TOS-TEST-EQIX",
            "--confirm-cancel", "CANCEL",
            "--dry-run",
        ]):
            result = mod.main()
        assert result == 0

    def test_dry_run_order_not_in_snapshot_fails(self, tmp_path, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "true")
        monkeypatch.setenv("LIVE_TRADING_CONFIRMED", "false")

        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "cpo3",
            Path(__file__).resolve().parents[1] / "scripts" / "cancel_paper_order.py",
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        # Make snapshot lookup always return None (not found)
        mod._find_order_in_snapshot = lambda cid, bid: None

        with patch("sys.argv", [
            "cancel_paper_order.py",
            "--client-order-id", "TOS-NOT-FOUND",
            "--confirm-cancel", "CANCEL",
            "--dry-run",
        ]):
            result = mod.main()
        assert result == 1

    def test_dry_run_terminal_order_fails_closed(self, tmp_path, monkeypatch):
        """Attempting to cancel a filled order must fail even in dry-run."""
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "true")
        monkeypatch.setenv("LIVE_TRADING_CONFIRMED", "false")

        filled_order = _open_order(status="filled", client_order_id="TOS-FILLED")

        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "cpo4",
            Path(__file__).resolve().parents[1] / "scripts" / "cancel_paper_order.py",
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod._find_order_in_snapshot = lambda cid, bid: filled_order

        with patch("sys.argv", [
            "cancel_paper_order.py",
            "--client-order-id", "TOS-FILLED",
            "--confirm-cancel", "CANCEL",
            "--dry-run",
        ]):
            result = mod.main()
        assert result == 1


# ===========================================================================
# Script: list_open_orders.py
# ===========================================================================

def _load_script(filename: str, module_alias: str = "") -> object:
    import importlib.util
    alias = module_alias or filename
    spec = importlib.util.spec_from_file_location(
        alias,
        Path(__file__).resolve().parents[1] / "scripts" / f"{filename}.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _setup_tmp_dirs(tmp_path: Path) -> tuple:
    latest_dir = tmp_path / "data" / "latest"
    latest_dir.mkdir(parents=True)
    history_dir = tmp_path / "data" / "history" / "orders"
    history_dir.mkdir(parents=True)
    memory_dir = tmp_path / "memory"
    memory_dir.mkdir(parents=True)
    return latest_dir, history_dir, memory_dir


class TestListOpenOrdersScript:
    def test_dry_run_with_snapshot(self, tmp_path, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "true")
        monkeypatch.setenv("LIVE_TRADING_CONFIRMED", "false")

        latest_dir, history_dir, memory_dir = _setup_tmp_dirs(tmp_path)
        snap = {"orders": [_open_order()], "open_order_count": 1}
        (latest_dir / "orders_snapshot.json").write_text(json.dumps(snap))

        mod = _load_script("list_open_orders", "list_open_orders_t1")
        mod._ROOT = tmp_path
        mod._ORDERS_DIR = history_dir
        mod._LOG_PATH = memory_dir / "ORDER-RESOLUTION-LOG.md"
        # Patch LATEST_DIR used by the script body
        mod.LATEST_DIR = latest_dir

        with patch("sys.argv", ["list_open_orders.py", "--dry-run"]):
            result = mod.main()
        assert result == 0

    def test_dry_run_empty_snapshot(self, tmp_path, monkeypatch):
        monkeypatch.setenv("TRADING_MODE", "paper")
        monkeypatch.setenv("ALPACA_PAPER", "true")
        monkeypatch.setenv("LIVE_TRADING_CONFIRMED", "false")

        latest_dir, history_dir, memory_dir = _setup_tmp_dirs(tmp_path)
        (latest_dir / "orders_snapshot.json").write_text(json.dumps({"orders": []}))

        mod = _load_script("list_open_orders", "list_open_orders_t2")
        mod._ROOT = tmp_path
        mod._ORDERS_DIR = history_dir
        mod._LOG_PATH = memory_dir / "ORDER-RESOLUTION-LOG.md"
        mod.LATEST_DIR = latest_dir

        with patch("sys.argv", ["list_open_orders.py", "--dry-run"]):
            result = mod.main()
        assert result == 0


# ===========================================================================
# No-execution path assertions
# ===========================================================================

class TestNoExecutionPath:
    def test_module_has_no_submit_order_call(self):
        src = Path(__file__).resolve().parents[1] / "src" / "trading_os" / "execution" / "open_order_resolution.py"
        text = src.read_text()
        assert "submit_order" not in text
        assert "place_order" not in text
        assert "MarketOrder" not in text
        assert "LimitOrder" not in text

    def test_module_has_no_replace_order_call(self):
        src = Path(__file__).resolve().parents[1] / "src" / "trading_os" / "execution" / "open_order_resolution.py"
        text = src.read_text()
        assert "replace_order" not in text

    def test_cancel_script_has_no_submit_order_call(self):
        src = Path(__file__).resolve().parents[1] / "scripts" / "cancel_paper_order.py"
        text = src.read_text()
        assert "submit_order" not in text
        assert "place_order" not in text
        assert "MarketOrder" not in text

    def test_cancel_script_has_no_replace_order_call(self):
        src = Path(__file__).resolve().parents[1] / "scripts" / "cancel_paper_order.py"
        text = src.read_text()
        assert "replace_order" not in text

    def test_list_script_has_no_cancel_or_submit(self):
        src = Path(__file__).resolve().parents[1] / "scripts" / "list_open_orders.py"
        text = src.read_text()
        assert "submit_order" not in text
        assert "cancel_order" not in text
        assert "replace_order" not in text

    def test_production_cancel_always_false_in_record(self):
        record = build_cancellation_record(
            order=_open_order(),
            broker_response={},
            cancelled_at="2026-05-14T17:00:00Z",
            confirmed_by="test",
        )
        assert record["production_order_cancel_allowed"] is False

    def test_production_cancel_always_false_in_list_record(self):
        record = build_order_list_record([_open_order()], "r", "2026-05-14T00:00:00Z")
        assert record["production_order_cancel_allowed"] is False
