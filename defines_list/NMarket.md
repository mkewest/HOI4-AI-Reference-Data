---
domain: defines_list
concept: NMarket
version: 1.14+
requires: [defines]
relates: [market, trade]
---

```yaml
PURCHASE_CONTRACT_DELIVERY_TOTAL_DAYS:
  def: '30'
  type: int
  cmt: Number of days between purchase contract deliveries
MAX_CIV_FACTORIES_PER_CONTRACT:
  def: '15'
  type: int
  cmt: Max number of factories that can be assigned for paying single contract.
HIGH_PRICE_LEVEL_FACTOR:
  def: '1.25'
  type: float
  cmt: The factor of base equipment price for high price level. Should be more than
    1.
PURCHASE_CONTRACT_SUBSIDY_BONUS_SPEED_FACTOR:
  def: '1.0'
  type: float
  cmt: The factor of speed bonus from subsidies
REQUEST_AUTOMATION_AUTO_ACCEPT_MARKET_ACCESS_DEFAULT:
  def: 'true'
  type: bool
  cmt: Whether by default should accept market access requests from other countries.
REQUEST_AUTOMATION_AUTO_ACCEPT_PURCHASE_DEFAULT:
  def: 'false'
  type: bool
  cmt: Whether by default should accept purchase requests from other countries.
CONTRACT_ESTIMATE_AVERAGE_DAILY_PRODUCTION_ALPHA:
  def: '0.5'
  type: float
  cmt: How strong effect should have the daily production on the average (1.0 means
    it will use only the new number as average)
CONTRACT_ESTIMATE_AVERAGE_DAILY_PRODUCTION_SNAP_LIMIT:
  def: '1.5'
  type: float
  cmt: If the difference between current and estimated daily production is smaller
    then this value, we will use the current value for calculations.
CONTRACT_ESTIMATE_AVERAGE_CONVOY_SUNK_MULTIPLIER_SNAP_LIMIT:
  def: '0.05'
  type: float
  cmt: If the difference between current and estimated sunk efficiency convoy count
    is smaller then this value, we will use the current value for calculations.
```
