# Experiment and Promotion Governance

Formal process for proposing, evaluating, approving, and rejecting strategy
changes based on evidence. No production config is ever mutated automatically.

## Principles

1. **Evidence first.** Hypotheses are not production changes. An experiment
   needs minimum fills, minimum observations, positive expectancy, no risk
   breaches, and human approval before it can even be nominated for promotion.

2. **Human approval is non-negotiable.** `human_approval_required` cannot be
   set to false. An evaluation with all criteria met produces `promotion_ready=False`
   until a human runs `evaluate_promotion.py --approve --approved-by <name>`.

3. **Approval is a record, not a mutation.** Even a recorded approval does not
   change any config file. The approval produces candidate PR instructions that
   a human must follow manually.

4. **Experiments are append-only.** Each proposal and evaluation is written as
   a new JSON file in `data/history/experiments/`. Nothing is edited in-place.

5. **Protected files.** `config/strategy.json`, `config/risk_limits.json`, and
   `config/trigger_registry.json` are never touched by any governance script.

---

## Lifecycle

```
proposed → active → completed → promoted
                  ↘           ↘ rejected
                   demoted
```

| Status | Meaning |
|--------|---------|
| `proposed` | Experiment filed; evidence not yet collected. |
| `active` | Under observation during paper trading. |
| `completed` | Observation window closed; awaiting decision. |
| `rejected` | Formally rejected — criteria not met or operator rejected. |
| `promoted` | Approved by operator and applied via PR. |
| `demoted` | Demotion criteria triggered; experiment terminated. |

Status transitions are recorded by the operator — no script changes status automatically.

---

## Proposing an experiment

```bash
python scripts/propose_experiment.py \
    --hypothesis "Lowering breadth_threshold from 0.55 to 0.50 increases fills" \
    --trigger BREADTH_TREND \
    --benefit "Est. 5-10 pct more fills in moderate breadth regime" \
    --risk "May increase false positives in weak markets" \
    --sample-size 50
```

With optional patch documentation and promotion criteria overrides:

```bash
python scripts/propose_experiment.py \
    --hypothesis "Lowering breadth_threshold from 0.55 to 0.50 increases fills" \
    --trigger BREADTH_TREND \
    --benefit "Est. 5-10 pct more fills in moderate breadth regime" \
    --risk "May increase false positives in weak markets" \
    --sample-size 50 \
    --patch-file config/strategy.json \
    --patch-key  parameters.breadth_threshold \
    --patch-old  0.55 \
    --patch-new  0.50 \
    --min-fills  30 \
    --min-obs    75 \
    --notes      "Based on 60-day trigger performance log showing 40 pct breadth days below 0.55."
```

Or from a JSON file:

```bash
python scripts/propose_experiment.py --from-file proposal.json
```

**Output:**
- `data/history/experiments/<experiment_id>.json`
- `memory/EXPERIMENT-LOG.md` (appended)

---

## Experiment schema

```json
{
  "schema_version": "0.1.0",
  "experiment_id": "exp-20260514T123456-a1b2c3d4",
  "created_at": "2026-05-14T12:34:56Z",
  "status": "proposed",
  "hypothesis": "...",
  "affected_trigger_or_rule": "BREADTH_TREND",
  "affected_config_key": "parameters.breadth_threshold",
  "expected_benefit": "...",
  "risk": "...",
  "required_sample_size": 50,
  "required_backtest": true,
  "required_paper_validation": true,
  "promotion_criteria": {
    "min_filled_trade_count": 20,
    "min_observation_count": 50,
    "min_expectancy_after_costs": 0.001,
    "must_beat_spy": false,
    "must_beat_bil": true,
    "no_risk_limit_breach": true,
    "no_operational_failures": true,
    "human_approval_required": true
  },
  "demotion_criteria": {
    "max_drawdown_pct": -0.05,
    "max_consecutive_losses": 5,
    "min_expectancy_after_costs": -0.005
  },
  "candidate_patch": {
    "file": "config/strategy.json",
    "key": "parameters.breadth_threshold",
    "old_value": 0.55,
    "new_value": 0.50
  },
  "notes": "",
  "production_mutation_allowed": false
}
```

### Required fields

| Field | Description |
|-------|-------------|
| `hypothesis` | Clear, falsifiable statement of expected improvement |
| `affected_trigger_or_rule` | Trigger ID or config rule under test |
| `expected_benefit` | Quantified expected gain (fill rate, return, etc.) |
| `risk` | Potential downside or failure mode |
| `required_sample_size` | Minimum fills before evaluation is valid (≥ 1) |
| `required_backtest` | Whether backtest/replay is required before paper |
| `required_paper_validation` | Whether paper results are required before promotion |
| `promotion_criteria` | See below |
| `demotion_criteria` | See below |

### Promotion criteria fields

| Field | Default | Description |
|-------|---------|-------------|
| `min_filled_trade_count` | 20 | Minimum paper fills (hard floor: 10) |
| `min_observation_count` | 50 | Minimum trigger evaluations |
| `min_expectancy_after_costs` | 0.001 | Avg return minus 0.05% cost estimate |
| `must_beat_spy` | `false` | Strategy must exceed SPY return |
| `must_beat_bil` | `true` | Strategy must exceed BIL (risk-free) return |
| `no_risk_limit_breach` | `true` | No hard gate failures during experiment |
| `no_operational_failures` | `true` | No rejected orders or operational warnings |
| `human_approval_required` | `true` | **Always true — cannot be waived** |

### Demotion criteria fields

| Field | Default | Description |
|-------|---------|-------------|
| `max_drawdown_pct` | -0.05 | Portfolio drawdown threshold (-5%) |
| `max_consecutive_losses` | 5 | Trailing consecutive losing trades |
| `min_expectancy_after_costs` | -0.005 | Floor below which experiment is terminated |

---

## Evaluating an experiment

```bash
python scripts/evaluate_promotion.py --experiment-id exp-20260514T123456-a1b2c3d4
```

Reads evidence from `data/latest/` (outcomes, trigger performance, execution
report, order monitor, risk state) and writes an evaluation JSON.

**Output:**
- `data/history/experiments/<id>_eval_<ts>.json`

---

## Evaluation schema

```json
{
  "experiment_id": "exp-20260514T123456-a1b2c3d4",
  "generated_at": "...",
  "evidence": {
    "filled_trade_count": 25,
    "observation_count": 60,
    "expectancy_after_costs": 0.003,
    "strategy_period_return_pct": 0.08,
    "spy_period_return_pct": 0.05,
    "bil_period_return_pct": 0.01,
    "beats_spy": true,
    "beats_bil": true,
    "risk_limit_breaches": [],
    "operational_failures": [],
    "drawdown": -0.02,
    "consecutive_losses": 1
  },
  "criteria_met": {
    "min_filled_trade_count": true,
    "min_observation_count": true,
    "positive_expectancy_after_costs": true,
    "no_risk_limit_breach": true,
    "no_operational_failures": true,
    "beats_spy": true,
    "beats_bil": true
  },
  "all_promotion_criteria_met": true,
  "demotion_triggered": false,
  "demotion_reasons": [],
  "promotion_ready": false,
  "human_approval_required": true,
  "human_approved": false,
  "decision": "pending",
  "production_mutation_allowed": false,
  "candidate_pr_instructions": "..."
}
```

`promotion_ready` is always `false` from `evaluate_promotion`. It becomes
meaningful only after `build_promotion_decision` records an approval.

---

## Recording a decision

### Approve

```bash
python scripts/evaluate_promotion.py \
    --experiment-id exp-20260514T123456-a1b2c3d4 \
    --approve \
    --approved-by "operator-alice" \
    --notes "Paper evidence sufficient over 60-day window. Approving candidate PR."
```

### Reject

```bash
python scripts/evaluate_promotion.py \
    --experiment-id exp-20260514T123456-a1b2c3d4 \
    --reject \
    --notes "Insufficient fills (8 vs required 20). Re-open after more data."
```

**Output:**
- `data/history/experiments/<id>_decision_<ts>.json`
- `memory/PROMOTION-DECISIONS.md` (appended)

---

## After approval: applying the change

An approved decision does NOT change any config file. It produces
`candidate_pr_instructions` in the JSON. To apply:

1. **Read the instructions** from the decision JSON or the evaluation JSON.

2. **Create a branch:**
   ```bash
   git checkout -b "experiment/promote-<experiment_id>"
   ```

3. **Apply the patch manually** to the documented config file and key.

4. **Run validation:**
   ```bash
   python scripts/validate_all.py
   python -m pytest
   ```

5. **Open a PR** with:
   - Title: `experiment: promote <rule> change (<experiment_id>)`
   - Body: hypothesis, paper evidence, link to evaluation JSON, rollback notes
   - Reviewers: at least one second approver

6. **Do not merge** without explicit human review.

---

## Demotion

If demotion criteria are triggered during evaluation, the script prints a
warning. To formally record a demotion:

```bash
python scripts/evaluate_promotion.py \
    --experiment-id exp-20260514T123456-a1b2c3d4 \
    --reject \
    --notes "Demotion triggered: drawdown -6.2% exceeded threshold."
```

---

## File locations

| Path | Contents |
|------|----------|
| `data/history/experiments/<id>.json` | Experiment proposal |
| `data/history/experiments/<id>_eval_<ts>.json` | Evaluation result |
| `data/history/experiments/<id>_decision_<ts>.json` | Approval/rejection record |
| `memory/EXPERIMENT-LOG.md` | Human-readable log of all proposals |
| `memory/PROMOTION-DECISIONS.md` | Human-readable log of all decisions |

---

## What the governance system will NOT do

- Modify `config/strategy.json`, `config/risk_limits.json`, or
  `config/trigger_registry.json` — ever.
- Set `production_mutation_allowed=true` in any record.
- Auto-approve experiments when criteria are met.
- Waive `human_approval_required`.
- Enable paper execution or place orders.
- Change risk limits.
- Promote a strategy from fewer than `ABSOLUTE_MIN_FILLS` (10) paper fills.
