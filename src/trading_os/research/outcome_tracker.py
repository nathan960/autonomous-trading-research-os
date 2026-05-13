"""Research-only trade outcome tracker for Autonomous Trading Research OS.

Reads filled order data from order monitor reports and positions/market snapshots,
builds outcome records per filled order, and tracks paper trade performance over time.

SAFETY:
  - No execution path.
  - Never calls execute_paper.py.
  - Never approves trade plans.
  - Never places, cancels, or replaces orders.
  - Never modifies config/strategy.json or risk_limits.json.
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any, Optional

from ..config import HISTORY_DIR, LATEST_DIR, MEMORY_DIR
from ..hashing import stable_hash
from ..source_integrity import get_snapshot_source, is_mock_source
from ..time_utils import parse_iso_utc, utc_now_iso


# ---------------------------------------------------------------------------
# Outcome window definitions
# Threshold: calendar-day approximation of each trading-day window.
# same_day uses date comparison instead of elapsed seconds.
# ---------------------------------------------------------------------------

OUTCOME_WINDOWS: list = [
    ("same_day", None),           # elapsed once checked_at date > filled_at date
    ("1_trading_day", 1.3),       # ~1 calendar day
    ("5_trading_days", 7.0),      # ~1 calendar week
    ("20_trading_days", 28.0),    # ~4 calendar weeks
    ("63_trading_days", 91.0),    # ~3 calendar months
]


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _load_json(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _find_history_files(directory: Path, glob: str) -> list:
    if not directory.is_dir():
        return []
    return sorted(directory.glob(glob))


def _write_json_atomic(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True, default=str)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(path)


def _safe_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _get_position(symbol: str, positions: list) -> Optional[dict]:
    for p in positions:
        if isinstance(p, dict) and p.get("symbol") == symbol:
            return p
    return None


def _get_current_price(symbol: str, market_snapshot: dict) -> Optional[float]:
    """Return the latest bar close price, falling back to quote mid-price."""
    bars = market_snapshot.get("latest_bars", {})
    bar = bars.get(symbol)
    if bar and bar.get("close") is not None:
        return _safe_float(bar["close"])
    quotes = market_snapshot.get("quotes", {})
    q = quotes.get(symbol)
    if q:
        bid = _safe_float(q.get("bid_price"))
        ask = _safe_float(q.get("ask_price"))
        if bid is not None and ask is not None:
            return round((bid + ask) / 2.0, 4)
    return None


def _compute_slippage(
    fill_price: Optional[float],
    limit_price: Optional[float],
) -> tuple:
    """Return (slippage_vs_limit, slippage_pct). Negative = filled below limit (good for buy)."""
    if fill_price is None or limit_price is None or limit_price == 0:
        return None, None
    slippage = fill_price - limit_price
    slippage_pct = slippage / limit_price
    return round(slippage, 6), round(slippage_pct, 6)


def _compute_outcome_windows(filled_at_str: str, checked_at_str: str) -> dict:
    """Return {window_name: {"status": "elapsed"|"pending"}} for each defined window."""
    filled_at = parse_iso_utc(filled_at_str)
    checked_at = parse_iso_utc(checked_at_str)
    if not filled_at or not checked_at:
        return {name: {"status": "pending"} for name, _ in OUTCOME_WINDOWS}

    elapsed_days = (checked_at - filled_at).total_seconds() / 86400.0
    result = {}
    for name, threshold in OUTCOME_WINDOWS:
        if name == "same_day":
            elapsed = checked_at.date() > filled_at.date()
        else:
            elapsed = threshold is not None and elapsed_days >= threshold
        result[name] = {"status": "elapsed" if elapsed else "pending"}
    return result


# ---------------------------------------------------------------------------
# Build a single outcome record
# ---------------------------------------------------------------------------

def build_outcome_record(
    lifecycle: dict,
    positions: list,
    market_snapshot: dict,
    checked_at: str,
    first_seen_at: Optional[str] = None,
    positions_integrity_blocked: bool = False,
    market_integrity_blocked: bool = False,
    lineage_record: Optional[dict] = None,
) -> dict:
    """Build an outcome record from one filled lifecycle entry.

    Args:
        lifecycle:      One entry from order_monitor_report["lifecycles"].
        positions:      Position list from positions_snapshot["positions"].
        market_snapshot: Full market_snapshot dict for current prices.
        checked_at:     ISO timestamp for this run.
        first_seen_at:  Preserved from an earlier record (not overwritten on update).
        positions_integrity_blocked: True if positions_snapshot source is mock/invalid.
        market_integrity_blocked:    True if market_snapshot source is mock/invalid.
        lineage_record: Optional matching record from lineage_snapshot.json. When
                        present, populates trigger_snapshot_hash, trigger_ids,
                        lineage_status, candidate_rank, and momentum_score.

    Returns an outcome dict. Never submits anything.
    """
    fill = lifecycle.get("fill") or {}
    symbol: str = lifecycle.get("symbol", "")
    side: str = lifecycle.get("side", "")

    fill_price = _safe_float(fill.get("fill_price"))
    limit_price = _safe_float(lifecycle.get("limit_price"))
    filled_qty = _safe_float(fill.get("filled_qty"))
    filled_notional = _safe_float(fill.get("filled_notional"))
    filled_at: str = fill.get("filled_at") or lifecycle.get("submitted_at") or ""

    slippage, slippage_pct = _compute_slippage(fill_price, limit_price)

    # Source integrity check — block position/market-derived values from mock snapshots
    integrity_blocked = positions_integrity_blocked or market_integrity_blocked
    if integrity_blocked:
        source_integrity_status = "blocked_stale_or_mock_position_snapshot"
        current_position_qty = None
        current_market_value = None
        current_unrealized_pl = None
        current_unrealized_pl_pct = None
        current_price = None
        current_return_pct = None
        spy_price = None
        bil_price = None
    else:
        source_integrity_status = "ok"
        # Current position data
        pos = _get_position(symbol, positions)
        market_price = _get_current_price(symbol, market_snapshot)

        if pos:
            current_position_qty = _safe_float(pos.get("qty"))
            current_market_value = _safe_float(pos.get("market_value"))
            current_unrealized_pl = _safe_float(pos.get("unrealized_pl"))
            current_unrealized_pl_pct = _safe_float(pos.get("unrealized_plpc"))
            current_price = _safe_float(pos.get("current_price")) or market_price
        else:
            current_position_qty = None
            current_market_value = None
            current_unrealized_pl = None
            current_unrealized_pl_pct = None
            current_price = market_price

        current_return_pct: Optional[float] = None
        if fill_price and current_price:
            current_return_pct = round((current_price - fill_price) / fill_price, 6)

        spy_price = _get_current_price("SPY", market_snapshot)
        bil_price = _get_current_price("BIL", market_snapshot)

    # Lineage-enriched fields: prefer lineage_record values when available
    lr = lineage_record or {}
    recovered_trigger_hash = lr.get("trigger_snapshot_hash") or fill.get("trigger_snapshot_hash")

    return {
        "client_order_id": lifecycle.get("client_order_id", ""),
        "broker_order_id": lifecycle.get("broker_order_id", ""),
        "symbol": symbol,
        "side": side,
        "entry_or_exit": "entry" if side == "buy" else "exit",
        "plan_id": fill.get("plan_id"),
        "run_id": fill.get("run_id"),
        "trade_plan_hash": fill.get("trade_plan_hash"),
        "trigger_snapshot_hash": recovered_trigger_hash,
        "trigger_ids": lr.get("trigger_ids"),
        "lineage_status": lr.get("lineage_status"),
        "candidate_rank": lr.get("candidate_rank"),
        "momentum_score": lr.get("momentum_score"),
        "filled_at": filled_at,
        "fill_price": fill_price,
        "limit_price": limit_price,
        "filled_qty": filled_qty,
        "filled_notional": filled_notional,
        "slippage_vs_limit": slippage,
        "slippage_pct": slippage_pct,
        "current_price": current_price,
        "current_position_qty": current_position_qty,
        "current_market_value": current_market_value,
        "current_unrealized_pl": current_unrealized_pl,
        "current_unrealized_pl_pct": current_unrealized_pl_pct,
        "current_return_pct": current_return_pct,
        "spy_price_at_check": spy_price,
        "bil_price_at_check": bil_price,
        "outcome_windows": _compute_outcome_windows(filled_at, checked_at),
        "lifecycle_status": lifecycle.get("lifecycle_status", "filled"),
        "source_integrity_status": source_integrity_status,
        "checked_at": checked_at,
        "first_seen_at": first_seen_at or checked_at,
    }


# ---------------------------------------------------------------------------
# Build outcome snapshot from monitor report + snapshots
# ---------------------------------------------------------------------------

def build_outcome_snapshot(
    monitor_report: dict,
    positions_snapshot: dict,
    market_snapshot: dict,
    existing_outcomes: Optional[dict] = None,
    lineage_snapshot: Optional[dict] = None,
) -> dict:
    """Build a complete outcome snapshot.

    Only filled and partially_filled lifecycle entries produce outcome records.
    Existing outcomes are merged by client_order_id; later checked_at wins.

    When lineage_snapshot is provided, each outcome record is enriched with
    recovered trigger_snapshot_hash, trigger_ids, lineage_status, candidate_rank,
    and momentum_score from the matching lineage record.

    Never submits anything.
    """
    checked_at = monitor_report.get("generated_at") or utc_now_iso()
    positions = positions_snapshot.get("positions", [])
    existing: dict = existing_outcomes or {}

    # Index lineage records by client_order_id
    lineage_by_cid: dict = {}
    if lineage_snapshot:
        for lr in (lineage_snapshot.get("lineage_records") or []):
            cid = lr.get("client_order_id")
            if cid:
                lineage_by_cid[cid] = lr

    # Source integrity: block position/market-derived P/L from mock snapshots
    pos_source = get_snapshot_source(positions_snapshot)
    mkt_source = get_snapshot_source(market_snapshot)
    positions_integrity_blocked = is_mock_source(pos_source)
    market_integrity_blocked = is_mock_source(mkt_source)

    new_records: dict = {}
    for lc in monitor_report.get("lifecycles", []):
        if lc.get("lifecycle_status") not in ("filled", "partially_filled"):
            continue
        cid = lc.get("client_order_id", "")
        if not cid:
            continue
        first_seen = (existing.get(cid) or {}).get("first_seen_at") or checked_at
        record = build_outcome_record(
            lifecycle=lc,
            positions=positions,
            market_snapshot=market_snapshot,
            checked_at=checked_at,
            first_seen_at=first_seen,
            positions_integrity_blocked=positions_integrity_blocked,
            market_integrity_blocked=market_integrity_blocked,
            lineage_record=lineage_by_cid.get(cid),
        )
        new_records[cid] = record

    # Merge: newer checked_at replaces existing
    merged: dict = dict(existing)
    for cid, record in new_records.items():
        ex = merged.get(cid)
        if ex is None or (record.get("checked_at") or "") >= (ex.get("checked_at") or ""):
            merged[cid] = record

    outcomes_list = sorted(merged.values(), key=lambda r: r.get("filled_at") or "")

    now = utc_now_iso()
    run_id = (
        f"outcome_tracker-"
        f"{now.replace(':', '').replace('-', '').replace('Z', '')[:15]}"
        f"-{stable_hash({'ts': now})[:8]}"
    )

    # Snapshot-level integrity status (for downstream consumers)
    any_blocked = positions_integrity_blocked or market_integrity_blocked
    integrity_note: Optional[str] = None
    if any_blocked:
        parts = []
        if positions_integrity_blocked:
            parts.append(f"positions_snapshot.source={pos_source!r}")
        if market_integrity_blocked:
            parts.append(f"market_snapshot.source={mkt_source!r}")
        integrity_note = (
            "WARNING: current_return_pct and position data are BLOCKED — "
            f"{'; '.join(parts)} is not alpaca_paper. "
            "Run live Data Refresh before trusting P/L values."
        )

    snapshot: dict = {
        "run_id": run_id,
        "generated_at": now,
        "outcomes_count": len(outcomes_list),
        "source_integrity_status": "blocked_mock_source" if any_blocked else "ok",
        "source_integrity_note": integrity_note,
        "outcomes": outcomes_list,
    }
    snapshot["snapshot_hash"] = stable_hash(
        {k: v for k, v in snapshot.items() if k != "snapshot_hash"}
    )[:16]
    return snapshot


# ---------------------------------------------------------------------------
# Load existing outcomes
# ---------------------------------------------------------------------------

def load_existing_outcomes(latest_dir: Path) -> dict:
    """Return {client_order_id: record} from data/latest/outcome_snapshot.json, or {}."""
    existing = _load_json(Path(latest_dir) / "outcome_snapshot.json", {})
    if not isinstance(existing, dict):
        return {}
    result: dict = {}
    for record in existing.get("outcomes", []):
        cid = record.get("client_order_id")
        if cid:
            result[cid] = record
    return result


# ---------------------------------------------------------------------------
# Write outputs
# ---------------------------------------------------------------------------

def _format_trade_log_entry(snapshot: dict) -> str:
    outcomes = snapshot.get("outcomes", [])
    lines = [
        f"## Outcome Tracker — {snapshot.get('generated_at', '?')}",
        "",
        f"**Run ID:** `{snapshot.get('run_id')}`  "
        f"**Outcomes tracked:** {snapshot.get('outcomes_count', 0)}",
        "",
    ]
    integrity_note = snapshot.get("source_integrity_note")
    if integrity_note:
        lines += [f"> ⚠ {integrity_note}", ""]
    for o in outcomes:
        windows = o.get("outcome_windows", {})
        pending = [k for k, v in windows.items() if (v or {}).get("status") == "pending"]
        return_str = (
            f" return={o['current_return_pct']:+.3%}"
            if o.get("current_return_pct") is not None else ""
        )
        unpl_str = (
            f" unpl=${o['current_unrealized_pl']:+.4f}"
            if o.get("current_unrealized_pl") is not None else ""
        )
        lines.append(
            f"- {o.get('symbol')} {(o.get('side') or '').upper()} "
            f"({o.get('entry_or_exit')}) fill=${o.get('fill_price')}"
            f"{return_str}{unpl_str}"
            f" | pending: {', '.join(pending) if pending else 'none'}"
        )
    lines += ["", "---", ""]
    return "\n".join(lines)


def _format_experiment_observations(snapshot: dict) -> Optional[str]:
    outcomes = snapshot.get("outcomes", [])
    obs = [
        f"{o.get('symbol')} {o.get('entry_or_exit')}: "
        f"fill=${o.get('fill_price')} current=${o.get('current_price')} "
        f"return={o['current_return_pct']:+.3%}"
        for o in outcomes
        if o.get("current_return_pct") is not None
    ]
    if not obs:
        return None
    lines = [
        f"## Outcome Observations — {snapshot.get('generated_at', '?')}",
        "",
        f"*From outcome_tracker run `{snapshot.get('run_id')}`*",
        "",
        "**Current unrealized returns (intraday — no strategy conclusions yet):**",
    ]
    for line in obs:
        lines.append(f"- {line}")
    lines += [
        "",
        "*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*",
        "",
        "---",
        "",
    ]
    return "\n".join(lines)


def write_outcome_snapshot(
    snapshot: dict,
    latest_dir: Optional[Path] = None,
    outcomes_dir: Optional[Path] = None,
    memory_dir: Optional[Path] = None,
) -> dict:
    """Write outcome snapshot to latest/, history/outcomes/, and memory/. Returns paths."""
    latest_dir = Path(latest_dir) if latest_dir is not None else LATEST_DIR
    outcomes_dir = Path(outcomes_dir) if outcomes_dir is not None else HISTORY_DIR / "outcomes"
    memory_dir = Path(memory_dir) if memory_dir is not None else MEMORY_DIR

    latest_path = latest_dir / "outcome_snapshot.json"
    _write_json_atomic(latest_path, snapshot)

    today = date.today().isoformat()
    hash8 = (snapshot.get("snapshot_hash") or "00000000")[:8]
    history_path = outcomes_dir / f"outcome_{today}-{hash8}.json"
    _write_json_atomic(history_path, snapshot)

    trade_log_path = memory_dir / "TRADE-LOG.md"
    with trade_log_path.open("a", encoding="utf-8") as fh:
        fh.write(_format_trade_log_entry(snapshot))

    exp_entry = _format_experiment_observations(snapshot)
    exp_path = memory_dir / "EXPERIMENT-LOG.md"
    if exp_entry:
        with exp_path.open("a", encoding="utf-8") as fh:
            fh.write(exp_entry)

    return {
        "latest_path": str(latest_path),
        "history_path": str(history_path),
        "trade_log_path": str(trade_log_path),
        "experiment_log_path": str(exp_path) if exp_entry else None,
    }
