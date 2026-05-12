from __future__ import annotations

import json
from pathlib import Path

import pytest

import trading_os.config as cfg_module
from trading_os.config import (
    CONFIG_DIR,
    REQUIRED_CONFIG_FILES,
    ConfigError,
    load_all_configs,
    load_config_file,
    load_risk_state,
    validate_all_configs,
)
from trading_os.hashing import stable_hash, hash_file, hash_json_file
from trading_os.time_utils import utc_now_iso, parse_iso_utc, iso_age_minutes


# ---------------------------------------------------------------------------
# Required files present
# ---------------------------------------------------------------------------

class TestRequiredFilesPresent:
    def test_all_config_files_exist(self) -> None:
        for name in REQUIRED_CONFIG_FILES:
            path = CONFIG_DIR / name
            assert path.exists(), f"Required config file missing: {name}"

    def test_risk_state_exists(self) -> None:
        from trading_os.config import MEMORY_DIR
        assert (MEMORY_DIR / "RISK-STATE.json").exists()


# ---------------------------------------------------------------------------
# load_config_file
# ---------------------------------------------------------------------------

class TestLoadConfigFile:
    def test_loads_strategy(self) -> None:
        d = load_config_file("strategy.json")
        assert isinstance(d, dict)
        assert d.get("strategy_id")

    def test_loads_risk_limits(self) -> None:
        d = load_config_file("risk_limits.json")
        assert d.get("paper_only") is True
        assert d.get("live_trading_allowed") is False

    def test_loads_execution_policy(self) -> None:
        d = load_config_file("execution_policy.json")
        assert d.get("paper_only") is True
        assert d.get("allow_shorting") is False

    def test_loads_universe(self) -> None:
        d = load_config_file("universe.json")
        assert isinstance(d.get("symbols"), list)
        assert len(d["symbols"]) > 0

    def test_loads_sector_map(self) -> None:
        d = load_config_file("sector_map.json")
        assert isinstance(d, dict)
        assert len(d) > 0

    def test_loads_trigger_registry(self) -> None:
        d = load_config_file("trigger_registry.json")
        assert isinstance(d.get("triggers"), list)

    def test_missing_file_raises_config_error(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(cfg_module, "CONFIG_DIR", tmp_path)
        with pytest.raises(ConfigError, match="missing"):
            load_config_file("nonexistent.json")

    def test_invalid_json_raises_config_error(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        bad = tmp_path / "bad.json"
        bad.write_text("{not valid json", encoding="utf-8")
        monkeypatch.setattr(cfg_module, "CONFIG_DIR", tmp_path)
        with pytest.raises(ConfigError, match="valid JSON"):
            load_config_file("bad.json")

    def test_json_array_raises_config_error(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        arr = tmp_path / "arr.json"
        arr.write_text("[1, 2, 3]", encoding="utf-8")
        monkeypatch.setattr(cfg_module, "CONFIG_DIR", tmp_path)
        with pytest.raises(ConfigError, match="JSON object"):
            load_config_file("arr.json")


# ---------------------------------------------------------------------------
# load_all_configs
# ---------------------------------------------------------------------------

class TestLoadAllConfigs:
    def test_returns_all_required_keys(self) -> None:
        configs = load_all_configs()
        for name in REQUIRED_CONFIG_FILES:
            assert name in configs

    def test_all_values_are_dicts(self) -> None:
        configs = load_all_configs()
        for name, data in configs.items():
            assert isinstance(data, dict), f"{name} should be a dict"

    def test_strategy_paper_only(self) -> None:
        configs = load_all_configs()
        assert configs["strategy.json"]["trading_mode"] == "paper_only"

    def test_risk_limits_no_live_trading(self) -> None:
        configs = load_all_configs()
        assert configs["risk_limits.json"]["live_trading_allowed"] is False


# ---------------------------------------------------------------------------
# validate_all_configs (integration — hits real files)
# ---------------------------------------------------------------------------

class TestValidateAllConfigs:
    def test_passes_with_real_files(self) -> None:
        configs = validate_all_configs()
        assert isinstance(configs, dict)
        assert len(configs) == len(REQUIRED_CONFIG_FILES)

    def test_strategy_is_paper_only(self) -> None:
        configs = validate_all_configs()
        assert configs["strategy.json"]["trading_mode"] == "paper_only"

    def test_missing_config_fails(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(cfg_module, "CONFIG_DIR", tmp_path)
        with pytest.raises(ConfigError):
            validate_all_configs()


# ---------------------------------------------------------------------------
# load_risk_state
# ---------------------------------------------------------------------------

class TestLoadRiskState:
    def test_loads_successfully(self) -> None:
        state = load_risk_state()
        assert isinstance(state, dict)
        assert state.get("schema_version")
        assert isinstance(state.get("latest_equity"), (int, float))
        assert state["latest_equity"] > 0

    def test_missing_risk_state_raises(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(cfg_module, "MEMORY_DIR", tmp_path)
        with pytest.raises(ConfigError, match="missing"):
            load_risk_state()


# ---------------------------------------------------------------------------
# Hashing utilities
# ---------------------------------------------------------------------------

class TestHashing:
    def test_stable_hash_is_deterministic(self) -> None:
        obj = {"b": 2, "a": 1}
        assert stable_hash(obj) == stable_hash(obj)

    def test_stable_hash_is_key_order_independent(self) -> None:
        assert stable_hash({"a": 1, "b": 2}) == stable_hash({"b": 2, "a": 1})

    def test_stable_hash_is_64_hex_chars(self) -> None:
        h = stable_hash({"x": 1})
        assert len(h) == 64
        assert all(c in "0123456789abcdef" for c in h)

    def test_different_objects_different_hashes(self) -> None:
        assert stable_hash({"a": 1}) != stable_hash({"a": 2})

    def test_hash_file(self, tmp_path: Path) -> None:
        f = tmp_path / "test.bin"
        f.write_bytes(b"hello")
        h = hash_file(f)
        assert len(h) == 64

    def test_hash_json_file_canonical(self, tmp_path: Path) -> None:
        f1 = tmp_path / "a.json"
        f2 = tmp_path / "b.json"
        f1.write_text('{"b":2,"a":1}', encoding="utf-8")
        f2.write_text('{"a":1,"b":2}', encoding="utf-8")
        assert hash_json_file(f1) == hash_json_file(f2)

    def test_hash_real_strategy_file(self) -> None:
        path = CONFIG_DIR / "strategy.json"
        h = hash_json_file(path)
        assert len(h) == 64


# ---------------------------------------------------------------------------
# Time utilities
# ---------------------------------------------------------------------------

class TestTimeUtils:
    def test_utc_now_iso_format(self) -> None:
        ts = utc_now_iso()
        assert ts.endswith("Z")
        assert "T" in ts

    def test_parse_iso_utc_roundtrip(self) -> None:
        ts = utc_now_iso()
        dt = parse_iso_utc(ts)
        assert dt is not None
        assert dt.tzinfo is not None

    def test_parse_iso_utc_invalid_returns_none(self) -> None:
        assert parse_iso_utc("not-a-date") is None
        assert parse_iso_utc("") is None

    def test_iso_age_minutes_recent(self) -> None:
        ts = utc_now_iso()
        age = iso_age_minutes(ts)
        assert age is not None
        assert 0.0 <= age < 1.0

    def test_iso_age_minutes_invalid_returns_none(self) -> None:
        assert iso_age_minutes("garbage") is None
