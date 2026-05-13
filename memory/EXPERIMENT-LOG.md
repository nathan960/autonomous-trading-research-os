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
