"""Sector-cap selection: apply per-sector name limits to ranked candidates.

Not a blocking trigger on its own — applied after per-symbol triggers to select
the final portfolio from the ranked candidate list. Symbols excluded only due to
sector caps are recorded so the audit trail is complete.
"""
from __future__ import annotations

from typing import Any


def apply_sector_caps(
    ranked_candidates: list,
    sector_map: dict,
    max_names_per_sector: int = 2,
    max_holdings: int = 10,
) -> tuple:
    """Select up to max_holdings candidates respecting sector concentration limits.

    Returns:
        selected:              candidates that made the cut
        sector_counts:         {sector_code_str: count} for the selected set
        excluded_by_cap:       candidates skipped due to sector cap (each has skip_reason)
    """
    selected: list = []
    excluded_by_cap: list = []
    sector_counts: dict[str, int] = {}

    for candidate in ranked_candidates:
        if len(selected) >= max_holdings:
            excluded_by_cap.append({**candidate, "skip_reason": "max_holdings_reached"})
            continue

        symbol = candidate.get("symbol", "")
        sector_info = sector_map.get(symbol, {})
        sector_code = str(sector_info.get("sector_code") or "UNKNOWN")

        current = sector_counts.get(sector_code, 0)
        if current >= max_names_per_sector:
            excluded_by_cap.append(
                {
                    **candidate,
                    "skip_reason": (
                        f"sector_cap(sector_code={sector_code},"
                        f"count={current},max={max_names_per_sector})"
                    ),
                }
            )
            continue

        selected.append(candidate)
        sector_counts[sector_code] = current + 1

    return selected, sector_counts, excluded_by_cap
