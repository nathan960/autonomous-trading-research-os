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
## Outcome Observations — 2026-05-14T15:43:29Z

*From outcome_tracker run `outcome_tracker-20260514T154329-4c3be2d7`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.988 return=-0.375%
- JNJ entry: fill=$230.248 current=$230.11 return=-0.060%
- EQIX entry: fill=$1084.37 current=$1077.8325 return=-0.603%
- EQIX entry: fill=$1079.5 current=$1077.8325 return=-0.154%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T154329-4c3be2d7`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 35/79 symbols blocked (44%). Avg spread (blocked): 5.720%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 4. Need 16 more fills before P/L analysis is meaningful.
- Average current return across 4 tracked outcome(s): -0.298%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 4 records (0 complete, 4 partial). 18 trigger fill associations recovered. 4 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T15:44:50Z

*From outcome_tracker run `outcome_tracker-20260514T154450-35e30060`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.27 return=-0.246%
- JNJ entry: fill=$230.248 current=$230.185 return=-0.027%
- EQIX entry: fill=$1084.37 current=$1078.5 return=-0.541%
- EQIX entry: fill=$1079.5 current=$1078.5 return=-0.093%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T154450-35e30060`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 52% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 41/79 symbols blocked (52%). Avg spread (blocked): 5.377%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 4. Need 16 more fills before P/L analysis is meaningful.
- Average current return across 4 tracked outcome(s): -0.227%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 4 records (0 complete, 4 partial). 18 trigger fill associations recovered. 4 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T15:45:49Z

*From outcome_tracker run `outcome_tracker-20260514T154549-e3d51b1c`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.2739 return=-0.244%
- JNJ entry: fill=$230.248 current=$230.22 return=-0.012%
- EQIX entry: fill=$1084.37 current=$1078.275 return=-0.562%
- EQIX entry: fill=$1079.5 current=$1078.275 return=-0.113%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T154549-e3d51b1c`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 37/79 symbols blocked (47%). Avg spread (blocked): 5.733%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 4. Need 16 more fills before P/L analysis is meaningful.
- Average current return across 4 tracked outcome(s): -0.233%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 4 records (0 complete, 4 partial). 18 trigger fill associations recovered. 4 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T15:48:23Z

*From outcome_tracker run `outcome_tracker-20260514T154823-07890943`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.25 return=-0.255%
- JNJ entry: fill=$230.248 current=$230.35 return=+0.044%
- EQIX entry: fill=$1084.37 current=$1079.32 return=-0.466%
- EQIX entry: fill=$1079.5 current=$1079.32 return=-0.017%
- EQIX exit: fill=$1078.442 current=$1079.32 return=+0.081%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T154823-07890943`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 56% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 44/79 symbols blocked (56%). Avg spread (blocked): 5.488%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 5. Need 15 more fills before P/L analysis is meaningful.
- Average current return across 5 tracked outcome(s): -0.122%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 5 records (0 complete, 5 partial). 18 trigger fill associations recovered. 5 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T15:52:37Z

*From outcome_tracker run `outcome_tracker-20260514T155237-6c401389`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.115 return=-0.317%
- JNJ entry: fill=$230.248 current=$230.495 return=+0.107%
- EQIX entry: fill=$1084.37 current=$1077.84 return=-0.602%
- EQIX entry: fill=$1079.5 current=$1077.84 return=-0.154%
- EQIX exit: fill=$1078.442 current=$1077.84 return=-0.056%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T155237-6c401389`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 53% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 42/79 symbols blocked (53%). Avg spread (blocked): 5.613%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 5. Need 15 more fills before P/L analysis is meaningful.
- Average current return across 5 tracked outcome(s): -0.204%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 5 records (0 complete, 5 partial). 18 trigger fill associations recovered. 5 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T15:53:42Z

*From outcome_tracker run `outcome_tracker-20260514T155342-ecda892c`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.115 return=-0.317%
- JNJ entry: fill=$230.248 current=$230.45 return=+0.088%
- EQIX entry: fill=$1084.37 current=$1078.04 return=-0.584%
- EQIX entry: fill=$1079.5 current=$1078.04 return=-0.135%
- EQIX exit: fill=$1078.442 current=$1078.04 return=-0.037%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T155342-ecda892c`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 51% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 40/79 symbols blocked (51%). Avg spread (blocked): 5.523%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 5. Need 15 more fills before P/L analysis is meaningful.
- Average current return across 5 tracked outcome(s): -0.197%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 5 records (0 complete, 5 partial). 18 trigger fill associations recovered. 5 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T16:30:03Z

*From outcome_tracker run `outcome_tracker-20260514T163003-ef335475`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.94 return=-0.397%
- JNJ entry: fill=$230.248 current=$230.27 return=+0.010%
- EQIX entry: fill=$1084.37 current=$1076.955 return=-0.684%
- EQIX entry: fill=$1079.5 current=$1076.955 return=-0.236%
- EQIX exit: fill=$1078.442 current=$1076.955 return=-0.138%
- EQIX entry: fill=$1078.41 current=$1076.955 return=-0.135%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T163004-d263b0c5`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 35/79 symbols blocked (44%). Avg spread (blocked): 5.521%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 6. Need 14 more fills before P/L analysis is meaningful.
- Average current return across 6 tracked outcome(s): -0.263%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 6 records (0 complete, 6 partial). 30 trigger fill associations recovered. 6 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=5, LIQUIDITY_GATE_V1=5, MOMENTUM_BLEND_6M_12M_V1=5, SPREAD_GATE_V1=5, STOCK_TREND_200DMA_V1=5.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T16:31:20Z

*From outcome_tracker run `outcome_tracker-20260514T163120-833c0bc8`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.045 return=-0.349%
- JNJ entry: fill=$230.248 current=$230.27 return=+0.010%
- EQIX entry: fill=$1084.37 current=$1077.51 return=-0.633%
- EQIX entry: fill=$1079.5 current=$1077.51 return=-0.184%
- EQIX exit: fill=$1078.442 current=$1077.51 return=-0.086%
- EQIX entry: fill=$1078.41 current=$1077.51 return=-0.084%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T163120-833c0bc8`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 33/79 symbols blocked (42%). Avg spread (blocked): 6.012%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 6. Need 14 more fills before P/L analysis is meaningful.
- Average current return across 6 tracked outcome(s): -0.221%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 6 records (0 complete, 6 partial). 30 trigger fill associations recovered. 6 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=5, LIQUIDITY_GATE_V1=5, MOMENTUM_BLEND_6M_12M_V1=5, SPREAD_GATE_V1=5, STOCK_TREND_200DMA_V1=5.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T16:52:38Z

*From outcome_tracker run `outcome_tracker-20260514T165238-45a1b2a9`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.175 return=-0.289%
- JNJ entry: fill=$230.248 current=$230.25 return=+0.001%
- EQIX entry: fill=$1084.37 current=$1079.41 return=-0.457%
- EQIX entry: fill=$1079.5 current=$1079.41 return=-0.008%
- EQIX exit: fill=$1078.442 current=$1079.41 return=+0.090%
- EQIX entry: fill=$1078.41 current=$1079.41 return=+0.093%
- JNJ entry: fill=$230.116 current=$230.25 return=+0.058%
- WMT entry: fill=$132.276 current=$132.275 return=-0.001%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T165238-45a1b2a9`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 36/79 symbols blocked (46%). Avg spread (blocked): 6.371%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 8. Need 12 more fills before P/L analysis is meaningful.
- Average current return across 8 tracked outcome(s): -0.064%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 8 records (1 complete, 7 partial). 36 trigger fill associations recovered. 7 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=6, LIQUIDITY_GATE_V1=6, MOMENTUM_BLEND_6M_12M_V1=6, SPREAD_GATE_V1=6, STOCK_TREND_200DMA_V1=6.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T17:17:45Z

*From outcome_tracker run `outcome_tracker-20260514T171745-bcccbeb9`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.48 return=-0.607%
- JNJ entry: fill=$230.248 current=$230.17 return=-0.034%
- EQIX entry: fill=$1084.37 current=$1077.735 return=-0.612%
- EQIX entry: fill=$1079.5 current=$1077.735 return=-0.164%
- EQIX exit: fill=$1078.442 current=$1077.735 return=-0.066%
- EQIX entry: fill=$1078.41 current=$1077.735 return=-0.063%
- JNJ entry: fill=$230.116 current=$230.17 return=+0.024%
- WMT entry: fill=$132.276 current=$132.5 return=+0.169%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T171745-bcccbeb9`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 38/79 symbols blocked (48%). Avg spread (blocked): 5.839%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 8. Need 12 more fills before P/L analysis is meaningful.
- Average current return across 8 tracked outcome(s): -0.169%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 8 records (0 complete, 8 partial). 42 trigger fill associations recovered. 8 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=7, LIQUIDITY_GATE_V1=7, MOMENTUM_BLEND_6M_12M_V1=7, SPREAD_GATE_V1=7, STOCK_TREND_200DMA_V1=7.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T17:18:53Z

*From outcome_tracker run `outcome_tracker-20260514T171853-e8122113`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.39 return=-0.648%
- JNJ entry: fill=$230.248 current=$230.15 return=-0.043%
- EQIX entry: fill=$1084.37 current=$1077.735 return=-0.612%
- EQIX entry: fill=$1079.5 current=$1077.735 return=-0.164%
- EQIX exit: fill=$1078.442 current=$1077.735 return=-0.066%
- EQIX entry: fill=$1078.41 current=$1077.735 return=-0.063%
- JNJ entry: fill=$230.116 current=$230.15 return=+0.015%
- WMT entry: fill=$132.276 current=$132.54 return=+0.200%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T171853-e8122113`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 35/79 symbols blocked (44%). Avg spread (blocked): 6.655%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 8. Need 12 more fills before P/L analysis is meaningful.
- Average current return across 8 tracked outcome(s): -0.172%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 8 records (0 complete, 8 partial). 42 trigger fill associations recovered. 8 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=7, LIQUIDITY_GATE_V1=7, MOMENTUM_BLEND_6M_12M_V1=7, SPREAD_GATE_V1=7, STOCK_TREND_200DMA_V1=7.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T17:19:58Z

*From outcome_tracker run `outcome_tracker-20260514T171958-3d5a3be6`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.305 return=-0.687%
- JNJ entry: fill=$230.248 current=$230.265 return=+0.007%
- EQIX entry: fill=$1084.37 current=$1078.12 return=-0.576%
- EQIX entry: fill=$1079.5 current=$1078.12 return=-0.128%
- EQIX exit: fill=$1078.442 current=$1078.12 return=-0.030%
- EQIX entry: fill=$1078.41 current=$1078.12 return=-0.027%
- JNJ entry: fill=$230.116 current=$230.265 return=+0.065%
- WMT entry: fill=$132.276 current=$132.5325 return=+0.194%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T171958-3d5a3be6`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 34/79 symbols blocked (43%). Avg spread (blocked): 5.847%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 8. Need 12 more fills before P/L analysis is meaningful.
- Average current return across 8 tracked outcome(s): -0.148%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 8 records (0 complete, 8 partial). 48 trigger fill associations recovered. 8 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=8, LIQUIDITY_GATE_V1=8, MOMENTUM_BLEND_6M_12M_V1=8, SPREAD_GATE_V1=8, STOCK_TREND_200DMA_V1=8.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T17:21:09Z

*From outcome_tracker run `outcome_tracker-20260514T172109-0160a03c`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.163 return=-0.752%
- JNJ entry: fill=$230.248 current=$230.035 return=-0.092%
- EQIX entry: fill=$1084.37 current=$1076.65 return=-0.712%
- EQIX entry: fill=$1079.5 current=$1076.65 return=-0.264%
- EQIX exit: fill=$1078.442 current=$1076.65 return=-0.166%
- EQIX entry: fill=$1078.41 current=$1076.65 return=-0.163%
- JNJ entry: fill=$230.116 current=$230.035 return=-0.035%
- WMT entry: fill=$132.276 current=$132.36 return=+0.064%
- WMT entry: fill=$132.474 current=$132.36 return=-0.086%
- EQIX entry: fill=$1076.89 current=$1076.65 return=-0.022%
- EQIX entry: fill=$1076.82 current=$1076.65 return=-0.016%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T172109-0160a03c`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 36/79 symbols blocked (46%). Avg spread (blocked): 6.379%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 11. Need 9 more fills before P/L analysis is meaningful.
- Average current return across 11 tracked outcome(s): -0.204%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 11 records (1 complete, 10 partial). 54 trigger fill associations recovered. 10 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=9, LIQUIDITY_GATE_V1=9, MOMENTUM_BLEND_6M_12M_V1=9, SPREAD_GATE_V1=9, STOCK_TREND_200DMA_V1=9.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T17:22:32Z

*From outcome_tracker run `outcome_tracker-20260514T172232-2e4ad7df`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.31 return=-0.685%
- JNJ entry: fill=$230.248 current=$230.03 return=-0.095%
- EQIX entry: fill=$1084.37 current=$1076.625 return=-0.714%
- EQIX entry: fill=$1079.5 current=$1076.625 return=-0.266%
- EQIX exit: fill=$1078.442 current=$1076.625 return=-0.169%
- EQIX entry: fill=$1078.41 current=$1076.625 return=-0.166%
- JNJ entry: fill=$230.116 current=$230.03 return=-0.037%
- WMT entry: fill=$132.276 current=$132.3 return=+0.018%
- WMT entry: fill=$132.474 current=$132.3 return=-0.131%
- EQIX entry: fill=$1076.89 current=$1076.625 return=-0.025%
- EQIX entry: fill=$1076.82 current=$1076.625 return=-0.018%
- JNJ entry: fill=$230.044 current=$230.03 return=-0.006%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T172232-2e4ad7df`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 36/79 symbols blocked (46%). Avg spread (blocked): 5.989%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 12. Need 8 more fills before P/L analysis is meaningful.
- Average current return across 12 tracked outcome(s): -0.191%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 12 records (0 complete, 12 partial). 66 trigger fill associations recovered. 12 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T17:23:42Z

*From outcome_tracker run `outcome_tracker-20260514T172342-3397bcc4`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.47 return=-0.611%
- JNJ entry: fill=$230.248 current=$230.04 return=-0.090%
- EQIX entry: fill=$1084.37 current=$1077.16 return=-0.665%
- EQIX entry: fill=$1079.5 current=$1077.16 return=-0.217%
- EQIX exit: fill=$1078.442 current=$1077.16 return=-0.119%
- EQIX entry: fill=$1078.41 current=$1077.16 return=-0.116%
- JNJ entry: fill=$230.116 current=$230.04 return=-0.033%
- WMT entry: fill=$132.276 current=$132.345 return=+0.052%
- WMT entry: fill=$132.474 current=$132.345 return=-0.097%
- EQIX entry: fill=$1076.89 current=$1077.16 return=+0.025%
- EQIX entry: fill=$1076.82 current=$1077.16 return=+0.032%
- JNJ entry: fill=$230.044 current=$230.04 return=-0.002%
- EQIX exit: fill=$1076.718 current=$1077.16 return=+0.041%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T172342-3397bcc4`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 34/79 symbols blocked (43%). Avg spread (blocked): 5.424%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 13. Need 7 more fills before P/L analysis is meaningful.
- Average current return across 13 tracked outcome(s): -0.138%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 13 records (0 complete, 13 partial). 60 trigger fill associations recovered. 13 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=10, LIQUIDITY_GATE_V1=10, MOMENTUM_BLEND_6M_12M_V1=10, SPREAD_GATE_V1=10, STOCK_TREND_200DMA_V1=10.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T17:49:06Z

*From outcome_tracker run `outcome_tracker-20260514T174906-0396f2c0`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.12 return=-0.314%
- JNJ entry: fill=$230.248 current=$230.27 return=+0.010%
- EQIX entry: fill=$1084.37 current=$1078.06 return=-0.582%
- EQIX entry: fill=$1079.5 current=$1078.06 return=-0.133%
- EQIX exit: fill=$1078.442 current=$1078.06 return=-0.035%
- EQIX entry: fill=$1078.41 current=$1078.06 return=-0.033%
- JNJ entry: fill=$230.116 current=$230.27 return=+0.067%
- WMT entry: fill=$132.276 current=$132.73 return=+0.343%
- WMT entry: fill=$132.474 current=$132.73 return=+0.193%
- EQIX entry: fill=$1076.89 current=$1078.06 return=+0.109%
- EQIX entry: fill=$1076.82 current=$1078.06 return=+0.115%
- JNJ entry: fill=$230.044 current=$230.27 return=+0.098%
- EQIX exit: fill=$1076.718 current=$1078.06 return=+0.125%
- EQIX entry: fill=$1076.542 current=$1078.06 return=+0.141%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T174906-0396f2c0`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 33/79 symbols blocked (42%). Avg spread (blocked): 5.491%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +0.007%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 60 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=10, LIQUIDITY_GATE_V1=10, MOMENTUM_BLEND_6M_12M_V1=10, SPREAD_GATE_V1=10, STOCK_TREND_200DMA_V1=10.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T17:50:28Z

*From outcome_tracker run `outcome_tracker-20260514T175028-5d1f8063`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.135 return=-0.308%
- JNJ entry: fill=$230.248 current=$230.15 return=-0.043%
- EQIX entry: fill=$1084.37 current=$1077.825 return=-0.604%
- EQIX entry: fill=$1079.5 current=$1077.825 return=-0.155%
- EQIX exit: fill=$1078.442 current=$1077.825 return=-0.057%
- EQIX entry: fill=$1078.41 current=$1077.825 return=-0.054%
- JNJ entry: fill=$230.116 current=$230.15 return=+0.015%
- WMT entry: fill=$132.276 current=$132.735 return=+0.347%
- WMT entry: fill=$132.474 current=$132.735 return=+0.197%
- EQIX entry: fill=$1076.89 current=$1077.825 return=+0.087%
- EQIX entry: fill=$1076.82 current=$1077.825 return=+0.093%
- JNJ entry: fill=$230.044 current=$230.15 return=+0.046%
- EQIX exit: fill=$1076.718 current=$1077.825 return=+0.103%
- EQIX entry: fill=$1076.542 current=$1077.825 return=+0.119%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T175028-5d1f8063`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 28/79 symbols blocked (35%). Avg spread (blocked): 6.419%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -0.015%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 60 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=10, LIQUIDITY_GATE_V1=10, MOMENTUM_BLEND_6M_12M_V1=10, SPREAD_GATE_V1=10, STOCK_TREND_200DMA_V1=10.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T17:52:26Z

*From outcome_tracker run `outcome_tracker-20260514T175226-ca48b7d0`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.895 return=-0.417%
- JNJ entry: fill=$230.248 current=$230.14 return=-0.047%
- EQIX entry: fill=$1084.37 current=$1077.15 return=-0.666%
- EQIX entry: fill=$1079.5 current=$1077.15 return=-0.218%
- EQIX exit: fill=$1078.442 current=$1077.15 return=-0.120%
- EQIX entry: fill=$1078.41 current=$1077.15 return=-0.117%
- JNJ entry: fill=$230.116 current=$230.14 return=+0.010%
- WMT entry: fill=$132.276 current=$132.745 return=+0.355%
- WMT entry: fill=$132.474 current=$132.745 return=+0.205%
- EQIX entry: fill=$1076.89 current=$1077.15 return=+0.024%
- EQIX entry: fill=$1076.82 current=$1077.15 return=+0.031%
- JNJ entry: fill=$230.044 current=$230.14 return=+0.042%
- EQIX exit: fill=$1076.718 current=$1077.15 return=+0.040%
- EQIX entry: fill=$1076.542 current=$1077.15 return=+0.056%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T175226-ca48b7d0`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 29/79 symbols blocked (37%). Avg spread (blocked): 6.207%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -0.059%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 78 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=13, LIQUIDITY_GATE_V1=13, MOMENTUM_BLEND_6M_12M_V1=13, SPREAD_GATE_V1=13, STOCK_TREND_200DMA_V1=13.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T17:57:44Z

*From outcome_tracker run `outcome_tracker-20260514T175744-22c6744b`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.765 return=-0.477%
- JNJ entry: fill=$230.248 current=$229.87 return=-0.164%
- EQIX entry: fill=$1084.37 current=$1077.465 return=-0.637%
- EQIX entry: fill=$1079.5 current=$1077.465 return=-0.189%
- EQIX exit: fill=$1078.442 current=$1077.465 return=-0.091%
- EQIX entry: fill=$1078.41 current=$1077.465 return=-0.088%
- JNJ entry: fill=$230.116 current=$229.87 return=-0.107%
- WMT entry: fill=$132.276 current=$132.5601 return=+0.215%
- WMT entry: fill=$132.474 current=$132.5601 return=+0.065%
- EQIX entry: fill=$1076.89 current=$1077.465 return=+0.053%
- EQIX entry: fill=$1076.82 current=$1077.465 return=+0.060%
- JNJ entry: fill=$230.044 current=$229.87 return=-0.076%
- EQIX exit: fill=$1076.718 current=$1077.465 return=+0.069%
- EQIX entry: fill=$1076.542 current=$1077.465 return=+0.086%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T175744-22c6744b`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 32/79 symbols blocked (41%). Avg spread (blocked): 5.412%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -0.091%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 66 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T18:07:56Z

*From outcome_tracker run `outcome_tracker-20260514T180756-786bd07b`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.365 return=-0.659%
- JNJ entry: fill=$230.248 current=$229.826 return=-0.183%
- EQIX entry: fill=$1084.37 current=$1075.56 return=-0.812%
- EQIX entry: fill=$1079.5 current=$1075.56 return=-0.365%
- EQIX exit: fill=$1078.442 current=$1075.56 return=-0.267%
- EQIX entry: fill=$1078.41 current=$1075.56 return=-0.264%
- JNJ entry: fill=$230.116 current=$229.826 return=-0.126%
- WMT entry: fill=$132.276 current=$132.35 return=+0.056%
- WMT entry: fill=$132.474 current=$132.35 return=-0.094%
- EQIX entry: fill=$1076.89 current=$1075.56 return=-0.123%
- EQIX entry: fill=$1076.82 current=$1075.56 return=-0.117%
- JNJ entry: fill=$230.044 current=$229.826 return=-0.095%
- EQIX exit: fill=$1076.718 current=$1075.56 return=-0.107%
- EQIX entry: fill=$1076.542 current=$1075.56 return=-0.091%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T180756-786bd07b`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 28/79 symbols blocked (35%). Avg spread (blocked): 5.864%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -0.232%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 78 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=13, LIQUIDITY_GATE_V1=13, MOMENTUM_BLEND_6M_12M_V1=13, SPREAD_GATE_V1=13, STOCK_TREND_200DMA_V1=13.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T21:49:47Z

*From outcome_tracker run `outcome_tracker-20260514T214947-34139ff6`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.75 return=-0.483%
- JNJ entry: fill=$230.248 current=$230.8 return=+0.240%
- EQIX entry: fill=$1084.37 current=$1079.68 return=-0.432%
- EQIX entry: fill=$1079.5 current=$1079.68 return=+0.017%
- EQIX exit: fill=$1078.442 current=$1079.68 return=+0.115%
- EQIX entry: fill=$1078.41 current=$1079.68 return=+0.118%
- JNJ entry: fill=$230.116 current=$230.8 return=+0.297%
- WMT entry: fill=$132.276 current=$132.49 return=+0.162%
- WMT entry: fill=$132.474 current=$132.49 return=+0.012%
- EQIX entry: fill=$1076.89 current=$1079.68 return=+0.259%
- EQIX entry: fill=$1076.82 current=$1079.68 return=+0.266%
- JNJ entry: fill=$230.044 current=$230.8 return=+0.329%
- EQIX exit: fill=$1076.718 current=$1079.68 return=+0.275%
- EQIX entry: fill=$1076.542 current=$1079.68 return=+0.291%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T214947-34139ff6`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 56% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 44/79 symbols blocked (56%). Avg spread (blocked): 10.102%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +0.105%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 18 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T22:12:20Z

*From outcome_tracker run `outcome_tracker-20260514T221220-d3c04dca`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.75 return=-0.483%
- JNJ entry: fill=$230.248 current=$230.8 return=+0.240%
- EQIX entry: fill=$1084.37 current=$1079.68 return=-0.432%
- EQIX entry: fill=$1079.5 current=$1079.68 return=+0.017%
- EQIX exit: fill=$1078.442 current=$1079.68 return=+0.115%
- EQIX entry: fill=$1078.41 current=$1079.68 return=+0.118%
- JNJ entry: fill=$230.116 current=$230.8 return=+0.297%
- WMT entry: fill=$132.276 current=$132.49 return=+0.162%
- WMT entry: fill=$132.474 current=$132.49 return=+0.012%
- EQIX entry: fill=$1076.89 current=$1079.68 return=+0.259%
- EQIX entry: fill=$1076.82 current=$1079.68 return=+0.266%
- JNJ entry: fill=$230.044 current=$230.8 return=+0.329%
- EQIX exit: fill=$1076.718 current=$1079.68 return=+0.275%
- EQIX entry: fill=$1076.542 current=$1079.68 return=+0.291%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T221220-d3c04dca`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 56% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 44/79 symbols blocked (56%). Avg spread (blocked): 10.102%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +0.105%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 18 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-14T22:32:38Z

*From outcome_tracker run `outcome_tracker-20260514T223238-4f7bae5c`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.75 return=-0.483%
- JNJ entry: fill=$230.248 current=$230.8 return=+0.240%
- EQIX entry: fill=$1084.37 current=$1079.68 return=-0.432%
- EQIX entry: fill=$1079.5 current=$1079.68 return=+0.017%
- EQIX exit: fill=$1078.442 current=$1079.68 return=+0.115%
- EQIX entry: fill=$1078.41 current=$1079.68 return=+0.118%
- JNJ entry: fill=$230.116 current=$230.8 return=+0.297%
- WMT entry: fill=$132.276 current=$132.49 return=+0.162%
- WMT entry: fill=$132.474 current=$132.49 return=+0.012%
- EQIX entry: fill=$1076.89 current=$1079.68 return=+0.259%
- EQIX entry: fill=$1076.82 current=$1079.68 return=+0.266%
- JNJ entry: fill=$230.044 current=$230.8 return=+0.329%
- EQIX exit: fill=$1076.718 current=$1079.68 return=+0.275%
- EQIX entry: fill=$1076.542 current=$1079.68 return=+0.291%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-14

*From trigger_performance run `trigger_performance-20260514T223644-62ca6da0`*
*Period: 2026-05-08 to 2026-05-14 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 56% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 44/79 symbols blocked (56%). Avg spread (blocked): 10.102%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +0.105%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 18 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-15T21:41:04Z

*From outcome_tracker run `outcome_tracker-20260515T214104-e7913778`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$213.74 return=-2.316%
- JNJ entry: fill=$230.248 current=$227.3756 return=-1.248%
- EQIX entry: fill=$1084.37 current=$1060.0 return=-2.247%
- EQIX entry: fill=$1079.5 current=$1060.0 return=-1.806%
- EQIX exit: fill=$1078.442 current=$1060.0 return=-1.710%
- EQIX entry: fill=$1078.41 current=$1060.0 return=-1.707%
- JNJ entry: fill=$230.116 current=$227.3756 return=-1.191%
- WMT entry: fill=$132.276 current=$131.79 return=-0.367%
- WMT entry: fill=$132.474 current=$131.79 return=-0.516%
- EQIX entry: fill=$1076.89 current=$1060.0 return=-1.568%
- EQIX entry: fill=$1076.82 current=$1060.0 return=-1.562%
- JNJ entry: fill=$230.044 current=$227.3756 return=-1.160%
- EQIX exit: fill=$1076.718 current=$1060.0 return=-1.553%
- EQIX entry: fill=$1076.542 current=$1060.0 return=-1.537%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-15

*From trigger_performance run `trigger_performance-20260515T214104-e7913778`*
*Period: 2026-05-09 to 2026-05-15 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 57% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 0 risk-on (0%).
- Spread gate: 45/79 symbols blocked (57%). Avg spread (blocked): 10.222%
- Trend gate (200 DMA): 36/79 symbols below 200 DMA (46% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.464%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 50 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=10, LIQUIDITY_GATE_V1=10, MOMENTUM_BLEND_6M_12M_V1=10, SPREAD_GATE_V1=10, STOCK_TREND_200DMA_V1=10.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-15T22:00:12Z

*From outcome_tracker run `outcome_tracker-20260515T220012-2f7844b8`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$213.74 return=-2.316%
- JNJ entry: fill=$230.248 current=$227.3756 return=-1.248%
- EQIX entry: fill=$1084.37 current=$1060.0 return=-2.247%
- EQIX entry: fill=$1079.5 current=$1060.0 return=-1.806%
- EQIX exit: fill=$1078.442 current=$1060.0 return=-1.710%
- EQIX entry: fill=$1078.41 current=$1060.0 return=-1.707%
- JNJ entry: fill=$230.116 current=$227.3756 return=-1.191%
- WMT entry: fill=$132.276 current=$131.79 return=-0.367%
- WMT entry: fill=$132.474 current=$131.79 return=-0.516%
- EQIX entry: fill=$1076.89 current=$1060.0 return=-1.568%
- EQIX entry: fill=$1076.82 current=$1060.0 return=-1.562%
- JNJ entry: fill=$230.044 current=$227.3756 return=-1.160%
- EQIX exit: fill=$1076.718 current=$1060.0 return=-1.553%
- EQIX entry: fill=$1076.542 current=$1060.0 return=-1.537%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-15

*From trigger_performance run `trigger_performance-20260515T220012-2f7844b8`*
*Period: 2026-05-09 to 2026-05-15 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 57% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 45/79 symbols blocked (57%). Avg spread (blocked): 10.222%
- Trend gate (200 DMA): 36/79 symbols below 200 DMA (46% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.464%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 50 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=10, LIQUIDITY_GATE_V1=10, MOMENTUM_BLEND_6M_12M_V1=10, SPREAD_GATE_V1=10, STOCK_TREND_200DMA_V1=10.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-15T22:13:15Z

*From outcome_tracker run `outcome_tracker-20260515T221315-6e75adb7`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$213.74 return=-2.316%
- JNJ entry: fill=$230.248 current=$227.3756 return=-1.248%
- EQIX entry: fill=$1084.37 current=$1060.0 return=-2.247%
- EQIX entry: fill=$1079.5 current=$1060.0 return=-1.806%
- EQIX exit: fill=$1078.442 current=$1060.0 return=-1.710%
- EQIX entry: fill=$1078.41 current=$1060.0 return=-1.707%
- JNJ entry: fill=$230.116 current=$227.3756 return=-1.191%
- WMT entry: fill=$132.276 current=$131.79 return=-0.367%
- WMT entry: fill=$132.474 current=$131.79 return=-0.516%
- EQIX entry: fill=$1076.89 current=$1060.0 return=-1.568%
- EQIX entry: fill=$1076.82 current=$1060.0 return=-1.562%
- JNJ entry: fill=$230.044 current=$227.3756 return=-1.160%
- EQIX exit: fill=$1076.718 current=$1060.0 return=-1.553%
- EQIX entry: fill=$1076.542 current=$1060.0 return=-1.537%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Experiment Candidates — 2026-05-15

*From weekly review run weekly_review-2026-05-15*

**Operational issues to investigate:**
- [ ] Paper execution execution-20260513T193130-305917e5 had unexpected status: PAPER_ORDER_ERRORS
- [ ] Paper execution execution-20260514T134814-b4369954 had unexpected status: PAPER_FAIL
- [ ] Paper execution execution-20260514T135504-19cce5c5 had unexpected status: PAPER_FAIL
- [ ] Paper execution execution-20260514T150121-0f807e87 had unexpected status: PAPER_BLOCKED
- [ ] Paper execution execution-20260514T171953-fe151e9b had unexpected status: PAPER_BLOCKED
- [ ] Paper execution execution-20260514T174900-1d804822 had unexpected status: PAPER_BLOCKED
- [ ] Paper execution execution-20260514T175023-d2a85437 had unexpected status: PAPER_BLOCKED
- [ ] Paper execution execution-20260514T175221-05f9ad9c had unexpected status: PAPER_BLOCKED
- [ ] Paper execution execution-20260514T175739-c2e2d180 had unexpected status: PAPER_BLOCKED

**Observations (hypothesis candidates):**
- 23 paper execution attempt(s), 15 order(s) submitted.
- 14 order fill(s) confirmed by order monitor.
- 12 external alert(s) ingested this period, 5 routed.

**To propose a strategy experiment, open a PR with:**
- Hypothesis
- Supporting evidence (backtest or paper results)
- Success criteria
- Rollback plan

---
## Outcome Observations — 2026-05-18T21:50:59Z

*From outcome_tracker run `outcome_tracker-20260518T215059-9cc946e9`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$212.61 return=-2.833%
- JNJ entry: fill=$230.248 current=$228.88 return=-0.594%
- EQIX entry: fill=$1084.37 current=$1062.62 return=-2.006%
- EQIX entry: fill=$1079.5 current=$1062.62 return=-1.564%
- EQIX exit: fill=$1078.442 current=$1062.62 return=-1.467%
- EQIX entry: fill=$1078.41 current=$1062.62 return=-1.464%
- JNJ entry: fill=$230.116 current=$228.88 return=-0.537%
- WMT entry: fill=$132.276 current=$133.26 return=+0.744%
- WMT entry: fill=$132.474 current=$133.26 return=+0.593%
- EQIX entry: fill=$1076.89 current=$1062.62 return=-1.325%
- EQIX entry: fill=$1076.82 current=$1062.62 return=-1.319%
- JNJ entry: fill=$230.044 current=$228.88 return=-0.506%
- EQIX exit: fill=$1076.718 current=$1062.62 return=-1.309%
- EQIX entry: fill=$1076.542 current=$1062.62 return=-1.293%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-18

*From trigger_performance run `trigger_performance-20260518T215059-9cc946e9`*
*Period: 2026-05-12 to 2026-05-18 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.427%
- Trend gate (200 DMA): 35/79 symbols below 200 DMA (44% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.063%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 72 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=12, LIQUIDITY_GATE_V1=12, MOMENTUM_BLEND_6M_12M_V1=12, SPREAD_GATE_V1=12, STOCK_TREND_200DMA_V1=12.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-18T22:03:49Z

*From outcome_tracker run `outcome_tracker-20260518T220349-6b6f1b32`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$212.61 return=-2.833%
- JNJ entry: fill=$230.248 current=$228.88 return=-0.594%
- EQIX entry: fill=$1084.37 current=$1062.62 return=-2.006%
- EQIX entry: fill=$1079.5 current=$1062.62 return=-1.564%
- EQIX exit: fill=$1078.442 current=$1062.62 return=-1.467%
- EQIX entry: fill=$1078.41 current=$1062.62 return=-1.464%
- JNJ entry: fill=$230.116 current=$228.88 return=-0.537%
- WMT entry: fill=$132.276 current=$133.26 return=+0.744%
- WMT entry: fill=$132.474 current=$133.26 return=+0.593%
- EQIX entry: fill=$1076.89 current=$1062.62 return=-1.325%
- EQIX entry: fill=$1076.82 current=$1062.62 return=-1.319%
- JNJ entry: fill=$230.044 current=$228.88 return=-0.506%
- EQIX exit: fill=$1076.718 current=$1062.62 return=-1.309%
- EQIX entry: fill=$1076.542 current=$1062.62 return=-1.293%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-18

*From trigger_performance run `trigger_performance-20260518T220349-6b6f1b32`*
*Period: 2026-05-12 to 2026-05-18 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.427%
- Trend gate (200 DMA): 35/79 symbols below 200 DMA (44% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.063%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 72 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=12, LIQUIDITY_GATE_V1=12, MOMENTUM_BLEND_6M_12M_V1=12, SPREAD_GATE_V1=12, STOCK_TREND_200DMA_V1=12.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-18T22:15:28Z

*From outcome_tracker run `outcome_tracker-20260518T221528-a5d89d8f`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$212.61 return=-2.833%
- JNJ entry: fill=$230.248 current=$228.88 return=-0.594%
- EQIX entry: fill=$1084.37 current=$1062.62 return=-2.006%
- EQIX entry: fill=$1079.5 current=$1062.62 return=-1.564%
- EQIX exit: fill=$1078.442 current=$1062.62 return=-1.467%
- EQIX entry: fill=$1078.41 current=$1062.62 return=-1.464%
- JNJ entry: fill=$230.116 current=$228.88 return=-0.537%
- WMT entry: fill=$132.276 current=$133.26 return=+0.744%
- WMT entry: fill=$132.474 current=$133.26 return=+0.593%
- EQIX entry: fill=$1076.89 current=$1062.62 return=-1.325%
- EQIX entry: fill=$1076.82 current=$1062.62 return=-1.319%
- JNJ entry: fill=$230.044 current=$228.88 return=-0.506%
- EQIX exit: fill=$1076.718 current=$1062.62 return=-1.309%
- EQIX entry: fill=$1076.542 current=$1062.62 return=-1.293%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-18

*From trigger_performance run `trigger_performance-20260518T223242-2f07a5ca`*
*Period: 2026-05-12 to 2026-05-18 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.427%
- Trend gate (200 DMA): 35/79 symbols below 200 DMA (44% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.063%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 72 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=12, LIQUIDITY_GATE_V1=12, MOMENTUM_BLEND_6M_12M_V1=12, SPREAD_GATE_V1=12, STOCK_TREND_200DMA_V1=12.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-19T22:00:14Z

*From outcome_tracker run `outcome_tracker-20260519T220014-2791b0ae`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.0 return=-0.369%
- JNJ entry: fill=$230.248 current=$229.5752 return=-0.292%
- EQIX entry: fill=$1084.37 current=$1049.0 return=-3.262%
- EQIX entry: fill=$1079.5 current=$1049.0 return=-2.825%
- EQIX exit: fill=$1078.442 current=$1049.0 return=-2.730%
- EQIX entry: fill=$1078.41 current=$1049.0 return=-2.727%
- JNJ entry: fill=$230.116 current=$229.5752 return=-0.235%
- WMT entry: fill=$132.276 current=$134.19 return=+1.447%
- WMT entry: fill=$132.474 current=$134.19 return=+1.295%
- EQIX entry: fill=$1076.89 current=$1049.0 return=-2.590%
- EQIX entry: fill=$1076.82 current=$1049.0 return=-2.583%
- JNJ entry: fill=$230.044 current=$229.5752 return=-0.204%
- EQIX exit: fill=$1076.718 current=$1049.0 return=-2.574%
- EQIX entry: fill=$1076.542 current=$1049.0 return=-2.558%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-19

*From trigger_performance run `trigger_performance-20260519T220014-2791b0ae`*
*Period: 2026-05-13 to 2026-05-19 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 68% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 0 risk-on (0%).
- Spread gate: 54/79 symbols blocked (68%). Avg spread (blocked): 10.053%
- Trend gate (200 DMA): 37/79 symbols below 200 DMA (47% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.444%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 55 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-19T22:17:18Z

*From outcome_tracker run `outcome_tracker-20260519T221718-6eb465ae`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.0 return=-0.369%
- JNJ entry: fill=$230.248 current=$229.5752 return=-0.292%
- EQIX entry: fill=$1084.37 current=$1049.0 return=-3.262%
- EQIX entry: fill=$1079.5 current=$1049.0 return=-2.825%
- EQIX exit: fill=$1078.442 current=$1049.0 return=-2.730%
- EQIX entry: fill=$1078.41 current=$1049.0 return=-2.727%
- JNJ entry: fill=$230.116 current=$229.5752 return=-0.235%
- WMT entry: fill=$132.276 current=$134.19 return=+1.447%
- WMT entry: fill=$132.474 current=$134.19 return=+1.295%
- EQIX entry: fill=$1076.89 current=$1049.0 return=-2.590%
- EQIX entry: fill=$1076.82 current=$1049.0 return=-2.583%
- JNJ entry: fill=$230.044 current=$229.5752 return=-0.204%
- EQIX exit: fill=$1076.718 current=$1049.0 return=-2.574%
- EQIX entry: fill=$1076.542 current=$1049.0 return=-2.558%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-19

*From trigger_performance run `trigger_performance-20260519T221718-6eb465ae`*
*Period: 2026-05-13 to 2026-05-19 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 68% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 54/79 symbols blocked (68%). Avg spread (blocked): 10.053%
- Trend gate (200 DMA): 37/79 symbols below 200 DMA (47% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.444%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 55 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-19T22:40:20Z

*From outcome_tracker run `outcome_tracker-20260519T224020-0db7e321`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.0 return=-0.369%
- JNJ entry: fill=$230.248 current=$229.5752 return=-0.292%
- EQIX entry: fill=$1084.37 current=$1049.0 return=-3.262%
- EQIX entry: fill=$1079.5 current=$1049.0 return=-2.825%
- EQIX exit: fill=$1078.442 current=$1049.0 return=-2.730%
- EQIX entry: fill=$1078.41 current=$1049.0 return=-2.727%
- JNJ entry: fill=$230.116 current=$229.5752 return=-0.235%
- WMT entry: fill=$132.276 current=$134.19 return=+1.447%
- WMT entry: fill=$132.474 current=$134.19 return=+1.295%
- EQIX entry: fill=$1076.89 current=$1049.0 return=-2.590%
- EQIX entry: fill=$1076.82 current=$1049.0 return=-2.583%
- JNJ entry: fill=$230.044 current=$229.5752 return=-0.204%
- EQIX exit: fill=$1076.718 current=$1049.0 return=-2.574%
- EQIX entry: fill=$1076.542 current=$1049.0 return=-2.558%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-19

*From trigger_performance run `trigger_performance-20260519T224435-e940f1e3`*
*Period: 2026-05-13 to 2026-05-19 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 68% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 54/79 symbols blocked (68%). Avg spread (blocked): 10.053%
- Trend gate (200 DMA): 37/79 symbols below 200 DMA (47% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.444%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 55 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-20T22:15:23Z

*From outcome_tracker run `outcome_tracker-20260520T221523-9ded7818`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.99 return=-0.374%
- JNJ entry: fill=$230.248 current=$229.28 return=-0.420%
- EQIX entry: fill=$1084.37 current=$1063.0 return=-1.971%
- EQIX entry: fill=$1079.5 current=$1063.0 return=-1.528%
- EQIX exit: fill=$1078.442 current=$1063.0 return=-1.432%
- EQIX entry: fill=$1078.41 current=$1063.0 return=-1.429%
- JNJ entry: fill=$230.116 current=$229.28 return=-0.363%
- WMT entry: fill=$132.276 current=$131.26 return=-0.768%
- WMT entry: fill=$132.474 current=$131.26 return=-0.916%
- EQIX entry: fill=$1076.89 current=$1063.0 return=-1.290%
- EQIX entry: fill=$1076.82 current=$1063.0 return=-1.283%
- JNJ entry: fill=$230.044 current=$229.28 return=-0.332%
- EQIX exit: fill=$1076.718 current=$1063.0 return=-1.274%
- EQIX entry: fill=$1076.542 current=$1063.0 return=-1.258%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-20

*From trigger_performance run `trigger_performance-20260520T221523-9ded7818`*
*Period: 2026-05-14 to 2026-05-20 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 10.575%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.046%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 30 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=5, LIQUIDITY_GATE_V1=5, MOMENTUM_BLEND_6M_12M_V1=5, SPREAD_GATE_V1=5, STOCK_TREND_200DMA_V1=5.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-20T22:24:31Z

*From outcome_tracker run `outcome_tracker-20260520T222431-6880f16d`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.99 return=-0.374%
- JNJ entry: fill=$230.248 current=$229.28 return=-0.420%
- EQIX entry: fill=$1084.37 current=$1063.0 return=-1.971%
- EQIX entry: fill=$1079.5 current=$1063.0 return=-1.528%
- EQIX exit: fill=$1078.442 current=$1063.0 return=-1.432%
- EQIX entry: fill=$1078.41 current=$1063.0 return=-1.429%
- JNJ entry: fill=$230.116 current=$229.28 return=-0.363%
- WMT entry: fill=$132.276 current=$131.26 return=-0.768%
- WMT entry: fill=$132.474 current=$131.26 return=-0.916%
- EQIX entry: fill=$1076.89 current=$1063.0 return=-1.290%
- EQIX entry: fill=$1076.82 current=$1063.0 return=-1.283%
- JNJ entry: fill=$230.044 current=$229.28 return=-0.332%
- EQIX exit: fill=$1076.718 current=$1063.0 return=-1.274%
- EQIX entry: fill=$1076.542 current=$1063.0 return=-1.258%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-20

*From trigger_performance run `trigger_performance-20260520T222431-6880f16d`*
*Period: 2026-05-14 to 2026-05-20 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 10.575%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.046%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 30 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=5, LIQUIDITY_GATE_V1=5, MOMENTUM_BLEND_6M_12M_V1=5, SPREAD_GATE_V1=5, STOCK_TREND_200DMA_V1=5.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-20T22:45:32Z

*From outcome_tracker run `outcome_tracker-20260520T224532-a4da27d9`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.99 return=-0.374%
- JNJ entry: fill=$230.248 current=$229.28 return=-0.420%
- EQIX entry: fill=$1084.37 current=$1063.0 return=-1.971%
- EQIX entry: fill=$1079.5 current=$1063.0 return=-1.528%
- EQIX exit: fill=$1078.442 current=$1063.0 return=-1.432%
- EQIX entry: fill=$1078.41 current=$1063.0 return=-1.429%
- JNJ entry: fill=$230.116 current=$229.28 return=-0.363%
- WMT entry: fill=$132.276 current=$131.26 return=-0.768%
- WMT entry: fill=$132.474 current=$131.26 return=-0.916%
- EQIX entry: fill=$1076.89 current=$1063.0 return=-1.290%
- EQIX entry: fill=$1076.82 current=$1063.0 return=-1.283%
- JNJ entry: fill=$230.044 current=$229.28 return=-0.332%
- EQIX exit: fill=$1076.718 current=$1063.0 return=-1.274%
- EQIX entry: fill=$1076.542 current=$1063.0 return=-1.258%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-20

*From trigger_performance run `trigger_performance-20260520T225138-20b1a1a1`*
*Period: 2026-05-14 to 2026-05-20 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 10.575%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.046%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 30 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=5, LIQUIDITY_GATE_V1=5, MOMENTUM_BLEND_6M_12M_V1=5, SPREAD_GATE_V1=5, STOCK_TREND_200DMA_V1=5.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-21T22:05:34Z

*From outcome_tracker run `outcome_tracker-20260521T220534-9e42e720`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$216.01 return=-1.279%
- JNJ entry: fill=$230.248 current=$231.68 return=+0.622%
- EQIX entry: fill=$1084.37 current=$1072.92 return=-1.056%
- EQIX entry: fill=$1079.5 current=$1072.92 return=-0.609%
- EQIX exit: fill=$1078.442 current=$1072.92 return=-0.512%
- EQIX entry: fill=$1078.41 current=$1072.92 return=-0.509%
- JNJ entry: fill=$230.116 current=$231.68 return=+0.680%
- WMT entry: fill=$132.276 current=$121.8 return=-7.920%
- WMT entry: fill=$132.474 current=$121.8 return=-8.057%
- EQIX entry: fill=$1076.89 current=$1072.92 return=-0.369%
- EQIX entry: fill=$1076.82 current=$1072.92 return=-0.362%
- JNJ entry: fill=$230.044 current=$231.68 return=+0.711%
- EQIX exit: fill=$1076.718 current=$1072.92 return=-0.353%
- EQIX entry: fill=$1076.542 current=$1072.92 return=-0.336%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-21

*From trigger_performance run `trigger_performance-20260521T220534-9e42e720`*
*Period: 2026-05-15 to 2026-05-21 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 10.753%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.382%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 30 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=5, LIQUIDITY_GATE_V1=5, MOMENTUM_BLEND_6M_12M_V1=5, SPREAD_GATE_V1=5, STOCK_TREND_200DMA_V1=5.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-21T22:19:51Z

*From outcome_tracker run `outcome_tracker-20260521T221951-2d32a116`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$216.01 return=-1.279%
- JNJ entry: fill=$230.248 current=$231.68 return=+0.622%
- EQIX entry: fill=$1084.37 current=$1072.92 return=-1.056%
- EQIX entry: fill=$1079.5 current=$1072.92 return=-0.609%
- EQIX exit: fill=$1078.442 current=$1072.92 return=-0.512%
- EQIX entry: fill=$1078.41 current=$1072.92 return=-0.509%
- JNJ entry: fill=$230.116 current=$231.68 return=+0.680%
- WMT entry: fill=$132.276 current=$121.8 return=-7.920%
- WMT entry: fill=$132.474 current=$121.8 return=-8.057%
- EQIX entry: fill=$1076.89 current=$1072.92 return=-0.369%
- EQIX entry: fill=$1076.82 current=$1072.92 return=-0.362%
- JNJ entry: fill=$230.044 current=$231.68 return=+0.711%
- EQIX exit: fill=$1076.718 current=$1072.92 return=-0.353%
- EQIX entry: fill=$1076.542 current=$1072.92 return=-0.336%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-21

*From trigger_performance run `trigger_performance-20260521T221951-2d32a116`*
*Period: 2026-05-15 to 2026-05-21 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 10.753%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.382%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 30 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=5, LIQUIDITY_GATE_V1=5, MOMENTUM_BLEND_6M_12M_V1=5, SPREAD_GATE_V1=5, STOCK_TREND_200DMA_V1=5.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-21T22:43:49Z

*From outcome_tracker run `outcome_tracker-20260521T224349-b468dff4`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$216.01 return=-1.279%
- JNJ entry: fill=$230.248 current=$231.68 return=+0.622%
- EQIX entry: fill=$1084.37 current=$1072.92 return=-1.056%
- EQIX entry: fill=$1079.5 current=$1072.92 return=-0.609%
- EQIX exit: fill=$1078.442 current=$1072.92 return=-0.512%
- EQIX entry: fill=$1078.41 current=$1072.92 return=-0.509%
- JNJ entry: fill=$230.116 current=$231.68 return=+0.680%
- WMT entry: fill=$132.276 current=$121.8 return=-7.920%
- WMT entry: fill=$132.474 current=$121.8 return=-8.057%
- EQIX entry: fill=$1076.89 current=$1072.92 return=-0.369%
- EQIX entry: fill=$1076.82 current=$1072.92 return=-0.362%
- JNJ entry: fill=$230.044 current=$231.68 return=+0.711%
- EQIX exit: fill=$1076.718 current=$1072.92 return=-0.353%
- EQIX entry: fill=$1076.542 current=$1072.92 return=-0.336%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-21

*From trigger_performance run `trigger_performance-20260521T224905-f2206457`*
*Period: 2026-05-15 to 2026-05-21 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 10.753%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.382%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 30 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=5, LIQUIDITY_GATE_V1=5, MOMENTUM_BLEND_6M_12M_V1=5, SPREAD_GATE_V1=5, STOCK_TREND_200DMA_V1=5.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
