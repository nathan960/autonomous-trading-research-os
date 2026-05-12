#!/usr/bin/env python3
"""Phase 5 dry-run execution gates — simulate pre-execution checks, no order submission.

Usage:
    python scripts/dry_run_execute.py

Exit codes:
    0  all data loaded, gates evaluated, report written (even if some gates fail)
    1  missing required input files or unrecoverable error

Outputs:
    data/latest/execution_report.json
    data/history/executions/<run_id>_dry_run.json
    memory/TRADE-LOG.md  (appended)

Safety guarantees:
- NEVER submits an order, touches a broker API, or calls any trading endpoint.
- Fails closed (exit 1) if any required file is missing.
- Every gate result is logged regardless of pass/fail.
- No secrets are printed, logged, or written.
"""
from __future__ import annotations

import json
import sys
import uuid
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
from trading_os.execution.execution_gates import all_gates_pass, run_all_gates
from trading_os.execution.order_builder import build_execution_orders
from trading_os.hashing import stable_hash
from trading_os.time_utils import utc_now_iso

_EXEC_HISTORY_DIR = HISTORY_DIR / "executions"


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


def _load_json(path: Path, label: str) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"{label} not found: {path}")
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as exc:
        raise ValueError(f"Could not parse {label}: {exc}") from exc


def _append_trade_log(report: dict) -> None:
    log_path = MEMORY_DIR / "TRADE-LOG.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    if existing and not existing.endswith("\n"):
        existing += "\n"

    failed = [g["gate_id"] for g in report.get("gate_results", []) if not g["passes"]]
    summary = {
        "run_id": report.get("run_id"),
        "generated_at": report.get("generated_at"),
        "plan_id": report.get("plan_id"),
        "dry_run": report.get("dry_run"),
        "status": report.get("status"),
        "all_gates_pass": report.get("all_gates_pass"),
        "failed_gates": failed,
        "orders_validated": len(report.get("orders_validated", [])),
        "orders_ready": sum(1 for o in report.get("orders_validated", []) if o.get("execution_ready")),
        "no_submit_reason": report.get("no_submit_reason"),
        "trade_plan_hash": report.get("trade_plan_hash"),
    }
    block = (
        "\n## dry_run_execute run\n\n"
        "```json\n"
        + json.dumps(summary, indent=2, sort_keys=True, default=str)
        + "\n```\n"
    )
    log_path.write_text(existing + block, encoding="utf-8")
    print(f"  appended {log_path.relative_to(_ROOT)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("[dry_run_execute] starting  dry_run=True  (NEVER submits orders)")

    # ── Load configs ────────────────────────────────────────────────────────
    try:
        strategy = load_config_file("strategy.json")
        risk_limits = load_config_file("risk_limits.json")
        universe = load_config_file("universe.json")
    except Exception as exc:
        print(f"[dry_run_execute] ERROR loading configs: {exc}", file=sys.stderr)
        return 1

    # ── Load risk state ──────────────────────────────────────────────────────
    try:
        risk_state = load_risk_state()
    except Exception as exc:
        print(f"[dry_run_execute] ERROR loading risk state: {exc}", file=sys.stderr)
        return 1

    # ── Load data snapshots — fail closed on any missing file ────────────────
    required_snapshots = {
        "trade_plan":         LATEST_DIR / "trade_plan.json",
        "market_snapshot":    LATEST_DIR / "market_snapshot.json",
        "account_snapshot":   LATEST_DIR / "account_snapshot.json",
        "positions_snapshot": LATEST_DIR / "positions_snapshot.json",
        "orders_snapshot":    LATEST_DIR / "orders_snapshot.json",
    }
    loaded: dict = {}
    for label, path in required_snapshots.items():
        try:
            loaded[label] = _load_json(path, label)
        except FileNotFoundError as exc:
            print(f"[dry_run_execute] ERROR: {exc}", file=sys.stderr)
            print(
                "[dry_run_execute] Run refresh_data.py, scan_triggers.py, and "
                "generate_trade_plan.py first.",
                file=sys.stderr,
            )
            return 1
        except Exception as exc:
            print(f"[dry_run_execute] ERROR loading {label}: {exc}", file=sys.stderr)
            return 1

    trade_plan = loaded["trade_plan"]
    print(f"  trade_plan plan_id={trade_plan.get('plan_id', '?')}")
    print(f"  trade_plan generated_at={trade_plan.get('generated_at', '?')}")
    print(f"  trade_plan proposed_orders={len(trade_plan.get('proposed_orders', []))}")

    # ── Build gate context ───────────────────────────────────────────────────
    _EXEC_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    ctx = {
        "trade_plan":         trade_plan,
        "account_snapshot":   loaded["account_snapshot"],
        "positions_snapshot": loaded["positions_snapshot"],
        "orders_snapshot":    loaded["orders_snapshot"],
        "market_snapshot":    loaded["market_snapshot"],
        "risk_state":         risk_state,
        "universe":           universe,
        "risk_limits":        risk_limits,
        "strategy":           strategy,
        "exec_history_dir":   _EXEC_HISTORY_DIR,
        "dry_run":            True,
    }

    # ── Run all 16 gates ─────────────────────────────────────────────────────
    gate_results = run_all_gates(ctx)
    gates_ok = all_gates_pass(gate_results)

    failed_gates = [g["gate_id"] for g in gate_results if not g["passes"]]
    for g in gate_results:
        icon = "PASS" if g["passes"] else "FAIL"
        detail = f"  [{g['detail']}]" if g.get("detail") else ""
        print(f"  {icon:4s}  {g['gate_id']}{detail}")

    print(f"  all_gates_pass={gates_ok}  failed={failed_gates}")

    # ── Build execution orders (validate, enrich — do NOT submit) ────────────
    try:
        orders_validated = build_execution_orders(
            trade_plan=trade_plan,
            universe=universe,
            risk_limits=risk_limits,
            strategy=strategy,
            market_snapshot=loaded["market_snapshot"],
        )
    except Exception as exc:
        print(f"[dry_run_execute] ERROR building orders: {exc}", file=sys.stderr)
        return 1

    orders_ready = [o for o in orders_validated if o.get("execution_ready")]
    print(f"  orders_validated={len(orders_validated)}  execution_ready={len(orders_ready)}")

    # ── Assemble execution report ─────────────────────────────────────────────
    run_id = f"execution-{utc_now_iso().replace(':', '').replace('-', '').replace('Z', '')[:15]}-{uuid.uuid4().hex[:8]}"
    generated_at = utc_now_iso()

    if gates_ok:
        status = "DRY_RUN_PASS"
    elif any(not g["passes"] and "missing" not in (g.get("detail") or "").lower() for g in gate_results if not g["passes"]):
        status = "DRY_RUN_FAIL"
    else:
        status = "DRY_RUN_FAIL"

    report: dict = {
        "run_id": run_id,
        "plan_id": trade_plan.get("plan_id"),
        "generated_at": generated_at,
        "dry_run": True,
        "trade_plan_hash": trade_plan.get("trade_plan_hash"),
        "gate_results": gate_results,
        "all_gates_pass": gates_ok,
        "failed_gates": failed_gates,
        "orders_validated": orders_validated,
        "orders_submitted": [],
        "no_submit_reason": "dry_run_mode",
        "status": status,
    }
    report["execution_report_hash"] = stable_hash(
        {k: v for k, v in report.items() if k != "execution_report_hash"}
    )

    # ── Write outputs ─────────────────────────────────────────────────────────
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    _write_json(LATEST_DIR / "execution_report.json", report)

    history_path = _EXEC_HISTORY_DIR / f"{run_id}_dry_run.json"
    _write_json(history_path, report)

    _append_trade_log(report)

    print(f"[dry_run_execute] done  status={status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
