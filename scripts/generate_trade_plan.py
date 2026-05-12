#!/usr/bin/env python3
"""Phase 4 trade plan generator — deterministic, no order submission.

Usage:
    python scripts/generate_trade_plan.py              # dry-run (default)
    python scripts/generate_trade_plan.py --approve-paper

Exit codes:
    0  plan written (including valid no-trade plans)
    1  missing required input files or unrecoverable error

Outputs:
    data/latest/trade_plan.json

Safety:
- Reads only from data/latest/ and config/. Never submits orders.
- Requires TRADING_MODE=paper validation via risk checks.
- Paper approval only set when --approve-paper flag is passed AND all gates pass.
- Never prints secrets.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import (
    LATEST_DIR,
    MEMORY_DIR,
    load_config_file,
)
from trading_os.hashing import stable_hash
from trading_os.planning.trade_plan_builder import build_trade_plan
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


def _load_json(path: Path, label: str) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"{label} not found at {path}")
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as exc:
        raise ValueError(f"Could not parse {label}: {exc}") from exc


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(approve_paper: bool = False) -> int:
    print(f"[generate_trade_plan] starting  approve_paper={approve_paper}")

    # ── Load configs ────────────────────────────────────────────────────────
    try:
        strategy = load_config_file("strategy.json")
        risk_limits = load_config_file("risk_limits.json")
        execution_policy = load_config_file("execution_policy.json")
        sector_map = load_config_file("sector_map.json")
    except Exception as exc:
        print(f"[generate_trade_plan] ERROR loading configs: {exc}", file=sys.stderr)
        return 1

    # ── Load data snapshots ──────────────────────────────────────────────────
    try:
        market_snapshot = _load_json(LATEST_DIR / "market_snapshot.json", "market_snapshot")
        trigger_snapshot = _load_json(LATEST_DIR / "trigger_snapshot.json", "trigger_snapshot")
        account_snapshot = _load_json(LATEST_DIR / "account_snapshot.json", "account_snapshot")
    except FileNotFoundError as exc:
        print(f"[generate_trade_plan] ERROR: {exc}", file=sys.stderr)
        print(
            "[generate_trade_plan] Run refresh_data.py and scan_triggers.py first.",
            file=sys.stderr,
        )
        return 1
    except Exception as exc:
        print(f"[generate_trade_plan] ERROR loading snapshots: {exc}", file=sys.stderr)
        return 1

    # Positions may live in positions_snapshot or account_snapshot
    positions_path = LATEST_DIR / "positions_snapshot.json"
    if positions_path.exists():
        try:
            pos_data = _load_json(positions_path, "positions_snapshot")
            positions = pos_data.get("positions", [])
        except Exception:
            positions = account_snapshot.get("positions", [])
    else:
        positions = account_snapshot.get("positions", [])

    print(f"  market_snapshot  generated_at={market_snapshot.get('generated_at', '?')}")
    print(f"  trigger_snapshot scanned_at={trigger_snapshot.get('scanned_at', '?')}")
    print(f"  account equity={account_snapshot.get('account', {}).get('equity', '?')}")
    print(f"  positions={len(positions)}")

    # ── Build trade plan ─────────────────────────────────────────────────────
    try:
        trade_plan = build_trade_plan(
            market_snapshot=market_snapshot,
            trigger_snapshot=trigger_snapshot,
            account_snapshot=account_snapshot,
            positions=positions,
            strategy=strategy,
            risk_limits=risk_limits,
            execution_policy=execution_policy,
            sector_map=sector_map,
            approve_paper=approve_paper,
        )
    except Exception as exc:
        print(f"[generate_trade_plan] ERROR building plan: {exc}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1

    approval = trade_plan.get("approval", {})
    regime = trade_plan.get("regime") or {}
    print(f"  regime risk_on={regime.get('risk_on')}")
    print(f"  targets={list(trade_plan.get('targets', {}).keys())}")
    print(f"  proposed_orders={len(trade_plan.get('proposed_orders', []))}")
    print(f"  blocked_symbols={len(trade_plan.get('blocked_symbols', []))}")
    gates = trade_plan.get("risk_checks", [])
    failed = [c["check_id"] for c in gates if not c["passes"]]
    print(f"  risk_checks={len(gates)}  failed={failed}")
    print(f"  approved_for_execution={approval.get('approved_for_execution')}")
    if trade_plan.get("no_trade_reasons"):
        print(f"  no_trade_reasons={trade_plan['no_trade_reasons']}")

    # ── Write output ─────────────────────────────────────────────────────────
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    _write_json(LATEST_DIR / "trade_plan.json", trade_plan)

    print("[generate_trade_plan] done")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deterministic trade plan generator")
    parser.add_argument(
        "--approve-paper",
        action="store_true",
        help=(
            "Mark plan as approved_for_execution if all risk gates pass. "
            "Does NOT submit orders — that is Phase 5."
        ),
    )
    args = parser.parse_args()
    sys.exit(main(approve_paper=args.approve_paper))
