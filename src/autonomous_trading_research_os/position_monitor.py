from __future__ import annotations

from typing import Any

from .alpaca_adapter import AlpacaAdapter
from .audit import append_event, new_run_id, record_error
from .file_io import read_json, safe_float, write_json, utc_now_iso
from .paths import LATEST_DIR, MEMORY_DIR, ensure_repo_dirs
from .risk import classify_symbol


def _load_snapshot(use_alpaca: bool) -> dict[str, Any]:
    if use_alpaca:
        return AlpacaAdapter().refresh_snapshot([])
    return read_json(LATEST_DIR / "market_snapshot.json", default={})


def run_position_monitor(use_alpaca: bool = False) -> dict[str, Any]:
    ensure_repo_dirs()
    run_id = new_run_id("position_monitor")
    try:
        snapshot = _load_snapshot(use_alpaca)
        positions = snapshot.get("positions", []) if isinstance(snapshot.get("positions"), list) else []
        account = snapshot.get("account", {}) if isinstance(snapshot.get("account"), dict) else {}
        equity = safe_float(account.get("equity") or account.get("portfolio_value") or account.get("cash"), 0.0)
        risk_state = read_json(MEMORY_DIR / "RISK-STATE.json", default={}) or {}
        previous_peak = safe_float(risk_state.get("peak_equity"), equity)
        peak = max(previous_peak, equity)
        drawdown = (equity / peak - 1.0) if peak > 0 else 0.0

        violations: list[dict[str, Any]] = []
        for position in positions:
            if not isinstance(position, dict):
                continue
            symbol = str(position.get("symbol") or "")
            qty = safe_float(position.get("qty") or position.get("quantity"), 0.0)
            kind = classify_symbol(symbol)
            if qty < -1e-9:
                violations.append({"symbol": symbol, "violation": "short_position", "qty": qty})
            if kind != "equity_or_etf":
                violations.append({"symbol": symbol, "violation": "forbidden_asset_class", "classify_symbol": kind})

        new_state = {
            "schema_version": "0.1.0",
            "updated_at": utc_now_iso(),
            "latest_equity": equity,
            "peak_equity": peak,
            "drawdown": drawdown,
            "position_count": len(positions),
            "last_monitor_run_id": run_id,
        }
        write_json(MEMORY_DIR / "RISK-STATE.json", new_state)
        report: dict[str, Any] = {
            "schema_version": "0.1.0",
            "run_id": run_id,
            "generated_at": utc_now_iso(),
            "use_alpaca": use_alpaca,
            "equity": equity,
            "drawdown": drawdown,
            "position_count": len(positions),
            "violations": violations,
            "status": "OK" if not violations else "ATTENTION_REQUIRED",
        }
        write_json(LATEST_DIR / "position_report.json", report)
        append_event("TRADE-LOG.md", "Position monitor completed", report)
        return report
    except Exception as exc:
        record_error("position_monitor", exc, {"use_alpaca": use_alpaca})
        raise
