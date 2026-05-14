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
## Outcome Observations — 2026-05-13T22:40:21Z

*From outcome_tracker run `outcome_tracker-20260513T224021-e7ad10a5`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$220.14 return=+0.609%
- JNJ entry: fill=$230.248 current=$230.43 return=+0.079%
- EQIX entry: fill=$1084.37 current=$1077.28 return=-0.654%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-13

*From trigger_performance run `trigger_performance-20260513T224527-6119bcdc`*
*Period: 2026-05-07 to 2026-05-13 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.013%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 3. Need 17 more fills before P/L analysis is meaningful.
- Average current return across 3 tracked outcome(s): +0.011%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 3 records (3 complete, 0 partial). 18 trigger fill associations recovered.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T13:50:52Z

*From outcome_tracker run `outcome_tracker-20260514T135052-782298a9`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$219.62 return=+0.371%
- JNJ entry: fill=$230.248 current=$230.9 return=+0.283%
- EQIX entry: fill=$1084.37 current=$1075.43 return=-0.824%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T135139-204f5157`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 6.965%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 3. Need 17 more fills before P/L analysis is meaningful.
- Average current return across 3 tracked outcome(s): -0.057%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 3 records (3 complete, 0 partial). 18 trigger fill associations recovered.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T13:56:45Z

*From outcome_tracker run `outcome_tracker-20260514T135645-bc7586e4`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$220.09 return=+0.586%
- JNJ entry: fill=$230.248 current=$231.225 return=+0.424%
- EQIX entry: fill=$1084.37 current=$1080.34 return=-0.372%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T135734-d2ee5807`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 58% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 46/79 symbols blocked (58%). Avg spread (blocked): 7.791%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 3. Need 17 more fills before P/L analysis is meaningful.
- Average current return across 3 tracked outcome(s): +0.213%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 3 records (3 complete, 0 partial). 18 trigger fill associations recovered.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T14:16:25Z

*From outcome_tracker run `outcome_tracker-20260514T141625-5c83a59b`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$219.42 return=+0.280%
- JNJ entry: fill=$230.248 current=$231.05 return=+0.348%
- EQIX entry: fill=$1084.37 current=$1076.135 return=-0.759%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T141626-c23d8f37`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 59% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 47/79 symbols blocked (59%). Avg spread (blocked): 7.338%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 3. Need 17 more fills before P/L analysis is meaningful.
- Average current return across 3 tracked outcome(s): -0.044%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 3 records (0 complete, 3 partial). 6 trigger fill associations recovered. 3 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=1, LIQUIDITY_GATE_V1=1, MOMENTUM_BLEND_6M_12M_V1=1, SPREAD_GATE_V1=1, STOCK_TREND_200DMA_V1=1.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T14:55:09Z

*From outcome_tracker run `outcome_tracker-20260514T145509-dd18af53`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.83 return=+0.010%
- JNJ entry: fill=$230.248 current=$229.995 return=-0.110%
- EQIX entry: fill=$1084.37 current=$1079.565 return=-0.443%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T145509-dd18af53`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 54% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 43/79 symbols blocked (54%). Avg spread (blocked): 6.115%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 3. Need 17 more fills before P/L analysis is meaningful.
- Average current return across 3 tracked outcome(s): -0.181%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 3 records (0 complete, 3 partial). 6 trigger fill associations recovered. 3 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=1, LIQUIDITY_GATE_V1=1, MOMENTUM_BLEND_6M_12M_V1=1, SPREAD_GATE_V1=1, STOCK_TREND_200DMA_V1=1.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T14:56:34Z

*From outcome_tracker run `outcome_tracker-20260514T145634-50dad7cb`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$219.0341 return=+0.103%
- JNJ entry: fill=$230.248 current=$230.265 return=+0.007%
- EQIX entry: fill=$1084.37 current=$1080.395 return=-0.367%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T145634-50dad7cb`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 51% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 40/79 symbols blocked (51%). Avg spread (blocked): 6.196%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 3. Need 17 more fills before P/L analysis is meaningful.
- Average current return across 3 tracked outcome(s): -0.085%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 3 records (0 complete, 3 partial). 6 trigger fill associations recovered. 3 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=1, LIQUIDITY_GATE_V1=1, MOMENTUM_BLEND_6M_12M_V1=1, SPREAD_GATE_V1=1, STOCK_TREND_200DMA_V1=1.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T15:00:15Z

*From outcome_tracker run `outcome_tracker-20260514T150015-70c5c992`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$219.675 return=+0.396%
- JNJ entry: fill=$230.248 current=$230.32 return=+0.031%
- EQIX entry: fill=$1084.37 current=$1082.35 return=-0.186%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T150015-70c5c992`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 53% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 42/79 symbols blocked (53%). Avg spread (blocked): 6.491%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 3. Need 17 more fills before P/L analysis is meaningful.
- Average current return across 3 tracked outcome(s): +0.080%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 3 records (0 complete, 3 partial). 12 trigger fill associations recovered. 3 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=2, LIQUIDITY_GATE_V1=2, MOMENTUM_BLEND_6M_12M_V1=2, SPREAD_GATE_V1=2, STOCK_TREND_200DMA_V1=2.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T15:01:27Z

*From outcome_tracker run `outcome_tracker-20260514T150127-4dbd4463`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$219.68 return=+0.398%
- JNJ entry: fill=$230.248 current=$230.21 return=-0.017%
- EQIX entry: fill=$1084.37 current=$1082.51 return=-0.171%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T150127-4dbd4463`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 52% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 41/79 symbols blocked (52%). Avg spread (blocked): 6.788%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 3. Need 17 more fills before P/L analysis is meaningful.
- Average current return across 3 tracked outcome(s): +0.070%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 3 records (0 complete, 3 partial). 12 trigger fill associations recovered. 3 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=2, LIQUIDITY_GATE_V1=2, MOMENTUM_BLEND_6M_12M_V1=2, SPREAD_GATE_V1=2, STOCK_TREND_200DMA_V1=2.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T15:13:14Z

*From outcome_tracker run `outcome_tracker-20260514T151314-7ed26ffc`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.76 return=-0.022%
- JNJ entry: fill=$230.248 current=$229.77 return=-0.208%
- EQIX entry: fill=$1084.37 current=$1084.0 return=-0.034%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T151315-66148988`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 36/79 symbols blocked (46%). Avg spread (blocked): 6.617%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 3. Need 17 more fills before P/L analysis is meaningful.
- Average current return across 3 tracked outcome(s): -0.088%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 3 records (0 complete, 3 partial). 6 trigger fill associations recovered. 3 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=1, LIQUIDITY_GATE_V1=1, MOMENTUM_BLEND_6M_12M_V1=1, SPREAD_GATE_V1=1, STOCK_TREND_200DMA_V1=1.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Experiment — exp-20260514T153959-e47e771d

**Created:** 2026-05-14T15:39:59Z  **Status:** proposed

**Hypothesis:** Lowering breadth_threshold from 0.55 to 0.50 increases fills in moderate breadth regime
**Affected rule / trigger:** BREADTH_TREND  **Config key:** —
**Expected benefit:** Est. 5-10 pct more fills on moderate breadth days
**Risk:** May increase false positives in weak market conditions

**Required sample size:** 50 fills  **Backtest required:** True  **Paper validation required:** True

**Promotion criteria:**
- min fills: 20
- min observations: 50
- min expectancy after costs: 0.001
- must beat BIL: True
- must beat SPY: False
- no risk breaches: True
- human approval required: True

**Demotion criteria:**
- max drawdown: -0.05
- max consecutive losses: 5
- expectancy floor: -0.005

**Candidate patch (documentary — no config modified):**
- File: `config/strategy.json`
- Key: `parameters.breadth_threshold`
- Old: `'0.55'`  →  New: `'0.50'`

**Notes:** Based on 60-day trigger log showing 40 pct of breadth days fall between 0.50 and 0.55

**Safety:** production_mutation_allowed=False
---
