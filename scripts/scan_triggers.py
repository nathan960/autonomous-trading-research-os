#!/usr/bin/env python3
"""Phase 3 trigger scanner — evaluate all signal triggers against latest market data.

Usage:
    python scripts/scan_triggers.py            # normal run
    python scripts/scan_triggers.py --dry-run  # accept a stale/missing snapshot (test mode)

Exit codes:
    0  trigger snapshot written successfully
    1  missing data, gate failure, or write error

Outputs:
    data/latest/trigger_snapshot.json          (latest canonical snapshot)
    data/history/triggers/YYYY-MM-DD.jsonl     (one JSONL line per run)
    memory/TRIGGER-LOG.md                      (regime + summary append)
    memory/SIGNAL-LOG.md                       (candidates list append)

Safety:
- Reads only. No orders. No trade plan mutation.
- Fails closed on missing required files.
- Never logs secrets.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import (
    HISTORY_DIR,
    LATEST_DIR,
    MEMORY_DIR,
    load_config_file,
)
from trading_os.hashing import stable_hash
from trading_os.signals.trigger_engine import run_trigger_scan
from trading_os.time_utils import utc_now_iso

_TRIGGERS_HISTORY_DIR = HISTORY_DIR / "triggers"


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True, default=str)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(path)
    print(f"  wrote {path.relative_to(_ROOT)}")


def _append_jsonl(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(record, sort_keys=True, default=str) + "\n"
    with path.open("a", encoding="utf-8") as fh:
        fh.write(line)
    print(f"  appended {path.relative_to(_ROOT)}")


def _append_trigger_log(snapshot: dict) -> None:
    log_path = MEMORY_DIR / "TRIGGER-LOG.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    if existing and not existing.endswith("\n"):
        existing += "\n"

    regime = snapshot.get("regime") or {}
    stale = snapshot.get("data_stale_gate") or {}
    breadth = (regime.get("breadth") or {})
    spy_sig = (regime.get("spy_signals") or {})
    selected = snapshot.get("selected", [])
    candidates = snapshot.get("candidates", [])
    excluded = snapshot.get("excluded", [])

    summary = {
        "scanned_at": snapshot.get("scanned_at"),
        "data_stale_gate_passes": stale.get("passes"),
        "snapshot_age_minutes": stale.get("age_minutes"),
        "regime_risk_on": regime.get("risk_on"),
        "regime_skip_reason": regime.get("skip_reason"),
        "spy_passes_200dma": spy_sig.get("passes_200dma"),
        "spy_passes_6m_momentum": spy_sig.get("passes_6m_momentum"),
        "breadth": breadth.get("breadth"),
        "breadth_ok": breadth.get("breadth_ok"),
        "candidates_count": len(candidates),
        "selected_count": len(selected),
        "selected": selected,
        "excluded_count": len(excluded),
        "trigger_snapshot_hash": snapshot.get("trigger_snapshot_hash"),
    }
    block = (
        "\n## scan_triggers run\n\n"
        "```json\n"
        + json.dumps(summary, indent=2, sort_keys=True, default=str)
        + "\n```\n"
    )
    log_path.write_text(existing + block, encoding="utf-8")
    print(f"  appended {log_path.relative_to(_ROOT)}")


def _append_signal_log(snapshot: dict) -> None:
    log_path = MEMORY_DIR / "SIGNAL-LOG.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    if existing and not existing.endswith("\n"):
        existing += "\n"

    scanned_at = snapshot.get("scanned_at", "")
    candidates = snapshot.get("candidates", [])
    selected = snapshot.get("selected", [])
    symbol_results = snapshot.get("symbol_results", {})

    rows: list[str] = []
    for sym in candidates:
        res = symbol_results.get(sym, {})
        mom = res.get("momentum", {})
        atr = res.get("atr", {})
        score = mom.get("momentum_score")
        atr_pct = atr.get("atr_pct")
        mark = "SELECTED" if sym in selected else "candidate"
        score_str = f"{score:.4f}" if score is not None else "n/a"
        atr_str = f"{atr_pct:.4f}" if atr_pct is not None else "n/a"
        rows.append(f"  {sym:8s}  score={score_str}  atr_pct={atr_str}  [{mark}]")

    candidate_block = "\n".join(rows) if rows else "  (none)"
    block = (
        f"\n## scan_triggers candidates  ({scanned_at})\n\n"
        f"```\n{candidate_block}\n```\n"
    )
    log_path.write_text(existing + block, encoding="utf-8")
    print(f"  appended {log_path.relative_to(_ROOT)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(dry_run: bool = False) -> int:
    print(f"[scan_triggers] starting  dry_run={dry_run}")

    # ── Load required config files ──────────────────────────────────────────
    try:
        strategy = load_config_file("strategy.json")
        universe = load_config_file("universe.json")
        sector_map = load_config_file("sector_map.json")
    except Exception as exc:
        print(f"[scan_triggers] ERROR loading config: {exc}", file=sys.stderr)
        return 1

    # ── Load market snapshot ────────────────────────────────────────────────
    snapshot_path = LATEST_DIR / "market_snapshot.json"
    if not snapshot_path.exists():
        print(
            f"[scan_triggers] ERROR market_snapshot.json not found at {snapshot_path}",
            file=sys.stderr,
        )
        print(
            "[scan_triggers] Run scripts/refresh_data.py first (or --dry-run for testing).",
            file=sys.stderr,
        )
        return 1

    try:
        market_snapshot: dict = json.loads(snapshot_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"[scan_triggers] ERROR reading market_snapshot.json: {exc}", file=sys.stderr)
        return 1

    print(f"  loaded market_snapshot  generated_at={market_snapshot.get('generated_at', '?')}")

    # ── Run trigger scan ────────────────────────────────────────────────────
    try:
        trigger_snapshot = run_trigger_scan(
            market_snapshot=market_snapshot,
            strategy=strategy,
            universe=universe,
            sector_map=sector_map,
        )
    except Exception as exc:
        print(f"[scan_triggers] ERROR in trigger scan: {exc}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1

    stale_gate = trigger_snapshot.get("data_stale_gate") or {}
    if not dry_run and not stale_gate.get("passes", True):
        print(
            f"[scan_triggers] FAIL data stale gate: {stale_gate.get('skip_reason')}",
            file=sys.stderr,
        )
        return 1

    # ── Print summary ───────────────────────────────────────────────────────
    regime = trigger_snapshot.get("regime") or {}
    selected = trigger_snapshot.get("selected", [])
    candidates = trigger_snapshot.get("candidates", [])
    excluded = trigger_snapshot.get("excluded", [])
    print(f"  regime risk_on={regime.get('risk_on')}  skip={regime.get('skip_reason')}")
    print(f"  candidates={len(candidates)}  selected={len(selected)}  excluded={len(excluded)}")
    if selected:
        print(f"  selected: {selected}")

    # ── Write outputs ───────────────────────────────────────────────────────
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    _write_json(LATEST_DIR / "trigger_snapshot.json", trigger_snapshot)

    # Archive full snapshot by hash so lineage can recover rich trigger data
    snap_hash = trigger_snapshot.get("trigger_snapshot_hash")
    if snap_hash:
        _write_json(
            HISTORY_DIR / "trigger_snapshots" / f"{snap_hash}.json",
            trigger_snapshot,
        )

    scanned_at = trigger_snapshot.get("scanned_at", utc_now_iso())
    date_str = scanned_at[:10]
    _TRIGGERS_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    history_path = _TRIGGERS_HISTORY_DIR / f"{date_str}.jsonl"
    _append_jsonl(
        history_path,
        {
            "scanned_at": scanned_at,
            "risk_on": regime.get("risk_on"),
            "regime_skip_reason": regime.get("skip_reason"),
            "candidates": candidates,
            "selected": selected,
            "excluded_count": len(excluded),
            "trigger_snapshot_hash": trigger_snapshot.get("trigger_snapshot_hash"),
        },
    )

    _append_trigger_log(trigger_snapshot)
    _append_signal_log(trigger_snapshot)

    print("[scan_triggers] done")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deterministic trigger scanner")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Skip stale-data gate failure (use with existing snapshot for testing)",
    )
    args = parser.parse_args()
    sys.exit(main(dry_run=args.dry_run))
