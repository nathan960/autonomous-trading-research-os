#!/usr/bin/env python3
"""
DEPRECATED — use scripts/monitor_positions.py instead.

This script called the legacy autonomous_trading_research_os package
which has been superseded by trading_os. It is intentionally disabled.

Canonical script:
    python scripts/monitor_positions.py [--dry-run]
"""
import sys

print(
    "[position_monitor] DEPRECATED: this script is disabled.\n"
    "Use the canonical script instead:\n"
    "    python scripts/monitor_positions.py [--dry-run]",
    file=sys.stderr,
)
sys.exit(1)
