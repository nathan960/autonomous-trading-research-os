#!/usr/bin/env python3
"""
DEPRECATED — use the canonical pipeline scripts instead.

This script ran the full legacy autonomous_trading_research_os pipeline
which has been superseded by trading_os. It is intentionally disabled.

Canonical dry-run pipeline:
    python scripts/refresh_data.py
    python scripts/monitor_positions.py
    python scripts/scan_triggers.py
    python scripts/generate_trade_plan.py
    python scripts/dry_run_execute.py
"""
import sys

print(
    "[run_all_dry_run] DEPRECATED: this script is disabled.\n"
    "Run the canonical pipeline instead:\n"
    "    python scripts/refresh_data.py\n"
    "    python scripts/monitor_positions.py\n"
    "    python scripts/scan_triggers.py\n"
    "    python scripts/generate_trade_plan.py\n"
    "    python scripts/dry_run_execute.py",
    file=sys.stderr,
)
sys.exit(1)
