# Open Order Resolution

Manual workflow for inspecting and optionally cancelling a single open
Alpaca paper order. This is the correct tool when `NO_DUPLICATE_OPEN_ORDERS`
fails at execution time or when an order is unexpectedly stuck.

## Principles

1. **Read before acting.** Always run `list_only` first to confirm the order
   exists and is in the expected state.

2. **Explicit confirmation is non-negotiable.** `cancel_one` requires
   `confirm_cancel=CANCEL` (exact string) in both the workflow input and the
   script argument. Any other value fails closed without touching the broker.

3. **No new orders.** This workflow and its scripts cannot place, replace, or
   modify orders. Only cancellation of a single existing paper order is possible.

4. **Full audit trail.** Every run — list or cancel — produces a JSON audit
   file in `data/history/orders/` and appends to `memory/ORDER-RESOLUTION-LOG.md`.
   Cancellations also append to `memory/TRADE-LOG.md`.

5. **Paper only.** The Alpaca client is constructed with `paper=True`.
   `LIVE_TRADING_CONFIRMED` and `ENABLE_PAPER_EXECUTION` are both `false` in
   the workflow environment.

---

## When to use this workflow

- `NO_DUPLICATE_OPEN_ORDERS` execution gate fails because a previous order
  was not filled or cancelled and is still open.
- An order was submitted but the market closed before it could fill.
- You want to inspect open orders without running the full research cycle.

---

## Workflow inputs

| Input | Required | Description |
|-------|----------|-------------|
| `action` | yes | `list_only` or `cancel_one` |
| `client_order_id` | conditional | TOS-... format ID. Required for `cancel_one` unless `broker_order_id` is set. |
| `broker_order_id` | conditional | Alpaca UUID. Used if `client_order_id` is not provided. |
| `confirm_cancel` | yes | Must be exactly `CANCEL` for cancellation. Ignored for `list_only`. |
| `notes` | no | Free-text rationale appended to the audit record. |

---

## Step-by-step

### 1. Inspect open orders

Run **list_only** first:

```
action:          list_only
confirm_cancel:  NO  (default — not used)
```

Review the printed output and `data/history/orders/list_open_orders_*.json`
to confirm the `client_order_id` and `broker_order_id` of the target order.

### 2. Cancel one order

Run **cancel_one** with the order identified in step 1:

```
action:           cancel_one
client_order_id:  TOS-20260514T154817-EQIX-BUY
confirm_cancel:   CANCEL
notes:            Cancelling stale day order after market close.
```

The workflow will:
1. Verify `confirm_cancel == CANCEL` (fails closed if not).
2. Call `cancel_paper_order.py` which:
   - Re-validates `confirm_cancel` independently.
   - Fetches the order from Alpaca to verify it exists and is cancellable.
   - Validates the order is in a cancellable status (new, accepted,
     pending_new, held, partially_filled).
   - Validates the order side is `buy` (this system is long-only).
   - Calls `cancel_order_by_id` on the Alpaca paper trading client.
   - Writes an audit JSON to `data/history/orders/`.
   - Appends to `memory/TRADE-LOG.md` and `memory/ORDER-RESOLUTION-LOG.md`.

### 3. After cancellation

Re-run the research cycle or `monitor_orders.py` to confirm the cancellation
was accepted and the order no longer appears as open.

---

## CLI usage (local)

### List open orders

```bash
export TRADING_MODE=paper
export ALPACA_PAPER=true
python scripts/list_open_orders.py

# Dry-run (uses stored data/latest/orders_snapshot.json):
python scripts/list_open_orders.py --dry-run
```

### Cancel a single paper order

```bash
export TRADING_MODE=paper
export ALPACA_PAPER=true

# By client order ID:
python scripts/cancel_paper_order.py \
    --client-order-id TOS-20260514T154817-EQIX-BUY \
    --confirm-cancel CANCEL \
    --notes "Cancelling stale day order after market close."

# By broker order UUID:
python scripts/cancel_paper_order.py \
    --broker-order-id 3351082e-8e6a-4148-af27-81e5414dd0db \
    --confirm-cancel CANCEL

# Dry-run (no broker API call — uses stored snapshot for order lookup):
python scripts/cancel_paper_order.py \
    --client-order-id TOS-20260514T154817-EQIX-BUY \
    --confirm-cancel CANCEL \
    --dry-run
```

---

## File locations

| Path | Contents |
|------|----------|
| `data/history/orders/list_open_orders_<run_id>.json` | Order list audit record |
| `data/history/orders/order_cancel_<run_id>.json` | Cancellation audit record |
| `memory/ORDER-RESOLUTION-LOG.md` | Human-readable log of all list and cancel actions |
| `memory/TRADE-LOG.md` | Cancellations appended here alongside execution records |

---

## What this workflow will NOT do

- Place new orders.
- Replace or modify existing orders.
- Cancel orders in bulk.
- Operate in live trading mode.
- Cancel orders that are already in a terminal state (filled, canceled,
  expired, replaced, rejected).
- Cancel a sell order (this system is long-only; a sell order would be
  unexpected and is blocked by validation).
- Proceed without `confirm_cancel=CANCEL` (exact string).
- Write or read `ALPACA_API_KEY` or `ALPACA_API_SECRET` anywhere other than
  the secure secrets store.
