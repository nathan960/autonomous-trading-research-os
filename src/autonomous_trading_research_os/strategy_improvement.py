from __future__ import annotations

from typing import Any

from .audit import append_event, new_run_id, record_error
from .file_io import read_json, utc_now_iso
from .paths import LATEST_DIR, MEMORY_DIR, ensure_repo_dirs


def _entries(filename: str) -> int:
    path = MEMORY_DIR / filename
    if not path.exists():
        return 0
    return path.read_text(encoding="utf-8").count("\n## ")


def run_strategy_improvement_review() -> dict[str, Any]:
    ensure_repo_dirs()
    run_id = new_run_id("strategy_improvement")
    try:
        dq = read_json(LATEST_DIR / "data_quality_report.json", default={})
        trade_entries = _entries("TRADE-LOG.md")
        trigger_entries = _entries("TRIGGER-LOG.md")
        enough_evidence = trade_entries >= 20 and trigger_entries >= 20 and dq.get("status") == "PASS"
        report: dict[str, Any] = {
            "schema_version": "0.1.0",
            "run_id": run_id,
            "generated_at": utc_now_iso(),
            "evidence_counts": {
                "trade_log_entries": trade_entries,
                "trigger_log_entries": trigger_entries,
            },
            "promotion_recommended": False,
            "production_mutation_allowed": False,
            "reason": "Insufficient paper evidence for promotion." if not enough_evidence else "Evidence threshold reached; still require candidate PR, backtest/paper analysis, and explicit approval.",
            "candidate_hypotheses": [
                {
                    "hypothesis": "Review breadth threshold sensitivity after enough trigger outcomes accumulate.",
                    "status": "hypothesis_only",
                    "requires": ["trigger outcomes", "paper fills", "drawdown evidence", "candidate PR"]
                },
                {
                    "hypothesis": "Compare ATR% weighting against capped equal weight as an experiment.",
                    "status": "hypothesis_only",
                    "requires": ["backtest", "paper comparison", "risk review", "candidate PR"]
                }
            ],
        }
        append_event("EXPERIMENT-LOG.md", "Strategy improvement hypotheses reviewed", report)
        append_event("PROMOTION-DECISIONS.md", "Promotion decision", {
            "run_id": run_id,
            "generated_at": report["generated_at"],
            "promotion_recommended": False,
            "production_mutation_allowed": False,
            "reason": report["reason"],
        })
        return report
    except Exception as exc:
        record_error("strategy_improvement", exc)
        raise
