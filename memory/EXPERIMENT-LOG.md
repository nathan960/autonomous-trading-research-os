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
## Outcome Observations — 2026-05-22T21:51:48Z

*From outcome_tracker run `outcome_tracker-20260522T215148-7373ee95`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$216.17 return=-1.206%
- JNJ entry: fill=$230.248 current=$234.35 return=+1.782%
- EQIX entry: fill=$1084.37 current=$1079.79 return=-0.422%
- EQIX entry: fill=$1079.5 current=$1079.79 return=+0.027%
- EQIX exit: fill=$1078.442 current=$1079.79 return=+0.125%
- EQIX entry: fill=$1078.41 current=$1079.79 return=+0.128%
- JNJ entry: fill=$230.116 current=$234.35 return=+1.840%
- WMT entry: fill=$132.276 current=$120.07 return=-9.228%
- WMT entry: fill=$132.474 current=$120.07 return=-9.363%
- EQIX entry: fill=$1076.89 current=$1079.79 return=+0.269%
- EQIX entry: fill=$1076.82 current=$1079.79 return=+0.276%
- JNJ entry: fill=$230.044 current=$234.35 return=+1.872%
- EQIX exit: fill=$1076.718 current=$1079.79 return=+0.285%
- EQIX entry: fill=$1076.542 current=$1079.79 return=+0.302%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-22

*From trigger_performance run `trigger_performance-20260522T215148-7373ee95`*
*Period: 2026-05-16 to 2026-05-22 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 73% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 58/79 symbols blocked (73%). Avg spread (blocked): 10.608%
- Trend gate (200 DMA): 31/79 symbols below 200 DMA (39% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -0.951%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 12 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=2, LIQUIDITY_GATE_V1=2, MOMENTUM_BLEND_6M_12M_V1=2, SPREAD_GATE_V1=2, STOCK_TREND_200DMA_V1=2.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-22T22:08:26Z

*From outcome_tracker run `outcome_tracker-20260522T220826-2b8c11a4`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$216.17 return=-1.206%
- JNJ entry: fill=$230.248 current=$234.35 return=+1.782%
- EQIX entry: fill=$1084.37 current=$1079.79 return=-0.422%
- EQIX entry: fill=$1079.5 current=$1079.79 return=+0.027%
- EQIX exit: fill=$1078.442 current=$1079.79 return=+0.125%
- EQIX entry: fill=$1078.41 current=$1079.79 return=+0.128%
- JNJ entry: fill=$230.116 current=$234.35 return=+1.840%
- WMT entry: fill=$132.276 current=$120.07 return=-9.228%
- WMT entry: fill=$132.474 current=$120.07 return=-9.363%
- EQIX entry: fill=$1076.89 current=$1079.79 return=+0.269%
- EQIX entry: fill=$1076.82 current=$1079.79 return=+0.276%
- JNJ entry: fill=$230.044 current=$234.35 return=+1.872%
- EQIX exit: fill=$1076.718 current=$1079.79 return=+0.285%
- EQIX entry: fill=$1076.542 current=$1079.79 return=+0.302%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-22

*From trigger_performance run `trigger_performance-20260522T220826-2b8c11a4`*
*Period: 2026-05-16 to 2026-05-22 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 73% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 58/79 symbols blocked (73%). Avg spread (blocked): 10.608%
- Trend gate (200 DMA): 31/79 symbols below 200 DMA (39% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -0.951%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 12 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=2, LIQUIDITY_GATE_V1=2, MOMENTUM_BLEND_6M_12M_V1=2, SPREAD_GATE_V1=2, STOCK_TREND_200DMA_V1=2.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-22T22:17:19Z

*From outcome_tracker run `outcome_tracker-20260522T221719-939a8e03`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$216.17 return=-1.206%
- JNJ entry: fill=$230.248 current=$234.35 return=+1.782%
- EQIX entry: fill=$1084.37 current=$1079.79 return=-0.422%
- EQIX entry: fill=$1079.5 current=$1079.79 return=+0.027%
- EQIX exit: fill=$1078.442 current=$1079.79 return=+0.125%
- EQIX entry: fill=$1078.41 current=$1079.79 return=+0.128%
- JNJ entry: fill=$230.116 current=$234.35 return=+1.840%
- WMT entry: fill=$132.276 current=$120.07 return=-9.228%
- WMT entry: fill=$132.474 current=$120.07 return=-9.363%
- EQIX entry: fill=$1076.89 current=$1079.79 return=+0.269%
- EQIX entry: fill=$1076.82 current=$1079.79 return=+0.276%
- JNJ entry: fill=$230.044 current=$234.35 return=+1.872%
- EQIX exit: fill=$1076.718 current=$1079.79 return=+0.285%
- EQIX entry: fill=$1076.542 current=$1079.79 return=+0.302%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Experiment Candidates — 2026-05-22

*From weekly review run weekly_review-2026-05-22*

**Observations (hypothesis candidates):**
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.
- 9 external alert(s) ingested this period, 0 routed.

**To propose a strategy experiment, open a PR with:**
- Hypothesis
- Supporting evidence (backtest or paper results)
- Success criteria
- Rollback plan

---
## Outcome Observations — 2026-05-25T21:50:50Z

*From outcome_tracker run `outcome_tracker-20260525T215050-24e09eed`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$216.17 return=-1.206%
- JNJ entry: fill=$230.248 current=$234.34 return=+1.777%
- EQIX entry: fill=$1084.37 current=$1079.79 return=-0.422%
- EQIX entry: fill=$1079.5 current=$1079.79 return=+0.027%
- EQIX exit: fill=$1078.442 current=$1079.79 return=+0.125%
- EQIX entry: fill=$1078.41 current=$1079.79 return=+0.128%
- JNJ entry: fill=$230.116 current=$234.34 return=+1.836%
- WMT entry: fill=$132.276 current=$120.27 return=-9.076%
- WMT entry: fill=$132.474 current=$120.27 return=-9.212%
- EQIX entry: fill=$1076.89 current=$1079.79 return=+0.269%
- EQIX entry: fill=$1076.82 current=$1079.79 return=+0.276%
- JNJ entry: fill=$230.044 current=$234.34 return=+1.868%
- EQIX exit: fill=$1076.718 current=$1079.79 return=+0.285%
- EQIX entry: fill=$1076.542 current=$1079.79 return=+0.302%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-25

*From trigger_performance run `trigger_performance-20260525T215050-24e09eed`*
*Period: 2026-05-19 to 2026-05-25 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 73% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 58/79 symbols blocked (73%). Avg spread (blocked): 10.608%
- Trend gate (200 DMA): 31/79 symbols below 200 DMA (39% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -0.930%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 12 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=2, LIQUIDITY_GATE_V1=2, MOMENTUM_BLEND_6M_12M_V1=2, SPREAD_GATE_V1=2, STOCK_TREND_200DMA_V1=2.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-25T22:09:18Z

*From outcome_tracker run `outcome_tracker-20260525T220918-116f7da7`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$216.17 return=-1.206%
- JNJ entry: fill=$230.248 current=$234.34 return=+1.777%
- EQIX entry: fill=$1084.37 current=$1079.79 return=-0.422%
- EQIX entry: fill=$1079.5 current=$1079.79 return=+0.027%
- EQIX exit: fill=$1078.442 current=$1079.79 return=+0.125%
- EQIX entry: fill=$1078.41 current=$1079.79 return=+0.128%
- JNJ entry: fill=$230.116 current=$234.34 return=+1.836%
- WMT entry: fill=$132.276 current=$120.27 return=-9.076%
- WMT entry: fill=$132.474 current=$120.27 return=-9.212%
- EQIX entry: fill=$1076.89 current=$1079.79 return=+0.269%
- EQIX entry: fill=$1076.82 current=$1079.79 return=+0.276%
- JNJ entry: fill=$230.044 current=$234.34 return=+1.868%
- EQIX exit: fill=$1076.718 current=$1079.79 return=+0.285%
- EQIX entry: fill=$1076.542 current=$1079.79 return=+0.302%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-25

*From trigger_performance run `trigger_performance-20260525T220918-116f7da7`*
*Period: 2026-05-19 to 2026-05-25 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 73% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 58/79 symbols blocked (73%). Avg spread (blocked): 10.608%
- Trend gate (200 DMA): 31/79 symbols below 200 DMA (39% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -0.930%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 12 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=2, LIQUIDITY_GATE_V1=2, MOMENTUM_BLEND_6M_12M_V1=2, SPREAD_GATE_V1=2, STOCK_TREND_200DMA_V1=2.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-25T22:18:59Z

*From outcome_tracker run `outcome_tracker-20260525T221859-a21941d4`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$216.17 return=-1.206%
- JNJ entry: fill=$230.248 current=$234.34 return=+1.777%
- EQIX entry: fill=$1084.37 current=$1079.79 return=-0.422%
- EQIX entry: fill=$1079.5 current=$1079.79 return=+0.027%
- EQIX exit: fill=$1078.442 current=$1079.79 return=+0.125%
- EQIX entry: fill=$1078.41 current=$1079.79 return=+0.128%
- JNJ entry: fill=$230.116 current=$234.34 return=+1.836%
- WMT entry: fill=$132.276 current=$120.27 return=-9.076%
- WMT entry: fill=$132.474 current=$120.27 return=-9.212%
- EQIX entry: fill=$1076.89 current=$1079.79 return=+0.269%
- EQIX entry: fill=$1076.82 current=$1079.79 return=+0.276%
- JNJ entry: fill=$230.044 current=$234.34 return=+1.868%
- EQIX exit: fill=$1076.718 current=$1079.79 return=+0.285%
- EQIX entry: fill=$1076.542 current=$1079.79 return=+0.302%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-25

*From trigger_performance run `trigger_performance-20260525T223411-6722976f`*
*Period: 2026-05-19 to 2026-05-25 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 73% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 58/79 symbols blocked (73%). Avg spread (blocked): 10.608%
- Trend gate (200 DMA): 31/79 symbols below 200 DMA (39% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -0.930%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 12 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=2, LIQUIDITY_GATE_V1=2, MOMENTUM_BLEND_6M_12M_V1=2, SPREAD_GATE_V1=2, STOCK_TREND_200DMA_V1=2.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-26T22:11:52Z

*From outcome_tracker run `outcome_tracker-20260526T221152-8901247a`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.13 return=-0.310%
- JNJ entry: fill=$230.248 current=$230.0686 return=-0.078%
- EQIX entry: fill=$1084.37 current=$1075.0 return=-0.864%
- EQIX entry: fill=$1079.5 current=$1075.0 return=-0.417%
- EQIX exit: fill=$1078.442 current=$1075.0 return=-0.319%
- EQIX entry: fill=$1078.41 current=$1075.0 return=-0.316%
- JNJ entry: fill=$230.116 current=$230.0686 return=-0.021%
- WMT entry: fill=$132.276 current=$118.5015 return=-10.414%
- WMT entry: fill=$132.474 current=$118.5015 return=-10.547%
- EQIX entry: fill=$1076.89 current=$1075.0 return=-0.176%
- EQIX entry: fill=$1076.82 current=$1075.0 return=-0.169%
- JNJ entry: fill=$230.044 current=$230.0686 return=+0.011%
- EQIX exit: fill=$1076.718 current=$1075.0 return=-0.160%
- EQIX entry: fill=$1076.542 current=$1075.0 return=-0.143%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-26

*From trigger_performance run `trigger_performance-20260526T221153-0ead38f6`*
*Period: 2026-05-20 to 2026-05-26 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 9.990%
- Trend gate (200 DMA): 30/79 symbols below 200 DMA (38% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.709%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-26T22:20:08Z

*From outcome_tracker run `outcome_tracker-20260526T222008-5ccc60aa`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.13 return=-0.310%
- JNJ entry: fill=$230.248 current=$230.0686 return=-0.078%
- EQIX entry: fill=$1084.37 current=$1075.0 return=-0.864%
- EQIX entry: fill=$1079.5 current=$1075.0 return=-0.417%
- EQIX exit: fill=$1078.442 current=$1075.0 return=-0.319%
- EQIX entry: fill=$1078.41 current=$1075.0 return=-0.316%
- JNJ entry: fill=$230.116 current=$230.0686 return=-0.021%
- WMT entry: fill=$132.276 current=$118.5015 return=-10.414%
- WMT entry: fill=$132.474 current=$118.5015 return=-10.547%
- EQIX entry: fill=$1076.89 current=$1075.0 return=-0.176%
- EQIX entry: fill=$1076.82 current=$1075.0 return=-0.169%
- JNJ entry: fill=$230.044 current=$230.0686 return=+0.011%
- EQIX exit: fill=$1076.718 current=$1075.0 return=-0.160%
- EQIX entry: fill=$1076.542 current=$1075.0 return=-0.143%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-26

*From trigger_performance run `trigger_performance-20260526T222008-5ccc60aa`*
*Period: 2026-05-20 to 2026-05-26 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 9.990%
- Trend gate (200 DMA): 30/79 symbols below 200 DMA (38% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.709%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-26T22:41:10Z

*From outcome_tracker run `outcome_tracker-20260526T224110-79ebccdb`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$218.13 return=-0.310%
- JNJ entry: fill=$230.248 current=$230.0686 return=-0.078%
- EQIX entry: fill=$1084.37 current=$1075.0 return=-0.864%
- EQIX entry: fill=$1079.5 current=$1075.0 return=-0.417%
- EQIX exit: fill=$1078.442 current=$1075.0 return=-0.319%
- EQIX entry: fill=$1078.41 current=$1075.0 return=-0.316%
- JNJ entry: fill=$230.116 current=$230.0686 return=-0.021%
- WMT entry: fill=$132.276 current=$118.5015 return=-10.414%
- WMT entry: fill=$132.474 current=$118.5015 return=-10.547%
- EQIX entry: fill=$1076.89 current=$1075.0 return=-0.176%
- EQIX entry: fill=$1076.82 current=$1075.0 return=-0.169%
- JNJ entry: fill=$230.044 current=$230.0686 return=+0.011%
- EQIX exit: fill=$1076.718 current=$1075.0 return=-0.160%
- EQIX entry: fill=$1076.542 current=$1075.0 return=-0.143%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-26

*From trigger_performance run `trigger_performance-20260526T224806-7e2123a0`*
*Period: 2026-05-20 to 2026-05-26 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 9.990%
- Trend gate (200 DMA): 30/79 symbols below 200 DMA (38% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.709%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-27T22:22:29Z

*From outcome_tracker run `outcome_tracker-20260527T222229-0ccab35c`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$214.18 return=-2.115%
- JNJ entry: fill=$230.248 current=$231.14 return=+0.387%
- EQIX entry: fill=$1084.37 current=$1070.22 return=-1.305%
- EQIX entry: fill=$1079.5 current=$1070.22 return=-0.860%
- EQIX exit: fill=$1078.442 current=$1070.22 return=-0.762%
- EQIX entry: fill=$1078.41 current=$1070.22 return=-0.760%
- JNJ entry: fill=$230.116 current=$231.14 return=+0.445%
- WMT entry: fill=$132.276 current=$118.82 return=-10.173%
- WMT entry: fill=$132.474 current=$118.82 return=-10.307%
- EQIX entry: fill=$1076.89 current=$1070.22 return=-0.619%
- EQIX entry: fill=$1076.82 current=$1070.22 return=-0.613%
- JNJ entry: fill=$230.044 current=$231.14 return=+0.476%
- EQIX exit: fill=$1076.718 current=$1070.22 return=-0.604%
- EQIX entry: fill=$1076.542 current=$1070.22 return=-0.587%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-27

*From trigger_performance run `trigger_performance-20260527T222229-0ccab35c`*
*Period: 2026-05-21 to 2026-05-27 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 9.749%
- Trend gate (200 DMA): 32/79 symbols below 200 DMA (41% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.957%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-27T22:41:33Z

*From outcome_tracker run `outcome_tracker-20260527T224133-47dabb4b`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$214.18 return=-2.115%
- JNJ entry: fill=$230.248 current=$231.14 return=+0.387%
- EQIX entry: fill=$1084.37 current=$1070.22 return=-1.305%
- EQIX entry: fill=$1079.5 current=$1070.22 return=-0.860%
- EQIX exit: fill=$1078.442 current=$1070.22 return=-0.762%
- EQIX entry: fill=$1078.41 current=$1070.22 return=-0.760%
- JNJ entry: fill=$230.116 current=$231.14 return=+0.445%
- WMT entry: fill=$132.276 current=$118.82 return=-10.173%
- WMT entry: fill=$132.474 current=$118.82 return=-10.307%
- EQIX entry: fill=$1076.89 current=$1070.22 return=-0.619%
- EQIX entry: fill=$1076.82 current=$1070.22 return=-0.613%
- JNJ entry: fill=$230.044 current=$231.14 return=+0.476%
- EQIX exit: fill=$1076.718 current=$1070.22 return=-0.604%
- EQIX entry: fill=$1076.542 current=$1070.22 return=-0.587%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-27

*From trigger_performance run `trigger_performance-20260527T224133-47dabb4b`*
*Period: 2026-05-21 to 2026-05-27 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 9.749%
- Trend gate (200 DMA): 32/79 symbols below 200 DMA (41% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.957%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-27T22:52:25Z

*From outcome_tracker run `outcome_tracker-20260527T225225-4f23147c`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$214.18 return=-2.115%
- JNJ entry: fill=$230.248 current=$231.14 return=+0.387%
- EQIX entry: fill=$1084.37 current=$1070.22 return=-1.305%
- EQIX entry: fill=$1079.5 current=$1070.22 return=-0.860%
- EQIX exit: fill=$1078.442 current=$1070.22 return=-0.762%
- EQIX entry: fill=$1078.41 current=$1070.22 return=-0.760%
- JNJ entry: fill=$230.116 current=$231.14 return=+0.445%
- WMT entry: fill=$132.276 current=$118.82 return=-10.173%
- WMT entry: fill=$132.474 current=$118.82 return=-10.307%
- EQIX entry: fill=$1076.89 current=$1070.22 return=-0.619%
- EQIX entry: fill=$1076.82 current=$1070.22 return=-0.613%
- JNJ entry: fill=$230.044 current=$231.14 return=+0.476%
- EQIX exit: fill=$1076.718 current=$1070.22 return=-0.604%
- EQIX entry: fill=$1076.542 current=$1070.22 return=-0.587%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-27

*From trigger_performance run `trigger_performance-20260527T225613-6aaa7549`*
*Period: 2026-05-21 to 2026-05-27 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 9.749%
- Trend gate (200 DMA): 32/79 symbols below 200 DMA (41% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.957%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-28T22:21:35Z

*From outcome_tracker run `outcome_tracker-20260528T222135-e1d46794`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$210.29 return=-3.893%
- JNJ entry: fill=$230.248 current=$231.0 return=+0.327%
- EQIX entry: fill=$1084.37 current=$1069.35 return=-1.385%
- EQIX entry: fill=$1079.5 current=$1069.35 return=-0.940%
- EQIX exit: fill=$1078.442 current=$1069.35 return=-0.843%
- EQIX entry: fill=$1078.41 current=$1069.35 return=-0.840%
- JNJ entry: fill=$230.116 current=$231.0 return=+0.384%
- WMT entry: fill=$132.276 current=$118.48 return=-10.430%
- WMT entry: fill=$132.474 current=$118.48 return=-10.564%
- EQIX entry: fill=$1076.89 current=$1069.35 return=-0.700%
- EQIX entry: fill=$1076.82 current=$1069.35 return=-0.694%
- JNJ entry: fill=$230.044 current=$231.0 return=+0.416%
- EQIX exit: fill=$1076.718 current=$1069.35 return=-0.684%
- EQIX entry: fill=$1076.542 current=$1069.35 return=-0.668%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-28

*From trigger_performance run `trigger_performance-20260528T222135-e1d46794`*
*Period: 2026-05-22 to 2026-05-28 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 68% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 54/79 symbols blocked (68%). Avg spread (blocked): 10.373%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.180%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 66 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-28T22:41:50Z

*From outcome_tracker run `outcome_tracker-20260528T224150-ffa82f3b`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$210.29 return=-3.893%
- JNJ entry: fill=$230.248 current=$231.0 return=+0.327%
- EQIX entry: fill=$1084.37 current=$1069.35 return=-1.385%
- EQIX entry: fill=$1079.5 current=$1069.35 return=-0.940%
- EQIX exit: fill=$1078.442 current=$1069.35 return=-0.843%
- EQIX entry: fill=$1078.41 current=$1069.35 return=-0.840%
- JNJ entry: fill=$230.116 current=$231.0 return=+0.384%
- WMT entry: fill=$132.276 current=$118.48 return=-10.430%
- WMT entry: fill=$132.474 current=$118.48 return=-10.564%
- EQIX entry: fill=$1076.89 current=$1069.35 return=-0.700%
- EQIX entry: fill=$1076.82 current=$1069.35 return=-0.694%
- JNJ entry: fill=$230.044 current=$231.0 return=+0.416%
- EQIX exit: fill=$1076.718 current=$1069.35 return=-0.684%
- EQIX entry: fill=$1076.542 current=$1069.35 return=-0.668%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-28

*From trigger_performance run `trigger_performance-20260528T224150-ffa82f3b`*
*Period: 2026-05-22 to 2026-05-28 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 68% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 54/79 symbols blocked (68%). Avg spread (blocked): 10.373%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.180%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 66 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-28T22:47:10Z

*From outcome_tracker run `outcome_tracker-20260528T224710-ef0bf2b8`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$210.29 return=-3.893%
- JNJ entry: fill=$230.248 current=$231.0 return=+0.327%
- EQIX entry: fill=$1084.37 current=$1069.35 return=-1.385%
- EQIX entry: fill=$1079.5 current=$1069.35 return=-0.940%
- EQIX exit: fill=$1078.442 current=$1069.35 return=-0.843%
- EQIX entry: fill=$1078.41 current=$1069.35 return=-0.840%
- JNJ entry: fill=$230.116 current=$231.0 return=+0.384%
- WMT entry: fill=$132.276 current=$118.48 return=-10.430%
- WMT entry: fill=$132.474 current=$118.48 return=-10.564%
- EQIX entry: fill=$1076.89 current=$1069.35 return=-0.700%
- EQIX entry: fill=$1076.82 current=$1069.35 return=-0.694%
- JNJ entry: fill=$230.044 current=$231.0 return=+0.416%
- EQIX exit: fill=$1076.718 current=$1069.35 return=-0.684%
- EQIX entry: fill=$1076.542 current=$1069.35 return=-0.668%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-28

*From trigger_performance run `trigger_performance-20260528T225220-b360ed99`*
*Period: 2026-05-22 to 2026-05-28 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 68% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 54/79 symbols blocked (68%). Avg spread (blocked): 10.373%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.180%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 66 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-29T22:18:30Z

*From outcome_tracker run `outcome_tracker-20260529T221830-3513851f`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$205.5 return=-6.082%
- JNJ entry: fill=$230.248 current=$225.4842 return=-2.069%
- EQIX entry: fill=$1084.37 current=$1066.54 return=-1.644%
- EQIX entry: fill=$1079.5 current=$1066.54 return=-1.201%
- EQIX exit: fill=$1078.442 current=$1066.54 return=-1.104%
- EQIX entry: fill=$1078.41 current=$1066.54 return=-1.101%
- JNJ entry: fill=$230.116 current=$225.4842 return=-2.013%
- WMT entry: fill=$132.276 current=$115.84 return=-12.425%
- WMT entry: fill=$132.474 current=$115.84 return=-12.556%
- EQIX entry: fill=$1076.89 current=$1066.54 return=-0.961%
- EQIX entry: fill=$1076.82 current=$1066.54 return=-0.955%
- JNJ entry: fill=$230.044 current=$225.4842 return=-1.982%
- EQIX exit: fill=$1076.718 current=$1066.54 return=-0.945%
- EQIX entry: fill=$1076.542 current=$1066.54 return=-0.929%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-29

*From trigger_performance run `trigger_performance-20260529T221830-3513851f`*
*Period: 2026-05-23 to 2026-05-29 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 61% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 48/79 symbols blocked (61%). Avg spread (blocked): 9.976%
- Trend gate (200 DMA): 35/79 symbols below 200 DMA (44% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -3.283%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 48 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=8, LIQUIDITY_GATE_V1=8, MOMENTUM_BLEND_6M_12M_V1=8, SPREAD_GATE_V1=8, STOCK_TREND_200DMA_V1=8.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-29T22:37:47Z

*From outcome_tracker run `outcome_tracker-20260529T223747-e7a526ed`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$205.5 return=-6.082%
- JNJ entry: fill=$230.248 current=$225.4842 return=-2.069%
- EQIX entry: fill=$1084.37 current=$1066.54 return=-1.644%
- EQIX entry: fill=$1079.5 current=$1066.54 return=-1.201%
- EQIX exit: fill=$1078.442 current=$1066.54 return=-1.104%
- EQIX entry: fill=$1078.41 current=$1066.54 return=-1.101%
- JNJ entry: fill=$230.116 current=$225.4842 return=-2.013%
- WMT entry: fill=$132.276 current=$115.84 return=-12.425%
- WMT entry: fill=$132.474 current=$115.84 return=-12.556%
- EQIX entry: fill=$1076.89 current=$1066.54 return=-0.961%
- EQIX entry: fill=$1076.82 current=$1066.54 return=-0.955%
- JNJ entry: fill=$230.044 current=$225.4842 return=-1.982%
- EQIX exit: fill=$1076.718 current=$1066.54 return=-0.945%
- EQIX entry: fill=$1076.542 current=$1066.54 return=-0.929%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-05-29

*From trigger_performance run `trigger_performance-20260529T223747-e7a526ed`*
*Period: 2026-05-23 to 2026-05-29 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 61% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 48/79 symbols blocked (61%). Avg spread (blocked): 9.976%
- Trend gate (200 DMA): 35/79 symbols below 200 DMA (44% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -3.283%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 48 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=8, LIQUIDITY_GATE_V1=8, MOMENTUM_BLEND_6M_12M_V1=8, SPREAD_GATE_V1=8, STOCK_TREND_200DMA_V1=8.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-05-29T22:43:42Z

*From outcome_tracker run `outcome_tracker-20260529T224342-6d02f89c`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$205.5 return=-6.082%
- JNJ entry: fill=$230.248 current=$225.4842 return=-2.069%
- EQIX entry: fill=$1084.37 current=$1066.54 return=-1.644%
- EQIX entry: fill=$1079.5 current=$1066.54 return=-1.201%
- EQIX exit: fill=$1078.442 current=$1066.54 return=-1.104%
- EQIX entry: fill=$1078.41 current=$1066.54 return=-1.101%
- JNJ entry: fill=$230.116 current=$225.4842 return=-2.013%
- WMT entry: fill=$132.276 current=$115.84 return=-12.425%
- WMT entry: fill=$132.474 current=$115.84 return=-12.556%
- EQIX entry: fill=$1076.89 current=$1066.54 return=-0.961%
- EQIX entry: fill=$1076.82 current=$1066.54 return=-0.955%
- JNJ entry: fill=$230.044 current=$225.4842 return=-1.982%
- EQIX exit: fill=$1076.718 current=$1066.54 return=-0.945%
- EQIX entry: fill=$1076.542 current=$1066.54 return=-0.929%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Experiment Candidates — 2026-05-29

*From weekly review run weekly_review-2026-05-29*

**Observations (hypothesis candidates):**
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.
- 2 external alert(s) ingested this period, 0 routed.

**To propose a strategy experiment, open a PR with:**
- Hypothesis
- Supporting evidence (backtest or paper results)
- Success criteria
- Rollback plan

---
## Outcome Observations — 2026-06-01T22:50:35Z

*From outcome_tracker run `outcome_tracker-20260601T225035-313337d3`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$197.36 return=-9.802%
- JNJ entry: fill=$230.248 current=$223.77 return=-2.813%
- EQIX entry: fill=$1084.37 current=$1051.0 return=-3.077%
- EQIX entry: fill=$1079.5 current=$1051.0 return=-2.640%
- EQIX exit: fill=$1078.442 current=$1051.0 return=-2.545%
- EQIX entry: fill=$1078.41 current=$1051.0 return=-2.542%
- JNJ entry: fill=$230.116 current=$223.77 return=-2.758%
- WMT entry: fill=$132.276 current=$114.3831 return=-13.527%
- WMT entry: fill=$132.474 current=$114.3831 return=-13.656%
- EQIX entry: fill=$1076.89 current=$1051.0 return=-2.404%
- EQIX entry: fill=$1076.82 current=$1051.0 return=-2.398%
- JNJ entry: fill=$230.044 current=$223.77 return=-2.727%
- EQIX exit: fill=$1076.718 current=$1051.0 return=-2.389%
- EQIX entry: fill=$1076.542 current=$1051.0 return=-2.373%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-01

*From trigger_performance run `trigger_performance-20260601T225035-313337d3`*
*Period: 2026-05-26 to 2026-06-01 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 72% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 0 risk-on (0%).
- Spread gate: 57/79 symbols blocked (72%). Avg spread (blocked): 10.386%
- Trend gate (200 DMA): 37/79 symbols below 200 DMA (47% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -4.689%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-01T23:02:58Z

*From outcome_tracker run `outcome_tracker-20260601T230258-7fc6c62f`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$197.36 return=-9.802%
- JNJ entry: fill=$230.248 current=$223.77 return=-2.813%
- EQIX entry: fill=$1084.37 current=$1051.0 return=-3.077%
- EQIX entry: fill=$1079.5 current=$1051.0 return=-2.640%
- EQIX exit: fill=$1078.442 current=$1051.0 return=-2.545%
- EQIX entry: fill=$1078.41 current=$1051.0 return=-2.542%
- JNJ entry: fill=$230.116 current=$223.77 return=-2.758%
- WMT entry: fill=$132.276 current=$114.3831 return=-13.527%
- WMT entry: fill=$132.474 current=$114.3831 return=-13.656%
- EQIX entry: fill=$1076.89 current=$1051.0 return=-2.404%
- EQIX entry: fill=$1076.82 current=$1051.0 return=-2.398%
- JNJ entry: fill=$230.044 current=$223.77 return=-2.727%
- EQIX exit: fill=$1076.718 current=$1051.0 return=-2.389%
- EQIX entry: fill=$1076.542 current=$1051.0 return=-2.373%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-01

*From trigger_performance run `trigger_performance-20260601T230258-7fc6c62f`*
*Period: 2026-05-26 to 2026-06-01 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 72% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 57/79 symbols blocked (72%). Avg spread (blocked): 10.386%
- Trend gate (200 DMA): 37/79 symbols below 200 DMA (47% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -4.689%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-01T23:12:01Z

*From outcome_tracker run `outcome_tracker-20260601T231201-53cdf593`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$197.36 return=-9.802%
- JNJ entry: fill=$230.248 current=$223.77 return=-2.813%
- EQIX entry: fill=$1084.37 current=$1051.0 return=-3.077%
- EQIX entry: fill=$1079.5 current=$1051.0 return=-2.640%
- EQIX exit: fill=$1078.442 current=$1051.0 return=-2.545%
- EQIX entry: fill=$1078.41 current=$1051.0 return=-2.542%
- JNJ entry: fill=$230.116 current=$223.77 return=-2.758%
- WMT entry: fill=$132.276 current=$114.3831 return=-13.527%
- WMT entry: fill=$132.474 current=$114.3831 return=-13.656%
- EQIX entry: fill=$1076.89 current=$1051.0 return=-2.404%
- EQIX entry: fill=$1076.82 current=$1051.0 return=-2.398%
- JNJ entry: fill=$230.044 current=$223.77 return=-2.727%
- EQIX exit: fill=$1076.718 current=$1051.0 return=-2.389%
- EQIX entry: fill=$1076.542 current=$1051.0 return=-2.373%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-01

*From trigger_performance run `trigger_performance-20260601T231337-5bd6ead0`*
*Period: 2026-05-26 to 2026-06-01 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 72% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 57/79 symbols blocked (72%). Avg spread (blocked): 10.386%
- Trend gate (200 DMA): 37/79 symbols below 200 DMA (47% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -4.689%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-02T22:51:05Z

*From outcome_tracker run `outcome_tracker-20260602T225105-d47eed29`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$195.35 return=-10.721%
- JNJ entry: fill=$230.248 current=$222.5046 return=-3.363%
- EQIX entry: fill=$1084.37 current=$1071.8 return=-1.159%
- EQIX entry: fill=$1079.5 current=$1071.8 return=-0.713%
- EQIX exit: fill=$1078.442 current=$1071.8 return=-0.616%
- EQIX entry: fill=$1078.41 current=$1071.8 return=-0.613%
- JNJ entry: fill=$230.116 current=$222.5046 return=-3.308%
- WMT entry: fill=$132.276 current=$112.96 return=-14.603%
- WMT entry: fill=$132.474 current=$112.96 return=-14.730%
- EQIX entry: fill=$1076.89 current=$1071.8 return=-0.473%
- EQIX entry: fill=$1076.82 current=$1071.8 return=-0.466%
- JNJ entry: fill=$230.044 current=$222.5046 return=-3.277%
- EQIX exit: fill=$1076.718 current=$1071.8 return=-0.457%
- EQIX entry: fill=$1076.542 current=$1071.8 return=-0.441%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-02

*From trigger_performance run `trigger_performance-20260602T225105-d47eed29`*
*Period: 2026-05-27 to 2026-06-02 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 0 risk-on (0%).
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.397%
- Trend gate (200 DMA): 38/79 symbols below 200 DMA (48% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -3.924%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-02T23:03:19Z

*From outcome_tracker run `outcome_tracker-20260602T230319-8461e136`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$195.35 return=-10.721%
- JNJ entry: fill=$230.248 current=$222.5046 return=-3.363%
- EQIX entry: fill=$1084.37 current=$1071.8 return=-1.159%
- EQIX entry: fill=$1079.5 current=$1071.8 return=-0.713%
- EQIX exit: fill=$1078.442 current=$1071.8 return=-0.616%
- EQIX entry: fill=$1078.41 current=$1071.8 return=-0.613%
- JNJ entry: fill=$230.116 current=$222.5046 return=-3.308%
- WMT entry: fill=$132.276 current=$112.96 return=-14.603%
- WMT entry: fill=$132.474 current=$112.96 return=-14.730%
- EQIX entry: fill=$1076.89 current=$1071.8 return=-0.473%
- EQIX entry: fill=$1076.82 current=$1071.8 return=-0.466%
- JNJ entry: fill=$230.044 current=$222.5046 return=-3.277%
- EQIX exit: fill=$1076.718 current=$1071.8 return=-0.457%
- EQIX entry: fill=$1076.542 current=$1071.8 return=-0.441%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-02

*From trigger_performance run `trigger_performance-20260602T230319-8461e136`*
*Period: 2026-05-27 to 2026-06-02 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.397%
- Trend gate (200 DMA): 38/79 symbols below 200 DMA (48% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -3.924%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-02T23:10:47Z

*From outcome_tracker run `outcome_tracker-20260602T231047-b7f335ff`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$195.35 return=-10.721%
- JNJ entry: fill=$230.248 current=$222.5046 return=-3.363%
- EQIX entry: fill=$1084.37 current=$1071.8 return=-1.159%
- EQIX entry: fill=$1079.5 current=$1071.8 return=-0.713%
- EQIX exit: fill=$1078.442 current=$1071.8 return=-0.616%
- EQIX entry: fill=$1078.41 current=$1071.8 return=-0.613%
- JNJ entry: fill=$230.116 current=$222.5046 return=-3.308%
- WMT entry: fill=$132.276 current=$112.96 return=-14.603%
- WMT entry: fill=$132.474 current=$112.96 return=-14.730%
- EQIX entry: fill=$1076.89 current=$1071.8 return=-0.473%
- EQIX entry: fill=$1076.82 current=$1071.8 return=-0.466%
- JNJ entry: fill=$230.044 current=$222.5046 return=-3.277%
- EQIX exit: fill=$1076.718 current=$1071.8 return=-0.457%
- EQIX entry: fill=$1076.542 current=$1071.8 return=-0.441%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-02

*From trigger_performance run `trigger_performance-20260602T231506-23a0e034`*
*Period: 2026-05-27 to 2026-06-02 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.397%
- Trend gate (200 DMA): 38/79 symbols below 200 DMA (48% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -3.924%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-03T22:53:09Z

*From outcome_tracker run `outcome_tracker-20260603T225309-17b4f6e1`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$199.59 return=-8.783%
- JNJ entry: fill=$230.248 current=$223.24 return=-3.044%
- EQIX entry: fill=$1084.37 current=$1077.0 return=-0.680%
- EQIX entry: fill=$1079.5 current=$1077.0 return=-0.232%
- EQIX exit: fill=$1078.442 current=$1077.0 return=-0.134%
- EQIX entry: fill=$1078.41 current=$1077.0 return=-0.131%
- JNJ entry: fill=$230.116 current=$223.24 return=-2.988%
- WMT entry: fill=$132.276 current=$118.08 return=-10.732%
- WMT entry: fill=$132.474 current=$118.08 return=-10.866%
- EQIX entry: fill=$1076.89 current=$1077.0 return=+0.010%
- EQIX entry: fill=$1076.82 current=$1077.0 return=+0.017%
- JNJ entry: fill=$230.044 current=$223.24 return=-2.958%
- EQIX exit: fill=$1076.718 current=$1077.0 return=+0.026%
- EQIX entry: fill=$1076.542 current=$1077.0 return=+0.042%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-03

*From trigger_performance run `trigger_performance-20260603T225309-17b4f6e1`*
*Period: 2026-05-28 to 2026-06-03 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 0 risk-on (0%).
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 10.255%
- Trend gate (200 DMA): 37/79 symbols below 200 DMA (47% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.889%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-03T23:05:42Z

*From outcome_tracker run `outcome_tracker-20260603T230542-3561aec1`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$199.59 return=-8.783%
- JNJ entry: fill=$230.248 current=$223.24 return=-3.044%
- EQIX entry: fill=$1084.37 current=$1077.0 return=-0.680%
- EQIX entry: fill=$1079.5 current=$1077.0 return=-0.232%
- EQIX exit: fill=$1078.442 current=$1077.0 return=-0.134%
- EQIX entry: fill=$1078.41 current=$1077.0 return=-0.131%
- JNJ entry: fill=$230.116 current=$223.24 return=-2.988%
- WMT entry: fill=$132.276 current=$118.08 return=-10.732%
- WMT entry: fill=$132.474 current=$118.08 return=-10.866%
- EQIX entry: fill=$1076.89 current=$1077.0 return=+0.010%
- EQIX entry: fill=$1076.82 current=$1077.0 return=+0.017%
- JNJ entry: fill=$230.044 current=$223.24 return=-2.958%
- EQIX exit: fill=$1076.718 current=$1077.0 return=+0.026%
- EQIX entry: fill=$1076.542 current=$1077.0 return=+0.042%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-03

*From trigger_performance run `trigger_performance-20260603T230542-3561aec1`*
*Period: 2026-05-28 to 2026-06-03 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 10.255%
- Trend gate (200 DMA): 37/79 symbols below 200 DMA (47% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.889%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-03T23:14:48Z

*From outcome_tracker run `outcome_tracker-20260603T231448-58272fb8`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$199.59 return=-8.783%
- JNJ entry: fill=$230.248 current=$223.24 return=-3.044%
- EQIX entry: fill=$1084.37 current=$1077.0 return=-0.680%
- EQIX entry: fill=$1079.5 current=$1077.0 return=-0.232%
- EQIX exit: fill=$1078.442 current=$1077.0 return=-0.134%
- EQIX entry: fill=$1078.41 current=$1077.0 return=-0.131%
- JNJ entry: fill=$230.116 current=$223.24 return=-2.988%
- WMT entry: fill=$132.276 current=$118.08 return=-10.732%
- WMT entry: fill=$132.474 current=$118.08 return=-10.866%
- EQIX entry: fill=$1076.89 current=$1077.0 return=+0.010%
- EQIX entry: fill=$1076.82 current=$1077.0 return=+0.017%
- JNJ entry: fill=$230.044 current=$223.24 return=-2.958%
- EQIX exit: fill=$1076.718 current=$1077.0 return=+0.026%
- EQIX entry: fill=$1076.542 current=$1077.0 return=+0.042%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-03

*From trigger_performance run `trigger_performance-20260603T231742-f1bc813c`*
*Period: 2026-05-28 to 2026-06-03 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 10.255%
- Trend gate (200 DMA): 37/79 symbols below 200 DMA (47% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.889%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-04T22:11:32Z

*From outcome_tracker run `outcome_tracker-20260604T221132-223776bb`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$200.85 return=-8.207%
- JNJ entry: fill=$230.248 current=$228.76 return=-0.646%
- EQIX entry: fill=$1084.37 current=$1089.13 return=+0.439%
- EQIX entry: fill=$1079.5 current=$1089.13 return=+0.892%
- EQIX exit: fill=$1078.442 current=$1089.13 return=+0.991%
- EQIX entry: fill=$1078.41 current=$1089.13 return=+0.994%
- JNJ entry: fill=$230.116 current=$228.76 return=-0.589%
- WMT entry: fill=$132.276 current=$118.06 return=-10.747%
- WMT entry: fill=$132.474 current=$118.06 return=-10.881%
- EQIX entry: fill=$1076.89 current=$1089.13 return=+1.137%
- EQIX entry: fill=$1076.82 current=$1089.13 return=+1.143%
- JNJ entry: fill=$230.044 current=$228.76 return=-0.558%
- EQIX exit: fill=$1076.718 current=$1089.13 return=+1.153%
- EQIX entry: fill=$1076.542 current=$1089.13 return=+1.169%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-04

*From trigger_performance run `trigger_performance-20260604T221132-223776bb`*
*Period: 2026-05-29 to 2026-06-04 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 63% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 50/79 symbols blocked (63%). Avg spread (blocked): 10.305%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.694%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-04T22:21:45Z

*From outcome_tracker run `outcome_tracker-20260604T222145-efb16027`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$200.85 return=-8.207%
- JNJ entry: fill=$230.248 current=$228.76 return=-0.646%
- EQIX entry: fill=$1084.37 current=$1089.13 return=+0.439%
- EQIX entry: fill=$1079.5 current=$1089.13 return=+0.892%
- EQIX exit: fill=$1078.442 current=$1089.13 return=+0.991%
- EQIX entry: fill=$1078.41 current=$1089.13 return=+0.994%
- JNJ entry: fill=$230.116 current=$228.76 return=-0.589%
- WMT entry: fill=$132.276 current=$118.06 return=-10.747%
- WMT entry: fill=$132.474 current=$118.06 return=-10.881%
- EQIX entry: fill=$1076.89 current=$1089.13 return=+1.137%
- EQIX entry: fill=$1076.82 current=$1089.13 return=+1.143%
- JNJ entry: fill=$230.044 current=$228.76 return=-0.558%
- EQIX exit: fill=$1076.718 current=$1089.13 return=+1.153%
- EQIX entry: fill=$1076.542 current=$1089.13 return=+1.169%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-04

*From trigger_performance run `trigger_performance-20260604T222145-efb16027`*
*Period: 2026-05-29 to 2026-06-04 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 63% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 50/79 symbols blocked (63%). Avg spread (blocked): 10.305%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.694%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-04T22:47:55Z

*From outcome_tracker run `outcome_tracker-20260604T224755-c31ab5b9`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$200.85 return=-8.207%
- JNJ entry: fill=$230.248 current=$228.76 return=-0.646%
- EQIX entry: fill=$1084.37 current=$1089.13 return=+0.439%
- EQIX entry: fill=$1079.5 current=$1089.13 return=+0.892%
- EQIX exit: fill=$1078.442 current=$1089.13 return=+0.991%
- EQIX entry: fill=$1078.41 current=$1089.13 return=+0.994%
- JNJ entry: fill=$230.116 current=$228.76 return=-0.589%
- WMT entry: fill=$132.276 current=$118.06 return=-10.747%
- WMT entry: fill=$132.474 current=$118.06 return=-10.881%
- EQIX entry: fill=$1076.89 current=$1089.13 return=+1.137%
- EQIX entry: fill=$1076.82 current=$1089.13 return=+1.143%
- JNJ entry: fill=$230.044 current=$228.76 return=-0.558%
- EQIX exit: fill=$1076.718 current=$1089.13 return=+1.153%
- EQIX entry: fill=$1076.542 current=$1089.13 return=+1.169%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-04

*From trigger_performance run `trigger_performance-20260604T225306-addf4dd1`*
*Period: 2026-05-29 to 2026-06-04 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 63% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 50/79 symbols blocked (63%). Avg spread (blocked): 10.305%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.694%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-05T22:05:51Z

*From outcome_tracker run `outcome_tracker-20260605T220551-f4dcade2`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$206.93 return=-5.428%
- JNJ entry: fill=$230.248 current=$231.9979 return=+0.760%
- EQIX entry: fill=$1084.37 current=$1080.0 return=-0.403%
- EQIX entry: fill=$1079.5 current=$1080.0 return=+0.046%
- EQIX exit: fill=$1078.442 current=$1080.0 return=+0.145%
- EQIX entry: fill=$1078.41 current=$1080.0 return=+0.147%
- JNJ entry: fill=$230.116 current=$231.9979 return=+0.818%
- WMT entry: fill=$132.276 current=$118.19 return=-10.649%
- WMT entry: fill=$132.474 current=$118.19 return=-10.783%
- EQIX entry: fill=$1076.89 current=$1080.0 return=+0.289%
- EQIX entry: fill=$1076.82 current=$1080.0 return=+0.295%
- JNJ entry: fill=$230.044 current=$231.9979 return=+0.849%
- EQIX exit: fill=$1076.718 current=$1080.0 return=+0.305%
- EQIX entry: fill=$1076.542 current=$1080.0 return=+0.321%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-05

*From trigger_performance run `trigger_performance-20260605T220551-f4dcade2`*
*Period: 2026-05-30 to 2026-06-05 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 58% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 46/79 symbols blocked (58%). Avg spread (blocked): 10.069%
- Trend gate (200 DMA): 31/79 symbols below 200 DMA (39% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.663%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 66 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-05T22:15:09Z

*From outcome_tracker run `outcome_tracker-20260605T221509-910bc80c`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$206.93 return=-5.428%
- JNJ entry: fill=$230.248 current=$231.9979 return=+0.760%
- EQIX entry: fill=$1084.37 current=$1080.0 return=-0.403%
- EQIX entry: fill=$1079.5 current=$1080.0 return=+0.046%
- EQIX exit: fill=$1078.442 current=$1080.0 return=+0.145%
- EQIX entry: fill=$1078.41 current=$1080.0 return=+0.147%
- JNJ entry: fill=$230.116 current=$231.9979 return=+0.818%
- WMT entry: fill=$132.276 current=$118.19 return=-10.649%
- WMT entry: fill=$132.474 current=$118.19 return=-10.783%
- EQIX entry: fill=$1076.89 current=$1080.0 return=+0.289%
- EQIX entry: fill=$1076.82 current=$1080.0 return=+0.295%
- JNJ entry: fill=$230.044 current=$231.9979 return=+0.849%
- EQIX exit: fill=$1076.718 current=$1080.0 return=+0.305%
- EQIX entry: fill=$1076.542 current=$1080.0 return=+0.321%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-05

*From trigger_performance run `trigger_performance-20260605T221509-910bc80c`*
*Period: 2026-05-30 to 2026-06-05 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 58% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 46/79 symbols blocked (58%). Avg spread (blocked): 10.069%
- Trend gate (200 DMA): 31/79 symbols below 200 DMA (39% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.663%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 66 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-05T22:36:46Z

*From outcome_tracker run `outcome_tracker-20260605T223646-903ce6ed`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$206.93 return=-5.428%
- JNJ entry: fill=$230.248 current=$231.9979 return=+0.760%
- EQIX entry: fill=$1084.37 current=$1080.0 return=-0.403%
- EQIX entry: fill=$1079.5 current=$1080.0 return=+0.046%
- EQIX exit: fill=$1078.442 current=$1080.0 return=+0.145%
- EQIX entry: fill=$1078.41 current=$1080.0 return=+0.147%
- JNJ entry: fill=$230.116 current=$231.9979 return=+0.818%
- WMT entry: fill=$132.276 current=$118.19 return=-10.649%
- WMT entry: fill=$132.474 current=$118.19 return=-10.783%
- EQIX entry: fill=$1076.89 current=$1080.0 return=+0.289%
- EQIX entry: fill=$1076.82 current=$1080.0 return=+0.295%
- JNJ entry: fill=$230.044 current=$231.9979 return=+0.849%
- EQIX exit: fill=$1076.718 current=$1080.0 return=+0.305%
- EQIX entry: fill=$1076.542 current=$1080.0 return=+0.321%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Experiment Candidates — 2026-06-05

*From weekly review run weekly_review-2026-06-05*

**Observations (hypothesis candidates):**
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

**To propose a strategy experiment, open a PR with:**
- Hypothesis
- Supporting evidence (backtest or paper results)
- Success criteria
- Rollback plan

---
## Outcome Observations — 2026-06-08T22:15:13Z

*From outcome_tracker run `outcome_tracker-20260608T221513-a01e8640`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$200.0 return=-8.596%
- JNJ entry: fill=$230.248 current=$231.9011 return=+0.718%
- EQIX entry: fill=$1084.37 current=$1062.74 return=-1.995%
- EQIX entry: fill=$1079.5 current=$1062.74 return=-1.553%
- EQIX exit: fill=$1078.442 current=$1062.74 return=-1.456%
- EQIX entry: fill=$1078.41 current=$1062.74 return=-1.453%
- JNJ entry: fill=$230.116 current=$231.9011 return=+0.776%
- WMT entry: fill=$132.276 current=$119.51 return=-9.651%
- WMT entry: fill=$132.474 current=$119.51 return=-9.786%
- EQIX entry: fill=$1076.89 current=$1062.74 return=-1.314%
- EQIX entry: fill=$1076.82 current=$1062.74 return=-1.308%
- JNJ entry: fill=$230.044 current=$231.9011 return=+0.807%
- EQIX exit: fill=$1076.718 current=$1062.74 return=-1.298%
- EQIX entry: fill=$1076.542 current=$1062.74 return=-1.282%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-08

*From trigger_performance run `trigger_performance-20260608T221513-a01e8640`*
*Period: 2026-06-02 to 2026-06-08 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 75% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 0 risk-on (0%).
- Spread gate: 59/79 symbols blocked (75%). Avg spread (blocked): 10.744%
- Trend gate (200 DMA): 36/79 symbols below 200 DMA (46% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.671%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-08T22:40:27Z

*From outcome_tracker run `outcome_tracker-20260608T224027-ec3f1743`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$200.0 return=-8.596%
- JNJ entry: fill=$230.248 current=$231.9011 return=+0.718%
- EQIX entry: fill=$1084.37 current=$1062.74 return=-1.995%
- EQIX entry: fill=$1079.5 current=$1062.74 return=-1.553%
- EQIX exit: fill=$1078.442 current=$1062.74 return=-1.456%
- EQIX entry: fill=$1078.41 current=$1062.74 return=-1.453%
- JNJ entry: fill=$230.116 current=$231.9011 return=+0.776%
- WMT entry: fill=$132.276 current=$119.51 return=-9.651%
- WMT entry: fill=$132.474 current=$119.51 return=-9.786%
- EQIX entry: fill=$1076.89 current=$1062.74 return=-1.314%
- EQIX entry: fill=$1076.82 current=$1062.74 return=-1.308%
- JNJ entry: fill=$230.044 current=$231.9011 return=+0.807%
- EQIX exit: fill=$1076.718 current=$1062.74 return=-1.298%
- EQIX entry: fill=$1076.542 current=$1062.74 return=-1.282%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-08

*From trigger_performance run `trigger_performance-20260608T224027-ec3f1743`*
*Period: 2026-06-02 to 2026-06-08 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 75% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 59/79 symbols blocked (75%). Avg spread (blocked): 10.744%
- Trend gate (200 DMA): 36/79 symbols below 200 DMA (46% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.671%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-08T22:51:27Z

*From outcome_tracker run `outcome_tracker-20260608T225127-720cad87`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$200.0 return=-8.596%
- JNJ entry: fill=$230.248 current=$231.9011 return=+0.718%
- EQIX entry: fill=$1084.37 current=$1062.74 return=-1.995%
- EQIX entry: fill=$1079.5 current=$1062.74 return=-1.553%
- EQIX exit: fill=$1078.442 current=$1062.74 return=-1.456%
- EQIX entry: fill=$1078.41 current=$1062.74 return=-1.453%
- JNJ entry: fill=$230.116 current=$231.9011 return=+0.776%
- WMT entry: fill=$132.276 current=$119.51 return=-9.651%
- WMT entry: fill=$132.474 current=$119.51 return=-9.786%
- EQIX entry: fill=$1076.89 current=$1062.74 return=-1.314%
- EQIX entry: fill=$1076.82 current=$1062.74 return=-1.308%
- JNJ entry: fill=$230.044 current=$231.9011 return=+0.807%
- EQIX exit: fill=$1076.718 current=$1062.74 return=-1.298%
- EQIX entry: fill=$1076.542 current=$1062.74 return=-1.282%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-08

*From trigger_performance run `trigger_performance-20260608T225548-59e7f547`*
*Period: 2026-06-02 to 2026-06-08 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 75% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 59/79 symbols blocked (75%). Avg spread (blocked): 10.744%
- Trend gate (200 DMA): 36/79 symbols below 200 DMA (46% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.671%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-09T22:14:09Z

*From outcome_tracker run `outcome_tracker-20260609T221409-9a6b4472`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$206.77 return=-5.502%
- JNJ entry: fill=$230.248 current=$237.2221 return=+3.029%
- EQIX entry: fill=$1084.37 current=$1059.84 return=-2.262%
- EQIX entry: fill=$1079.5 current=$1059.84 return=-1.821%
- EQIX exit: fill=$1078.442 current=$1059.84 return=-1.725%
- EQIX entry: fill=$1078.41 current=$1059.84 return=-1.722%
- JNJ entry: fill=$230.116 current=$237.2221 return=+3.088%
- WMT entry: fill=$132.276 current=$118.9147 return=-10.101%
- WMT entry: fill=$132.474 current=$118.9147 return=-10.235%
- EQIX entry: fill=$1076.89 current=$1059.84 return=-1.583%
- EQIX entry: fill=$1076.82 current=$1059.84 return=-1.577%
- JNJ entry: fill=$230.044 current=$237.2221 return=+3.120%
- EQIX exit: fill=$1076.718 current=$1059.84 return=-1.568%
- EQIX entry: fill=$1076.542 current=$1059.84 return=-1.551%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-09

*From trigger_performance run `trigger_performance-20260609T221409-9a6b4472`*
*Period: 2026-06-03 to 2026-06-09 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 10.188%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.172%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-09T22:24:32Z

*From outcome_tracker run `outcome_tracker-20260609T222432-622c71c0`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$206.77 return=-5.502%
- JNJ entry: fill=$230.248 current=$237.2221 return=+3.029%
- EQIX entry: fill=$1084.37 current=$1059.84 return=-2.262%
- EQIX entry: fill=$1079.5 current=$1059.84 return=-1.821%
- EQIX exit: fill=$1078.442 current=$1059.84 return=-1.725%
- EQIX entry: fill=$1078.41 current=$1059.84 return=-1.722%
- JNJ entry: fill=$230.116 current=$237.2221 return=+3.088%
- WMT entry: fill=$132.276 current=$118.9147 return=-10.101%
- WMT entry: fill=$132.474 current=$118.9147 return=-10.235%
- EQIX entry: fill=$1076.89 current=$1059.84 return=-1.583%
- EQIX entry: fill=$1076.82 current=$1059.84 return=-1.577%
- JNJ entry: fill=$230.044 current=$237.2221 return=+3.120%
- EQIX exit: fill=$1076.718 current=$1059.84 return=-1.568%
- EQIX entry: fill=$1076.542 current=$1059.84 return=-1.551%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-09

*From trigger_performance run `trigger_performance-20260609T222432-622c71c0`*
*Period: 2026-06-03 to 2026-06-09 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 10.188%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.172%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-09T22:52:07Z

*From outcome_tracker run `outcome_tracker-20260609T225207-3d4ba06b`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$206.77 return=-5.502%
- JNJ entry: fill=$230.248 current=$237.2221 return=+3.029%
- EQIX entry: fill=$1084.37 current=$1059.84 return=-2.262%
- EQIX entry: fill=$1079.5 current=$1059.84 return=-1.821%
- EQIX exit: fill=$1078.442 current=$1059.84 return=-1.725%
- EQIX entry: fill=$1078.41 current=$1059.84 return=-1.722%
- JNJ entry: fill=$230.116 current=$237.2221 return=+3.088%
- WMT entry: fill=$132.276 current=$118.9147 return=-10.101%
- WMT entry: fill=$132.474 current=$118.9147 return=-10.235%
- EQIX entry: fill=$1076.89 current=$1059.84 return=-1.583%
- EQIX entry: fill=$1076.82 current=$1059.84 return=-1.577%
- JNJ entry: fill=$230.044 current=$237.2221 return=+3.120%
- EQIX exit: fill=$1076.718 current=$1059.84 return=-1.568%
- EQIX entry: fill=$1076.542 current=$1059.84 return=-1.551%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-09

*From trigger_performance run `trigger_performance-20260609T225721-4a6e98b5`*
*Period: 2026-06-03 to 2026-06-09 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 10.188%
- Trend gate (200 DMA): 34/79 symbols below 200 DMA (43% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.172%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-10T22:30:55Z

*From outcome_tracker run `outcome_tracker-20260610T223055-d6d44e53`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$211.36 return=-3.404%
- JNJ entry: fill=$230.248 current=$238.49 return=+3.580%
- EQIX entry: fill=$1084.37 current=$1038.33 return=-4.246%
- EQIX entry: fill=$1079.5 current=$1038.33 return=-3.814%
- EQIX exit: fill=$1078.442 current=$1038.33 return=-3.719%
- EQIX entry: fill=$1078.41 current=$1038.33 return=-3.717%
- JNJ entry: fill=$230.116 current=$238.49 return=+3.639%
- WMT entry: fill=$132.276 current=$120.2224 return=-9.112%
- WMT entry: fill=$132.474 current=$120.2224 return=-9.248%
- EQIX entry: fill=$1076.89 current=$1038.33 return=-3.581%
- EQIX entry: fill=$1076.82 current=$1038.33 return=-3.574%
- JNJ entry: fill=$230.044 current=$238.49 return=+3.671%
- EQIX exit: fill=$1076.718 current=$1038.33 return=-3.565%
- EQIX entry: fill=$1076.542 current=$1038.33 return=-3.550%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-10

*From trigger_performance run `trigger_performance-20260610T223055-d6d44e53`*
*Period: 2026-06-04 to 2026-06-10 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 68% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 54/79 symbols blocked (68%). Avg spread (blocked): 10.829%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.903%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-10T22:51:25Z

*From outcome_tracker run `outcome_tracker-20260610T225125-32670b57`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$211.36 return=-3.404%
- JNJ entry: fill=$230.248 current=$238.49 return=+3.580%
- EQIX entry: fill=$1084.37 current=$1038.33 return=-4.246%
- EQIX entry: fill=$1079.5 current=$1038.33 return=-3.814%
- EQIX exit: fill=$1078.442 current=$1038.33 return=-3.719%
- EQIX entry: fill=$1078.41 current=$1038.33 return=-3.717%
- JNJ entry: fill=$230.116 current=$238.49 return=+3.639%
- WMT entry: fill=$132.276 current=$120.2224 return=-9.112%
- WMT entry: fill=$132.474 current=$120.2224 return=-9.248%
- EQIX entry: fill=$1076.89 current=$1038.33 return=-3.581%
- EQIX entry: fill=$1076.82 current=$1038.33 return=-3.574%
- JNJ entry: fill=$230.044 current=$238.49 return=+3.671%
- EQIX exit: fill=$1076.718 current=$1038.33 return=-3.565%
- EQIX entry: fill=$1076.542 current=$1038.33 return=-3.550%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-10

*From trigger_performance run `trigger_performance-20260610T225125-32670b57`*
*Period: 2026-06-04 to 2026-06-10 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 68% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 54/79 symbols blocked (68%). Avg spread (blocked): 10.829%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.903%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-10T22:58:27Z

*From outcome_tracker run `outcome_tracker-20260610T225827-46706b9f`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$211.36 return=-3.404%
- JNJ entry: fill=$230.248 current=$238.49 return=+3.580%
- EQIX entry: fill=$1084.37 current=$1038.33 return=-4.246%
- EQIX entry: fill=$1079.5 current=$1038.33 return=-3.814%
- EQIX exit: fill=$1078.442 current=$1038.33 return=-3.719%
- EQIX entry: fill=$1078.41 current=$1038.33 return=-3.717%
- JNJ entry: fill=$230.116 current=$238.49 return=+3.639%
- WMT entry: fill=$132.276 current=$120.2224 return=-9.112%
- WMT entry: fill=$132.474 current=$120.2224 return=-9.248%
- EQIX entry: fill=$1076.89 current=$1038.33 return=-3.581%
- EQIX entry: fill=$1076.82 current=$1038.33 return=-3.574%
- JNJ entry: fill=$230.044 current=$238.49 return=+3.671%
- EQIX exit: fill=$1076.718 current=$1038.33 return=-3.565%
- EQIX entry: fill=$1076.542 current=$1038.33 return=-3.550%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-10

*From trigger_performance run `trigger_performance-20260610T230723-0003f387`*
*Period: 2026-06-04 to 2026-06-10 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 68% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 54/79 symbols blocked (68%). Avg spread (blocked): 10.829%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.903%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-11T22:28:15Z

*From outcome_tracker run `outcome_tracker-20260611T222815-5b9e865f`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$210.67 return=-3.719%
- JNJ entry: fill=$230.248 current=$237.68 return=+3.228%
- EQIX entry: fill=$1084.37 current=$1043.18 return=-3.798%
- EQIX entry: fill=$1079.5 current=$1043.18 return=-3.365%
- EQIX exit: fill=$1078.442 current=$1043.18 return=-3.270%
- EQIX entry: fill=$1078.41 current=$1043.18 return=-3.267%
- JNJ entry: fill=$230.116 current=$237.68 return=+3.287%
- WMT entry: fill=$132.276 current=$120.3 return=-9.054%
- WMT entry: fill=$132.474 current=$120.3 return=-9.190%
- EQIX entry: fill=$1076.89 current=$1043.18 return=-3.130%
- EQIX entry: fill=$1076.82 current=$1043.18 return=-3.124%
- JNJ entry: fill=$230.044 current=$237.68 return=+3.319%
- EQIX exit: fill=$1076.718 current=$1043.18 return=-3.115%
- EQIX entry: fill=$1076.542 current=$1043.18 return=-3.099%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-11

*From trigger_performance run `trigger_performance-20260611T222816-b93d2876`*
*Period: 2026-06-05 to 2026-06-11 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 57% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 45/79 symbols blocked (57%). Avg spread (blocked): 11.552%
- Trend gate (200 DMA): 29/79 symbols below 200 DMA (37% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.735%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 66 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-11T22:50:05Z

*From outcome_tracker run `outcome_tracker-20260611T225005-b1c9dfdd`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$210.67 return=-3.719%
- JNJ entry: fill=$230.248 current=$237.68 return=+3.228%
- EQIX entry: fill=$1084.37 current=$1043.18 return=-3.798%
- EQIX entry: fill=$1079.5 current=$1043.18 return=-3.365%
- EQIX exit: fill=$1078.442 current=$1043.18 return=-3.270%
- EQIX entry: fill=$1078.41 current=$1043.18 return=-3.267%
- JNJ entry: fill=$230.116 current=$237.68 return=+3.287%
- WMT entry: fill=$132.276 current=$120.3 return=-9.054%
- WMT entry: fill=$132.474 current=$120.3 return=-9.190%
- EQIX entry: fill=$1076.89 current=$1043.18 return=-3.130%
- EQIX entry: fill=$1076.82 current=$1043.18 return=-3.124%
- JNJ entry: fill=$230.044 current=$237.68 return=+3.319%
- EQIX exit: fill=$1076.718 current=$1043.18 return=-3.115%
- EQIX entry: fill=$1076.542 current=$1043.18 return=-3.099%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-11

*From trigger_performance run `trigger_performance-20260611T225005-b1c9dfdd`*
*Period: 2026-06-05 to 2026-06-11 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 57% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 45/79 symbols blocked (57%). Avg spread (blocked): 11.552%
- Trend gate (200 DMA): 29/79 symbols below 200 DMA (37% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.735%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 66 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-11T22:59:45Z

*From outcome_tracker run `outcome_tracker-20260611T225945-b5264921`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$210.67 return=-3.719%
- JNJ entry: fill=$230.248 current=$237.68 return=+3.228%
- EQIX entry: fill=$1084.37 current=$1043.18 return=-3.798%
- EQIX entry: fill=$1079.5 current=$1043.18 return=-3.365%
- EQIX exit: fill=$1078.442 current=$1043.18 return=-3.270%
- EQIX entry: fill=$1078.41 current=$1043.18 return=-3.267%
- JNJ entry: fill=$230.116 current=$237.68 return=+3.287%
- WMT entry: fill=$132.276 current=$120.3 return=-9.054%
- WMT entry: fill=$132.474 current=$120.3 return=-9.190%
- EQIX entry: fill=$1076.89 current=$1043.18 return=-3.130%
- EQIX entry: fill=$1076.82 current=$1043.18 return=-3.124%
- JNJ entry: fill=$230.044 current=$237.68 return=+3.319%
- EQIX exit: fill=$1076.718 current=$1043.18 return=-3.115%
- EQIX entry: fill=$1076.542 current=$1043.18 return=-3.099%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-11

*From trigger_performance run `trigger_performance-20260611T230626-d208f787`*
*Period: 2026-06-05 to 2026-06-11 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 57% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 45/79 symbols blocked (57%). Avg spread (blocked): 11.552%
- Trend gate (200 DMA): 29/79 symbols below 200 DMA (37% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.735%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 66 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-12T22:14:33Z

*From outcome_tracker run `outcome_tracker-20260612T221433-ef2ccf9f`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$214.28 return=-2.069%
- JNJ entry: fill=$230.248 current=$240.63 return=+4.509%
- EQIX entry: fill=$1084.37 current=$1055.85 return=-2.630%
- EQIX entry: fill=$1079.5 current=$1055.85 return=-2.191%
- EQIX exit: fill=$1078.442 current=$1055.85 return=-2.095%
- EQIX entry: fill=$1078.41 current=$1055.85 return=-2.092%
- JNJ entry: fill=$230.116 current=$240.63 return=+4.569%
- WMT entry: fill=$132.276 current=$120.855 return=-8.634%
- WMT entry: fill=$132.474 current=$120.855 return=-8.771%
- EQIX entry: fill=$1076.89 current=$1055.85 return=-1.954%
- EQIX entry: fill=$1076.82 current=$1055.85 return=-1.947%
- JNJ entry: fill=$230.044 current=$240.63 return=+4.602%
- EQIX exit: fill=$1076.718 current=$1055.85 return=-1.938%
- EQIX entry: fill=$1076.542 current=$1055.85 return=-1.922%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-12

*From trigger_performance run `trigger_performance-20260612T221434-4b7c3b8b`*
*Period: 2026-06-06 to 2026-06-12 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 10.416%
- Trend gate (200 DMA): 27/79 symbols below 200 DMA (34% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.612%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-12T22:25:11Z

*From outcome_tracker run `outcome_tracker-20260612T222511-d26291ae`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$214.28 return=-2.069%
- JNJ entry: fill=$230.248 current=$240.63 return=+4.509%
- EQIX entry: fill=$1084.37 current=$1055.85 return=-2.630%
- EQIX entry: fill=$1079.5 current=$1055.85 return=-2.191%
- EQIX exit: fill=$1078.442 current=$1055.85 return=-2.095%
- EQIX entry: fill=$1078.41 current=$1055.85 return=-2.092%
- JNJ entry: fill=$230.116 current=$240.63 return=+4.569%
- WMT entry: fill=$132.276 current=$120.855 return=-8.634%
- WMT entry: fill=$132.474 current=$120.855 return=-8.771%
- EQIX entry: fill=$1076.89 current=$1055.85 return=-1.954%
- EQIX entry: fill=$1076.82 current=$1055.85 return=-1.947%
- JNJ entry: fill=$230.044 current=$240.63 return=+4.602%
- EQIX exit: fill=$1076.718 current=$1055.85 return=-1.938%
- EQIX entry: fill=$1076.542 current=$1055.85 return=-1.922%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-12

*From trigger_performance run `trigger_performance-20260612T222511-d26291ae`*
*Period: 2026-06-06 to 2026-06-12 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 10.416%
- Trend gate (200 DMA): 27/79 symbols below 200 DMA (34% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.612%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-12T22:49:11Z

*From outcome_tracker run `outcome_tracker-20260612T224911-46ef9680`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$214.28 return=-2.069%
- JNJ entry: fill=$230.248 current=$240.63 return=+4.509%
- EQIX entry: fill=$1084.37 current=$1055.85 return=-2.630%
- EQIX entry: fill=$1079.5 current=$1055.85 return=-2.191%
- EQIX exit: fill=$1078.442 current=$1055.85 return=-2.095%
- EQIX entry: fill=$1078.41 current=$1055.85 return=-2.092%
- JNJ entry: fill=$230.116 current=$240.63 return=+4.569%
- WMT entry: fill=$132.276 current=$120.855 return=-8.634%
- WMT entry: fill=$132.474 current=$120.855 return=-8.771%
- EQIX entry: fill=$1076.89 current=$1055.85 return=-1.954%
- EQIX entry: fill=$1076.82 current=$1055.85 return=-1.947%
- JNJ entry: fill=$230.044 current=$240.63 return=+4.602%
- EQIX exit: fill=$1076.718 current=$1055.85 return=-1.938%
- EQIX entry: fill=$1076.542 current=$1055.85 return=-1.922%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Experiment Candidates — 2026-06-12

*From weekly review run weekly_review-2026-06-12*

**Observations (hypothesis candidates):**
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

**To propose a strategy experiment, open a PR with:**
- Hypothesis
- Supporting evidence (backtest or paper results)
- Success criteria
- Rollback plan

---
## Outcome Observations — 2026-06-15T22:50:21Z

*From outcome_tracker run `outcome_tracker-20260615T225021-86ab54e4`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$212.82 return=-2.737%
- JNJ entry: fill=$230.248 current=$235.66 return=+2.351%
- EQIX entry: fill=$1084.37 current=$1064.43 return=-1.839%
- EQIX entry: fill=$1079.5 current=$1064.43 return=-1.396%
- EQIX exit: fill=$1078.442 current=$1064.43 return=-1.299%
- EQIX entry: fill=$1078.41 current=$1064.43 return=-1.296%
- JNJ entry: fill=$230.116 current=$235.66 return=+2.409%
- WMT entry: fill=$132.276 current=$120.7 return=-8.751%
- WMT entry: fill=$132.474 current=$120.7 return=-8.888%
- EQIX entry: fill=$1076.89 current=$1064.43 return=-1.157%
- EQIX entry: fill=$1076.82 current=$1064.43 return=-1.151%
- JNJ entry: fill=$230.044 current=$235.66 return=+2.441%
- EQIX exit: fill=$1076.718 current=$1064.43 return=-1.141%
- EQIX entry: fill=$1076.542 current=$1064.43 return=-1.125%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-15

*From trigger_performance run `trigger_performance-20260615T225021-86ab54e4`*
*Period: 2026-06-09 to 2026-06-15 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 63% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 50/79 symbols blocked (63%). Avg spread (blocked): 9.891%
- Trend gate (200 DMA): 28/79 symbols below 200 DMA (35% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.684%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 78 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=13, LIQUIDITY_GATE_V1=13, MOMENTUM_BLEND_6M_12M_V1=13, SPREAD_GATE_V1=13, STOCK_TREND_200DMA_V1=13.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-15T23:03:05Z

*From outcome_tracker run `outcome_tracker-20260615T230305-a685193c`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$212.82 return=-2.737%
- JNJ entry: fill=$230.248 current=$235.66 return=+2.351%
- EQIX entry: fill=$1084.37 current=$1064.43 return=-1.839%
- EQIX entry: fill=$1079.5 current=$1064.43 return=-1.396%
- EQIX exit: fill=$1078.442 current=$1064.43 return=-1.299%
- EQIX entry: fill=$1078.41 current=$1064.43 return=-1.296%
- JNJ entry: fill=$230.116 current=$235.66 return=+2.409%
- WMT entry: fill=$132.276 current=$120.7 return=-8.751%
- WMT entry: fill=$132.474 current=$120.7 return=-8.888%
- EQIX entry: fill=$1076.89 current=$1064.43 return=-1.157%
- EQIX entry: fill=$1076.82 current=$1064.43 return=-1.151%
- JNJ entry: fill=$230.044 current=$235.66 return=+2.441%
- EQIX exit: fill=$1076.718 current=$1064.43 return=-1.141%
- EQIX entry: fill=$1076.542 current=$1064.43 return=-1.125%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-15

*From trigger_performance run `trigger_performance-20260615T230305-a685193c`*
*Period: 2026-06-09 to 2026-06-15 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 63% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 50/79 symbols blocked (63%). Avg spread (blocked): 9.891%
- Trend gate (200 DMA): 28/79 symbols below 200 DMA (35% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.684%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 78 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=13, LIQUIDITY_GATE_V1=13, MOMENTUM_BLEND_6M_12M_V1=13, SPREAD_GATE_V1=13, STOCK_TREND_200DMA_V1=13.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-15T23:10:43Z

*From outcome_tracker run `outcome_tracker-20260615T231043-74ccfff1`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$212.82 return=-2.737%
- JNJ entry: fill=$230.248 current=$235.66 return=+2.351%
- EQIX entry: fill=$1084.37 current=$1064.43 return=-1.839%
- EQIX entry: fill=$1079.5 current=$1064.43 return=-1.396%
- EQIX exit: fill=$1078.442 current=$1064.43 return=-1.299%
- EQIX entry: fill=$1078.41 current=$1064.43 return=-1.296%
- JNJ entry: fill=$230.116 current=$235.66 return=+2.409%
- WMT entry: fill=$132.276 current=$120.7 return=-8.751%
- WMT entry: fill=$132.474 current=$120.7 return=-8.888%
- EQIX entry: fill=$1076.89 current=$1064.43 return=-1.157%
- EQIX entry: fill=$1076.82 current=$1064.43 return=-1.151%
- JNJ entry: fill=$230.044 current=$235.66 return=+2.441%
- EQIX exit: fill=$1076.718 current=$1064.43 return=-1.141%
- EQIX entry: fill=$1076.542 current=$1064.43 return=-1.125%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-15

*From trigger_performance run `trigger_performance-20260615T231640-70da6184`*
*Period: 2026-06-09 to 2026-06-15 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 63% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 50/79 symbols blocked (63%). Avg spread (blocked): 9.891%
- Trend gate (200 DMA): 28/79 symbols below 200 DMA (35% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.684%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 78 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=13, LIQUIDITY_GATE_V1=13, MOMENTUM_BLEND_6M_12M_V1=13, SPREAD_GATE_V1=13, STOCK_TREND_200DMA_V1=13.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-16T22:35:23Z

*From outcome_tracker run `outcome_tracker-20260616T223523-2c913a20`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$213.5 return=-2.426%
- JNJ entry: fill=$230.248 current=$235.18 return=+2.142%
- EQIX entry: fill=$1084.37 current=$1094.68 return=+0.951%
- EQIX entry: fill=$1079.5 current=$1094.68 return=+1.406%
- EQIX exit: fill=$1078.442 current=$1094.68 return=+1.506%
- EQIX entry: fill=$1078.41 current=$1094.68 return=+1.509%
- JNJ entry: fill=$230.116 current=$235.18 return=+2.201%
- WMT entry: fill=$132.276 current=$120.99 return=-8.532%
- WMT entry: fill=$132.474 current=$120.99 return=-8.669%
- EQIX entry: fill=$1076.89 current=$1094.68 return=+1.652%
- EQIX entry: fill=$1076.82 current=$1094.68 return=+1.659%
- JNJ entry: fill=$230.044 current=$235.18 return=+2.233%
- EQIX exit: fill=$1076.718 current=$1094.68 return=+1.668%
- EQIX entry: fill=$1076.542 current=$1094.68 return=+1.685%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-16

*From trigger_performance run `trigger_performance-20260616T223523-2c913a20`*
*Period: 2026-06-10 to 2026-06-16 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.124%
- Trend gate (200 DMA): 24/79 symbols below 200 DMA (30% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -0.073%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 12 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=2, LIQUIDITY_GATE_V1=2, MOMENTUM_BLEND_6M_12M_V1=2, SPREAD_GATE_V1=2, STOCK_TREND_200DMA_V1=2.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-16T22:52:57Z

*From outcome_tracker run `outcome_tracker-20260616T225257-d8af4163`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$213.5 return=-2.426%
- JNJ entry: fill=$230.248 current=$235.18 return=+2.142%
- EQIX entry: fill=$1084.37 current=$1094.68 return=+0.951%
- EQIX entry: fill=$1079.5 current=$1094.68 return=+1.406%
- EQIX exit: fill=$1078.442 current=$1094.68 return=+1.506%
- EQIX entry: fill=$1078.41 current=$1094.68 return=+1.509%
- JNJ entry: fill=$230.116 current=$235.18 return=+2.201%
- WMT entry: fill=$132.276 current=$120.99 return=-8.532%
- WMT entry: fill=$132.474 current=$120.99 return=-8.669%
- EQIX entry: fill=$1076.89 current=$1094.68 return=+1.652%
- EQIX entry: fill=$1076.82 current=$1094.68 return=+1.659%
- JNJ entry: fill=$230.044 current=$235.18 return=+2.233%
- EQIX exit: fill=$1076.718 current=$1094.68 return=+1.668%
- EQIX entry: fill=$1076.542 current=$1094.68 return=+1.685%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-16

*From trigger_performance run `trigger_performance-20260616T225258-8a1a23aa`*
*Period: 2026-06-10 to 2026-06-16 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.124%
- Trend gate (200 DMA): 24/79 symbols below 200 DMA (30% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -0.073%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 12 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=2, LIQUIDITY_GATE_V1=2, MOMENTUM_BLEND_6M_12M_V1=2, SPREAD_GATE_V1=2, STOCK_TREND_200DMA_V1=2.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-16T22:57:42Z

*From outcome_tracker run `outcome_tracker-20260616T225742-4519fa61`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$213.5 return=-2.426%
- JNJ entry: fill=$230.248 current=$235.18 return=+2.142%
- EQIX entry: fill=$1084.37 current=$1094.68 return=+0.951%
- EQIX entry: fill=$1079.5 current=$1094.68 return=+1.406%
- EQIX exit: fill=$1078.442 current=$1094.68 return=+1.506%
- EQIX entry: fill=$1078.41 current=$1094.68 return=+1.509%
- JNJ entry: fill=$230.116 current=$235.18 return=+2.201%
- WMT entry: fill=$132.276 current=$120.99 return=-8.532%
- WMT entry: fill=$132.474 current=$120.99 return=-8.669%
- EQIX entry: fill=$1076.89 current=$1094.68 return=+1.652%
- EQIX entry: fill=$1076.82 current=$1094.68 return=+1.659%
- JNJ entry: fill=$230.044 current=$235.18 return=+2.233%
- EQIX exit: fill=$1076.718 current=$1094.68 return=+1.668%
- EQIX entry: fill=$1076.542 current=$1094.68 return=+1.685%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-16

*From trigger_performance run `trigger_performance-20260616T230320-0d92ee4a`*
*Period: 2026-06-10 to 2026-06-16 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.124%
- Trend gate (200 DMA): 24/79 symbols below 200 DMA (30% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -0.073%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 12 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=2, LIQUIDITY_GATE_V1=2, MOMENTUM_BLEND_6M_12M_V1=2, SPREAD_GATE_V1=2, STOCK_TREND_200DMA_V1=2.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-17T22:26:05Z

*From outcome_tracker run `outcome_tracker-20260617T222605-1ce0d134`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$207.0 return=-5.396%
- JNJ entry: fill=$230.248 current=$232.2448 return=+0.867%
- EQIX entry: fill=$1084.37 current=$1087.43 return=+0.282%
- EQIX entry: fill=$1079.5 current=$1087.43 return=+0.735%
- EQIX exit: fill=$1078.442 current=$1087.43 return=+0.833%
- EQIX entry: fill=$1078.41 current=$1087.43 return=+0.836%
- JNJ entry: fill=$230.116 current=$232.2448 return=+0.925%
- WMT entry: fill=$132.276 current=$118.16 return=-10.672%
- WMT entry: fill=$132.474 current=$118.16 return=-10.805%
- EQIX entry: fill=$1076.89 current=$1087.43 return=+0.979%
- EQIX entry: fill=$1076.82 current=$1087.43 return=+0.985%
- JNJ entry: fill=$230.044 current=$232.2448 return=+0.957%
- EQIX exit: fill=$1076.718 current=$1087.43 return=+0.995%
- EQIX entry: fill=$1076.542 current=$1087.43 return=+1.011%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-17

*From trigger_performance run `trigger_performance-20260617T222605-1ce0d134`*
*Period: 2026-06-11 to 2026-06-17 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 10.947%
- Trend gate (200 DMA): 30/79 symbols below 200 DMA (38% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.248%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 24 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=4, LIQUIDITY_GATE_V1=4, MOMENTUM_BLEND_6M_12M_V1=4, SPREAD_GATE_V1=4, STOCK_TREND_200DMA_V1=4.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-17T22:45:21Z

*From outcome_tracker run `outcome_tracker-20260617T224521-4d18f2ea`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$207.0 return=-5.396%
- JNJ entry: fill=$230.248 current=$232.2448 return=+0.867%
- EQIX entry: fill=$1084.37 current=$1087.43 return=+0.282%
- EQIX entry: fill=$1079.5 current=$1087.43 return=+0.735%
- EQIX exit: fill=$1078.442 current=$1087.43 return=+0.833%
- EQIX entry: fill=$1078.41 current=$1087.43 return=+0.836%
- JNJ entry: fill=$230.116 current=$232.2448 return=+0.925%
- WMT entry: fill=$132.276 current=$118.16 return=-10.672%
- WMT entry: fill=$132.474 current=$118.16 return=-10.805%
- EQIX entry: fill=$1076.89 current=$1087.43 return=+0.979%
- EQIX entry: fill=$1076.82 current=$1087.43 return=+0.985%
- JNJ entry: fill=$230.044 current=$232.2448 return=+0.957%
- EQIX exit: fill=$1076.718 current=$1087.43 return=+0.995%
- EQIX entry: fill=$1076.542 current=$1087.43 return=+1.011%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-17

*From trigger_performance run `trigger_performance-20260617T224521-4d18f2ea`*
*Period: 2026-06-11 to 2026-06-17 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 10.947%
- Trend gate (200 DMA): 30/79 symbols below 200 DMA (38% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.248%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 24 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=4, LIQUIDITY_GATE_V1=4, MOMENTUM_BLEND_6M_12M_V1=4, SPREAD_GATE_V1=4, STOCK_TREND_200DMA_V1=4.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-17T22:53:51Z

*From outcome_tracker run `outcome_tracker-20260617T225351-d14de65d`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$207.0 return=-5.396%
- JNJ entry: fill=$230.248 current=$232.2448 return=+0.867%
- EQIX entry: fill=$1084.37 current=$1087.43 return=+0.282%
- EQIX entry: fill=$1079.5 current=$1087.43 return=+0.735%
- EQIX exit: fill=$1078.442 current=$1087.43 return=+0.833%
- EQIX entry: fill=$1078.41 current=$1087.43 return=+0.836%
- JNJ entry: fill=$230.116 current=$232.2448 return=+0.925%
- WMT entry: fill=$132.276 current=$118.16 return=-10.672%
- WMT entry: fill=$132.474 current=$118.16 return=-10.805%
- EQIX entry: fill=$1076.89 current=$1087.43 return=+0.979%
- EQIX entry: fill=$1076.82 current=$1087.43 return=+0.985%
- JNJ entry: fill=$230.044 current=$232.2448 return=+0.957%
- EQIX exit: fill=$1076.718 current=$1087.43 return=+0.995%
- EQIX entry: fill=$1076.542 current=$1087.43 return=+1.011%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-17

*From trigger_performance run `trigger_performance-20260617T225700-197d2750`*
*Period: 2026-06-11 to 2026-06-17 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 10.947%
- Trend gate (200 DMA): 30/79 symbols below 200 DMA (38% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.248%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 24 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=4, LIQUIDITY_GATE_V1=4, MOMENTUM_BLEND_6M_12M_V1=4, SPREAD_GATE_V1=4, STOCK_TREND_200DMA_V1=4.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-18T22:33:20Z

*From outcome_tracker run `outcome_tracker-20260618T223320-ab5b0674`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$206.65 return=-5.557%
- JNJ entry: fill=$230.248 current=$228.39 return=-0.807%
- EQIX entry: fill=$1084.37 current=$1092.19 return=+0.721%
- EQIX entry: fill=$1079.5 current=$1092.19 return=+1.175%
- EQIX exit: fill=$1078.442 current=$1092.19 return=+1.275%
- EQIX entry: fill=$1078.41 current=$1092.19 return=+1.278%
- JNJ entry: fill=$230.116 current=$228.39 return=-0.750%
- WMT entry: fill=$132.276 current=$116.92 return=-11.609%
- WMT entry: fill=$132.474 current=$116.92 return=-11.741%
- EQIX entry: fill=$1076.89 current=$1092.19 return=+1.421%
- EQIX entry: fill=$1076.82 current=$1092.19 return=+1.427%
- JNJ entry: fill=$230.044 current=$228.39 return=-0.719%
- EQIX exit: fill=$1076.718 current=$1092.19 return=+1.437%
- EQIX entry: fill=$1076.542 current=$1092.19 return=+1.454%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-18

*From trigger_performance run `trigger_performance-20260618T223321-573ba9e2`*
*Period: 2026-06-12 to 2026-06-18 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 9.701%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.500%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 48 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=8, LIQUIDITY_GATE_V1=8, MOMENTUM_BLEND_6M_12M_V1=8, SPREAD_GATE_V1=8, STOCK_TREND_200DMA_V1=8.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-18T22:56:08Z

*From outcome_tracker run `outcome_tracker-20260618T225608-677edc25`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$206.65 return=-5.557%
- JNJ entry: fill=$230.248 current=$228.39 return=-0.807%
- EQIX entry: fill=$1084.37 current=$1092.19 return=+0.721%
- EQIX entry: fill=$1079.5 current=$1092.19 return=+1.175%
- EQIX exit: fill=$1078.442 current=$1092.19 return=+1.275%
- EQIX entry: fill=$1078.41 current=$1092.19 return=+1.278%
- JNJ entry: fill=$230.116 current=$228.39 return=-0.750%
- WMT entry: fill=$132.276 current=$116.92 return=-11.609%
- WMT entry: fill=$132.474 current=$116.92 return=-11.741%
- EQIX entry: fill=$1076.89 current=$1092.19 return=+1.421%
- EQIX entry: fill=$1076.82 current=$1092.19 return=+1.427%
- JNJ entry: fill=$230.044 current=$228.39 return=-0.719%
- EQIX exit: fill=$1076.718 current=$1092.19 return=+1.437%
- EQIX entry: fill=$1076.542 current=$1092.19 return=+1.454%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-18

*From trigger_performance run `trigger_performance-20260618T225608-677edc25`*
*Period: 2026-06-12 to 2026-06-18 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 9.701%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.500%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 48 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=8, LIQUIDITY_GATE_V1=8, MOMENTUM_BLEND_6M_12M_V1=8, SPREAD_GATE_V1=8, STOCK_TREND_200DMA_V1=8.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-18T23:11:32Z

*From outcome_tracker run `outcome_tracker-20260618T231132-94b767e0`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$206.65 return=-5.557%
- JNJ entry: fill=$230.248 current=$228.39 return=-0.807%
- EQIX entry: fill=$1084.37 current=$1092.19 return=+0.721%
- EQIX entry: fill=$1079.5 current=$1092.19 return=+1.175%
- EQIX exit: fill=$1078.442 current=$1092.19 return=+1.275%
- EQIX entry: fill=$1078.41 current=$1092.19 return=+1.278%
- JNJ entry: fill=$230.116 current=$228.39 return=-0.750%
- WMT entry: fill=$132.276 current=$116.92 return=-11.609%
- WMT entry: fill=$132.474 current=$116.92 return=-11.741%
- EQIX entry: fill=$1076.89 current=$1092.19 return=+1.421%
- EQIX entry: fill=$1076.82 current=$1092.19 return=+1.427%
- JNJ entry: fill=$230.044 current=$228.39 return=-0.719%
- EQIX exit: fill=$1076.718 current=$1092.19 return=+1.437%
- EQIX entry: fill=$1076.542 current=$1092.19 return=+1.454%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-18

*From trigger_performance run `trigger_performance-20260618T231743-7fffceb2`*
*Period: 2026-06-12 to 2026-06-18 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 9.701%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.500%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 48 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=8, LIQUIDITY_GATE_V1=8, MOMENTUM_BLEND_6M_12M_V1=8, SPREAD_GATE_V1=8, STOCK_TREND_200DMA_V1=8.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-19T21:49:23Z

*From outcome_tracker run `outcome_tracker-20260619T214923-d67ecf86`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$206.65 return=-5.557%
- JNJ entry: fill=$230.248 current=$228.39 return=-0.807%
- EQIX entry: fill=$1084.37 current=$1092.19 return=+0.721%
- EQIX entry: fill=$1079.5 current=$1092.19 return=+1.175%
- EQIX exit: fill=$1078.442 current=$1092.19 return=+1.275%
- EQIX entry: fill=$1078.41 current=$1092.19 return=+1.278%
- JNJ entry: fill=$230.116 current=$228.39 return=-0.750%
- WMT entry: fill=$132.276 current=$117.18 return=-11.412%
- WMT entry: fill=$132.474 current=$117.18 return=-11.545%
- EQIX entry: fill=$1076.89 current=$1092.19 return=+1.421%
- EQIX entry: fill=$1076.82 current=$1092.19 return=+1.427%
- JNJ entry: fill=$230.044 current=$228.39 return=-0.719%
- EQIX exit: fill=$1076.718 current=$1092.19 return=+1.437%
- EQIX entry: fill=$1076.542 current=$1092.19 return=+1.454%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-19

*From trigger_performance run `trigger_performance-20260619T214924-61704322`*
*Period: 2026-06-13 to 2026-06-19 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 9.701%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.472%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 48 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=8, LIQUIDITY_GATE_V1=8, MOMENTUM_BLEND_6M_12M_V1=8, SPREAD_GATE_V1=8, STOCK_TREND_200DMA_V1=8.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-19T22:04:11Z

*From outcome_tracker run `outcome_tracker-20260619T220411-92718a8f`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$206.65 return=-5.557%
- JNJ entry: fill=$230.248 current=$228.39 return=-0.807%
- EQIX entry: fill=$1084.37 current=$1092.19 return=+0.721%
- EQIX entry: fill=$1079.5 current=$1092.19 return=+1.175%
- EQIX exit: fill=$1078.442 current=$1092.19 return=+1.275%
- EQIX entry: fill=$1078.41 current=$1092.19 return=+1.278%
- JNJ entry: fill=$230.116 current=$228.39 return=-0.750%
- WMT entry: fill=$132.276 current=$117.18 return=-11.412%
- WMT entry: fill=$132.474 current=$117.18 return=-11.545%
- EQIX entry: fill=$1076.89 current=$1092.19 return=+1.421%
- EQIX entry: fill=$1076.82 current=$1092.19 return=+1.427%
- JNJ entry: fill=$230.044 current=$228.39 return=-0.719%
- EQIX exit: fill=$1076.718 current=$1092.19 return=+1.437%
- EQIX entry: fill=$1076.542 current=$1092.19 return=+1.454%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-19

*From trigger_performance run `trigger_performance-20260619T220411-92718a8f`*
*Period: 2026-06-13 to 2026-06-19 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 9.701%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.472%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 48 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=8, LIQUIDITY_GATE_V1=8, MOMENTUM_BLEND_6M_12M_V1=8, SPREAD_GATE_V1=8, STOCK_TREND_200DMA_V1=8.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-19T22:14:40Z

*From outcome_tracker run `outcome_tracker-20260619T221440-c77da9be`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$206.65 return=-5.557%
- JNJ entry: fill=$230.248 current=$228.39 return=-0.807%
- EQIX entry: fill=$1084.37 current=$1092.19 return=+0.721%
- EQIX entry: fill=$1079.5 current=$1092.19 return=+1.175%
- EQIX exit: fill=$1078.442 current=$1092.19 return=+1.275%
- EQIX entry: fill=$1078.41 current=$1092.19 return=+1.278%
- JNJ entry: fill=$230.116 current=$228.39 return=-0.750%
- WMT entry: fill=$132.276 current=$117.18 return=-11.412%
- WMT entry: fill=$132.474 current=$117.18 return=-11.545%
- EQIX entry: fill=$1076.89 current=$1092.19 return=+1.421%
- EQIX entry: fill=$1076.82 current=$1092.19 return=+1.427%
- JNJ entry: fill=$230.044 current=$228.39 return=-0.719%
- EQIX exit: fill=$1076.718 current=$1092.19 return=+1.437%
- EQIX entry: fill=$1076.542 current=$1092.19 return=+1.454%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Experiment Candidates — 2026-06-19

*From weekly review run weekly_review-2026-06-19*

**Observations (hypothesis candidates):**
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

**To propose a strategy experiment, open a PR with:**
- Hypothesis
- Supporting evidence (backtest or paper results)
- Success criteria
- Rollback plan

---
## Outcome Observations — 2026-06-22T22:25:33Z

*From outcome_tracker run `outcome_tracker-20260622T222533-9cc40141`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$211.45 return=-3.363%
- JNJ entry: fill=$230.248 current=$229.9352 return=-0.136%
- EQIX entry: fill=$1084.37 current=$1115.94 return=+2.911%
- EQIX entry: fill=$1079.5 current=$1115.94 return=+3.376%
- EQIX exit: fill=$1078.442 current=$1115.94 return=+3.477%
- EQIX entry: fill=$1078.41 current=$1115.94 return=+3.480%
- JNJ entry: fill=$230.116 current=$229.9352 return=-0.079%
- WMT entry: fill=$132.276 current=$117.1 return=-11.473%
- WMT entry: fill=$132.474 current=$117.1 return=-11.605%
- EQIX entry: fill=$1076.89 current=$1115.94 return=+3.626%
- EQIX entry: fill=$1076.82 current=$1115.94 return=+3.633%
- JNJ entry: fill=$230.044 current=$229.9352 return=-0.047%
- EQIX exit: fill=$1076.718 current=$1115.94 return=+3.643%
- EQIX entry: fill=$1076.542 current=$1115.94 return=+3.660%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-22

*From trigger_performance run `trigger_performance-20260622T222533-9cc40141`*
*Period: 2026-06-16 to 2026-06-22 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 10.425%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +0.079%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 60 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=10, LIQUIDITY_GATE_V1=10, MOMENTUM_BLEND_6M_12M_V1=10, SPREAD_GATE_V1=10, STOCK_TREND_200DMA_V1=10.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-22T22:47:45Z

*From outcome_tracker run `outcome_tracker-20260622T224745-5c80fc97`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$211.45 return=-3.363%
- JNJ entry: fill=$230.248 current=$229.9352 return=-0.136%
- EQIX entry: fill=$1084.37 current=$1115.94 return=+2.911%
- EQIX entry: fill=$1079.5 current=$1115.94 return=+3.376%
- EQIX exit: fill=$1078.442 current=$1115.94 return=+3.477%
- EQIX entry: fill=$1078.41 current=$1115.94 return=+3.480%
- JNJ entry: fill=$230.116 current=$229.9352 return=-0.079%
- WMT entry: fill=$132.276 current=$117.1 return=-11.473%
- WMT entry: fill=$132.474 current=$117.1 return=-11.605%
- EQIX entry: fill=$1076.89 current=$1115.94 return=+3.626%
- EQIX entry: fill=$1076.82 current=$1115.94 return=+3.633%
- JNJ entry: fill=$230.044 current=$229.9352 return=-0.047%
- EQIX exit: fill=$1076.718 current=$1115.94 return=+3.643%
- EQIX entry: fill=$1076.542 current=$1115.94 return=+3.660%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-22

*From trigger_performance run `trigger_performance-20260622T224746-eb6438c7`*
*Period: 2026-06-16 to 2026-06-22 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 10.425%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +0.079%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 60 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=10, LIQUIDITY_GATE_V1=10, MOMENTUM_BLEND_6M_12M_V1=10, SPREAD_GATE_V1=10, STOCK_TREND_200DMA_V1=10.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-22T22:56:22Z

*From outcome_tracker run `outcome_tracker-20260622T225622-243e1086`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$211.45 return=-3.363%
- JNJ entry: fill=$230.248 current=$229.9352 return=-0.136%
- EQIX entry: fill=$1084.37 current=$1115.94 return=+2.911%
- EQIX entry: fill=$1079.5 current=$1115.94 return=+3.376%
- EQIX exit: fill=$1078.442 current=$1115.94 return=+3.477%
- EQIX entry: fill=$1078.41 current=$1115.94 return=+3.480%
- JNJ entry: fill=$230.116 current=$229.9352 return=-0.079%
- WMT entry: fill=$132.276 current=$117.1 return=-11.473%
- WMT entry: fill=$132.474 current=$117.1 return=-11.605%
- EQIX entry: fill=$1076.89 current=$1115.94 return=+3.626%
- EQIX entry: fill=$1076.82 current=$1115.94 return=+3.633%
- JNJ entry: fill=$230.044 current=$229.9352 return=-0.047%
- EQIX exit: fill=$1076.718 current=$1115.94 return=+3.643%
- EQIX entry: fill=$1076.542 current=$1115.94 return=+3.660%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-22

*From trigger_performance run `trigger_performance-20260622T230051-646a433f`*
*Period: 2026-06-16 to 2026-06-22 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 10.425%
- Trend gate (200 DMA): 33/79 symbols below 200 DMA (42% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +0.079%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 60 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=10, LIQUIDITY_GATE_V1=10, MOMENTUM_BLEND_6M_12M_V1=10, SPREAD_GATE_V1=10, STOCK_TREND_200DMA_V1=10.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-23T22:04:24Z

*From outcome_tracker run `outcome_tracker-20260623T220424-90df8ed0`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.67 return=-0.520%
- JNJ entry: fill=$230.248 current=$239.479 return=+4.009%
- EQIX entry: fill=$1084.37 current=$1118.0 return=+3.101%
- EQIX entry: fill=$1079.5 current=$1118.0 return=+3.567%
- EQIX exit: fill=$1078.442 current=$1118.0 return=+3.668%
- EQIX entry: fill=$1078.41 current=$1118.0 return=+3.671%
- JNJ entry: fill=$230.116 current=$239.479 return=+4.069%
- WMT entry: fill=$132.276 current=$119.5 return=-9.659%
- WMT entry: fill=$132.474 current=$119.5 return=-9.794%
- EQIX entry: fill=$1076.89 current=$1118.0 return=+3.817%
- EQIX entry: fill=$1076.82 current=$1118.0 return=+3.824%
- JNJ entry: fill=$230.044 current=$239.479 return=+4.101%
- EQIX exit: fill=$1076.718 current=$1118.0 return=+3.834%
- EQIX entry: fill=$1076.542 current=$1118.0 return=+3.851%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-23

*From trigger_performance run `trigger_performance-20260623T220425-7cafea00`*
*Period: 2026-06-17 to 2026-06-23 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.887%
- Trend gate (200 DMA): 30/79 symbols below 200 DMA (38% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +1.539%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 66 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-23T22:13:39Z

*From outcome_tracker run `outcome_tracker-20260623T221339-e4dcb452`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.67 return=-0.520%
- JNJ entry: fill=$230.248 current=$239.479 return=+4.009%
- EQIX entry: fill=$1084.37 current=$1118.0 return=+3.101%
- EQIX entry: fill=$1079.5 current=$1118.0 return=+3.567%
- EQIX exit: fill=$1078.442 current=$1118.0 return=+3.668%
- EQIX entry: fill=$1078.41 current=$1118.0 return=+3.671%
- JNJ entry: fill=$230.116 current=$239.479 return=+4.069%
- WMT entry: fill=$132.276 current=$119.5 return=-9.659%
- WMT entry: fill=$132.474 current=$119.5 return=-9.794%
- EQIX entry: fill=$1076.89 current=$1118.0 return=+3.817%
- EQIX entry: fill=$1076.82 current=$1118.0 return=+3.824%
- JNJ entry: fill=$230.044 current=$239.479 return=+4.101%
- EQIX exit: fill=$1076.718 current=$1118.0 return=+3.834%
- EQIX entry: fill=$1076.542 current=$1118.0 return=+3.851%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-23

*From trigger_performance run `trigger_performance-20260623T221339-e4dcb452`*
*Period: 2026-06-17 to 2026-06-23 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.887%
- Trend gate (200 DMA): 30/79 symbols below 200 DMA (38% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +1.539%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 66 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-23T22:39:25Z

*From outcome_tracker run `outcome_tracker-20260623T223925-07a616e9`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$217.67 return=-0.520%
- JNJ entry: fill=$230.248 current=$239.479 return=+4.009%
- EQIX entry: fill=$1084.37 current=$1118.0 return=+3.101%
- EQIX entry: fill=$1079.5 current=$1118.0 return=+3.567%
- EQIX exit: fill=$1078.442 current=$1118.0 return=+3.668%
- EQIX entry: fill=$1078.41 current=$1118.0 return=+3.671%
- JNJ entry: fill=$230.116 current=$239.479 return=+4.069%
- WMT entry: fill=$132.276 current=$119.5 return=-9.659%
- WMT entry: fill=$132.474 current=$119.5 return=-9.794%
- EQIX entry: fill=$1076.89 current=$1118.0 return=+3.817%
- EQIX entry: fill=$1076.82 current=$1118.0 return=+3.824%
- JNJ entry: fill=$230.044 current=$239.479 return=+4.101%
- EQIX exit: fill=$1076.718 current=$1118.0 return=+3.834%
- EQIX entry: fill=$1076.542 current=$1118.0 return=+3.851%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-23

*From trigger_performance run `trigger_performance-20260623T224613-661baa62`*
*Period: 2026-06-17 to 2026-06-23 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.887%
- Trend gate (200 DMA): 30/79 symbols below 200 DMA (38% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +1.539%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 66 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-24T22:00:53Z

*From outcome_tracker run `outcome_tracker-20260624T220053-6aa24c4e`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$222.0 return=+1.459%
- JNJ entry: fill=$230.248 current=$239.0084 return=+3.805%
- EQIX entry: fill=$1084.37 current=$1093.56 return=+0.848%
- EQIX entry: fill=$1079.5 current=$1093.56 return=+1.302%
- EQIX exit: fill=$1078.442 current=$1093.56 return=+1.402%
- EQIX entry: fill=$1078.41 current=$1093.56 return=+1.405%
- JNJ entry: fill=$230.116 current=$239.0084 return=+3.864%
- WMT entry: fill=$132.276 current=$117.77 return=-10.966%
- WMT entry: fill=$132.474 current=$117.77 return=-11.099%
- EQIX entry: fill=$1076.89 current=$1093.56 return=+1.548%
- EQIX entry: fill=$1076.82 current=$1093.56 return=+1.555%
- JNJ entry: fill=$230.044 current=$239.0084 return=+3.897%
- EQIX exit: fill=$1076.718 current=$1093.56 return=+1.564%
- EQIX entry: fill=$1076.542 current=$1093.56 return=+1.581%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-24

*From trigger_performance run `trigger_performance-20260624T220053-6aa24c4e`*
*Period: 2026-06-18 to 2026-06-24 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 68% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 54/79 symbols blocked (68%). Avg spread (blocked): 10.702%
- Trend gate (200 DMA): 26/79 symbols below 200 DMA (33% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +0.154%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 6 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=1, LIQUIDITY_GATE_V1=1, MOMENTUM_BLEND_6M_12M_V1=1, SPREAD_GATE_V1=1, STOCK_TREND_200DMA_V1=1.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-24T22:18:20Z

*From outcome_tracker run `outcome_tracker-20260624T221820-4233c1d2`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$222.0 return=+1.459%
- JNJ entry: fill=$230.248 current=$239.0084 return=+3.805%
- EQIX entry: fill=$1084.37 current=$1093.56 return=+0.848%
- EQIX entry: fill=$1079.5 current=$1093.56 return=+1.302%
- EQIX exit: fill=$1078.442 current=$1093.56 return=+1.402%
- EQIX entry: fill=$1078.41 current=$1093.56 return=+1.405%
- JNJ entry: fill=$230.116 current=$239.0084 return=+3.864%
- WMT entry: fill=$132.276 current=$117.77 return=-10.966%
- WMT entry: fill=$132.474 current=$117.77 return=-11.099%
- EQIX entry: fill=$1076.89 current=$1093.56 return=+1.548%
- EQIX entry: fill=$1076.82 current=$1093.56 return=+1.555%
- JNJ entry: fill=$230.044 current=$239.0084 return=+3.897%
- EQIX exit: fill=$1076.718 current=$1093.56 return=+1.564%
- EQIX entry: fill=$1076.542 current=$1093.56 return=+1.581%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-24

*From trigger_performance run `trigger_performance-20260624T221820-4233c1d2`*
*Period: 2026-06-18 to 2026-06-24 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 68% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 54/79 symbols blocked (68%). Avg spread (blocked): 10.702%
- Trend gate (200 DMA): 26/79 symbols below 200 DMA (33% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +0.154%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 6 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=1, LIQUIDITY_GATE_V1=1, MOMENTUM_BLEND_6M_12M_V1=1, SPREAD_GATE_V1=1, STOCK_TREND_200DMA_V1=1.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-24T22:41:06Z

*From outcome_tracker run `outcome_tracker-20260624T224106-7ac8c36c`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$222.0 return=+1.459%
- JNJ entry: fill=$230.248 current=$239.0084 return=+3.805%
- EQIX entry: fill=$1084.37 current=$1093.56 return=+0.848%
- EQIX entry: fill=$1079.5 current=$1093.56 return=+1.302%
- EQIX exit: fill=$1078.442 current=$1093.56 return=+1.402%
- EQIX entry: fill=$1078.41 current=$1093.56 return=+1.405%
- JNJ entry: fill=$230.116 current=$239.0084 return=+3.864%
- WMT entry: fill=$132.276 current=$117.77 return=-10.966%
- WMT entry: fill=$132.474 current=$117.77 return=-11.099%
- EQIX entry: fill=$1076.89 current=$1093.56 return=+1.548%
- EQIX entry: fill=$1076.82 current=$1093.56 return=+1.555%
- JNJ entry: fill=$230.044 current=$239.0084 return=+3.897%
- EQIX exit: fill=$1076.718 current=$1093.56 return=+1.564%
- EQIX entry: fill=$1076.542 current=$1093.56 return=+1.581%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-24

*From trigger_performance run `trigger_performance-20260624T224647-f5d08b9e`*
*Period: 2026-06-18 to 2026-06-24 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 68% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 54/79 symbols blocked (68%). Avg spread (blocked): 10.702%
- Trend gate (200 DMA): 26/79 symbols below 200 DMA (33% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +0.154%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 6 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=1, LIQUIDITY_GATE_V1=1, MOMENTUM_BLEND_6M_12M_V1=1, SPREAD_GATE_V1=1, STOCK_TREND_200DMA_V1=1.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-25T22:10:21Z

*From outcome_tracker run `outcome_tracker-20260625T221021-4b5eee91`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$223.73 return=+2.250%
- JNJ entry: fill=$230.248 current=$245.2144 return=+6.500%
- EQIX entry: fill=$1084.37 current=$1087.61 return=+0.299%
- EQIX entry: fill=$1079.5 current=$1087.61 return=+0.751%
- EQIX exit: fill=$1078.442 current=$1087.61 return=+0.850%
- EQIX entry: fill=$1078.41 current=$1087.61 return=+0.853%
- JNJ entry: fill=$230.116 current=$245.2144 return=+6.561%
- WMT entry: fill=$132.276 current=$116.15 return=-12.191%
- WMT entry: fill=$132.474 current=$116.15 return=-12.322%
- EQIX entry: fill=$1076.89 current=$1087.61 return=+0.996%
- EQIX entry: fill=$1076.82 current=$1087.61 return=+1.002%
- JNJ entry: fill=$230.044 current=$245.2144 return=+6.595%
- EQIX exit: fill=$1076.718 current=$1087.61 return=+1.012%
- EQIX entry: fill=$1076.542 current=$1087.61 return=+1.028%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-25

*From trigger_performance run `trigger_performance-20260625T221021-4b5eee91`*
*Period: 2026-06-19 to 2026-06-25 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 77% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 61/79 symbols blocked (77%). Avg spread (blocked): 11.708%
- Trend gate (200 DMA): 29/79 symbols below 200 DMA (37% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +0.299%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 24 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=4, LIQUIDITY_GATE_V1=4, MOMENTUM_BLEND_6M_12M_V1=4, SPREAD_GATE_V1=4, STOCK_TREND_200DMA_V1=4.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-25T22:21:32Z

*From outcome_tracker run `outcome_tracker-20260625T222132-94b92b2b`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$223.73 return=+2.250%
- JNJ entry: fill=$230.248 current=$245.2144 return=+6.500%
- EQIX entry: fill=$1084.37 current=$1087.61 return=+0.299%
- EQIX entry: fill=$1079.5 current=$1087.61 return=+0.751%
- EQIX exit: fill=$1078.442 current=$1087.61 return=+0.850%
- EQIX entry: fill=$1078.41 current=$1087.61 return=+0.853%
- JNJ entry: fill=$230.116 current=$245.2144 return=+6.561%
- WMT entry: fill=$132.276 current=$116.15 return=-12.191%
- WMT entry: fill=$132.474 current=$116.15 return=-12.322%
- EQIX entry: fill=$1076.89 current=$1087.61 return=+0.996%
- EQIX entry: fill=$1076.82 current=$1087.61 return=+1.002%
- JNJ entry: fill=$230.044 current=$245.2144 return=+6.595%
- EQIX exit: fill=$1076.718 current=$1087.61 return=+1.012%
- EQIX entry: fill=$1076.542 current=$1087.61 return=+1.028%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-25

*From trigger_performance run `trigger_performance-20260625T222132-94b92b2b`*
*Period: 2026-06-19 to 2026-06-25 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 77% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 61/79 symbols blocked (77%). Avg spread (blocked): 11.708%
- Trend gate (200 DMA): 29/79 symbols below 200 DMA (37% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +0.299%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 24 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=4, LIQUIDITY_GATE_V1=4, MOMENTUM_BLEND_6M_12M_V1=4, SPREAD_GATE_V1=4, STOCK_TREND_200DMA_V1=4.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-25T22:48:33Z

*From outcome_tracker run `outcome_tracker-20260625T224833-fd50c6ed`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$223.73 return=+2.250%
- JNJ entry: fill=$230.248 current=$245.2144 return=+6.500%
- EQIX entry: fill=$1084.37 current=$1087.61 return=+0.299%
- EQIX entry: fill=$1079.5 current=$1087.61 return=+0.751%
- EQIX exit: fill=$1078.442 current=$1087.61 return=+0.850%
- EQIX entry: fill=$1078.41 current=$1087.61 return=+0.853%
- JNJ entry: fill=$230.116 current=$245.2144 return=+6.561%
- WMT entry: fill=$132.276 current=$116.15 return=-12.191%
- WMT entry: fill=$132.474 current=$116.15 return=-12.322%
- EQIX entry: fill=$1076.89 current=$1087.61 return=+0.996%
- EQIX entry: fill=$1076.82 current=$1087.61 return=+1.002%
- JNJ entry: fill=$230.044 current=$245.2144 return=+6.595%
- EQIX exit: fill=$1076.718 current=$1087.61 return=+1.012%
- EQIX entry: fill=$1076.542 current=$1087.61 return=+1.028%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-25

*From trigger_performance run `trigger_performance-20260625T225454-6ac49348`*
*Period: 2026-06-19 to 2026-06-25 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 77% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 61/79 symbols blocked (77%). Avg spread (blocked): 11.708%
- Trend gate (200 DMA): 29/79 symbols below 200 DMA (37% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +0.299%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 24 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=4, LIQUIDITY_GATE_V1=4, MOMENTUM_BLEND_6M_12M_V1=4, SPREAD_GATE_V1=4, STOCK_TREND_200DMA_V1=4.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-26T21:51:50Z

*From outcome_tracker run `outcome_tracker-20260626T215150-3b6f9daf`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$227.1 return=+3.790%
- JNJ entry: fill=$230.248 current=$254.2 return=+10.403%
- EQIX entry: fill=$1084.37 current=$1091.3 return=+0.639%
- EQIX entry: fill=$1079.5 current=$1091.3 return=+1.093%
- EQIX exit: fill=$1078.442 current=$1091.3 return=+1.192%
- EQIX entry: fill=$1078.41 current=$1091.3 return=+1.195%
- JNJ entry: fill=$230.116 current=$254.2 return=+10.466%
- WMT entry: fill=$132.276 current=$115.59 return=-12.615%
- WMT entry: fill=$132.474 current=$115.59 return=-12.745%
- EQIX entry: fill=$1076.89 current=$1091.3 return=+1.338%
- EQIX entry: fill=$1076.82 current=$1091.3 return=+1.345%
- JNJ entry: fill=$230.044 current=$254.2 return=+10.501%
- EQIX exit: fill=$1076.718 current=$1091.3 return=+1.354%
- EQIX entry: fill=$1076.542 current=$1091.3 return=+1.371%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-26

*From trigger_performance run `trigger_performance-20260626T215150-3b6f9daf`*
*Period: 2026-06-20 to 2026-06-26 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 65% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 51/79 symbols blocked (65%). Avg spread (blocked): 10.131%
- Trend gate (200 DMA): 30/79 symbols below 200 DMA (38% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +1.381%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 18 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-26T22:13:48Z

*From outcome_tracker run `outcome_tracker-20260626T221348-872e930a`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$227.1 return=+3.790%
- JNJ entry: fill=$230.248 current=$254.2 return=+10.403%
- EQIX entry: fill=$1084.37 current=$1091.3 return=+0.639%
- EQIX entry: fill=$1079.5 current=$1091.3 return=+1.093%
- EQIX exit: fill=$1078.442 current=$1091.3 return=+1.192%
- EQIX entry: fill=$1078.41 current=$1091.3 return=+1.195%
- JNJ entry: fill=$230.116 current=$254.2 return=+10.466%
- WMT entry: fill=$132.276 current=$115.59 return=-12.615%
- WMT entry: fill=$132.474 current=$115.59 return=-12.745%
- EQIX entry: fill=$1076.89 current=$1091.3 return=+1.338%
- EQIX entry: fill=$1076.82 current=$1091.3 return=+1.345%
- JNJ entry: fill=$230.044 current=$254.2 return=+10.501%
- EQIX exit: fill=$1076.718 current=$1091.3 return=+1.354%
- EQIX entry: fill=$1076.542 current=$1091.3 return=+1.371%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-26

*From trigger_performance run `trigger_performance-20260626T221348-872e930a`*
*Period: 2026-06-20 to 2026-06-26 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 65% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 51/79 symbols blocked (65%). Avg spread (blocked): 10.131%
- Trend gate (200 DMA): 30/79 symbols below 200 DMA (38% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +1.381%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 18 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-26T22:37:54Z

*From outcome_tracker run `outcome_tracker-20260626T223754-00b36e95`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$227.1 return=+3.790%
- JNJ entry: fill=$230.248 current=$254.2 return=+10.403%
- EQIX entry: fill=$1084.37 current=$1091.3 return=+0.639%
- EQIX entry: fill=$1079.5 current=$1091.3 return=+1.093%
- EQIX exit: fill=$1078.442 current=$1091.3 return=+1.192%
- EQIX entry: fill=$1078.41 current=$1091.3 return=+1.195%
- JNJ entry: fill=$230.116 current=$254.2 return=+10.466%
- WMT entry: fill=$132.276 current=$115.59 return=-12.615%
- WMT entry: fill=$132.474 current=$115.59 return=-12.745%
- EQIX entry: fill=$1076.89 current=$1091.3 return=+1.338%
- EQIX entry: fill=$1076.82 current=$1091.3 return=+1.345%
- JNJ entry: fill=$230.044 current=$254.2 return=+10.501%
- EQIX exit: fill=$1076.718 current=$1091.3 return=+1.354%
- EQIX entry: fill=$1076.542 current=$1091.3 return=+1.371%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Experiment Candidates — 2026-06-26

*From weekly review run weekly_review-2026-06-26*

**Observations (hypothesis candidates):**
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

**To propose a strategy experiment, open a PR with:**
- Hypothesis
- Supporting evidence (backtest or paper results)
- Success criteria
- Rollback plan

---
## Trigger Performance Observations — 2026-06-26

*From trigger_performance run `trigger_performance-20260626T224417-2b647765`*
*Period: 2026-06-20 to 2026-06-26 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 65% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 51/79 symbols blocked (65%). Avg spread (blocked): 10.131%
- Trend gate (200 DMA): 30/79 symbols below 200 DMA (38% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +1.381%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 18 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-29T21:59:10Z

*From outcome_tracker run `outcome_tracker-20260629T215910-c81f939c`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$227.73 return=+4.077%
- JNJ entry: fill=$230.248 current=$258.39 return=+12.223%
- EQIX entry: fill=$1084.37 current=$1085.17 return=+0.074%
- EQIX entry: fill=$1079.5 current=$1085.17 return=+0.525%
- EQIX exit: fill=$1078.442 current=$1085.17 return=+0.624%
- EQIX entry: fill=$1078.41 current=$1085.17 return=+0.627%
- JNJ entry: fill=$230.116 current=$258.39 return=+12.287%
- WMT entry: fill=$132.276 current=$114.6194 return=-13.348%
- WMT entry: fill=$132.474 current=$114.6194 return=-13.478%
- EQIX entry: fill=$1076.89 current=$1085.17 return=+0.769%
- EQIX entry: fill=$1076.82 current=$1085.17 return=+0.775%
- JNJ entry: fill=$230.044 current=$258.39 return=+12.322%
- EQIX exit: fill=$1076.718 current=$1085.17 return=+0.785%
- EQIX entry: fill=$1076.542 current=$1085.17 return=+0.801%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-29

*From trigger_performance run `trigger_performance-20260629T215910-c81f939c`*
*Period: 2026-06-23 to 2026-06-29 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 75% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 59/79 symbols blocked (75%). Avg spread (blocked): 10.826%
- Trend gate (200 DMA): 32/79 symbols below 200 DMA (41% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +1.362%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 54 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=9, LIQUIDITY_GATE_V1=9, MOMENTUM_BLEND_6M_12M_V1=9, SPREAD_GATE_V1=9, STOCK_TREND_200DMA_V1=9.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-29T22:08:16Z

*From outcome_tracker run `outcome_tracker-20260629T220816-bf6c69fc`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$227.73 return=+4.077%
- JNJ entry: fill=$230.248 current=$258.39 return=+12.223%
- EQIX entry: fill=$1084.37 current=$1085.17 return=+0.074%
- EQIX entry: fill=$1079.5 current=$1085.17 return=+0.525%
- EQIX exit: fill=$1078.442 current=$1085.17 return=+0.624%
- EQIX entry: fill=$1078.41 current=$1085.17 return=+0.627%
- JNJ entry: fill=$230.116 current=$258.39 return=+12.287%
- WMT entry: fill=$132.276 current=$114.6194 return=-13.348%
- WMT entry: fill=$132.474 current=$114.6194 return=-13.478%
- EQIX entry: fill=$1076.89 current=$1085.17 return=+0.769%
- EQIX entry: fill=$1076.82 current=$1085.17 return=+0.775%
- JNJ entry: fill=$230.044 current=$258.39 return=+12.322%
- EQIX exit: fill=$1076.718 current=$1085.17 return=+0.785%
- EQIX entry: fill=$1076.542 current=$1085.17 return=+0.801%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-29

*From trigger_performance run `trigger_performance-20260629T220816-bf6c69fc`*
*Period: 2026-06-23 to 2026-06-29 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 75% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 59/79 symbols blocked (75%). Avg spread (blocked): 10.826%
- Trend gate (200 DMA): 32/79 symbols below 200 DMA (41% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +1.362%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 54 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=9, LIQUIDITY_GATE_V1=9, MOMENTUM_BLEND_6M_12M_V1=9, SPREAD_GATE_V1=9, STOCK_TREND_200DMA_V1=9.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-29T22:33:04Z

*From outcome_tracker run `outcome_tracker-20260629T223304-f36c3261`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$227.73 return=+4.077%
- JNJ entry: fill=$230.248 current=$258.39 return=+12.223%
- EQIX entry: fill=$1084.37 current=$1085.17 return=+0.074%
- EQIX entry: fill=$1079.5 current=$1085.17 return=+0.525%
- EQIX exit: fill=$1078.442 current=$1085.17 return=+0.624%
- EQIX entry: fill=$1078.41 current=$1085.17 return=+0.627%
- JNJ entry: fill=$230.116 current=$258.39 return=+12.287%
- WMT entry: fill=$132.276 current=$114.6194 return=-13.348%
- WMT entry: fill=$132.474 current=$114.6194 return=-13.478%
- EQIX entry: fill=$1076.89 current=$1085.17 return=+0.769%
- EQIX entry: fill=$1076.82 current=$1085.17 return=+0.775%
- JNJ entry: fill=$230.044 current=$258.39 return=+12.322%
- EQIX exit: fill=$1076.718 current=$1085.17 return=+0.785%
- EQIX entry: fill=$1076.542 current=$1085.17 return=+0.801%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-29

*From trigger_performance run `trigger_performance-20260629T223615-f5b78483`*
*Period: 2026-06-23 to 2026-06-29 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 75% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 59/79 symbols blocked (75%). Avg spread (blocked): 10.826%
- Trend gate (200 DMA): 32/79 symbols below 200 DMA (41% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): +1.362%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 54 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=9, LIQUIDITY_GATE_V1=9, MOMENTUM_BLEND_6M_12M_V1=9, SPREAD_GATE_V1=9, STOCK_TREND_200DMA_V1=9.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-30T22:03:50Z

*From outcome_tracker run `outcome_tracker-20260630T220350-928c3264`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$226.97 return=+3.730%
- JNJ entry: fill=$230.248 current=$255.01 return=+10.755%
- EQIX entry: fill=$1084.37 current=$1042.0 return=-3.907%
- EQIX entry: fill=$1079.5 current=$1042.0 return=-3.474%
- EQIX exit: fill=$1078.442 current=$1042.0 return=-3.379%
- EQIX entry: fill=$1078.41 current=$1042.0 return=-3.376%
- JNJ entry: fill=$230.116 current=$255.01 return=+10.818%
- WMT entry: fill=$132.276 current=$113.3522 return=-14.306%
- WMT entry: fill=$132.474 current=$113.3522 return=-14.434%
- EQIX entry: fill=$1076.89 current=$1042.0 return=-3.240%
- EQIX entry: fill=$1076.82 current=$1042.0 return=-3.234%
- JNJ entry: fill=$230.044 current=$255.01 return=+10.853%
- EQIX exit: fill=$1076.718 current=$1042.0 return=-3.224%
- EQIX entry: fill=$1076.542 current=$1042.0 return=-3.209%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-30

*From trigger_performance run `trigger_performance-20260630T220350-928c3264`*
*Period: 2026-06-24 to 2026-06-30 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.520%
- Trend gate (200 DMA): 31/79 symbols below 200 DMA (39% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.402%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 66 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-30T22:14:58Z

*From outcome_tracker run `outcome_tracker-20260630T221458-c5d27657`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$226.97 return=+3.730%
- JNJ entry: fill=$230.248 current=$255.01 return=+10.755%
- EQIX entry: fill=$1084.37 current=$1042.0 return=-3.907%
- EQIX entry: fill=$1079.5 current=$1042.0 return=-3.474%
- EQIX exit: fill=$1078.442 current=$1042.0 return=-3.379%
- EQIX entry: fill=$1078.41 current=$1042.0 return=-3.376%
- JNJ entry: fill=$230.116 current=$255.01 return=+10.818%
- WMT entry: fill=$132.276 current=$113.3522 return=-14.306%
- WMT entry: fill=$132.474 current=$113.3522 return=-14.434%
- EQIX entry: fill=$1076.89 current=$1042.0 return=-3.240%
- EQIX entry: fill=$1076.82 current=$1042.0 return=-3.234%
- JNJ entry: fill=$230.044 current=$255.01 return=+10.853%
- EQIX exit: fill=$1076.718 current=$1042.0 return=-3.224%
- EQIX entry: fill=$1076.542 current=$1042.0 return=-3.209%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-30

*From trigger_performance run `trigger_performance-20260630T221459-5f50cbbd`*
*Period: 2026-06-24 to 2026-06-30 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.520%
- Trend gate (200 DMA): 31/79 symbols below 200 DMA (39% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.402%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 66 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-06-30T22:41:58Z

*From outcome_tracker run `outcome_tracker-20260630T224158-62047898`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$226.97 return=+3.730%
- JNJ entry: fill=$230.248 current=$255.01 return=+10.755%
- EQIX entry: fill=$1084.37 current=$1042.0 return=-3.907%
- EQIX entry: fill=$1079.5 current=$1042.0 return=-3.474%
- EQIX exit: fill=$1078.442 current=$1042.0 return=-3.379%
- EQIX entry: fill=$1078.41 current=$1042.0 return=-3.376%
- JNJ entry: fill=$230.116 current=$255.01 return=+10.818%
- WMT entry: fill=$132.276 current=$113.3522 return=-14.306%
- WMT entry: fill=$132.474 current=$113.3522 return=-14.434%
- EQIX entry: fill=$1076.89 current=$1042.0 return=-3.240%
- EQIX entry: fill=$1076.82 current=$1042.0 return=-3.234%
- JNJ entry: fill=$230.044 current=$255.01 return=+10.853%
- EQIX exit: fill=$1076.718 current=$1042.0 return=-3.224%
- EQIX entry: fill=$1076.542 current=$1042.0 return=-3.209%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-06-30

*From trigger_performance run `trigger_performance-20260630T224925-c2a29580`*
*Period: 2026-06-24 to 2026-06-30 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 67% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 53/79 symbols blocked (67%). Avg spread (blocked): 10.520%
- Trend gate (200 DMA): 31/79 symbols below 200 DMA (39% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.402%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 66 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=11, LIQUIDITY_GATE_V1=11, MOMENTUM_BLEND_6M_12M_V1=11, SPREAD_GATE_V1=11, STOCK_TREND_200DMA_V1=11.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-01T22:07:39Z

*From outcome_tracker run `outcome_tracker-20260701T220739-458befa0`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$230.19 return=+5.202%
- JNJ entry: fill=$230.248 current=$252.8594 return=+9.821%
- EQIX entry: fill=$1084.37 current=$1013.62 return=-6.524%
- EQIX entry: fill=$1079.5 current=$1013.62 return=-6.103%
- EQIX exit: fill=$1078.442 current=$1013.62 return=-6.011%
- EQIX entry: fill=$1078.41 current=$1013.62 return=-6.008%
- JNJ entry: fill=$230.116 current=$252.8594 return=+9.884%
- WMT entry: fill=$132.276 current=$108.38 return=-18.065%
- WMT entry: fill=$132.474 current=$108.38 return=-18.188%
- EQIX entry: fill=$1076.89 current=$1013.62 return=-5.875%
- EQIX entry: fill=$1076.82 current=$1013.62 return=-5.869%
- JNJ entry: fill=$230.044 current=$252.8594 return=+9.918%
- EQIX exit: fill=$1076.718 current=$1013.62 return=-5.860%
- EQIX entry: fill=$1076.542 current=$1013.62 return=-5.845%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-01

*From trigger_performance run `trigger_performance-20260701T220739-458befa0`*
*Period: 2026-06-25 to 2026-07-01 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 57% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 45/79 symbols blocked (57%). Avg spread (blocked): 10.434%
- Trend gate (200 DMA): 31/79 symbols below 200 DMA (39% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -3.537%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 18 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-01T22:17:27Z

*From outcome_tracker run `outcome_tracker-20260701T221727-da4d2d53`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$230.19 return=+5.202%
- JNJ entry: fill=$230.248 current=$252.8594 return=+9.821%
- EQIX entry: fill=$1084.37 current=$1013.62 return=-6.524%
- EQIX entry: fill=$1079.5 current=$1013.62 return=-6.103%
- EQIX exit: fill=$1078.442 current=$1013.62 return=-6.011%
- EQIX entry: fill=$1078.41 current=$1013.62 return=-6.008%
- JNJ entry: fill=$230.116 current=$252.8594 return=+9.884%
- WMT entry: fill=$132.276 current=$108.38 return=-18.065%
- WMT entry: fill=$132.474 current=$108.38 return=-18.188%
- EQIX entry: fill=$1076.89 current=$1013.62 return=-5.875%
- EQIX entry: fill=$1076.82 current=$1013.62 return=-5.869%
- JNJ entry: fill=$230.044 current=$252.8594 return=+9.918%
- EQIX exit: fill=$1076.718 current=$1013.62 return=-5.860%
- EQIX entry: fill=$1076.542 current=$1013.62 return=-5.845%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-01

*From trigger_performance run `trigger_performance-20260701T221727-da4d2d53`*
*Period: 2026-06-25 to 2026-07-01 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 57% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 45/79 symbols blocked (57%). Avg spread (blocked): 10.434%
- Trend gate (200 DMA): 31/79 symbols below 200 DMA (39% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -3.537%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 18 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-01T22:41:47Z

*From outcome_tracker run `outcome_tracker-20260701T224147-ee0ce994`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$230.19 return=+5.202%
- JNJ entry: fill=$230.248 current=$252.8594 return=+9.821%
- EQIX entry: fill=$1084.37 current=$1013.62 return=-6.524%
- EQIX entry: fill=$1079.5 current=$1013.62 return=-6.103%
- EQIX exit: fill=$1078.442 current=$1013.62 return=-6.011%
- EQIX entry: fill=$1078.41 current=$1013.62 return=-6.008%
- JNJ entry: fill=$230.116 current=$252.8594 return=+9.884%
- WMT entry: fill=$132.276 current=$108.38 return=-18.065%
- WMT entry: fill=$132.474 current=$108.38 return=-18.188%
- EQIX entry: fill=$1076.89 current=$1013.62 return=-5.875%
- EQIX entry: fill=$1076.82 current=$1013.62 return=-5.869%
- JNJ entry: fill=$230.044 current=$252.8594 return=+9.918%
- EQIX exit: fill=$1076.718 current=$1013.62 return=-5.860%
- EQIX entry: fill=$1076.542 current=$1013.62 return=-5.845%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-01

*From trigger_performance run `trigger_performance-20260701T224620-ff720760`*
*Period: 2026-06-25 to 2026-07-01 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 57% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 45/79 symbols blocked (57%). Avg spread (blocked): 10.434%
- Trend gate (200 DMA): 31/79 symbols below 200 DMA (39% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -3.537%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 18 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=3, LIQUIDITY_GATE_V1=3, MOMENTUM_BLEND_6M_12M_V1=3, SPREAD_GATE_V1=3, STOCK_TREND_200DMA_V1=3.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-02T21:49:02Z

*From outcome_tracker run `outcome_tracker-20260702T214902-4626a3b9`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$236.06 return=+7.885%
- JNJ entry: fill=$230.248 current=$261.9 return=+13.747%
- EQIX entry: fill=$1084.37 current=$1002.02 return=-7.594%
- EQIX entry: fill=$1079.5 current=$1002.02 return=-7.177%
- EQIX exit: fill=$1078.442 current=$1002.02 return=-7.086%
- EQIX entry: fill=$1078.41 current=$1002.02 return=-7.084%
- JNJ entry: fill=$230.116 current=$261.9 return=+13.812%
- WMT entry: fill=$132.276 current=$111.65 return=-15.593%
- WMT entry: fill=$132.474 current=$111.65 return=-15.719%
- EQIX entry: fill=$1076.89 current=$1002.02 return=-6.952%
- EQIX entry: fill=$1076.82 current=$1002.02 return=-6.946%
- JNJ entry: fill=$230.044 current=$261.9 return=+13.848%
- EQIX exit: fill=$1076.718 current=$1002.02 return=-6.938%
- EQIX entry: fill=$1076.542 current=$1002.02 return=-6.922%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-02

*From trigger_performance run `trigger_performance-20260702T214902-4626a3b9`*
*Period: 2026-06-26 to 2026-07-02 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 10.937%
- Trend gate (200 DMA): 27/79 symbols below 200 DMA (34% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.766%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 54 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=9, LIQUIDITY_GATE_V1=9, MOMENTUM_BLEND_6M_12M_V1=9, SPREAD_GATE_V1=9, STOCK_TREND_200DMA_V1=9.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-02T22:06:06Z

*From outcome_tracker run `outcome_tracker-20260702T220606-d5127cc4`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$236.06 return=+7.885%
- JNJ entry: fill=$230.248 current=$261.9 return=+13.747%
- EQIX entry: fill=$1084.37 current=$1002.02 return=-7.594%
- EQIX entry: fill=$1079.5 current=$1002.02 return=-7.177%
- EQIX exit: fill=$1078.442 current=$1002.02 return=-7.086%
- EQIX entry: fill=$1078.41 current=$1002.02 return=-7.084%
- JNJ entry: fill=$230.116 current=$261.9 return=+13.812%
- WMT entry: fill=$132.276 current=$111.65 return=-15.593%
- WMT entry: fill=$132.474 current=$111.65 return=-15.719%
- EQIX entry: fill=$1076.89 current=$1002.02 return=-6.952%
- EQIX entry: fill=$1076.82 current=$1002.02 return=-6.946%
- JNJ entry: fill=$230.044 current=$261.9 return=+13.848%
- EQIX exit: fill=$1076.718 current=$1002.02 return=-6.938%
- EQIX entry: fill=$1076.542 current=$1002.02 return=-6.922%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-02

*From trigger_performance run `trigger_performance-20260702T220606-d5127cc4`*
*Period: 2026-06-26 to 2026-07-02 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 10.937%
- Trend gate (200 DMA): 27/79 symbols below 200 DMA (34% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.766%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 54 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=9, LIQUIDITY_GATE_V1=9, MOMENTUM_BLEND_6M_12M_V1=9, SPREAD_GATE_V1=9, STOCK_TREND_200DMA_V1=9.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-02T22:28:46Z

*From outcome_tracker run `outcome_tracker-20260702T222846-9487ed18`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$236.06 return=+7.885%
- JNJ entry: fill=$230.248 current=$261.9 return=+13.747%
- EQIX entry: fill=$1084.37 current=$1002.02 return=-7.594%
- EQIX entry: fill=$1079.5 current=$1002.02 return=-7.177%
- EQIX exit: fill=$1078.442 current=$1002.02 return=-7.086%
- EQIX entry: fill=$1078.41 current=$1002.02 return=-7.084%
- JNJ entry: fill=$230.116 current=$261.9 return=+13.812%
- WMT entry: fill=$132.276 current=$111.65 return=-15.593%
- WMT entry: fill=$132.474 current=$111.65 return=-15.719%
- EQIX entry: fill=$1076.89 current=$1002.02 return=-6.952%
- EQIX entry: fill=$1076.82 current=$1002.02 return=-6.946%
- JNJ entry: fill=$230.044 current=$261.9 return=+13.848%
- EQIX exit: fill=$1076.718 current=$1002.02 return=-6.938%
- EQIX entry: fill=$1076.542 current=$1002.02 return=-6.922%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-02

*From trigger_performance run `trigger_performance-20260702T223614-7508a297`*
*Period: 2026-06-26 to 2026-07-02 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 10.937%
- Trend gate (200 DMA): 27/79 symbols below 200 DMA (34% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.766%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 54 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=9, LIQUIDITY_GATE_V1=9, MOMENTUM_BLEND_6M_12M_V1=9, SPREAD_GATE_V1=9, STOCK_TREND_200DMA_V1=9.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-03T21:44:37Z

*From outcome_tracker run `outcome_tracker-20260703T214437-af0b552b`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$236.06 return=+7.885%
- JNJ entry: fill=$230.248 current=$263.04 return=+14.242%
- EQIX entry: fill=$1084.37 current=$1002.02 return=-7.594%
- EQIX entry: fill=$1079.5 current=$1002.02 return=-7.177%
- EQIX exit: fill=$1078.442 current=$1002.02 return=-7.086%
- EQIX entry: fill=$1078.41 current=$1002.02 return=-7.084%
- JNJ entry: fill=$230.116 current=$263.04 return=+14.308%
- WMT entry: fill=$132.276 current=$111.84 return=-15.449%
- WMT entry: fill=$132.474 current=$111.84 return=-15.576%
- EQIX entry: fill=$1076.89 current=$1002.02 return=-6.952%
- EQIX entry: fill=$1076.82 current=$1002.02 return=-6.946%
- JNJ entry: fill=$230.044 current=$263.04 return=+14.343%
- EQIX exit: fill=$1076.718 current=$1002.02 return=-6.938%
- EQIX entry: fill=$1076.542 current=$1002.02 return=-6.922%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-03

*From trigger_performance run `trigger_performance-20260703T214438-a9c85e14`*
*Period: 2026-06-27 to 2026-07-03 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 10.937%
- Trend gate (200 DMA): 27/79 symbols below 200 DMA (34% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.639%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 54 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=9, LIQUIDITY_GATE_V1=9, MOMENTUM_BLEND_6M_12M_V1=9, SPREAD_GATE_V1=9, STOCK_TREND_200DMA_V1=9.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-03T22:04:07Z

*From outcome_tracker run `outcome_tracker-20260703T220407-e69ef453`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$236.06 return=+7.885%
- JNJ entry: fill=$230.248 current=$263.04 return=+14.242%
- EQIX entry: fill=$1084.37 current=$1002.02 return=-7.594%
- EQIX entry: fill=$1079.5 current=$1002.02 return=-7.177%
- EQIX exit: fill=$1078.442 current=$1002.02 return=-7.086%
- EQIX entry: fill=$1078.41 current=$1002.02 return=-7.084%
- JNJ entry: fill=$230.116 current=$263.04 return=+14.308%
- WMT entry: fill=$132.276 current=$111.84 return=-15.449%
- WMT entry: fill=$132.474 current=$111.84 return=-15.576%
- EQIX entry: fill=$1076.89 current=$1002.02 return=-6.952%
- EQIX entry: fill=$1076.82 current=$1002.02 return=-6.946%
- JNJ entry: fill=$230.044 current=$263.04 return=+14.343%
- EQIX exit: fill=$1076.718 current=$1002.02 return=-6.938%
- EQIX entry: fill=$1076.542 current=$1002.02 return=-6.922%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-03

*From trigger_performance run `trigger_performance-20260703T220407-e69ef453`*
*Period: 2026-06-27 to 2026-07-03 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 66% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 52/79 symbols blocked (66%). Avg spread (blocked): 10.937%
- Trend gate (200 DMA): 27/79 symbols below 200 DMA (34% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -2.639%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 54 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=9, LIQUIDITY_GATE_V1=9, MOMENTUM_BLEND_6M_12M_V1=9, SPREAD_GATE_V1=9, STOCK_TREND_200DMA_V1=9.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-03T22:17:22Z

*From outcome_tracker run `outcome_tracker-20260703T221722-6d77758a`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$236.06 return=+7.885%
- JNJ entry: fill=$230.248 current=$263.04 return=+14.242%
- EQIX entry: fill=$1084.37 current=$1002.02 return=-7.594%
- EQIX entry: fill=$1079.5 current=$1002.02 return=-7.177%
- EQIX exit: fill=$1078.442 current=$1002.02 return=-7.086%
- EQIX entry: fill=$1078.41 current=$1002.02 return=-7.084%
- JNJ entry: fill=$230.116 current=$263.04 return=+14.308%
- WMT entry: fill=$132.276 current=$111.84 return=-15.449%
- WMT entry: fill=$132.474 current=$111.84 return=-15.576%
- EQIX entry: fill=$1076.89 current=$1002.02 return=-6.952%
- EQIX entry: fill=$1076.82 current=$1002.02 return=-6.946%
- JNJ entry: fill=$230.044 current=$263.04 return=+14.343%
- EQIX exit: fill=$1076.718 current=$1002.02 return=-6.938%
- EQIX entry: fill=$1076.542 current=$1002.02 return=-6.922%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Experiment Candidates — 2026-07-03

*From weekly review run weekly_review-2026-07-03*

**Observations (hypothesis candidates):**
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

**To propose a strategy experiment, open a PR with:**
- Hypothesis
- Supporting evidence (backtest or paper results)
- Success criteria
- Rollback plan

---
## Outcome Observations — 2026-07-06T22:02:54Z

*From outcome_tracker run `outcome_tracker-20260706T220254-62231326`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$232.69 return=+6.344%
- JNJ entry: fill=$230.248 current=$259.0 return=+12.487%
- EQIX entry: fill=$1084.37 current=$998.84 return=-7.888%
- EQIX entry: fill=$1079.5 current=$998.84 return=-7.472%
- EQIX exit: fill=$1078.442 current=$998.84 return=-7.381%
- EQIX entry: fill=$1078.41 current=$998.84 return=-7.379%
- JNJ entry: fill=$230.116 current=$259.0 return=+12.552%
- WMT entry: fill=$132.276 current=$110.53 return=-16.440%
- WMT entry: fill=$132.474 current=$110.53 return=-16.565%
- EQIX entry: fill=$1076.89 current=$998.84 return=-7.248%
- EQIX entry: fill=$1076.82 current=$998.84 return=-7.242%
- JNJ entry: fill=$230.044 current=$259.0 return=+12.587%
- EQIX exit: fill=$1076.718 current=$998.84 return=-7.233%
- EQIX entry: fill=$1076.542 current=$998.84 return=-7.218%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-06

*From trigger_performance run `trigger_performance-20260706T220254-62231326`*
*Period: 2026-06-30 to 2026-07-06 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 75% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 59/79 symbols blocked (75%). Avg spread (blocked): 11.182%
- Trend gate (200 DMA): 26/79 symbols below 200 DMA (33% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -3.435%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-06T22:13:26Z

*From outcome_tracker run `outcome_tracker-20260706T221326-18bf20c1`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$232.69 return=+6.344%
- JNJ entry: fill=$230.248 current=$259.0 return=+12.487%
- EQIX entry: fill=$1084.37 current=$998.84 return=-7.888%
- EQIX entry: fill=$1079.5 current=$998.84 return=-7.472%
- EQIX exit: fill=$1078.442 current=$998.84 return=-7.381%
- EQIX entry: fill=$1078.41 current=$998.84 return=-7.379%
- JNJ entry: fill=$230.116 current=$259.0 return=+12.552%
- WMT entry: fill=$132.276 current=$110.53 return=-16.440%
- WMT entry: fill=$132.474 current=$110.53 return=-16.565%
- EQIX entry: fill=$1076.89 current=$998.84 return=-7.248%
- EQIX entry: fill=$1076.82 current=$998.84 return=-7.242%
- JNJ entry: fill=$230.044 current=$259.0 return=+12.587%
- EQIX exit: fill=$1076.718 current=$998.84 return=-7.233%
- EQIX entry: fill=$1076.542 current=$998.84 return=-7.218%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-06

*From trigger_performance run `trigger_performance-20260706T221326-18bf20c1`*
*Period: 2026-06-30 to 2026-07-06 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 75% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 59/79 symbols blocked (75%). Avg spread (blocked): 11.182%
- Trend gate (200 DMA): 26/79 symbols below 200 DMA (33% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -3.435%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-06T22:40:17Z

*From outcome_tracker run `outcome_tracker-20260706T224017-6bc5f17b`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$232.69 return=+6.344%
- JNJ entry: fill=$230.248 current=$259.0 return=+12.487%
- EQIX entry: fill=$1084.37 current=$998.84 return=-7.888%
- EQIX entry: fill=$1079.5 current=$998.84 return=-7.472%
- EQIX exit: fill=$1078.442 current=$998.84 return=-7.381%
- EQIX entry: fill=$1078.41 current=$998.84 return=-7.379%
- JNJ entry: fill=$230.116 current=$259.0 return=+12.552%
- WMT entry: fill=$132.276 current=$110.53 return=-16.440%
- WMT entry: fill=$132.474 current=$110.53 return=-16.565%
- EQIX entry: fill=$1076.89 current=$998.84 return=-7.248%
- EQIX entry: fill=$1076.82 current=$998.84 return=-7.242%
- JNJ entry: fill=$230.044 current=$259.0 return=+12.587%
- EQIX exit: fill=$1076.718 current=$998.84 return=-7.233%
- EQIX entry: fill=$1076.542 current=$998.84 return=-7.218%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-06

*From trigger_performance run `trigger_performance-20260706T224536-01581f39`*
*Period: 2026-06-30 to 2026-07-06 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 75% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 59/79 symbols blocked (75%). Avg spread (blocked): 11.182%
- Trend gate (200 DMA): 26/79 symbols below 200 DMA (33% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -3.435%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 0 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- No fills linked to triggers via lineage — run build_lineage.py to recover trigger provenance.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-07T22:00:14Z

*From outcome_tracker run `outcome_tracker-20260707T220014-e61b1e68`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$237.63 return=+8.602%
- JNJ entry: fill=$230.248 current=$267.5 return=+16.179%
- EQIX entry: fill=$1084.37 current=$1022.93 return=-5.666%
- EQIX entry: fill=$1079.5 current=$1022.93 return=-5.240%
- EQIX exit: fill=$1078.442 current=$1022.93 return=-5.147%
- EQIX entry: fill=$1078.41 current=$1022.93 return=-5.145%
- JNJ entry: fill=$230.116 current=$267.5 return=+16.246%
- WMT entry: fill=$132.276 current=$111.59 return=-15.639%
- WMT entry: fill=$132.474 current=$111.59 return=-15.765%
- EQIX entry: fill=$1076.89 current=$1022.93 return=-5.011%
- EQIX entry: fill=$1076.82 current=$1022.93 return=-5.005%
- JNJ entry: fill=$230.044 current=$267.5 return=+16.282%
- EQIX exit: fill=$1076.718 current=$1022.93 return=-4.996%
- EQIX entry: fill=$1076.542 current=$1022.93 return=-4.980%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-07

*From trigger_performance run `trigger_performance-20260707T220015-d0b2572a`*
*Period: 2026-07-01 to 2026-07-07 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 11.056%
- Trend gate (200 DMA): 25/79 symbols below 200 DMA (32% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.092%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 24 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=4, LIQUIDITY_GATE_V1=4, MOMENTUM_BLEND_6M_12M_V1=4, SPREAD_GATE_V1=4, STOCK_TREND_200DMA_V1=4.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-07T22:10:51Z

*From outcome_tracker run `outcome_tracker-20260707T221051-ec2c222f`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$237.63 return=+8.602%
- JNJ entry: fill=$230.248 current=$267.5 return=+16.179%
- EQIX entry: fill=$1084.37 current=$1022.93 return=-5.666%
- EQIX entry: fill=$1079.5 current=$1022.93 return=-5.240%
- EQIX exit: fill=$1078.442 current=$1022.93 return=-5.147%
- EQIX entry: fill=$1078.41 current=$1022.93 return=-5.145%
- JNJ entry: fill=$230.116 current=$267.5 return=+16.246%
- WMT entry: fill=$132.276 current=$111.59 return=-15.639%
- WMT entry: fill=$132.474 current=$111.59 return=-15.765%
- EQIX entry: fill=$1076.89 current=$1022.93 return=-5.011%
- EQIX entry: fill=$1076.82 current=$1022.93 return=-5.005%
- JNJ entry: fill=$230.044 current=$267.5 return=+16.282%
- EQIX exit: fill=$1076.718 current=$1022.93 return=-4.996%
- EQIX entry: fill=$1076.542 current=$1022.93 return=-4.980%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-07

*From trigger_performance run `trigger_performance-20260707T221051-ec2c222f`*
*Period: 2026-07-01 to 2026-07-07 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 11.056%
- Trend gate (200 DMA): 25/79 symbols below 200 DMA (32% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.092%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 24 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=4, LIQUIDITY_GATE_V1=4, MOMENTUM_BLEND_6M_12M_V1=4, SPREAD_GATE_V1=4, STOCK_TREND_200DMA_V1=4.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-07T22:32:46Z

*From outcome_tracker run `outcome_tracker-20260707T223246-413f640e`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$237.63 return=+8.602%
- JNJ entry: fill=$230.248 current=$267.5 return=+16.179%
- EQIX entry: fill=$1084.37 current=$1022.93 return=-5.666%
- EQIX entry: fill=$1079.5 current=$1022.93 return=-5.240%
- EQIX exit: fill=$1078.442 current=$1022.93 return=-5.147%
- EQIX entry: fill=$1078.41 current=$1022.93 return=-5.145%
- JNJ entry: fill=$230.116 current=$267.5 return=+16.246%
- WMT entry: fill=$132.276 current=$111.59 return=-15.639%
- WMT entry: fill=$132.474 current=$111.59 return=-15.765%
- EQIX entry: fill=$1076.89 current=$1022.93 return=-5.011%
- EQIX entry: fill=$1076.82 current=$1022.93 return=-5.005%
- JNJ entry: fill=$230.044 current=$267.5 return=+16.282%
- EQIX exit: fill=$1076.718 current=$1022.93 return=-4.996%
- EQIX entry: fill=$1076.542 current=$1022.93 return=-4.980%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-07

*From trigger_performance run `trigger_performance-20260707T223640-326f065e`*
*Period: 2026-07-01 to 2026-07-07 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 62% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 49/79 symbols blocked (62%). Avg spread (blocked): 11.056%
- Trend gate (200 DMA): 25/79 symbols below 200 DMA (32% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.092%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 24 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=4, LIQUIDITY_GATE_V1=4, MOMENTUM_BLEND_6M_12M_V1=4, SPREAD_GATE_V1=4, STOCK_TREND_200DMA_V1=4.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-08T21:47:45Z

*From outcome_tracker run `outcome_tracker-20260708T214745-6bc8a133`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$233.9 return=+6.897%
- JNJ entry: fill=$230.248 current=$263.35 return=+14.377%
- EQIX entry: fill=$1084.37 current=$1016.54 return=-6.255%
- EQIX entry: fill=$1079.5 current=$1016.54 return=-5.832%
- EQIX exit: fill=$1078.442 current=$1016.54 return=-5.740%
- EQIX entry: fill=$1078.41 current=$1016.54 return=-5.737%
- JNJ entry: fill=$230.116 current=$263.35 return=+14.442%
- WMT entry: fill=$132.276 current=$112.9999 return=-14.573%
- WMT entry: fill=$132.474 current=$112.9999 return=-14.700%
- EQIX entry: fill=$1076.89 current=$1016.54 return=-5.604%
- EQIX entry: fill=$1076.82 current=$1016.54 return=-5.598%
- JNJ entry: fill=$230.044 current=$263.35 return=+14.478%
- EQIX exit: fill=$1076.718 current=$1016.54 return=-5.589%
- EQIX entry: fill=$1076.542 current=$1016.54 return=-5.574%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-08

*From trigger_performance run `trigger_performance-20260708T214746-d5fdc5e7`*
*Period: 2026-07-02 to 2026-07-08 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 84% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 66/79 symbols blocked (84%). Avg spread (blocked): 10.152%
- Trend gate (200 DMA): 29/79 symbols below 200 DMA (37% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.786%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 48 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=8, LIQUIDITY_GATE_V1=8, MOMENTUM_BLEND_6M_12M_V1=8, SPREAD_GATE_V1=8, STOCK_TREND_200DMA_V1=8.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-08T22:06:06Z

*From outcome_tracker run `outcome_tracker-20260708T220606-0817b182`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$233.9 return=+6.897%
- JNJ entry: fill=$230.248 current=$263.35 return=+14.377%
- EQIX entry: fill=$1084.37 current=$1016.54 return=-6.255%
- EQIX entry: fill=$1079.5 current=$1016.54 return=-5.832%
- EQIX exit: fill=$1078.442 current=$1016.54 return=-5.740%
- EQIX entry: fill=$1078.41 current=$1016.54 return=-5.737%
- JNJ entry: fill=$230.116 current=$263.35 return=+14.442%
- WMT entry: fill=$132.276 current=$112.9999 return=-14.573%
- WMT entry: fill=$132.474 current=$112.9999 return=-14.700%
- EQIX entry: fill=$1076.89 current=$1016.54 return=-5.604%
- EQIX entry: fill=$1076.82 current=$1016.54 return=-5.598%
- JNJ entry: fill=$230.044 current=$263.35 return=+14.478%
- EQIX exit: fill=$1076.718 current=$1016.54 return=-5.589%
- EQIX entry: fill=$1076.542 current=$1016.54 return=-5.574%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-08

*From trigger_performance run `trigger_performance-20260708T220606-0817b182`*
*Period: 2026-07-02 to 2026-07-08 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 84% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 66/79 symbols blocked (84%). Avg spread (blocked): 10.152%
- Trend gate (200 DMA): 29/79 symbols below 200 DMA (37% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.786%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 48 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=8, LIQUIDITY_GATE_V1=8, MOMENTUM_BLEND_6M_12M_V1=8, SPREAD_GATE_V1=8, STOCK_TREND_200DMA_V1=8.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-08T22:17:55Z

*From outcome_tracker run `outcome_tracker-20260708T221755-5fc507f4`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$233.9 return=+6.897%
- JNJ entry: fill=$230.248 current=$263.35 return=+14.377%
- EQIX entry: fill=$1084.37 current=$1016.54 return=-6.255%
- EQIX entry: fill=$1079.5 current=$1016.54 return=-5.832%
- EQIX exit: fill=$1078.442 current=$1016.54 return=-5.740%
- EQIX entry: fill=$1078.41 current=$1016.54 return=-5.737%
- JNJ entry: fill=$230.116 current=$263.35 return=+14.442%
- WMT entry: fill=$132.276 current=$112.9999 return=-14.573%
- WMT entry: fill=$132.474 current=$112.9999 return=-14.700%
- EQIX entry: fill=$1076.89 current=$1016.54 return=-5.604%
- EQIX entry: fill=$1076.82 current=$1016.54 return=-5.598%
- JNJ entry: fill=$230.044 current=$263.35 return=+14.478%
- EQIX exit: fill=$1076.718 current=$1016.54 return=-5.589%
- EQIX entry: fill=$1076.542 current=$1016.54 return=-5.574%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-08

*From trigger_performance run `trigger_performance-20260708T223212-eab094cb`*
*Period: 2026-07-02 to 2026-07-08 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 84% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 66/79 symbols blocked (84%). Avg spread (blocked): 10.152%
- Trend gate (200 DMA): 29/79 symbols below 200 DMA (37% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.786%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 48 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=8, LIQUIDITY_GATE_V1=8, MOMENTUM_BLEND_6M_12M_V1=8, SPREAD_GATE_V1=8, STOCK_TREND_200DMA_V1=8.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-09T22:07:39Z

*From outcome_tracker run `outcome_tracker-20260709T220739-1eecf04b`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$232.12 return=+6.084%
- JNJ entry: fill=$230.248 current=$258.87 return=+12.431%
- EQIX entry: fill=$1084.37 current=$1034.87 return=-4.565%
- EQIX entry: fill=$1079.5 current=$1034.87 return=-4.134%
- EQIX exit: fill=$1078.442 current=$1034.87 return=-4.040%
- EQIX entry: fill=$1078.41 current=$1034.87 return=-4.037%
- JNJ entry: fill=$230.116 current=$258.87 return=+12.495%
- WMT entry: fill=$132.276 current=$111.57 return=-15.654%
- WMT entry: fill=$132.474 current=$111.57 return=-15.780%
- EQIX entry: fill=$1076.89 current=$1034.87 return=-3.902%
- EQIX entry: fill=$1076.82 current=$1034.87 return=-3.896%
- JNJ entry: fill=$230.044 current=$258.87 return=+12.531%
- EQIX exit: fill=$1076.718 current=$1034.87 return=-3.887%
- EQIX entry: fill=$1076.542 current=$1034.87 return=-3.871%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-09

*From trigger_performance run `trigger_performance-20260709T220739-1eecf04b`*
*Period: 2026-07-03 to 2026-07-09 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 65% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Regime: 1 session(s) scanned, 1 risk-on (100%).
- Spread gate: 51/79 symbols blocked (65%). Avg spread (blocked): 11.186%
- Trend gate (200 DMA): 29/79 symbols below 200 DMA (37% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.445%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 48 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=8, LIQUIDITY_GATE_V1=8, MOMENTUM_BLEND_6M_12M_V1=8, SPREAD_GATE_V1=8, STOCK_TREND_200DMA_V1=8.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-09T22:27:42Z

*From outcome_tracker run `outcome_tracker-20260709T222742-924d5f60`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$232.12 return=+6.084%
- JNJ entry: fill=$230.248 current=$258.87 return=+12.431%
- EQIX entry: fill=$1084.37 current=$1034.87 return=-4.565%
- EQIX entry: fill=$1079.5 current=$1034.87 return=-4.134%
- EQIX exit: fill=$1078.442 current=$1034.87 return=-4.040%
- EQIX entry: fill=$1078.41 current=$1034.87 return=-4.037%
- JNJ entry: fill=$230.116 current=$258.87 return=+12.495%
- WMT entry: fill=$132.276 current=$111.57 return=-15.654%
- WMT entry: fill=$132.474 current=$111.57 return=-15.780%
- EQIX entry: fill=$1076.89 current=$1034.87 return=-3.902%
- EQIX entry: fill=$1076.82 current=$1034.87 return=-3.896%
- JNJ entry: fill=$230.044 current=$258.87 return=+12.531%
- EQIX exit: fill=$1076.718 current=$1034.87 return=-3.887%
- EQIX entry: fill=$1076.542 current=$1034.87 return=-3.871%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-09

*From trigger_performance run `trigger_performance-20260709T222743-7eec3e40`*
*Period: 2026-07-03 to 2026-07-09 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 65% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 51/79 symbols blocked (65%). Avg spread (blocked): 11.186%
- Trend gate (200 DMA): 29/79 symbols below 200 DMA (37% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.445%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 48 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=8, LIQUIDITY_GATE_V1=8, MOMENTUM_BLEND_6M_12M_V1=8, SPREAD_GATE_V1=8, STOCK_TREND_200DMA_V1=8.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
## Outcome Observations — 2026-07-09T22:44:37Z

*From outcome_tracker run `outcome_tracker-20260709T224437-b924c4ea`*

**Current unrealized returns (intraday — no strategy conclusions yet):**
- WELL entry: fill=$218.808 current=$232.12 return=+6.084%
- JNJ entry: fill=$230.248 current=$258.87 return=+12.431%
- EQIX entry: fill=$1084.37 current=$1034.87 return=-4.565%
- EQIX entry: fill=$1079.5 current=$1034.87 return=-4.134%
- EQIX exit: fill=$1078.442 current=$1034.87 return=-4.040%
- EQIX entry: fill=$1078.41 current=$1034.87 return=-4.037%
- JNJ entry: fill=$230.116 current=$258.87 return=+12.495%
- WMT entry: fill=$132.276 current=$111.57 return=-15.654%
- WMT entry: fill=$132.474 current=$111.57 return=-15.780%
- EQIX entry: fill=$1076.89 current=$1034.87 return=-3.902%
- EQIX entry: fill=$1076.82 current=$1034.87 return=-3.896%
- JNJ entry: fill=$230.044 current=$258.87 return=+12.531%
- EQIX exit: fill=$1076.718 current=$1034.87 return=-3.887%
- EQIX entry: fill=$1076.542 current=$1034.87 return=-3.871%

*Outcome windows pending — revisit after 1, 5, 20, 63 trading days.*

---
## Trigger Performance Observations — 2026-07-09

*From trigger_performance run `trigger_performance-20260709T224928-c02a285d`*
*Period: 2026-07-03 to 2026-07-09 (7 days)*

**Operational issues:**
- [ ] Trigger 'SPREAD_GATE_V1' (spread_gate): Spread gate blocking 65% of candidates — review spread threshold or data freshness.

**Observations (research only — no strategy conclusions):**
- Spread gate: 51/79 symbols blocked (65%). Avg spread (blocked): 11.186%
- Trend gate (200 DMA): 29/79 symbols below 200 DMA (37% block rate).
- Fill count this period: 14. Need 6 more fills before P/L analysis is meaningful.
- Average current return across 14 tracked outcome(s): -1.445%. Window pending — no conclusions yet.
- Lineage: Lineage snapshot: 14 records (0 complete, 14 partial). 48 trigger fill associations recovered. 14 record(s) have partial lineage — save trade plans to history/trade_plans/ to improve completeness.
- Fills linked to triggers (via lineage): ATR_SIZING_V1=8, LIQUIDITY_GATE_V1=8, MOMENTUM_BLEND_6M_12M_V1=8, SPREAD_GATE_V1=8, STOCK_TREND_200DMA_V1=8.
- IMPORTANT: With only a few paper fills, no trigger should be promoted or demoted. These observations require 20+ fills and a comparison backtest.

**Reminder:** Do not modify strategy.json, risk_limits.json, or trigger_registry.json
based on this report alone. Any experiment requires a candidate PR with:
- Hypothesis, supporting evidence, success criteria, and rollback plan.

---
