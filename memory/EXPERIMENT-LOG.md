# Experiment Log

Evidence-backed experiment proposals live here. Hypotheses are not production changes.

## Strategy improvement hypotheses reviewed

```json
{
  "candidate_hypotheses": [
    {
      "hypothesis": "Review breadth threshold sensitivity after enough trigger outcomes accumulate.",
      "requires": [
        "trigger outcomes",
        "paper fills",
        "drawdown evidence",
        "candidate PR"
      ],
      "status": "hypothesis_only"
    },
    {
      "hypothesis": "Compare ATR% weighting against capped equal weight as an experiment.",
      "requires": [
        "backtest",
        "paper comparison",
        "risk review",
        "candidate PR"
      ],
      "status": "hypothesis_only"
    }
  ],
  "evidence_counts": {
    "trade_log_entries": 2,
    "trigger_log_entries": 1
  },
  "generated_at": "2026-05-12T15:31:20Z",
  "production_mutation_allowed": false,
  "promotion_recommended": false,
  "reason": "Insufficient paper evidence for promotion.",
  "run_id": "strategy_improvement-20260512T153120-bc98ee7d",
  "schema_version": "0.1.0"
}
```

## Strategy improvement hypotheses reviewed

```json
{
  "candidate_hypotheses": [
    {
      "hypothesis": "Review breadth threshold sensitivity after enough trigger outcomes accumulate.",
      "requires": [
        "trigger outcomes",
        "paper fills",
        "drawdown evidence",
        "candidate PR"
      ],
      "status": "hypothesis_only"
    },
    {
      "hypothesis": "Compare ATR% weighting against capped equal weight as an experiment.",
      "requires": [
        "backtest",
        "paper comparison",
        "risk review",
        "candidate PR"
      ],
      "status": "hypothesis_only"
    }
  ],
  "evidence_counts": {
    "trade_log_entries": 5,
    "trigger_log_entries": 3
  },
  "generated_at": "2026-05-12T15:32:53Z",
  "production_mutation_allowed": false,
  "promotion_recommended": false,
  "reason": "Insufficient paper evidence for promotion.",
  "run_id": "strategy_improvement-20260512T153253-426c4103",
  "schema_version": "0.1.0"
}
```

## Strategy improvement hypotheses reviewed

```json
{
  "candidate_hypotheses": [
    {
      "hypothesis": "Review breadth threshold sensitivity after enough trigger outcomes accumulate.",
      "requires": [
        "trigger outcomes",
        "paper fills",
        "drawdown evidence",
        "candidate PR"
      ],
      "status": "hypothesis_only"
    },
    {
      "hypothesis": "Compare ATR% weighting against capped equal weight as an experiment.",
      "requires": [
        "backtest",
        "paper comparison",
        "risk review",
        "candidate PR"
      ],
      "status": "hypothesis_only"
    }
  ],
  "evidence_counts": {
    "trade_log_entries": 7,
    "trigger_log_entries": 4
  },
  "generated_at": "2026-05-12T15:33:05Z",
  "production_mutation_allowed": false,
  "promotion_recommended": false,
  "reason": "Insufficient paper evidence for promotion.",
  "run_id": "strategy_improvement-20260512T153305-cfe87d64",
  "schema_version": "0.1.0"
}
```
## Experiment Candidates — 2026-05-13

*From weekly review run weekly_review-2026-05-13*

**Operational issues to investigate:**
- [ ] Dry-run gate 'RISK_STATE_NOT_PAUSED' failed 4 time(s) this period.
- [ ] Dry-run gate 'SPREAD_NOT_TOO_WIDE' failed 1 time(s) this period.
- [ ] 5 order(s) have lifecycle_status=missing — verify on broker.
- [ ] Drawdown is -59.9% — approaching warning threshold (-5%).

**Observations (hypothesis candidates):**
- Market regime: 14/14 sessions risk_on (100%). Avg candidates=67.9, avg excluded=69.0.
- 1 paper execution attempt(s), 1 order(s) submitted.
- 8 external alert(s) ingested this period, 5 routed.

**To propose a strategy experiment, open a PR with:**
- Hypothesis
- Supporting evidence (backtest or paper results)
- Success criteria
- Rollback plan

---
## Experiment Candidates — 2026-05-13

*From weekly review run weekly_review-2026-05-13*

**Operational issues to investigate:**
- [ ] 6 order(s) have lifecycle_status=missing — verify on broker.

**Observations (hypothesis candidates):**
- 1 paper execution attempt(s), 1 order(s) submitted.
- 1 order fill(s) confirmed by order monitor.
- 8 external alert(s) ingested this period, 5 routed.

**To propose a strategy experiment, open a PR with:**
- Hypothesis
- Supporting evidence (backtest or paper results)
- Success criteria
- Rollback plan

---
## Experiment Candidates — 2026-05-13

*From weekly review run weekly_review-2026-05-13*

**Operational issues to investigate:**
- [ ] Paper execution execution-20260513T193130-305917e5 had unexpected status: PAPER_ORDER_ERRORS
- [ ] 6 order(s) have lifecycle_status=missing — verify on broker.

**Observations (hypothesis candidates):**
- 4 paper execution attempt(s), 4 order(s) submitted.
- 6 order fill(s) confirmed by order monitor.
- 8 external alert(s) ingested this period, 5 routed.

**To propose a strategy experiment, open a PR with:**
- Hypothesis
- Supporting evidence (backtest or paper results)
- Success criteria
- Rollback plan

---
## Experiment Candidates — 2026-05-13

*From weekly review run weekly_review-2026-05-13*

**Operational issues to investigate:**
- [ ] Paper execution execution-20260513T193130-305917e5 had unexpected status: PAPER_ORDER_ERRORS

**Observations (hypothesis candidates):**
- 4 paper execution attempt(s), 4 order(s) submitted.
- 3 order fill(s) confirmed by order monitor.
- 8 external alert(s) ingested this period, 5 routed.

**To propose a strategy experiment, open a PR with:**
- Hypothesis
- Supporting evidence (backtest or paper results)
- Success criteria
- Rollback plan

---
## Trigger Performance Observations — 2026-05-13

*From trigger_performance run `trigger_performance-20260513T201006-077c7bad`*
*Period: 2026-05-07 to 2026-05-13 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 14 session(s) scanned, 14 risk-on (100%).
- Spread gate: 21/79 symbols blocked (27%). Avg spread (blocked): 5.026%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 3. Need 17 more fills before P/L analysis is meaningful.
- Average current return across 3 tracked outcome(s): -2.340%. Window pending — no conclusions yet.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-13T21:03:03Z

*From outcome_tracker run `outcome_tracker-20260513T210303-fe0c667b`*
## Outcome Observations — 2026-05-13T21:27:51Z

*From outcome_tracker run `outcome_tracker-20260513T212751-abca712a`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$220.14 return=+0.609%
- JNJ entry: fill=$230.248 current=$230.896 return=+0.281%
- EQIX entry: fill=$1084.37 current=$1077.28 return=-0.654%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-13

*From trigger_performance run `trigger_performance-20260513T210354-bb200c9c`*
*From trigger_performance run `trigger_performance-20260513T212755-af5b15f5`*
*Period: 2026-05-07 to 2026-05-13 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 14 session(s) scanned, 14 risk-on (100%).
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.013%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 3. Need 17 more fills before P/L analysis is meaningful.
- Average current return across 3 tracked outcome(s): +0.079%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 3 records (3 complete, 0 partial). 18 trigger fill associations recovered.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Experiment Candidates — 2026-05-13

*From weekly review run weekly_review-2026-05-13*

**Operational issues to investigate:**
- [ ] Paper execution execution-20260513T193130-305917e5 had unexpected status: PAPER_ORDER_ERRORS

**Observations (hypothesis candidates):**
- 4 paper execution attempt(s), 4 order(s) submitted.
- 3 order fill(s) confirmed by order monitor.
- 8 external alert(s) ingested this period, 5 routed.

**To propose a strategy experiment, open a PR with:**
- Hypothesis
- Supporting evidence (backtest or paper results)
- Success criteria
- Rollback plan

---
