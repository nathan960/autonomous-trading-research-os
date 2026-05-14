"""System status dashboard for Autonomous Trading Research OS.

Reads all available data/latest and config artifacts and produces a single
operator-readable status dict indicating whether the system is safe for:
  - research cycle
  - manual paper cycle (research_only)
  - manual paper cycle (paper_execution)
  - scheduled paper execution (always False — policy: requires manual confirm)

All functions are pure (no I/O, no side effects, no order submission).
The only output is the status dict returned by build_system_status().
"""
from __future__ import annotations

from typing import Optional

from ..hashing import stable_hash
from ..source_integrity import check_execution_snapshots
from ..time_utils import iso_age_minutes, utc_now_iso

SCHEMA_VERSION = "0.1.0"

STATUS_GREEN = "GREEN"
STATUS_YELLOW = "YELLOW"
STATUS_RED = "RED"

RISK_STATE_STALE_MINUTES = 120.0

# Gates that routinely fail outside market hours and are non-blocking for
# research; their failure should not alone cause RED status.
NON_CRITICAL_GATES: frozenset = frozenset({
    "MARKET_CLOCK_OPEN",
    "QUOTE_FRESHNESS",
    "SPREAD_NOT_TOO_WIDE",
})

# Gates whose failure is always a hard blocker regardless of market hours.
HARD_BLOCK_GATES: frozenset = frozenset({
    "CANONICAL_SOURCE_INTEGRITY",
    "TRADING_MODE_PAPER",
    "ALPACA_PAPER_MODE",
    "NO_PROHIBITED_ORDERS",
    "RISK_LIMITS_RESPECTED",
})


# ---------------------------------------------------------------------------
# Individual check functions — all pure, no I/O
# ---------------------------------------------------------------------------

def check_source_integrity(
    account_snapshot: dict,
    positions_snapshot: dict,
    orders_snapshot: dict,
    market_snapshot: dict,
) -> dict:
    """Return source integrity check over the four execution-critical snapshots."""
    result = check_execution_snapshots(
        account_snapshot=account_snapshot,
        positions_snapshot=positions_snapshot,
        orders_snapshot=orders_snapshot,
        market_snapshot=market_snapshot,
    )
    return {
        "passes": result["passes"],
        "failed": result["failed"],
        "checked": result["checked"],
    }


def check_risk_state(risk_state: dict, risk_limits: dict) -> dict:
    """Check risk state freshness, pause status, and drawdown thresholds."""
    paused = bool(risk_state.get("paused", False))
    drawdown = float(risk_state.get("drawdown", 0.0))
    updated_at = risk_state.get("updated_at", "")

    age = iso_age_minutes(updated_at)
    stale = age is None or age > RISK_STATE_STALE_MINUTES

    warn_threshold = float(risk_limits.get("max_drawdown_warn_pct", -0.05))
    block_threshold = float(risk_limits.get("max_drawdown_block_pct", -0.1))

    return {
        "passes": not paused and not stale and not (drawdown <= block_threshold),
        "paused": paused,
        "stale": stale,
        "stale_minutes": round(age, 1) if age is not None else None,
        "drawdown": drawdown,
        "drawdown_warn": drawdown <= warn_threshold,
        "drawdown_blocked": drawdown <= block_threshold,
        "peak_equity": risk_state.get("peak_equity"),
        "latest_equity": risk_state.get("latest_equity"),
        "updated_at": updated_at,
    }


def check_data_quality(data_quality_snapshot: dict) -> dict:
    """Check data quality status and surface any notable issues."""
    status = data_quality_snapshot.get("status", "unknown")
    issues = data_quality_snapshot.get("issues", [])
    wide_spreads = data_quality_snapshot.get("wide_spreads", {})
    missing_quotes = data_quality_snapshot.get("missing_quotes", [])
    missing_bars = data_quality_snapshot.get("missing_bars", [])
    not_tradable = data_quality_snapshot.get("not_tradable", [])

    passes = status not in ("ERROR", "CRITICAL")

    return {
        "passes": passes,
        "status": status,
        "issues": issues,
        "wide_spread_count": len(wide_spreads),
        "wide_spread_symbols": list(wide_spreads.keys()) if wide_spreads else [],
        "missing_quote_count": len(missing_quotes),
        "missing_bar_count": len(missing_bars),
        "not_tradable_count": len(not_tradable),
        "snapshot_age_minutes": data_quality_snapshot.get("snapshot_age_minutes"),
        "data_feed": data_quality_snapshot.get("data_feed"),
    }


def check_dry_run_gates(execution_report: dict) -> dict:
    """Classify execution gate results as hard failures, soft/market failures, or passing."""
    all_pass = bool(execution_report.get("all_gates_pass", False))
    failed = list(execution_report.get("failed_gates", []))
    status = execution_report.get("status", "unknown")

    hard_failures = [g for g in failed if g in HARD_BLOCK_GATES]
    soft_failures = [g for g in failed if g in NON_CRITICAL_GATES]
    other_failures = [g for g in failed if g not in HARD_BLOCK_GATES and g not in NON_CRITICAL_GATES]

    return {
        "passes": all_pass,
        "all_gates_pass": all_pass,
        "failed_gates": failed,
        "hard_failures": hard_failures,
        "soft_failures": soft_failures,
        "other_failures": other_failures,
        "has_hard_failures": bool(hard_failures or other_failures),
        "status": status,
        "generated_at": execution_report.get("generated_at"),
    }


def check_trade_plan(trade_plan: dict, execution_policy: dict) -> dict:
    """Check trade plan freshness, approval status, and order safety."""
    if not trade_plan:
        return {
            "passes": False,
            "missing": True,
            "plan_id": None,
            "is_approved": False,
            "is_expired": True,
            "is_stale": True,
            "proposed_order_count": 0,
            "proposed_orders": [],
            "non_limit_orders": [],
            "trading_mode": None,
        }

    plan_id = trade_plan.get("plan_id")
    expires_at = trade_plan.get("expires_at", "")
    generated_at = trade_plan.get("generated_at", "")
    approval = trade_plan.get("approval", {})
    is_approved = bool(approval.get("approved_for_execution"))

    expiry_age = iso_age_minutes(expires_at)
    is_expired = expiry_age is not None and expiry_age > 0

    plan_age = iso_age_minutes(generated_at)
    max_age = float(execution_policy.get("plan_max_age_minutes", 360))
    is_stale = plan_age is None or plan_age > max_age

    proposed_orders = trade_plan.get("proposed_orders", [])
    non_limit = [
        o.get("symbol", "?")
        for o in proposed_orders
        if o.get("skip_reason") is None and o.get("order_type") != "limit"
    ]

    return {
        "passes": not is_expired and not is_stale and not non_limit,
        "missing": False,
        "plan_id": plan_id,
        "is_approved": is_approved,
        "is_expired": is_expired,
        "is_stale": is_stale,
        "plan_age_minutes": round(plan_age, 1) if plan_age is not None else None,
        "proposed_order_count": len(proposed_orders),
        "proposed_orders": proposed_orders,
        "non_limit_orders": non_limit,
        "trading_mode": trade_plan.get("trading_mode"),
    }


def check_order_safety(orders_snapshot: dict, trade_plan: dict) -> dict:
    """Detect open orders that conflict with planned symbols."""
    proposed_symbols: set = {
        o["symbol"]
        for o in trade_plan.get("proposed_orders", [])
        if o.get("skip_reason") is None
    }
    open_orders = orders_snapshot.get("orders", [])
    conflicts = [o.get("symbol") for o in open_orders if o.get("symbol") in proposed_symbols]

    return {
        "passes": not conflicts,
        "has_duplicates": bool(conflicts),
        "conflict_symbols": conflicts,
        "open_order_count": orders_snapshot.get("open_order_count", 0),
    }


def check_execution_policy(risk_limits: dict, execution_policy: dict) -> dict:
    """Confirm paper-only policy is correctly configured."""
    violations: list = []
    if risk_limits.get("live_trading_allowed", False):
        violations.append("live_trading_allowed=true in risk_limits — CRITICAL")
    if execution_policy.get("allow_shorting", False):
        violations.append("allow_shorting=true in execution_policy")
    if execution_policy.get("allow_options", False):
        violations.append("allow_options=true in execution_policy")
    if execution_policy.get("allow_crypto", False):
        violations.append("allow_crypto=true in execution_policy")
    if not execution_policy.get("paper_only", True):
        violations.append("paper_only=false in execution_policy")

    return {
        "passes": not violations,
        "violations": violations,
        "live_trading_allowed": risk_limits.get("live_trading_allowed", False),
        "paper_only": execution_policy.get("paper_only", True),
        "allow_shorting": execution_policy.get("allow_shorting", False),
        "allow_options": execution_policy.get("allow_options", False),
        "allow_crypto": execution_policy.get("allow_crypto", False),
    }


# ---------------------------------------------------------------------------
# Summary builders — collapse snapshots to compact fields for the status doc
# ---------------------------------------------------------------------------

def _account_summary(
    account_snapshot: dict,
    positions_snapshot: dict,
    orders_snapshot: dict,
) -> dict:
    acct = account_snapshot.get("account", {})
    positions = positions_snapshot.get("positions", [])
    compact_positions = [
        {
            "symbol": p.get("symbol"),
            "qty": p.get("qty"),
            "market_value": p.get("market_value"),
            "unrealized_pl": p.get("unrealized_pl"),
            "avg_entry_price": p.get("avg_entry_price"),
            "current_price": p.get("current_price"),
        }
        for p in positions
    ]
    return {
        "latest_account_equity": _to_float(acct.get("equity")),
        "cash": _to_float(acct.get("cash")),
        "buying_power": _to_float(acct.get("buying_power")),
        "position_count": account_snapshot.get("position_count", 0),
        "open_order_count": account_snapshot.get("open_order_count", 0),
        "current_positions": compact_positions,
    }


def _outcome_summary(outcome_snapshot: dict) -> dict:
    outcomes = outcome_snapshot.get("outcomes", [])
    ok = [o for o in outcomes if o.get("source_integrity_status") == "ok"]
    returns = [o["current_return_pct"] for o in ok if o.get("current_return_pct") is not None]
    return {
        "outcomes_count": outcome_snapshot.get("outcomes_count", len(outcomes)),
        "source_integrity_status": outcome_snapshot.get("source_integrity_status", "unknown"),
        "avg_current_return_pct": round(sum(returns) / len(returns), 6) if returns else None,
        "tracked_symbols": [o.get("symbol") for o in outcomes if o.get("symbol")],
    }


def _lineage_summary(lineage_snapshot: dict) -> dict:
    return {
        "lineage_count": lineage_snapshot.get("lineage_count", 0),
        "complete_count": lineage_snapshot.get("complete_count", 0),
        "partial_count": lineage_snapshot.get("partial_count", 0),
        "generated_at": lineage_snapshot.get("generated_at"),
    }


def _trigger_performance_summary(trigger_performance: dict) -> dict:
    fill_outcomes = trigger_performance.get("fill_outcomes", {})
    regime = trigger_performance.get("regime", {})
    return {
        "status": trigger_performance.get("status", "unknown"),
        "days": trigger_performance.get("days"),
        "recommendation": fill_outcomes.get("recommendation"),
        "avg_current_return_pct": fill_outcomes.get("avg_current_return_pct"),
        "avg_slippage_pct": fill_outcomes.get("avg_slippage_pct"),
        "regime_category": regime.get("category"),
        "regime_recommendation": regime.get("recommendation"),
        "operational_issues": trigger_performance.get("operational_issues", []),
    }


def _order_lifecycle_summary(order_monitor_report: dict) -> dict:
    return {
        "orders_tracked": order_monitor_report.get("orders_tracked", 0),
        "orders_filled": order_monitor_report.get("orders_filled", 0),
        "orders_active": order_monitor_report.get("orders_active", 0),
        "orders_canceled": order_monitor_report.get("orders_canceled", 0),
        "orders_rejected": order_monitor_report.get("orders_rejected", 0),
        "orders_expired": order_monitor_report.get("orders_expired", 0),
        "stale_orders": order_monitor_report.get("stale_orders", []),
        "warnings": order_monitor_report.get("warnings", []),
        "safety": order_monitor_report.get("safety", {}),
    }


# ---------------------------------------------------------------------------
# Status determination
# ---------------------------------------------------------------------------

def _determine_status(checks: dict) -> tuple:
    """Return (overall_status, blocking_issues, warnings, required_operator_actions)."""
    blocking: list = []
    warnings_: list = []
    actions: list = []

    # ── Hard RED: source integrity ──────────────────────────────────────────
    if not checks["source_integrity"]["passes"]:
        failed_desc = [f"{c['name']}={c['source']!r}" for c in checks["source_integrity"]["failed"]]
        blocking.append(f"Source integrity failed — mock/unknown source: {failed_desc}")
        actions.append("Run refresh_data.py (without --dry-run) to overwrite mock snapshots with live data")

    # ── Hard RED: execution policy violations ──────────────────────────────
    if not checks["execution_policy"]["passes"]:
        for v in checks["execution_policy"]["violations"]:
            blocking.append(f"Execution policy violation: {v}")
        actions.append("Fix config/risk_limits.json and config/execution_policy.json — paper_only and no live trading")

    # ── Hard RED: drawdown block ────────────────────────────────────────────
    if checks["risk_state"]["drawdown_blocked"]:
        blocking.append(
            f"Drawdown {checks['risk_state']['drawdown']:.2%} breaches "
            f"block threshold — execution halted"
        )
        actions.append("Review drawdown. Reset risk state only after manual investigation.")

    # ── Hard RED: duplicate open orders ────────────────────────────────────
    if checks["order_safety"]["has_duplicates"]:
        blocking.append(f"Open duplicate orders for planned symbols: {checks['order_safety']['conflict_symbols']}")
        actions.append("Cancel or wait for existing open orders to settle before re-running")

    # ── RED/YELLOW: gate failures ───────────────────────────────────────────
    gate = checks["dry_run_gates"]
    if not gate["passes"]:
        if gate["hard_failures"]:
            blocking.append(f"Execution gates: hard failures: {gate['hard_failures']}")
            actions.append(f"Fix hard gate failures before any execution: {gate['hard_failures']}")
        if gate["other_failures"]:
            blocking.append(f"Execution gates: unexpected failures: {gate['other_failures']}")
            actions.append(f"Investigate gate failures: {gate['other_failures']}")
        if gate["soft_failures"] and not gate["hard_failures"] and not gate["other_failures"]:
            warnings_.append(f"Dry-run gates failed for market/timing reasons: {gate['soft_failures']}")

    # ── YELLOW: risk state ──────────────────────────────────────────────────
    if checks["risk_state"]["stale"]:
        warnings_.append(
            f"Risk state is stale ({checks['risk_state']['stale_minutes']}min old) — "
            "run monitor_positions.py"
        )
        actions.append("Run monitor_positions.py to refresh risk state")

    if checks["risk_state"]["paused"]:
        warnings_.append("Risk state is paused — execution blocked by risk monitor")
        actions.append("Review why risk state is paused before resuming")

    if checks["risk_state"]["drawdown_warn"] and not checks["risk_state"]["drawdown_blocked"]:
        warnings_.append(f"Drawdown {checks['risk_state']['drawdown']:.2%} is at warning threshold")

    # ── YELLOW: data quality ────────────────────────────────────────────────
    if not checks["data_quality"]["passes"]:
        warnings_.append(f"Data quality: {checks['data_quality']['status']} — {checks['data_quality']['issues']}")
        actions.append("Review data quality issues before paper execution")
    elif checks["data_quality"]["wide_spread_count"] > 0:
        warnings_.append(
            f"{checks['data_quality']['wide_spread_count']} wide-spread symbols "
            f"({checks['data_quality']['wide_spread_symbols']}) — SPREAD_NOT_TOO_WIDE may block execution"
        )

    # ── YELLOW: trade plan ──────────────────────────────────────────────────
    if checks["trade_plan"]["missing"]:
        warnings_.append("No trade plan found — run refresh_data → scan_triggers → generate_trade_plan")
        actions.append("Run full research cycle to generate a trade plan")
    elif checks["trade_plan"]["is_expired"]:
        warnings_.append("Trade plan has expired")
        actions.append("Re-run generate_trade_plan.py to refresh the plan")
    elif checks["trade_plan"]["is_stale"]:
        warnings_.append(f"Trade plan is stale ({checks['trade_plan']['plan_age_minutes']}min old)")
        actions.append("Re-run generate_trade_plan.py")

    if checks["trade_plan"]["non_limit_orders"]:
        warnings_.append(f"Non-limit orders in trade plan: {checks['trade_plan']['non_limit_orders']}")
        actions.append("Regenerate trade plan — only limit orders are allowed for paper execution")

    if blocking:
        return STATUS_RED, blocking, warnings_, actions
    if warnings_:
        return STATUS_YELLOW, blocking, warnings_, actions
    return STATUS_GREEN, blocking, warnings_, actions


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def build_system_status(snapshots: dict, configs: dict) -> dict:
    """Build a full system status report from loaded snapshots and configs.

    Args:
        snapshots: dict with keys matching data/latest filenames (snake_case, no .json):
            account_snapshot, positions_snapshot, orders_snapshot, market_snapshot,
            data_quality_snapshot, trigger_snapshot, trade_plan, execution_report,
            order_monitor_report, outcome_snapshot, lineage_snapshot, trigger_performance
        configs: dict with keys:
            risk_limits, strategy, execution_policy, risk_state

    Returns:
        Status dict ready to write to data/latest/system_status.json.
        Never raises — missing snapshots degrade gracefully to warnings.
    """
    # Unpack with safe defaults
    account_snap = snapshots.get("account_snapshot", {})
    positions_snap = snapshots.get("positions_snapshot", {})
    orders_snap = snapshots.get("orders_snapshot", {})
    market_snap = snapshots.get("market_snapshot", {})
    dq_snap = snapshots.get("data_quality_snapshot", {})
    trigger_snap = snapshots.get("trigger_snapshot", {})
    trade_plan = snapshots.get("trade_plan", {})
    exec_report = snapshots.get("execution_report", {})
    monitor_report = snapshots.get("order_monitor_report", {})
    outcome_snap = snapshots.get("outcome_snapshot", {})
    lineage_snap = snapshots.get("lineage_snapshot", {})
    tp_snap = snapshots.get("trigger_performance", {})

    risk_limits = configs.get("risk_limits", {})
    execution_policy = configs.get("execution_policy", {})
    risk_state = configs.get("risk_state", {})

    # Run all checks
    checks = {
        "source_integrity": check_source_integrity(account_snap, positions_snap, orders_snap, market_snap),
        "risk_state": check_risk_state(risk_state, risk_limits),
        "data_quality": check_data_quality(dq_snap),
        "dry_run_gates": check_dry_run_gates(exec_report),
        "trade_plan": check_trade_plan(trade_plan, execution_policy),
        "order_safety": check_order_safety(orders_snap, trade_plan),
        "execution_policy": check_execution_policy(risk_limits, execution_policy),
    }

    # Determine overall status
    overall_status, blocking, warnings, actions = _determine_status(checks)

    # Derive readiness flags
    source_ok = checks["source_integrity"]["passes"]
    policy_ok = checks["execution_policy"]["passes"]
    gates_pass = checks["dry_run_gates"]["all_gates_pass"]
    plan_approved = checks["trade_plan"]["is_approved"]
    no_hard_blockers = not blocking

    safe_for_research = source_ok and policy_ok and overall_status != STATUS_RED
    safe_for_paper_execution = (
        safe_for_research
        and gates_pass
        and plan_approved
        and not checks["order_safety"]["has_duplicates"]
        and not checks["risk_state"]["drawdown_blocked"]
        and overall_status == STATUS_GREEN
    )

    # Build summaries from available snapshots
    acct_summary = _account_summary(account_snap, positions_snap, orders_snap)
    tp_summary = _trigger_performance_summary(tp_snap)
    lifecycle_summary = _order_lifecycle_summary(monitor_report)
    outcome_sum = _outcome_summary(outcome_snap)
    lineage_sum = _lineage_summary(lineage_snap)

    # Alert / route counts from trigger snapshot and monitor report
    last_alert_count = len(trigger_snap.get("candidates", []))
    last_route_count = int(monitor_report.get("orders_tracked", 0))

    # Compact trade plan fields for the status doc
    plan_summary = {
        "latest_plan_id": checks["trade_plan"]["plan_id"],
        "trade_plan_approved_for_execution": checks["trade_plan"]["is_approved"],
        "proposed_order_count": checks["trade_plan"]["proposed_order_count"],
        "proposed_orders": [
            {
                "symbol": o.get("symbol"),
                "side": o.get("side"),
                "order_type": o.get("order_type"),
                "limit_price": o.get("limit_price"),
                "notional": o.get("notional"),
                "skip_reason": o.get("skip_reason"),
            }
            for o in checks["trade_plan"]["proposed_orders"]
        ],
    }

    generated_at = utc_now_iso()
    status_doc: dict = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": generated_at,

        # ── Overall readiness ──────────────────────────────────────────────
        "overall_status": overall_status,
        "safe_for_research_cycle": safe_for_research,
        "safe_for_manual_paper_execution": safe_for_paper_execution,
        "safe_for_scheduled_paper_execution": False,  # always — policy requires manual confirm

        # ── Issues and actions ─────────────────────────────────────────────
        "blocking_issues": blocking,
        "warnings": warnings,
        "required_operator_actions": actions,

        # ── Account state ──────────────────────────────────────────────────
        **acct_summary,

        # ── Trade plan ─────────────────────────────────────────────────────
        **plan_summary,

        # ── Execution gate state ───────────────────────────────────────────
        "dry_run_all_gates_pass": gates_pass,
        "failed_gates": checks["dry_run_gates"]["failed_gates"],

        # ── Data integrity ─────────────────────────────────────────────────
        "source_integrity_status": (
            "ok" if checks["source_integrity"]["passes"] else "failed"
        ),
        "data_quality_status": checks["data_quality"]["status"],

        # ── Summaries ──────────────────────────────────────────────────────
        "order_lifecycle_summary": lifecycle_summary,
        "outcome_summary": outcome_sum,
        "trigger_performance_summary": tp_summary,
        "lineage_status": lineage_sum,

        # ── Signals / alerts ───────────────────────────────────────────────
        "last_alert_count": last_alert_count,
        "last_route_count": last_route_count,

        # ── Risk state ─────────────────────────────────────────────────────
        "risk_state": {
            "drawdown": checks["risk_state"]["drawdown"],
            "drawdown_warn": checks["risk_state"]["drawdown_warn"],
            "drawdown_blocked": checks["risk_state"]["drawdown_blocked"],
            "paused": checks["risk_state"]["paused"],
            "stale": checks["risk_state"]["stale"],
            "updated_at": checks["risk_state"]["updated_at"],
            "latest_equity": checks["risk_state"]["latest_equity"],
            "peak_equity": checks["risk_state"]["peak_equity"],
        },
    }

    status_doc["status_hash"] = stable_hash(
        {k: v for k, v in status_doc.items() if k != "status_hash"}
    )
    return status_doc


# ---------------------------------------------------------------------------
# Markdown formatter
# ---------------------------------------------------------------------------

def format_status_markdown(status: dict) -> str:
    """Return a human-readable SYSTEM-STATUS.md entry for one status run."""
    ts = status.get("generated_at", "?")
    overall = status.get("overall_status", "?")
    research = "YES" if status.get("safe_for_research_cycle") else "NO"
    paper = "YES" if status.get("safe_for_manual_paper_execution") else "NO"
    sched = "NO (policy)"

    equity = status.get("latest_account_equity")
    equity_str = f"${equity:,.2f}" if equity is not None else "?"
    drawdown = status.get("risk_state", {}).get("drawdown", 0.0)
    pos = status.get("position_count", 0)
    open_ord = status.get("open_order_count", 0)
    gates = status.get("dry_run_all_gates_pass")
    failed = status.get("failed_gates", [])
    plan_id = status.get("latest_plan_id", "none")
    approved = status.get("trade_plan_approved_for_execution", False)

    blocking = status.get("blocking_issues", [])
    warnings_ = status.get("warnings", [])
    actions = status.get("required_operator_actions", [])

    lines = [
        f"## System Status — {ts}",
        "",
        f"**Overall:** {overall}  "
        f"| Research: {research}  "
        f"| Paper Execution: {paper}  "
        f"| Scheduled: {sched}",
        "",
        f"**Account:** equity={equity_str}  drawdown={drawdown:.2%}  "
        f"positions={pos}  open_orders={open_ord}",
        f"**Trade Plan:** {plan_id}  approved={approved}",
        f"**Dry-run gates:** {'PASS' if gates else 'FAIL'}  failed={failed}",
        "",
    ]

    if blocking:
        lines.append("**Blocking Issues:**")
        for b in blocking:
            lines.append(f"- {b}")
        lines.append("")

    if warnings_:
        lines.append("**Warnings:**")
        for w in warnings_:
            lines.append(f"- {w}")
        lines.append("")

    if actions:
        lines.append("**Required Operator Actions:**")
        for a in actions:
            lines.append(f"- [ ] {a}")
        lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _to_float(value) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
