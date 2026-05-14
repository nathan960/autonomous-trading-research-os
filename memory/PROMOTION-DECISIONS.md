# Promotion Decisions

Production strategy promotions require evidence, candidate PR, and explicit approval.

## Promotion decision

```json
{
  "generated_at": "2026-05-12T15:31:20Z",
  "production_mutation_allowed": false,
  "promotion_recommended": false,
  "reason": "Insufficient paper evidence for promotion.",
  "run_id": "strategy_improvement-20260512T153120-bc98ee7d"
}
```

## Promotion decision

```json
{
  "generated_at": "2026-05-12T15:32:53Z",
  "production_mutation_allowed": false,
  "promotion_recommended": false,
  "reason": "Insufficient paper evidence for promotion.",
  "run_id": "strategy_improvement-20260512T153253-426c4103"
}
```

## Promotion decision

```json
{
  "generated_at": "2026-05-12T15:33:05Z",
  "production_mutation_allowed": false,
  "promotion_recommended": false,
  "reason": "Insufficient paper evidence for promotion.",
  "run_id": "strategy_improvement-20260512T153305-cfe87d64"
}
```

## Phase Gate — 2026-05-14T18:54:46Z

**run_id:** `phase_gate-20260514T185446-d482be60`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 13 (need ≥ 20)  
- active_orders: 1  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/13 complete (ratio=0.0)  
- drawdown: -7e-06  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 28  
- weekly_reviews_in_history: 6  

**Blocking Issues:**  
- Only 13 filled order(s). Need at least 20 before reviewing promotion.  
- 1 open/active order(s) still pending. Wait for settlement or cancel via cancel_paper_order.py before promotion review.  

**Warnings:**  
- Daily order limit reached today (max=3, violations=['EQIX(count=4,limit=1)', 'JNJ(count=1,limit=1)', 'WMT(count=1,limit=1)']). Churn guard is now active and will prevent future violations. Ensure churn guard config is in place before promotion.  
- Lineage completeness ratio 0.0% (0/13). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---
