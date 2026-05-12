#!/usr/bin/env python3
"""
DEPRECATED — use scripts/scan_triggers.py instead.

This script called the legacy autonomous_trading_research_os package
which has been superseded by trading_os. It is intentionally disabled.

Canonical script:
    python scripts/scan_triggers.py
"""
import sys

print(
    "[trigger_scan] DEPRECATED: this script is disabled.\n"
    "Use the canonical script instead:\n"
    "    python scripts/scan_triggers.py",
    file=sys.stderr,
)
sys.exit(1)
