#!/usr/bin/env python3
"""Phase 1 validator — fail closed if any required file is missing or schema-invalid.

Usage:
    python scripts/validate_all.py

Exit codes:
    0  all checks passed
    1  one or more checks failed
"""
from __future__ import annotations

import sys
from pathlib import Path

# Allow running from any working directory.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trading_os.config import (
    CONFIG_DIR,
    MEMORY_DIR,
    REQUIRED_CONFIG_FILES,
    ConfigError,
    validate_all_configs,
)
from trading_os.schemas import SchemaError


def _check_files_present() -> list:
    missing = []
    for name in REQUIRED_CONFIG_FILES:
        if not (CONFIG_DIR / name).exists():
            missing.append(str(CONFIG_DIR / name))
    risk_state_path = MEMORY_DIR / "RISK-STATE.json"
    if not risk_state_path.exists():
        missing.append(str(risk_state_path))
    return missing


def main() -> int:
    print("=== validate_all.py ===")

    missing = _check_files_present()
    if missing:
        for path in missing:
            print(f"MISSING: {path}")
        print(f"FAIL: {len(missing)} required file(s) missing.")
        return 1

    print(f"Files present: {len(REQUIRED_CONFIG_FILES)} config + RISK-STATE.json")

    try:
        configs = validate_all_configs()
    except ConfigError as exc:
        print(f"FAIL [config]: {exc}")
        return 1
    except SchemaError as exc:
        print(f"FAIL [schema/{exc.context}]:")
        for err in exc.errors:
            print(f"  - {err}")
        return 1
    except Exception as exc:
        print(f"FAIL [unexpected {type(exc).__name__}]: {exc}")
        return 1

    for name in sorted(configs):
        print(f"  OK {name}")
    print("  OK memory/RISK-STATE.json")
    print(f"PASS: all {len(configs)} config files and risk state validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
