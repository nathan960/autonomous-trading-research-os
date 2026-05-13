"""Research-only trade lineage linker for Autonomous Trading Research OS.

Links filled orders back to the trigger snapshots, candidates, and trigger IDs
that produced them. Enables trigger_performance to count fills per trigger and
outcome_tracker to surface recovered trigger provenance.

SAFETY:
  - No execution path.
  - Never calls execute_paper.py.
  - Never approves trade plans.
  - Never places, cancels, or replaces orders.
  - Never modifies config/strategy.json, risk_limits.json, or trigger_registry.json.
"""
from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Optional

from ..config import HISTORY_DIR, LATEST_DIR, MEMORY_DIR
from ..hashing import stable_hash
from ..time_utils import utc_now_iso


# ---------------------------------------------------------------------------
# Status constants
# ---------------------------------------------------------------------------

LINEAGE_STATUS_COMPLETE = "complete_from_trade_plan"
LINEAGE_STATUS_RECOVERED = "complete_recovered_from_trigger_history"
LINEAGE_STATUS_PARTIAL_NO_HASH = "partial_missing_trigger_snapshot_hash"
LINEAGE_STATUS_PARTIAL_NO_IDS = "partial_missing_trigger_ids"

# Trigger IDs that must all pass for a symbol to appear in candidates.
# A symbol in candidates (or selected) passed all of these.
ELIGIBILITY_TRIGGER_IDS: tuple = (
    "SPY_REGIME_200DMA_V1",
    "STOCK_TREND_200DMA_V1",
    "LIQUIDITY_GATE_V1",
    "SPREAD_GATE_V1",
    "MOMENTUM_BLEND_6M_12M_V1",
    "ATR_SIZING_V1",
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_json(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


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


def _date_range(end_date_str: str, days: int) -> list:
    end = date.fromisoformat(end_date_str)
    return [(end - timedelta(days=i)).isoformat() for i in range(days - 1, -1, -1)]


# ---------------------------------------------------------------------------
# Data loaders
# ---------------------------------------------------------------------------

def load_trigger_history_lines(history_dir: Path, date_strs: list) -> list:
    """Load all JSONL entries from trigger history for given dates, sorted by scanned_at."""
    entries = []
    for date_str in date_strs:
        path = history_dir / "triggers" / f"{date_str}.jsonl"
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
                entries.append(entry)
            except Exception:
                continue
    return sorted(entries, key=lambda e: e.get("scanned_at") or "")


def load_execution_index(history_dir: Path) -> dict:
    """Build {run_id: execution_report} from history/executions/*.json files."""
    index: dict = {}
    exec_dir = history_dir / "executions"
    if not exec_dir.is_dir():
        return index
    for f in sorted(exec_dir.glob("*.json")):
        data = _load_json(f, {})
        run_id = data.get("run_id")
        if run_id:
            index[run_id] = data
    return index


def load_order_records(history_dir: Path) -> dict:
    """Build {client_order_id: order_record} from history/orders/TOS-*.json files."""
    index: dict = {}
    orders_dir = history_dir / "orders"
    if not orders_dir.is_dir():
        return index
    for f in sorted(orders_dir.glob("TOS-*.json")):
        data = _load_json(f, {})
        cid = data.get("client_order_id")
        if cid:
            index[cid] = data
    return index


# ---------------------------------------------------------------------------
# Trigger hash recovery
# ---------------------------------------------------------------------------

def recover_trigger_snapshot_hash(
    plan_id: Optional[str],
    symbol: str,
    executed_at_str: str,
    current_trade_plan: dict,
    trigger_history_lines: list,
) -> tuple:
    """Try to recover trigger_snapshot_hash for a fill.

    Returns (hash_or_none, source_string_or_none, matching_entry_or_none).

    Sources:
      "from_current_trade_plan"         — current data/latest/trade_plan.json matched.
      "recovered_from_trigger_history"  — closest JSONL entry before execution found.
    """
    # 1. Check current trade plan — cheapest path
    if plan_id and current_trade_plan.get("plan_id") == plan_id:
        h = current_trade_plan.get("trigger_snapshot_hash")
        if h:
            return (h, "from_current_trade_plan", None)

    # 2. Search trigger JSONL history for the closest entry where the symbol
    #    was evaluated (in candidates or selected) and scanned_at <= executed_at.
    best_entry: Optional[dict] = None
    best_scanned: str = ""
    for entry in trigger_history_lines:
        scanned_at = entry.get("scanned_at") or ""
        if executed_at_str and scanned_at > executed_at_str:
            continue
        if symbol not in entry.get("selected", []) and symbol not in entry.get("candidates", []):
            continue
        if scanned_at >= best_scanned:
            best_scanned = scanned_at
            best_entry = entry

    if best_entry:
        h = best_entry.get("trigger_snapshot_hash")
        if h:
            return (h, "recovered_from_trigger_history", best_entry)

    return (None, None, None)


# ---------------------------------------------------------------------------
# Trigger ID inference
# ---------------------------------------------------------------------------

def infer_trigger_ids(
    symbol: str,
    trigger_entry: Optional[dict],
    trigger_snapshot: dict,
) -> tuple:
    """Infer trigger_ids passed by symbol at fill time.

    Returns (trigger_ids_list_or_none, source_string_or_none).

    Never invents IDs — returns None if evidence is insufficient.
    """
    # From current trigger snapshot symbol_results (most reliable per-trigger data)
    sym_result = (trigger_snapshot.get("symbol_results") or {}).get(symbol)
    if sym_result and sym_result.get("passes"):
        ids = []
        if (trigger_snapshot.get("regime") or {}).get("risk_on"):
            ids.append("SPY_REGIME_200DMA_V1")
        for sub_key, id_key in (
            ("spread", "trigger_id"),
            ("trend", "trigger_id"),
            ("momentum", "trigger_id"),
            ("liquidity", "trigger_id"),
        ):
            sub = sym_result.get(sub_key) or {}
            tid = sub.get(id_key)
            if tid and sub.get("passes"):
                ids.append(tid)
        atr = sym_result.get("atr") or {}
        if atr.get("signal_id"):
            ids.append(atr["signal_id"])
        if ids:
            return (sorted(set(ids)), "from_current_trigger_snapshot")

    # From JSONL entry: if symbol was in candidates (passed all eligibility checks),
    # infer it passed all ELIGIBILITY_TRIGGER_IDS. This is safe because candidates
    # are defined as symbols that passed every required gate.
    if trigger_entry:
        in_selected = symbol in (trigger_entry.get("selected") or [])
        in_candidates = symbol in (trigger_entry.get("candidates") or [])
        if (in_selected or in_candidates) and trigger_entry.get("risk_on"):
            source = (
                "inferred_from_selected_in_trigger_history"
                if in_selected
                else "inferred_from_candidates_in_trigger_history"
            )
            return (list(ELIGIBILITY_TRIGGER_IDS), source)

    return (None, None)


# ---------------------------------------------------------------------------
# Candidate metadata
# ---------------------------------------------------------------------------

def _candidate_metadata(
    symbol: str,
    trigger_entry: Optional[dict],
    trigger_snapshot: dict,
) -> dict:
    """Extract candidate rank, source, and momentum score."""
    candidate_rank: Optional[int] = None
    candidate_source: Optional[str] = None
    momentum_score: Optional[float] = None

    if trigger_entry:
        selected = trigger_entry.get("selected") or []
        candidates = trigger_entry.get("candidates") or []
        if symbol in selected:
            candidate_rank = selected.index(symbol)
            candidate_source = "selected"
        elif symbol in candidates:
            candidate_source = "candidates_not_selected"

    # Momentum score from current snapshot (best available even if stale)
    sym_result = (trigger_snapshot.get("symbol_results") or {}).get(symbol) or {}
    mom = sym_result.get("momentum") or {}
    momentum_score = _safe_float(mom.get("momentum_score"))

    return {
        "candidate_rank": candidate_rank,
        "candidate_source": candidate_source,
        "momentum_score": momentum_score,
    }


# ---------------------------------------------------------------------------
# Build a single lineage record
# ---------------------------------------------------------------------------

def build_lineage_record(
    lifecycle: dict,
    execution_index: dict,
    current_trade_plan: dict,
    trigger_history_lines: list,
    trigger_snapshot: dict,
    outcome_by_cid: dict,
    linked_at: str,
) -> dict:
    """Build a lineage record for one filled lifecycle entry.

    Never submits or approves anything. Pure computation.
    """
    cid: str = lifecycle.get("client_order_id", "")
    symbol: str = lifecycle.get("symbol", "")
    side: str = lifecycle.get("side", "")
    broker_order_id = lifecycle.get("broker_order_id")
    broker_status = lifecycle.get("broker_status")
    limit_price = _safe_float(lifecycle.get("limit_price"))

    fill = lifecycle.get("fill") or {}
    plan_id = fill.get("plan_id")
    trade_plan_hash = fill.get("trade_plan_hash")
    run_id = fill.get("run_id")
    fill_price = _safe_float(fill.get("fill_price"))
    filled_qty = _safe_float(fill.get("filled_qty"))
    filled_notional = _safe_float(fill.get("filled_notional"))
    filled_at: str = fill.get("filled_at") or lifecycle.get("submitted_at") or ""

    # Execution report lookup
    exec_report = execution_index.get(run_id) or {}

    # Trigger snapshot hash recovery
    trigger_hash, hash_source, trigger_entry = recover_trigger_snapshot_hash(
        plan_id, symbol, filled_at, current_trade_plan, trigger_history_lines
    )

    # Trigger ID inference
    trigger_ids, ids_source = infer_trigger_ids(symbol, trigger_entry, trigger_snapshot)

    # Candidate metadata
    cand = _candidate_metadata(symbol, trigger_entry, trigger_snapshot)

    # Target data — only available if current trade plan matches this fill's plan_id
    target_weight: Optional[float] = None
    target_notional: Optional[float] = None
    target_reason: Optional[str] = None
    if plan_id and current_trade_plan.get("plan_id") == plan_id:
        targets = current_trade_plan.get("targets") or {}
        t = targets.get(symbol) or {}
        target_weight = _safe_float(t.get("weight"))
        target_notional = _safe_float(t.get("notional"))
        target_reason = t.get("reason")

    # Proposed order data from execution report
    proposed_side: Optional[str] = None
    proposed_notional: Optional[float] = None
    proposed_limit_price: Optional[float] = None
    proposed_target_weight: Optional[float] = None
    for order in (exec_report.get("orders_validated") or exec_report.get("orders_submitted") or []):
        if isinstance(order, dict) and order.get("symbol") == symbol:
            proposed_side = order.get("side")
            proposed_notional = _safe_float(order.get("notional"))
            proposed_limit_price = _safe_float(order.get("limit_price"))
            proposed_target_weight = _safe_float(order.get("target_weight"))
            break

    # Outcome data
    outcome = outcome_by_cid.get(cid) or {}

    # Lineage status — direct plan match is always COMPLETE; history recovery
    # requires trigger_ids to be inferred as well.
    if hash_source == "from_current_trade_plan":
        lineage_status = LINEAGE_STATUS_COMPLETE
    elif trigger_hash and trigger_ids:
        lineage_status = LINEAGE_STATUS_RECOVERED
    elif trigger_hash and not trigger_ids:
        lineage_status = LINEAGE_STATUS_PARTIAL_NO_IDS
    else:
        lineage_status = LINEAGE_STATUS_PARTIAL_NO_HASH

    lineage_note: Optional[str] = None
    if lineage_status == LINEAGE_STATUS_PARTIAL_NO_HASH:
        lineage_note = (
            f"trigger_snapshot_hash not recoverable for plan_id={plan_id!r}. "
            "Trade plan history is not persisted to data/history/; no JSONL entry found "
            "before filled_at. Save trade plans to history to improve lineage completeness."
        )
    elif lineage_status == LINEAGE_STATUS_PARTIAL_NO_IDS:
        lineage_note = (
            f"trigger_snapshot_hash recovered but trigger_ids not inferrable for {symbol!r}. "
            "Symbol not found in trigger history candidates."
        )

    return {
        # Fill identification
        "client_order_id": cid,
        "broker_order_id": broker_order_id,
        "symbol": symbol,
        "side": side,
        # Execution provenance
        "plan_id": plan_id,
        "trade_plan_hash": trade_plan_hash,
        "run_id": run_id,
        "broker_status": broker_status,
        # Alert provenance (not tracked in current pipeline)
        "alert_id": None,
        # Trigger provenance
        "trigger_snapshot_hash": trigger_hash,
        "trigger_snapshot_hash_source": hash_source,
        "trigger_ids": trigger_ids,
        "trigger_ids_source": ids_source,
        # Candidate metadata
        "candidate_rank": cand["candidate_rank"],
        "candidate_source": cand["candidate_source"],
        "momentum_score": cand["momentum_score"],
        # Target data (from trade plan — None if plan not in history)
        "target_weight": target_weight,
        "target_notional": target_notional,
        "target_reason": target_reason,
        # Proposed order data (from execution report)
        "proposed_side": proposed_side,
        "proposed_notional": proposed_notional,
        "proposed_limit_price": proposed_limit_price,
        "proposed_target_weight": proposed_target_weight,
        # Fill data
        "limit_price": limit_price,
        "fill_price": fill_price,
        "filled_qty": filled_qty,
        "filled_notional": filled_notional,
        "filled_at": filled_at,
        # Outcome link
        "outcome_client_order_id": cid if outcome else None,
        "current_return_pct": outcome.get("current_return_pct"),
        "current_unrealized_pl": outcome.get("current_unrealized_pl"),
        "outcome_windows": outcome.get("outcome_windows"),
        # Lineage quality
        "lineage_status": lineage_status,
        "lineage_note": lineage_note,
        "linked_at": linked_at,
    }


# ---------------------------------------------------------------------------
# Build full lineage snapshot
# ---------------------------------------------------------------------------

def build_lineage_snapshot(
    monitor_report: dict,
    execution_index: dict,
    current_trade_plan: dict,
    trigger_history_lines: list,
    trigger_snapshot: dict,
    outcome_snapshot: dict,
) -> dict:
    """Build a complete lineage snapshot from all data sources.

    Only filled and partially_filled lifecycles produce lineage records.
    Deduped by client_order_id — latest checked_at wins.

    Never submits anything.
    """
    linked_at = utc_now_iso()

    # Index outcomes by client_order_id
    outcome_by_cid: dict = {}
    for o in (outcome_snapshot.get("outcomes") or []):
        cid = o.get("client_order_id")
        if cid:
            outcome_by_cid[cid] = o

    # Build records, dedup by client_order_id
    records_by_cid: dict = {}
    for lc in (monitor_report.get("lifecycles") or []):
        if lc.get("lifecycle_status") not in ("filled", "partially_filled"):
            continue
        cid = lc.get("client_order_id", "")
        if not cid:
            continue
        record = build_lineage_record(
            lifecycle=lc,
            execution_index=execution_index,
            current_trade_plan=current_trade_plan,
            trigger_history_lines=trigger_history_lines,
            trigger_snapshot=trigger_snapshot,
            outcome_by_cid=outcome_by_cid,
            linked_at=linked_at,
        )
        records_by_cid[cid] = record

    records = sorted(records_by_cid.values(), key=lambda r: r.get("filled_at") or "")

    complete = sum(1 for r in records if r["lineage_status"] in (LINEAGE_STATUS_COMPLETE, LINEAGE_STATUS_RECOVERED))
    partial = len(records) - complete

    now = utc_now_iso()
    run_id = (
        f"lineage-"
        f"{now.replace(':', '').replace('-', '').replace('Z', '')[:15]}"
        f"-{stable_hash({'ts': now})[:8]}"
    )

    snapshot: dict = {
        "run_id": run_id,
        "generated_at": now,
        "lineage_count": len(records),
        "complete_count": complete,
        "partial_count": partial,
        "lineage_records": records,
    }
    snapshot["snapshot_hash"] = stable_hash(
        {k: v for k, v in snapshot.items() if k != "snapshot_hash"}
    )[:16]
    return snapshot


# ---------------------------------------------------------------------------
# Fill counts for trigger performance
# ---------------------------------------------------------------------------

def collect_fill_counts_from_lineage(lineage_snapshot: dict) -> dict:
    """Return {trigger_id: fill_count} from a lineage snapshot.

    Only counts records with trigger_ids (i.e., complete/recovered lineage).
    """
    counts: dict = {}
    for record in (lineage_snapshot.get("lineage_records") or []):
        trigger_ids = record.get("trigger_ids") or []
        for tid in trigger_ids:
            counts[tid] = counts.get(tid, 0) + 1
    return counts


# ---------------------------------------------------------------------------
# Write outputs
# ---------------------------------------------------------------------------

def _format_lineage_signal_log_entry(snapshot: dict) -> str:
    records = snapshot.get("lineage_records", [])
    lines = [
        f"## Lineage Snapshot — {snapshot.get('generated_at', '?')}",
        "",
        f"**Run ID:** `{snapshot.get('run_id')}`  "
        f"**Records:** {snapshot.get('lineage_count', 0)} "
        f"(complete: {snapshot.get('complete_count', 0)}, "
        f"partial: {snapshot.get('partial_count', 0)})",
        "",
    ]
    for r in records:
        status = r.get("lineage_status", "?")
        tids = r.get("trigger_ids") or []
        tid_str = ", ".join(tids[:3]) + ("…" if len(tids) > 3 else "") if tids else "none"
        lines.append(
            f"- {r.get('symbol')} {(r.get('side') or '').upper()} "
            f"cid={r.get('client_order_id')} "
            f"trigger_hash={str(r.get('trigger_snapshot_hash') or 'null')[:12]} "
            f"trigger_ids=[{tid_str}] "
            f"status={status}"
        )
    lines += ["", "---", ""]
    return "\n".join(lines)


def write_lineage_snapshot(
    snapshot: dict,
    latest_dir: Optional[Path] = None,
    lineage_history_dir: Optional[Path] = None,
    memory_dir: Optional[Path] = None,
) -> dict:
    """Write lineage snapshot to latest/, history/lineage/, and memory/. Returns paths."""
    latest_dir = Path(latest_dir) if latest_dir is not None else LATEST_DIR
    lineage_history_dir = (
        Path(lineage_history_dir) if lineage_history_dir is not None
        else HISTORY_DIR / "lineage"
    )
    memory_dir = Path(memory_dir) if memory_dir is not None else MEMORY_DIR

    latest_path = latest_dir / "lineage_snapshot.json"
    _write_json_atomic(latest_path, snapshot)

    today = date.today().isoformat()
    hash8 = (snapshot.get("snapshot_hash") or "00000000")[:8]
    history_path = lineage_history_dir / f"lineage_{today}-{hash8}.json"
    _write_json_atomic(history_path, snapshot)

    signal_log_path = memory_dir / "SIGNAL-LOG.md"
    entry = _format_lineage_signal_log_entry(snapshot)
    with signal_log_path.open("a", encoding="utf-8") as fh:
        fh.write(entry)

    return {
        "latest_path": str(latest_path),
        "history_path": str(history_path),
        "signal_log_path": str(signal_log_path),
    }
