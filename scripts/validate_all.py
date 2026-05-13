#!/usr/bin/env python3
"""Phase 1 validator — fail closed if any required file is missing or schema-invalid.

Usage:
    python scripts/validate_all.py
    python scripts/validate_all.py --execution-check   # fail closed on mock canonical files

Exit codes:
    0  all checks passed (warnings are printed but do not fail)
    1  one or more checks failed
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Allow running from any working directory.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trading_os.config import (
    CONFIG_DIR,
    LATEST_DIR,
    MEMORY_DIR,
    REQUIRED_CONFIG_FILES,
    ConfigError,
    validate_all_configs,
)
from trading_os.schemas import SchemaError
from trading_os.source_integrity import (
    EXECUTION_CRITICAL_FILES,
    get_snapshot_source,
    is_valid_execution_source,
)


def _check_files_present() -> list:
    missing = []
    for name in REQUIRED_CONFIG_FILES:
        if not (CONFIG_DIR / name).exists():
            missing.append(str(CONFIG_DIR / name))
    risk_state_path = MEMORY_DIR / "RISK-STATE.json"
    if not risk_state_path.exists():
        missing.append(str(risk_state_path))
    return missing


def _check_canonical_sources(execution_check: bool) -> list:
    """Check source fields on canonical data/latest files.

    Returns a list of warning/error strings. Empty = all clean.
    """
    issues = []
    for filename in EXECUTION_CRITICAL_FILES:
        path = LATEST_DIR / filename
        if not path.exists():
            issues.append(f"MISSING canonical file: {path.relative_to(Path.cwd()) if path.is_relative_to(Path.cwd()) else path}")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            issues.append(f"PARSE ERROR {filename}: {exc}")
            continue
        source = get_snapshot_source(data)
        if not is_valid_execution_source(source):
            level = "FAIL" if execution_check else "WARN"
            issues.append(
                f"{level} [source_integrity] {filename}: source={source!r} "
                "(not alpaca_paper — run live Data Refresh before paper execution)"
            )
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Phase 1 validator. "
        "Use --execution-check to fail closed on mock canonical files."
    )
    parser.add_argument(
        "--execution-check",
        action="store_true",
        default=False,
        help="Fail (exit 1) if any canonical data/latest file has non-alpaca_paper source.",
    )
    args = parser.parse_args()

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

    # --- Source integrity check on canonical data/latest files ----------------
    source_issues = _check_canonical_sources(execution_check=args.execution_check)
    if source_issues:
        print("\n--- Source integrity check ---")
        for issue in source_issues:
            print(f"  {issue}")
        if args.execution_check and any(i.startswith("FAIL") for i in source_issues):
            print(
                "FAIL: canonical data/latest files contain non-alpaca_paper sources. "
                "Run live Data Refresh before paper execution."
            )
            return 1
        elif any(i.startswith("WARN") for i in source_issues):
            print(
                "NOTE: source integrity warnings above. "
                "Use --execution-check to fail closed on mock canonical files."
            )
    else:
        print("  OK source_integrity: all canonical files are alpaca_paper")

    return 0


if __name__ == "__main__":
    sys.exit(main())
