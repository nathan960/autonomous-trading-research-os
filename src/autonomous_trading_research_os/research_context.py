from __future__ import annotations

from typing import Any

from .audit import append_event, new_run_id, record_error
from .file_io import read_json, utc_now_iso
from .paths import LATEST_DIR, RESEARCH_DIR, ensure_repo_dirs


def run_research_context() -> dict[str, Any]:
    ensure_repo_dirs()
    run_id = new_run_id("research_context")
    try:
        plan = read_json(LATEST_DIR / "trade_plan.json", default={})
        dq = read_json(LATEST_DIR / "data_quality_report.json", default={})
        inbox_path = RESEARCH_DIR / "inbox.md"
        manual_notes = inbox_path.read_text(encoding="utf-8") if inbox_path.exists() else ""
        report: dict[str, Any] = {
            "schema_version": "0.1.0",
            "run_id": run_id,
            "generated_at": utc_now_iso(),
            "scope": "research_context_only_not_trade_critical",
            "trade_generation_allowed": False,
            "latest_plan_status": plan.get("approval", {}).get("status"),
            "latest_plan_target_reason": plan.get("target_reason"),
            "latest_data_quality_status": dq.get("status"),
            "manual_research_notes_present": bool(manual_notes.strip()),
            "notes": [
                "Research context may support hypotheses only.",
                "Do not create orders from web or connector content.",
                "Production strategy changes require evidence, PR review, and explicit approval."
            ],
        }
        append_event("RESEARCH-CONTEXT.md", "Research context reviewed", report)
        return report
    except Exception as exc:
        record_error("research_context", exc)
        raise
