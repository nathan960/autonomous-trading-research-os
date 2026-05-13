"""Research-only weekly review for Autonomous Trading Research OS.

Aggregates the last 7 days of history artifacts and produces:
  - data/history/runs/weekly_review-<date>-<hash8>.json
  - memory/WEEKLY-REVIEW.md  (append-only)
  - memory/EXPERIMENT-LOG.md (append-only, experiments only)

SAFETY:
  - No execution path.
  - Never calls execute_paper.py.
  - Never approves trade plans.
  - Never places orders.
  - Never modifies config/strategy.json or risk_limits.json.
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
# Internal helpers
# ---------------------------------------------------------------------------

def _load_json(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _date_nodash(date_str: str) -> str:
    return date_str.replace("-", "")


def _find_history_files(directory: Path, glob: str) -> list[Path]:
    if not directory.is_dir():
        return []
    return sorted(directory.glob(glob))


def _date_range(end_date_str: str, days: int) -> list[str]:
    """Return list of ISO date strings [end-days+1 .. end] inclusive."""
    end = date.fromisoformat(end_date_str)
    return [(end - timedelta(days=i)).isoformat() for i in range(days - 1, -1, -1)]


# ---------------------------------------------------------------------------
# Per-period collectors
# ---------------------------------------------------------------------------

def _aggregate_trigger_scans(history_dir: Path, dates: list[str]) -> dict:
    total_runs = 0
    risk_on_count = 0
    risk_off_count = 0
    candidate_counts: list[int] = []
    excluded_counts: list[int] = []
    regime_errors: list[str] = []

    for date_str in dates:
        triggers_file = history_dir / "triggers" / f"{date_str}.jsonl"
        if not triggers_file.exists():
            continue
        try:
            lines = triggers_file.read_text(encoding="utf-8").splitlines()
        except Exception:
            continue
        for line in lines:
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            total_runs += 1
            if d.get("risk_on"):
                risk_on_count += 1
            else:
                risk_off_count += 1
            cands = d.get("candidates", [])
            candidate_counts.append(len(cands))
            excluded_counts.append(d.get("excluded_count", 0))
            if d.get("regime_skip_reason"):
                regime_errors.append(d["regime_skip_reason"])

    avg_candidates = sum(candidate_counts) / len(candidate_counts) if candidate_counts else 0.0
    avg_excluded = sum(excluded_counts) / len(excluded_counts) if excluded_counts else 0.0
    return {
        "total_runs": total_runs,
        "risk_on_sessions": risk_on_count,
        "risk_off_sessions": risk_off_count,
        "avg_candidates": round(avg_candidates, 1),
        "avg_excluded": round(avg_excluded, 1),
        "regime_errors": regime_errors,
    }


def _aggregate_dry_runs(exec_dir: Path, dates: list[str]) -> dict:
    total = 0
    all_pass = 0
    fail = 0
    failing_gates: dict[str, int] = {}

    for date_str in dates:
        dn = _date_nodash(date_str)
        for f in _find_history_files(exec_dir, f"execution-{dn}T*_dry_run.json"):
            d = _load_json(f, {})
            if not d:
                continue
            total += 1
            if d.get("all_gates_pass"):
                all_pass += 1
            else:
                fail += 1
                for g in d.get("failed_gates", []):
                    failing_gates[g] = failing_gates.get(g, 0) + 1

    return {
        "total_runs": total,
        "all_pass_count": all_pass,
        "fail_count": fail,
        "failing_gates": dict(sorted(failing_gates.items(), key=lambda x: -x[1])),
    }


def _aggregate_paper_executions(exec_dir: Path, dates: list[str]) -> dict:
    total_attempts = 0
    total_orders = 0
    runs: list[dict] = []

    for date_str in dates:
        dn = _date_nodash(date_str)
        for f in _find_history_files(exec_dir, f"execution-{dn}T*_paper.json"):
            d = _load_json(f, {})
            if not d:
                continue
            total_attempts += 1
            submitted = d.get("orders_submitted", [])
            total_orders += len(submitted)
            runs.append({
                "run_id": d.get("run_id"),
                "date": date_str,
                "status": d.get("status"),
                "orders_count": len(submitted),
                "orders": [
                    {"symbol": o.get("symbol"), "side": o.get("side"),
                     "notional": o.get("notional"), "limit_price": o.get("limit_price")}
                    for o in submitted
                ],
            })

    return {
        "total_attempts": total_attempts,
        "total_orders_submitted": total_orders,
        "runs": runs,
    }


def _aggregate_order_monitor(orders_dir: Path, dates: list[str]) -> dict:
    """Aggregate order lifecycle across monitor runs, deduplicating by client_order_id.

    Each unique order is represented by its most recent lifecycle entry (latest
    checked_at). This prevents an order that was 'missing' in early runs and
    'filled' in a later run from being counted under both statuses.
    """
    total_runs = 0
    # {client_order_id: lifecycle_dict} — latest checked_at wins
    latest_by_order: dict = {}

    for date_str in dates:
        dn = _date_nodash(date_str)
        for f in _find_history_files(orders_dir, f"order_monitor-{dn}T*.json"):
            d = _load_json(f, {})
            if not d:
                continue
            total_runs += 1
            for lc in d.get("lifecycles", []):
                cid = lc.get("client_order_id")
                if not cid:
                    continue
                existing = latest_by_order.get(cid)
                if existing is None or (lc.get("checked_at") or "") > (existing.get("checked_at") or ""):
                    latest_by_order[cid] = lc

    def _count(status: str) -> int:
        return sum(1 for lc in latest_by_order.values() if lc.get("lifecycle_status") == status)

    latest_lifecycle_by_order = sorted(
        [
            {
                "client_order_id": lc.get("client_order_id"),
                "symbol": lc.get("symbol"),
                "side": lc.get("side"),
                "lifecycle_status": lc.get("lifecycle_status"),
                "fill_price": (lc.get("fill") or {}).get("fill_price"),
                "filled_qty": (lc.get("fill") or {}).get("filled_qty"),
                "filled_notional": (lc.get("fill") or {}).get("filled_notional"),
                "checked_at": lc.get("checked_at"),
            }
            for lc in latest_by_order.values()
        ],
        key=lambda x: x.get("checked_at") or "",
    )

    return {
        "total_runs": total_runs,
        "total_tracked": len(latest_by_order),
        "fills": _count("filled"),
        "partially_filled": _count("partially_filled"),
        "missing": _count("missing"),
        "expired": _count("expired"),
        "rejected": _count("rejected"),
        "canceled": _count("canceled"),
        "latest_lifecycle_by_order": latest_lifecycle_by_order,
    }


def _aggregate_alerts(alerts_dir: Path, dates: list[str]) -> dict:
    all_alerts = []
    period_alerts: list[dict] = []
    routes_dir = alerts_dir / "routes"

    for f in _find_history_files(alerts_dir, "alert-*.json"):
        d = _load_json(f, {})
        if not d:
            continue
        all_alerts.append(d)
        ingested = d.get("ingested_at", "")
        if any(ingested.startswith(ds) for ds in dates):
            period_alerts.append(d)

    by_next_step: dict[str, int] = {}
    by_source: dict[str, int] = {}
    for a in period_alerts:
        ns = a.get("next_step", "unknown")
        by_next_step[ns] = by_next_step.get(ns, 0) + 1
        src = a.get("source", "unknown")
        by_source[src] = by_source.get(src, 0) + 1

    # Routes
    total_routes = 0
    period_routes = 0
    by_action: dict[str, int] = {}
    execution_called_any = False
    approved_plan_any = False

    date_nodashes = {_date_nodash(ds) for ds in dates}
    for f in _find_history_files(routes_dir, "route_*.json"):
        d = _load_json(f, {})
        if not d:
            continue
        total_routes += 1
        routed_at = d.get("routed_at", "")
        if any(routed_at.startswith(ds) for ds in dates):
            period_routes += 1
        action = d.get("action_taken", "unknown")
        by_action[action] = by_action.get(action, 0) + 1
        if d.get("execution_called"):
            execution_called_any = True
        if d.get("approved_trade_plan_created"):
            approved_plan_any = True

    return {
        "total_alerts_all_time": len(all_alerts),
        "alerts_this_period": len(period_alerts),
        "by_next_step": by_next_step,
        "by_source": by_source,
        "total_routes_all_time": total_routes,
        "routes_this_period": period_routes,
        "by_action": by_action,
        "execution_called_any": execution_called_any,
        "approved_trade_plan_created_any": approved_plan_any,
    }


def _aggregate_data_quality(latest_dir: Path, history_dir: Path) -> dict:
    # Use only the latest DQ report (no history of DQ reports yet)
    rep = _load_json(latest_dir / "data_quality_report.json", {})
    if not rep:
        return {"available": False}
    return {
        "available": True,
        "latest_status": rep.get("status"),
        "latest_generated_at": rep.get("generated_at"),
        "issues_count": len(rep.get("issues", [])),
        "wide_spreads_count": len(rep.get("wide_spreads", [])),
        "missing_bars_count": len(rep.get("missing_bars", [])),
        "insufficient_bars_count": len(rep.get("insufficient_bars", [])),
    }


def _aggregate_risk_state(memory_dir: Path) -> dict:
    rs = _load_json(memory_dir / "RISK-STATE.json", {})
    return {
        "latest_equity": rs.get("latest_equity"),
        "peak_equity": rs.get("peak_equity"),
        "drawdown": rs.get("drawdown"),
        "position_count": rs.get("position_count"),
        "updated_at": rs.get("updated_at"),
    }


# ---------------------------------------------------------------------------
# Operational issue detection
# ---------------------------------------------------------------------------

def _identify_issues(review: dict) -> list[str]:
    issues = []

    dry = review.get("dry_runs", {})
    if dry.get("fail_count", 0) > 0:
        gates = dry.get("failing_gates", {})
        for gate, count in gates.items():
            issues.append(f"Dry-run gate {gate!r} failed {count} time(s) this period.")

    paper = review.get("paper_executions", {})
    for run in paper.get("runs", []):
        if run.get("status") not in ("PAPER_SUBMITTED", "DRY_RUN_SKIPPED", None):
            issues.append(f"Paper execution {run.get('run_id')} had unexpected status: {run.get('status')}")

    om = review.get("order_monitor", {})
    if om.get("missing", 0) > 0:
        issues.append(f"{om['missing']} order(s) have lifecycle_status=missing — verify on broker.")
    if om.get("rejected", 0) > 0:
        issues.append(f"{om['rejected']} order(s) were rejected.")

    alerts = review.get("alerts", {})
    if alerts.get("execution_called_any"):
        issues.append("SAFETY: execution_called=true found in a route record — investigate immediately.")
    if alerts.get("approved_trade_plan_created_any"):
        issues.append("SAFETY: approved_trade_plan_created=true found in a route record — investigate immediately.")

    dq = review.get("data_quality", {})
    if dq.get("latest_status") not in ("PASS", None):
        issues.append(f"Data quality check is {dq['latest_status']} — review data_quality_report.json.")

    rs = review.get("risk_state", {})
    drawdown = rs.get("drawdown")
    if drawdown is not None and drawdown < -0.05:
        issues.append(f"Drawdown is {drawdown:.1%} — approaching warning threshold (-5%).")

    return issues


def _generate_observations(review: dict) -> list[str]:
    obs = []

    ts = review.get("trigger_scans", {})
    if ts.get("total_runs", 0) > 0:
        risk_on_pct = ts.get("risk_on_sessions", 0) / ts["total_runs"]
        obs.append(
            f"Market regime: {ts['risk_on_sessions']}/{ts['total_runs']} sessions risk_on "
            f"({risk_on_pct:.0%}). Avg candidates={ts.get('avg_candidates')}, "
            f"avg excluded={ts.get('avg_excluded')}."
        )

    pe = review.get("paper_executions", {})
    if pe.get("total_attempts", 0) > 0:
        obs.append(
            f"{pe['total_attempts']} paper execution attempt(s), "
            f"{pe['total_orders_submitted']} order(s) submitted."
        )
    else:
        obs.append("No paper executions this period.")

    om = review.get("order_monitor", {})
    if om.get("fills", 0) > 0:
        obs.append(f"{om['fills']} order fill(s) confirmed by order monitor.")

    alerts = review.get("alerts", {})
    if alerts.get("alerts_this_period", 0) > 0:
        obs.append(
            f"{alerts['alerts_this_period']} external alert(s) ingested this period, "
            f"{alerts.get('routes_this_period', 0)} routed."
        )

    return obs


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build_weekly_review(
    end_date_str: Optional[str] = None,
    days: int = 7,
    latest_dir: Optional[Path] = None,
    history_dir: Optional[Path] = None,
    memory_dir: Optional[Path] = None,
) -> dict:
    """Collect and return the weekly review dict. No I/O side effects."""
    if end_date_str is None:
        end_date_str = date.today().isoformat()
    if latest_dir is None:
        latest_dir = LATEST_DIR
    if history_dir is None:
        history_dir = HISTORY_DIR
    if memory_dir is None:
        memory_dir = MEMORY_DIR

    latest_dir = Path(latest_dir)
    history_dir = Path(history_dir)
    memory_dir = Path(memory_dir)

    dates = _date_range(end_date_str, days)
    period_start = dates[0]
    exec_dir = history_dir / "executions"
    orders_dir = history_dir / "orders"
    alerts_dir = history_dir / "alerts"

    review: dict = {
        "run_id": f"weekly_review-{end_date_str}",
        "period_start": period_start,
        "period_end": end_date_str,
        "days": days,
        "generated_at": utc_now_iso(),
        "status": "ok",
        "trigger_scans": _aggregate_trigger_scans(history_dir, dates),
        "dry_runs": _aggregate_dry_runs(exec_dir, dates),
        "paper_executions": _aggregate_paper_executions(exec_dir, dates),
        "order_monitor": _aggregate_order_monitor(orders_dir, dates),
        "alerts": _aggregate_alerts(alerts_dir, dates),
        "data_quality": _aggregate_data_quality(latest_dir, history_dir),
        "risk_state": _aggregate_risk_state(memory_dir),
    }

    review["operational_issues"] = _identify_issues(review)
    review["research_observations"] = _generate_observations(review)

    # Proposed experiments are written to EXPERIMENT-LOG.md only; not in JSON
    review["proposed_experiments"] = []

    review["review_hash"] = stable_hash(review)[:16]
    return review


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def format_weekly_review_md(review: dict) -> str:
    lines = [
        f"## Weekly Review — {review.get('period_start')} to {review.get('period_end')} "
        f"({review.get('days')} days)",
        "",
        f"**Generated:** {review.get('generated_at')}  "
        f"**Run ID:** {review.get('run_id')}",
        "",
    ]

    # Trigger scans
    ts = review.get("trigger_scans", {})
    lines += [
        "### Trigger Scans",
        f"- Total runs: {ts.get('total_runs', 0)} | "
        f"Risk-on: {ts.get('risk_on_sessions', 0)} | "
        f"Risk-off: {ts.get('risk_off_sessions', 0)}",
        f"- Avg candidates: {ts.get('avg_candidates', 0)} | "
        f"Avg excluded: {ts.get('avg_excluded', 0)}",
    ]
    if ts.get("regime_errors"):
        lines.append(f"- Regime errors: {ts['regime_errors']}")
    lines.append("")

    # Dry runs
    dr = review.get("dry_runs", {})
    lines += [
        "### Dry Runs",
        f"- Total: {dr.get('total_runs', 0)} | "
        f"Pass: {dr.get('all_pass_count', 0)} | "
        f"Fail: {dr.get('fail_count', 0)}",
    ]
    if dr.get("failing_gates"):
        for gate, count in dr["failing_gates"].items():
            lines.append(f"  - {gate}: {count}x")
    lines.append("")

    # Paper executions
    pe = review.get("paper_executions", {})
    lines += [
        "### Paper Executions",
        f"- Attempts: {pe.get('total_attempts', 0)} | "
        f"Orders submitted: {pe.get('total_orders_submitted', 0)}",
    ]
    for run in pe.get("runs", []):
        for o in run.get("orders", []):
            lines.append(
                f"  - [{run.get('date')}] {o.get('symbol')} {(o.get('side') or '').upper()} "
                f"${o.get('notional')} @ ${o.get('limit_price')} ({run.get('status')})"
            )
    lines.append("")

    # Order monitor
    om = review.get("order_monitor", {})
    lines += [
        "### Order Lifecycle",
        f"- Monitor runs: {om.get('total_runs', 0)} | "
        f"Unique orders: {om.get('total_tracked', 0)}",
        f"- Fills: {om.get('fills', 0)} | "
        f"Partial: {om.get('partially_filled', 0)} | "
        f"Missing: {om.get('missing', 0)} | "
        f"Expired: {om.get('expired', 0)} | "
        f"Rejected: {om.get('rejected', 0)} | "
        f"Canceled: {om.get('canceled', 0)}",
    ]
    orders_list = om.get("latest_lifecycle_by_order", [])
    if orders_list:
        lines.append(f"- Latest lifecycle by order ({len(orders_list)}):")
        for o in orders_list:
            fill_price = o.get("fill_price")
            filled_qty = o.get("filled_qty")
            filled_notional = o.get("filled_notional")
            fill_str = (
                f" fill=${fill_price} qty={filled_qty} notional=${filled_notional}"
                if fill_price is not None else ""
            )
            lines.append(
                f"  - {o.get('client_order_id')} | {o.get('symbol')} {o.get('side')} | "
                f"status={o.get('lifecycle_status')}{fill_str} | "
                f"checked={o.get('checked_at')}"
            )
    lines.append("")

    # Alerts
    al = review.get("alerts", {})
    lines += [
        "### External Alerts",
        f"- Ingested this period: {al.get('alerts_this_period', 0)} "
        f"(all-time: {al.get('total_alerts_all_time', 0)})",
        f"- Routes this period: {al.get('routes_this_period', 0)} "
        f"(all-time: {al.get('total_routes_all_time', 0)})",
        f"- Execution called (ever): {'**YES — INVESTIGATE**' if al.get('execution_called_any') else 'NO'}",
        f"- Approved plan created (ever): {'**YES — INVESTIGATE**' if al.get('approved_trade_plan_created_any') else 'NO'}",
    ]
    if al.get("by_next_step"):
        lines.append("- By next_step: " + ", ".join(f"{k}={v}" for k, v in al["by_next_step"].items()))
    lines.append("")

    # Risk state
    rs = review.get("risk_state", {})
    eq = rs.get("latest_equity") or 0
    peak = rs.get("peak_equity") or 0
    dd = rs.get("drawdown") or 0
    lines += [
        "### Risk State",
        f"- Equity: ${eq:,.2f} | Peak: ${peak:,.2f} | "
        f"Drawdown: {dd:.2%} | Positions: {rs.get('position_count', 0)}",
        f"- Last updated: {rs.get('updated_at', '?')}",
        "",
    ]

    # Operational issues
    issues = review.get("operational_issues", [])
    lines.append(f"### Operational Issues ({len(issues)})")
    if issues:
        for issue in issues:
            lines.append(f"- {issue}")
    else:
        lines.append("None identified.")
    lines.append("")

    # Research observations
    obs = review.get("research_observations", [])
    lines.append("### Research Observations")
    if obs:
        for o in obs:
            lines.append(f"- {o}")
    else:
        lines.append("None.")
    lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def _format_experiment_log_entry(review: dict) -> Optional[str]:
    """Return an EXPERIMENT-LOG.md entry if there are items to note, else None."""
    issues = review.get("operational_issues", [])
    obs = review.get("research_observations", [])
    if not issues and not obs:
        return None

    lines = [
        f"## Experiment Candidates — {review.get('period_end')}",
        "",
        f"*From weekly review run {review.get('run_id')}*",
        "",
    ]

    if issues:
        lines.append("**Operational issues to investigate:**")
        for issue in issues:
            lines.append(f"- [ ] {issue}")
        lines.append("")

    if obs:
        lines.append("**Observations (hypothesis candidates):**")
        for o in obs:
            lines.append(f"- {o}")
        lines.append("")

    lines += [
        "**To propose a strategy experiment, open a PR with:**",
        "- Hypothesis",
        "- Supporting evidence (backtest or paper results)",
        "- Success criteria",
        "- Rollback plan",
        "",
        "---",
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Write
# ---------------------------------------------------------------------------

def write_weekly_review(
    review: dict,
    runs_dir: Optional[Path] = None,
    memory_dir: Optional[Path] = None,
) -> dict:
    """Write JSON and markdown outputs. Returns paths written."""
    if runs_dir is None:
        runs_dir = HISTORY_DIR / "runs"
    if memory_dir is None:
        memory_dir = MEMORY_DIR

    runs_dir = Path(runs_dir)
    memory_dir = Path(memory_dir)
    runs_dir.mkdir(parents=True, exist_ok=True)
    memory_dir.mkdir(parents=True, exist_ok=True)

    end_date = review.get("period_end", "unknown")
    hash8 = (review.get("review_hash") or "00000000")[:8]
    json_filename = f"weekly_review-{end_date}-{hash8}.json"
    json_path = runs_dir / json_filename

    text = json.dumps(review, indent=2, sort_keys=True, default=str)
    tmp = json_path.with_suffix(".json.tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(json_path)

    md_path = memory_dir / "WEEKLY-REVIEW.md"
    md_content = format_weekly_review_md(review)
    with md_path.open("a", encoding="utf-8") as fh:
        fh.write(md_content)

    experiment_entry = _format_experiment_log_entry(review)
    exp_path = memory_dir / "EXPERIMENT-LOG.md"
    if experiment_entry:
        with exp_path.open("a", encoding="utf-8") as fh:
            fh.write(experiment_entry)

    return {
        "json_path": str(json_path),
        "md_path": str(md_path),
        "experiment_log_path": str(exp_path) if experiment_entry else None,
    }
