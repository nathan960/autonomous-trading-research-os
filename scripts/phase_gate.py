#!/usr/bin/env python3
"""Phase-gate scorecard — evidence review for paper ops promotion decisions.

Usage:
    python scripts/phase_gate.py

Exit codes:
    0  scorecard written
    1  unrecoverable error (missing required config)

Outputs:
    data/latest/phase_gate.json
    data/history/runs/phase_gate_<date>-<hash>.json
    memory/PROMOTION-DECISIONS.md  (appended)

Safety guarantees:
- NEVER submits orders, calls any broker API, or touches any execution path.
- Never calls execute_paper.py or any execution code path.
- Never enables paper execution.
- Never approves trade plans.
- Never modifies risk_limits.json or any config file.
- Never recommends PHASE_4 activation.
- No secrets are printed, logged, or written.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import (
    HISTORY_DIR,
    LATEST_DIR,
    MEMORY_DIR,
    load_config_file,
    load_risk_state,
)
from trading_os.research.phase_gate import build_phase_gate, format_phase_gate_markdown
from trading_os.time_utils import utc_now_iso


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True, default=str)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(path)
    print(f"  wrote {path.relative_to(_ROOT)}")


def _load_json_optional(path: Path, label: str) -> dict:
    """Load a JSON file; return empty dict if absent or unreadable."""
    if not path.exists():
        print(f"  [phase_gate] {label} not found — using empty default")
        return {}
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as exc:
        print(f"  [phase_gate] WARNING: could not parse {label}: {exc}")
        return {}


def _count_history_runs(runs_dir: Path, prefix: str) -> int:
    """Count JSON files in data/history/runs/ matching a prefix."""
    if not runs_dir.is_dir():
        return 0
    return sum(1 for f in runs_dir.glob(f"{prefix}*.json") if f.is_file())


def _append_promotion_log(result: dict) -> None:
    log_path = MEMORY_DIR / "PROMOTION-DECISIONS.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    if not existing:
        existing = "# Promotion Decisions\n\nProduction strategy promotions require evidence, candidate PR, and explicit approval.\n"
    if existing and not existing.endswith("\n"):
        existing += "\n"
    entry = format_phase_gate_markdown(result)
    log_path.write_text(existing + entry, encoding="utf-8")
    print(f"  appended {log_path.relative_to(_ROOT)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("[phase_gate] starting — no orders will be placed or enabled")
    print("[phase_gate] no config will be modified")

    # ── Load configs (required — fail closed) ─────────────────────────────────
    try:
        risk_limits = load_config_file("risk_limits.json")
    except Exception as exc:
        print(f"[phase_gate] ERROR loading risk_limits.json: {exc}", file=sys.stderr)
        return 1

    # ── Load risk state (optional) ────────────────────────────────────────────
    try:
        risk_state = load_risk_state()
    except Exception as exc:
        print(f"  [phase_gate] WARNING: could not load risk state: {exc} — using empty")
        risk_state = {}

    # ── Load data snapshots (all optional — degrade gracefully) ──────────────
    snapshot_files = {
        "system_status":       LATEST_DIR / "system_status.json",
        "order_monitor_report": LATEST_DIR / "order_monitor_report.json",
        "outcome_snapshot":    LATEST_DIR / "outcome_snapshot.json",
        "lineage_snapshot":    LATEST_DIR / "lineage_snapshot.json",
        "trigger_performance": LATEST_DIR / "trigger_performance.json",
        "execution_report":    LATEST_DIR / "execution_report.json",
        "trade_plan":          LATEST_DIR / "trade_plan.json",
    }
    snapshots: dict = {
        label: _load_json_optional(path, label)
        for label, path in snapshot_files.items()
    }

    # ── Count history artifacts ────────────────────────────────────────────────
    runs_dir = HISTORY_DIR / "runs"
    daily_summaries = _count_history_runs(runs_dir, "daily_summary")
    weekly_reviews = _count_history_runs(runs_dir, "weekly_review")
    history_counts = {
        "daily_summaries": daily_summaries,
        "weekly_reviews": weekly_reviews,
    }
    print(f"  history_counts  daily_summaries={daily_summaries}  weekly_reviews={weekly_reviews}")

    # ── Build scorecard (pure — no I/O, no execution) ─────────────────────────
    result = build_phase_gate(
        system_status=snapshots["system_status"],
        order_monitor_report=snapshots["order_monitor_report"],
        outcome_snapshot=snapshots["outcome_snapshot"],
        lineage_snapshot=snapshots["lineage_snapshot"],
        trigger_performance=snapshots["trigger_performance"],
        execution_report=snapshots["execution_report"],
        trade_plan=snapshots["trade_plan"],
        risk_state=risk_state,
        risk_limits=risk_limits,
        history_counts=history_counts,
    )

    # ── Write outputs ──────────────────────────────────────────────────────────
    _write_json(LATEST_DIR / "phase_gate.json", result)

    # History run file
    date_str = (result.get("generated_at") or utc_now_iso())[:10]
    run_id = result.get("run_id", "phase_gate-unknown")
    run_hash = result.get("phase_gate_hash", "00000000")[:8]
    history_name = f"phase_gate_{date_str}-{run_hash}.json"
    _write_json(runs_dir / history_name, result)

    _append_promotion_log(result)

    # ── Print summary ──────────────────────────────────────────────────────────
    phase = result["current_phase"]
    eligible = result["eligible_for_next_phase"]
    recommendation = result["recommendation"]
    blocking = result.get("blocking_issues", [])
    warnings = result.get("warnings", [])

    print()
    print(
        f"[phase_gate] current_phase={phase}  "
        f"eligible_for_next_phase={eligible}  "
        f"recommendation={recommendation}"
    )
    if blocking:
        print("[phase_gate] BLOCKING ISSUES:")
        for b in blocking:
            print(f"  - {b}")
    if warnings:
        print("[phase_gate] WARNINGS:")
        for w in warnings:
            print(f"  - {w}")
    print()
    print(f"[phase_gate] safety_note: {result['safety_note']}")
    print("[phase_gate] done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
