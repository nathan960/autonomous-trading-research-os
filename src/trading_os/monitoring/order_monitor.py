"""Order lifecycle monitor — read-only, never submits, cancels, or replaces orders.

Fetches current broker order state for every submitted paper order,
matches it to per-order audit files, updates lifecycle status, and
writes a consolidated monitor report.

Safety invariants enforced unconditionally:
  - Never calls submit_order, cancel_order, replace_order, or any write method.
  - Never imports or references paper_executor.
  - Never sets approved_for_execution=True.
  - Reads broker state; never mutates it.
  - All file writes are atomic (.tmp → .replace()).
  - Secrets are never included in any output.

Lifecycle statuses (superset of Alpaca statuses):
  pending_new       broker received the order, not yet confirmed
  accepted          broker confirmed (may not yet be at exchange)
  new               at the exchange, resting
  partially_filled  partially filled
  filled            fully filled
  canceled          order was canceled
  rejected          broker rejected the order
  expired           day order expired at close
  missing           broker has no record (may be too old or never submitted)
  unknown           broker returned a status not recognised here
"""
from __future__ import annotations

import json
import logging
import re
import warnings
from pathlib import Path
from typing import Any, Optional

logger = logging.getLogger(__name__)

from ..hashing import stable_hash
from ..time_utils import utc_now_iso

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

TERMINAL_STATUSES: frozenset = frozenset({
    "filled", "partially_filled", "canceled", "rejected", "expired",
})

ACTIVE_STATUSES: frozenset = frozenset({
    "new", "pending_new", "accepted", "accepted_for_bidding",
    "held", "pending_cancel", "pending_replace", "done_for_day",
})

# British-spelling alias for "canceled"
_STATUS_ALIASES: dict = {"cancelled": "canceled"}

# Pattern that identifies per-order audit files (client_order_id prefix)
_CLIENT_ORDER_FILE_RE = re.compile(r"^TOS-.*\.json$")

# Pattern for monitor-report files (skip these when scanning for order audits)
_MONITOR_REPORT_RE = re.compile(r"^order_monitor_.*\.json$")


# ---------------------------------------------------------------------------
# Status normalisation
# ---------------------------------------------------------------------------

def _normalize_status(status: Any) -> str:
    """Return a canonical lowercase status string.

    Handles Alpaca SDK str-enum members (OrderStatus) where str() returns
    "OrderStatus.FILLED" instead of "filled" on Python 3.9.  We extract
    .value when available so we always get the raw string value.
    """
    if status is None:
        return "unknown"
    raw = str(status.value).lower().strip() if hasattr(status, "value") else str(status).lower().strip()
    return _STATUS_ALIASES.get(raw, raw)


# ---------------------------------------------------------------------------
# Broker order fetch (lazy SDK imports so tests don't need credentials)
# ---------------------------------------------------------------------------

def fetch_broker_orders(
    trading_client: Any,
    known_broker_ids: Optional[list] = None,
    known_client_ids: Optional[list] = None,
    lookback_days: int = 7,
) -> dict:
    """Fetch open and recent closed orders from Alpaca; fall back to direct lookups.

    Strategy (three layers, each read-only):
      1. Bulk fetch all open orders.
      2. Bulk fetch closed orders from the last *lookback_days* days (default 7).
      3. For any known_broker_id not yet found: call get_order_by_id().
      4. For any known_client_id not yet found: call get_order_by_client_id().

    Returns:
        {
            "by_broker_id":  {broker_order_id: order_primitive},
            "by_client_id":  {client_order_id: order_primitive},
            "fetch_log":     {open_count, closed_count, direct_broker_id_hits,
                              direct_client_id_hits, direct_broker_id_errors,
                              direct_client_id_errors}
        }

    Never submits, cancels, or replaces orders.
    Exceptions from individual fallback lookups are caught and counted, never raised.
    """
    from datetime import datetime, timezone, timedelta

    from alpaca.trading.requests import GetOrderByIdRequest, GetOrdersRequest

    from ..data.alpaca_client import _to_primitive

    result_by_broker: dict = {}
    result_by_client: dict = {}

    fetch_log: dict = {
        "open_count": 0,
        "closed_count": 0,
        "direct_broker_id_lookups": 0,
        "direct_broker_id_hits": 0,
        "direct_broker_id_errors": 0,
        "direct_client_id_lookups": 0,
        "direct_client_id_hits": 0,
        "direct_client_id_errors": 0,
    }

    def _index(orders_raw: Any) -> int:
        """Add orders to lookup dicts; return count added."""
        orders = _to_primitive(orders_raw)
        if not isinstance(orders, list):
            return 0
        added = 0
        for o in orders:
            if not isinstance(o, dict):
                continue
            bid = o.get("id") or o.get("order_id")
            cid = o.get("client_order_id")
            if bid:
                result_by_broker[str(bid)] = o
            if cid:
                result_by_client[str(cid)] = o
            added += 1
        return added

    # ── Layer 1: bulk open orders ────────────────────────────────────────────
    open_req = GetOrdersRequest(status="open")
    fetch_log["open_count"] = _index(trading_client.get_orders(filter=open_req))

    # ── Layer 2: bulk closed orders with explicit 7-day lookback ────────────
    # Without `after`, Alpaca defaults to the current calendar day (ET), which
    # misses orders from earlier days.  Force a full 7-day window.
    after_dt = datetime.now(timezone.utc) - timedelta(days=lookback_days)
    closed_req = GetOrdersRequest(status="closed", limit=500, after=after_dt)
    fetch_log["closed_count"] = _index(trading_client.get_orders(filter=closed_req))

    # ── Layer 3a: direct lookup by broker_order_id (UUID) ───────────────────
    # Catches orders that slipped through pagination or landed outside the
    # lookback window.  Uses get_order_by_id which always hits the live index.
    for bid in (known_broker_ids or []):
        bid_str = str(bid).strip()
        if not bid_str or bid_str in result_by_broker:
            continue
        fetch_log["direct_broker_id_lookups"] += 1
        try:
            raw = trading_client.get_order_by_id(bid_str, filter=GetOrderByIdRequest(nested=False))
            prim = _to_primitive(raw)
            if isinstance(prim, dict):
                cid = prim.get("client_order_id")
                result_by_broker[bid_str] = prim
                if cid:
                    result_by_client[str(cid)] = prim
                fetch_log["direct_broker_id_hits"] += 1
        except Exception:
            fetch_log["direct_broker_id_errors"] += 1

    # ── Layer 3b: direct lookup by client_order_id ──────────────────────────
    # Final fallback: if still not found after broker_id lookup, try the
    # client_order_id endpoint (deterministic TOS- prefix ID we assigned).
    for cid in (known_client_ids or []):
        cid_str = str(cid).strip()
        if not cid_str or cid_str in result_by_client:
            continue
        fetch_log["direct_client_id_lookups"] += 1
        try:
            raw = trading_client.get_order_by_client_id(cid_str)
            prim = _to_primitive(raw)
            if isinstance(prim, dict):
                bid = prim.get("id") or prim.get("order_id")
                result_by_client[cid_str] = prim
                if bid:
                    result_by_broker[str(bid)] = prim
                fetch_log["direct_client_id_hits"] += 1
        except Exception:
            fetch_log["direct_client_id_errors"] += 1

    return {
        "by_broker_id": result_by_broker,
        "by_client_id": result_by_client,
        "fetch_log": fetch_log,
    }


# ---------------------------------------------------------------------------
# Order audit file helpers
# ---------------------------------------------------------------------------

def load_submitted_audits(orders_dir: Path) -> list:
    """Load all per-order audit files that have submitted=True.

    Skips monitor-report files (order_monitor_*.json).
    Returns a list of (path, audit_dict) tuples.
    """
    results: list = []
    if not orders_dir.exists():
        return results
    for f in sorted(orders_dir.iterdir()):
        if not f.is_file() or f.suffix != ".json":
            continue
        if _MONITOR_REPORT_RE.match(f.name):
            continue
        try:
            audit = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        if audit.get("submitted") is True:
            results.append((f, audit))
    return results


def _write_json_atomic(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True, default=str)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(path)


# ---------------------------------------------------------------------------
# Execution report index — link client_order_id to plan context
# ---------------------------------------------------------------------------

def build_plan_refs_index(executions_dir: Path) -> dict:
    """Scan execution history for paper runs; build {client_order_id: plan_refs}.

    plan_refs = {plan_id, run_id, trade_plan_hash}
    """
    index: dict = {}
    if not executions_dir.exists():
        return index
    for f in executions_dir.glob("*_paper.json"):
        try:
            report = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        plan_id = report.get("plan_id")
        run_id = report.get("run_id")
        trade_plan_hash = report.get("trade_plan_hash")
        for o in report.get("orders_submitted", []):
            cid = o.get("client_order_id")
            if cid:
                index[str(cid)] = {
                    "plan_id": plan_id,
                    "run_id": run_id,
                    "trade_plan_hash": trade_plan_hash,
                }
    return index


def find_trigger_snapshot_hash(trade_plan_path: Optional[Path], plan_id: Optional[str]) -> Optional[str]:
    """Return trigger_snapshot_hash from the current trade plan if plan_id matches."""
    if not trade_plan_path or not trade_plan_path.exists() or not plan_id:
        return None
    try:
        plan = json.loads(trade_plan_path.read_text(encoding="utf-8"))
        if plan.get("plan_id") == plan_id:
            return plan.get("trigger_snapshot_hash")
    except Exception:
        pass
    return None


# ---------------------------------------------------------------------------
# Fill reconciliation
# ---------------------------------------------------------------------------

def reconcile_fill(
    broker_order: dict,
    positions: list,
    plan_refs: Optional[dict],
    trigger_snapshot_hash: Optional[str],
) -> dict:
    """Build fill reconciliation data from a filled/partially-filled broker order.

    Never submits anything. Pure computation.
    """
    symbol: str = broker_order.get("symbol", "")

    fill_price: Optional[float] = None
    raw_fp = broker_order.get("filled_avg_price")
    if raw_fp is not None:
        try:
            fill_price = float(raw_fp)
        except (TypeError, ValueError):
            pass

    filled_qty: Optional[float] = None
    raw_qty = broker_order.get("filled_qty")
    if raw_qty is not None:
        try:
            filled_qty = float(raw_qty)
        except (TypeError, ValueError):
            pass

    filled_notional: Optional[float] = None
    if fill_price is not None and filled_qty is not None:
        filled_notional = round(fill_price * filled_qty, 2)

    filled_at: Optional[str] = broker_order.get("filled_at")

    # Confirm position appears in current positions snapshot
    position_confirmed = any(
        p.get("symbol") == symbol and float(p.get("qty") or 0) > 0
        for p in positions
        if isinstance(p, dict)
    )

    fill: dict = {
        "fill_price": fill_price,
        "filled_qty": filled_qty,
        "filled_notional": filled_notional,
        "filled_at": filled_at,
        "position_confirmed": position_confirmed,
    }

    if plan_refs:
        fill["plan_id"] = plan_refs.get("plan_id")
        fill["run_id"] = plan_refs.get("run_id")
        fill["trade_plan_hash"] = plan_refs.get("trade_plan_hash")
        fill["trigger_snapshot_hash"] = trigger_snapshot_hash
    else:
        fill["plan_id"] = None
        fill["run_id"] = None
        fill["trade_plan_hash"] = None
        fill["trigger_snapshot_hash"] = None

    return fill


# ---------------------------------------------------------------------------
# Stale order detection
# ---------------------------------------------------------------------------

def is_stale_order(lifecycle_status: str, clock: dict, time_in_force: str = "day") -> bool:
    """Return True if a day order is still active but market is closed.

    Only flags DAY orders; GTC orders are not flagged as stale.
    """
    if time_in_force.lower() not in ("day", ""):
        return False
    if lifecycle_status not in ACTIVE_STATUSES:
        return False
    is_open = clock.get("is_open", True)
    return not is_open


# ---------------------------------------------------------------------------
# Single-order lifecycle computation
# ---------------------------------------------------------------------------

def build_order_lifecycle(
    audit: dict,
    broker_lookup: dict,
    plan_refs: Optional[dict],
    trigger_snapshot_hash: Optional[str],
    positions: list,
    clock: dict,
    checked_at: str,
) -> dict:
    """Compute the lifecycle record for a single submitted order.

    Args:
        audit:                  Per-order audit dict (from data/history/orders/).
        broker_lookup:          {"by_broker_id": {...}, "by_client_id": {...}}
        plan_refs:              {plan_id, run_id, trade_plan_hash} or None.
        trigger_snapshot_hash:  From trade plan, or None.
        positions:              Current positions list.
        clock:                  Broker clock dict.
        checked_at:             ISO timestamp for this check.

    Returns a lifecycle dict. Never submits anything.
    """
    client_order_id: str = audit.get("client_order_id", "")
    broker_order_id: str = audit.get("broker_order_id", "") or ""
    symbol: str = audit.get("symbol", "")
    time_in_force: str = audit.get("time_in_force", "day")

    # Look up in broker cache: prefer broker_order_id, fall back to client_order_id
    by_broker = broker_lookup.get("by_broker_id", {})
    by_client = broker_lookup.get("by_client_id", {})

    broker_order: Optional[dict] = None
    if broker_order_id:
        broker_order = by_broker.get(broker_order_id)
    if broker_order is None and client_order_id:
        broker_order = by_client.get(client_order_id)

    if broker_order is None:
        lifecycle_status = "missing"
        warning = (
            f"order {client_order_id} (broker_id={broker_order_id!r}) "
            "not found in Alpaca open or recent closed orders"
        )
        fill = None
        stale_warning = None
    else:
        raw_status = _normalize_status(broker_order.get("status"))
        if raw_status in TERMINAL_STATUSES or raw_status in ACTIVE_STATUSES:
            lifecycle_status = raw_status
        else:
            lifecycle_status = "unknown"
            msg = (
                f"order {audit.get('client_order_id', '?')} has unrecognised "
                f"broker status {broker_order.get('status')!r} (normalised: {raw_status!r})"
            )
            warnings.warn(msg, RuntimeWarning, stacklevel=2)
            logger.warning(msg)

        warning = None

        fill = None
        if lifecycle_status in ("filled", "partially_filled"):
            fill = reconcile_fill(
                broker_order=broker_order,
                positions=positions,
                plan_refs=plan_refs,
                trigger_snapshot_hash=trigger_snapshot_hash,
            )

        stale_warning = None
        if is_stale_order(lifecycle_status, clock, time_in_force):
            stale_warning = (
                f"day order {client_order_id} ({symbol}) is still active "
                f"(status={lifecycle_status!r}) but market is closed"
            )

    lifecycle: dict = {
        "client_order_id": client_order_id,
        "broker_order_id": broker_order_id,
        "symbol": symbol,
        "side": audit.get("side"),
        "notional": audit.get("notional"),
        "limit_price": audit.get("limit_price"),
        "submitted_at": audit.get("submitted_at"),
        "submitted": True,
        "lifecycle_status": lifecycle_status,
        "broker_status": broker_order.get("status") if broker_order else None,
        "fill": fill,
        "stale_warning": stale_warning,
        "warning": warning,
        "checked_at": checked_at,
    }
    return lifecycle


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

def run_order_monitor(
    broker_lookup: dict,
    orders_dir: Path,
    executions_dir: Path,
    positions: list,
    clock: dict,
    trade_plan_path: Optional[Path] = None,
    dry_run: bool = False,
) -> dict:
    """Run the full order lifecycle monitor.

    Args:
        broker_lookup:      {"by_broker_id": {...}, "by_client_id": {...},
                             "fetch_log": {...}} or empty.
                            fetch_log is optional and surfaced in the report.
        orders_dir:         data/history/orders/
        executions_dir:     data/history/executions/
        positions:          Current positions list (from account state or snapshot).
        clock:              Broker clock dict.
        trade_plan_path:    Path to data/latest/trade_plan.json (for trigger_snapshot_hash).
        dry_run:            If True, broker_lookup is from stored snapshot (noted in report).

    Returns a report dict. Never submits, cancels, or replaces orders.
    """
    run_id = (
        f"order_monitor-"
        f"{utc_now_iso().replace(':', '').replace('-', '').replace('Z', '')[:15]}"
        f"-{stable_hash({'ts': utc_now_iso()})[:8]}"
    )
    generated_at = utc_now_iso()

    # Build plan refs index from execution history
    plan_refs_index = build_plan_refs_index(executions_dir)

    # Load all submitted audit files
    audit_entries = load_submitted_audits(orders_dir)

    lifecycles: list = []
    warnings: list = []
    stale_orders: list = []
    updated_audits: list = []

    for audit_path, audit in audit_entries:
        client_order_id = audit.get("client_order_id", "")
        plan_refs = plan_refs_index.get(client_order_id)

        trigger_hash = None
        if plan_refs:
            trigger_hash = find_trigger_snapshot_hash(
                trade_plan_path, plan_refs.get("plan_id")
            )

        lifecycle = build_order_lifecycle(
            audit=audit,
            broker_lookup=broker_lookup,
            plan_refs=plan_refs,
            trigger_snapshot_hash=trigger_hash,
            positions=positions,
            clock=clock,
            checked_at=generated_at,
        )
        lifecycles.append(lifecycle)

        if lifecycle.get("warning"):
            warnings.append(lifecycle["warning"])
        if lifecycle.get("stale_warning"):
            stale_orders.append(lifecycle["stale_warning"])

        # Update audit file with latest lifecycle status (atomic)
        updated_audit = dict(audit)
        updated_audit["lifecycle_status"] = lifecycle["lifecycle_status"]
        updated_audit["broker_status_latest"] = lifecycle["broker_status"]
        updated_audit["lifecycle_checked_at"] = generated_at
        if lifecycle.get("fill"):
            updated_audit["fill"] = lifecycle["fill"]
        if lifecycle.get("stale_warning"):
            updated_audit["stale_warning"] = lifecycle["stale_warning"]
        updated_audits.append((audit_path, updated_audit))

    # Aggregate counts
    n_total = len(lifecycles)
    n_filled = sum(1 for lc in lifecycles if lc["lifecycle_status"] == "filled")
    n_partially = sum(1 for lc in lifecycles if lc["lifecycle_status"] == "partially_filled")
    n_active = sum(1 for lc in lifecycles if lc["lifecycle_status"] in ACTIVE_STATUSES)
    n_missing = sum(1 for lc in lifecycles if lc["lifecycle_status"] == "missing")
    n_rejected = sum(1 for lc in lifecycles if lc["lifecycle_status"] == "rejected")
    n_canceled = sum(1 for lc in lifecycles if lc["lifecycle_status"] == "canceled")
    n_expired = sum(1 for lc in lifecycles if lc["lifecycle_status"] == "expired")

    report: dict = {
        "run_id": run_id,
        "generated_at": generated_at,
        "dry_run": dry_run,
        "source": "stored_snapshot" if dry_run else "alpaca_paper",
        "clock": clock,
        "fetch_log": broker_lookup.get("fetch_log"),
        "orders_tracked": n_total,
        "orders_filled": n_filled,
        "orders_partially_filled": n_partially,
        "orders_active": n_active,
        "orders_missing": n_missing,
        "orders_rejected": n_rejected,
        "orders_canceled": n_canceled,
        "orders_expired": n_expired,
        "stale_orders": stale_orders,
        "warnings": warnings,
        "lifecycles": lifecycles,
        # Safety proof — these are always False in this module
        "safety": {
            "submit_order_called": False,
            "cancel_order_called": False,
            "replace_order_called": False,
        },
    }
    report["report_hash"] = stable_hash(
        {k: v for k, v in report.items() if k != "report_hash"}
    )

    # Commit updated audit files
    for audit_path, updated_audit in updated_audits:
        _write_json_atomic(audit_path, updated_audit)

    return report


# ---------------------------------------------------------------------------
# TRADE-LOG append
# ---------------------------------------------------------------------------

def append_trade_log(report: dict, log_path: Path) -> None:
    """Append a summary of the order monitor run to TRADE-LOG.md."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    if existing and not existing.endswith("\n"):
        existing += "\n"

    summary = {
        "run_id": report.get("run_id"),
        "generated_at": report.get("generated_at"),
        "dry_run": report.get("dry_run"),
        "source": report.get("source"),
        "orders_tracked": report.get("orders_tracked"),
        "orders_filled": report.get("orders_filled"),
        "orders_active": report.get("orders_active"),
        "orders_missing": report.get("orders_missing"),
        "orders_rejected": report.get("orders_rejected"),
        "stale_orders": report.get("stale_orders"),
        "warnings": report.get("warnings"),
        "lifecycles": [
            {
                "client_order_id": lc.get("client_order_id"),
                "symbol": lc.get("symbol"),
                "side": lc.get("side"),
                "notional": lc.get("notional"),
                "lifecycle_status": lc.get("lifecycle_status"),
                "fill": lc.get("fill"),
            }
            for lc in report.get("lifecycles", [])
        ],
    }
    block = (
        "\n## order_monitor run\n\n"
        "```json\n"
        + json.dumps(summary, indent=2, sort_keys=True, default=str)
        + "\n```\n"
    )
    log_path.write_text(existing + block, encoding="utf-8")
