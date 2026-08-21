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

## Phase Gate — 2026-05-15T22:41:46Z

**run_id:** `phase_gate-20260515T224146-b5a48338`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 14 (need ≥ 20)  
- active_orders: 0  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/14 complete (ratio=0.0)  
- drawdown: -3.9e-05  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 37  
- weekly_reviews_in_history: 7  

**Blocking Issues:**  
- Only 14 filled order(s). Need at least 20 before reviewing promotion.  

**Warnings:**  
- Lineage completeness ratio 0.0% (0/14). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---

## Phase Gate — 2026-05-22T22:45:58Z

**run_id:** `phase_gate-20260522T224558-bcd144aa`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 14 (need ≥ 20)  
- active_orders: 0  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/14 complete (ratio=0.0)  
- drawdown: -3.9e-05  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 47  
- weekly_reviews_in_history: 8  

**Blocking Issues:**  
- Only 14 filled order(s). Need at least 20 before reviewing promotion.  

**Warnings:**  
- Lineage completeness ratio 0.0% (0/14). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---

## Phase Gate — 2026-05-29T23:01:15Z

**run_id:** `phase_gate-20260529T230115-a7992169`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 14 (need ≥ 20)  
- active_orders: 0  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/14 complete (ratio=0.0)  
- drawdown: -0.000109  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 57  
- weekly_reviews_in_history: 9  

**Blocking Issues:**  
- Only 14 filled order(s). Need at least 20 before reviewing promotion.  

**Warnings:**  
- Lineage completeness ratio 0.0% (0/14). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---

## Phase Gate — 2026-06-05T22:54:37Z

**run_id:** `phase_gate-20260605T225437-fc959571`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 14 (need ≥ 20)  
- active_orders: 0  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/14 complete (ratio=0.0)  
- drawdown: -6.5e-05  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 67  
- weekly_reviews_in_history: 10  

**Blocking Issues:**  
- Only 14 filled order(s). Need at least 20 before reviewing promotion.  

**Warnings:**  
- Lineage completeness ratio 0.0% (0/14). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---

## Phase Gate — 2026-06-12T23:05:25Z

**run_id:** `phase_gate-20260612T230525-19597d49`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 14 (need ≥ 20)  
- active_orders: 0  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/14 complete (ratio=0.0)  
- drawdown: -4e-05  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 77  
- weekly_reviews_in_history: 11  

**Blocking Issues:**  
- Only 14 filled order(s). Need at least 20 before reviewing promotion.  

**Warnings:**  
- Lineage completeness ratio 0.0% (0/14). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---

## Phase Gate — 2026-06-19T22:41:21Z

**run_id:** `phase_gate-20260619T224121-1a760364`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 14 (need ≥ 20)  
- active_orders: 0  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/14 complete (ratio=0.0)  
- drawdown: -6.9e-05  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 87  
- weekly_reviews_in_history: 12  

**Blocking Issues:**  
- Only 14 filled order(s). Need at least 20 before reviewing promotion.  

**Warnings:**  
- Lineage completeness ratio 0.0% (0/14). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---

## Phase Gate — 2026-06-26T22:57:16Z

**run_id:** `phase_gate-20260626T225716-a4eaca9b`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 14 (need ≥ 20)  
- active_orders: 0  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/14 complete (ratio=0.0)  
- drawdown: -0.0  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 97  
- weekly_reviews_in_history: 13  

**Blocking Issues:**  
- Only 14 filled order(s). Need at least 20 before reviewing promotion.  

**Warnings:**  
- Lineage completeness ratio 0.0% (0/14). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---

## Phase Gate — 2026-07-03T22:50:59Z

**run_id:** `phase_gate-20260703T225059-4d1469bf`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 14 (need ≥ 20)  
- active_orders: 0  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/14 complete (ratio=0.0)  
- drawdown: -6.3e-05  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 107  
- weekly_reviews_in_history: 14  

**Blocking Issues:**  
- Only 14 filled order(s). Need at least 20 before reviewing promotion.  

**Warnings:**  
- Lineage completeness ratio 0.0% (0/14). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---

## Phase Gate — 2026-07-10T22:46:17Z

**run_id:** `phase_gate-20260710T224617-5e75c9db`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 14 (need ≥ 20)  
- active_orders: 0  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/14 complete (ratio=0.0)  
- drawdown: -3.4e-05  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 117  
- weekly_reviews_in_history: 15  

**Blocking Issues:**  
- Only 14 filled order(s). Need at least 20 before reviewing promotion.  

**Warnings:**  
- Lineage completeness ratio 0.0% (0/14). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---

## Phase Gate — 2026-07-17T22:35:58Z

**run_id:** `phase_gate-20260717T223558-0660dea8`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 14 (need ≥ 20)  
- active_orders: 0  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/14 complete (ratio=0.0)  
- drawdown: -6.3e-05  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 127  
- weekly_reviews_in_history: 16  

**Blocking Issues:**  
- Only 14 filled order(s). Need at least 20 before reviewing promotion.  

**Warnings:**  
- Lineage completeness ratio 0.0% (0/14). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---

## Phase Gate — 2026-07-24T22:48:52Z

**run_id:** `phase_gate-20260724T224852-31e00141`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 14 (need ≥ 20)  
- active_orders: 0  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/14 complete (ratio=0.0)  
- drawdown: -6e-06  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 137  
- weekly_reviews_in_history: 17  

**Blocking Issues:**  
- Only 14 filled order(s). Need at least 20 before reviewing promotion.  

**Warnings:**  
- Lineage completeness ratio 0.0% (0/14). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---

## Phase Gate — 2026-07-31T22:46:46Z

**run_id:** `phase_gate-20260731T224646-db02b34a`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 14 (need ≥ 20)  
- active_orders: 0  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/14 complete (ratio=0.0)  
- drawdown: -0.0001  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 147  
- weekly_reviews_in_history: 18  

**Blocking Issues:**  
- Only 14 filled order(s). Need at least 20 before reviewing promotion.  

**Warnings:**  
- Lineage completeness ratio 0.0% (0/14). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---

## Phase Gate — 2026-08-07T22:22:13Z

**run_id:** `phase_gate-20260807T222213-924d2125`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 14 (need ≥ 20)  
- active_orders: 0  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/14 complete (ratio=0.0)  
- drawdown: -6.7e-05  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 157  
- weekly_reviews_in_history: 19  

**Blocking Issues:**  
- Only 14 filled order(s). Need at least 20 before reviewing promotion.  

**Warnings:**  
- Lineage completeness ratio 0.0% (0/14). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---

## Phase Gate — 2026-08-14T22:09:37Z

**run_id:** `phase_gate-20260814T220937-77718465`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 14 (need ≥ 20)  
- active_orders: 0  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/14 complete (ratio=0.0)  
- drawdown: 0.0  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 167  
- weekly_reviews_in_history: 20  

**Blocking Issues:**  
- Only 14 filled order(s). Need at least 20 before reviewing promotion.  

**Warnings:**  
- Lineage completeness ratio 0.0% (0/14). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---

## Phase Gate — 2026-08-21T22:10:07Z

**run_id:** `phase_gate-20260821T221007-86aa0d96`  
**current_phase:** PHASE_1_TINY_MANUAL  
**recommended_phase:** PHASE_1_TINY_MANUAL  
**status:** STAY AT CURRENT PHASE  
**recommendation:** stay_at_phase  

**Evidence:**  
- filled_orders: 14 (need ≥ 20)  
- active_orders: 0  
- missing_orders: 0  
- rejected_orders: 0  
- source_integrity: ok  
- outcome_integrity: ok  
- lineage: 0/14 complete (ratio=0.0)  
- drawdown: -8.8e-05  
- max_orders_per_run: 1  
- max_notional_per_order: 25.0  
- daily_summaries_in_history: 177  
- weekly_reviews_in_history: 21  

**Blocking Issues:**  
- Only 14 filled order(s). Need at least 20 before reviewing promotion.  

**Warnings:**  
- Lineage completeness ratio 0.0% (0/14). Older fills have partial lineage — trade plan archiving to data/history/trade_plans/ is now active so future fills will be complete. Run build_lineage.py to update after more fills are archived.  

*No config was changed. No orders were placed. No paper execution was enabled. No trade plans were approved. No scheduled execution was enabled.*  

---
