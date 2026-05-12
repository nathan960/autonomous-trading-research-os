from __future__ import annotations

from typing import Any

from .audit import append_event, new_run_id, record_error
from .file_io import read_json, utc_now_iso
from .paths import LATEST_DIR, ensure_repo_dirs


def run_daily_summary() -> dict[str, Any]:
    ensure_repo_dirs()
    run_id = new_run_id("daily_summary")
    try:
        trigger = read_json(LATEST_DIR / "trigger_snapshot.json", default={})
        plan = read_json(LATEST_DIR / "trade_plan.json", default={})
        execution = read_json(LATEST_DIR / "execution_report.json", default={})
        position = read_json(LATEST_DIR / "position_report.json", default={})
        dq = read_json(LATEST_DIR / "data_quality_report.json", default={})
        summary: dict[str, Any] = {
            "schema_version": "0.1.0",
            "run_id": run_id,
            "generated_at": utc_now_iso(),
            "risk_on": trigger.get("regime", {}).get("risk_on"),
            "breadth": trigger.get("regime", {}).get("breadth"),
            "selected_symbols": [item.get("symbol") for item in trigger.get("selected", [])],
            "plan_status": plan.get("approval", {}).get("status"),
            "plan_targets": plan.get("targets", {}),
            "execution_status": execution.get("status"),
            "submitted_count": len(execution.get("submitted", []) or []),
            "skipped_count": len(execution.get("skipped", []) or []),
            "position_status": position.get("status"),
            "data_quality_status": dq.get("status"),
            "failed_gates": plan.get("no_trade_reasons", []),
        }
        append_event("DAILY-SUMMARY.md", "Daily summary", summary)
        return summary
    except Exception as exc:
        record_error("daily_summary", exc)
        raise
