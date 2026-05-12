from __future__ import annotations

from typing import Any

from .audit import append_event, new_run_id, record_error
from .file_io import read_json, utc_now_iso
from .paths import LATEST_DIR, MEMORY_DIR, ensure_repo_dirs


def _count_log_entries(filename: str) -> int:
    path = MEMORY_DIR / filename
    if not path.exists():
        return 0
    return path.read_text(encoding="utf-8").count("\n## ")


def run_weekly_review() -> dict[str, Any]:
    ensure_repo_dirs()
    run_id = new_run_id("weekly_review")
    try:
        plan = read_json(LATEST_DIR / "trade_plan.json", default={})
        position = read_json(LATEST_DIR / "position_report.json", default={})
        summary: dict[str, Any] = {
            "schema_version": "0.1.0",
            "run_id": run_id,
            "generated_at": utc_now_iso(),
            "trigger_log_entries": _count_log_entries("TRIGGER-LOG.md"),
            "signal_log_entries": _count_log_entries("SIGNAL-LOG.md"),
            "trade_log_entries": _count_log_entries("TRADE-LOG.md"),
            "data_quality_entries": _count_log_entries("DATA-QUALITY-LOG.md"),
            "latest_plan_status": plan.get("approval", {}).get("status"),
            "latest_position_status": position.get("status"),
            "review_notes": [
                "Do not overfit from a short paper run.",
                "Evaluate trigger hit rate, skip reasons, fills, slippage, drawdown, and operational failures over time.",
                "Escalate only evidence-backed experiments to strategy improvement review."
            ],
        }
        append_event("WEEKLY-REVIEW.md", "Weekly review", summary)
        return summary
    except Exception as exc:
        record_error("weekly_review", exc)
        raise
