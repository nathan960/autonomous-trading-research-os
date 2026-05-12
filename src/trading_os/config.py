from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .schemas import (
    SchemaError,
    validate_execution_policy,
    validate_risk_limits,
    validate_risk_state,
    validate_sector_map,
    validate_strategy,
    validate_trigger_registry,
    validate_universe,
)


class ConfigError(RuntimeError):
    """Raised when a required config file is missing, unreadable, or not a JSON object."""


# Resolved at import time; scripts run from any working directory.
_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = _ROOT / "config"
MEMORY_DIR = _ROOT / "memory"
DATA_DIR = _ROOT / "data"
LATEST_DIR = DATA_DIR / "latest"
HISTORY_DIR = DATA_DIR / "history"
SNAPSHOTS_DIR = HISTORY_DIR / "snapshots"

REQUIRED_CONFIG_FILES: tuple = (
    "strategy.json",
    "risk_limits.json",
    "execution_policy.json",
    "universe.json",
    "sector_map.json",
    "trigger_registry.json",
)


def load_config_file(name: str) -> dict:
    path = CONFIG_DIR / name
    if not path.exists():
        raise ConfigError(f"Required config file missing: {path}")
    try:
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as exc:
        raise ConfigError(f"Config file is not valid JSON — {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ConfigError(f"Config file must be a JSON object (got {type(data).__name__}): {path}")
    return data


def load_all_configs() -> dict:
    return {name: load_config_file(name) for name in REQUIRED_CONFIG_FILES}


def load_risk_state() -> dict:
    path = MEMORY_DIR / "RISK-STATE.json"
    if not path.exists():
        raise ConfigError(f"Required state file missing: {path}")
    try:
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as exc:
        raise ConfigError(f"State file is not valid JSON — {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ConfigError(f"State file must be a JSON object (got {type(data).__name__}): {path}")
    return data


def validate_all_configs() -> dict:
    """Load and schema-validate all required config files and memory/RISK-STATE.json.

    Returns the loaded configs dict on success. Raises ConfigError or SchemaError on failure.
    """
    configs = load_all_configs()
    validate_strategy(configs["strategy.json"])
    validate_risk_limits(configs["risk_limits.json"])
    validate_execution_policy(configs["execution_policy.json"])
    validate_universe(configs["universe.json"])
    validate_sector_map(configs["sector_map.json"])
    validate_trigger_registry(configs["trigger_registry.json"])
    risk_state = load_risk_state()
    validate_risk_state(risk_state)
    return configs
