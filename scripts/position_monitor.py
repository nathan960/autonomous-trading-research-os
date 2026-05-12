#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from autonomous_trading_research_os.position_monitor import run_position_monitor


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--alpaca', action='store_true', help='Use Alpaca for live paper account reconciliation.')
    args = parser.parse_args()
    result = run_position_monitor(use_alpaca=args.alpaca)
    print(json.dumps({
        "run_id": result.get("run_id"),
        "status": result.get("status") or result.get("approval", {}).get("status"),
        "generated_at": result.get("generated_at"),
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
