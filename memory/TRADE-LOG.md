# Trade Log

Execution attempts, submitted paper orders, skips, errors, and position-monitor outcomes are logged here.

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T15:31:20Z",
  "run_id": "execution-20260512T153120-a20828c0",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "3db855f6bc252467eed8d7675c053c1b94dddde0c5ae7bf5ada481935cd557be",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.02559465,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Position monitor completed

```json
{
  "drawdown": 0.0,
  "equity": 40000.0,
  "generated_at": "2026-05-12T15:31:20Z",
  "position_count": 0,
  "run_id": "position_monitor-20260512T153120-83bf6e24",
  "schema_version": "0.1.0",
  "status": "OK",
  "use_alpaca": false,
  "violations": []
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T15:31:30Z",
  "run_id": "execution-20260512T153129-86d9b9f0",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "781e14195cfc473146586404e3c3d9e8b38a2f06bfad35867b68bb43f158a0ed",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.01597525,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T15:32:53Z",
  "run_id": "execution-20260512T153253-0ba5873e",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "acc6818ef018c8530abf46de23e1ffc4400a4dbbb91ce543fda54c6929e4ca0e",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.023264183333333334,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Position monitor completed

```json
{
  "drawdown": 0.0,
  "equity": 40000.0,
  "generated_at": "2026-05-12T15:32:53Z",
  "position_count": 0,
  "run_id": "position_monitor-20260512T153253-f5b2f106",
  "schema_version": "0.1.0",
  "status": "OK",
  "use_alpaca": false,
  "violations": []
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T15:33:05Z",
  "run_id": "execution-20260512T153305-15251a6c",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "209321ee8bfc8308e88d3f37670894bc67fdc87e7ea8621a81b6ded9262aaa5e",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.013966983333333332,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Position monitor completed

```json
{
  "drawdown": 0.0,
  "equity": 40000.0,
  "generated_at": "2026-05-12T15:33:05Z",
  "position_count": 0,
  "run_id": "position_monitor-20260512T153305-53451c31",
  "schema_version": "0.1.0",
  "status": "OK",
  "use_alpaca": false,
  "violations": []
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T15:33:12Z",
  "run_id": "execution-20260512T153311-29338c98",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "eafa80017fbe07fddac1b2e89bb027ea4845eeb38c9940dd532a26d16ed642bb",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.016075883333333332,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T16:25:43Z",
  "run_id": "execution-20260512T162543-f43bd673",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "8775d5146cc11c1af1ebf14fdd8b2fa5c4ecdf4f94d15577d3e2bbb212508e12",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.010717966666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T16:41:43Z",
  "run_id": "execution-20260512T164143-d22ae89d",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "704c77858eb7b24f9b54c7a1e9924cc05a21a5b37f8bb3f8da5f6fd0bb8e5841",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.0046165166666666665,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T16:56:01Z",
  "run_id": "execution-20260512T165601-c8d84990",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "43c6e75e13b2091d0ef514e42e32c4645ef595f00933206e90df501659d3fdbb",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.010833116666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:09:04Z",
  "run_id": "execution-20260512T170904-4530a860",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "45e42630febca33310762bd820c61df313580a19f15d3cad2c47422ad66e32af",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.01146715,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:09:39Z",
  "run_id": "execution-20260512T170939-8ba4104f",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "50ac2d692a66edd4310fcb296642f30c215fed8f5c373fb323d25e6285688d27",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.007178916666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-12T17:21:53Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 11,
  "orders_validated": 11,
  "plan_id": "trade_plan-20260512T171215-200ec4ba",
  "run_id": "execution-20260512T172153-12e1a120",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "0d9edf4f1ccc2f9df3dad0de535b6faad1673807e4f71a748eaa2b3b4e8dd139"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:35:26Z",
  "run_id": "execution-20260512T173526-4e3f28d8",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "054760162b875c1258d7e9eeb6d0b1da74f538139859fea34e629b163a5ffba4",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.0107853,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:47:36Z",
  "run_id": "execution-20260512T174736-aab62b09",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "e9cf75575fe00cf90f6568e97f76fe4bea47b77312fa7bb892cd85658ba5a8ce",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.010707,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:47:44Z",
  "run_id": "execution-20260512T174744-3632a627",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "9552350933e92f326793c4b9c4a89058da4983262fbaf2e4d7d637a4dc3acbee",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.019361383333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:47:49Z",
  "run_id": "execution-20260512T174749-0e432044",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "4628a115d34f79cc64d7304791ba0900e8048dd093b3510c25141d2ea8d11438",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.008237616666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:47:55Z",
  "run_id": "execution-20260512T174755-44c42d0c",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "f2d9abf471ece7e6cd38bf21fde5354df7916bb0f6119876db4c7be4804b9c21",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.006437300000000001,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "SPREAD_NOT_TOO_WIDE"
  ],
  "generated_at": "2026-05-12T17:48:33Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 15,
  "orders_validated": 17,
  "plan_id": "trade_plan-20260512T174833-a95ddc3a",
  "run_id": "execution-20260512T174833-8a168561",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "7187194f79dbf8a3c6f64fb9cc356eaee1ab6456b3396a6ed6aaf7c95cb0a9e9"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T18:23:53Z",
  "run_id": "execution-20260512T182353-45daa85c",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "da79f7820b51fca182ae899b675e835f364d36d715dceb7f61e8a03e743aac18",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.01570595,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T18:24:13Z",
  "run_id": "execution-20260512T182413-184b60f8",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "b024ae27bcc8ba7a0baf5470ce2eb62124ac106003f72af751fe2b68ecf80774",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.020626066666666668,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T18:24:19Z",
  "run_id": "execution-20260512T182419-3035be12",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "4529428e6110412e5bc4302d23693624cb2220b56fc4a5242852761876af8bbc",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.005748433333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T18:24:25Z",
  "run_id": "execution-20260512T182425-d7f0fbc3",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "c582a4e5785e46172c36164d9103016ea752b9b87025b41039ea8d6c8bfda988",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.016776266666666664,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T18:24:31Z",
  "run_id": "execution-20260512T182431-d1a4cff4",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "4abd85771a1f7a0f6d4e38c0b0769d266624c681fc90de71ce6841f653731c15",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.00974325,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "RISK_STATE_NOT_PAUSED"
  ],
  "generated_at": "2026-05-12T18:25:07Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 11,
  "orders_validated": 11,
  "plan_id": "trade_plan-20260512T182449-e8679da5",
  "run_id": "execution-20260512T182507-73855233",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "e93171f73d02323ba8d12bf92d714be2aa9fda4bade9192679e05b01aacadac1"
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "SPREAD_NOT_TOO_WIDE"
  ],
  "generated_at": "2026-05-12T19:45:51Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 13,
  "orders_validated": 15,
  "plan_id": "trade_plan-20260512T194551-286a1ccf",
  "run_id": "execution-20260512T194551-8b775a07",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "129d27c931075227bc616d6d83e64909e1de5f989cc8c58e9ce81a5b730cc51d"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:46:26Z",
  "run_id": "execution-20260512T204626-14c11f55",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "df7e66450535adfaba51e8edec8e1113e34ff9482e5a82a45a9b65edeee3c8ca",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.004942533333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:49:02Z",
  "run_id": "execution-20260512T204902-2160169f",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "d2c85fdd0f532536fc281ae4c7082d3c77bfa0650545f5544856ef00ef891146",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.0062546,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:50:36Z",
  "run_id": "execution-20260512T205036-03817eb3",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "fdbe7fbf89cba55fd53b0dd36d865f47cfb78d2d6b660e8dff2838c893d57aea",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.007643366666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:51:34Z",
  "run_id": "execution-20260512T205134-5a169ba6",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "54ee2d8eeb40bf0119d7e3fc68c9ce58fbb4ee8e6484b039ab624111de237df7",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.008520583333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:51:56Z",
  "run_id": "execution-20260512T205156-c61deb8e",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "a46a349a7f936ba49b22e8c264ca526e6888a95e73f96c5797a046907f8b9248",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.007743166666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:52:13Z",
  "run_id": "execution-20260512T205213-d32d0cbf",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "54abef48d25e009a00dbb218e857516089bf9b6f632dce39c89fd75d43d5c1a5",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.010255366666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:52:22Z",
  "run_id": "execution-20260512T205222-c45b38f9",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "72e596acf4000d83e564ed09b7564190e75ec4cabe28f1da66ffe1b62ffecb78",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.0152097,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:52:28Z",
  "run_id": "execution-20260512T205228-c66044bf",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "5bf1f4d16797bf28375bd97c8d582edcd70f102afcc3ddc9b494eb3c71bc7502",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.015124416666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:52:36Z",
  "run_id": "execution-20260512T205236-2ee9428f",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "0dba45346458e6e79898c167aee17f8898366247aeb4cc5a56cad3eefc954485",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.012359716666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:52:43Z",
  "run_id": "execution-20260512T205243-cb30ace3",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "716e3a673ba6b7b2b35758d26c7c68fd6d83c49aa156e09d025419d0f70fffff",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.007410016666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "RISK_STATE_NOT_PAUSED"
  ],
  "generated_at": "2026-05-12T20:55:41Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260512T205538-6e92e41f",
  "run_id": "execution-20260512T205541-f6030429",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "a60cf1f47122f119465ec97026fbeb226c5790f69ce8b876b0de028eb3b05d2e"
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-12T20:56:07Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260512T205538-6e92e41f",
  "run_id": "execution-20260512T205607-5978f6f5",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "a60cf1f47122f119465ec97026fbeb226c5790f69ce8b876b0de028eb3b05d2e"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:56:11Z",
  "run_id": "execution-20260512T205611-08292204",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "410a9b72153b1f52a740ec95688f6f9428c303e4220b6159a0f85140e2d33ff6",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.008039766666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-12T20:57:30Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260512T205611-b0ec7467",
  "run_id": "execution-20260512T205730-981a1726",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "c2a47ebea76369ce01a751c6ee3bff86059ad55ee73e3511646827b4f28445df"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:57:37Z",
  "run_id": "execution-20260512T205736-c3491168",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "9e6196fd88e15f96a2d29b9fc724d7d5c4dbeaa8d4cfb3939d4f6c2e1cf7a1a1",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.016469833333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-12T20:59:18Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260512T205918-71daec15",
  "run_id": "execution-20260512T205918-0602a349",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "935f3ddc4666246177b96f599daedb2749f5400466f02d50624539ed9f1d3a2c"
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-12T21:16:51Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260512T211650-20309759",
  "run_id": "execution-20260512T211651-ec294806",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "74a42f0a5a7c7356bc22d8c767aa170ff8530965987efaf083bc8dad198adc4c"
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-12T21:18:05Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260512T211805-192708ea",
  "run_id": "execution-20260512T211805-695513a6",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "0583cb7de3ff35add81317df307519a705da0275a4b6926eb15c486748f97bb5"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T12:31:35Z",
  "run_id": "execution-20260513T123135-d9c9c196",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "8adb9ac2d7ed33006c4cb6c2c27b2630006dd0eebbb5971e1697aa6a481a41ae",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.018799316666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-13T12:32:24Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T123221-0c1f1017",
  "run_id": "execution-20260513T123224-6f8cd635",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "3fa458ed29a14b1d57c82884546bbc667214640aedb7124b03f9e259aff2e2dc"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T12:33:17Z",
  "run_id": "execution-20260513T123317-88081f22",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "31d5f44310fd33c794cdf4b13ab589f18d84776414a9e306b05135ec353a4fd4",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.014444066666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-13T12:33:29Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T123325-29c7072f",
  "run_id": "execution-20260513T123329-6216ebe6",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "3194c0f3311249f7a12d5151594a47c2f38d8aa1c1b132479a57a50cd07a7316"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T12:59:49Z",
  "run_id": "execution-20260513T125949-07d72fbc",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "26dacadf73d90c473d5db3c8d8b84760578c8882da7577514ece12a3e9fed61c",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.008499,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T12:59:55Z",
  "run_id": "execution-20260513T125955-ab3c7b18",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "f558f80b633065be6549b488183173ac7ea4b3363243b15c438bacafa4ee823d",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.010637666666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T13:00:02Z",
  "run_id": "execution-20260513T130002-b8ab2ece",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "f5ce032e9f0ebe9f603f6187e067644ec38e06fb8f440f4149733b672e01c6aa",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.020788033333333334,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T13:00:07Z",
  "run_id": "execution-20260513T130007-7d5407c1",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "ef87b380e222b85fa9a27b38d6d9284baed5e59bdcf2f83e559627111483736a",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.008498,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T13:00:13Z",
  "run_id": "execution-20260513T130013-84b24029",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "e1ea7db9cc45908ca2f10a016557469bca003d822304476c2619e3d90ca8a235",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.005203483333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T15:43:36Z",
  "run_id": "execution-20260513T154336-ff0b6596",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "bf29c76b5f2975b2e570a74fb91b2a2a740303369351d4b89f1876fffc01d949",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.0081979,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T15:57:02Z",
  "run_id": "execution-20260513T155702-395e8b7f",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "949999d39a53661bf404773b8b7b72d362f31c84b7b098b986955b958263cad5",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.00996855,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-13T15:57:22Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T155719-180cf00b",
  "run_id": "execution-20260513T155722-f0483960",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "50ae17c976bd03def65743862c357ee4a2c30482bf6951ff6479172615fbeb16"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T15:58:05Z",
  "run_id": "execution-20260513T155805-1b178365",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "b6362663a274be009081aa84699cdacb008458828ffa62708369db6a106c07ae",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.0197076,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T15:58:13Z",
  "run_id": "execution-20260513T155813-679e88a5",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "2cde00fa843c04bc0b0d4ed6816ee63241a5f39fddcc5c008dcb9c8c18a4cbaa",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.014322466666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T15:58:19Z",
  "run_id": "execution-20260513T155819-da355d12",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "6b1ca38d0488b9ef763c852baab86675d1680090a14f28b1d5c2f376506e7e3b",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.01901325,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T15:58:24Z",
  "run_id": "execution-20260513T155824-08089232",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "be7c519cad6f98e95e251b663ab8784fd720d0c0dd6ffe5cf71b3495c06ea7bb",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.011068533333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-13T15:58:44Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T155844-a000af7b",
  "run_id": "execution-20260513T155844-cf4871a2",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "d5d5a202dc4bdbb7312c3c289d5142332a757f2df2ad67195322c61c6e0983ec"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T16:14:11Z",
  "run_id": "execution-20260513T161411-18959257",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "4192165ea37c5f607dac3422ff022ed3abf4485763496187168c559225dc7d01",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.005924250000000001,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-13T16:14:22Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T161422-f1812cd5",
  "run_id": "execution-20260513T161422-c7cdee2a",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "eefe0d38abcec21f36e04cb1297e1027664eafee76d1e88b6593a147cfd327ae"
}
```

## order_monitor run

```json
{
  "dry_run": true,
  "generated_at": "2026-05-13T16:14:27Z",
  "lifecycles": [],
  "orders_active": 0,
  "orders_filled": 0,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 0,
  "run_id": "order_monitor-20260513T161427-d75995ca",
  "source": "stored_snapshot",
  "stale_orders": [],
  "warnings": []
}
```

## order_monitor run

```json
{
  "dry_run": true,
  "generated_at": "2026-05-13T16:16:33Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": null,
      "lifecycle_status": "missing",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    }
  ],
  "orders_active": 0,
  "orders_filled": 0,
  "orders_missing": 1,
  "orders_rejected": 0,
  "orders_tracked": 1,
  "run_id": "order_monitor-20260513T161633-e8b4ec95",
  "source": "stored_snapshot",
  "stale_orders": [],
  "warnings": [
    "order TOS-20260513T160035-WELL-BUY (broker_id='a57f3df1-f9d5-4ab7-8655-ed8240ade13e') not found in Alpaca open or recent closed orders"
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T16:16:43Z",
  "run_id": "execution-20260513T161643-37f3e528",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "44e7927f97fda9b8be6a65481f512543a808064bb61d811185e82901ed9f18d4",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.005116183333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T16:34:39Z",
  "run_id": "execution-20260513T163439-3e69e775",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "201add782f1a65864852e61f05a5ef99779f25fb3798210471effd9141c1356b",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.011110116666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## order_monitor run

```json
{
  "dry_run": true,
  "generated_at": "2026-05-13T16:34:45Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": null,
      "lifecycle_status": "missing",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    }
  ],
  "orders_active": 0,
  "orders_filled": 0,
  "orders_missing": 1,
  "orders_rejected": 0,
  "orders_tracked": 1,
  "run_id": "order_monitor-20260513T163445-db740ab7",
  "source": "stored_snapshot",
  "stale_orders": [],
  "warnings": [
    "order TOS-20260513T160035-WELL-BUY (broker_id='a57f3df1-f9d5-4ab7-8655-ed8240ade13e') not found in Alpaca open or recent closed orders"
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-13T16:39:14Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T163914-a0408f5c",
  "run_id": "execution-20260513T163914-5806a296",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "2c0fc9294920e8abd2d5186ed978296e3a8b42070cd514e4ba005d0d3d88af6f"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T16:59:28Z",
  "run_id": "execution-20260513T165928-9002a1ab",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "2be35cb9540b6134ee2401aed545b280d71b5b6a893018f87e3fc214a0c13711",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.01753521666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-13T17:23:27Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T172327-90852869",
  "run_id": "execution-20260513T172327-9066f495",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "2b00ebed42a5c402feffaa6c2087fdbe767e88f3fe4c16ca62123a8738fefcd1"
}
```

## order_monitor run

```json
{
  "dry_run": true,
  "generated_at": "2026-05-13T17:24:01Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": null,
      "lifecycle_status": "missing",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    }
  ],
  "orders_active": 0,
  "orders_filled": 0,
  "orders_missing": 1,
  "orders_rejected": 0,
  "orders_tracked": 1,
  "run_id": "order_monitor-20260513T172401-ba786d52",
  "source": "stored_snapshot",
  "stale_orders": [],
  "warnings": [
    "order TOS-20260513T160035-WELL-BUY (broker_id='a57f3df1-f9d5-4ab7-8655-ed8240ade13e') not found in Alpaca open or recent closed orders"
  ]
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-13T17:47:42Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": null,
      "lifecycle_status": "unknown",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    }
  ],
  "orders_active": 0,
  "orders_filled": 0,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 1,
  "run_id": "order_monitor-20260513T174742-2bda44ae",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T19:04:43Z",
  "run_id": "execution-20260513T190443-c14eaa08",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "16f4ebbb8ce119dfb68ce1f939f28a89796ec3c4eeac3acde47b87c6286c94e8",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.020721633333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T19:04:53Z",
  "run_id": "execution-20260513T190453-c6e0ae17",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "f89898bdd40c95bd1fbb4808e9bab6959dc70af840c5a21c2b87bc30976df323",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.010818316666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T19:04:59Z",
  "run_id": "execution-20260513T190459-bb4a5926",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "1ef52caf7c0d296665599802beef49082553bb43a75a00bdda95ab84eeede2b0",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.007667516666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## order_monitor run

```json
{
  "dry_run": true,
  "generated_at": "2026-05-13T19:16:57Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": null,
      "lifecycle_status": "missing",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    }
  ],
  "orders_active": 0,
  "orders_filled": 0,
  "orders_missing": 1,
  "orders_rejected": 0,
  "orders_tracked": 1,
  "run_id": "order_monitor-20260513T191657-7236613c",
  "source": "stored_snapshot",
  "stale_orders": [],
  "warnings": [
    "order TOS-20260513T160035-WELL-BUY (broker_id='a57f3df1-f9d5-4ab7-8655-ed8240ade13e') not found in Alpaca open or recent closed orders"
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T19:17:07Z",
  "run_id": "execution-20260513T191707-e1168ae0",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "eb6bcf4a5dfeb6d72b6019a1e87340bacea3cfaf93b9fd526bcbce08f0778068",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.018373466666666668,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-13T19:19:59Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    }
  ],
  "orders_active": 0,
  "orders_filled": 1,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 1,
  "run_id": "order_monitor-20260513T191959-be097bf5",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-13T19:20:55Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T192054-7bc0d923",
  "run_id": "execution-20260513T192055-9711b452",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "338cb4a89319ff12d217ed489a5ab71dde6b1a9f961bd8f07a20a40d375e58e6"
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-13T19:25:26Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T192526-c793d98e",
  "run_id": "execution-20260513T192526-de0f27e6",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e"
}
```

## execute_paper run

```json
{
  "all_gates_pass": true,
  "blocked_reason": null,
  "dry_run": false,
  "failed_gates": [],
  "generated_at": "2026-05-13T19:25:27Z",
  "orders_submitted": 1,
  "orders_submitted_err": 0,
  "orders_submitted_ok": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T192526-c793d98e",
  "run_id": "execution-20260513T192527-04dacaf4",
  "status": "PAPER_SUBMITTED",
  "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e"
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-13T19:28:24Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T192823-a50ed039",
  "run_id": "execution-20260513T192824-10e2f864",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "28bb34ae1e3159dbfb57ed39d15e610811d8e613c0a8a7ee41d5b9368fd00df1"
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-13T19:29:34Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T192934-3bac0e2c",
  "run_id": "execution-20260513T192934-5bf69ea9",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2"
}
```

## execute_paper run

```json
{
  "all_gates_pass": true,
  "blocked_reason": null,
  "dry_run": false,
  "failed_gates": [],
  "generated_at": "2026-05-13T19:29:35Z",
  "orders_submitted": 1,
  "orders_submitted_err": 0,
  "orders_submitted_ok": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T192934-3bac0e2c",
  "run_id": "execution-20260513T192935-303e6fbe",
  "status": "PAPER_SUBMITTED",
  "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-13T19:30:31Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 1,
  "orders_filled": 2,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 3,
  "run_id": "order_monitor-20260513T193031-beade3eb",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-13T19:31:29Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T193129-1ae31684",
  "run_id": "execution-20260513T193129-d9b8742a",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "70d351684fd0ff1d656b332817fbe6f1dee77935f2384cc3c2b3771f0c571d59"
}
```

## execute_paper run

```json
{
  "all_gates_pass": true,
  "blocked_reason": "all_attempted_orders_failed_broker_submission: ['APIError: {\"available\":\"0.023054861\",\"code\":40310000,\"existing_qty\":\"0.023054861\",\"held_for_orders\":\"0\",\"message\":\"insufficient qty available for order (requested: 0.023057412, available: 0.023054861)\",\"symbol\":\"EQIX\"}']",
  "dry_run": false,
  "failed_gates": [],
  "generated_at": "2026-05-13T19:31:30Z",
  "orders_submitted": 1,
  "orders_submitted_err": 1,
  "orders_submitted_ok": 0,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T193129-1ae31684",
  "run_id": "execution-20260513T193130-305917e5",
  "status": "PAPER_ORDER_ERRORS",
  "trade_plan_hash": "70d351684fd0ff1d656b332817fbe6f1dee77935f2384cc3c2b3771f0c571d59"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-13T19:32:15Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 3,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 3,
  "run_id": "order_monitor-20260513T193215-abd957a2",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-13T19:33:17Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 0,
  "orders_validated": 0,
  "plan_id": "trade_plan-20260513T193317-e5036a68",
  "run_id": "execution-20260513T193317-d8bfdaf4",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "5730cbef1c1dc9990c985d7fb9957380ed9658f529e54d0134fc3ab1a753bd5e"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T19:52:37Z",
  "run_id": "execution-20260513T195237-118aaac8",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "991ddff373b8320cc98b22ac42bfdb8bcce001d7a272eaacefc755359f8bcdc5",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.015672066666666668,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```
## Outcome Tracker — 2026-05-13T19:53:51Z

**Run ID:** `outcome_tracker-20260513T195351-015ef98f`  **Outcomes tracked:** 3

- WELL BUY (entry) fill=$218.808 return=-31.064% | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+78.669% | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-54.625% | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T19:54:58Z",
  "run_id": "execution-20260513T195458-3c5f91be",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "ef30dc53c1cd77dcd1b94c6a21b32032359febc1576cd221304f5a9b29414784",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.006574066666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T20:08:09Z",
  "run_id": "execution-20260513T200809-3a7b0615",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "24d74548e1ad4b704ec8c4e127ba25c5d85aa5ecb8721996ede9fe7fef032363",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.016730366666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T20:08:15Z",
  "run_id": "execution-20260513T200814-7e96a2f1",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "ef2e7ac1a3da5e072afe2b14a8eb358cb9464e18c9e9338f0d9b0442a52cb30b",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.01656695,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T20:08:22Z",
  "run_id": "execution-20260513T200822-ecde18f6",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "566e9820796b4b3cce55be0a3a01c91bd377ae55d25980941131c5b8a53ca615",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.019417466666666668,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T20:08:27Z",
  "run_id": "execution-20260513T200827-e0449ed2",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "c574ea23d700ec7613216dbeacf275653468e60e5d3669ca742b211b9edc5d0f",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.013311433333333334,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T20:08:33Z",
  "run_id": "execution-20260513T200833-b302bbd9",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "513bf6601290146c0c86ccb792a1dfacc9b4145a3a24ff47bfe42450df5bb3ab",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.011943366666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T20:10:13Z",
  "run_id": "execution-20260513T201013-6fe0f2ee",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "3671c8e3e3d8c8c9a289557b37dfc9957b6afbb6800567b374272d49d3fd4aa0",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.019550083333333336,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T20:55:25Z",
  "run_id": "execution-20260513T205525-c6d70e53",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "2c5dba1d457a00ef731a7fba960eb3044e76688320ef6ff452592015a0e694d1",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.018794433333333336,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T20:57:04Z",
  "run_id": "execution-20260513T205704-4c990a3c",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "685e35187fabdd9a06941456f29bba557328122d306d605335330fc7b660a41b",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.016011016666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T20:57:13Z",
  "run_id": "execution-20260513T205713-6941fcda",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "d338f7d77f27e49a4f600159d17b32e33466ea9dbe823f95e970a7ab70739169",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.015159933333333332,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T20:57:24Z",
  "run_id": "execution-20260513T205724-2711aaf3",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "a76be8d07fc355f91e43d9676c61d04a8581235d2e2d4e4bef4d08c8ac6e769b",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.0173234,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T20:58:15Z",
  "run_id": "execution-20260513T205815-53297e18",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "49a0d5bb462df2aae5490d78e2395ac60db91fb42405077ec7cfa29446e36e9e",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.008887283333333332,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-13T21:02:02Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 3,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 3,
  "run_id": "order_monitor-20260513T210202-634fc7d9",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```
## Outcome Tracker — 2026-05-13T21:03:03Z

**Run ID:** `outcome_tracker-20260513T210303-fe0c667b`  **Outcomes tracked:** 3
## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T21:27:37Z",
  "run_id": "execution-20260513T212737-3e8a991b",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "63eac28dac4c3292ea76dc1906317544a528b1fefce196785aa01a2dbeb15271",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.019627333333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```
## Outcome Tracker — 2026-05-13T21:27:51Z

**Run ID:** `outcome_tracker-20260513T212751-abca712a`  **Outcomes tracked:** 3

- WELL BUY (entry) fill=$218.808 return=+0.609% unpl=$+0.1522 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.281% unpl=$+0.0704 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.654% unpl=$-0.1635 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T21:39:18Z",
  "run_id": "execution-20260513T213918-42ac7893",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "7259d36acd592961981bc4552c8862eddbc4aa1770282b7b05b4701eb688c235",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.009120650000000001,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "QUOTE_FRESHNESS"
  ],
  "generated_at": "2026-05-13T21:50:27Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260513T215026-c8754de3",
  "run_id": "execution-20260513T215027-de088ae7",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "319bdf24dc5149dc938bf41e76d15f72250104181c38b3aed18cc331c18e982b"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-13T21:51:50Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 3,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 3,
  "run_id": "order_monitor-20260513T215150-081d0a9f",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```
## Outcome Tracker — 2026-05-13T22:40:21Z

**Run ID:** `outcome_tracker-20260513T224021-e7ad10a5`  **Outcomes tracked:** 3

- WELL BUY (entry) fill=$218.808 return=+0.609% unpl=$+0.1522 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.079% unpl=$+0.0198 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.654% unpl=$-0.1635 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T22:09:16Z",
  "run_id": "execution-20260513T220916-a1b41aec",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "f344e03a736ea769da059ff98499639a59a6489fdef423ce333fdc458da817c7",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.020317666666666668,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-13T22:10:46Z",
  "run_id": "execution-20260513T221046-7bc3f75a",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "6bebf18a080ca883f89a8049ff866dac885792b8c9073ad3eed126afdc02f3aa",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.012992433333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T13:46:28Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T134628-b5d9bd7f",
  "run_id": "execution-20260514T134628-9c44a1a9",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "8860af9907681d29685f7a697835b802958c5f815f028ecaf8ca6fd058f3abfa"
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T13:48:13Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T134813-981486ac",
  "run_id": "execution-20260514T134813-10d10286",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "7640812d552e7f825dd8ffda3202fe1661acd3cc3ac155e20fb4977b9f2a640a"
}
```

## execute_paper run

```json
{
  "all_gates_pass": false,
  "blocked_reason": "gate(s) failed: ['CANONICAL_SOURCE_INTEGRITY']",
  "dry_run": false,
  "failed_gates": [
    "CANONICAL_SOURCE_INTEGRITY"
  ],
  "generated_at": "2026-05-14T13:48:14Z",
  "orders_submitted": 0,
  "orders_submitted_err": 0,
  "orders_submitted_ok": 0,
  "orders_validated": 0,
  "plan_id": "trade_plan-20260514T134813-981486ac",
  "run_id": "execution-20260514T134814-b4369954",
  "status": "PAPER_FAIL",
  "trade_plan_hash": "7640812d552e7f825dd8ffda3202fe1661acd3cc3ac155e20fb4977b9f2a640a"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T13:50:03Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 3,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 3,
  "run_id": "order_monitor-20260514T135003-8d27b238",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```
## Outcome Tracker — 2026-05-14T13:50:52Z

**Run ID:** `outcome_tracker-20260514T135052-782298a9`  **Outcomes tracked:** 3

- WELL BUY (entry) fill=$218.808 return=+0.371% unpl=$+0.0928 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.283% unpl=$+0.0708 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.824% unpl=$-0.2061 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T13:53:52Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T135352-f5848ff8",
  "run_id": "execution-20260514T135352-6d5d4d04",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "20573e8975fabd34cd94e60c3a1beca8799befd85cfe00f94329ae5fb678558e"
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T13:55:03Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T135503-484a3f03",
  "run_id": "execution-20260514T135503-e885485c",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "2efbed265751d3233eb8a1511f9b4d8f6cfdc0226d9e3f613addc0913576d579"
}
```

## execute_paper run

```json
{
  "all_gates_pass": false,
  "blocked_reason": "gate(s) failed: ['CANONICAL_SOURCE_INTEGRITY']",
  "dry_run": false,
  "failed_gates": [
    "CANONICAL_SOURCE_INTEGRITY"
  ],
  "generated_at": "2026-05-14T13:55:04Z",
  "orders_submitted": 0,
  "orders_submitted_err": 0,
  "orders_submitted_ok": 0,
  "orders_validated": 0,
  "plan_id": "trade_plan-20260514T135503-484a3f03",
  "run_id": "execution-20260514T135504-19cce5c5",
  "status": "PAPER_FAIL",
  "trade_plan_hash": "2efbed265751d3233eb8a1511f9b4d8f6cfdc0226d9e3f613addc0913576d579"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T13:56:04Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 3,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 3,
  "run_id": "order_monitor-20260514T135604-69822f2b",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```
## Outcome Tracker — 2026-05-14T13:56:45Z

**Run ID:** `outcome_tracker-20260514T135645-bc7586e4`  **Outcomes tracked:** 3

- WELL BUY (entry) fill=$218.808 return=+0.586% unpl=$+0.1465 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.424% unpl=$+0.1061 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.372% unpl=$-0.0929 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---
## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T14:08:37Z",
  "run_id": "execution-20260514T140837-a1764156",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "91e5936d38bf90e62417d2b76ccc604e31394789fc57dec82db753e8074f97f4",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.016034866666666665,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T14:08:44Z",
  "run_id": "execution-20260514T140844-ae6fc7a2",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "667387c32728a17a365857ae5a9774827b81cba1ce6987e7445c733cded4c0bd",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.019886133333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T14:08:50Z",
  "run_id": "execution-20260514T140850-221c7f63",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "fe4a6589f58550795340002dcf3fccfdcf242e51cb74f1da25bd918067448b5e",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.017429233333333335,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T14:16:25Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 3,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 3,
  "run_id": "order_monitor-20260514T141625-5c83a59b",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T14:16:25Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T141625-a3944e26",
  "run_id": "execution-20260514T141625-7f7875ec",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "c4f4465fc7519aeccc2287525953fd7d5841f105ec69ca9ff68d4391c3bef14d"
}
```
## Outcome Tracker — 2026-05-14T14:16:25Z

**Run ID:** `outcome_tracker-20260514T141625-5c83a59b`  **Outcomes tracked:** 3

- WELL BUY (entry) fill=$218.808 return=+0.280% unpl=$+0.0699 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.348% unpl=$+0.0871 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.759% unpl=$-0.1899 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---
## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T14:13:21Z",
  "run_id": "execution-20260514T141321-6a2eef66",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "7b2b6d3e0b35cb66581c7d419040e982f2fce3e3112ce5128bd8945f1baba7ae",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.019294416666666665,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T14:20:18Z",
  "run_id": "execution-20260514T142018-2a606c3b",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "d5ef7e6ab917f7c751f192f115dfdc5556312ea7fd67f6070c40ca5c4f5c651f",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.008218366666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T14:55:01Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 3,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 3,
  "run_id": "order_monitor-20260514T145501-3f4a1031",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T14:55:02Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T145502-e78a9cd9",
  "run_id": "execution-20260514T145502-ccf45a10",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "bae1ddfd00fe353cb53157644a954c822a7f7781837c7d5badaf4203090e8a1a"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T14:55:08Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 3,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 3,
  "run_id": "order_monitor-20260514T145508-e2cd3c52",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```
## Outcome Tracker — 2026-05-14T14:55:09Z

**Run ID:** `outcome_tracker-20260514T145509-dd18af53`  **Outcomes tracked:** 3

- WELL BUY (entry) fill=$218.808 return=+0.010% unpl=$+0.0025 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-0.110% unpl=$-0.0275 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.443% unpl=$-0.1108 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T14:56:25Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 3,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 3,
  "run_id": "order_monitor-20260514T145625-fbedd40d",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T14:56:25Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T145625-7807f306",
  "run_id": "execution-20260514T145625-e9aa35b2",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e"
}
```

## execute_paper run

```json
{
  "all_gates_pass": true,
  "blocked_reason": null,
  "dry_run": false,
  "failed_gates": [],
  "generated_at": "2026-05-14T14:56:26Z",
  "orders_submitted": 1,
  "orders_submitted_err": 0,
  "orders_submitted_ok": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T145625-7807f306",
  "run_id": "execution-20260514T145626-8a29a24f",
  "status": "PAPER_SUBMITTED",
  "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T14:56:34Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 1,
  "orders_filled": 3,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 4,
  "run_id": "order_monitor-20260514T145634-50dad7cb",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```
## Outcome Tracker — 2026-05-14T14:56:34Z

**Run ID:** `outcome_tracker-20260514T145634-50dad7cb`  **Outcomes tracked:** 3

- WELL BUY (entry) fill=$218.808 return=+0.103% unpl=$+0.0258 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.007% unpl=$+0.0018 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.367% unpl=$-0.0916 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---
## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T14:58:01Z",
  "run_id": "execution-20260514T145801-926740b4",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "e3c63704be73d9cfd754166eef541c1940d9e8e16544c4f981ef2d72170a66de",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.010654933333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T15:27:29Z",
  "run_id": "execution-20260514T152729-ce5b07d9",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "c42e45d3e472e30ca4165887602e830d18f615c31e6bee86066e4d80a05ff5c7",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.009058716666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T15:27:38Z",
  "run_id": "execution-20260514T152738-ba6c7a51",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "1434d23dd99643ae43c900f954a1f0a16ecbc93528473670ea3dec8260e544a1",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.019338916666666664,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T15:27:44Z",
  "run_id": "execution-20260514T152744-4ee16f6a",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "f5f1adb71fe7ee1c1b1b60384265325a7e5d26eee85e21a11c783ee791f3bdc4",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.015468333333333334,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T15:27:50Z",
  "run_id": "execution-20260514T152750-926050ef",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "4f93bc98418510b11b19722b4ec414e9642cee93afd6b8a4c19c857e32838811",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.008708316666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T15:27:56Z",
  "run_id": "execution-20260514T152756-fd5a3ea4",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "66f1af002c7f39839a0aba0067e00a856bc61806a6c452004f29c09e01125d11",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.012878133333333335,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T15:39:46Z",
  "run_id": "execution-20260514T153946-80be5930",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "af3c2c35409cbe0a5b39b24ed9b7ceb43646c9c1bf9919863306f2fe90f3ddd8",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.014852716666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T15:43:23Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 4,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 4,
  "run_id": "order_monitor-20260514T154323-8f5dd83f",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T15:43:23Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T154323-1f27d10d",
  "run_id": "execution-20260514T154323-433cec94",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0"
}
```

## execute_paper run

```json
{
  "all_gates_pass": true,
  "blocked_reason": null,
  "dry_run": false,
  "failed_gates": [],
  "generated_at": "2026-05-14T15:43:24Z",
  "orders_submitted": 1,
  "orders_submitted_err": 0,
  "orders_submitted_ok": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T154323-1f27d10d",
  "run_id": "execution-20260514T154324-0732af2c",
  "status": "PAPER_SUBMITTED",
  "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T15:43:29Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    }
  ],
  "orders_active": 1,
  "orders_filled": 4,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 5,
  "run_id": "order_monitor-20260514T154329-4c3be2d7",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```
## Outcome Tracker — 2026-05-14T15:43:29Z

**Run ID:** `outcome_tracker-20260514T154329-4c3be2d7`  **Outcomes tracked:** 4

- WELL BUY (entry) fill=$218.808 return=-0.375% unpl=$-0.0937 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-0.060% unpl=$-0.0150 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.603% unpl=$-0.1893 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-0.154% unpl=$-0.1893 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T15:44:45Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    }
  ],
  "orders_active": 1,
  "orders_filled": 4,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 5,
  "run_id": "order_monitor-20260514T154445-9041df87",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T15:44:45Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T154445-01c16697",
  "run_id": "execution-20260514T154445-23b2e2b2",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "11bb219d80970d5ef7ae4e3985f77f121a32b4828a2eac56374c8e6f02746c86"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T15:44:49Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    }
  ],
  "orders_active": 1,
  "orders_filled": 4,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 5,
  "run_id": "order_monitor-20260514T154449-4dcd0712",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```
## Outcome Tracker — 2026-05-14T15:44:50Z

**Run ID:** `outcome_tracker-20260514T154450-35e30060`  **Outcomes tracked:** 4

- WELL BUY (entry) fill=$218.808 return=-0.246% unpl=$-0.0615 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-0.027% unpl=$-0.0068 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.541% unpl=$-0.1585 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-0.093% unpl=$-0.1585 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T15:45:42Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    }
  ],
  "orders_active": 1,
  "orders_filled": 4,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 5,
  "run_id": "order_monitor-20260514T154542-30ed0b4d",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T15:45:43Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T154543-b29ff94f",
  "run_id": "execution-20260514T154543-cb4f35e4",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09"
}
```

## execute_paper run

```json
{
  "all_gates_pass": true,
  "blocked_reason": null,
  "dry_run": false,
  "failed_gates": [],
  "generated_at": "2026-05-14T15:45:44Z",
  "orders_submitted": 1,
  "orders_submitted_err": 0,
  "orders_submitted_ok": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T154543-b29ff94f",
  "run_id": "execution-20260514T154544-c2e241e8",
  "status": "PAPER_SUBMITTED",
  "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T15:45:49Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 2,
  "orders_filled": 4,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 6,
  "run_id": "order_monitor-20260514T154549-e3d51b1c",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```
## Outcome Tracker — 2026-05-14T15:45:49Z

**Run ID:** `outcome_tracker-20260514T154549-e3d51b1c`  **Outcomes tracked:** 4

- WELL BUY (entry) fill=$218.808 return=-0.244% unpl=$-0.0610 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-0.012% unpl=$-0.0030 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.562% unpl=$-0.1689 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-0.113% unpl=$-0.1689 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T15:48:17Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": "134588c731983acd575c2d9c8d2ecd7ec2cf69da2484cacac3f4593ebe04b73d"
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 1,
  "orders_filled": 5,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 6,
  "run_id": "order_monitor-20260514T154817-27f0a157",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T15:48:17Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T154817-6a53654a",
  "run_id": "execution-20260514T154817-f46a6166",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3"
}
```

## execute_paper run

```json
{
  "all_gates_pass": true,
  "blocked_reason": null,
  "dry_run": false,
  "failed_gates": [],
  "generated_at": "2026-05-14T15:48:18Z",
  "orders_submitted": 1,
  "orders_submitted_err": 0,
  "orders_submitted_ok": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T154817-6a53654a",
  "run_id": "execution-20260514T154818-6157fada",
  "status": "PAPER_SUBMITTED",
  "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T15:48:23Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 2,
  "orders_filled": 5,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 7,
  "run_id": "order_monitor-20260514T154823-07890943",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```
## Outcome Tracker — 2026-05-14T15:48:23Z

**Run ID:** `outcome_tracker-20260514T154823-07890943`  **Outcomes tracked:** 5

- WELL BUY (entry) fill=$218.808 return=-0.255% unpl=$-0.0638 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.044% unpl=$+0.0111 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.466% unpl=$-0.0601 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-0.017% unpl=$-0.0601 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=+0.081% unpl=$-0.0601 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T15:50:31Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 2,
  "orders_filled": 5,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 7,
  "run_id": "order_monitor-20260514T155031-fd621a28",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "NO_DUPLICATE_OPEN_ORDERS"
  ],
  "generated_at": "2026-05-14T15:50:32Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T155032-c05cf55a",
  "run_id": "execution-20260514T155032-43f41202",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "c1fbcf96017ca150e36b9d4083e807bc68c095da1f74fb50232dc985e56ef82c"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T15:52:30Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 2,
  "orders_filled": 5,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 7,
  "run_id": "order_monitor-20260514T155230-610e999d",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "NO_DUPLICATE_OPEN_ORDERS"
  ],
  "generated_at": "2026-05-14T15:52:30Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T155230-b606f849",
  "run_id": "execution-20260514T155230-c8efe290",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "9238cc1a0dd5e2d85769af34909856154316397ef41c6ecada78c4b684fd4640"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T15:52:36Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 2,
  "orders_filled": 5,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 7,
  "run_id": "order_monitor-20260514T155236-24ace729",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```
## Outcome Tracker — 2026-05-14T15:52:37Z

**Run ID:** `outcome_tracker-20260514T155237-6c401389`  **Outcomes tracked:** 5

- WELL BUY (entry) fill=$218.808 return=-0.317% unpl=$-0.0792 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.107% unpl=$+0.0268 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.602% unpl=$-0.0942 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-0.154% unpl=$-0.0942 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-0.056% unpl=$-0.0942 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T15:53:41Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 2,
  "orders_filled": 5,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 7,
  "run_id": "order_monitor-20260514T155341-8b726252",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T15:53:42Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T155342-102808af",
  "run_id": "execution-20260514T155342-f0180db7",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "1c2610baa63628b7463e3997d90d7faf24f99bc7fcedb3bf64a3760cef10ad20"
}
```
## Outcome Tracker — 2026-05-14T15:53:42Z

**Run ID:** `outcome_tracker-20260514T155342-ecda892c`  **Outcomes tracked:** 5

- WELL BUY (entry) fill=$218.808 return=-0.317% unpl=$-0.0792 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.088% unpl=$+0.0219 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.584% unpl=$-0.0896 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-0.135% unpl=$-0.0896 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-0.037% unpl=$-0.0896 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T15:54:48Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 2,
  "orders_filled": 5,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 7,
  "run_id": "order_monitor-20260514T155448-3a6f1d73",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "NO_DUPLICATE_OPEN_ORDERS"
  ],
  "generated_at": "2026-05-14T15:54:48Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T155448-12f13857",
  "run_id": "execution-20260514T155448-0602c399",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "9f96f10928c70a84030bc41d4c7a97285e71b15bc501391047d2dd89d3c42eca"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T16:30:03Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 1,
  "orders_filled": 6,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 7,
  "run_id": "order_monitor-20260514T163003-ef335475",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T16:30:03Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T163003-2a802acf",
  "run_id": "execution-20260514T163003-73a62e3e",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "7aa55ea8dfbeaef774d466f8c57fffec2f7055f61c8bda5e8e9fa58a5ab1a8ac"
}
```
## Outcome Tracker — 2026-05-14T16:30:03Z

**Run ID:** `outcome_tracker-20260514T163003-ef335475`  **Outcomes tracked:** 6

- WELL BUY (entry) fill=$218.808 return=-0.397% unpl=$-0.0992 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.010% unpl=$+0.0024 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.684% unpl=$-0.1483 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-0.236% unpl=$-0.1483 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-0.138% unpl=$-0.1483 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-0.135% unpl=$-0.1483 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T16:31:12Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 1,
  "orders_filled": 6,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 7,
  "run_id": "order_monitor-20260514T163112-693a64d2",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T16:31:13Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T163113-1c676d38",
  "run_id": "execution-20260514T163113-0b51ab01",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b"
}
```

## execute_paper run

```json
{
  "all_gates_pass": true,
  "blocked_reason": null,
  "dry_run": false,
  "failed_gates": [],
  "generated_at": "2026-05-14T16:31:14Z",
  "orders_submitted": 1,
  "orders_submitted_err": 0,
  "orders_submitted_ok": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T163113-1c676d38",
  "run_id": "execution-20260514T163114-dd6029a9",
  "status": "PAPER_SUBMITTED",
  "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T16:31:20Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 2,
  "orders_filled": 6,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 8,
  "run_id": "order_monitor-20260514T163120-833c0bc8",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```
## Outcome Tracker — 2026-05-14T16:31:20Z

**Run ID:** `outcome_tracker-20260514T163120-833c0bc8`  **Outcomes tracked:** 6

- WELL BUY (entry) fill=$218.808 return=-0.349% unpl=$-0.0872 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.010% unpl=$+0.0024 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.633% unpl=$-0.1227 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-0.184% unpl=$-0.1227 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-0.086% unpl=$-0.1227 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-0.084% unpl=$-0.1227 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T16:52:31Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 1,
  "orders_filled": 7,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 8,
  "run_id": "order_monitor-20260514T165231-689e0867",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T16:52:32Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T165232-1f83cea2",
  "run_id": "execution-20260514T165232-630dc166",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b"
}
```

## execute_paper run

```json
{
  "all_gates_pass": true,
  "blocked_reason": null,
  "dry_run": false,
  "failed_gates": [],
  "generated_at": "2026-05-14T16:52:33Z",
  "orders_submitted": 1,
  "orders_submitted_err": 0,
  "orders_submitted_ok": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T165232-1f83cea2",
  "run_id": "execution-20260514T165233-adcb0da2",
  "status": "PAPER_SUBMITTED",
  "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T16:52:37Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": null,
      "lifecycle_status": "new",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": "04d3134a795621baabb716268a210988f99c925d868f964607ba6a55436d61fe"
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    }
  ],
  "orders_active": 1,
  "orders_filled": 8,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 9,
  "run_id": "order_monitor-20260514T165237-6aef2461",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```
## Outcome Tracker — 2026-05-14T16:52:38Z

**Run ID:** `outcome_tracker-20260514T165238-45a1b2a9`  **Outcomes tracked:** 8

- WELL BUY (entry) fill=$218.808 return=-0.289% unpl=$-0.0723 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.001% unpl=$+0.0148 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.457% unpl=$-0.0348 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-0.008% unpl=$-0.0348 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=+0.090% unpl=$-0.0348 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=+0.093% unpl=$-0.0348 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=+0.058% unpl=$+0.0148 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=-0.001% unpl=$-0.0002 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T17:02:39Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260514T170239-fe8b6ff7",
  "run_id": "execution-20260514T170239-335e20a8",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "3278197a27685b6da5509014ad72529f10feab776dbb0f7cb6e88a770cb5d968"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T17:13:40Z",
  "run_id": "execution-20260514T171340-58eec722",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "cd6f3302806a58c135f41c96e8bd8b67a693bfc36ed765be259a62b9851297b1",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.0103078,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## order_cancel

**run_id:** `order_cancel-20260514T171410-9dd5e164`  
**cancelled_at:** 2026-05-14T17:14:10Z  
**symbol:** EQIX  
**side:** buy  
**status_before_cancel:** new  
**client_order_id:** `TOS-20260514T163113-EQIX-BUY`  
**broker_order_id:** `cc380d6e-9b8f-4429-8f91-a7907b0c570f`  
**confirmed_by:** operator (confirm_cancel='CANCEL')  
**notes:** —  


## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T17:15:13Z",
  "run_id": "execution-20260514T171513-a0d602b3",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "60d6bbb20f6c58d7d3f30c291c786ea28169d8fa6a182ee884f1740a07196e6b",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.01077,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T17:44:12Z",
  "run_id": "execution-20260514T174412-3bcc3746",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "f624730e79078a07e1406fff1683ffe0fc6799fbd9dc97bbfd0dd13ad8623974",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.012085833333333332,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T17:44:32Z",
  "run_id": "execution-20260514T174431-c680b4c7",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "1c44699f9c375ad7451f9c49d4df19b7f644466beff077c926cc8c1c25b2f584",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.01630865,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T17:44:40Z",
  "run_id": "execution-20260514T174440-29ee98e8",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "48df7c6dab6861085f4eb8a15f852523ac2ad0f88baf1dd0dbe8034e94e1fdfb",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.017061766666666665,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T17:44:47Z",
  "run_id": "execution-20260514T174447-fffb1ea0",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "5708f350b5319f8d815ed0654a260c92b5982e4b190a059b79a6bf6aef1c6bba",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.01042055,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T17:44:55Z",
  "run_id": "execution-20260514T174455-47e63594",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "6c9fb776d5298d5b156427c20765657a3e6b85660e452126fed9a57452b42140",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.017233916666666668,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T18:54:19Z",
  "run_id": "execution-20260514T185418-5edfe1b3",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "74bcc8e5c1c04f7d6c87d4a1ef30006828042f58d07f37c354648a12e53fb8a9",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.016437216666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T18:54:25Z",
  "run_id": "execution-20260514T185425-c147510c",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "1b6933ffd3d85a3e978eaec04c5505e50d6d4c7fc73a04209ea8930e4b4ce09d",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.006481333333333334,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T18:54:32Z",
  "run_id": "execution-20260514T185432-2c31b225",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "aa77633fea3206ecde60d80b9f49bdbab55b33439e0c618abf46b0f79804bb96",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.013920766666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T18:54:38Z",
  "run_id": "execution-20260514T185438-75b1a1b9",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "c8dc6280eb24ede06961c39005675bfb1ec057e43bacb483efbfc5e377f0b596",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.012523466666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T19:05:22Z",
  "run_id": "execution-20260514T190522-f9bf1294",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "f66a5217f64131fd022979cbc7949258eeb21874ed13fc5bd988e06b1e228057",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.011881933333333334,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-14T19:05:35Z",
  "run_id": "execution-20260514T190534-99c0e772",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "9b93275ed432b28ebc5ee76dee6d40efc6c8c8ad1871103df256ca47bf361bb3",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.016473883333333335,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T21:43:39Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260514T214339-37c245a5",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-14T21:49:46Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260514T214946-f5d4b8ea",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-14T21:49:47Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 0,
  "orders_validated": 0,
  "plan_id": "trade_plan-20260514T214947-b0ee5f7f",
  "run_id": "execution-20260514T214947-fbdb271b",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "b4be96ec377ae43499ac5ec319ff8857c77ad3dc5c71e153dde2fa9988dec396"
}
```
## Outcome Tracker — 2026-05-14T21:49:47Z

**Run ID:** `outcome_tracker-20260514T214947-34139ff6`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-0.483% unpl=$-0.1209 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.240% unpl=$+0.2164 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.432% unpl=$+0.1544 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=+0.017% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=+0.115% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=+0.118% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=+0.297% unpl=$+0.2164 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=+0.162% unpl=$+0.0435 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=+0.012% unpl=$+0.0435 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=+0.259% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=+0.266% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=+0.329% unpl=$+0.2164 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=+0.275% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=+0.291% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---
## Outcome Tracker — 2026-05-14T22:12:20Z

**Run ID:** `outcome_tracker-20260514T221220-d3c04dca`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-0.483% unpl=$-0.1209 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.240% unpl=$+0.2164 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.432% unpl=$+0.1544 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=+0.017% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=+0.115% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=+0.118% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=+0.297% unpl=$+0.2164 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=+0.162% unpl=$+0.0435 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=+0.012% unpl=$+0.0435 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=+0.259% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=+0.266% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=+0.329% unpl=$+0.2164 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=+0.275% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=+0.291% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---
## Outcome Tracker — 2026-05-14T22:32:38Z

**Run ID:** `outcome_tracker-20260514T223238-4f7bae5c`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-0.483% unpl=$-0.1209 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.240% unpl=$+0.2164 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.432% unpl=$+0.1544 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=+0.017% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=+0.115% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=+0.118% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=+0.297% unpl=$+0.2164 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=+0.162% unpl=$+0.0435 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=+0.012% unpl=$+0.0435 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=+0.259% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=+0.266% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=+0.329% unpl=$+0.2164 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=+0.275% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=+0.291% unpl=$+0.1544 | pending: same_day, 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-15T17:00:34Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260515T170034-464b80d0",
  "run_id": "execution-20260515T170034-7c6f8c41",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "11d3cc9d568c8833c6a343130193991badb4ed1dd82aaae5fc5d031e74619b3f"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-15T21:33:40Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260515T213340-645ea594",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-15T21:41:03Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260515T214103-e9236256",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "QUOTE_FRESHNESS"
  ],
  "generated_at": "2026-05-15T21:41:04Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260515T214104-7822211e",
  "run_id": "execution-20260515T214104-6e56ad0c",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "957e93e3c85241af3a639b53959d4b74d7bc86bf0e9174d78a72b2accbd3d9b0"
}
```
## Outcome Tracker — 2026-05-15T21:41:04Z

**Run ID:** `outcome_tracker-20260515T214104-e7913778`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-2.316% unpl=$-0.5790 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-1.248% unpl=$-0.8996 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-2.247% unpl=$-1.6335 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-1.806% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-1.710% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-1.707% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=-1.191% unpl=$-0.8996 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=-0.367% unpl=$-0.2209 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=-0.516% unpl=$-0.2209 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=-1.568% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=-1.562% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=-1.160% unpl=$-0.8996 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=-1.553% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=-1.537% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---
## Outcome Tracker — 2026-05-15T22:00:12Z

**Run ID:** `outcome_tracker-20260515T220012-2f7844b8`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-2.316% unpl=$-0.5790 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-1.248% unpl=$-0.8996 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-2.247% unpl=$-1.6335 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-1.806% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-1.710% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-1.707% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=-1.191% unpl=$-0.8996 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=-0.367% unpl=$-0.2209 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=-0.516% unpl=$-0.2209 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=-1.568% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=-1.562% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=-1.160% unpl=$-0.8996 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=-1.553% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=-1.537% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---
## Outcome Tracker — 2026-05-15T22:13:15Z

**Run ID:** `outcome_tracker-20260515T221315-6e75adb7`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-2.316% unpl=$-0.5790 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-1.248% unpl=$-0.8996 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-2.247% unpl=$-1.6335 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-1.806% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-1.710% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-1.707% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=-1.191% unpl=$-0.8996 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=-0.367% unpl=$-0.2209 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=-0.516% unpl=$-0.2209 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=-1.568% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=-1.562% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=-1.160% unpl=$-0.8996 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=-1.553% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=-1.537% unpl=$-1.6335 | pending: 1_trading_day, 5_trading_days, 20_trading_days, 63_trading_days

---

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-18T17:36:46Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260518T173646-f9444299",
  "run_id": "execution-20260518T173646-6e2a5b63",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "724617b3ce4cc40684fd6d5a3d82eaf0394eae20c76ce5058af2a11a1e96fae2"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-18T21:45:53Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260518T214553-6f6f808a",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-18T21:50:58Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260518T215058-f205abfc",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "QUOTE_FRESHNESS"
  ],
  "generated_at": "2026-05-18T21:50:59Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260518T215059-e7e56c9f",
  "run_id": "execution-20260518T215059-d65e28f1",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "3d596d5db42aa0cfdf908878568a57687342cf1b2e5e3195daeb636ef5b1c4fc"
}
```
## Outcome Tracker — 2026-05-18T21:50:59Z

**Run ID:** `outcome_tracker-20260518T215059-9cc946e9`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-2.833% unpl=$-0.7082 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-0.594% unpl=$-0.4093 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-2.006% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-1.564% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-1.467% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-1.464% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=-0.537% unpl=$-0.4093 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=+0.744% unpl=$+0.3343 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=+0.593% unpl=$+0.3343 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=-1.325% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=-1.319% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=-0.506% unpl=$-0.4093 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=-1.309% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=-1.293% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days

---
## Outcome Tracker — 2026-05-18T22:03:49Z

**Run ID:** `outcome_tracker-20260518T220349-6b6f1b32`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-2.833% unpl=$-0.7082 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-0.594% unpl=$-0.4093 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-2.006% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-1.564% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-1.467% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-1.464% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=-0.537% unpl=$-0.4093 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=+0.744% unpl=$+0.3343 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=+0.593% unpl=$+0.3343 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=-1.325% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=-1.319% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=-0.506% unpl=$-0.4093 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=-1.309% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=-1.293% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days

---
## Outcome Tracker — 2026-05-18T22:15:28Z

**Run ID:** `outcome_tracker-20260518T221528-a5d89d8f`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-2.833% unpl=$-0.7082 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-0.594% unpl=$-0.4093 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-2.006% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-1.564% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-1.467% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-1.464% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=-0.537% unpl=$-0.4093 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=+0.744% unpl=$+0.3343 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=+0.593% unpl=$+0.3343 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=-1.325% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=-1.319% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=-0.506% unpl=$-0.4093 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=-1.309% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=-1.293% unpl=$-1.3908 | pending: 5_trading_days, 20_trading_days, 63_trading_days

---

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-19T17:42:09Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260519T174209-4e1098cc",
  "run_id": "execution-20260519T174209-b52e702f",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "9a4c7fbc4d10591d1e9d3495321581034bbecedceded72a2aec8b0798b0c9622"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-19T21:53:56Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260519T215356-6135bd03",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-19T22:00:13Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260519T220013-6d911730",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "QUOTE_FRESHNESS"
  ],
  "generated_at": "2026-05-19T22:00:14Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260519T220014-e0847b4b",
  "run_id": "execution-20260519T220014-65d972d2",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "e39f980acdc25f842be9c157049cca1b53f7754e8ca5259060d8a78c0b4811c4"
}
```
## Outcome Tracker — 2026-05-19T22:00:14Z

**Run ID:** `outcome_tracker-20260519T220014-2791b0ae`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-0.369% unpl=$-0.0923 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-0.292% unpl=$-0.1828 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-3.262% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-2.825% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-2.730% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-2.727% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=-0.235% unpl=$-0.1828 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=+1.447% unpl=$+0.6856 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=+1.295% unpl=$+0.6856 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=-2.590% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=-2.583% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=-0.204% unpl=$-0.1828 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=-2.574% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=-2.558% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days

---
## Outcome Tracker — 2026-05-19T22:17:18Z

**Run ID:** `outcome_tracker-20260519T221718-6eb465ae`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-0.369% unpl=$-0.0923 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-0.292% unpl=$-0.1828 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-3.262% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-2.825% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-2.730% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-2.727% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=-0.235% unpl=$-0.1828 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=+1.447% unpl=$+0.6856 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=+1.295% unpl=$+0.6856 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=-2.590% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=-2.583% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=-0.204% unpl=$-0.1828 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=-2.574% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=-2.558% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days

---
## Outcome Tracker — 2026-05-19T22:40:20Z

**Run ID:** `outcome_tracker-20260519T224020-0db7e321`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-0.369% unpl=$-0.0923 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-0.292% unpl=$-0.1828 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-3.262% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-2.825% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-2.730% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-2.727% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=-0.235% unpl=$-0.1828 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=+1.447% unpl=$+0.6856 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=+1.295% unpl=$+0.6856 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=-2.590% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=-2.583% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=-0.204% unpl=$-0.1828 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=-2.574% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=-2.558% unpl=$-2.6527 | pending: 5_trading_days, 20_trading_days, 63_trading_days

---

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-20T18:01:55Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260520T180155-b07c14e5",
  "run_id": "execution-20260520T180155-2c1cca10",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "a293e0d6495f0f5baac5d99b4eb3ac1ef50205bbdfd66e6e6d9d2cc5c52e783a"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-20T22:10:19Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260520T221019-bf6c5c89",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-20T22:15:22Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260520T221522-c13c2584",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "QUOTE_FRESHNESS"
  ],
  "generated_at": "2026-05-20T22:15:23Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260520T221523-26202569",
  "run_id": "execution-20260520T221523-122ec062",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "cb72b95e5504ce0eab327e8d7a8c0f5c6daf73f0e807c49dd2286937f03d4580"
}
```
## Outcome Tracker — 2026-05-20T22:15:23Z

**Run ID:** `outcome_tracker-20260520T221523-9ded7818`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-0.374% unpl=$-0.0935 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-0.420% unpl=$-0.2790 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-1.971% unpl=$-1.3556 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-1.528% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-1.432% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-1.429% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=-0.363% unpl=$-0.2790 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=-0.768% unpl=$-0.4211 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=-0.916% unpl=$-0.4211 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=-1.290% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=-1.283% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=-0.332% unpl=$-0.2790 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=-1.274% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=-1.258% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days

---
## Outcome Tracker — 2026-05-20T22:24:31Z

**Run ID:** `outcome_tracker-20260520T222431-6880f16d`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-0.374% unpl=$-0.0935 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-0.420% unpl=$-0.2790 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-1.971% unpl=$-1.3556 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-1.528% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-1.432% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-1.429% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=-0.363% unpl=$-0.2790 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=-0.768% unpl=$-0.4211 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=-0.916% unpl=$-0.4211 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=-1.290% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=-1.283% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=-0.332% unpl=$-0.2790 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=-1.274% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=-1.258% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days

---
## Outcome Tracker — 2026-05-20T22:45:32Z

**Run ID:** `outcome_tracker-20260520T224532-a4da27d9`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-0.374% unpl=$-0.0935 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=-0.420% unpl=$-0.2790 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-1.971% unpl=$-1.3556 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-1.528% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-1.432% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-1.429% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=-0.363% unpl=$-0.2790 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=-0.768% unpl=$-0.4211 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=-0.916% unpl=$-0.4211 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=-1.290% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=-1.283% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=-0.332% unpl=$-0.2790 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=-1.274% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=-1.258% unpl=$-1.3556 | pending: 5_trading_days, 20_trading_days, 63_trading_days

---

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-21T17:34:34Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260521T173434-a21e2578",
  "run_id": "execution-20260521T173434-bc0ad1a2",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "c8779fae43e9ba3e8e35d0cbb6f59956addfecbd3a8e50799b85aa1d63712e9b"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-21T21:56:38Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260521T215638-e7cb9024",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-21T22:05:33Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260521T220533-8df90e99",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "QUOTE_FRESHNESS"
  ],
  "generated_at": "2026-05-21T22:05:34Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260521T220533-65e68056",
  "run_id": "execution-20260521T220534-88285473",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "7f9a6ab0b248aa8668267f24ee47659141ca7e414c4c279bd335af56d1e6051d"
}
```
## Outcome Tracker — 2026-05-21T22:05:34Z

**Run ID:** `outcome_tracker-20260521T220534-9e42e720`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-1.279% unpl=$-0.3197 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.622% unpl=$+0.5032 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-1.056% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-0.609% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-0.512% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-0.509% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=+0.680% unpl=$+0.5032 | pending: 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=-7.920% unpl=$-3.9943 | pending: 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=-8.057% unpl=$-3.9943 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=-0.369% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=-0.362% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=+0.711% unpl=$+0.5032 | pending: 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=-0.353% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=-0.336% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days

---
## Outcome Tracker — 2026-05-21T22:19:51Z

**Run ID:** `outcome_tracker-20260521T221951-2d32a116`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-1.279% unpl=$-0.3197 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.622% unpl=$+0.5032 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-1.056% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-0.609% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-0.512% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-0.509% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=+0.680% unpl=$+0.5032 | pending: 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=-7.920% unpl=$-3.9943 | pending: 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=-8.057% unpl=$-3.9943 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=-0.369% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=-0.362% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=+0.711% unpl=$+0.5032 | pending: 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=-0.353% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=-0.336% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days

---
## Outcome Tracker — 2026-05-21T22:43:49Z

**Run ID:** `outcome_tracker-20260521T224349-b468dff4`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-1.279% unpl=$-0.3197 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+0.622% unpl=$+0.5032 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-1.056% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=-0.609% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=-0.512% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=-0.509% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=+0.680% unpl=$+0.5032 | pending: 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=-7.920% unpl=$-3.9943 | pending: 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=-8.057% unpl=$-3.9943 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=-0.369% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=-0.362% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=+0.711% unpl=$+0.5032 | pending: 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=-0.353% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=-0.336% unpl=$-0.4365 | pending: 20_trading_days, 63_trading_days

---

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-22T17:18:06Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260522T171806-14da032e",
  "run_id": "execution-20260522T171806-f78bf495",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "03cd40865aebd83dd1b86ca16d131f4371c6c580ad55fa17aa7cfc78ff932f8d"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-22T21:41:55Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260522T214155-0b6c69a2",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-22T21:51:47Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260522T215147-6804bf7b",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "QUOTE_FRESHNESS"
  ],
  "generated_at": "2026-05-22T21:51:48Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260522T215148-d536c070",
  "run_id": "execution-20260522T215148-eb37f028",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "8db71d56c0f50fa3abfeb55972339d7389583d6c2496abbb671e8763c4d6bbe5"
}
```
## Outcome Tracker — 2026-05-22T21:51:48Z

**Run ID:** `outcome_tracker-20260522T215148-7373ee95`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-1.206% unpl=$-0.3014 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+1.782% unpl=$+1.3733 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.422% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=+0.027% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=+0.125% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=+0.128% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=+1.840% unpl=$+1.3733 | pending: 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=-9.228% unpl=$-4.6478 | pending: 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=-9.363% unpl=$-4.6478 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=+0.269% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=+0.276% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=+1.872% unpl=$+1.3733 | pending: 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=+0.285% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=+0.302% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days

---
## Outcome Tracker — 2026-05-22T22:08:26Z

**Run ID:** `outcome_tracker-20260522T220826-2b8c11a4`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-1.206% unpl=$-0.3014 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+1.782% unpl=$+1.3733 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.422% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=+0.027% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=+0.125% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=+0.128% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=+1.840% unpl=$+1.3733 | pending: 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=-9.228% unpl=$-4.6478 | pending: 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=-9.363% unpl=$-4.6478 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=+0.269% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=+0.276% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=+1.872% unpl=$+1.3733 | pending: 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=+0.285% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=+0.302% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days

---
## Outcome Tracker — 2026-05-22T22:17:19Z

**Run ID:** `outcome_tracker-20260522T221719-939a8e03`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-1.206% unpl=$-0.3014 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+1.782% unpl=$+1.3733 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.422% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=+0.027% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=+0.125% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=+0.128% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=+1.840% unpl=$+1.3733 | pending: 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=-9.228% unpl=$-4.6478 | pending: 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=-9.363% unpl=$-4.6478 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=+0.269% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=+0.276% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=+1.872% unpl=$+1.3733 | pending: 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=+0.285% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=+0.302% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days

---

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "QUOTE_FRESHNESS"
  ],
  "generated_at": "2026-05-25T17:16:29Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260525T171629-29e54862",
  "run_id": "execution-20260525T171629-df99f728",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "ad6a21d62b9116078c78cd7fcf257abbebf9cd56be06b38b924ad9727c04c6f7"
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-25T21:43:23Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260525T214323-e810dd75",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## order_monitor run

```json
{
  "dry_run": false,
  "generated_at": "2026-05-25T21:50:49Z",
  "lifecycles": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "fill": {
        "fill_price": 218.808,
        "filled_at": "2026-05-13T16:00:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.11425542,
        "plan_id": "trade_plan-20260513T160035-0460e121",
        "position_confirmed": true,
        "run_id": "execution-20260513T160036-b4ad22c3",
        "trade_plan_hash": "d2b6605f29eb01f901b86e39fae682ac50c753d4f21ec3b665c106f98a6553b8",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WELL"
    },
    {
      "client_order_id": "TOS-20260513T192526-JNJ-BUY",
      "fill": {
        "fill_price": 230.248,
        "filled_at": "2026-05-13T19:25:31Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108578576,
        "plan_id": "trade_plan-20260513T192526-c793d98e",
        "position_confirmed": true,
        "run_id": "execution-20260513T192527-04dacaf4",
        "trade_plan_hash": "3343469f0673de3e6bfa138d5fddf1872ebc07a6a095b933abef3e886cc6456e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260513T192934-EQIX-BUY",
      "fill": {
        "fill_price": 1084.37,
        "filled_at": "2026-05-13T19:31:19Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023054861,
        "plan_id": "trade_plan-20260513T192934-3bac0e2c",
        "position_confirmed": true,
        "run_id": "execution-20260513T192935-303e6fbe",
        "trade_plan_hash": "c58aacec17f13c901a86b5101366f9f2587ec9e60aad8e68023e07db9612f0a2",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T145625-EQIX-BUY",
      "fill": {
        "fill_price": 1079.5,
        "filled_at": "2026-05-14T15:41:11Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023158869,
        "plan_id": "trade_plan-20260514T145625-7807f306",
        "position_confirmed": true,
        "run_id": "execution-20260514T145626-8a29a24f",
        "trade_plan_hash": "0298a30202102127b52b6753d2da05a0487667e088f90a3d2d9482a05d85aa0e",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154323-JNJ-BUY",
      "fill": {
        "fill_price": 230.116,
        "filled_at": "2026-05-14T16:34:23Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108640859,
        "plan_id": "trade_plan-20260514T154323-1f27d10d",
        "position_confirmed": true,
        "run_id": "execution-20260514T154324-0732af2c",
        "trade_plan_hash": "edd636a80898a01f62b9b46ed9b5b299a0053880453e9ddd02b20b4455da68a0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T154543-EQIX-SELL",
      "fill": {
        "fill_price": 1078.442,
        "filled_at": "2026-05-14T15:47:26Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023181589,
        "plan_id": "trade_plan-20260514T154543-b29ff94f",
        "position_confirmed": true,
        "run_id": "execution-20260514T154544-c2e241e8",
        "trade_plan_hash": "e509327fb66887dc158535967804ce7b8cee093ad40cdb65eab52e988f7e7c09",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T154817-EQIX-BUY",
      "fill": {
        "fill_price": 1078.41,
        "filled_at": "2026-05-14T16:01:36Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023182277,
        "plan_id": "trade_plan-20260514T154817-6a53654a",
        "position_confirmed": true,
        "run_id": "execution-20260514T154818-6157fada",
        "trade_plan_hash": "ec58d5499d6c8e52e3dd98e59782bcadc67f53d6dd35a04402e561cad33b77c3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T163113-EQIX-BUY",
      "fill": {
        "fill_price": 1076.89,
        "filled_at": "2026-05-14T17:20:40Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023214998,
        "plan_id": "trade_plan-20260514T163113-1c676d38",
        "position_confirmed": true,
        "run_id": "execution-20260514T163114-dd6029a9",
        "trade_plan_hash": "8ac7328c69c7cd0377af0133e8092381d3d9da649baea5bb5bda660ccdd83c2b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T165232-WMT-BUY",
      "fill": {
        "fill_price": 132.276,
        "filled_at": "2026-05-14T16:52:33Z",
        "filled_notional": 25.0,
        "filled_qty": 0.18899876,
        "plan_id": "trade_plan-20260514T165232-1f83cea2",
        "position_confirmed": true,
        "run_id": "execution-20260514T165233-adcb0da2",
        "trade_plan_hash": "c70b9817dd2fee23f677bbe06d26888ba6cf1888fe01c1fe1e0b7d542ee8342b",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T171739-JNJ-BUY",
      "fill": {
        "fill_price": 230.044,
        "filled_at": "2026-05-14T17:21:14Z",
        "filled_notional": 25.0,
        "filled_qty": 0.108674862,
        "plan_id": "trade_plan-20260514T171739-65285f83",
        "position_confirmed": true,
        "run_id": "execution-20260514T171740-77316146",
        "trade_plan_hash": "7ada198bc1596edefd21961d1f742195c9eead499fb75189bf15f965928dfe2f",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "JNJ"
    },
    {
      "client_order_id": "TOS-20260514T171844-WMT-BUY",
      "fill": {
        "fill_price": 132.474,
        "filled_at": "2026-05-14T17:20:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.188716276,
        "plan_id": "trade_plan-20260514T171844-6adf1380",
        "position_confirmed": true,
        "run_id": "execution-20260514T171846-d8b15803",
        "trade_plan_hash": "a0c973a51e85f59bd52d56c0d86f0df521a6a9ab142199800e2bfa7924e15360",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "WMT"
    },
    {
      "client_order_id": "TOS-20260514T172103-EQIX-BUY",
      "fill": {
        "fill_price": 1076.82,
        "filled_at": "2026-05-14T17:21:04Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023216507,
        "plan_id": "trade_plan-20260514T172103-835a36b9",
        "position_confirmed": true,
        "run_id": "execution-20260514T172104-b71591c3",
        "trade_plan_hash": "8b234ba2cc064e0cd75f91347d7261bf2de849e45a72c7bcddd3b232d31c2fe3",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172226-EQIX-SELL",
      "fill": {
        "fill_price": 1076.718,
        "filled_at": "2026-05-14T17:23:27Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023218707,
        "plan_id": "trade_plan-20260514T172226-ed557b0a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172227-c20719b0",
        "trade_plan_hash": "1177c0ee9807237a73f6a670c0d6a961753770caef2dc15bfd2466ef0d6bc0cc",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "sell",
      "symbol": "EQIX"
    },
    {
      "client_order_id": "TOS-20260514T172335-EQIX-BUY",
      "fill": {
        "fill_price": 1076.542,
        "filled_at": "2026-05-14T17:26:29Z",
        "filled_notional": 25.0,
        "filled_qty": 0.023222503,
        "plan_id": "trade_plan-20260514T172335-e46d4d8a",
        "position_confirmed": true,
        "run_id": "execution-20260514T172337-37cce12a",
        "trade_plan_hash": "be22bcde61b16718328b9c6215e426c7b4d2d3080b3671e392278d67b30b7ee0",
        "trigger_snapshot_hash": null
      },
      "lifecycle_status": "filled",
      "notional": 25.0,
      "side": "buy",
      "symbol": "EQIX"
    }
  ],
  "orders_active": 0,
  "orders_filled": 14,
  "orders_missing": 0,
  "orders_rejected": 0,
  "orders_tracked": 14,
  "run_id": "order_monitor-20260525T215049-78aa7d84",
  "source": "alpaca_paper",
  "stale_orders": [],
  "warnings": []
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "QUOTE_FRESHNESS"
  ],
  "generated_at": "2026-05-25T21:50:50Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260525T215050-9fe086a0",
  "run_id": "execution-20260525T215050-7b499df9",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "b48d0e19becd3562e3f33ae0be585556912348aaa1e85de1c7223c51561ec311"
}
```
## Outcome Tracker — 2026-05-25T21:50:50Z

**Run ID:** `outcome_tracker-20260525T215050-24e09eed`  **Outcomes tracked:** 14

- WELL BUY (entry) fill=$218.808 return=-1.206% unpl=$-0.3014 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.248 return=+1.777% unpl=$+1.3701 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1084.37 return=-0.422% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1079.5 return=+0.027% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1078.442 return=+0.125% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1078.41 return=+0.128% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.116 return=+1.836% unpl=$+1.3701 | pending: 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.276 return=-9.076% unpl=$-4.5722 | pending: 20_trading_days, 63_trading_days
- WMT BUY (entry) fill=$132.474 return=-9.212% unpl=$-4.5722 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.89 return=+0.269% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.82 return=+0.276% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- JNJ BUY (entry) fill=$230.044 return=+1.868% unpl=$+1.3701 | pending: 20_trading_days, 63_trading_days
- EQIX SELL (exit) fill=$1076.718 return=+0.285% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days
- EQIX BUY (entry) fill=$1076.542 return=+0.302% unpl=$+0.2000 | pending: 20_trading_days, 63_trading_days

---
