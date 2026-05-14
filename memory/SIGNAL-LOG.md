# Signal Log

Candidate ranking, trade-plan generation, and no-trade reasons are logged here.

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T153120-a8d76fc7",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T153120-b24052c1",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "3db855f6bc252467eed8d7675c053c1b94dddde0c5ae7bf5ada481935cd557be"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T153129-62645e34",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T153129-9869c4d7",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "781e14195cfc473146586404e3c3d9e8b38a2f06bfad35867b68bb43f158a0ed"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T153253-d75f00af",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T153253-0f139ccb",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "acc6818ef018c8530abf46de23e1ffc4400a4dbbb91ce543fda54c6929e4ca0e"
}
```

## Trade plan generated

```json
{
  "approval_status": "BLOCKED",
  "candidate_order_count": 11,
  "failed_gates": [
    "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER"
  ],
  "run_id": "trade_plan-20260512T153300-41352dc4",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "66e19502a46c261f9951c0a598c6ff33647003f663b581b39f96e00fec45a5aa"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T153305-2d0c50dd",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T153305-8ba0bff3",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "209321ee8bfc8308e88d3f37670894bc67fdc87e7ea8621a81b6ded9262aaa5e"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T153311-53c96d1b",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T153311-897f45cf",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "eafa80017fbe07fddac1b2e89bb027ea4845eeb38c9940dd532a26d16ed642bb"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T162543-93cf6035",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T162543-0b935930",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "8775d5146cc11c1af1ebf14fdd8b2fa5c4ecdf4f94d15577d3e2bbb212508e12"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T164143-e7366237",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T164143-5d007d4b",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "704c77858eb7b24f9b54c7a1e9924cc05a21a5b37f8bb3f8da5f6fd0bb8e5841"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T165601-127b46b9",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T165601-f14ddffe",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "43c6e75e13b2091d0ef514e42e32c4645ef595f00933206e90df501659d3fdbb"
}
```

## scan_triggers candidates  (2026-05-12T16:56:03Z)

```
  WMT       score=0.2220  atr_pct=0.0109  [SELECTED]
  APD       score=0.2198  atr_pct=0.0114  [SELECTED]
  DIS       score=0.2113  atr_pct=0.0105  [SELECTED]
  ORCL      score=0.2093  atr_pct=0.0103  [SELECTED]
  LLY       score=0.2016  atr_pct=0.0111  [SELECTED]
  BLK       score=0.1996  atr_pct=0.0098  [SELECTED]
  BKNG      score=0.1969  atr_pct=0.0118  [SELECTED]
  KO        score=0.1963  atr_pct=0.0110  [SELECTED]
  WELL      score=0.1905  atr_pct=0.0099  [SELECTED]
  EOG       score=0.1862  atr_pct=0.0102  [SELECTED]
  UNP       score=0.1859  atr_pct=0.0099  [candidate]
  CRM       score=0.1782  atr_pct=0.0104  [candidate]
  PG        score=0.1768  atr_pct=0.0105  [candidate]
  COST      score=0.1717  atr_pct=0.0115  [candidate]
  PEP       score=0.1712  atr_pct=0.0108  [candidate]
  MCD       score=0.1708  atr_pct=0.0111  [candidate]
  XOM       score=0.1671  atr_pct=0.0105  [candidate]
  WFC       score=0.1666  atr_pct=0.0117  [candidate]
  NFLX      score=0.1564  atr_pct=0.0103  [candidate]
  GOOGL     score=0.1557  atr_pct=0.0103  [candidate]
  CL        score=0.1537  atr_pct=0.0102  [candidate]
  AMGN      score=0.1489  atr_pct=0.0099  [candidate]
  MS        score=0.1472  atr_pct=0.0094  [candidate]
  LMT       score=0.1454  atr_pct=0.0105  [candidate]
  ABBV      score=0.1442  atr_pct=0.0116  [candidate]
  INTU      score=0.1425  atr_pct=0.0106  [candidate]
  TSLA      score=0.1422  atr_pct=0.0098  [candidate]
  GS        score=0.1396  atr_pct=0.0103  [candidate]
  HD        score=0.1392  atr_pct=0.0109  [candidate]
  CSCO      score=0.1378  atr_pct=0.0110  [candidate]
  NVDA      score=0.1334  atr_pct=0.0107  [candidate]
  AXP       score=0.1333  atr_pct=0.0111  [candidate]
  BAC       score=0.1318  atr_pct=0.0095  [candidate]
  EQIX      score=0.1316  atr_pct=0.0103  [candidate]
  AAPL      score=0.1295  atr_pct=0.0100  [candidate]
  NKE       score=0.1268  atr_pct=0.0109  [candidate]
  AMT       score=0.1266  atr_pct=0.0109  [candidate]
  AMD       score=0.1264  atr_pct=0.0094  [candidate]
  MSFT      score=0.1260  atr_pct=0.0112  [candidate]
  GE        score=0.1218  atr_pct=0.0112  [candidate]
  DE        score=0.1209  atr_pct=0.0109  [candidate]
  COP       score=0.1205  atr_pct=0.0099  [candidate]
  PLD       score=0.1175  atr_pct=0.0106  [candidate]
  AMZN      score=0.1169  atr_pct=0.0094  [candidate]
  ISRG      score=0.1167  atr_pct=0.0096  [candidate]
  SO        score=0.1155  atr_pct=0.0097  [candidate]
  CMCSA     score=0.1111  atr_pct=0.0120  [candidate]
  SLB       score=0.1033  atr_pct=0.0103  [candidate]
  CVX       score=0.1017  atr_pct=0.0108  [candidate]
  CAT       score=0.1004  atr_pct=0.0095  [candidate]
  ABT       score=0.0984  atr_pct=0.0102  [candidate]
  TMO       score=0.0967  atr_pct=0.0114  [candidate]
  HON       score=0.0966  atr_pct=0.0099  [candidate]
  ECL       score=0.0911  atr_pct=0.0110  [candidate]
  AEP       score=0.0909  atr_pct=0.0102  [candidate]
  META      score=0.0870  atr_pct=0.0105  [candidate]
  LIN       score=0.0845  atr_pct=0.0097  [candidate]
  SHW       score=0.0805  atr_pct=0.0099  [candidate]
  BA        score=0.0774  atr_pct=0.0100  [candidate]
  PM        score=0.0751  atr_pct=0.0108  [candidate]
  SRE       score=0.0718  atr_pct=0.0099  [candidate]
  JPM       score=0.0696  atr_pct=0.0103  [candidate]
  O         score=0.0676  atr_pct=0.0095  [candidate]
  TMUS      score=0.0606  atr_pct=0.0112  [candidate]
  MA        score=0.0588  atr_pct=0.0107  [candidate]
  NEE       score=0.0588  atr_pct=0.0108  [candidate]
  UPS       score=0.0465  atr_pct=0.0117  [candidate]
  UNH       score=0.0403  atr_pct=0.0114  [candidate]
  AVGO      score=0.0366  atr_pct=0.0094  [candidate]
  JNJ       score=0.0301  atr_pct=0.0100  [candidate]
  SBUX      score=0.0298  atr_pct=0.0100  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T170904-8a409ef7",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T170904-f7d8ce6c",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "45e42630febca33310762bd820c61df313580a19f15d3cad2c47422ad66e32af"
}
```

## scan_triggers candidates  (2026-05-12T17:09:22Z)

```
  WMT       score=0.2220  atr_pct=0.0109  [SELECTED]
  APD       score=0.2198  atr_pct=0.0114  [SELECTED]
  DIS       score=0.2113  atr_pct=0.0105  [SELECTED]
  ORCL      score=0.2093  atr_pct=0.0103  [SELECTED]
  LLY       score=0.2016  atr_pct=0.0111  [SELECTED]
  BLK       score=0.1996  atr_pct=0.0098  [SELECTED]
  BKNG      score=0.1969  atr_pct=0.0118  [SELECTED]
  KO        score=0.1963  atr_pct=0.0110  [SELECTED]
  WELL      score=0.1905  atr_pct=0.0099  [SELECTED]
  EOG       score=0.1862  atr_pct=0.0102  [SELECTED]
  UNP       score=0.1859  atr_pct=0.0099  [candidate]
  CRM       score=0.1782  atr_pct=0.0104  [candidate]
  PG        score=0.1768  atr_pct=0.0105  [candidate]
  COST      score=0.1717  atr_pct=0.0115  [candidate]
  PEP       score=0.1712  atr_pct=0.0108  [candidate]
  MCD       score=0.1708  atr_pct=0.0111  [candidate]
  XOM       score=0.1671  atr_pct=0.0105  [candidate]
  WFC       score=0.1666  atr_pct=0.0117  [candidate]
  NFLX      score=0.1564  atr_pct=0.0103  [candidate]
  GOOGL     score=0.1557  atr_pct=0.0103  [candidate]
  CL        score=0.1537  atr_pct=0.0102  [candidate]
  AMGN      score=0.1489  atr_pct=0.0099  [candidate]
  MS        score=0.1472  atr_pct=0.0094  [candidate]
  LMT       score=0.1454  atr_pct=0.0105  [candidate]
  ABBV      score=0.1442  atr_pct=0.0116  [candidate]
  INTU      score=0.1425  atr_pct=0.0106  [candidate]
  TSLA      score=0.1422  atr_pct=0.0098  [candidate]
  GS        score=0.1396  atr_pct=0.0103  [candidate]
  HD        score=0.1392  atr_pct=0.0109  [candidate]
  CSCO      score=0.1378  atr_pct=0.0110  [candidate]
  NVDA      score=0.1334  atr_pct=0.0107  [candidate]
  AXP       score=0.1333  atr_pct=0.0111  [candidate]
  BAC       score=0.1318  atr_pct=0.0095  [candidate]
  EQIX      score=0.1316  atr_pct=0.0103  [candidate]
  AAPL      score=0.1295  atr_pct=0.0100  [candidate]
  NKE       score=0.1268  atr_pct=0.0109  [candidate]
  AMT       score=0.1266  atr_pct=0.0109  [candidate]
  AMD       score=0.1264  atr_pct=0.0094  [candidate]
  MSFT      score=0.1260  atr_pct=0.0112  [candidate]
  GE        score=0.1218  atr_pct=0.0112  [candidate]
  DE        score=0.1209  atr_pct=0.0109  [candidate]
  COP       score=0.1205  atr_pct=0.0099  [candidate]
  PLD       score=0.1175  atr_pct=0.0106  [candidate]
  AMZN      score=0.1169  atr_pct=0.0094  [candidate]
  ISRG      score=0.1167  atr_pct=0.0096  [candidate]
  SO        score=0.1155  atr_pct=0.0097  [candidate]
  CMCSA     score=0.1111  atr_pct=0.0120  [candidate]
  SLB       score=0.1033  atr_pct=0.0103  [candidate]
  CVX       score=0.1017  atr_pct=0.0108  [candidate]
  CAT       score=0.1004  atr_pct=0.0095  [candidate]
  ABT       score=0.0984  atr_pct=0.0102  [candidate]
  TMO       score=0.0967  atr_pct=0.0114  [candidate]
  HON       score=0.0966  atr_pct=0.0099  [candidate]
  ECL       score=0.0911  atr_pct=0.0110  [candidate]
  AEP       score=0.0909  atr_pct=0.0102  [candidate]
  META      score=0.0870  atr_pct=0.0105  [candidate]
  LIN       score=0.0845  atr_pct=0.0097  [candidate]
  SHW       score=0.0805  atr_pct=0.0099  [candidate]
  BA        score=0.0774  atr_pct=0.0100  [candidate]
  PM        score=0.0751  atr_pct=0.0108  [candidate]
  SRE       score=0.0718  atr_pct=0.0099  [candidate]
  JPM       score=0.0696  atr_pct=0.0103  [candidate]
  O         score=0.0676  atr_pct=0.0095  [candidate]
  TMUS      score=0.0606  atr_pct=0.0112  [candidate]
  MA        score=0.0588  atr_pct=0.0107  [candidate]
  NEE       score=0.0588  atr_pct=0.0108  [candidate]
  UPS       score=0.0465  atr_pct=0.0117  [candidate]
  UNH       score=0.0403  atr_pct=0.0114  [candidate]
  AVGO      score=0.0366  atr_pct=0.0094  [candidate]
  JNJ       score=0.0301  atr_pct=0.0100  [candidate]
  SBUX      score=0.0298  atr_pct=0.0100  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T170939-c91a027a",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T170939-ca1e3ddf",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "50ac2d692a66edd4310fcb296642f30c215fed8f5c373fb323d25e6285688d27"
}
```

## scan_triggers candidates  (2026-05-12T17:12:15Z)

```
  WMT       score=0.2220  atr_pct=0.0109  [SELECTED]
  APD       score=0.2198  atr_pct=0.0114  [SELECTED]
  DIS       score=0.2113  atr_pct=0.0105  [SELECTED]
  ORCL      score=0.2093  atr_pct=0.0103  [SELECTED]
  LLY       score=0.2016  atr_pct=0.0111  [SELECTED]
  BLK       score=0.1996  atr_pct=0.0098  [SELECTED]
  BKNG      score=0.1969  atr_pct=0.0118  [SELECTED]
  KO        score=0.1963  atr_pct=0.0110  [SELECTED]
  WELL      score=0.1905  atr_pct=0.0099  [SELECTED]
  EOG       score=0.1862  atr_pct=0.0102  [SELECTED]
  UNP       score=0.1859  atr_pct=0.0099  [candidate]
  CRM       score=0.1782  atr_pct=0.0104  [candidate]
  PG        score=0.1768  atr_pct=0.0105  [candidate]
  COST      score=0.1717  atr_pct=0.0115  [candidate]
  PEP       score=0.1712  atr_pct=0.0108  [candidate]
  MCD       score=0.1708  atr_pct=0.0111  [candidate]
  XOM       score=0.1671  atr_pct=0.0105  [candidate]
  WFC       score=0.1666  atr_pct=0.0117  [candidate]
  NFLX      score=0.1564  atr_pct=0.0103  [candidate]
  GOOGL     score=0.1557  atr_pct=0.0103  [candidate]
  CL        score=0.1537  atr_pct=0.0102  [candidate]
  AMGN      score=0.1489  atr_pct=0.0099  [candidate]
  MS        score=0.1472  atr_pct=0.0094  [candidate]
  LMT       score=0.1454  atr_pct=0.0105  [candidate]
  ABBV      score=0.1442  atr_pct=0.0116  [candidate]
  INTU      score=0.1425  atr_pct=0.0106  [candidate]
  TSLA      score=0.1422  atr_pct=0.0098  [candidate]
  GS        score=0.1396  atr_pct=0.0103  [candidate]
  HD        score=0.1392  atr_pct=0.0109  [candidate]
  CSCO      score=0.1378  atr_pct=0.0110  [candidate]
  NVDA      score=0.1334  atr_pct=0.0107  [candidate]
  AXP       score=0.1333  atr_pct=0.0111  [candidate]
  BAC       score=0.1318  atr_pct=0.0095  [candidate]
  EQIX      score=0.1316  atr_pct=0.0103  [candidate]
  AAPL      score=0.1295  atr_pct=0.0100  [candidate]
  NKE       score=0.1268  atr_pct=0.0109  [candidate]
  AMT       score=0.1266  atr_pct=0.0109  [candidate]
  AMD       score=0.1264  atr_pct=0.0094  [candidate]
  MSFT      score=0.1260  atr_pct=0.0112  [candidate]
  GE        score=0.1218  atr_pct=0.0112  [candidate]
  DE        score=0.1209  atr_pct=0.0109  [candidate]
  COP       score=0.1205  atr_pct=0.0099  [candidate]
  PLD       score=0.1175  atr_pct=0.0106  [candidate]
  AMZN      score=0.1169  atr_pct=0.0094  [candidate]
  ISRG      score=0.1167  atr_pct=0.0096  [candidate]
  SO        score=0.1155  atr_pct=0.0097  [candidate]
  CMCSA     score=0.1111  atr_pct=0.0120  [candidate]
  SLB       score=0.1033  atr_pct=0.0103  [candidate]
  CVX       score=0.1017  atr_pct=0.0108  [candidate]
  CAT       score=0.1004  atr_pct=0.0095  [candidate]
  ABT       score=0.0984  atr_pct=0.0102  [candidate]
  TMO       score=0.0967  atr_pct=0.0114  [candidate]
  HON       score=0.0966  atr_pct=0.0099  [candidate]
  ECL       score=0.0911  atr_pct=0.0110  [candidate]
  AEP       score=0.0909  atr_pct=0.0102  [candidate]
  META      score=0.0870  atr_pct=0.0105  [candidate]
  LIN       score=0.0845  atr_pct=0.0097  [candidate]
  SHW       score=0.0805  atr_pct=0.0099  [candidate]
  BA        score=0.0774  atr_pct=0.0100  [candidate]
  PM        score=0.0751  atr_pct=0.0108  [candidate]
  SRE       score=0.0718  atr_pct=0.0099  [candidate]
  JPM       score=0.0696  atr_pct=0.0103  [candidate]
  O         score=0.0676  atr_pct=0.0095  [candidate]
  TMUS      score=0.0606  atr_pct=0.0112  [candidate]
  MA        score=0.0588  atr_pct=0.0107  [candidate]
  NEE       score=0.0588  atr_pct=0.0108  [candidate]
  UPS       score=0.0465  atr_pct=0.0117  [candidate]
  UNH       score=0.0403  atr_pct=0.0114  [candidate]
  AVGO      score=0.0366  atr_pct=0.0094  [candidate]
  JNJ       score=0.0301  atr_pct=0.0100  [candidate]
  SBUX      score=0.0298  atr_pct=0.0100  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T173526-5a0b79b8",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T173526-e2c36cfc",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "054760162b875c1258d7e9eeb6d0b1da74f538139859fea34e629b163a5ffba4"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T174736-6552a94b",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T174736-a1b02f12",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "e9cf75575fe00cf90f6568e97f76fe4bea47b77312fa7bb892cd85658ba5a8ce"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T174744-672a1dda",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T174744-1e550eb7",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "9552350933e92f326793c4b9c4a89058da4983262fbaf2e4d7d637a4dc3acbee"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T174749-b2ec0d22",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T174749-f20d7b8a",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "4628a115d34f79cc64d7304791ba0900e8048dd093b3510c25141d2ea8d11438"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T174755-7c1eea45",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T174755-afbf73bd",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "f2d9abf471ece7e6cd38bf21fde5354df7916bb0f6119876db4c7be4804b9c21"
}
```

## scan_triggers candidates  (2026-05-12T17:48:33Z)

```
  GOOGL     score=0.9491  atr_pct=0.0237  [SELECTED]
  FCX       score=0.6665  atr_pct=0.0403  [SELECTED]
  AVGO      score=0.5782  atr_pct=0.0345  [SELECTED]
  SLB       score=0.5660  atr_pct=0.0300  [SELECTED]
  CSCO      score=0.5172  atr_pct=0.0230  [SELECTED]
  NVDA      score=0.5170  atr_pct=0.0300  [candidate]
  GS        score=0.4243  atr_pct=0.0247  [SELECTED]
  XOM       score=0.3473  atr_pct=0.0287  [SELECTED]
  COP       score=0.3364  atr_pct=0.0305  [candidate]
  WMT       score=0.3101  atr_pct=0.0200  [SELECTED]
  WELL      score=0.3010  atr_pct=0.0214  [SELECTED]
  AAPL      score=0.2889  atr_pct=0.0208  [candidate]
  SBUX      score=0.2886  atr_pct=0.0239  [SELECTED]
  CVX       score=0.2764  atr_pct=0.0253  [candidate]
  EQIX      score=0.2754  atr_pct=0.0189  [candidate]
  NEE       score=0.2320  atr_pct=0.0224  [candidate]
  AMZN      score=0.2253  atr_pct=0.0253  [candidate]
  AEP       score=0.1712  atr_pct=0.0177  [candidate]
  APD       score=0.1443  atr_pct=0.0203  [candidate]
  KO        score=0.1356  atr_pct=0.0163  [candidate]
  SRE       score=0.1246  atr_pct=0.0194  [candidate]
  PEP       score=0.1145  atr_pct=0.0210  [candidate]
  O         score=0.1006  atr_pct=0.0149  [candidate]
  COST      score=0.0588  atr_pct=0.0179  [candidate]
  UPS       score=0.0283  atr_pct=0.0278  [candidate]
  SO        score=0.0270  atr_pct=0.0167  [candidate]
  DUK       score=0.0266  atr_pct=0.0159  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T182353-5a204b8c",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T182353-bba8978c",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "da79f7820b51fca182ae899b675e835f364d36d715dceb7f61e8a03e743aac18"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T182413-c87504bc",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T182413-d4616757",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "b024ae27bcc8ba7a0baf5470ce2eb62124ac106003f72af751fe2b68ecf80774"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T182419-d8a02546",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T182419-6fd89431",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "4529428e6110412e5bc4302d23693624cb2220b56fc4a5242852761876af8bbc"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T182424-5c7b57b9",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T182424-19cea115",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "c582a4e5785e46172c36164d9103016ea752b9b87025b41039ea8d6c8bfda988"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T182431-656c59ab",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T182431-519fd26f",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "4abd85771a1f7a0f6d4e38c0b0769d266624c681fc90de71ce6841f653731c15"
}
```

## scan_triggers candidates  (2026-05-12T18:24:45Z)

```
  WMT       score=0.2220  atr_pct=0.0109  [SELECTED]
  APD       score=0.2198  atr_pct=0.0114  [SELECTED]
  DIS       score=0.2113  atr_pct=0.0105  [SELECTED]
  ORCL      score=0.2093  atr_pct=0.0103  [SELECTED]
  LLY       score=0.2016  atr_pct=0.0111  [SELECTED]
  BLK       score=0.1996  atr_pct=0.0098  [SELECTED]
  BKNG      score=0.1969  atr_pct=0.0118  [SELECTED]
  KO        score=0.1963  atr_pct=0.0110  [SELECTED]
  WELL      score=0.1905  atr_pct=0.0099  [SELECTED]
  EOG       score=0.1862  atr_pct=0.0102  [SELECTED]
  UNP       score=0.1859  atr_pct=0.0099  [candidate]
  CRM       score=0.1782  atr_pct=0.0104  [candidate]
  PG        score=0.1768  atr_pct=0.0105  [candidate]
  COST      score=0.1717  atr_pct=0.0115  [candidate]
  PEP       score=0.1712  atr_pct=0.0108  [candidate]
  MCD       score=0.1708  atr_pct=0.0111  [candidate]
  XOM       score=0.1671  atr_pct=0.0105  [candidate]
  WFC       score=0.1666  atr_pct=0.0117  [candidate]
  NFLX      score=0.1564  atr_pct=0.0103  [candidate]
  GOOGL     score=0.1557  atr_pct=0.0103  [candidate]
  CL        score=0.1537  atr_pct=0.0102  [candidate]
  AMGN      score=0.1489  atr_pct=0.0099  [candidate]
  MS        score=0.1472  atr_pct=0.0094  [candidate]
  LMT       score=0.1454  atr_pct=0.0105  [candidate]
  ABBV      score=0.1442  atr_pct=0.0116  [candidate]
  INTU      score=0.1425  atr_pct=0.0106  [candidate]
  TSLA      score=0.1422  atr_pct=0.0098  [candidate]
  GS        score=0.1396  atr_pct=0.0103  [candidate]
  HD        score=0.1392  atr_pct=0.0109  [candidate]
  CSCO      score=0.1378  atr_pct=0.0110  [candidate]
  NVDA      score=0.1334  atr_pct=0.0107  [candidate]
  AXP       score=0.1333  atr_pct=0.0111  [candidate]
  BAC       score=0.1318  atr_pct=0.0095  [candidate]
  EQIX      score=0.1316  atr_pct=0.0103  [candidate]
  AAPL      score=0.1295  atr_pct=0.0100  [candidate]
  NKE       score=0.1268  atr_pct=0.0109  [candidate]
  AMT       score=0.1266  atr_pct=0.0109  [candidate]
  AMD       score=0.1264  atr_pct=0.0094  [candidate]
  MSFT      score=0.1260  atr_pct=0.0112  [candidate]
  GE        score=0.1218  atr_pct=0.0112  [candidate]
  DE        score=0.1209  atr_pct=0.0109  [candidate]
  COP       score=0.1205  atr_pct=0.0099  [candidate]
  PLD       score=0.1175  atr_pct=0.0106  [candidate]
  AMZN      score=0.1169  atr_pct=0.0094  [candidate]
  ISRG      score=0.1167  atr_pct=0.0096  [candidate]
  SO        score=0.1155  atr_pct=0.0097  [candidate]
  CMCSA     score=0.1111  atr_pct=0.0120  [candidate]
  SLB       score=0.1033  atr_pct=0.0103  [candidate]
  CVX       score=0.1017  atr_pct=0.0108  [candidate]
  CAT       score=0.1004  atr_pct=0.0095  [candidate]
  ABT       score=0.0984  atr_pct=0.0102  [candidate]
  TMO       score=0.0967  atr_pct=0.0114  [candidate]
  HON       score=0.0966  atr_pct=0.0099  [candidate]
  ECL       score=0.0911  atr_pct=0.0110  [candidate]
  AEP       score=0.0909  atr_pct=0.0102  [candidate]
  META      score=0.0870  atr_pct=0.0105  [candidate]
  LIN       score=0.0845  atr_pct=0.0097  [candidate]
  SHW       score=0.0805  atr_pct=0.0099  [candidate]
  BA        score=0.0774  atr_pct=0.0100  [candidate]
  PM        score=0.0751  atr_pct=0.0108  [candidate]
  SRE       score=0.0718  atr_pct=0.0099  [candidate]
  JPM       score=0.0696  atr_pct=0.0103  [candidate]
  O         score=0.0676  atr_pct=0.0095  [candidate]
  TMUS      score=0.0606  atr_pct=0.0112  [candidate]
  MA        score=0.0588  atr_pct=0.0107  [candidate]
  NEE       score=0.0588  atr_pct=0.0108  [candidate]
  UPS       score=0.0465  atr_pct=0.0117  [candidate]
  UNH       score=0.0403  atr_pct=0.0114  [candidate]
  AVGO      score=0.0366  atr_pct=0.0094  [candidate]
  JNJ       score=0.0301  atr_pct=0.0100  [candidate]
  SBUX      score=0.0298  atr_pct=0.0100  [candidate]
```

## scan_triggers candidates  (2026-05-12T19:45:50Z)

```
  GOOGL     score=0.9628  atr_pct=0.0235  [SELECTED]
  FCX       score=0.7073  atr_pct=0.0406  [SELECTED]
  AVGO      score=0.6044  atr_pct=0.0339  [SELECTED]
  SLB       score=0.5728  atr_pct=0.0303  [SELECTED]
  NVDA      score=0.5367  atr_pct=0.0296  [SELECTED]
  CSCO      score=0.5240  atr_pct=0.0229  [candidate]
  MRK       score=0.3948  atr_pct=0.0243  [SELECTED]
  XOM       score=0.3467  atr_pct=0.0287  [SELECTED]
  COP       score=0.3413  atr_pct=0.0306  [candidate]
  JNJ       score=0.3308  atr_pct=0.0178  [SELECTED]
  WMT       score=0.3087  atr_pct=0.0200  [SELECTED]
  AAPL      score=0.2910  atr_pct=0.0208  [candidate]
  SBUX      score=0.2834  atr_pct=0.0240  [SELECTED]
  EQIX      score=0.2826  atr_pct=0.0188  [candidate]
  NEE       score=0.2403  atr_pct=0.0222  [candidate]
  AMZN      score=0.2306  atr_pct=0.0252  [candidate]
  BA        score=0.2179  atr_pct=0.0277  [candidate]
  RTX       score=0.2066  atr_pct=0.0244  [candidate]
  AEP       score=0.1739  atr_pct=0.0177  [candidate]
  LIN       score=0.1550  atr_pct=0.0191  [candidate]
  AMGN      score=0.1536  atr_pct=0.0225  [candidate]
  KO        score=0.1370  atr_pct=0.0163  [candidate]
  UNH       score=0.1305  atr_pct=0.0233  [candidate]
  O         score=0.1013  atr_pct=0.0149  [candidate]
  SO        score=0.0290  atr_pct=0.0167  [candidate]
  DUK       score=0.0273  atr_pct=0.0159  [candidate]
  UPS       score=0.0264  atr_pct=0.0278  [candidate]
```

## scan_triggers candidates  (2026-05-12T19:46:42Z)

```
  GOOGL     score=0.9627  atr_pct=0.0235  [SELECTED]
  FCX       score=0.7061  atr_pct=0.0406  [SELECTED]
  AVGO      score=0.6040  atr_pct=0.0339  [SELECTED]
  SLB       score=0.5726  atr_pct=0.0303  [SELECTED]
  NVDA      score=0.5335  atr_pct=0.0297  [SELECTED]
  CSCO      score=0.5229  atr_pct=0.0229  [candidate]
  MRK       score=0.3950  atr_pct=0.0243  [SELECTED]
  XOM       score=0.3464  atr_pct=0.0287  [SELECTED]
  COP       score=0.3441  atr_pct=0.0306  [candidate]
  JNJ       score=0.3309  atr_pct=0.0178  [SELECTED]
  WMT       score=0.3089  atr_pct=0.0200  [SELECTED]
  WELL      score=0.3020  atr_pct=0.0214  [SELECTED]
  AAPL      score=0.2909  atr_pct=0.0208  [candidate]
  SBUX      score=0.2831  atr_pct=0.0240  [candidate]
  CVX       score=0.2718  atr_pct=0.0254  [candidate]
  EOG       score=0.2411  atr_pct=0.0278  [candidate]
  NEE       score=0.2408  atr_pct=0.0222  [candidate]
  AMZN      score=0.2307  atr_pct=0.0252  [candidate]
  BA        score=0.2182  atr_pct=0.0277  [candidate]
  LLY       score=0.2092  atr_pct=0.0305  [candidate]
  LIN       score=0.1558  atr_pct=0.0191  [candidate]
  AMGN      score=0.1541  atr_pct=0.0225  [candidate]
  KO        score=0.1374  atr_pct=0.0163  [candidate]
  UNH       score=0.1314  atr_pct=0.0233  [candidate]
  O         score=0.1013  atr_pct=0.0149  [candidate]
  COST      score=0.0588  atr_pct=0.0179  [candidate]
  SO        score=0.0291  atr_pct=0.0167  [candidate]
  UPS       score=0.0266  atr_pct=0.0278  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T204626-374e12d5",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T204626-ebd4fd19",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "df7e66450535adfaba51e8edec8e1113e34ff9482e5a82a45a9b65edeee3c8ca"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T204902-3eccd6ae",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T204902-0cee91cb",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "d2c85fdd0f532536fc281ae4c7082d3c77bfa0650545f5544856ef00ef891146"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T205036-6ca767ae",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T205036-b95a4d6a",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "fdbe7fbf89cba55fd53b0dd36d865f47cfb78d2d6b660e8dff2838c893d57aea"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T205134-42395701",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T205134-cace539d",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "54ee2d8eeb40bf0119d7e3fc68c9ce58fbb4ee8e6484b039ab624111de237df7"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T205156-5a647781",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T205156-05620a08",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "a46a349a7f936ba49b22e8c264ca526e6888a95e73f96c5797a046907f8b9248"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T205213-bb97ed18",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T205213-f8a19788",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "54abef48d25e009a00dbb218e857516089bf9b6f632dce39c89fd75d43d5c1a5"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T205222-aa78d03c",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T205222-6bdfc4ef",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "72e596acf4000d83e564ed09b7564190e75ec4cabe28f1da66ffe1b62ffecb78"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T205228-c5c85a3e",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T205228-80b62a91",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "5bf1f4d16797bf28375bd97c8d582edcd70f102afcc3ddc9b494eb3c71bc7502"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T205236-fca542a3",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T205236-2b09cffb",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "0dba45346458e6e79898c167aee17f8898366247aeb4cc5a56cad3eefc954485"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T205243-9d21d4b9",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T205243-ac2d58e1",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "716e3a673ba6b7b2b35758d26c7c68fd6d83c49aa156e09d025419d0f70fffff"
}
```

## scan_triggers candidates  (2026-05-12T20:55:33Z)

```
  WMT       score=0.2220  atr_pct=0.0109  [SELECTED]
  APD       score=0.2198  atr_pct=0.0114  [SELECTED]
  DIS       score=0.2113  atr_pct=0.0105  [SELECTED]
  ORCL      score=0.2093  atr_pct=0.0103  [SELECTED]
  LLY       score=0.2016  atr_pct=0.0111  [SELECTED]
  BLK       score=0.1996  atr_pct=0.0098  [SELECTED]
  BKNG      score=0.1969  atr_pct=0.0118  [SELECTED]
  KO        score=0.1963  atr_pct=0.0110  [SELECTED]
  WELL      score=0.1905  atr_pct=0.0099  [SELECTED]
  EOG       score=0.1862  atr_pct=0.0102  [SELECTED]
  UNP       score=0.1859  atr_pct=0.0099  [candidate]
  CRM       score=0.1782  atr_pct=0.0104  [candidate]
  PG        score=0.1768  atr_pct=0.0105  [candidate]
  COST      score=0.1717  atr_pct=0.0115  [candidate]
  PEP       score=0.1712  atr_pct=0.0108  [candidate]
  MCD       score=0.1708  atr_pct=0.0111  [candidate]
  XOM       score=0.1671  atr_pct=0.0105  [candidate]
  WFC       score=0.1666  atr_pct=0.0117  [candidate]
  NFLX      score=0.1564  atr_pct=0.0103  [candidate]
  GOOGL     score=0.1557  atr_pct=0.0103  [candidate]
  CL        score=0.1537  atr_pct=0.0102  [candidate]
  AMGN      score=0.1489  atr_pct=0.0099  [candidate]
  MS        score=0.1472  atr_pct=0.0094  [candidate]
  LMT       score=0.1454  atr_pct=0.0105  [candidate]
  ABBV      score=0.1442  atr_pct=0.0116  [candidate]
  INTU      score=0.1425  atr_pct=0.0106  [candidate]
  TSLA      score=0.1422  atr_pct=0.0098  [candidate]
  GS        score=0.1396  atr_pct=0.0103  [candidate]
  HD        score=0.1392  atr_pct=0.0109  [candidate]
  CSCO      score=0.1378  atr_pct=0.0110  [candidate]
  NVDA      score=0.1334  atr_pct=0.0107  [candidate]
  AXP       score=0.1333  atr_pct=0.0111  [candidate]
  BAC       score=0.1318  atr_pct=0.0095  [candidate]
  EQIX      score=0.1316  atr_pct=0.0103  [candidate]
  AAPL      score=0.1295  atr_pct=0.0100  [candidate]
  NKE       score=0.1268  atr_pct=0.0109  [candidate]
  AMT       score=0.1266  atr_pct=0.0109  [candidate]
  AMD       score=0.1264  atr_pct=0.0094  [candidate]
  MSFT      score=0.1260  atr_pct=0.0112  [candidate]
  GE        score=0.1218  atr_pct=0.0112  [candidate]
  DE        score=0.1209  atr_pct=0.0109  [candidate]
  COP       score=0.1205  atr_pct=0.0099  [candidate]
  PLD       score=0.1175  atr_pct=0.0106  [candidate]
  AMZN      score=0.1169  atr_pct=0.0094  [candidate]
  ISRG      score=0.1167  atr_pct=0.0096  [candidate]
  SO        score=0.1155  atr_pct=0.0097  [candidate]
  CMCSA     score=0.1111  atr_pct=0.0120  [candidate]
  SLB       score=0.1033  atr_pct=0.0103  [candidate]
  CVX       score=0.1017  atr_pct=0.0108  [candidate]
  CAT       score=0.1004  atr_pct=0.0095  [candidate]
  ABT       score=0.0984  atr_pct=0.0102  [candidate]
  TMO       score=0.0967  atr_pct=0.0114  [candidate]
  HON       score=0.0966  atr_pct=0.0099  [candidate]
  ECL       score=0.0911  atr_pct=0.0110  [candidate]
  AEP       score=0.0909  atr_pct=0.0102  [candidate]
  META      score=0.0870  atr_pct=0.0105  [candidate]
  LIN       score=0.0845  atr_pct=0.0097  [candidate]
  SHW       score=0.0805  atr_pct=0.0099  [candidate]
  BA        score=0.0774  atr_pct=0.0100  [candidate]
  PM        score=0.0751  atr_pct=0.0108  [candidate]
  SRE       score=0.0718  atr_pct=0.0099  [candidate]
  JPM       score=0.0696  atr_pct=0.0103  [candidate]
  O         score=0.0676  atr_pct=0.0095  [candidate]
  TMUS      score=0.0606  atr_pct=0.0112  [candidate]
  MA        score=0.0588  atr_pct=0.0107  [candidate]
  NEE       score=0.0588  atr_pct=0.0108  [candidate]
  UPS       score=0.0465  atr_pct=0.0117  [candidate]
  UNH       score=0.0403  atr_pct=0.0114  [candidate]
  AVGO      score=0.0366  atr_pct=0.0094  [candidate]
  JNJ       score=0.0301  atr_pct=0.0100  [candidate]
  SBUX      score=0.0298  atr_pct=0.0100  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T205611-ea1b99f6",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T205611-99ac8b2d",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "410a9b72153b1f52a740ec95688f6f9428c303e4220b6159a0f85140e2d33ff6"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T205736-33700482",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T205736-07351b76",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "9e6196fd88e15f96a2d29b9fc724d7d5c4dbeaa8d4cfb3939d4f6c2e1cf7a1a1"
}
```

## scan_triggers candidates  (2026-05-12T20:59:17Z)

```
  FCX       score=0.7019  atr_pct=0.0407  [SELECTED]
  NVDA      score=0.5339  atr_pct=0.0297  [SELECTED]
  GS        score=0.4362  atr_pct=0.0247  [SELECTED]
  XOM       score=0.3443  atr_pct=0.0288  [SELECTED]
  COP       score=0.3442  atr_pct=0.0307  [SELECTED]
  JNJ       score=0.3287  atr_pct=0.0178  [SELECTED]
  NEE       score=0.2354  atr_pct=0.0224  [SELECTED]
  LLY       score=0.2097  atr_pct=0.0305  [SELECTED]
  AEP       score=0.1733  atr_pct=0.0177  [SELECTED]
  APD       score=0.1442  atr_pct=0.0203  [SELECTED]
  UNH       score=0.1327  atr_pct=0.0232  [candidate]
  PEP       score=0.1135  atr_pct=0.0210  [candidate]
  BLK       score=0.0968  atr_pct=0.0227  [candidate]
  SO        score=0.0286  atr_pct=0.0168  [candidate]
```

## scan_triggers candidates  (2026-05-12T21:16:50Z)

```
  FCX       score=0.7019  atr_pct=0.0407  [SELECTED]
  NVDA      score=0.5339  atr_pct=0.0297  [SELECTED]
  GS        score=0.4362  atr_pct=0.0247  [SELECTED]
  XOM       score=0.3443  atr_pct=0.0288  [SELECTED]
  COP       score=0.3442  atr_pct=0.0307  [SELECTED]
  JNJ       score=0.3287  atr_pct=0.0178  [SELECTED]
  NEE       score=0.2354  atr_pct=0.0224  [SELECTED]
  LLY       score=0.2097  atr_pct=0.0305  [SELECTED]
  AEP       score=0.1733  atr_pct=0.0177  [SELECTED]
  APD       score=0.1442  atr_pct=0.0203  [SELECTED]
  UNH       score=0.1327  atr_pct=0.0232  [candidate]
  PEP       score=0.1135  atr_pct=0.0210  [candidate]
  BLK       score=0.0968  atr_pct=0.0227  [candidate]
  SO        score=0.0286  atr_pct=0.0168  [candidate]
```

## scan_triggers candidates  (2026-05-12T21:18:05Z)

```
  FCX       score=0.7019  atr_pct=0.0407  [SELECTED]
  NVDA      score=0.5339  atr_pct=0.0297  [SELECTED]
  GS        score=0.4362  atr_pct=0.0247  [SELECTED]
  XOM       score=0.3443  atr_pct=0.0288  [SELECTED]
  COP       score=0.3442  atr_pct=0.0307  [SELECTED]
  JNJ       score=0.3287  atr_pct=0.0178  [SELECTED]
  NEE       score=0.2354  atr_pct=0.0224  [SELECTED]
  LLY       score=0.2097  atr_pct=0.0305  [SELECTED]
  AEP       score=0.1733  atr_pct=0.0177  [SELECTED]
  APD       score=0.1442  atr_pct=0.0203  [SELECTED]
  UNH       score=0.1327  atr_pct=0.0232  [candidate]
  PEP       score=0.1135  atr_pct=0.0210  [candidate]
  BLK       score=0.0968  atr_pct=0.0227  [candidate]
  SO        score=0.0286  atr_pct=0.0168  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T123135-c5e03184",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T123135-edaad8ed",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "8adb9ac2d7ed33006c4cb6c2c27b2630006dd0eebbb5971e1697aa6a481a41ae"
}
```

## scan_triggers candidates  (2026-05-13T12:32:17Z)

```
  WMT       score=0.2220  atr_pct=0.0109  [SELECTED]
  APD       score=0.2198  atr_pct=0.0114  [SELECTED]
  DIS       score=0.2113  atr_pct=0.0105  [SELECTED]
  ORCL      score=0.2093  atr_pct=0.0103  [SELECTED]
  LLY       score=0.2016  atr_pct=0.0111  [SELECTED]
  BLK       score=0.1996  atr_pct=0.0098  [SELECTED]
  BKNG      score=0.1969  atr_pct=0.0118  [SELECTED]
  KO        score=0.1963  atr_pct=0.0110  [SELECTED]
  WELL      score=0.1905  atr_pct=0.0099  [SELECTED]
  EOG       score=0.1862  atr_pct=0.0102  [SELECTED]
  UNP       score=0.1859  atr_pct=0.0099  [candidate]
  CRM       score=0.1782  atr_pct=0.0104  [candidate]
  PG        score=0.1768  atr_pct=0.0105  [candidate]
  COST      score=0.1717  atr_pct=0.0115  [candidate]
  PEP       score=0.1712  atr_pct=0.0108  [candidate]
  MCD       score=0.1708  atr_pct=0.0111  [candidate]
  XOM       score=0.1671  atr_pct=0.0105  [candidate]
  WFC       score=0.1666  atr_pct=0.0117  [candidate]
  NFLX      score=0.1564  atr_pct=0.0103  [candidate]
  GOOGL     score=0.1557  atr_pct=0.0103  [candidate]
  CL        score=0.1537  atr_pct=0.0102  [candidate]
  AMGN      score=0.1489  atr_pct=0.0099  [candidate]
  MS        score=0.1472  atr_pct=0.0094  [candidate]
  LMT       score=0.1454  atr_pct=0.0105  [candidate]
  ABBV      score=0.1442  atr_pct=0.0116  [candidate]
  INTU      score=0.1425  atr_pct=0.0106  [candidate]
  TSLA      score=0.1422  atr_pct=0.0098  [candidate]
  GS        score=0.1396  atr_pct=0.0103  [candidate]
  HD        score=0.1392  atr_pct=0.0109  [candidate]
  CSCO      score=0.1378  atr_pct=0.0110  [candidate]
  NVDA      score=0.1334  atr_pct=0.0107  [candidate]
  AXP       score=0.1333  atr_pct=0.0111  [candidate]
  BAC       score=0.1318  atr_pct=0.0095  [candidate]
  EQIX      score=0.1316  atr_pct=0.0103  [candidate]
  AAPL      score=0.1295  atr_pct=0.0100  [candidate]
  NKE       score=0.1268  atr_pct=0.0109  [candidate]
  AMT       score=0.1266  atr_pct=0.0109  [candidate]
  AMD       score=0.1264  atr_pct=0.0094  [candidate]
  MSFT      score=0.1260  atr_pct=0.0112  [candidate]
  GE        score=0.1218  atr_pct=0.0112  [candidate]
  DE        score=0.1209  atr_pct=0.0109  [candidate]
  COP       score=0.1205  atr_pct=0.0099  [candidate]
  PLD       score=0.1175  atr_pct=0.0106  [candidate]
  AMZN      score=0.1169  atr_pct=0.0094  [candidate]
  ISRG      score=0.1167  atr_pct=0.0096  [candidate]
  SO        score=0.1155  atr_pct=0.0097  [candidate]
  CMCSA     score=0.1111  atr_pct=0.0120  [candidate]
  SLB       score=0.1033  atr_pct=0.0103  [candidate]
  CVX       score=0.1017  atr_pct=0.0108  [candidate]
  CAT       score=0.1004  atr_pct=0.0095  [candidate]
  ABT       score=0.0984  atr_pct=0.0102  [candidate]
  TMO       score=0.0967  atr_pct=0.0114  [candidate]
  HON       score=0.0966  atr_pct=0.0099  [candidate]
  ECL       score=0.0911  atr_pct=0.0110  [candidate]
  AEP       score=0.0909  atr_pct=0.0102  [candidate]
  META      score=0.0870  atr_pct=0.0105  [candidate]
  LIN       score=0.0845  atr_pct=0.0097  [candidate]
  SHW       score=0.0805  atr_pct=0.0099  [candidate]
  BA        score=0.0774  atr_pct=0.0100  [candidate]
  PM        score=0.0751  atr_pct=0.0108  [candidate]
  SRE       score=0.0718  atr_pct=0.0099  [candidate]
  JPM       score=0.0696  atr_pct=0.0103  [candidate]
  O         score=0.0676  atr_pct=0.0095  [candidate]
  TMUS      score=0.0606  atr_pct=0.0112  [candidate]
  MA        score=0.0588  atr_pct=0.0107  [candidate]
  NEE       score=0.0588  atr_pct=0.0108  [candidate]
  UPS       score=0.0465  atr_pct=0.0117  [candidate]
  UNH       score=0.0403  atr_pct=0.0114  [candidate]
  AVGO      score=0.0366  atr_pct=0.0094  [candidate]
  JNJ       score=0.0301  atr_pct=0.0100  [candidate]
  SBUX      score=0.0298  atr_pct=0.0100  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T123317-183719aa",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T123317-b791b506",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "31d5f44310fd33c794cdf4b13ab589f18d84776414a9e306b05135ec353a4fd4"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T125949-08c5e598",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T125949-f2d96612",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "26dacadf73d90c473d5db3c8d8b84760578c8882da7577514ece12a3e9fed61c"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T125955-19433db1",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T125955-de5c881c",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "f558f80b633065be6549b488183173ac7ea4b3363243b15c438bacafa4ee823d"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T130002-69bc76b8",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T130002-6f2fca60",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "f5ce032e9f0ebe9f603f6187e067644ec38e06fb8f440f4149733b672e01c6aa"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T130007-f035a629",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T130007-9c90bf33",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "ef87b380e222b85fa9a27b38d6d9284baed5e59bdcf2f83e559627111483736a"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T130013-e0fae197",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T130013-b1fa5bf3",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "e1ea7db9cc45908ca2f10a016557469bca003d822304476c2619e3d90ca8a235"
}
```

## scan_triggers candidates  (2026-05-13T15:28:42Z)

```
  AMD       score=1.9658  atr_pct=0.0458  [SELECTED]
  GOOGL     score=0.9382  atr_pct=0.0234  [SELECTED]
  FCX       score=0.7055  atr_pct=0.0392  [SELECTED]
  SLB       score=0.5134  atr_pct=0.0303  [SELECTED]
  CSCO      score=0.5116  atr_pct=0.0222  [SELECTED]
  AVGO      score=0.5096  atr_pct=0.0344  [candidate]
  NVDA      score=0.4859  atr_pct=0.0291  [candidate]
  MRK       score=0.3516  atr_pct=0.0239  [SELECTED]
  XOM       score=0.3261  atr_pct=0.0281  [SELECTED]
  WMT       score=0.3122  atr_pct=0.0204  [SELECTED]
  COP       score=0.2867  atr_pct=0.0305  [candidate]
  SBUX      score=0.2660  atr_pct=0.0232  [SELECTED]
  AAPL      score=0.2556  atr_pct=0.0203  [candidate]
  NEE       score=0.2384  atr_pct=0.0220  [SELECTED]
  PLD       score=0.2230  atr_pct=0.0180  [candidate]
  BA        score=0.2225  atr_pct=0.0272  [candidate]
  TSLA      score=0.2066  atr_pct=0.0365  [candidate]
  LLY       score=0.1847  atr_pct=0.0295  [candidate]
  AMZN      score=0.1768  atr_pct=0.0246  [candidate]
  AEP       score=0.1495  atr_pct=0.0197  [candidate]
  APD       score=0.1491  atr_pct=0.0199  [candidate]
  KO        score=0.1472  atr_pct=0.0162  [candidate]
  AMGN      score=0.1214  atr_pct=0.0227  [candidate]
  O         score=0.1031  atr_pct=0.0150  [candidate]
```

## scan_triggers candidates  (2026-05-13T15:32:08Z)

```
  AMD       score=1.9666  atr_pct=0.0457  [SELECTED]
  GOOGL     score=0.9432  atr_pct=0.0234  [SELECTED]
  FCX       score=0.7042  atr_pct=0.0393  [SELECTED]
  SLB       score=0.5155  atr_pct=0.0303  [SELECTED]
  CSCO      score=0.5100  atr_pct=0.0222  [SELECTED]
  AVGO      score=0.5066  atr_pct=0.0344  [candidate]
  NVDA      score=0.4858  atr_pct=0.0291  [candidate]
  MRK       score=0.3521  atr_pct=0.0239  [SELECTED]
  XOM       score=0.3254  atr_pct=0.0281  [SELECTED]
  WELL      score=0.3159  atr_pct=0.0209  [SELECTED]
  WMT       score=0.3110  atr_pct=0.0204  [SELECTED]
  COP       score=0.2848  atr_pct=0.0306  [candidate]
  EQIX      score=0.2714  atr_pct=0.0189  [SELECTED]
  AAPL      score=0.2587  atr_pct=0.0203  [candidate]
  CVX       score=0.2424  atr_pct=0.0248  [candidate]
  NEE       score=0.2387  atr_pct=0.0220  [candidate]
  TSLA      score=0.2176  atr_pct=0.0363  [candidate]
  APD       score=0.1496  atr_pct=0.0199  [candidate]
  AEP       score=0.1487  atr_pct=0.0197  [candidate]
  KO        score=0.1458  atr_pct=0.0162  [candidate]
  O         score=0.1023  atr_pct=0.0150  [candidate]
  COST      score=0.0645  atr_pct=0.0179  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T155702-2c30f111",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T155702-06081de0",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "949999d39a53661bf404773b8b7b72d362f31c84b7b098b986955b958263cad5"
}
```

## scan_triggers candidates  (2026-05-13T15:57:15Z)

```
  WMT       score=0.2220  atr_pct=0.0109  [SELECTED]
  APD       score=0.2198  atr_pct=0.0114  [SELECTED]
  DIS       score=0.2113  atr_pct=0.0105  [SELECTED]
  ORCL      score=0.2093  atr_pct=0.0103  [SELECTED]
  LLY       score=0.2016  atr_pct=0.0111  [SELECTED]
  BLK       score=0.1996  atr_pct=0.0098  [SELECTED]
  BKNG      score=0.1969  atr_pct=0.0118  [SELECTED]
  KO        score=0.1963  atr_pct=0.0110  [SELECTED]
  WELL      score=0.1905  atr_pct=0.0099  [SELECTED]
  EOG       score=0.1862  atr_pct=0.0102  [SELECTED]
  UNP       score=0.1859  atr_pct=0.0099  [candidate]
  CRM       score=0.1782  atr_pct=0.0104  [candidate]
  PG        score=0.1768  atr_pct=0.0105  [candidate]
  COST      score=0.1717  atr_pct=0.0115  [candidate]
  PEP       score=0.1712  atr_pct=0.0108  [candidate]
  MCD       score=0.1708  atr_pct=0.0111  [candidate]
  XOM       score=0.1671  atr_pct=0.0105  [candidate]
  WFC       score=0.1666  atr_pct=0.0117  [candidate]
  NFLX      score=0.1564  atr_pct=0.0103  [candidate]
  GOOGL     score=0.1557  atr_pct=0.0103  [candidate]
  CL        score=0.1537  atr_pct=0.0102  [candidate]
  AMGN      score=0.1489  atr_pct=0.0099  [candidate]
  MS        score=0.1472  atr_pct=0.0094  [candidate]
  LMT       score=0.1454  atr_pct=0.0105  [candidate]
  ABBV      score=0.1442  atr_pct=0.0116  [candidate]
  INTU      score=0.1425  atr_pct=0.0106  [candidate]
  TSLA      score=0.1422  atr_pct=0.0098  [candidate]
  GS        score=0.1396  atr_pct=0.0103  [candidate]
  HD        score=0.1392  atr_pct=0.0109  [candidate]
  CSCO      score=0.1378  atr_pct=0.0110  [candidate]
  NVDA      score=0.1334  atr_pct=0.0107  [candidate]
  AXP       score=0.1333  atr_pct=0.0111  [candidate]
  BAC       score=0.1318  atr_pct=0.0095  [candidate]
  EQIX      score=0.1316  atr_pct=0.0103  [candidate]
  AAPL      score=0.1295  atr_pct=0.0100  [candidate]
  NKE       score=0.1268  atr_pct=0.0109  [candidate]
  AMT       score=0.1266  atr_pct=0.0109  [candidate]
  AMD       score=0.1264  atr_pct=0.0094  [candidate]
  MSFT      score=0.1260  atr_pct=0.0112  [candidate]
  GE        score=0.1218  atr_pct=0.0112  [candidate]
  DE        score=0.1209  atr_pct=0.0109  [candidate]
  COP       score=0.1205  atr_pct=0.0099  [candidate]
  PLD       score=0.1175  atr_pct=0.0106  [candidate]
  AMZN      score=0.1169  atr_pct=0.0094  [candidate]
  ISRG      score=0.1167  atr_pct=0.0096  [candidate]
  SO        score=0.1155  atr_pct=0.0097  [candidate]
  CMCSA     score=0.1111  atr_pct=0.0120  [candidate]
  SLB       score=0.1033  atr_pct=0.0103  [candidate]
  CVX       score=0.1017  atr_pct=0.0108  [candidate]
  CAT       score=0.1004  atr_pct=0.0095  [candidate]
  ABT       score=0.0984  atr_pct=0.0102  [candidate]
  TMO       score=0.0967  atr_pct=0.0114  [candidate]
  HON       score=0.0966  atr_pct=0.0099  [candidate]
  ECL       score=0.0911  atr_pct=0.0110  [candidate]
  AEP       score=0.0909  atr_pct=0.0102  [candidate]
  META      score=0.0870  atr_pct=0.0105  [candidate]
  LIN       score=0.0845  atr_pct=0.0097  [candidate]
  SHW       score=0.0805  atr_pct=0.0099  [candidate]
  BA        score=0.0774  atr_pct=0.0100  [candidate]
  PM        score=0.0751  atr_pct=0.0108  [candidate]
  SRE       score=0.0718  atr_pct=0.0099  [candidate]
  JPM       score=0.0696  atr_pct=0.0103  [candidate]
  O         score=0.0676  atr_pct=0.0095  [candidate]
  TMUS      score=0.0606  atr_pct=0.0112  [candidate]
  MA        score=0.0588  atr_pct=0.0107  [candidate]
  NEE       score=0.0588  atr_pct=0.0108  [candidate]
  UPS       score=0.0465  atr_pct=0.0117  [candidate]
  UNH       score=0.0403  atr_pct=0.0114  [candidate]
  AVGO      score=0.0366  atr_pct=0.0094  [candidate]
  JNJ       score=0.0301  atr_pct=0.0100  [candidate]
  SBUX      score=0.0298  atr_pct=0.0100  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T155805-d43ed4e1",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T155805-41c1cba4",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "b6362663a274be009081aa84699cdacb008458828ffa62708369db6a106c07ae"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T155813-27582908",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T155813-20e34901",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "2cde00fa843c04bc0b0d4ed6816ee63241a5f39fddcc5c008dcb9c8c18a4cbaa"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T155819-dfdca702",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T155819-e402382e",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "6b1ca38d0488b9ef763c852baab86675d1680090a14f28b1d5c2f376506e7e3b"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T155824-e8933f30",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T155824-27deef7a",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "be7c519cad6f98e95e251b663ab8784fd720d0c0dd6ffe5cf71b3495c06ea7bb"
}
```

## scan_triggers candidates  (2026-05-13T15:58:44Z)

```
  WMT       score=0.2220  atr_pct=0.0109  [SELECTED]
  APD       score=0.2198  atr_pct=0.0114  [SELECTED]
  DIS       score=0.2113  atr_pct=0.0105  [SELECTED]
  ORCL      score=0.2093  atr_pct=0.0103  [SELECTED]
  LLY       score=0.2016  atr_pct=0.0111  [SELECTED]
  BLK       score=0.1996  atr_pct=0.0098  [SELECTED]
  BKNG      score=0.1969  atr_pct=0.0118  [SELECTED]
  KO        score=0.1963  atr_pct=0.0110  [SELECTED]
  WELL      score=0.1905  atr_pct=0.0099  [SELECTED]
  EOG       score=0.1862  atr_pct=0.0102  [SELECTED]
  UNP       score=0.1859  atr_pct=0.0099  [candidate]
  CRM       score=0.1782  atr_pct=0.0104  [candidate]
  PG        score=0.1768  atr_pct=0.0105  [candidate]
  COST      score=0.1717  atr_pct=0.0115  [candidate]
  PEP       score=0.1712  atr_pct=0.0108  [candidate]
  MCD       score=0.1708  atr_pct=0.0111  [candidate]
  XOM       score=0.1671  atr_pct=0.0105  [candidate]
  WFC       score=0.1666  atr_pct=0.0117  [candidate]
  NFLX      score=0.1564  atr_pct=0.0103  [candidate]
  GOOGL     score=0.1557  atr_pct=0.0103  [candidate]
  CL        score=0.1537  atr_pct=0.0102  [candidate]
  AMGN      score=0.1489  atr_pct=0.0099  [candidate]
  MS        score=0.1472  atr_pct=0.0094  [candidate]
  LMT       score=0.1454  atr_pct=0.0105  [candidate]
  ABBV      score=0.1442  atr_pct=0.0116  [candidate]
  INTU      score=0.1425  atr_pct=0.0106  [candidate]
  TSLA      score=0.1422  atr_pct=0.0098  [candidate]
  GS        score=0.1396  atr_pct=0.0103  [candidate]
  HD        score=0.1392  atr_pct=0.0109  [candidate]
  CSCO      score=0.1378  atr_pct=0.0110  [candidate]
  NVDA      score=0.1334  atr_pct=0.0107  [candidate]
  AXP       score=0.1333  atr_pct=0.0111  [candidate]
  BAC       score=0.1318  atr_pct=0.0095  [candidate]
  EQIX      score=0.1316  atr_pct=0.0103  [candidate]
  AAPL      score=0.1295  atr_pct=0.0100  [candidate]
  NKE       score=0.1268  atr_pct=0.0109  [candidate]
  AMT       score=0.1266  atr_pct=0.0109  [candidate]
  AMD       score=0.1264  atr_pct=0.0094  [candidate]
  MSFT      score=0.1260  atr_pct=0.0112  [candidate]
  GE        score=0.1218  atr_pct=0.0112  [candidate]
  DE        score=0.1209  atr_pct=0.0109  [candidate]
  COP       score=0.1205  atr_pct=0.0099  [candidate]
  PLD       score=0.1175  atr_pct=0.0106  [candidate]
  AMZN      score=0.1169  atr_pct=0.0094  [candidate]
  ISRG      score=0.1167  atr_pct=0.0096  [candidate]
  SO        score=0.1155  atr_pct=0.0097  [candidate]
  CMCSA     score=0.1111  atr_pct=0.0120  [candidate]
  SLB       score=0.1033  atr_pct=0.0103  [candidate]
  CVX       score=0.1017  atr_pct=0.0108  [candidate]
  CAT       score=0.1004  atr_pct=0.0095  [candidate]
  ABT       score=0.0984  atr_pct=0.0102  [candidate]
  TMO       score=0.0967  atr_pct=0.0114  [candidate]
  HON       score=0.0966  atr_pct=0.0099  [candidate]
  ECL       score=0.0911  atr_pct=0.0110  [candidate]
  AEP       score=0.0909  atr_pct=0.0102  [candidate]
  META      score=0.0870  atr_pct=0.0105  [candidate]
  LIN       score=0.0845  atr_pct=0.0097  [candidate]
  SHW       score=0.0805  atr_pct=0.0099  [candidate]
  BA        score=0.0774  atr_pct=0.0100  [candidate]
  PM        score=0.0751  atr_pct=0.0108  [candidate]
  SRE       score=0.0718  atr_pct=0.0099  [candidate]
  JPM       score=0.0696  atr_pct=0.0103  [candidate]
  O         score=0.0676  atr_pct=0.0095  [candidate]
  TMUS      score=0.0606  atr_pct=0.0112  [candidate]
  MA        score=0.0588  atr_pct=0.0107  [candidate]
  NEE       score=0.0588  atr_pct=0.0108  [candidate]
  UPS       score=0.0465  atr_pct=0.0117  [candidate]
  UNH       score=0.0403  atr_pct=0.0114  [candidate]
  AVGO      score=0.0366  atr_pct=0.0094  [candidate]
  JNJ       score=0.0301  atr_pct=0.0100  [candidate]
  SBUX      score=0.0298  atr_pct=0.0100  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T161411-96f65f27",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T161411-ba22de06",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "4192165ea37c5f607dac3422ff022ed3abf4485763496187168c559225dc7d01"
}
```

## scan_triggers candidates  (2026-05-13T16:14:22Z)

```
  WMT       score=0.2220  atr_pct=0.0109  [SELECTED]
  APD       score=0.2198  atr_pct=0.0114  [SELECTED]
  DIS       score=0.2113  atr_pct=0.0105  [SELECTED]
  ORCL      score=0.2093  atr_pct=0.0103  [SELECTED]
  LLY       score=0.2016  atr_pct=0.0111  [SELECTED]
  BLK       score=0.1996  atr_pct=0.0098  [SELECTED]
  BKNG      score=0.1969  atr_pct=0.0118  [SELECTED]
  KO        score=0.1963  atr_pct=0.0110  [SELECTED]
  WELL      score=0.1905  atr_pct=0.0099  [SELECTED]
  EOG       score=0.1862  atr_pct=0.0102  [SELECTED]
  UNP       score=0.1859  atr_pct=0.0099  [candidate]
  CRM       score=0.1782  atr_pct=0.0104  [candidate]
  PG        score=0.1768  atr_pct=0.0105  [candidate]
  COST      score=0.1717  atr_pct=0.0115  [candidate]
  PEP       score=0.1712  atr_pct=0.0108  [candidate]
  MCD       score=0.1708  atr_pct=0.0111  [candidate]
  XOM       score=0.1671  atr_pct=0.0105  [candidate]
  WFC       score=0.1666  atr_pct=0.0117  [candidate]
  NFLX      score=0.1564  atr_pct=0.0103  [candidate]
  GOOGL     score=0.1557  atr_pct=0.0103  [candidate]
  CL        score=0.1537  atr_pct=0.0102  [candidate]
  AMGN      score=0.1489  atr_pct=0.0099  [candidate]
  MS        score=0.1472  atr_pct=0.0094  [candidate]
  LMT       score=0.1454  atr_pct=0.0105  [candidate]
  ABBV      score=0.1442  atr_pct=0.0116  [candidate]
  INTU      score=0.1425  atr_pct=0.0106  [candidate]
  TSLA      score=0.1422  atr_pct=0.0098  [candidate]
  GS        score=0.1396  atr_pct=0.0103  [candidate]
  HD        score=0.1392  atr_pct=0.0109  [candidate]
  CSCO      score=0.1378  atr_pct=0.0110  [candidate]
  NVDA      score=0.1334  atr_pct=0.0107  [candidate]
  AXP       score=0.1333  atr_pct=0.0111  [candidate]
  BAC       score=0.1318  atr_pct=0.0095  [candidate]
  EQIX      score=0.1316  atr_pct=0.0103  [candidate]
  AAPL      score=0.1295  atr_pct=0.0100  [candidate]
  NKE       score=0.1268  atr_pct=0.0109  [candidate]
  AMT       score=0.1266  atr_pct=0.0109  [candidate]
  AMD       score=0.1264  atr_pct=0.0094  [candidate]
  MSFT      score=0.1260  atr_pct=0.0112  [candidate]
  GE        score=0.1218  atr_pct=0.0112  [candidate]
  DE        score=0.1209  atr_pct=0.0109  [candidate]
  COP       score=0.1205  atr_pct=0.0099  [candidate]
  PLD       score=0.1175  atr_pct=0.0106  [candidate]
  AMZN      score=0.1169  atr_pct=0.0094  [candidate]
  ISRG      score=0.1167  atr_pct=0.0096  [candidate]
  SO        score=0.1155  atr_pct=0.0097  [candidate]
  CMCSA     score=0.1111  atr_pct=0.0120  [candidate]
  SLB       score=0.1033  atr_pct=0.0103  [candidate]
  CVX       score=0.1017  atr_pct=0.0108  [candidate]
  CAT       score=0.1004  atr_pct=0.0095  [candidate]
  ABT       score=0.0984  atr_pct=0.0102  [candidate]
  TMO       score=0.0967  atr_pct=0.0114  [candidate]
  HON       score=0.0966  atr_pct=0.0099  [candidate]
  ECL       score=0.0911  atr_pct=0.0110  [candidate]
  AEP       score=0.0909  atr_pct=0.0102  [candidate]
  META      score=0.0870  atr_pct=0.0105  [candidate]
  LIN       score=0.0845  atr_pct=0.0097  [candidate]
  SHW       score=0.0805  atr_pct=0.0099  [candidate]
  BA        score=0.0774  atr_pct=0.0100  [candidate]
  PM        score=0.0751  atr_pct=0.0108  [candidate]
  SRE       score=0.0718  atr_pct=0.0099  [candidate]
  JPM       score=0.0696  atr_pct=0.0103  [candidate]
  O         score=0.0676  atr_pct=0.0095  [candidate]
  TMUS      score=0.0606  atr_pct=0.0112  [candidate]
  MA        score=0.0588  atr_pct=0.0107  [candidate]
  NEE       score=0.0588  atr_pct=0.0108  [candidate]
  UPS       score=0.0465  atr_pct=0.0117  [candidate]
  UNH       score=0.0403  atr_pct=0.0114  [candidate]
  AVGO      score=0.0366  atr_pct=0.0094  [candidate]
  JNJ       score=0.0301  atr_pct=0.0100  [candidate]
  SBUX      score=0.0298  atr_pct=0.0100  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T161643-75a37982",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T161643-8f14445e",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "44e7927f97fda9b8be6a65481f512543a808064bb61d811185e82901ed9f18d4"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T163439-1f3e2bd1",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T163439-0c7f4f94",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "201add782f1a65864852e61f05a5ef99779f25fb3798210471effd9141c1356b"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T165714-05add63e",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T165714-51528865",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "f0d9f18645c6651484cec84efddfa480e5d9c2fab2d50958fcc27b56cd5af6c5"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T165720-c77b5c3d",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T165720-67175062",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "ef88696bb0980fa309b5047c2a4986a7866a7191e9ae01a1479b9c9b2304f0e0"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T165726-259a9ce3",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T165726-82dd7dd8",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "023f0375736ba8958c2b180e357544b7074e45a31b66360407eba7fb9e623b0e"
}
```

## Alert routed  (2026-05-13T16:57:42Z)

```
  AAPL      alert_id=smoke-test-001  next_step=log_only  action=logged  [research-only — no execution]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T165927-05010b1b",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T165928-d5200e80",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "2be35cb9540b6134ee2401aed545b280d71b5b6a893018f87e3fc214a0c13711"
}
```

## scan_triggers candidates  (2026-05-13T17:23:26Z)

```
  AMD       score=2.0055  atr_pct=0.0452  [SELECTED]
  GOOGL     score=0.9578  atr_pct=0.0237  [SELECTED]
  FCX       score=0.7076  atr_pct=0.0396  [SELECTED]
  AVGO      score=0.5234  atr_pct=0.0341  [SELECTED]
  SLB       score=0.5232  atr_pct=0.0301  [SELECTED]
  CSCO      score=0.5121  atr_pct=0.0222  [candidate]
  NVDA      score=0.4949  atr_pct=0.0289  [candidate]
  MRK       score=0.3621  atr_pct=0.0237  [SELECTED]
  JNJ       score=0.3545  atr_pct=0.0177  [SELECTED]
  XOM       score=0.3336  atr_pct=0.0279  [SELECTED]
  WELL      score=0.3310  atr_pct=0.0213  [SELECTED]
  WMT       score=0.3147  atr_pct=0.0203  [SELECTED]
  COP       score=0.2979  atr_pct=0.0303  [candidate]
  EQIX      score=0.2750  atr_pct=0.0190  [candidate]
  AAPL      score=0.2655  atr_pct=0.0206  [candidate]
  CVX       score=0.2472  atr_pct=0.0248  [candidate]
  NEE       score=0.2426  atr_pct=0.0221  [candidate]
  PLD       score=0.2247  atr_pct=0.0180  [candidate]
  EOG       score=0.2196  atr_pct=0.0270  [candidate]
  TSLA      score=0.2096  atr_pct=0.0367  [candidate]
  AMZN      score=0.1886  atr_pct=0.0249  [candidate]
  AEP       score=0.1531  atr_pct=0.0196  [candidate]
  KO        score=0.1452  atr_pct=0.0162  [candidate]
  O         score=0.0972  atr_pct=0.0151  [candidate]
  BLK       score=0.0732  atr_pct=0.0225  [candidate]
  DUK       score=0.0401  atr_pct=0.0161  [candidate]
  SO        score=0.0397  atr_pct=0.0167  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T190443-dccac145",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T190443-c7b39e94",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "16f4ebbb8ce119dfb68ce1f939f28a89796ec3c4eeac3acde47b87c6286c94e8"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T190453-2837b30e",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T190453-4d83e3ce",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "f89898bdd40c95bd1fbb4808e9bab6959dc70af840c5a21c2b87bc30976df323"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T190459-82ecb834",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T190459-5b9ceab0",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "1ef52caf7c0d296665599802beef49082553bb43a75a00bdda95ab84eeede2b0"
}
```

## scan_triggers candidates  (2026-05-13T19:20:54Z)

```
  GOOGL     score=0.9646  atr_pct=0.0238  [SELECTED]
  FCX       score=0.6850  atr_pct=0.0401  [SELECTED]
  AVGO      score=0.5283  atr_pct=0.0340  [SELECTED]
  SLB       score=0.5262  atr_pct=0.0300  [SELECTED]
  CSCO      score=0.5152  atr_pct=0.0225  [SELECTED]
  NVDA      score=0.4933  atr_pct=0.0290  [candidate]
  MRK       score=0.3639  atr_pct=0.0236  [SELECTED]
  JNJ       score=0.3590  atr_pct=0.0179  [SELECTED]
  MS        score=0.3539  atr_pct=0.0239  [SELECTED]
  XOM       score=0.3321  atr_pct=0.0279  [SELECTED]
  WELL      score=0.3318  atr_pct=0.0214  [SELECTED]
  WMT       score=0.3178  atr_pct=0.0203  [candidate]
  COP       score=0.2985  atr_pct=0.0303  [candidate]
  EQIX      score=0.2780  atr_pct=0.0190  [candidate]
  AAPL      score=0.2635  atr_pct=0.0207  [candidate]
  CVX       score=0.2490  atr_pct=0.0247  [candidate]
  NEE       score=0.2447  atr_pct=0.0222  [candidate]
  BA        score=0.2256  atr_pct=0.0275  [candidate]
  PLD       score=0.2117  atr_pct=0.0184  [candidate]
  TSLA      score=0.2058  atr_pct=0.0368  [candidate]
  AMZN      score=0.1893  atr_pct=0.0249  [candidate]
  UNP       score=0.1645  atr_pct=0.0184  [candidate]
  AEP       score=0.1592  atr_pct=0.0195  [candidate]
  UNH       score=0.1534  atr_pct=0.0232  [candidate]
  KO        score=0.1472  atr_pct=0.0162  [candidate]
  AMGN      score=0.1324  atr_pct=0.0224  [candidate]
  O         score=0.0931  atr_pct=0.0155  [candidate]
  COST      score=0.0702  atr_pct=0.0179  [candidate]
  DUK       score=0.0413  atr_pct=0.0161  [candidate]
  SO        score=0.0411  atr_pct=0.0167  [candidate]
```

## scan_triggers candidates  (2026-05-13T19:25:26Z)

```
  AMD       score=1.9869  atr_pct=0.0454  [SELECTED]
  GOOGL     score=0.9626  atr_pct=0.0239  [SELECTED]
  FCX       score=0.6851  atr_pct=0.0401  [SELECTED]
  AVGO      score=0.5277  atr_pct=0.0340  [SELECTED]
  SLB       score=0.5273  atr_pct=0.0300  [SELECTED]
  CSCO      score=0.5147  atr_pct=0.0225  [candidate]
  NVDA      score=0.4890  atr_pct=0.0291  [candidate]
  MRK       score=0.3636  atr_pct=0.0237  [SELECTED]
  JNJ       score=0.3581  atr_pct=0.0179  [SELECTED]
  MS        score=0.3543  atr_pct=0.0239  [SELECTED]
  WELL      score=0.3337  atr_pct=0.0214  [SELECTED]
  XOM       score=0.3335  atr_pct=0.0279  [SELECTED]
  WMT       score=0.3207  atr_pct=0.0203  [candidate]
  COP       score=0.2992  atr_pct=0.0303  [candidate]
  EQIX      score=0.2780  atr_pct=0.0190  [candidate]
  AAPL      score=0.2630  atr_pct=0.0207  [candidate]
  NEE       score=0.2452  atr_pct=0.0222  [candidate]
  SBUX      score=0.2443  atr_pct=0.0241  [candidate]
  PLD       score=0.2114  atr_pct=0.0184  [candidate]
  LLY       score=0.1994  atr_pct=0.0298  [candidate]
  AMZN      score=0.1882  atr_pct=0.0249  [candidate]
  LIN       score=0.1722  atr_pct=0.0190  [candidate]
  AEP       score=0.1574  atr_pct=0.0195  [candidate]
  KO        score=0.1478  atr_pct=0.0162  [candidate]
  AMGN      score=0.1329  atr_pct=0.0224  [candidate]
  O         score=0.0933  atr_pct=0.0155  [candidate]
  COST      score=0.0722  atr_pct=0.0178  [candidate]
  DUK       score=0.0410  atr_pct=0.0161  [candidate]
```

## scan_triggers candidates  (2026-05-13T19:28:23Z)

```
  GOOGL     score=0.9654  atr_pct=0.0238  [SELECTED]
  FCX       score=0.6850  atr_pct=0.0401  [SELECTED]
  AVGO      score=0.5275  atr_pct=0.0340  [SELECTED]
  SLB       score=0.5270  atr_pct=0.0300  [SELECTED]
  CSCO      score=0.5196  atr_pct=0.0224  [SELECTED]
  NVDA      score=0.4901  atr_pct=0.0290  [candidate]
  MRK       score=0.3655  atr_pct=0.0237  [SELECTED]
  JNJ       score=0.3591  atr_pct=0.0179  [SELECTED]
  MS        score=0.3542  atr_pct=0.0239  [SELECTED]
  WELL      score=0.3360  atr_pct=0.0214  [SELECTED]
  XOM       score=0.3335  atr_pct=0.0279  [SELECTED]
  WMT       score=0.3207  atr_pct=0.0203  [candidate]
  COP       score=0.2991  atr_pct=0.0303  [candidate]
  EQIX      score=0.2782  atr_pct=0.0190  [candidate]
  AAPL      score=0.2634  atr_pct=0.0207  [candidate]
  NEE       score=0.2465  atr_pct=0.0222  [candidate]
  LLY       score=0.1999  atr_pct=0.0298  [candidate]
  AMZN      score=0.1900  atr_pct=0.0249  [candidate]
  PM        score=0.1822  atr_pct=0.0252  [candidate]
  UNP       score=0.1665  atr_pct=0.0184  [candidate]
  KO        score=0.1475  atr_pct=0.0162  [candidate]
  AMGN      score=0.1332  atr_pct=0.0224  [candidate]
  O         score=0.0938  atr_pct=0.0155  [candidate]
  COST      score=0.0722  atr_pct=0.0178  [candidate]
  DUK       score=0.0415  atr_pct=0.0161  [candidate]
```

## scan_triggers candidates  (2026-05-13T19:29:34Z)

```
  CAT       score=1.1176  atr_pct=0.0296  [SELECTED]
  GOOGL     score=0.9651  atr_pct=0.0238  [SELECTED]
  FCX       score=0.6852  atr_pct=0.0401  [SELECTED]
  AVGO      score=0.5276  atr_pct=0.0340  [SELECTED]
  SLB       score=0.5269  atr_pct=0.0300  [SELECTED]
  CSCO      score=0.5210  atr_pct=0.0224  [SELECTED]
  NVDA      score=0.4905  atr_pct=0.0290  [candidate]
  MS        score=0.3544  atr_pct=0.0239  [SELECTED]
  XOM       score=0.3333  atr_pct=0.0279  [SELECTED]
  WMT       score=0.3208  atr_pct=0.0203  [SELECTED]
  COP       score=0.2995  atr_pct=0.0303  [candidate]
  EQIX      score=0.2782  atr_pct=0.0190  [SELECTED]
  AAPL      score=0.2633  atr_pct=0.0207  [candidate]
  CVX       score=0.2496  atr_pct=0.0247  [candidate]
  NEE       score=0.2461  atr_pct=0.0222  [candidate]
  SBUX      score=0.2461  atr_pct=0.0241  [candidate]
  EOG       score=0.2215  atr_pct=0.0270  [candidate]
  DE        score=0.2020  atr_pct=0.0253  [candidate]
  LLY       score=0.1997  atr_pct=0.0298  [candidate]
  AMZN      score=0.1903  atr_pct=0.0249  [candidate]
  LIN       score=0.1728  atr_pct=0.0190  [candidate]
  UNP       score=0.1666  atr_pct=0.0184  [candidate]
  AEP       score=0.1597  atr_pct=0.0195  [candidate]
  UNH       score=0.1538  atr_pct=0.0232  [candidate]
  KO        score=0.1473  atr_pct=0.0162  [candidate]
  AMGN      score=0.1333  atr_pct=0.0224  [candidate]
  O         score=0.0939  atr_pct=0.0155  [candidate]
  SO        score=0.0425  atr_pct=0.0167  [candidate]
  DUK       score=0.0422  atr_pct=0.0161  [candidate]
```

## scan_triggers candidates  (2026-05-13T19:31:28Z)

```
  GOOGL     score=0.9672  atr_pct=0.0238  [SELECTED]
  FCX       score=0.6862  atr_pct=0.0401  [SELECTED]
  SLB       score=0.5278  atr_pct=0.0300  [SELECTED]
  AVGO      score=0.5263  atr_pct=0.0340  [SELECTED]
  CSCO      score=0.5231  atr_pct=0.0224  [SELECTED]
  NVDA      score=0.4904  atr_pct=0.0290  [candidate]
  MRK       score=0.3660  atr_pct=0.0237  [SELECTED]
  MS        score=0.3550  atr_pct=0.0239  [SELECTED]
  WELL      score=0.3371  atr_pct=0.0213  [SELECTED]
  XOM       score=0.3332  atr_pct=0.0279  [SELECTED]
  WMT       score=0.3203  atr_pct=0.0203  [SELECTED]
  COP       score=0.2995  atr_pct=0.0303  [candidate]
  EQIX      score=0.2778  atr_pct=0.0190  [candidate]
  AAPL      score=0.2643  atr_pct=0.0207  [candidate]
  CVX       score=0.2494  atr_pct=0.0247  [candidate]
  NEE       score=0.2465  atr_pct=0.0222  [candidate]
  SBUX      score=0.2465  atr_pct=0.0241  [candidate]
  BA        score=0.2239  atr_pct=0.0275  [candidate]
  AMZN      score=0.1924  atr_pct=0.0248  [candidate]
  LIN       score=0.1731  atr_pct=0.0190  [candidate]
  UNP       score=0.1666  atr_pct=0.0184  [candidate]
  AEP       score=0.1599  atr_pct=0.0195  [candidate]
  APD       score=0.1480  atr_pct=0.0199  [candidate]
  KO        score=0.1473  atr_pct=0.0162  [candidate]
  AMGN      score=0.1335  atr_pct=0.0224  [candidate]
  O         score=0.0941  atr_pct=0.0155  [candidate]
  SO        score=0.0425  atr_pct=0.0167  [candidate]
  DUK       score=0.0422  atr_pct=0.0161  [candidate]
```

## scan_triggers candidates  (2026-05-13T19:33:17Z)

```
  CAT       score=1.1147  atr_pct=0.0296  [SELECTED]
  GOOGL     score=0.9659  atr_pct=0.0238  [SELECTED]
  FCX       score=0.6837  atr_pct=0.0401  [SELECTED]
  SLB       score=0.5274  atr_pct=0.0300  [SELECTED]
  AVGO      score=0.5262  atr_pct=0.0340  [SELECTED]
  CSCO      score=0.5230  atr_pct=0.0224  [SELECTED]
  NVDA      score=0.4900  atr_pct=0.0290  [candidate]
  GS        score=0.4071  atr_pct=0.0246  [SELECTED]
  JNJ       score=0.3575  atr_pct=0.0179  [SELECTED]
  MS        score=0.3550  atr_pct=0.0239  [SELECTED]
  XOM       score=0.3332  atr_pct=0.0279  [SELECTED]
  WMT       score=0.3197  atr_pct=0.0203  [candidate]
  COP       score=0.2998  atr_pct=0.0303  [candidate]
  EQIX      score=0.2775  atr_pct=0.0190  [candidate]
  AAPL      score=0.2647  atr_pct=0.0207  [candidate]
  NEE       score=0.2455  atr_pct=0.0222  [candidate]
  DE        score=0.2022  atr_pct=0.0253  [candidate]
  LLY       score=0.1980  atr_pct=0.0298  [candidate]
  AMZN      score=0.1916  atr_pct=0.0249  [candidate]
  PM        score=0.1840  atr_pct=0.0252  [candidate]
  LIN       score=0.1728  atr_pct=0.0190  [candidate]
  AEP       score=0.1597  atr_pct=0.0195  [candidate]
  APD       score=0.1475  atr_pct=0.0199  [candidate]
  KO        score=0.1472  atr_pct=0.0162  [candidate]
  AMGN      score=0.1331  atr_pct=0.0224  [candidate]
  O         score=0.0937  atr_pct=0.0155  [candidate]
  BLK       score=0.0788  atr_pct=0.0224  [candidate]
  COST      score=0.0714  atr_pct=0.0178  [candidate]
  DUK       score=0.0417  atr_pct=0.0161  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T191802-96f2f659",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T191802-18409f90",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "bb76adaaa3a137839ea6a6e36221b143d5507627f36b4ecafb9fbc26a9191962"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T194248-443e3330",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T194248-906185c5",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "dcff63570263ad5c9f552b8262359c61011999506976aa8ec11bcc560c0b564e"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T195237-44315e0f",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T195237-5718ffd8",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "991ddff373b8320cc98b22ac42bfdb8bcce001d7a272eaacefc755359f8bcdc5"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T195458-775d7200",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T195458-693404f6",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "ef30dc53c1cd77dcd1b94c6a21b32032359febc1576cd221304f5a9b29414784"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T200808-c64dafef",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T200808-ea97b7d2",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "24d74548e1ad4b704ec8c4e127ba25c5d85aa5ecb8721996ede9fe7fef032363"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T200814-17f2bc00",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T200814-88cb2547",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "ef2e7ac1a3da5e072afe2b14a8eb358cb9464e18c9e9338f0d9b0442a52cb30b"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T200822-2d9cbeaa",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T200822-a5181b09",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "566e9820796b4b3cce55be0a3a01c91bd377ae55d25980941131c5b8a53ca615"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T200827-ddab4bf6",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T200827-2a32424e",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "c574ea23d700ec7613216dbeacf275653468e60e5d3669ca742b211b9edc5d0f"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T200833-3da71461",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T200833-eb474cfe",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "513bf6601290146c0c86ccb792a1dfacc9b4145a3a24ff47bfe42450df5bb3ab"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T201013-eeb38237",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T201013-12222448",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "3671c8e3e3d8c8c9a289557b37dfc9957b6afbb6800567b374272d49d3fd4aa0"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T205525-01f83454",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T205525-16f2ec0f",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "2c5dba1d457a00ef731a7fba960eb3044e76688320ef6ff452592015a0e694d1"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T205704-cafe11c0",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T205704-465c86ac",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "685e35187fabdd9a06941456f29bba557328122d306d605335330fc7b660a41b"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T205713-e968aec1",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T205713-176f5a2d",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "d338f7d77f27e49a4f600159d17b32e33466ea9dbe823f95e970a7ab70739169"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T205723-998ae2b2",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T205724-6e098438",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "a76be8d07fc355f91e43d9676c61d04a8581235d2e2d4e4bef4d08c8ac6e769b"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T205815-c4fc35c3",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T205815-3bba4dc1",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "49a0d5bb462df2aae5490d78e2395ac60db91fb42405077ec7cfa29446e36e9e"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T212737-b6e4eb10",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T212737-5f05d38d",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "63eac28dac4c3292ea76dc1906317544a528b1fefce196785aa01a2dbeb15271"
}
```
## Lineage Snapshot — 2026-05-13T21:27:46Z

**Run ID:** `lineage-20260513T212746-f5836379`  **Records:** 3 (complete: 3, partial: 0)

- WELL BUY cid=TOS-20260513T160035-WELL-BUY trigger_hash=d52e92b99f63 trigger_ids=[SPY_REGIME_200DMA_V1, STOCK_TREND_200DMA_V1, LIQUIDITY_GATE_V1…] status=complete_recovered_from_trigger_history
- JNJ BUY cid=TOS-20260513T192526-JNJ-BUY trigger_hash=d779e66ad03b trigger_ids=[SPY_REGIME_200DMA_V1, STOCK_TREND_200DMA_V1, LIQUIDITY_GATE_V1…] status=complete_recovered_from_trigger_history
- EQIX BUY cid=TOS-20260513T192934-EQIX-BUY trigger_hash=d779e66ad03b trigger_ids=[ATR_SIZING_V1, LIQUIDITY_GATE_V1, MOMENTUM_BLEND_6M_12M_V1…] status=complete_recovered_from_trigger_history

---

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T213918-0ab59141",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T213918-93f2bbb6",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "7259d36acd592961981bc4552c8862eddbc4aa1770282b7b05b4701eb688c235"
}
```

## scan_triggers candidates  (2026-05-13T21:50:26Z)

```
  GOOGL     score=0.9642  atr_pct=0.0238  [SELECTED]
  FCX       score=0.6790  atr_pct=0.0402  [SELECTED]
  CSCO      score=0.5329  atr_pct=0.0224  [SELECTED]
  AVGO      score=0.5223  atr_pct=0.0341  [SELECTED]
  NVDA      score=0.4859  atr_pct=0.0291  [candidate]
  GS        score=0.4074  atr_pct=0.0246  [SELECTED]
  MS        score=0.3506  atr_pct=0.0241  [SELECTED]
  XOM       score=0.3356  atr_pct=0.0279  [SELECTED]
  WMT       score=0.3222  atr_pct=0.0202  [SELECTED]
  EQIX      score=0.2694  atr_pct=0.0191  [SELECTED]
  NEE       score=0.2403  atr_pct=0.0223  [SELECTED]
  LIN       score=0.1755  atr_pct=0.0190  [candidate]
  APD       score=0.1477  atr_pct=0.0199  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T220916-93328892",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T220916-9c1f2ef6",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "f344e03a736ea769da059ff98499639a59a6489fdef423ce333fdc458da817c7"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260513T221046-7ca724ab",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260513T221046-7a199ca2",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "6bebf18a080ca883f89a8049ff866dac885792b8c9073ad3eed126afdc02f3aa"
}
```

## scan_triggers candidates  (2026-05-14T13:46:27Z)

```
  GOOGL     score=0.9429  atr_pct=0.0236  [SELECTED]
  CSCO      score=0.7624  atr_pct=0.0260  [SELECTED]
  FCX       score=0.6357  atr_pct=0.0403  [SELECTED]
  AVGO      score=0.5422  atr_pct=0.0334  [SELECTED]
  NVDA      score=0.4992  atr_pct=0.0284  [candidate]
  XOM       score=0.3316  atr_pct=0.0268  [SELECTED]
  WMT       score=0.3280  atr_pct=0.0197  [SELECTED]
  EQIX      score=0.2769  atr_pct=0.0185  [SELECTED]
  COP       score=0.2729  atr_pct=0.0291  [SELECTED]
  AAPL      score=0.2407  atr_pct=0.0203  [candidate]
  NEE       score=0.2056  atr_pct=0.0216  [SELECTED]
  AMZN      score=0.1838  atr_pct=0.0241  [SELECTED]
  TSLA      score=0.1715  atr_pct=0.0356  [candidate]
  KO        score=0.1406  atr_pct=0.0159  [candidate]
  O         score=0.0994  atr_pct=0.0149  [candidate]
  CL        score=0.0568  atr_pct=0.0209  [candidate]
  SO        score=0.0550  atr_pct=0.0160  [candidate]
```

## scan_triggers candidates  (2026-05-14T13:48:13Z)

```
  GOOGL     score=0.9400  atr_pct=0.0236  [SELECTED]
  CSCO      score=0.7564  atr_pct=0.0261  [SELECTED]
  AVGO      score=0.5351  atr_pct=0.0335  [SELECTED]
  SLB       score=0.5058  atr_pct=0.0291  [SELECTED]
  NVDA      score=0.4990  atr_pct=0.0284  [candidate]
  XOM       score=0.3331  atr_pct=0.0268  [SELECTED]
  EQIX      score=0.2769  atr_pct=0.0185  [SELECTED]
  COP       score=0.2723  atr_pct=0.0291  [candidate]
  AAPL      score=0.2427  atr_pct=0.0203  [candidate]
  NEE       score=0.2073  atr_pct=0.0216  [SELECTED]
  AMZN      score=0.1809  atr_pct=0.0241  [SELECTED]
  TSLA      score=0.1712  atr_pct=0.0356  [SELECTED]
  AEP       score=0.1650  atr_pct=0.0188  [SELECTED]
  KO        score=0.1420  atr_pct=0.0158  [candidate]
  O         score=0.0995  atr_pct=0.0149  [candidate]
  SO        score=0.0553  atr_pct=0.0160  [candidate]
```

## scan_triggers candidates  (2026-05-14T13:53:52Z)

```
  GOOGL     score=0.9355  atr_pct=0.0237  [SELECTED]
  CSCO      score=0.7674  atr_pct=0.0260  [SELECTED]
  FCX       score=0.6358  atr_pct=0.0403  [SELECTED]
  AVGO      score=0.5348  atr_pct=0.0335  [SELECTED]
  SLB       score=0.5043  atr_pct=0.0292  [SELECTED]
  NVDA      score=0.4934  atr_pct=0.0285  [candidate]
  MS        score=0.3366  atr_pct=0.0237  [SELECTED]
  XOM       score=0.3323  atr_pct=0.0268  [SELECTED]
  WMT       score=0.3302  atr_pct=0.0197  [SELECTED]
  EQIX      score=0.2769  atr_pct=0.0185  [SELECTED]
  COP       score=0.2739  atr_pct=0.0291  [candidate]
  AAPL      score=0.2412  atr_pct=0.0203  [candidate]
  SBUX      score=0.2400  atr_pct=0.0240  [SELECTED]
  NEE       score=0.2116  atr_pct=0.0215  [candidate]
  AMZN      score=0.1815  atr_pct=0.0241  [candidate]
  TSLA      score=0.1693  atr_pct=0.0357  [candidate]
  AEP       score=0.1664  atr_pct=0.0187  [candidate]
  KO        score=0.1434  atr_pct=0.0158  [candidate]
  O         score=0.1004  atr_pct=0.0149  [candidate]
```

## scan_triggers candidates  (2026-05-14T13:55:03Z)

```
  GOOGL     score=0.9341  atr_pct=0.0237  [SELECTED]
  CSCO      score=0.7651  atr_pct=0.0260  [SELECTED]
  FCX       score=0.6352  atr_pct=0.0403  [SELECTED]
  AVGO      score=0.5303  atr_pct=0.0336  [SELECTED]
  SLB       score=0.5069  atr_pct=0.0291  [SELECTED]
  NVDA      score=0.4910  atr_pct=0.0286  [candidate]
  XOM       score=0.3328  atr_pct=0.0268  [SELECTED]
  WMT       score=0.3297  atr_pct=0.0197  [SELECTED]
  EQIX      score=0.2769  atr_pct=0.0185  [SELECTED]
  COP       score=0.2753  atr_pct=0.0290  [candidate]
  AAPL      score=0.2413  atr_pct=0.0203  [candidate]
  NEE       score=0.2114  atr_pct=0.0215  [SELECTED]
  AMZN      score=0.1786  atr_pct=0.0242  [SELECTED]
  TSLA      score=0.1684  atr_pct=0.0357  [candidate]
  KO        score=0.1437  atr_pct=0.0158  [candidate]
  O         score=0.1015  atr_pct=0.0149  [candidate]
  CL        score=0.0610  atr_pct=0.0209  [candidate]
  SO        score=0.0562  atr_pct=0.0160  [candidate]
## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260514T140837-0eb8fca0",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260514T140837-d276e3c2",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "91e5936d38bf90e62417d2b76ccc604e31394789fc57dec82db753e8074f97f4"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260514T140844-014b1461",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260514T140844-b3bd8501",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "667387c32728a17a365857ae5a9774827b81cba1ce6987e7445c733cded4c0bd"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260514T140849-d697249a",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260514T140850-8a6ad831",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "fe4a6589f58550795340002dcf3fccfdcf242e51cb74f1da25bd918067448b5e"
}
```

## scan_triggers candidates  (2026-05-14T14:16:25Z)

```
  GOOGL     score=0.9292  atr_pct=0.0237  [SELECTED]
  CSCO      score=0.7436  atr_pct=0.0263  [SELECTED]
  FCX       score=0.6266  atr_pct=0.0408  [SELECTED]
  AVGO      score=0.5409  atr_pct=0.0334  [SELECTED]
  SLB       score=0.5111  atr_pct=0.0290  [SELECTED]
  NVDA      score=0.4934  atr_pct=0.0285  [candidate]
  XOM       score=0.3330  atr_pct=0.0268  [SELECTED]
  WMT       score=0.3282  atr_pct=0.0197  [SELECTED]
  COP       score=0.2757  atr_pct=0.0290  [candidate]
  EQIX      score=0.2712  atr_pct=0.0187  [SELECTED]
  AAPL      score=0.2436  atr_pct=0.0203  [candidate]
  NEE       score=0.2100  atr_pct=0.0216  [SELECTED]
  DE        score=0.1985  atr_pct=0.0244  [SELECTED]
  AMZN      score=0.1730  atr_pct=0.0244  [candidate]
  TSLA      score=0.1687  atr_pct=0.0358  [candidate]
  KO        score=0.1437  atr_pct=0.0158  [candidate]
  O         score=0.1010  atr_pct=0.0149  [candidate]
  SO        score=0.0573  atr_pct=0.0161  [candidate]
```
## Lineage Snapshot — 2026-05-14T14:16:25Z

**Run ID:** `lineage-20260514T141625-5c83a59b`  **Records:** 3 (complete: 0, partial: 3)

- WELL BUY cid=TOS-20260513T160035-WELL-BUY trigger_hash=null trigger_ids=[none] status=partial_missing_trigger_snapshot_hash
- JNJ BUY cid=TOS-20260513T192526-JNJ-BUY trigger_hash=null trigger_ids=[none] status=partial_missing_trigger_snapshot_hash
- EQIX BUY cid=TOS-20260513T192934-EQIX-BUY trigger_hash=null trigger_ids=[ATR_SIZING_V1, LIQUIDITY_GATE_V1, MOMENTUM_BLEND_6M_12M_V1…] status=partial_missing_trigger_snapshot_hash

---
## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260514T141321-7ab7bc7d",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260514T141321-7982e9b6",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "7b2b6d3e0b35cb66581c7d419040e982f2fce3e3112ce5128bd8945f1baba7ae"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260514T142018-74e11824",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260514T142018-635c1e26",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "d5ef7e6ab917f7c751f192f115dfdc5556312ea7fd67f6070c40ca5c4f5c651f"
}
```

## scan_triggers candidates  (2026-05-14T14:55:02Z)

```
  GOOGL     score=0.9285  atr_pct=0.0238  [SELECTED]
  CSCO      score=0.7467  atr_pct=0.0263  [SELECTED]
  FCX       score=0.6222  atr_pct=0.0409  [SELECTED]
  NVDA      score=0.5142  atr_pct=0.0287  [SELECTED]
  SLB       score=0.5024  atr_pct=0.0292  [SELECTED]
  XOM       score=0.3249  atr_pct=0.0270  [SELECTED]
  WMT       score=0.3239  atr_pct=0.0198  [SELECTED]
  EQIX      score=0.2762  atr_pct=0.0186  [SELECTED]
  AAPL      score=0.2428  atr_pct=0.0203  [candidate]
  NEE       score=0.2069  atr_pct=0.0216  [SELECTED]
  DE        score=0.1910  atr_pct=0.0246  [SELECTED]
  TSLA      score=0.1738  atr_pct=0.0357  [candidate]
  AMZN      score=0.1713  atr_pct=0.0246  [candidate]
  AEP       score=0.1614  atr_pct=0.0190  [candidate]
  KO        score=0.1452  atr_pct=0.0158  [candidate]
  O         score=0.1003  atr_pct=0.0150  [candidate]
  BLK       score=0.0825  atr_pct=0.0216  [candidate]
  CL        score=0.0666  atr_pct=0.0211  [candidate]
  SO        score=0.0528  atr_pct=0.0162  [candidate]
```
## Lineage Snapshot — 2026-05-14T14:55:09Z

**Run ID:** `lineage-20260514T145509-dd18af53`  **Records:** 3 (complete: 0, partial: 3)

- WELL BUY cid=TOS-20260513T160035-WELL-BUY trigger_hash=null trigger_ids=[none] status=partial_missing_trigger_snapshot_hash
- JNJ BUY cid=TOS-20260513T192526-JNJ-BUY trigger_hash=null trigger_ids=[none] status=partial_missing_trigger_snapshot_hash
- EQIX BUY cid=TOS-20260513T192934-EQIX-BUY trigger_hash=null trigger_ids=[ATR_SIZING_V1, LIQUIDITY_GATE_V1, MOMENTUM_BLEND_6M_12M_V1…] status=partial_missing_trigger_snapshot_hash

---

## scan_triggers candidates  (2026-05-14T14:56:25Z)

```
  AMD       score=1.9585  atr_pct=0.0447  [SELECTED]
  GOOGL     score=0.9288  atr_pct=0.0238  [SELECTED]
  CSCO      score=0.7504  atr_pct=0.0262  [SELECTED]
  FCX       score=0.6244  atr_pct=0.0408  [SELECTED]
  AVGO      score=0.5560  atr_pct=0.0334  [candidate]
  NVDA      score=0.5122  atr_pct=0.0288  [candidate]
  SLB       score=0.5049  atr_pct=0.0292  [SELECTED]
  MRK       score=0.3600  atr_pct=0.0231  [SELECTED]
  XOM       score=0.3245  atr_pct=0.0270  [SELECTED]
  WMT       score=0.3227  atr_pct=0.0198  [SELECTED]
  EQIX      score=0.2790  atr_pct=0.0185  [SELECTED]
  AAPL      score=0.2430  atr_pct=0.0203  [candidate]
  NEE       score=0.2068  atr_pct=0.0216  [SELECTED]
  DE        score=0.1950  atr_pct=0.0245  [candidate]
  TSLA      score=0.1725  atr_pct=0.0358  [candidate]
  AMZN      score=0.1701  atr_pct=0.0246  [candidate]
  AEP       score=0.1614  atr_pct=0.0190  [candidate]
  KO        score=0.1451  atr_pct=0.0158  [candidate]
  O         score=0.1006  atr_pct=0.0150  [candidate]
  COST      score=0.0754  atr_pct=0.0174  [candidate]
  CL        score=0.0664  atr_pct=0.0211  [candidate]
  SO        score=0.0537  atr_pct=0.0161  [candidate]
```
## Lineage Snapshot — 2026-05-14T14:56:34Z

**Run ID:** `lineage-20260514T145634-50dad7cb`  **Records:** 3 (complete: 0, partial: 3)

- WELL BUY cid=TOS-20260513T160035-WELL-BUY trigger_hash=null trigger_ids=[none] status=partial_missing_trigger_snapshot_hash
- JNJ BUY cid=TOS-20260513T192526-JNJ-BUY trigger_hash=null trigger_ids=[none] status=partial_missing_trigger_snapshot_hash
- EQIX BUY cid=TOS-20260513T192934-EQIX-BUY trigger_hash=null trigger_ids=[ATR_SIZING_V1, LIQUIDITY_GATE_V1, MOMENTUM_BLEND_6M_12M_V1…] status=partial_missing_trigger_snapshot_hash

---
