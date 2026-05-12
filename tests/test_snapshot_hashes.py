"""Tests: data_hash present and valid in all three snapshot files.

Covers:
- positions_snapshot.json contains data_hash.
- orders_snapshot.json contains data_hash.
- market_snapshot.json contains data_hash.
- Each data_hash is a 64-char hex string.
- data_hash verifies correctly against snapshot content (stable_hash).
- If the snapshot is mutated the stored hash no longer matches.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.hashing import stable_hash


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_valid_sha256(value: object) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(
        c in "0123456789abcdef" for c in value
    )


def _verify_data_hash(snapshot: dict, exclude_key: str = "data_hash") -> bool:
    """Return True if the stored data_hash matches the canonical hash of the rest."""
    stored = snapshot.get(exclude_key)
    if not stored:
        return False
    body = {k: v for k, v in snapshot.items() if k != exclude_key}
    return stable_hash(body) == stored


# ---------------------------------------------------------------------------
# Unit tests: logic for adding data_hash to payloads
# ---------------------------------------------------------------------------

class TestDataHashLogic:
    def test_hash_is_sha256_hex(self):
        payload = {"schema_version": "0.1.0", "positions": [], "fetched_at": "2026-05-12T00:00:00Z"}
        h = stable_hash(payload)
        assert _is_valid_sha256(h)

    def test_hash_changes_when_content_changes(self):
        p1 = {"positions": [], "fetched_at": "2026-05-12T00:00:00Z"}
        p2 = {"positions": [{"symbol": "AAPL"}], "fetched_at": "2026-05-12T00:00:00Z"}
        assert stable_hash(p1) != stable_hash(p2)

    def test_hash_stable_across_key_ordering(self):
        p1 = {"a": 1, "b": 2}
        p2 = {"b": 2, "a": 1}
        assert stable_hash(p1) == stable_hash(p2)

    def test_positions_snapshot_hash_pattern(self):
        payload: dict = {
            "schema_version": "0.1.0",
            "source": "alpaca_paper",
            "fetched_at": "2026-05-12T00:00:00Z",
            "positions": [{"symbol": "AAPL", "market_value": "1000.0"}],
            "position_count": 1,
        }
        payload["data_hash"] = stable_hash(payload)
        assert _is_valid_sha256(payload["data_hash"])
        assert _verify_data_hash(payload)

    def test_orders_snapshot_hash_pattern(self):
        payload: dict = {
            "schema_version": "0.1.0",
            "source": "alpaca_paper",
            "fetched_at": "2026-05-12T00:00:00Z",
            "orders": [],
            "open_order_count": 0,
        }
        payload["data_hash"] = stable_hash(payload)
        assert _verify_data_hash(payload)

    def test_market_snapshot_hash_pattern(self):
        payload: dict = {
            "schema_version": "0.1.0",
            "run_mode": "dry_run",
            "generated_at": "2026-05-12T00:00:00Z",
            "bars": {},
            "quotes": {},
        }
        # Exclude data_hash key when computing (same pattern as refresh_data.py)
        payload["data_hash"] = stable_hash({k: v for k, v in payload.items() if k != "data_hash"})
        assert _verify_data_hash(payload)

    def test_mutated_snapshot_fails_hash_check(self):
        payload: dict = {
            "schema_version": "0.1.0",
            "positions": [],
            "position_count": 0,
        }
        payload["data_hash"] = stable_hash(payload)
        # Mutate
        payload["position_count"] = 99
        assert not _verify_data_hash(payload), "Mutated snapshot should not pass hash check"

    def test_missing_hash_key_fails_check(self):
        payload = {"schema_version": "0.1.0", "positions": []}
        assert not _verify_data_hash(payload)


# ---------------------------------------------------------------------------
# Integration: run refresh_data.py --dry-run and check output snapshots
# ---------------------------------------------------------------------------

class TestRefreshDataSnapshotHashes:
    """Run refresh_data.py --dry-run and verify data_hash in written snapshot files."""

    @pytest.fixture(scope="class")
    def _run_refresh(self):
        result = subprocess.run(
            [sys.executable, str(_ROOT / "scripts" / "refresh_data.py"), "--dry-run"],
            capture_output=True,
            text=True,
            cwd=str(_ROOT),
        )
        return result

    def test_refresh_exits_zero(self, _run_refresh):
        assert _run_refresh.returncode == 0, (
            f"refresh_data.py --dry-run failed:\n{_run_refresh.stdout}\n{_run_refresh.stderr}"
        )

    def _load(self, name: str) -> dict:
        path = _ROOT / "data" / "latest" / name
        assert path.exists(), f"{name} not found at {path}"
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)

    def test_positions_snapshot_has_data_hash(self, _run_refresh):
        snap = self._load("positions_snapshot.json")
        assert "data_hash" in snap, "positions_snapshot.json missing data_hash"
        assert _is_valid_sha256(snap["data_hash"]), f"Invalid hash: {snap['data_hash']}"

    def test_positions_snapshot_hash_verifies(self, _run_refresh):
        snap = self._load("positions_snapshot.json")
        assert _verify_data_hash(snap), "positions_snapshot.json data_hash mismatch"

    def test_orders_snapshot_has_data_hash(self, _run_refresh):
        snap = self._load("orders_snapshot.json")
        assert "data_hash" in snap, "orders_snapshot.json missing data_hash"
        assert _is_valid_sha256(snap["data_hash"]), f"Invalid hash: {snap['data_hash']}"

    def test_orders_snapshot_hash_verifies(self, _run_refresh):
        snap = self._load("orders_snapshot.json")
        assert _verify_data_hash(snap), "orders_snapshot.json data_hash mismatch"

    def test_market_snapshot_has_data_hash(self, _run_refresh):
        snap = self._load("market_snapshot.json")
        assert "data_hash" in snap, "market_snapshot.json missing data_hash"
        assert _is_valid_sha256(snap["data_hash"]), f"Invalid hash: {snap['data_hash']}"

    def test_market_snapshot_hash_verifies(self, _run_refresh):
        snap = self._load("market_snapshot.json")
        assert _verify_data_hash(snap), "market_snapshot.json data_hash mismatch"

    def test_all_three_hashes_are_distinct(self, _run_refresh):
        pos = self._load("positions_snapshot.json")["data_hash"]
        ord_ = self._load("orders_snapshot.json")["data_hash"]
        mkt = self._load("market_snapshot.json")["data_hash"]
        assert len({pos, ord_, mkt}) == 3, "All three snapshot hashes should be distinct"
