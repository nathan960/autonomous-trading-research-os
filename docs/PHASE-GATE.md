# Phase Gate Scorecard — Operator Runbook

Evidence-based promotion review for Autonomous Trading Research OS.
This scorecard never modifies config, never places orders, never enables execution.

---

## Overview

The phase gate determines whether accumulated paper trading evidence meets the criteria
for a **human-initiated promotion review**. It does not automatically promote anything —
promotion always requires a human PR with rationale, backtest/paper evidence, and rollback notes.

**Phases (in order):**

| Phase | Description | max $/order | max orders/run | Scheduled execution |
|-------|-------------|-------------|-----------------|---------------------|
| PHASE_0_BUILD | Build/test only, no paper execution | — | — | No |
| PHASE_1_TINY_MANUAL | Manual paper only | $25 | 1 | No |
| PHASE_2_SMALL_MANUAL | Manual paper only | $50 | 1 | No |
| PHASE_3_LIMITED_SCHEDULED_RESEARCH_ONLY | Scheduled research, no scheduled execution | $50 | 1 | No |
| PHASE_4_LIMITED_SCHEDULED_PAPER | **Blocked — requires explicit human approval outside this system** | $50 | 1 | Yes |

---

## Running the scorecard

```bash
python scripts/phase_gate.py
```

**Outputs:**
- `data/latest/phase_gate.json` — current scorecard
- `data/history/runs/phase_gate_<date>-<hash>.json` — archived copy
- `memory/PROMOTION-DECISIONS.md` — appended scorecard summary

**GitHub Actions:**  
`workflow_dispatch` (manual) or weekly Friday at 22:00 UTC via `.github/workflows/phase-gate.yml`.

---

## How phase is determined

The current phase is inferred from `config/risk_limits.json`:

| `max_notional_per_order` | `max_orders_per_run` | Inferred phase |
|--------------------------|----------------------|----------------|
| None (absent) | None | PHASE_0_BUILD |
| ≤ $25 | ≤ 1 | PHASE_1_TINY_MANUAL |
| ≤ $50 | ≤ 1 | PHASE_2_SMALL_MANUAL |
| > $50 or > 1 | any | PHASE_3_LIMITED_SCHEDULED_RESEARCH_ONLY |

---

## Gate checks (Phase 1 → Phase 2)

All checks are listed in `data/latest/phase_gate.json` under `checks`.

### Blocking checks (must all pass to be eligible)

| Check ID | Requirement | Evidence field |
|----------|-------------|----------------|
| FILLED_ORDERS_MIN_20 | ≥ 20 filled orders | `order_monitor_report.orders_filled` |
| NO_MISSING_ORDERS | 0 missing orders | `order_monitor_report.orders_missing` |
| NO_REJECTED_ORDERS | 0 rejected orders | `order_monitor_report.orders_rejected` |
| SOURCE_INTEGRITY_OK | `source_integrity_status == "ok"` | `system_status.source_integrity_status` |
| NO_SYSTEM_BLOCKING_ISSUES | Empty `blocking_issues` list | `system_status.blocking_issues` |
| OPEN_ORDERS_ZERO | 0 active/open orders | `order_monitor_report.orders_active` |
| DRAWDOWN_NOT_BREACHED | `drawdown > max_drawdown_block_pct` | `risk_state.drawdown` |
| DAILY_SUMMARIES_PRESENT | ≥ 1 daily summary in history | `data/history/runs/daily_summary*.json` count |
| WEEKLY_REVIEW_PRESENT | ≥ 1 weekly review in history | `data/history/runs/weekly_review*.json` count |
| OUTCOME_INTEGRITY_OK | `outcome_snapshot.source_integrity_status == "ok"` | `outcome_snapshot.source_integrity_status` |
| TRIGGER_PERFORMANCE_OK | `trigger_performance.status == "ok"` | `trigger_performance.status` |
| MAX_ORDERS_PER_RUN_ONE | `max_orders_per_run == 1` | `risk_limits.max_orders_per_run` |

### Warning checks (non-blocking — show in `warnings`, not `blocking_issues`)

| Check ID | Requirement | Note |
|----------|-------------|------|
| DAILY_ORDER_LIMIT_RESPECTED | Daily limits not exceeded today | Churn guard now prevents future violations |
| LINEAGE_ADEQUATE | ≥ 50% lineage complete ratio | Older fills acceptable; archiving now active |

---

## Resolving blocking issues

### FILLED_ORDERS_MIN_20

Need more paper trading evidence. Continue running the manual paper cycle:
```bash
python scripts/generate_trade_plan.py --approve-paper
python scripts/execute_paper.py --confirm-paper
```
Re-run after 20+ orders have filled.

### NO_MISSING_ORDERS / NO_REJECTED_ORDERS

Investigate via the order monitor and resolution log:
```bash
python scripts/monitor_orders.py
cat memory/ORDER-RESOLUTION-LOG.md
```

### SOURCE_INTEGRITY_OK

Run a fresh data refresh:
```bash
python scripts/refresh_data.py
python scripts/system_status.py
```

### NO_SYSTEM_BLOCKING_ISSUES

Check `data/latest/system_status.json` `blocking_issues` field and resolve each.

### OPEN_ORDERS_ZERO

Wait for open orders to settle, or cancel them:
```bash
python scripts/list_open_orders.py
python scripts/cancel_paper_order.py --order-id <id>
```

### DRAWDOWN_NOT_BREACHED

Review `memory/RISK-STATE.json` drawdown field. Do not request promotion while drawdown is in breach.

### DAILY_SUMMARIES_PRESENT / WEEKLY_REVIEW_PRESENT

Run the missing review:
```bash
python scripts/daily_summary.py
python scripts/weekly_review.py
```

### OUTCOME_INTEGRITY_OK

Run outcome tracker with live data:
```bash
python scripts/track_outcomes.py
```

### TRIGGER_PERFORMANCE_OK

Check `data/latest/trigger_performance.json` and `scripts/score_triggers.py` for errors.

---

## Promotion process (human steps required)

The scorecard only ever produces `recommendation: "eligible_for_review"` — it never
automatically promotes. When the scorecard shows `eligible_for_next_phase: true`:

1. **Read the full scorecard** — review every check, evidence summary, and any warnings.
2. **Review PROMOTION-DECISIONS.md** — understand prior decisions and context.
3. **Prepare a candidate PR** containing:
   - Updated `config/risk_limits.json` with the new `max_notional_per_order` cap
   - Evidence rationale (fills, lineage, outcomes, drawdown, weekly review summary)
   - Rollback notes (how to revert to previous limits)
4. **Get explicit approval** from a second reviewer before merging.
5. **Do not rely solely on this scorecard** — human judgment is required.

**PHASE_4 (scheduled paper execution)** is always blocked by this automated scorecard.
It requires explicit human approval and a separate PR with enhanced evidence.

---

## Safety guarantees

The `scripts/phase_gate.py` script and `src/trading_os/research/phase_gate.py` module:

- Never modify `risk_limits.json` or any config file
- Never call `execute_paper.py` or any execution code path
- Never approve trade plans
- Never enable paper execution
- Never enable scheduled paper execution
- Never recommend PHASE_4 activation
- Never print, log, or write secrets

Every scorecard output contains an explicit safety note:

> No config was changed. No orders were placed. No paper execution was enabled.
> No trade plans were approved. No scheduled execution was enabled.
