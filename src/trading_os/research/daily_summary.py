"""Research-only daily summary for Autonomous Trading Research OS.

Reads data/latest and data/history artifacts and produces:
  - data/history/runs/daily_summary-<date>-<hash8>.json
  - memory/DAILY-SUMMARY.md  (append-only)

SAFETY:
  - No execution path.
  - Never calls execute_paper.py.
  - Never approves trade plans.
  - Never places orders.
  - Never modifies config or strategy.
"""
from __future__ import annotations

import json
from datetime import date, timezone
from pathlib import Path
from typing import Any, Optional

from ..config import HISTORY_DIR, LATEST_DIR, MEMORY_DIR
from ..hashing import stable_hash
from ..time_utils import utc_now_iso


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _load_json(path: Path, default: Any = None) -> Any:
    """Load JSON; return default on any error."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _date_nodash(date_str: str) -> str:
    """'2026-05-13' → '20260513'."""
    return date_str.replace("-", "")


def _find_history_files(directory: Path, glob: str) -> list[Path]:
    """Sorted list of matching paths; empty list if dir absent."""
    if not directory.is_dir():
        return []
    return sorted(directory.glob(glob))


# ---------------------------------------------------------------------------
# Per-section collectors
# ---------------------------------------------------------------------------

def _collect_account(latest_dir: Path) -> dict:
    snap = _load_json(latest_dir / "account_snapshot.json", {})
    acct = snap.get("account", snap)
    return {
        "equity": _float(acct.get("equity") or acct.get("portfolio_value")),
        "cash": _float(acct.get("cash")),
        "buying_power": _float(acct.get("buying_power")),
        "position_count": acct.get("position_count") or snap.get("position_count"),
        "fetched_at": snap.get("fetched_at") or acct.get("fetched_at"),
        "source": snap.get("source"),
    }


def _float(v: Any) -> Optional[float]:
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _collect_risk_state(memory_dir: Path) -> dict:
    rs = _load_json(memory_dir / "RISK-STATE.json", {})
    return {
        "latest_equity": rs.get("latest_equity"),
        "peak_equity": rs.get("peak_equity"),
        "drawdown": rs.get("drawdown"),
        "position_count": rs.get("position_count"),
        "updated_at": rs.get("updated_at"),
    }


def _collect_positions(latest_dir: Path) -> list[dict]:
    snap = _load_json(latest_dir / "positions_snapshot.json", {})
    out = []
    for p in snap.get("positions", []):
        out.append({
            "symbol": p.get("symbol"),
            "side": p.get("side"),
            "qty": p.get("qty"),
            "market_value": _float(p.get("market_value")),
            "unrealized_pl": _float(p.get("unrealized_pl")),
            "unrealized_plpc": _float(p.get("unrealized_plpc")),
            "avg_entry_price": _float(p.get("avg_entry_price")),
        })
    return out


def _collect_open_orders(latest_dir: Path) -> list[dict]:
    snap = _load_json(latest_dir / "orders_snapshot.json", {})
    out = []
    for o in snap.get("orders", []):
        out.append({
            "symbol": o.get("symbol"),
            "side": o.get("side"),
            "order_type": o.get("order_type") or o.get("type"),
            "limit_price": _float(o.get("limit_price")),
            "notional": _float(o.get("notional")),
            "status": o.get("status"),
            "client_order_id": o.get("client_order_id"),
        })
    return out


def _collect_trigger_scan(latest_dir: Path) -> dict:
    snap = _load_json(latest_dir / "trigger_snapshot.json", {})
    if not snap:
        return {"available": False}
    regime = snap.get("regime", {})
    spy = regime.get("spy_signals", {})
    breadth = regime.get("breadth", {})
    return {
        "available": True,
        "scanned_at": snap.get("scanned_at"),
        "risk_on": regime.get("risk_on"),
        "spy_close": spy.get("latest_close"),
        "spy_200dma": spy.get("sma"),
        "spy_passes_200dma": spy.get("passes_200dma"),
        "spy_6m_roc": spy.get("roc"),
        "breadth_pct": breadth.get("breadth"),
        "breadth_ok": breadth.get("breadth_ok"),
        "candidates_count": len(snap.get("candidates", [])),
        "selected_count": len(snap.get("selected", [])),
        "excluded_count": len(snap.get("excluded", [])),
    }


def _collect_trade_plan(latest_dir: Path) -> dict:
    plan = _load_json(latest_dir / "trade_plan.json", {})
    if not plan:
        return {"available": False}
    approval = plan.get("approval", {})
    orders = [
        {
            "symbol": o.get("symbol"),
            "side": o.get("side"),
            "order_type": o.get("order_type"),
            "limit_price": o.get("limit_price"),
            "notional": o.get("notional"),
            "time_in_force": o.get("time_in_force"),
            "would_short": o.get("would_short"),
        }
        for o in plan.get("proposed_orders", [])
        if o.get("skip_reason") is None
    ]
    risk_checks = plan.get("risk_checks", [])
    failed_checks = [c["check_id"] for c in risk_checks if not c.get("passes")]
    return {
        "available": True,
        "plan_id": plan.get("plan_id"),
        "generated_at": plan.get("generated_at"),
        "expires_at": plan.get("expires_at"),
        "trading_mode": plan.get("trading_mode"),
        "approved_for_execution": approval.get("approved_for_execution"),
        "approve_paper_flag": approval.get("approve_paper_flag"),
        "approval_reason": approval.get("reason"),
        "all_risk_checks_pass": approval.get("all_risk_checks_pass"),
        "failed_risk_checks": failed_checks,
        "proposed_orders_count": len(orders),
        "proposed_orders": orders,
        "blocked_symbols_count": len(plan.get("blocked_symbols", [])),
    }


def _collect_execution_report(latest_dir: Path) -> dict:
    rep = _load_json(latest_dir / "execution_report.json", {})
    if not rep:
        return {"available": False}
    return {
        "available": True,
        "run_id": rep.get("run_id"),
        "generated_at": rep.get("generated_at"),
        "dry_run": rep.get("dry_run"),
        "all_gates_pass": rep.get("all_gates_pass"),
        "failed_gates": rep.get("failed_gates", []),
        "status": rep.get("status"),
        "orders_submitted_count": len(rep.get("orders_submitted", [])),
    }


def _collect_dry_runs(exec_dir: Path, date_nodash: str) -> dict:
    files = _find_history_files(exec_dir, f"execution-{date_nodash}T*_dry_run.json")
    runs = []
    for f in files:
        d = _load_json(f, {})
        if d:
            runs.append({
                "run_id": d.get("run_id"),
                "all_gates_pass": d.get("all_gates_pass"),
                "failed_gates": d.get("failed_gates", []),
                "status": d.get("status"),
            })
    failing_gates: dict[str, int] = {}
    for r in runs:
        for g in r.get("failed_gates") or []:
            failing_gates[g] = failing_gates.get(g, 0) + 1
    latest = runs[-1] if runs else None
    return {
        "count": len(runs),
        "all_pass_count": sum(1 for r in runs if r.get("all_gates_pass")),
        "fail_count": sum(1 for r in runs if not r.get("all_gates_pass")),
        "failing_gates": failing_gates,
        "latest": latest,
    }


def _collect_paper_executions(exec_dir: Path, date_nodash: str) -> dict:
    files = _find_history_files(exec_dir, f"execution-{date_nodash}T*_paper.json")
    runs = []
    for f in files:
        d = _load_json(f, {})
        if d:
            runs.append({
                "run_id": d.get("run_id"),
                "status": d.get("status"),
                "orders_submitted": d.get("orders_submitted", []),
            })
    total_submitted = sum(len(r.get("orders_submitted", [])) for r in runs)
    return {
        "count": len(runs),
        "total_orders_submitted": total_submitted,
        "runs": runs,
    }


def _collect_order_monitor(latest_dir: Path, orders_dir: Path, date_nodash: str) -> dict:
    # Latest report
    rep = _load_json(latest_dir / "order_monitor_report.json", {})
    today_files = _find_history_files(orders_dir, f"order_monitor-{date_nodash}T*.json")
    return {
        "available": bool(rep),
        "latest_run_id": rep.get("run_id"),
        "generated_at": rep.get("generated_at"),
        "orders_tracked": rep.get("orders_tracked", 0),
        "orders_filled": rep.get("orders_filled", 0),
        "orders_missing": rep.get("orders_missing", 0),
        "orders_expired": rep.get("orders_expired", 0),
        "orders_rejected": rep.get("orders_rejected", 0),
        "orders_canceled": rep.get("orders_canceled", 0),
        "orders_active": rep.get("orders_active", 0),
        "runs_today": len(today_files),
    }


def _collect_alerts(alerts_dir: Path, date_str: str) -> dict:
    all_files = _find_history_files(alerts_dir, "alert-*.json")
    all_alerts = []
    today_alerts = []
    for f in all_files:
        d = _load_json(f, {})
        if not d:
            continue
        all_alerts.append(d)
        ingested_at = d.get("ingested_at", "")
        if ingested_at.startswith(date_str):
            today_alerts.append(d)

    by_next_step: dict[str, int] = {}
    by_source: dict[str, int] = {}
    for a in all_alerts:
        ns = a.get("next_step", "unknown")
        by_next_step[ns] = by_next_step.get(ns, 0) + 1
        src = a.get("source", "unknown")
        by_source[src] = by_source.get(src, 0) + 1

    return {
        "total_count": len(all_alerts),
        "ingested_today": len(today_alerts),
        "by_next_step": by_next_step,
        "by_source": by_source,
    }


def _collect_routes(routes_dir: Path, date_nodash: str) -> dict:
    all_files = _find_history_files(routes_dir, "route_*.json")
    today_files = _find_history_files(routes_dir, f"route_{date_nodash}T*.json")

    by_action: dict[str, int] = {}
    execution_called_any = False
    approved_plan_any = False
    for f in all_files:
        d = _load_json(f, {})
        if not d:
            continue
        action = d.get("action_taken", "unknown")
        by_action[action] = by_action.get(action, 0) + 1
        if d.get("execution_called"):
            execution_called_any = True
        if d.get("approved_trade_plan_created"):
            approved_plan_any = True

    return {
        "total_routes": len(all_files),
        "routes_today": len(today_files),
        "by_action": by_action,
        "execution_called_any": execution_called_any,
        "approved_trade_plan_created_any": approved_plan_any,
    }


def _collect_data_quality(latest_dir: Path) -> dict:
    rep = _load_json(latest_dir / "data_quality_report.json", {})
    if not rep:
        return {"available": False}
    return {
        "available": True,
        "status": rep.get("status"),
        "generated_at": rep.get("generated_at"),
        "issues_count": len(rep.get("issues", [])),
        "wide_spreads_count": len(rep.get("wide_spreads", [])),
        "missing_bars_count": len(rep.get("missing_bars", [])),
        "insufficient_bars_count": len(rep.get("insufficient_bars", [])),
        "missing_quotes_count": len(rep.get("missing_quotes", [])),
    }


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build_daily_summary(
    date_str: Optional[str] = None,
    latest_dir: Optional[Path] = None,
    history_dir: Optional[Path] = None,
    memory_dir: Optional[Path] = None,
) -> dict:
    """Collect and return the daily summary dict. No I/O side effects."""
    if date_str is None:
        date_str = date.today().isoformat()
    if latest_dir is None:
        latest_dir = LATEST_DIR
    if history_dir is None:
        history_dir = HISTORY_DIR
    if memory_dir is None:
        memory_dir = MEMORY_DIR

    latest_dir = Path(latest_dir)
    history_dir = Path(history_dir)
    memory_dir = Path(memory_dir)

    date_nodash = _date_nodash(date_str)
    exec_dir = history_dir / "executions"
    orders_dir = history_dir / "orders"
    alerts_dir = history_dir / "alerts"
    routes_dir = alerts_dir / "routes"

    summary: dict = {
        "run_id": f"daily_summary-{date_str}",
        "date": date_str,
        "generated_at": utc_now_iso(),
        "status": "ok",
        "account": _collect_account(latest_dir),
        "risk_state": _collect_risk_state(memory_dir),
        "positions": _collect_positions(latest_dir),
        "open_orders": _collect_open_orders(latest_dir),
        "trigger_scan": _collect_trigger_scan(latest_dir),
        "trade_plan": _collect_trade_plan(latest_dir),
        "execution_report": _collect_execution_report(latest_dir),
        "dry_runs": _collect_dry_runs(exec_dir, date_nodash),
        "paper_executions": _collect_paper_executions(exec_dir, date_nodash),
        "order_monitor": _collect_order_monitor(latest_dir, orders_dir, date_nodash),
        "alerts": _collect_alerts(alerts_dir, date_str),
        "alert_routes": _collect_routes(routes_dir, date_nodash),
        "data_quality": _collect_data_quality(latest_dir),
    }

    # Derive hash last
    summary["summary_hash"] = stable_hash(summary)[:16]
    return summary


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def _fmt_money(v: Optional[float]) -> str:
    if v is None:
        return "?"
    return f"${v:,.2f}"


def _fmt_pct(v: Optional[float]) -> str:
    if v is None:
        return "?"
    return f"{v * 100:.2f}%"


def format_daily_summary_md(summary: dict) -> str:
    """Return the markdown string for DAILY-SUMMARY.md."""
    lines = [
        f"## Daily Summary — {summary.get('date', '?')}",
        "",
        f"**Generated:** {summary.get('generated_at', '?')}  "
        f"**Run ID:** {summary.get('run_id', '?')}",
        "",
    ]

    # Account / risk
    acct = summary.get("account", {})
    rs = summary.get("risk_state", {})
    lines += [
        "### Account & Risk",
        f"- Equity: {_fmt_money(_float(acct.get('equity')))} | "
        f"Cash: {_fmt_money(_float(acct.get('cash')))} | "
        f"Buying power: {_fmt_money(_float(acct.get('buying_power')))}",
        f"- Peak: {_fmt_money(_float(rs.get('peak_equity')))} | "
        f"Drawdown: {_fmt_pct(_float(rs.get('drawdown')))} | "
        f"Positions: {rs.get('position_count', '?')}",
        "",
    ]

    # Positions
    positions = summary.get("positions", [])
    lines.append(f"### Positions ({len(positions)})")
    if positions:
        lines.append("| Symbol | Side | Qty | Market Value | Unrealized P/L |")
        lines.append("|--------|------|-----|--------------|----------------|")
        for p in positions:
            pl = p.get("unrealized_pl")
            pl_pct = p.get("unrealized_plpc")
            pl_str = f"+{_fmt_money(pl)} ({_fmt_pct(pl_pct)})" if pl and pl >= 0 else f"{_fmt_money(pl)} ({_fmt_pct(pl_pct)})"
            lines.append(
                f"| {p.get('symbol')} | {p.get('side')} | {p.get('qty')} | "
                f"{_fmt_money(_float(p.get('market_value')))} | {pl_str} |"
            )
    else:
        lines.append("None.")
    lines.append("")

    # Open orders
    open_orders = summary.get("open_orders", [])
    lines.append(f"### Open Orders ({len(open_orders)})")
    if open_orders:
        for o in open_orders:
            lines.append(
                f"- {o.get('symbol')} {o.get('side').upper()} "
                f"{_fmt_money(_float(o.get('notional')))} @ {_fmt_money(_float(o.get('limit_price')))} "
                f"({o.get('order_type')}) status={o.get('status')}"
            )
    else:
        lines.append("None.")
    lines.append("")

    # Trigger scan
    ts = summary.get("trigger_scan", {})
    if ts.get("available"):
        regime_str = "RISK_ON" if ts.get("risk_on") else "RISK_OFF"
        roc_str = f"+{ts['spy_6m_roc']:.2%}" if ts.get("spy_6m_roc") else "?"
        lines += [
            "### Trigger Scan",
            f"- Regime: **{regime_str}** (SPY 200DMA={'✓' if ts.get('spy_passes_200dma') else '✗'}, "
            f"6m ROC={roc_str}, breadth={_fmt_pct(ts.get('breadth_pct'))})",
            f"- Candidates: {ts.get('candidates_count')} | "
            f"Selected: {ts.get('selected_count')} | "
            f"Excluded: {ts.get('excluded_count')}",
            f"- Scanned at: {ts.get('scanned_at', '?')}",
            "",
        ]
    else:
        lines += ["### Trigger Scan", "No snapshot available.", ""]

    # Trade plan
    tp = summary.get("trade_plan", {})
    if tp.get("available"):
        approved = tp.get("approved_for_execution")
        approved_str = "**YES**" if approved else "NO"
        lines += [
            "### Trade Plan",
            f"- Plan ID: `{tp.get('plan_id')}`",
            f"- Generated: {tp.get('generated_at')} | Expires: {tp.get('expires_at')}",
            f"- Approved for execution: {approved_str} | Reason: {tp.get('approval_reason')}",
            f"- All risk checks pass: {'YES' if tp.get('all_risk_checks_pass') else 'NO'}",
        ]
        if tp.get("failed_risk_checks"):
            lines.append(f"- Failed checks: {', '.join(tp['failed_risk_checks'])}")
        orders = tp.get("proposed_orders", [])
        if orders:
            lines.append(f"- Proposed orders ({len(orders)}):")
            for o in orders:
                lines.append(
                    f"  - {o.get('symbol')} {o.get('side').upper()} "
                    f"{_fmt_money(_float(o.get('notional')))} @ {_fmt_money(_float(o.get('limit_price')))} "
                    f"({o.get('order_type')}, {o.get('time_in_force')})"
                )
        else:
            lines.append("- No proposed orders.")
        lines.append("")
    else:
        lines += ["### Trade Plan", "No trade plan available.", ""]

    # Execution report (latest dry-run)
    er = summary.get("execution_report", {})
    if er.get("available"):
        lines += [
            "### Latest Execution Report (Dry Run)",
            f"- Run ID: `{er.get('run_id')}`",
            f"- All gates pass: {'YES' if er.get('all_gates_pass') else 'NO'}",
        ]
        if er.get("failed_gates"):
            lines.append(f"- Failed gates: {', '.join(er['failed_gates'])}")
        lines.append("")

    # Dry runs today
    dr = summary.get("dry_runs", {})
    lines += [
        f"### Dry Runs Today ({dr.get('count', 0)})",
        f"- Pass: {dr.get('all_pass_count', 0)} | Fail: {dr.get('fail_count', 0)}",
    ]
    if dr.get("failing_gates"):
        for gate, count in dr["failing_gates"].items():
            lines.append(f"  - {gate}: {count}x")
    lines.append("")

    # Paper executions
    pe = summary.get("paper_executions", {})
    lines.append(f"### Paper Executions Today ({pe.get('count', 0)})")
    for run in pe.get("runs", []):
        for o in run.get("orders_submitted", []):
            lines.append(
                f"- {o.get('symbol')} {o.get('side', '').upper()} "
                f"{_fmt_money(_float(o.get('notional')))} @ {_fmt_money(_float(o.get('limit_price')))} "
                f"({run.get('status')}) submitted={o.get('submitted_at')}"
            )
    if not pe.get("runs"):
        lines.append("None today.")
    lines.append("")

    # Order monitor
    om = summary.get("order_monitor", {})
    lines += [
        "### Order Monitor",
        f"- Tracked: {om.get('orders_tracked', 0)} | "
        f"Filled: {om.get('orders_filled', 0)} | "
        f"Missing: {om.get('orders_missing', 0)} | "
        f"Expired: {om.get('orders_expired', 0)} | "
        f"Rejected: {om.get('orders_rejected', 0)} | "
        f"Active: {om.get('orders_active', 0)}",
        f"- Runs today: {om.get('runs_today', 0)} | "
        f"Latest: {om.get('latest_run_id', 'N/A')}",
        "",
    ]

    # Alerts
    al = summary.get("alerts", {})
    lines += [
        f"### Alerts (total={al.get('total_count', 0)}, today={al.get('ingested_today', 0)})",
    ]
    if al.get("by_source"):
        lines.append("- By source: " + ", ".join(f"{k}={v}" for k, v in al["by_source"].items()))
    if al.get("by_next_step"):
        lines.append("- By next_step: " + ", ".join(f"{k}={v}" for k, v in al["by_next_step"].items()))
    lines.append("")

    # Alert routes
    ar = summary.get("alert_routes", {})
    lines += [
        f"### Alert Routes (total={ar.get('total_routes', 0)}, today={ar.get('routes_today', 0)})",
        f"- Execution called (ever): {'**YES — INVESTIGATE**' if ar.get('execution_called_any') else 'NO'}",
        f"- Approved plan created (ever): {'**YES — INVESTIGATE**' if ar.get('approved_trade_plan_created_any') else 'NO'}",
    ]
    if ar.get("by_action"):
        lines.append("- By action: " + ", ".join(f"{k}={v}" for k, v in ar["by_action"].items()))
    lines.append("")

    # Data quality
    dq = summary.get("data_quality", {})
    if dq.get("available"):
        status = dq.get("status", "?")
        lines += [
            "### Data Quality",
            f"- Status: **{status}** | Issues: {dq.get('issues_count', 0)} | "
            f"Wide spreads: {dq.get('wide_spreads_count', 0)} | "
            f"Missing bars: {dq.get('missing_bars_count', 0)} | "
            f"Insufficient bars: {dq.get('insufficient_bars_count', 0)}",
            f"- Generated: {dq.get('generated_at', '?')}",
            "",
        ]

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Write
# ---------------------------------------------------------------------------

def write_daily_summary(
    summary: dict,
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

    date_str = summary.get("date", "unknown")
    hash8 = (summary.get("summary_hash") or "00000000")[:8]
    json_filename = f"daily_summary-{date_str}-{hash8}.json"
    json_path = runs_dir / json_filename

    text = json.dumps(summary, indent=2, sort_keys=True, default=str)
    tmp = json_path.with_suffix(".json.tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(json_path)

    md_path = memory_dir / "DAILY-SUMMARY.md"
    md_content = format_daily_summary_md(summary)
    with md_path.open("a", encoding="utf-8") as fh:
        fh.write(md_content)

    return {
        "json_path": str(json_path),
        "md_path": str(md_path),
    }
