#!/usr/bin/env python3
"""Phase 5 position monitor — re-fetch broker state and update RISK-STATE.json.

Usage:
    python scripts/monitor_positions.py
    python scripts/monitor_positions.py --dry-run   # use stored snapshots, no network

Exit codes:
    0  monitor completed; RISK-STATE.json and POSITION-MONITOR.md updated
    1  missing env vars, missing API keys, fetch error, or unrecoverable failure

Outputs:
    memory/RISK-STATE.json           (updated in-place)
    memory/POSITION-MONITOR.md       (appended)
    data/history/portfolio/<run_id>_portfolio.json  (per-run record)

Safety guarantees:
- Never places orders. Never submits to Alpaca trading endpoints.
- Fails closed (exit 1) if TRADING_MODE != paper or ALPACA_PAPER is not true/1.
- Never prints, logs, or writes API keys or secrets.
- Atomic file writes via .tmp → .replace().
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import (
    HISTORY_DIR,
    LATEST_DIR,
    MEMORY_DIR,
    load_risk_state,
)
from trading_os.hashing import stable_hash
from trading_os.time_utils import utc_now_iso

_PORTFOLIO_DIR = HISTORY_DIR / "portfolio"
_RISK_STATE_PATH = MEMORY_DIR / "RISK-STATE.json"
_MONITOR_LOG_PATH = MEMORY_DIR / "POSITION-MONITOR.md"


# ---------------------------------------------------------------------------
# Env guards — called before any network I/O
# ---------------------------------------------------------------------------

def _check_env_gates() -> None:
    """Raise RuntimeError if paper-mode env vars are not correct."""
    mode = os.environ.get("TRADING_MODE", "")
    if mode.lower() != "paper":
        raise RuntimeError(
            f"TRADING_MODE must be 'paper' (got '{mode}'). "
            "monitor_positions.py never runs in live mode."
        )
    alpaca_paper = os.environ.get("ALPACA_PAPER", "").lower()
    if alpaca_paper not in ("true", "1"):
        raise RuntimeError(
            f"ALPACA_PAPER must be 'true' or '1' (got '{alpaca_paper}'). "
            "monitor_positions.py only operates in paper mode."
        )
    if os.environ.get("LIVE_TRADING_CONFIRMED", "").lower() in (
        "true", "1", "yes", "y", "on"
    ):
        raise RuntimeError(
            "LIVE_TRADING_CONFIRMED must not be set — "
            "monitor_positions.py refuses to run when live trading is confirmed."
        )


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


def _append_monitor_log(report: dict) -> None:
    _MONITOR_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = (
        _MONITOR_LOG_PATH.read_text(encoding="utf-8")
        if _MONITOR_LOG_PATH.exists()
        else ""
    )
    if existing and not existing.endswith("\n"):
        existing += "\n"
    summary = {
        "run_id": report.get("run_id"),
        "generated_at": report.get("generated_at"),
        "source": report.get("source"),
        "equity": report.get("equity"),
        "peak_equity": report.get("peak_equity"),
        "drawdown": report.get("drawdown"),
        "position_count": report.get("position_count"),
        "open_order_count": report.get("open_order_count"),
        "dry_run": report.get("dry_run"),
    }
    block = (
        "\n## monitor_positions run\n\n"
        "```json\n"
        + json.dumps(summary, indent=2, sort_keys=True, default=str)
        + "\n```\n"
    )
    _MONITOR_LOG_PATH.write_text(existing + block, encoding="utf-8")
    print(f"  appended {_MONITOR_LOG_PATH.relative_to(_ROOT)}")


# ---------------------------------------------------------------------------
# Core logic — pure, testable
# ---------------------------------------------------------------------------

def compute_risk_state_update(
    current_risk_state: dict,
    positions: list,
    account: dict,
    run_id: str,
    updated_at: str,
) -> dict:
    """Compute the new RISK-STATE.json content from broker data.

    Never places orders. Never touches network. Pure computation.
    """
    # Derive equity — prefer portfolio_value, fall back to equity, then last_equity
    equity: float = 0.0
    for key in ("portfolio_value", "equity", "last_equity"):
        raw = account.get(key)
        if raw is not None:
            try:
                v = float(raw)
                if v > 0:
                    equity = v
                    break
            except (TypeError, ValueError):
                pass

    prior_peak: float = float(current_risk_state.get("peak_equity") or equity or 1.0)
    new_peak: float = max(prior_peak, equity) if equity > 0 else prior_peak

    drawdown: float = 0.0
    if new_peak > 0 and equity > 0:
        drawdown = round((equity - new_peak) / new_peak, 6)

    return {
        "schema_version": "0.1.0",
        "last_monitor_run_id": run_id,
        "latest_equity": round(equity, 2) if equity > 0 else current_risk_state.get("latest_equity", 0.0),
        "peak_equity": round(new_peak, 2),
        "drawdown": drawdown,
        "position_count": len([p for p in positions if p]),
        "updated_at": updated_at,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Phase 5 position monitor — re-fetch broker state, update RISK-STATE."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Use stored snapshots from data/latest/ instead of fetching from Alpaca.",
    )
    args = parser.parse_args()

    import hashlib
    run_ts = utc_now_iso().replace(":", "").replace("-", "")[:15]
    run_suffix = hashlib.sha256(run_ts.encode()).hexdigest()[:8]
    run_id = f"monitor_positions-{run_ts}-{run_suffix}"

    print(
        f"[monitor_positions] starting  run_id={run_id}  dry_run={args.dry_run}"
    )

    # ── Env gates — before any network call ──────────────────────────────────
    if not args.dry_run:
        try:
            _check_env_gates()
        except RuntimeError as exc:
            print(f"[monitor_positions] FATAL env gate: {exc}", file=sys.stderr)
            return 1

    # ── Load current risk state ───────────────────────────────────────────────
    try:
        current_risk_state = load_risk_state()
    except Exception as exc:
        print(
            f"[monitor_positions] ERROR loading RISK-STATE.json: {exc}",
            file=sys.stderr,
        )
        return 1

    # ── Fetch or load broker state ────────────────────────────────────────────
    positions: list = []
    account: dict = {}
    orders: list = []
    open_order_count: int = 0
    source: str = "unknown"

    if args.dry_run:
        print("  dry_run=True — loading stored snapshots from data/latest/")
        try:
            pos_snap = _load_json(
                LATEST_DIR / "positions_snapshot.json", "positions_snapshot"
            )
            positions = pos_snap.get("positions", [])
            source = pos_snap.get("source", "stored_snapshot")
        except FileNotFoundError:
            print(
                "[monitor_positions] WARNING: positions_snapshot.json not found — "
                "positions will be empty",
                file=sys.stderr,
            )
            positions = []
            source = "stored_snapshot_missing"

        try:
            ord_snap = _load_json(
                LATEST_DIR / "orders_snapshot.json", "orders_snapshot"
            )
            orders = ord_snap.get("orders", [])
            open_order_count = ord_snap.get("open_order_count", len(orders))
        except FileNotFoundError:
            orders = []
            open_order_count = 0

        try:
            mkt_snap = _load_json(
                LATEST_DIR / "market_snapshot.json", "market_snapshot"
            )
            account_inner = mkt_snap.get("account", {})
            if account_inner:
                account = account_inner
        except FileNotFoundError:
            account = {}

    else:
        # Live fetch via Alpaca paper client
        try:
            from trading_os.data.alpaca_client import AlpacaPaperClient
            from trading_os.data.account_state import fetch_account_state

            alpaca_client = AlpacaPaperClient()
            fresh_state = fetch_account_state(alpaca_client)
        except RuntimeError as exc:
            print(
                f"[monitor_positions] FATAL broker gate: {exc}", file=sys.stderr
            )
            return 1
        except Exception as exc:
            print(
                f"[monitor_positions] ERROR fetching account state: {exc}",
                file=sys.stderr,
            )
            return 1

        positions = fresh_state.get("positions", [])
        orders = fresh_state.get("orders", [])
        open_order_count = fresh_state.get("open_order_count", 0)
        account = fresh_state.get("account", {})
        source = fresh_state.get("source", "alpaca_paper")

        clock = fresh_state.get("clock", {})
        print(
            f"  fetched from Alpaca  is_open={clock.get('is_open')}  "
            f"positions={len(positions)}  open_orders={open_order_count}"
        )

    # ── Compute new risk state ────────────────────────────────────────────────
    updated_at = utc_now_iso()
    new_risk_state = compute_risk_state_update(
        current_risk_state=current_risk_state,
        positions=positions,
        account=account,
        run_id=run_id,
        updated_at=updated_at,
    )

    equity = new_risk_state["latest_equity"]
    peak = new_risk_state["peak_equity"]
    drawdown = new_risk_state["drawdown"]
    position_count = new_risk_state["position_count"]

    print(
        f"  equity={equity}  peak={peak}  drawdown={drawdown:.4%}  "
        f"positions={position_count}"
    )

    # ── Build portfolio report ────────────────────────────────────────────────
    portfolio_report: dict = {
        "schema_version": "0.1.0",
        "run_id": run_id,
        "generated_at": updated_at,
        "source": source,
        "dry_run": args.dry_run,
        "equity": equity,
        "peak_equity": peak,
        "drawdown": drawdown,
        "position_count": position_count,
        "open_order_count": open_order_count,
        "positions": positions,
        "orders_summary": [
            {
                "symbol": o.get("symbol"),
                "side": o.get("side"),
                "qty": o.get("qty"),
                "status": o.get("status"),
            }
            for o in orders
        ],
    }
    portfolio_report["data_hash"] = stable_hash(
        {k: v for k, v in portfolio_report.items() if k != "data_hash"}
    )

    # ── Write outputs ─────────────────────────────────────────────────────────
    # 1. Update RISK-STATE.json (atomic)
    _write_json(_RISK_STATE_PATH, new_risk_state)

    # 2. Write per-run portfolio report to history
    _PORTFOLIO_DIR.mkdir(parents=True, exist_ok=True)
    portfolio_path = _PORTFOLIO_DIR / f"{run_id}_portfolio.json"
    _write_json(portfolio_path, portfolio_report)

    # 3. Append to POSITION-MONITOR.md log
    _append_monitor_log(portfolio_report)

    print(
        f"[monitor_positions] done  run_id={run_id}  "
        f"equity={equity}  drawdown={drawdown:.4%}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
