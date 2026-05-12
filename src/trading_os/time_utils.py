from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def utc_now_iso() -> str:
    return utc_now().replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_iso_utc(value: str) -> Optional[datetime]:
    """Parse an ISO 8601 UTC string; returns None on failure."""
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def iso_age_minutes(value: str) -> Optional[float]:
    """Minutes elapsed since the given ISO 8601 UTC timestamp."""
    dt = parse_iso_utc(value)
    if dt is None:
        return None
    return (utc_now() - dt).total_seconds() / 60.0
