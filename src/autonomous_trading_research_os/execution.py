from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .alpaca_adapter import AlpacaAdapter
from .audit import append_event, new_run_id, record_error
from .file_io import parse_iso_datetime, read_json, utc_now_iso, write_json
from .paths import CONFIG_DIR, LATEST_DIR, ensure_repo_dirs
from .settings import RuntimeSettings
from .risk import all_gates_pass, evaluate_plan_risk
from .trade_plan import _build_orders


def _plan_expired(plan: dict[str, Any]) -> bool:
    expires_at = parse_iso_datetime(str(plan.get("expires_at") or ""))
    if expires_at is None:
        return True
    return datetime.now(timezone.utc) >= expires_at


def _clock_is_open(snapshot: dict[str, Any]) -> bool:
    clock = snapshot.get("clock", {}) if isinstance(snapshot.get("clock"), dict) else {}
    return bool(clock.get("is_open"))


def execute_trade_plan(dry_run: bool = True, confirm_paper: bool = False) -> dict[str, Any]:
    ensure_repo_dirs()
    run_id = new_run_id("execution")
    try:
        settings = RuntimeSettings.from_env()
        plan = read_json(LATEST_DIR / "trade_plan.json", default=None)
        snapshot = read_json(LATEST_DIR / "market_snapshot.json", default={})
        if plan is None:
            raise RuntimeError("No trade_plan.json found. Execution is blocked.")

        validation: list[dict[str, Any]] = []
        validation.append({"id": "PLAN_EXISTS", "passed": True, "reason": "data/latest/trade_plan.json exists."})
        validation.append({"id": "PLAN_NOT_EXPIRED", "passed": not _plan_expired(plan), "reason": "Plan expiry must be in the future."})
        validation.append({"id": "PAPER_ONLY_SETTINGS", "passed": settings.trading_mode == "paper" and settings.alpaca_paper and not settings.live_trading_confirmed, "reason": "Runtime settings must be paper-only.", "details": settings.redacted_summary()})
        validation.append({"id": "MARKET_CLOCK_OPEN", "passed": _clock_is_open(snapshot), "reason": "Alpaca market clock must be open for submission."})
        validation.append({"id": "PLAN_NOT_DRY_RUN", "passed": not bool(plan.get("dry_run")), "reason": "Actual submission requires a non-dry-run approved paper plan."})
        validation.append({"id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA", "passed": plan.get("trade_critical_data_source") == "alpaca_paper" and plan.get("trade_critical_run_mode") == "alpaca_paper", "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."})
        validation.extend(plan.get("risk_gates", []))

        candidate_orders = [order for order in plan.get("proposed_orders", []) if order.get("action") == "submit_candidate"]
        submitted: list[dict[str, Any]] = []
        skipped: list[dict[str, Any]] = []

        if dry_run:
            status = "DRY_RUN_NO_SUBMISSION"
            skipped = [{"symbol": order.get("symbol"), "reason": "dry_run_execution"} for order in candidate_orders]
        else:
            settings.validate_paper_only()
            if not confirm_paper:
                status = "BLOCKED"
                skipped = [{"symbol": order.get("symbol"), "reason": "missing_--confirm-paper"} for order in candidate_orders]
            elif not settings.allow_paper_order_submission:
                status = "BLOCKED"
                skipped = [{"symbol": order.get("symbol"), "reason": "ALLOW_PAPER_ORDER_SUBMISSION_not_true"} for order in candidate_orders]
            elif plan.get("approval", {}).get("status") != "APPROVED_FOR_PAPER":
                status = "BLOCKED"
                skipped = [{"symbol": order.get("symbol"), "reason": "plan_not_approved_for_paper"} for order in candidate_orders]
            elif any(not item.get("passed") for item in validation):
                status = "BLOCKED"
                skipped = [{"symbol": order.get("symbol"), "reason": "risk_gate_failed"} for order in candidate_orders]
            else:
                adapter = AlpacaAdapter(settings)
                # Revalidation must happen immediately before submission.
                strategy = read_json(CONFIG_DIR / "strategy.json", default={})
                universe = read_json(CONFIG_DIR / "universe.json", default={})
                sector_map = read_json(CONFIG_DIR / "sector_map.json", default={})
                target_symbols = sorted(plan.get("targets", {}).keys())
                revalidated_snapshot = adapter.refresh_snapshot(target_symbols)
                revalidated_orders = _build_orders(
                    revalidated_snapshot,
                    {symbol: float(weight) for symbol, weight in plan.get("targets", {}).items()},
                    run_id,
                    float(strategy.get("parameters", {}).get("min_order_notional", 25.0)),
                )
                revalidation_gates = evaluate_plan_risk(
                    plan.get("targets", {}),
                    revalidated_orders,
                    strategy,
                    universe,
                    sector_map,
                    revalidated_snapshot,
                    require_alpaca_trade_data=True,
                )
                validation.extend({**gate, "id": f"REVALIDATED_{gate.get('id')}"} for gate in revalidation_gates)
                if not _clock_is_open(revalidated_snapshot):
                    status = "BLOCKED"
                    skipped = [{"symbol": order.get("symbol"), "reason": "revalidated_market_clock_closed"} for order in revalidated_orders if order.get("action") == "submit_candidate"]
                elif not all_gates_pass(revalidation_gates):
                    status = "BLOCKED"
                    skipped = [{"symbol": order.get("symbol"), "reason": "revalidated_risk_gate_failed"} for order in revalidated_orders if order.get("action") == "submit_candidate"]
                else:
                    candidate_orders = [order for order in revalidated_orders if order.get("action") == "submit_candidate"]
                    status = "SUBMITTED"
                    for order in candidate_orders:
                        submitted.append(adapter.submit_market_order(order))

        report: dict[str, Any] = {
            "schema_version": "0.1.0",
            "run_id": run_id,
            "generated_at": utc_now_iso(),
            "dry_run": dry_run,
            "confirm_paper": confirm_paper,
            "status": status,
            "trade_plan_hash": plan.get("trade_plan_hash"),
            "validation": validation,
            "candidate_order_count": len(candidate_orders),
            "submitted": submitted,
            "skipped": skipped,
        }
        write_json(LATEST_DIR / "execution_report.json", report)
        append_event("TRADE-LOG.md", "Execution attempt completed", report)
        return report
    except Exception as exc:
        record_error("execution", exc, {"dry_run": dry_run, "confirm_paper": confirm_paper})
        raise
