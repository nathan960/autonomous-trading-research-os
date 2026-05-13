#!/usr/bin/env python3
"""Diagnose spread gate failures — research only, no execution path.

Classifies every spread failure in the latest market snapshot as:
  off_hours_quote, zero_bid_or_ask, stale_quote, data_feed_limitation,
  wide_spread_real, missing_bid/ask, or pass.

Usage:
    python scripts/diagnose_spreads.py
    python scripts/diagnose_spreads.py --dry-run   # print, do not write files

Exit codes:
    0  diagnostics written (or dry-run completed)
    1  error

Outputs:
    data/latest/spread_diagnostics.json               (replaced each run)
    data/history/data_quality/spread_diagnostics/     (timestamped archive)
    memory/DATA-QUALITY-LOG.md                        (appended)

Safety:
    ENABLE_PAPER_EXECUTION is never read.
    No Alpaca API calls. No order submission. No risk config changes.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import CONFIG_DIR, HISTORY_DIR, LATEST_DIR, MEMORY_DIR
from trading_os.research.spread_diagnostics import (
    FC_PASS,
    build_spread_diagnostics,
    write_spread_diagnostics,
)


def _load_json(path: Path, default=None):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Diagnose spread gate failures. Research only — no execution path.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Build and print diagnostics without writing any files.",
    )
    args = parser.parse_args()

    print(
        "[diagnose_spreads] starting  "
        "(ENABLE_PAPER_EXECUTION is not read — execution impossible from this path)"
    )

    market_snapshot = _load_json(LATEST_DIR / "market_snapshot.json", {})
    data_quality_snapshot = _load_json(LATEST_DIR / "data_quality_snapshot.json", {})
    risk_limits = _load_json(CONFIG_DIR / "risk_limits.json", {})
    sector_map = _load_json(CONFIG_DIR / "sector_map.json", {})

    if not market_snapshot:
        print("[diagnose_spreads] ERROR: market_snapshot.json not found or empty", file=sys.stderr)
        return 1
    if not risk_limits:
        print("[diagnose_spreads] ERROR: risk_limits.json not found or empty", file=sys.stderr)
        return 1

    feed = market_snapshot.get("data_feed") or data_quality_snapshot.get("data_feed") or "unknown"
    clock = market_snapshot.get("clock") or {}
    print(f"  market_snapshot: {market_snapshot.get('generated_at')}  feed={feed}  "
          f"is_open={clock.get('is_open')}")

    try:
        snapshot = build_spread_diagnostics(
            market_snapshot=market_snapshot,
            data_quality_snapshot=data_quality_snapshot,
            risk_limits=risk_limits,
            sector_map=sector_map,
        )
    except Exception as exc:
        print(f"[diagnose_spreads] ERROR building diagnostics: {exc}", file=sys.stderr)
        return 1

    s = snapshot.get("summary") or {}
    by_class = s.get("by_failure_class") or {}

    summary_print = {
        "run_id": snapshot.get("run_id"),
        "generated_at": snapshot.get("generated_at"),
        "market_is_open": snapshot.get("market_is_open"),
        "data_feed": snapshot.get("data_feed"),
        "max_spread_pct": snapshot.get("max_spread_pct"),
        "total_symbols": s.get("total_symbols"),
        "pass_count": s.get("pass_count"),
        "fail_count": s.get("fail_count"),
        "block_rate": s.get("block_rate"),
        "by_failure_class": {k: v for k, v in by_class.items() if v > 0},
    }

    if args.dry_run:
        print("[diagnose_spreads] DRY RUN — not writing files.")
        print(json.dumps(summary_print, indent=2))
        print("\nFindings:")
        for f in snapshot.get("findings") or []:
            print(f"  - {f}")
        print("\nRecommendations:")
        for r in snapshot.get("recommendations") or []:
            print(f"  [{r.get('priority').upper()}] {r.get('action')}: {r.get('detail')}")
        print("\nPer-symbol (failing only):")
        for rec in snapshot.get("symbols") or []:
            if rec.get("failure_class") != FC_PASS:
                print(
                    f"  {rec['symbol']:6s} {rec['sector']:<20s} "
                    f"spread_pct={rec.get('spread_pct') or 'null':>8}  "
                    f"age={rec.get('quote_age_minutes') or 'n/a':>6}m  "
                    f"class={rec['failure_class']}"
                )
        return 0

    try:
        paths = write_spread_diagnostics(
            snapshot,
            latest_dir=LATEST_DIR,
            history_dir=HISTORY_DIR / "data_quality" / "spread_diagnostics",
            memory_dir=MEMORY_DIR,
        )
    except Exception as exc:
        print(f"[diagnose_spreads] ERROR writing: {exc}", file=sys.stderr)
        return 1

    print("[diagnose_spreads] done")
    print(f"  latest_path:   {paths['latest_path']}")
    print(f"  history_path:  {paths['history_path']}")
    print(f"  dq_log:        {paths['dq_log_path']}")
    print(json.dumps(summary_print, indent=2))

    print("\nFindings:")
    for f in snapshot.get("findings") or []:
        print(f"  - {f}")

    print("\nRecommendations:")
    for r in snapshot.get("recommendations") or []:
        print(f"  [{r.get('priority').upper()}] {r.get('action')}")
        print(f"    {r.get('detail')}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
