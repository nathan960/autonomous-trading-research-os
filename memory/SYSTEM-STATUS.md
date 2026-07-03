## System Status — 2026-05-14T15:28:02Z

**Overall:** RED  | Research: NO  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,802.70  drawdown=-0.00%  positions=3  open_orders=1
**Trade Plan:** trade_plan-20260514T152756-a1cc9ba9  approved=False
**Dry-run gates:** PASS  failed=[]

**Blocking Issues:**
- Open duplicate orders for planned symbols: ['EQIX']

**Warnings:**
- 40 wide-spread symbols (['AMT', 'APD', 'AXP', 'BA', 'BLK', 'CAT', 'COST', 'CVX', 'DIS', 'DUK', 'ECL', 'EOG', 'GS', 'HD', 'HON', 'INTU', 'ISRG', 'JNJ', 'JPM', 'LIN', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MS', 'NEE', 'ORCL', 'PG', 'PLD', 'PM', 'RTX', 'SHW', 'SRE', 'TMO', 'TMUS', 'UNH', 'UNP', 'UPS', 'WELL']) — SPREAD_NOT_TOO_WIDE may block execution

**Required Operator Actions:**
- [ ] Cancel or wait for existing open orders to settle before re-running

---
## System Status — 2026-05-14T15:29:43Z

**Overall:** RED  | Research: NO  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,802.69  drawdown=-0.00%  positions=3  open_orders=1
**Trade Plan:** trade_plan-20260514T152756-a1cc9ba9  approved=False
**Dry-run gates:** FAIL  failed=['NO_DUPLICATE_OPEN_ORDERS']

**Blocking Issues:**
- Open duplicate orders for planned symbols: ['EQIX']
- Execution gates: unexpected failures: ['NO_DUPLICATE_OPEN_ORDERS']

**Warnings:**
- 36 wide-spread symbols (['ABBV', 'ADBE', 'AMGN', 'AMT', 'APD', 'AXP', 'BA', 'BLK', 'COST', 'CRM', 'CVX', 'DE', 'ECL', 'EOG', 'GS', 'HD', 'HON', 'ISRG', 'JNJ', 'LIN', 'LLY', 'LMT', 'LOW', 'MA', 'MS', 'ORCL', 'PG', 'PM', 'RTX', 'TMO', 'TMUS', 'UNH', 'UNP', 'UPS', 'V', 'WELL']) — SPREAD_NOT_TOO_WIDE may block execution

**Required Operator Actions:**
- [ ] Cancel or wait for existing open orders to settle before re-running
- [ ] Investigate gate failures: ['NO_DUPLICATE_OPEN_ORDERS']

---
## System Status — 2026-05-14T17:45:26Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,802.43  drawdown=-0.00%  positions=4  open_orders=1
**Trade Plan:** trade_plan-20260514T174516-ddb701fd  approved=False
**Dry-run gates:** PASS  failed=[]

**Warnings:**
- 37 wide-spread symbols (['ABBV', 'ABT', 'ADBE', 'AMGN', 'APD', 'AXP', 'BA', 'BKNG', 'CAT', 'COP', 'COST', 'CVX', 'DE', 'DIS', 'ECL', 'FCX', 'GS', 'HON', 'INTU', 'ISRG', 'LLY', 'LOW', 'MA', 'MCD', 'MS', 'ORCL', 'PEP', 'PG', 'PLD', 'PM', 'RTX', 'SHW', 'TMO', 'TMUS', 'UNH', 'UNP', 'UPS']) — SPREAD_NOT_TOO_WIDE may block execution
- Daily order limit reached: 6 orders today (max_total_paper_orders_per_day=3)
- Per-symbol daily order limits reached: ['EQIX(count=4,limit=1)', 'JNJ(count=1,limit=1)', 'WMT(count=1,limit=1)']

**Required Operator Actions:**
- [ ] Daily order limits hit — churn guard will block new orders until tomorrow

---
## System Status — 2026-05-14T18:08:57Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,802.14  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260514T180756-fc25ae26  approved=False
**Dry-run gates:** PASS  failed=[]

**Warnings:**
- 28 wide-spread symbols (['ABBV', 'ADBE', 'AMD', 'AMGN', 'AMT', 'APD', 'CAT', 'COST', 'DE', 'ECL', 'EOG', 'GE', 'HON', 'ISRG', 'JPM', 'LIN', 'LLY', 'LOW', 'MCD', 'MS', 'ORCL', 'PEP', 'PG', 'PM', 'RTX', 'TMUS', 'UNP', 'WELL']) — SPREAD_NOT_TOO_WIDE may block execution
- Daily order limit reached: 11 orders today (max_total_paper_orders_per_day=3)
- Per-symbol daily order limits reached: ['EQIX(count=7,limit=1)', 'JNJ(count=2,limit=1)', 'WMT(count=2,limit=1)']

**Required Operator Actions:**
- [ ] Daily order limits hit — churn guard will block new orders until tomorrow

---
## System Status — 2026-05-14T22:18:59Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,802.93  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260514T214947-b0ee5f7f  approved=False
**Dry-run gates:** PASS  failed=[]

**Warnings:**
- 44 wide-spread symbols (['AAPL', 'ABBV', 'AEP', 'AMD', 'AMGN', 'AMT', 'AMZN', 'APD', 'AVGO', 'AXP', 'BA', 'CAT', 'CL', 'CMCSA', 'COST', 'CRM', 'CSCO', 'CVX', 'DIS', 'DUK', 'EOG', 'EQIX', 'GE', 'HON', 'INTU', 'LLY', 'LOW', 'META', 'MRK', 'MSFT', 'NEE', 'ORCL', 'PEP', 'PG', 'PM', 'RTX', 'SHW', 'SLB', 'SO', 'TMUS', 'UNH', 'UPS', 'WELL', 'WMT']) — SPREAD_NOT_TOO_WIDE may block execution
- Daily order limit reached: 11 orders today (max_total_paper_orders_per_day=3)
- Per-symbol daily order limits reached: ['EQIX(count=7,limit=1)', 'JNJ(count=2,limit=1)', 'WMT(count=2,limit=1)']

**Required Operator Actions:**
- [ ] Daily order limits hit — churn guard will block new orders until tomorrow

---
## System Status — 2026-05-15T22:09:58Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,799.26  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260515T214104-7822211e  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 45 wide-spread symbols (['ABBV', 'ADBE', 'AMD', 'AMGN', 'AMT', 'AMZN', 'APD', 'BA', 'BAC', 'BKNG', 'BLK', 'CAT', 'CMCSA', 'COP', 'COST', 'CSCO', 'CVX', 'DIS', 'DUK', 'EOG', 'FCX', 'HD', 'HON', 'INTU', 'JNJ', 'KO', 'MA', 'MCD', 'MDLZ', 'META', 'MRK', 'NEE', 'NKE', 'NVDA', 'ORCL', 'PLD', 'SBUX', 'SHW', 'SRE', 'TMO', 'UNH', 'UPS', 'WELL', 'WFC', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-05-18T22:12:09Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,800.42  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260518T215059-e7e56c9f  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 54 wide-spread symbols (['AAPL', 'ABBV', 'ABT', 'ADBE', 'AMD', 'AMGN', 'AMZN', 'APD', 'AXP', 'BA', 'BAC', 'CMCSA', 'COP', 'COST', 'CRM', 'CSCO', 'DE', 'DIS', 'ECL', 'EOG', 'FCX', 'GE', 'HON', 'INTU', 'ISRG', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MDLZ', 'META', 'MSFT', 'NEE', 'NFLX', 'NKE', 'NVDA', 'ORCL', 'PEP', 'PLD', 'SHW', 'SLB', 'SO', 'SPY', 'SRE', 'TMO', 'TMUS', 'UNH', 'UNP', 'UPS', 'V', 'WFC', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-05-19T22:23:47Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,800.35  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260519T220014-e0847b4b  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 55 wide-spread symbols (['AAPL', 'ABBV', 'ABT', 'ADBE', 'AEP', 'AMGN', 'APD', 'AVGO', 'AXP', 'BA', 'BKNG', 'BLK', 'CL', 'COP', 'COST', 'CSCO', 'CVX', 'DE', 'DIS', 'ECL', 'GE', 'GOOGL', 'GS', 'HD', 'HON', 'INTU', 'JNJ', 'JPM', 'KO', 'LLY', 'LMT', 'MA', 'MDLZ', 'META', 'MRK', 'MS', 'NEE', 'NFLX', 'NVDA', 'ORCL', 'PEP', 'PG', 'PLD', 'SBUX', 'SLB', 'SO', 'SPY', 'SRE', 'TMO', 'TMUS', 'TSLA', 'UNP', 'UPS', 'WFC', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-05-20T22:42:29Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,800.44  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260520T221523-26202569  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 49 wide-spread symbols (['ABBV', 'ABT', 'ADBE', 'AEP', 'AMD', 'AMGN', 'AMT', 'APD', 'AVGO', 'AXP', 'BAC', 'BLK', 'CAT', 'CL', 'CMCSA', 'COP', 'CRM', 'CSCO', 'DUK', 'EOG', 'EQIX', 'GE', 'GS', 'HD', 'INTU', 'ISRG', 'KO', 'LLY', 'LMT', 'MDLZ', 'META', 'MS', 'NEE', 'NFLX', 'NKE', 'NVDA', 'O', 'ORCL', 'PEP', 'PG', 'PLD', 'RTX', 'SBUX', 'SO', 'SRE', 'TMO', 'UNH', 'WELL', 'WFC']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-05-21T22:39:24Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,798.34  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260521T220533-65e68056  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 53 wide-spread symbols (['ABBV', 'ABT', 'ADBE', 'AEP', 'AMD', 'AMGN', 'APD', 'AXP', 'BA', 'BKNG', 'BLK', 'CAT', 'CL', 'COST', 'CRM', 'DE', 'ECL', 'EOG', 'EQIX', 'FCX', 'GE', 'GS', 'INTU', 'ISRG', 'JPM', 'KO', 'LLY', 'LMT', 'LOW', 'MCD', 'MDLZ', 'META', 'MSFT', 'NEE', 'NFLX', 'NKE', 'ORCL', 'PEP', 'PG', 'RTX', 'SBUX', 'SHW', 'SPY', 'SRE', 'TMO', 'TMUS', 'TSLA', 'UNH', 'UNP', 'UPS', 'V', 'WELL', 'WFC']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-05-22T22:16:17Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,799.22  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260522T215148-d536c070  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 59 wide-spread symbols (['AAPL', 'ABBV', 'ABT', 'ADBE', 'AEP', 'AMD', 'AMGN', 'AMT', 'AMZN', 'APD', 'BLK', 'CL', 'CMCSA', 'CRM', 'CVX', 'DE', 'DIS', 'ECL', 'EOG', 'EQIX', 'FCX', 'GE', 'GOOGL', 'GS', 'HD', 'HON', 'INTU', 'JNJ', 'JPM', 'KO', 'LIN', 'LLY', 'LOW', 'MA', 'MCD', 'MDLZ', 'META', 'MS', 'MSFT', 'NEE', 'NFLX', 'NVDA', 'ORCL', 'PLD', 'SBUX', 'SHW', 'SLB', 'SO', 'SPY', 'SRE', 'TMO', 'TMUS', 'TSLA', 'UNP', 'UPS', 'V', 'WELL', 'WFC', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-05-25T22:16:04Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,799.29  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260525T215050-9fe086a0  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 59 wide-spread symbols (['AAPL', 'ABBV', 'ABT', 'ADBE', 'AEP', 'AMD', 'AMGN', 'AMT', 'AMZN', 'APD', 'BLK', 'CL', 'CMCSA', 'CRM', 'CVX', 'DE', 'DIS', 'ECL', 'EOG', 'EQIX', 'FCX', 'GE', 'GOOGL', 'GS', 'HD', 'HON', 'INTU', 'JNJ', 'JPM', 'KO', 'LIN', 'LLY', 'LOW', 'MA', 'MCD', 'MDLZ', 'META', 'MS', 'MSFT', 'NEE', 'NFLX', 'NVDA', 'ORCL', 'PLD', 'SBUX', 'SHW', 'SLB', 'SO', 'SPY', 'SRE', 'TMO', 'TMUS', 'TSLA', 'UNP', 'UPS', 'V', 'WELL', 'WFC', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-05-26T22:38:07Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,797.01  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260526T221152-f5a3f47e  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 54 wide-spread symbols (['ABT', 'AEP', 'AMD', 'AMGN', 'AMT', 'AMZN', 'AVGO', 'AXP', 'BA', 'BAC', 'BKNG', 'BLK', 'CAT', 'CL', 'CMCSA', 'COST', 'CRM', 'CSCO', 'CVX', 'DIS', 'DUK', 'ECL', 'EQIX', 'FCX', 'GE', 'GOOGL', 'INTU', 'ISRG', 'JNJ', 'LLY', 'LMT', 'LOW', 'MCD', 'META', 'MRK', 'NFLX', 'NKE', 'NVDA', 'O', 'ORCL', 'PEP', 'PLD', 'SHW', 'SLB', 'SO', 'SPY', 'SRE', 'TMUS', 'UNP', 'UPS', 'V', 'WELL', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-05-27T22:49:51Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,796.58  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260527T222228-34add6a2  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 53 wide-spread symbols (['ABT', 'ADBE', 'AMD', 'AMGN', 'AMZN', 'AVGO', 'BA', 'BAC', 'BKNG', 'BLK', 'CAT', 'CL', 'COST', 'CRM', 'CSCO', 'DE', 'DIS', 'DUK', 'ECL', 'EOG', 'EQIX', 'GE', 'GOOGL', 'INTU', 'JNJ', 'JPM', 'KO', 'LIN', 'LLY', 'LMT', 'LOW', 'MDLZ', 'META', 'MRK', 'NEE', 'NFLX', 'NKE', 'NVDA', 'O', 'ORCL', 'PG', 'RTX', 'SLB', 'TMO', 'TMUS', 'UNH', 'UNP', 'UPS', 'V', 'WELL', 'WFC', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-05-28T22:47:50Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,795.89  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260528T222134-2790195b  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 55 wide-spread symbols (['ABBV', 'ABT', 'ADBE', 'AEP', 'AMD', 'AMT', 'AMZN', 'APD', 'AVGO', 'BA', 'CAT', 'CL', 'COP', 'COST', 'CRM', 'CSCO', 'DE', 'DIS', 'ECL', 'EOG', 'FCX', 'GS', 'INTU', 'ISRG', 'KO', 'LIN', 'LLY', 'LMT', 'MCD', 'MDLZ', 'META', 'MRK', 'MS', 'MSFT', 'NVDA', 'ORCL', 'PG', 'PLD', 'RTX', 'SBUX', 'SHW', 'SO', 'SPY', 'SRE', 'TMO', 'TMUS', 'TSLA', 'UNH', 'UNP', 'UPS', 'V', 'WELL', 'WFC', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-05-29T22:41:49Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,792.28  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260529T221830-a6bd11cf  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 48 wide-spread symbols (['ABBV', 'ABT', 'ADBE', 'AMD', 'AMGN', 'AMT', 'AMZN', 'AVGO', 'BA', 'BAC', 'BKNG', 'CL', 'CMCSA', 'COP', 'COST', 'DUK', 'EOG', 'FCX', 'GE', 'GOOGL', 'INTU', 'JNJ', 'JPM', 'KO', 'MA', 'MCD', 'MDLZ', 'META', 'MS', 'MSFT', 'NEE', 'NVDA', 'O', 'ORCL', 'PLD', 'PM', 'RTX', 'SBUX', 'SO', 'SRE', 'TMUS', 'TSLA', 'UNH', 'UNP', 'UPS', 'WELL', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-01T23:07:58Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,788.80  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260601T225035-7f1f2e01  approved=False
**Dry-run gates:** PASS  failed=[]

**Warnings:**
- 57 wide-spread symbols (['ABT', 'ADBE', 'AEP', 'AMD', 'AMGN', 'AMT', 'APD', 'BA', 'CAT', 'CL', 'CMCSA', 'COP', 'COST', 'CRM', 'DE', 'DIS', 'DUK', 'ECL', 'EQIX', 'FCX', 'GE', 'GS', 'HD', 'INTU', 'JNJ', 'KO', 'LIN', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'META', 'MRK', 'MSFT', 'NEE', 'NFLX', 'NKE', 'NVDA', 'O', 'ORCL', 'PEP', 'PG', 'PLD', 'RTX', 'SBUX', 'SHW', 'SLB', 'SO', 'SRE', 'TMO', 'UNH', 'UNP', 'UPS', 'V', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-02T23:07:14Z

**Overall:** RED  | Research: NO  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,789.55  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260602T225104-87aaea10  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS', 'RISK_LIMITS_RESPECTED']

**Blocking Issues:**
- Execution gates: hard failures: ['RISK_LIMITS_RESPECTED']

**Warnings:**
- 53 wide-spread symbols (['ABBV', 'ABT', 'ADBE', 'AMD', 'AMGN', 'AMT', 'AMZN', 'APD', 'AXP', 'BA', 'BAC', 'BLK', 'CAT', 'CL', 'COST', 'CVX', 'DE', 'DIS', 'DUK', 'ECL', 'EQIX', 'GOOGL', 'HON', 'INTU', 'ISRG', 'JNJ', 'LIN', 'LOW', 'MDLZ', 'META', 'MRK', 'MS', 'NEE', 'NFLX', 'NKE', 'NVDA', 'O', 'ORCL', 'PEP', 'PG', 'PLD', 'PM', 'SHW', 'SLB', 'SO', 'SRE', 'TMO', 'UNP', 'UPS', 'V', 'WELL', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

**Required Operator Actions:**
- [ ] Fix hard gate failures before any execution: ['RISK_LIMITS_RESPECTED']

---
## System Status — 2026-06-03T23:11:19Z

**Overall:** RED  | Research: NO  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,792.69  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260603T225309-f5f975f1  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS', 'RISK_LIMITS_RESPECTED']

**Blocking Issues:**
- Execution gates: hard failures: ['RISK_LIMITS_RESPECTED']

**Warnings:**
- 53 wide-spread symbols (['ABT', 'AEP', 'AMGN', 'AMT', 'APD', 'AVGO', 'BA', 'BAC', 'BKNG', 'BLK', 'CAT', 'COP', 'COST', 'CSCO', 'DE', 'DIS', 'ECL', 'EOG', 'EQIX', 'HD', 'INTU', 'JNJ', 'JPM', 'LIN', 'LLY', 'LOW', 'MA', 'MDLZ', 'META', 'MRK', 'MS', 'NFLX', 'NKE', 'NVDA', 'ORCL', 'PG', 'PLD', 'PM', 'RTX', 'SBUX', 'SHW', 'SLB', 'SO', 'SPY', 'SRE', 'TMO', 'TMUS', 'TSLA', 'UPS', 'WELL', 'WFC', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

**Required Operator Actions:**
- [ ] Fix hard gate failures before any execution: ['RISK_LIMITS_RESPECTED']

---
## System Status — 2026-06-04T22:42:00Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,795.75  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260604T221132-a5501470  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 50 wide-spread symbols (['AAPL', 'ABT', 'ADBE', 'AMGN', 'AMZN', 'APD', 'AVGO', 'BA', 'BKNG', 'CAT', 'CL', 'CRM', 'CSCO', 'CVX', 'DE', 'DUK', 'ECL', 'EOG', 'EQIX', 'FCX', 'GE', 'GOOGL', 'HD', 'INTU', 'JNJ', 'JPM', 'KO', 'LIN', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MDLZ', 'META', 'MRK', 'NEE', 'NKE', 'NVDA', 'ORCL', 'PLD', 'SBUX', 'SO', 'SRE', 'TMUS', 'TSLA', 'UNP', 'WELL', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-05T22:22:39Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,796.70  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260605T220550-ed452261  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 47 wide-spread symbols (['ABBV', 'ADBE', 'AMGN', 'AMT', 'AMZN', 'APD', 'BA', 'BAC', 'BKNG', 'BLK', 'CL', 'CMCSA', 'COP', 'COST', 'CRM', 'CSCO', 'DIS', 'ECL', 'EOG', 'GE', 'GOOGL', 'GS', 'INTU', 'JPM', 'KO', 'LOW', 'META', 'MS', 'MSFT', 'NFLX', 'NKE', 'NVDA', 'O', 'PEP', 'PLD', 'PM', 'SHW', 'SLB', 'SO', 'SPY', 'SRE', 'TMUS', 'TSLA', 'UPS', 'WELL', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-08T22:46:09Z

**Overall:** RED  | Research: NO  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,794.78  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260608T221512-6e5e2f60  approved=False
**Dry-run gates:** FAIL  failed=['RISK_LIMITS_RESPECTED']

**Blocking Issues:**
- Execution gates: hard failures: ['RISK_LIMITS_RESPECTED']

**Warnings:**
- 60 wide-spread symbols (['ABBV', 'ABT', 'ADBE', 'AEP', 'AMD', 'AMGN', 'AMT', 'AMZN', 'APD', 'AXP', 'BKNG', 'BLK', 'CL', 'CMCSA', 'COP', 'COST', 'CVX', 'DE', 'DIS', 'DUK', 'EQIX', 'GE', 'GOOGL', 'GS', 'HD', 'HON', 'INTU', 'ISRG', 'JNJ', 'KO', 'LIN', 'LOW', 'MA', 'MCD', 'MDLZ', 'META', 'MRK', 'MSFT', 'NEE', 'NFLX', 'NKE', 'NVDA', 'O', 'ORCL', 'PEP', 'PG', 'PM', 'RTX', 'SBUX', 'SLB', 'SO', 'SPY', 'SRE', 'TMUS', 'TSLA', 'UNP', 'UPS', 'WELL', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

**Required Operator Actions:**
- [ ] Fix hard gate failures before any execution: ['RISK_LIMITS_RESPECTED']

---
## System Status — 2026-06-09T22:46:05Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,796.79  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260609T221409-465d6d04  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 50 wide-spread symbols (['AAPL', 'ABBV', 'ABT', 'AMGN', 'AMZN', 'AXP', 'BA', 'BKNG', 'CAT', 'CL', 'COP', 'COST', 'CRM', 'CSCO', 'CVX', 'DE', 'DIS', 'DUK', 'ECL', 'EQIX', 'GE', 'INTU', 'ISRG', 'JNJ', 'JPM', 'KO', 'LIN', 'LMT', 'MCD', 'META', 'MRK', 'MSFT', 'NFLX', 'NKE', 'NVDA', 'O', 'ORCL', 'PEP', 'PG', 'PLD', 'PM', 'SHW', 'SLB', 'SPY', 'TSLA', 'UPS', 'WELL', 'WFC', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-10T22:56:07Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,796.23  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260610T223055-8fd8c448  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 54 wide-spread symbols (['ABBV', 'ABT', 'AMD', 'AMGN', 'AMT', 'AVGO', 'AXP', 'BA', 'BAC', 'BLK', 'CAT', 'CL', 'COST', 'CRM', 'CSCO', 'DE', 'DUK', 'ECL', 'EOG', 'EQIX', 'FCX', 'GE', 'GOOGL', 'GS', 'HD', 'INTU', 'ISRG', 'JNJ', 'KO', 'LIN', 'LLY', 'LMT', 'MA', 'META', 'MS', 'MSFT', 'NEE', 'NFLX', 'NKE', 'NVDA', 'PG', 'PLD', 'RTX', 'SBUX', 'SHW', 'SLB', 'SRE', 'TSLA', 'UNH', 'UPS', 'V', 'WELL', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-11T22:56:16Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,796.37  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260611T222815-13077acf  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 45 wide-spread symbols (['ABBV', 'AMD', 'AMGN', 'AMT', 'APD', 'AVGO', 'AXP', 'CAT', 'CMCSA', 'COP', 'COST', 'CRM', 'DE', 'ECL', 'EOG', 'FCX', 'GE', 'GOOGL', 'GS', 'HD', 'INTU', 'ISRG', 'LLY', 'MA', 'MDLZ', 'MS', 'MSFT', 'NEE', 'NFLX', 'ORCL', 'PLD', 'RTX', 'SBUX', 'SHW', 'SO', 'SRE', 'TMO', 'TMUS', 'UNH', 'UNP', 'UPS', 'V', 'WELL', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-12T22:43:58Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,799.13  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260612T221433-ee2be16e  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 50 wide-spread symbols (['AAPL', 'ABT', 'AEP', 'AMD', 'AMGN', 'AVGO', 'AXP', 'BA', 'BKNG', 'BLK', 'COP', 'COST', 'CVX', 'DIS', 'ECL', 'EOG', 'EQIX', 'GE', 'HON', 'INTU', 'ISRG', 'JNJ', 'JPM', 'LLY', 'LMT', 'LOW', 'MCD', 'META', 'MRK', 'MS', 'NEE', 'NKE', 'NVDA', 'O', 'ORCL', 'PEP', 'PG', 'PLD', 'PM', 'RTX', 'SO', 'SPY', 'UNH', 'UNP', 'UPS', 'V', 'WELL', 'WFC', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-15T23:07:49Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,798.08  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260615T225020-7870d4cc  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 50 wide-spread symbols (['ABBV', 'AMD', 'AMGN', 'AMZN', 'AVGO', 'AXP', 'BKNG', 'BLK', 'CAT', 'CL', 'CMCSA', 'COST', 'CRM', 'CSCO', 'CVX', 'DE', 'DUK', 'ECL', 'GE', 'GS', 'HD', 'HON', 'INTU', 'KO', 'LIN', 'LLY', 'MA', 'MCD', 'MDLZ', 'META', 'MRK', 'MS', 'MSFT', 'NVDA', 'O', 'ORCL', 'PG', 'PLD', 'PM', 'SHW', 'SLB', 'SO', 'SRE', 'TSLA', 'UNP', 'UPS', 'V', 'WELL', 'WFC', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-16T22:57:12Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,800.91  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260616T223523-aac6ff24  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 53 wide-spread symbols (['ABBV', 'ADBE', 'AEP', 'AMD', 'AVGO', 'AXP', 'BAC', 'BKNG', 'CAT', 'CL', 'COP', 'COST', 'CSCO', 'DE', 'DIS', 'DUK', 'EOG', 'EQIX', 'FCX', 'GE', 'GOOGL', 'GS', 'HD', 'HON', 'INTU', 'ISRG', 'JNJ', 'KO', 'LIN', 'LLY', 'LMT', 'LOW', 'MCD', 'MDLZ', 'META', 'MS', 'MSFT', 'NVDA', 'ORCL', 'PEP', 'PLD', 'PM', 'RTX', 'SHW', 'SLB', 'SO', 'TMO', 'UNH', 'UPS', 'V', 'WELL', 'WFC', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-17T22:51:38Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,797.47  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260617T222605-fc02b41c  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 50 wide-spread symbols (['AAPL', 'ABT', 'ADBE', 'AEP', 'AMD', 'AMGN', 'AMT', 'AMZN', 'AVGO', 'BLK', 'CAT', 'CL', 'CMCSA', 'COP', 'COST', 'CSCO', 'DE', 'DUK', 'ECL', 'EOG', 'EQIX', 'GOOGL', 'GS', 'HD', 'HON', 'INTU', 'JPM', 'KO', 'LIN', 'LLY', 'MA', 'MDLZ', 'MRK', 'MS', 'NVDA', 'PEP', 'PG', 'PLD', 'PM', 'RTX', 'SHW', 'SLB', 'SO', 'SPY', 'SRE', 'TMUS', 'TSLA', 'UNP', 'WFC', 'WMT']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-18T23:02:31Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,796.15  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260618T223320-58ad17c2  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 52 wide-spread symbols (['AAPL', 'ABBV', 'ABT', 'ADBE', 'AEP', 'AMD', 'AMT', 'AVGO', 'AXP', 'BA', 'BAC', 'BKNG', 'CMCSA', 'COST', 'CVX', 'DE', 'DIS', 'DUK', 'EOG', 'GE', 'GS', 'HD', 'HON', 'INTU', 'JNJ', 'KO', 'LMT', 'LOW', 'MA', 'MCD', 'MDLZ', 'MRK', 'NEE', 'NKE', 'NVDA', 'PLD', 'PM', 'SHW', 'SLB', 'SO', 'SRE', 'TMO', 'TMUS', 'TSLA', 'UNH', 'UNP', 'UPS', 'V', 'WELL', 'WFC', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-19T22:12:28Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,796.24  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260619T214923-006f0e6c  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 52 wide-spread symbols (['AAPL', 'ABBV', 'ABT', 'ADBE', 'AEP', 'AMD', 'AMT', 'AVGO', 'AXP', 'BA', 'BAC', 'BKNG', 'CMCSA', 'COST', 'CVX', 'DE', 'DIS', 'DUK', 'EOG', 'GE', 'GS', 'HD', 'HON', 'INTU', 'JNJ', 'KO', 'LMT', 'LOW', 'MA', 'MCD', 'MDLZ', 'MRK', 'NEE', 'NKE', 'NVDA', 'PLD', 'PM', 'SHW', 'SLB', 'SO', 'SRE', 'TMO', 'TMUS', 'TSLA', 'UNH', 'UNP', 'UPS', 'V', 'WELL', 'WFC', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-22T22:53:36Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,799.47  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260622T222533-51c70f9f  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 49 wide-spread symbols (['ABBV', 'ADBE', 'AEP', 'AMT', 'APD', 'AVGO', 'AXP', 'BA', 'BLK', 'CL', 'CMCSA', 'COP', 'COST', 'CRM', 'CVX', 'DUK', 'EOG', 'FCX', 'GE', 'GOOGL', 'GS', 'HD', 'HON', 'INTU', 'JNJ', 'KO', 'LIN', 'LLY', 'LMT', 'MA', 'MCD', 'MDLZ', 'META', 'MSFT', 'NEE', 'NVDA', 'O', 'ORCL', 'PG', 'RTX', 'SHW', 'SLB', 'SRE', 'TMO', 'TSLA', 'UNH', 'UPS', 'WELL', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-23T22:21:38Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,804.38  drawdown=0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260623T220424-c1b61181  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 53 wide-spread symbols (['ABT', 'AMD', 'AMT', 'AMZN', 'AVGO', 'AXP', 'BA', 'BAC', 'BKNG', 'BLK', 'CAT', 'CMCSA', 'COST', 'CRM', 'CSCO', 'CVX', 'DE', 'DIS', 'DUK', 'GE', 'GOOGL', 'HD', 'HON', 'INTU', 'ISRG', 'JPM', 'KO', 'LIN', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MRK', 'MSFT', 'NEE', 'NFLX', 'NVDA', 'O', 'PG', 'PLD', 'PM', 'RTX', 'SHW', 'SLB', 'SRE', 'TMUS', 'UNP', 'V', 'WELL', 'WFC', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-24T22:37:43Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,801.81  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260624T220053-1d9ba5e1  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 54 wide-spread symbols (['ABT', 'ADBE', 'AEP', 'AMD', 'AMGN', 'AMT', 'APD', 'AVGO', 'BA', 'BKNG', 'CAT', 'CL', 'CMCSA', 'COP', 'COST', 'CRM', 'CSCO', 'DE', 'DIS', 'DUK', 'ECL', 'EOG', 'EQIX', 'FCX', 'GOOGL', 'GS', 'HD', 'HON', 'INTU', 'JNJ', 'JPM', 'KO', 'LIN', 'LMT', 'MA', 'MCD', 'MDLZ', 'MS', 'MSFT', 'NFLX', 'NKE', 'NVDA', 'ORCL', 'RTX', 'SBUX', 'SHW', 'SLB', 'TMO', 'TMUS', 'UNH', 'UNP', 'UPS', 'WFC', 'WMT']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-25T22:42:36Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,802.86  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260625T221020-b39e9ac0  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 61 wide-spread symbols (['AAPL', 'ABBV', 'ABT', 'ADBE', 'AEP', 'AMD', 'AMGN', 'AMT', 'APD', 'AVGO', 'AXP', 'BA', 'BAC', 'BKNG', 'CAT', 'CL', 'CMCSA', 'COST', 'CRM', 'CSCO', 'CVX', 'DE', 'DUK', 'ECL', 'EOG', 'EQIX', 'FCX', 'GE', 'GOOGL', 'GS', 'HON', 'INTU', 'ISRG', 'JPM', 'KO', 'LLY', 'LMT', 'LOW', 'MCD', 'MDLZ', 'MRK', 'MS', 'MSFT', 'NEE', 'NFLX', 'NKE', 'O', 'ORCL', 'PEP', 'PG', 'PLD', 'PM', 'RTX', 'TMO', 'TMUS', 'UNP', 'UPS', 'V', 'WFC', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-26T22:22:15Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,806.31  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260626T215150-fad49b07  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 51 wide-spread symbols (['ABBV', 'ABT', 'AEP', 'AMD', 'AMGN', 'AMT', 'AMZN', 'AXP', 'BAC', 'BLK', 'CAT', 'CL', 'COP', 'CRM', 'CSCO', 'DE', 'ECL', 'EOG', 'EQIX', 'FCX', 'GE', 'GS', 'INTU', 'ISRG', 'LMT', 'LOW', 'MA', 'MCD', 'MDLZ', 'META', 'MRK', 'MS', 'NEE', 'NVDA', 'O', 'ORCL', 'PEP', 'PLD', 'RTX', 'SBUX', 'SHW', 'SLB', 'SO', 'SRE', 'TMO', 'TSLA', 'UPS', 'WELL', 'WFC', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-29T22:18:28Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,806.81  drawdown=0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260629T215910-86afd73d  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 59 wide-spread symbols (['AAPL', 'ABBV', 'ABT', 'ADBE', 'AEP', 'AMGN', 'AVGO', 'AXP', 'BA', 'BAC', 'BLK', 'CAT', 'CL', 'CMCSA', 'COP', 'COST', 'CRM', 'CSCO', 'CVX', 'DE', 'DUK', 'ECL', 'EOG', 'FCX', 'GE', 'GOOGL', 'GS', 'HON', 'INTU', 'ISRG', 'JNJ', 'JPM', 'KO', 'LIN', 'MA', 'MCD', 'MDLZ', 'MS', 'MSFT', 'NFLX', 'NKE', 'NVDA', 'O', 'ORCL', 'PEP', 'PLD', 'PM', 'SBUX', 'SHW', 'SLB', 'SO', 'TMO', 'TSLA', 'UNP', 'UPS', 'V', 'WFC', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-06-30T22:36:29Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,801.14  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260630T220350-6225e7ec  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 53 wide-spread symbols (['AAPL', 'ABT', 'ADBE', 'AMGN', 'AMT', 'APD', 'AVGO', 'AXP', 'BA', 'BAC', 'BKNG', 'CAT', 'CMCSA', 'COP', 'COST', 'CRM', 'CVX', 'DIS', 'EOG', 'FCX', 'GE', 'GOOGL', 'GS', 'INTU', 'KO', 'LLY', 'LOW', 'MA', 'MDLZ', 'META', 'MRK', 'MS', 'MSFT', 'NEE', 'NFLX', 'NVDA', 'ORCL', 'PEP', 'PG', 'PLD', 'RTX', 'SBUX', 'SHW', 'SRE', 'TMO', 'TMUS', 'TSLA', 'UNH', 'UNP', 'UPS', 'WELL', 'WFC', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-07-01T22:38:22Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,796.30  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260701T220738-ea134a4e  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 45 wide-spread symbols (['ABT', 'AMT', 'AMZN', 'AXP', 'BA', 'BKNG', 'CAT', 'COP', 'CVX', 'DE', 'DUK', 'ECL', 'EQIX', 'GE', 'GS', 'HD', 'HON', 'INTU', 'ISRG', 'JPM', 'LIN', 'LMT', 'MDLZ', 'MRK', 'MS', 'MSFT', 'NVDA', 'O', 'ORCL', 'PG', 'PLD', 'RTX', 'SHW', 'SLB', 'SO', 'TMO', 'TMUS', 'TSLA', 'UNH', 'UPS', 'V', 'WELL', 'WFC', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-07-02T22:17:02Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,800.08  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260702T214902-9a75395b  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 53 wide-spread symbols (['AAPL', 'ABBV', 'ADBE', 'AMGN', 'AMT', 'AMZN', 'APD', 'AVGO', 'AXP', 'BA', 'BAC', 'BKNG', 'BLK', 'CAT', 'CL', 'COP', 'CRM', 'CVX', 'DIS', 'EOG', 'GE', 'GS', 'HD', 'HON', 'INTU', 'JNJ', 'JPM', 'LLY', 'LMT', 'MA', 'MCD', 'MDLZ', 'MSFT', 'NFLX', 'NKE', 'NVDA', 'O', 'ORCL', 'PEP', 'PG', 'PLD', 'PM', 'RTX', 'SBUX', 'SHW', 'SLB', 'SO', 'SPY', 'TSLA', 'UNH', 'UNP', 'UPS', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-07-03T22:14:17Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,800.52  drawdown=-0.01%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260703T214437-e4bef21e  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 53 wide-spread symbols (['AAPL', 'ABBV', 'ADBE', 'AMGN', 'AMT', 'AMZN', 'APD', 'AVGO', 'AXP', 'BA', 'BAC', 'BKNG', 'BLK', 'CAT', 'CL', 'COP', 'CRM', 'CVX', 'DIS', 'EOG', 'GE', 'GS', 'HD', 'HON', 'INTU', 'JNJ', 'JPM', 'LLY', 'LMT', 'MA', 'MCD', 'MDLZ', 'MSFT', 'NFLX', 'NKE', 'NVDA', 'O', 'ORCL', 'PEP', 'PG', 'PLD', 'PM', 'RTX', 'SBUX', 'SHW', 'SLB', 'SO', 'SPY', 'TSLA', 'UNH', 'UNP', 'UPS', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
