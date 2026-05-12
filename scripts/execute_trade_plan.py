#!/usr/bin/env python3
"""
Deprecated script.

This legacy script is intentionally disabled. The only valid execution path is:

    scripts/execute_paper.py

Do not restore this script without a reviewed migration plan.
"""

import sys


def main() -> int:
    print(
        "ERROR: scripts/execute_trade_plan.py is deprecated. "
        "Use scripts/execute_paper.py instead.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
