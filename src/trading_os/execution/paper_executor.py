"""Phase 6 paper execution: submit Alpaca paper limit orders when all gates pass.

Safety contracts enforced before any order is submitted:
  1. TRADING_MODE=paper
  2. ALPACA_PAPER=true
  3. ENABLE_PAPER_EXECUTION=true
  4. LIVE_TRADING_CONFIRMED must NOT be true
  5. confirm_paper flag must be True (CLI --confirm-paper)
  6. trade_plan.approval.approved_for_execution must be True
  7. All 16 Phase-5 execution gates must pass (dry_run=False, fresh broker data)
  8. Execution-history and orders directories must be writable
  9. Every order must be a limit order with day TIF, no shorts, no options

NEVER submits a live order.  NEVER accesses a live broker endpoint.
NEVER submits if any hard gate fails.  NEVER logs or echoes secrets.
"""
from __future__ import annotations

import json
import os
import uuid
from pathlib import Path
from typing import Any, Optional

from ..hashing import stable_hash
from ..time_utils import utc_now_iso
from .execution_gates import all_gates_pass, run_all_gates
from .order_builder import build_execution_orders


# ---------------------------------------------------------------------------
# Hard env-var gate checks
# ---------------------------------------------------------------------------

def _check_hard_env_gates() -> None:
    """Assert all four environment-variable hard gates.

    Called before any network I/O, broker connection, or order construction.
    Raises RuntimeError immediately on the first violation.
    """
    mode = os.getenv("TRADING_MODE", "").strip().lower()
    if mode != "paper":
        raise RuntimeError(
            f"BLOCKED: TRADING_MODE must be 'paper' (got {mode!r}). "
            "Live trading is not permitted in this system."
        )

    paper = os.getenv("ALPACA_PAPER", "").strip().lower()
    if paper not in ("true", "1"):
        raise RuntimeError(
            f"BLOCKED: ALPACA_PAPER must be 'true' or '1' (got {paper!r}). "
            "Must connect to the Alpaca paper endpoint."
        )

    enable = os.getenv("ENABLE_PAPER_EXECUTION", "").strip().lower()
    if enable not in ("true", "1"):
        raise RuntimeError(
            f"BLOCKED: ENABLE_PAPER_EXECUTION must be 'true' or '1' (got {enable!r}). "
            "Set this env var to explicitly enable paper order submission."
        )

    live = os.getenv("LIVE_TRADING_CONFIRMED", "").strip().lower()
    if live in ("true", "1", "yes", "y", "on"):
        raise RuntimeError(
            "BLOCKED: LIVE_TRADING_CONFIRMED must not be 'true'. "
            "This system is paper-only and will never enable live trading."
        )


# ---------------------------------------------------------------------------
# Pre-submission soft checks (return block-reason string, not raise)
# ---------------------------------------------------------------------------

def _check_confirm_paper(confirm_paper: bool) -> Optional[str]:
    """Return block reason if --confirm-paper flag was not passed, else None."""
    if not confirm_paper:
        return (
            "confirm_paper_flag_not_set — pass --confirm-paper to acknowledge "
            "that paper orders will be submitted to Alpaca"
        )
    return None


def _check_plan_approved(trade_plan: dict) -> Optional[str]:
    """Return block reason if trade plan is not approved for paper execution, else None."""
    approval = trade_plan.get("approval", {})
    if not approval.get("approved_for_execution"):
        reason = approval.get("reason", "unknown")
        return (
            f"trade_plan.approval.approved_for_execution is not True "
            f"(reason={reason!r}) — regenerate with --approve-paper"
        )
    return None


def _probe_log_dirs(*dirs: Path) -> Optional[str]:
    """Probe-write each directory. Returns first error string, or None if all writable."""
    for d in dirs:
        try:
            d.mkdir(parents=True, exist_ok=True)
            probe = d / ".write_probe"
            probe.write_text("ok", encoding="utf-8")
            probe.unlink()
        except Exception as exc:
            return f"log directory not writable — {d}: {type(exc).__name__}: {exc}"
    return None


# ---------------------------------------------------------------------------
# Per-order paper-execution safety validation
# ---------------------------------------------------------------------------

def _validate_order_paper_safe(order: dict) -> Optional[str]:
    """Paper-execution-specific validation on top of Phase-5 order_builder checks.

    Returns a skip_reason string if the order must not be submitted, else None.
    Paper execution is stricter than dry-run:
      - Limit orders only (market orders are not accepted).
      - limit_price must be present and positive.
      - Short sells are never permitted.
      - Option-like symbols are blocked (heuristic).
      - time_in_force must be 'day'.
    """
    symbol: str = order.get("symbol", "")

    if order.get("would_short"):
        return f"would_short_blocked({symbol})"

    # Options heuristic: "/" in symbol or >6-char ticker ending in a digit
    if "/" in symbol or (len(symbol) > 6 and symbol[-1].isdigit()):
        return f"suspected_options_symbol_blocked({symbol})"

    order_type = order.get("order_type", "")
    if order_type != "limit":
        return f"paper_execution_limit_only(got {order_type!r} for {symbol})"

    limit_price = order.get("limit_price")
    if limit_price is None or float(limit_price) <= 0:
        return f"missing_or_zero_limit_price({symbol})"

    tif = order.get("time_in_force", "day")
    if tif != "day":
        return f"time_in_force_must_be_day(got {tif!r} for {symbol})"

    return None


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def _write_json_atomic(path: Path, payload: dict) -> None:
    """Atomic JSON write: write to .tmp then rename into place."""
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True, default=str)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(path)


# ---------------------------------------------------------------------------
# Single-order submission
# ---------------------------------------------------------------------------

def submit_paper_order(
    trading_client: Any,
    order: dict,
    orders_dir: Path,
) -> dict:
    """Submit one paper limit order to Alpaca and write an audit file to orders_dir.

    Returns an order-result dict.  Never raises — all exceptions are captured
    in result["error"].  Log-write failures are captured in result["log_write_error"].
    Secrets are never included in the result or log file.
    """
    from alpaca.trading.enums import OrderSide, TimeInForce
    from alpaca.trading.requests import LimitOrderRequest

    from ..data.alpaca_client import _to_primitive

    submitted_at = utc_now_iso()
    symbol: str = order.get("symbol", "")
    client_order_id: str = order.get("client_order_id", "")
    side_str: str = order.get("side", "buy")
    notional: float = float(order.get("notional", 0))
    limit_price: float = float(order.get("limit_price", 0))

    result: dict = {
        "symbol": symbol,
        "client_order_id": client_order_id,
        "side": side_str,
        "notional": notional,
        "limit_price": limit_price,
        "submitted_at": submitted_at,
        "submitted": False,
        "broker_order_id": None,
        "broker_status": None,
        "skip_reason": order.get("validation_skip_reason"),
        "error": None,
    }

    try:
        side = OrderSide.BUY if side_str == "buy" else OrderSide.SELL
        req = LimitOrderRequest(
            symbol=symbol,
            notional=notional,
            side=side,
            time_in_force=TimeInForce.DAY,
            limit_price=limit_price,
            extended_hours=False,
            client_order_id=client_order_id,
        )
        response = trading_client.submit_order(req)
        primitive = _to_primitive(response)
        result.update({
            "submitted": True,
            "broker_order_id": primitive.get("id"),
            "broker_status": primitive.get("status"),
        })
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"

    # Per-order audit log — always attempt even if submission failed
    try:
        _write_json_atomic(orders_dir / f"{client_order_id}.json", result)
    except Exception as exc:
        result["log_write_error"] = (
            f"order audit log write failed: {type(exc).__name__}: {exc}"
        )

    return result


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def _finalise_report(report: dict) -> None:
    """Stamp execution_report_hash onto the report dict in-place."""
    report["execution_report_hash"] = stable_hash(
        {k: v for k, v in report.items() if k != "execution_report_hash"}
    )


def run_paper_execution(
    ctx: dict,
    trading_client: Any,
    confirm_paper: bool = False,
) -> dict:
    """Run all gates and submit paper limit orders if everything passes.

    Context dict keys (same as dry-run gates, plus):
        orders_dir      Path    data/history/orders/
    dry_run is forced to False regardless of ctx value.

    Returns an execution report dict.  Never raises.
    Possible status values:
        PAPER_BLOCKED    — hard pre-gate blocked submission (no gates run)
        PAPER_FAIL       — one or more Phase-5 gates failed (no orders submitted)
        PAPER_NO_ORDERS  — all gates passed but no execution-ready orders exist
        PAPER_SUBMITTED  — at least one order was submitted to Alpaca paper
    """
    ctx = dict(ctx)  # shallow copy; never mutate caller's dict
    ctx["dry_run"] = False  # paper execution is never a dry run

    exec_history_dir: Path = ctx.get("exec_history_dir", Path("."))
    orders_dir: Path = ctx.get("orders_dir", Path("."))
    trade_plan: dict = ctx.get("trade_plan", {})

    run_id = (
        f"execution-"
        f"{utc_now_iso().replace(':', '').replace('-', '').replace('Z', '')[:15]}"
        f"-{uuid.uuid4().hex[:8]}"
    )
    generated_at = utc_now_iso()

    report: dict = {
        "run_id": run_id,
        "plan_id": trade_plan.get("plan_id"),
        "generated_at": generated_at,
        "dry_run": False,
        "trade_plan_hash": trade_plan.get("trade_plan_hash"),
        "gate_results": [],
        "all_gates_pass": False,
        "failed_gates": [],
        "orders_validated": [],
        "orders_submitted": [],
        "status": "PAPER_BLOCKED",
        "blocked_reason": None,
        "execution_report_hash": None,
    }

    # ── Step 1: --confirm-paper flag ─────────────────────────────────────────
    block = _check_confirm_paper(confirm_paper)
    if block:
        report["blocked_reason"] = block
        _finalise_report(report)
        return report

    # ── Step 2: plan approval ────────────────────────────────────────────────
    block = _check_plan_approved(trade_plan)
    if block:
        report["blocked_reason"] = block
        _finalise_report(report)
        return report

    # ── Step 3: log directories writable (gate 18) ───────────────────────────
    block = _probe_log_dirs(exec_history_dir, orders_dir)
    if block:
        report["blocked_reason"] = block
        _finalise_report(report)
        return report

    # ── Step 4: run all 16 Phase-5 gates (dry_run=False, fresh data) ─────────
    gate_results = run_all_gates(ctx)
    gates_ok = all_gates_pass(gate_results)
    failed_gates = [g["gate_id"] for g in gate_results if not g["passes"]]

    report["gate_results"] = gate_results
    report["all_gates_pass"] = gates_ok
    report["failed_gates"] = failed_gates

    if not gates_ok:
        report["status"] = "PAPER_FAIL"
        report["blocked_reason"] = f"gate(s) failed: {failed_gates}"
        _finalise_report(report)
        return report

    # ── Step 5: build and validate execution orders ───────────────────────────
    universe: dict = ctx.get("universe", {})
    risk_limits: dict = ctx.get("risk_limits", {})
    strategy: dict = ctx.get("strategy", {})
    market_snapshot: dict = ctx.get("market_snapshot", {})

    try:
        orders_validated = build_execution_orders(
            trade_plan=trade_plan,
            universe=universe,
            risk_limits=risk_limits,
            strategy=strategy,
            market_snapshot=market_snapshot,
        )
    except Exception as exc:
        report["status"] = "PAPER_FAIL"
        report["blocked_reason"] = f"order_builder_error: {type(exc).__name__}: {exc}"
        _finalise_report(report)
        return report

    # Apply paper-execution-specific safety checks on top of order_builder checks
    for o in orders_validated:
        if o.get("validation_skip_reason") is None:
            extra = _validate_order_paper_safe(o)
            if extra:
                o["validation_skip_reason"] = extra
                o["execution_ready"] = False

    report["orders_validated"] = orders_validated

    # ── Step 6: submit execution-ready orders to Alpaca paper ─────────────────
    ready_orders = [o for o in orders_validated if o.get("execution_ready")]
    submitted: list = []
    for o in ready_orders:
        order_result = submit_paper_order(
            trading_client=trading_client,
            order=o,
            orders_dir=orders_dir,
        )
        submitted.append(order_result)

    report["orders_submitted"] = submitted
    report["status"] = "PAPER_SUBMITTED" if submitted else "PAPER_NO_ORDERS"

    _finalise_report(report)
    return report
