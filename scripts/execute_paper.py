#!/usr/bin/env python3
"""Phase 6 paper execution — submit Alpaca paper limit orders after all gates pass.

Usage:
    python scripts/execute_paper.py --confirm-paper

The --confirm-paper flag is required. It acknowledges that paper orders will be
submitted to Alpaca. Without it the script fails closed immediately.

Exit codes:
    0  execution pipeline ran to completion (check status in execution_report.json;
       status may be PAPER_SUBMITTED, PAPER_NO_ORDERS, PAPER_FAIL, or PAPER_BLOCKED)
    1  missing required env vars, missing API keys, missing config/data files,
       or unrecoverable error before the pipeline could run

Outputs:
    data/latest/execution_report.json
    data/history/executions/<run_id>_paper.json
    data/history/orders/<client_order_id>.json   (one per submitted order)
    memory/TRADE-LOG.md  (appended)

Safety guarantees:
- Fails closed (exit 1) if TRADING_MODE, ALPACA_PAPER, ENABLE_PAPER_EXECUTION,
  or LIVE_TRADING_CONFIRMED env vars are missing or wrong.
- Fails closed (exit 1) if ALPACA_API_KEY or ALPACA_API_SECRET are absent.
- Fails closed (exit 1) if any required config or trade_plan.json is missing.
- Never submits orders if any of the 16 execution gates fails.
- Never submits orders if trade_plan.approval.approved_for_execution is not True.
- Never prints, logs, or writes API keys or secrets.
- Orders history dir and execution history dir are both probed for writability
  before any order submission.
"""
from __future__ import annotations

import argparse
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
from trading_os.data.account_state import fetch_account_state
from trading_os.data.alpaca_client import AlpacaPaperClient
from trading_os.execution.paper_executor import (
    _check_hard_env_gates,
    run_paper_execution,
)
from trading_os.hashing import stable_hash
from trading_os.time_utils import utc_now_iso

_EXEC_HISTORY_DIR = HISTORY_DIR / "executions"
_ORDERS_HISTORY_DIR = HISTORY_DIR / "orders"


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

    submitted = report.get("orders_submitted", [])
    summary = {
        "run_id": report.get("run_id"),
        "generated_at": report.get("generated_at"),
        "plan_id": report.get("plan_id"),
        "dry_run": report.get("dry_run"),
        "status": report.get("status"),
        "all_gates_pass": report.get("all_gates_pass"),
        "failed_gates": report.get("failed_gates"),
        "blocked_reason": report.get("blocked_reason"),
        "orders_validated": len(report.get("orders_validated", [])),
        "orders_submitted": len(submitted),
        "orders_submitted_ok": sum(1 for o in submitted if o.get("submitted")),
        "orders_submitted_err": sum(1 for o in submitted if o.get("error")),
        "trade_plan_hash": report.get("trade_plan_hash"),
    }
    block = (
        "\n## execute_paper run\n\n"
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
    parser = argparse.ArgumentParser(
        description="Phase 6 paper execution — submit Alpaca paper limit orders."
    )
    parser.add_argument(
        "--confirm-paper",
        action="store_true",
        default=False,
        help=(
            "Required. Acknowledge that paper orders will be submitted to Alpaca. "
            "Without this flag the script fails closed."
        ),
    )
    args = parser.parse_args()

    print(
        "[execute_paper] starting  dry_run=False  confirm_paper="
        f"{args.confirm_paper}  (paper orders will be submitted if all gates pass)"
    )

    # ── Hard env gates — must pass before any network call ───────────────────
    try:
        _check_hard_env_gates()
    except RuntimeError as exc:
        print(f"[execute_paper] FATAL env gate: {exc}", file=sys.stderr)
        return 1

    # ── Load configs ─────────────────────────────────────────────────────────
    try:
        strategy = load_config_file("strategy.json")
        risk_limits = load_config_file("risk_limits.json")
        universe = load_config_file("universe.json")
        execution_policy = load_config_file("execution_policy.json")
    except Exception as exc:
        print(f"[execute_paper] ERROR loading configs: {exc}", file=sys.stderr)
        return 1

    # ── Load risk state ───────────────────────────────────────────────────────
    try:
        risk_state = load_risk_state()
    except Exception as exc:
        print(f"[execute_paper] ERROR loading risk state: {exc}", file=sys.stderr)
        return 1

    # ── Load trade plan — fail closed if missing ──────────────────────────────
    trade_plan_path = LATEST_DIR / "trade_plan.json"
    try:
        trade_plan = _load_json(trade_plan_path, "trade_plan")
    except FileNotFoundError as exc:
        print(f"[execute_paper] ERROR: {exc}", file=sys.stderr)
        print(
            "[execute_paper] Run refresh_data.py, scan_triggers.py, and "
            "generate_trade_plan.py --approve-paper first.",
            file=sys.stderr,
        )
        return 1
    except Exception as exc:
        print(f"[execute_paper] ERROR loading trade_plan: {exc}", file=sys.stderr)
        return 1

    print(f"  trade_plan plan_id={trade_plan.get('plan_id', '?')}")
    print(f"  trade_plan generated_at={trade_plan.get('generated_at', '?')}")
    print(
        f"  trade_plan approved_for_execution="
        f"{trade_plan.get('approval', {}).get('approved_for_execution', '?')}"
    )
    print(f"  trade_plan proposed_orders={len(trade_plan.get('proposed_orders', []))}")

    # ── Connect to Alpaca paper broker and fetch fresh state ─────────────────
    # AlpacaPaperClient constructor enforces TRADING_MODE, ALPACA_PAPER,
    # LIVE_TRADING_CONFIRMED, and key/secret presence.
    try:
        alpaca_client = AlpacaPaperClient()
        trading_client = alpaca_client.trading_client()
    except RuntimeError as exc:
        print(f"[execute_paper] FATAL broker gate: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"[execute_paper] ERROR creating Alpaca client: {exc}", file=sys.stderr)
        return 1

    print("  Alpaca paper client created — fetching fresh account state...")
    try:
        fresh_state = fetch_account_state(alpaca_client)
    except Exception as exc:
        print(f"[execute_paper] ERROR fetching account state: {exc}", file=sys.stderr)
        return 1

    # Decompose fresh_state into the snapshot dicts expected by gate functions
    account_snapshot = {
        "account": fresh_state.get("account", {}),
        "clock": fresh_state.get("clock", {}),
        "position_count": fresh_state.get("position_count", 0),
        "fetched_at": fresh_state.get("fetched_at", ""),
    }
    positions_snapshot = {
        "positions": fresh_state.get("positions", []),
        "position_count": fresh_state.get("position_count", 0),
        "fetched_at": fresh_state.get("fetched_at", ""),
    }
    orders_snapshot = {
        "orders": fresh_state.get("orders", []),
        "open_order_count": fresh_state.get("open_order_count", 0),
    }

    clock = fresh_state.get("clock", {})
    print(
        f"  fresh account fetched  is_open={clock.get('is_open')}  "
        f"positions={fresh_state.get('position_count')}  "
        f"open_orders={fresh_state.get('open_order_count')}"
    )

    # ── Load latest market snapshot (quotes/spreads freshness gate will catch stale) ─
    market_snapshot_path = LATEST_DIR / "market_snapshot.json"
    try:
        market_snapshot = _load_json(market_snapshot_path, "market_snapshot")
    except FileNotFoundError as exc:
        print(f"[execute_paper] ERROR: {exc}", file=sys.stderr)
        print(
            "[execute_paper] Run refresh_data.py first.", file=sys.stderr
        )
        return 1
    except Exception as exc:
        print(f"[execute_paper] ERROR loading market_snapshot: {exc}", file=sys.stderr)
        return 1

    # ── Set up history directories ────────────────────────────────────────────
    _EXEC_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    _ORDERS_HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    # ── Build gate context (dry_run=False forced inside run_paper_execution) ──
    ctx = {
        "trade_plan":         trade_plan,
        "account_snapshot":   account_snapshot,
        "positions_snapshot": positions_snapshot,
        "orders_snapshot":    orders_snapshot,
        "market_snapshot":    market_snapshot,
        "risk_state":         risk_state,
        "universe":           universe,
        "risk_limits":        risk_limits,
        "strategy":           strategy,
        "exec_history_dir":   _EXEC_HISTORY_DIR,
        "orders_dir":         _ORDERS_HISTORY_DIR,
        "dry_run":            False,
    }

    # ── Run the full paper execution pipeline ─────────────────────────────────
    report = run_paper_execution(
        ctx=ctx,
        trading_client=trading_client,
        confirm_paper=args.confirm_paper,
    )

    # Print gate results
    for g in report.get("gate_results", []):
        icon = "PASS" if g["passes"] else "FAIL"
        detail = f"  [{g['detail']}]" if g.get("detail") else ""
        print(f"  {icon:4s}  {g['gate_id']}{detail}")

    gates_ok = report.get("all_gates_pass", False)
    failed = report.get("failed_gates", [])
    print(f"  all_gates_pass={gates_ok}  failed={failed}")

    submitted = report.get("orders_submitted", [])
    for o in submitted:
        icon = "OK" if o.get("submitted") else "ERR"
        err = f"  error={o['error']}" if o.get("error") else ""
        print(
            f"  {icon}  {o['symbol']} {o['side'].upper()} "
            f"notional={o['notional']:.2f} limit={o['limit_price']}"
            f"  broker_id={o.get('broker_order_id')}{err}"
        )

    status = report.get("status", "?")
    blocked = report.get("blocked_reason")
    if blocked:
        print(f"  blocked_reason: {blocked}")
    print(f"  orders_submitted={len(submitted)}")

    # ── Write outputs ─────────────────────────────────────────────────────────
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    _write_json(LATEST_DIR / "execution_report.json", report)

    run_id = report["run_id"]
    history_path = _EXEC_HISTORY_DIR / f"{run_id}_paper.json"
    _write_json(history_path, report)

    _append_trade_log(report)

    print(f"[execute_paper] done  status={status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
