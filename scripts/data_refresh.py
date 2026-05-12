#!/usr/bin/env python3
"""
DEPRECATED — use scripts/refresh_data.py instead.

This script called the legacy autonomous_trading_research_os package
which has been superseded by trading_os. It is intentionally disabled.

Canonical script:
    python scripts/refresh_data.py
"""
import sys

print(
    "[data_refresh] DEPRECATED: this script is disabled.\n"
    "Use the canonical script instead:\n"
    "    python scripts/refresh_data.py",
    file=sys.stderr,
)
sys.exit(1)
