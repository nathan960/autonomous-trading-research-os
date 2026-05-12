from __future__ import annotations

from typing import Any

from .audit import append_event, new_run_id, record_error
from .file_io import read_json, sha256_json, write_json
from .indicators import latest_indicator_snapshot
from .paths import CONFIG_DIR, LATEST_DIR, ensure_repo_dirs


def run_trigger_scan() -> dict[str, Any]:
    ensure_repo_dirs()
    run_id = new_run_id("trigger_scan")
    try:
        strategy = read_json(CONFIG_DIR / "strategy.json", default={})
        universe = read_json(CONFIG_DIR / "universe.json", default={})
        sector_map = read_json(CONFIG_DIR / "sector_map.json", default={})
        snapshot = read_json(LATEST_DIR / "market_snapshot.json", default=None)
        if snapshot is None:
            raise RuntimeError("Missing data/latest/market_snapshot.json. Run data refresh first.")

        params = strategy.get("parameters", {})
        bars = snapshot.get("bars", {})
        spy_indicators = latest_indicator_snapshot("SPY", bars.get("SPY", []), params.get("sma_period", 200), params.get("roc_6m_period", 126), params.get("roc_12m_period", 252), params.get("atr_period", 20))
        spy_trend_ok = bool(spy_indicators.get("passes_trend_filter"))
        spy_momentum_ok = bool((spy_indicators.get("roc126") or 0.0) > 0.0)

        ready_count = 0
        above_count = 0
        candidates: list[dict[str, Any]] = []
        trigger_rows: list[dict[str, Any]] = []

        for symbol in universe.get("symbols", []):
            indicators = latest_indicator_snapshot(symbol, bars.get(symbol, []), params.get("sma_period", 200), params.get("roc_6m_period", 126), params.get("roc_12m_period", 252), params.get("atr_period", 20))
            row = {
                "symbol": symbol,
                "trigger_ids": ["STOCK_TREND_200DMA", "STOCK_MOMENTUM_126_252"],
                "status": "skipped",
                "skip_reason": None,
                "indicators": indicators,
                "sector": sector_map.get(symbol),
            }
            if not indicators.get("is_ready"):
                row["skip_reason"] = "indicators_not_ready"
                trigger_rows.append(row)
                continue
            ready_count += 1
            if indicators.get("passes_trend_filter"):
                above_count += 1
            else:
                row["skip_reason"] = "failed_stock_200dma_trend_filter"
                trigger_rows.append(row)
                continue

            mom6 = indicators.get("roc126") or 0.0
            mom12 = indicators.get("roc252") or 0.0
            if mom6 <= float(params.get("min_momentum_6m", 0.0)):
                row["skip_reason"] = "failed_min_6m_momentum"
                trigger_rows.append(row)
                continue
            if mom12 <= float(params.get("min_momentum_12m", 0.0)):
                row["skip_reason"] = "failed_min_12m_momentum"
                trigger_rows.append(row)
                continue
            sector = sector_map.get(symbol)
            if not sector:
                row["skip_reason"] = "missing_sector_map"
                trigger_rows.append(row)
                continue

            candidate = {
                "symbol": symbol,
                "momentum_score": indicators.get("momentum_score"),
                "roc126": indicators.get("roc126"),
                "roc252": indicators.get("roc252"),
                "atr_pct": indicators.get("atr_pct"),
                "latest_close": indicators.get("latest_close"),
                "sector_code": sector.get("sector_code"),
                "sector": sector.get("sector"),
            }
            row["status"] = "candidate"
            row["skip_reason"] = None
            row["candidate"] = candidate
            trigger_rows.append(row)
            candidates.append(candidate)

        breadth = (above_count / ready_count) if ready_count else 0.0
        risk_on = bool(spy_trend_ok and spy_momentum_ok and breadth >= float(params.get("breadth_threshold", 0.55)))

        ranked = sorted(candidates, key=lambda item: item.get("momentum_score") or -999.0, reverse=True)
        selected: list[dict[str, Any]] = []
        sector_counts: dict[str, int] = {}
        max_names_per_sector = int(params.get("max_names_per_sector", 2))
        max_holdings = int(params.get("max_holdings", 10))
        for candidate in ranked:
            sector_code = str(candidate.get("sector_code"))
            if sector_counts.get(sector_code, 0) >= max_names_per_sector:
                continue
            selected.append(candidate)
            sector_counts[sector_code] = sector_counts.get(sector_code, 0) + 1
            if len(selected) >= max_holdings:
                break

        output: dict[str, Any] = {
            "schema_version": "0.1.0",
            "run_id": run_id,
            "generated_at": snapshot.get("generated_at"),
            "data_refresh_run_id": snapshot.get("run_id"),
            "market_snapshot_hash": snapshot.get("source_data_hash"),
            "strategy_id": strategy.get("strategy_id"),
            "regime": {
                "spy_indicators": spy_indicators,
                "spy_trend_ok": spy_trend_ok,
                "spy_momentum_ok": spy_momentum_ok,
                "ready_count": ready_count,
                "above_200dma_count": above_count,
                "breadth": breadth,
                "breadth_threshold": params.get("breadth_threshold", 0.55),
                "risk_on": risk_on,
            },
            "candidates": ranked,
            "selected": selected if risk_on else [],
            "sector_counts_selected": sector_counts if risk_on else {},
            "triggers": trigger_rows,
            "trigger_snapshot_hash": None,
        }
        output["trigger_snapshot_hash"] = sha256_json({k: v for k, v in output.items() if k != "trigger_snapshot_hash"})
        write_json(LATEST_DIR / "trigger_snapshot.json", output)

        append_event("TRIGGER-LOG.md", "Trigger scan completed", {
            "run_id": run_id,
            "risk_on": risk_on,
            "spy_trend_ok": spy_trend_ok,
            "spy_momentum_ok": spy_momentum_ok,
            "breadth": breadth,
            "ready_count": ready_count,
            "candidate_count": len(ranked),
            "selected_count": len(output["selected"]),
            "market_snapshot_hash": snapshot.get("source_data_hash"),
        })
        append_event("SIGNAL-LOG.md", "Signal candidates ranked", {
            "run_id": run_id,
            "risk_on": risk_on,
            "top_candidates": ranked[:10],
            "selected": output["selected"],
        })
        return output
    except Exception as exc:
        record_error("trigger_scan", exc)
        raise
