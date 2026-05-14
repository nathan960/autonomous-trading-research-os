#!/usr/bin/env python3
"""System status dashboard — reads all data/latest artifacts and produces a status report.

Usage:
    python scripts/system_status.py

Exit codes:
    0  status report written successfully
    1  unrecoverable error (missing required config files)

Outputs:
    data/latest/system_status.json
    memory/SYSTEM-STATUS.md  (appended)

Safety guarantees:
- NEVER submits orders, calls any broker API, or touches any execution path.
- Never calls execute_paper.py or any execution code path.
- Never enables paper execution.
- Never approves trade plans.
- No secrets are printed, logged, or written.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import (
    LATEST_DIR,
    MEMORY_DIR,
    load_config_file,
    load_risk_state,
)
from trading_os.monitoring.system_status import build_system_status, format_status_markdown


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
        print(f"  [system_status] {label} not found — using empty default")
        return {}
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as exc:
        print(f"  [system_status] WARNING: could not parse {label}: {exc}")
        return {}


def _append_status_log(status: dict) -> None:
    log_path = MEMORY_DIR / "SYSTEM-STATUS.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    if existing and not existing.endswith("\n"):
        existing += "\n"
    entry = format_status_markdown(status)
    log_path.write_text(existing + entry, encoding="utf-8")
    print(f"  appended {log_path.relative_to(_ROOT)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("[system_status] collecting status — no orders will be placed or enabled")

    # ── Load configs (required — fail closed) ─────────────────────────────────
    try:
        risk_limits = load_config_file("risk_limits.json")
        execution_policy = load_config_file("execution_policy.json")
        strategy = load_config_file("strategy.json")
    except Exception as exc:
        print(f"[system_status] ERROR loading required config: {exc}", file=sys.stderr)
        return 1

    # ── Load risk state (optional — degrade to empty) ─────────────────────────
    try:
        risk_state = load_risk_state()
    except Exception as exc:
        print(f"  [system_status] WARNING: could not load risk state: {exc}")
        risk_state = {}

    # ── Load data snapshots (all optional — degrade gracefully to YELLOW/RED) ──
    snapshot_files = {
        "account_snapshot":     LATEST_DIR / "account_snapshot.json",
        "positions_snapshot":   LATEST_DIR / "positions_snapshot.json",
        "orders_snapshot":      LATEST_DIR / "orders_snapshot.json",
        "market_snapshot":      LATEST_DIR / "market_snapshot.json",
        "data_quality_snapshot": LATEST_DIR / "data_quality_snapshot.json",
        "trigger_snapshot":     LATEST_DIR / "trigger_snapshot.json",
        "trade_plan":           LATEST_DIR / "trade_plan.json",
        "execution_report":     LATEST_DIR / "execution_report.json",
        "order_monitor_report": LATEST_DIR / "order_monitor_report.json",
        "outcome_snapshot":     LATEST_DIR / "outcome_snapshot.json",
        "lineage_snapshot":     LATEST_DIR / "lineage_snapshot.json",
        "trigger_performance":  LATEST_DIR / "trigger_performance.json",
    }
    snapshots: dict = {
        label: _load_json_optional(path, label)
        for label, path in snapshot_files.items()
    }

    configs = {
        "risk_limits":      risk_limits,
        "execution_policy": execution_policy,
        "strategy":         strategy,
        "risk_state":       risk_state,
    }

    # ── Build status (pure — no I/O, no execution) ────────────────────────────
    status = build_system_status(snapshots, configs)

    # ── Write outputs ──────────────────────────────────────────────────────────
    _write_json(LATEST_DIR / "system_status.json", status)
    _append_status_log(status)

    # ── Print summary ──────────────────────────────────────────────────────────
    overall = status["overall_status"]
    research = status["safe_for_research_cycle"]
    paper = status["safe_for_manual_paper_execution"]
    blocking = status.get("blocking_issues", [])
    warnings = status.get("warnings", [])

    print()
    print(
        f"[system_status] overall={overall}  "
        f"safe_for_research={research}  "
        f"safe_for_paper_execution={paper}"
    )
    if blocking:
        print("[system_status] BLOCKING ISSUES:")
        for b in blocking:
            print(f"  - {b}")
    if warnings:
        print("[system_status] WARNINGS:")
        for w in warnings:
            print(f"  - {w}")
    print()
    print("[system_status] done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
