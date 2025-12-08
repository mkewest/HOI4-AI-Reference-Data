---
domain: defines_list
concept: NMarket
version: 1.17.2
requires: [defines]
relates: [market, trade]
---

```yaml
PURCHASE_CONTRACT_DELIVERY_TOTAL_DAYS:
  def: '30'
  type: int
  cmt: Number of days between purchase contract deliveries
IC_TO_CIC_FACTOR:
  def: '2.0'
  type: float
  cmt: The factor for mapping IC cost to CIC cost. Should be a positive number.
MAX_CIV_FACTORIES_PER_CONTRACT:
  def: '15'
  type: int
  cmt: Max number of factories that can be assigned for paying single contract.
LOW_PRICE_LEVEL_FACTOR:
  def: '0.75'
  type: float
  cmt: The factor of base equipment price for low price level. Should be in range (0,1]
HIGH_PRICE_LEVEL_FACTOR:
  def: '1.25'
  type: float
  cmt: The factor of base equipment price for high price level. Should be more than 1.
MIN_DELIVERY_LIMIT_WARNING_UI:
  def: '0.8'
  type: float
  cmt: The delivery percentage under we want to let player know the contract is
    inefficient. [0,1]
PURCHASE_CONTRACT_SUBSIDY_BONUS_SPEED_FACTOR:
  def: '1.0'
  type: float
  cmt: The factor of speed bonus from subsidies
CONVOY_WEIGHT_OVERRIDE:
  def: '0.0'
  type: float
  cmt: Overrides the default lend leas weight of convoys for international market
REQUEST_AUTOMATION_AUTO_ACCEPT_MARKET_ACCESS_DEFAULT:
  def: 'true'
  type: bool
  cmt: Whether by default should accept market access requests from other countries.
REQUEST_AUTOMATION_AUTO_SEND_MARKET_ACCESS_DEFAULT:
  def: 'true'
  type: bool
  cmt: Whether by default should send market access requests to other countries.
REQUEST_AUTOMATION_AUTO_ACCEPT_PURCHASE_DEFAULT:
  def: 'false'
  type: bool
  cmt: Whether by default should accept purchase requests from other countries.
CONTRACT_ESTIMATE_AVERAGE_CONVOY_COUNT_ALPHA:
  def: '0.5'
  type: float
  cmt: How strong effect should have the daily convoy count on the average (1.0 means it
    will use only the new number as average)
CONTRACT_ESTIMATE_AVERAGE_DAILY_PRODUCTION_ALPHA:
  def: '0.5'
  type: float
  cmt: How strong effect should have the daily production on the average (1.0 means it
    will use only the new number as average)
CONTRACT_ESTIMATE_AVERAGE_CONVOY_COUNT_SNAP_LIMIT:
  def: '0.3'
  type: float
  cmt: If the difference between current and estimated available convoy count is smaller
    then this value, we will use the current value for calculations.
CONTRACT_ESTIMATE_AVERAGE_DAILY_PRODUCTION_SNAP_LIMIT:
  def: '1.5'
  type: float
  cmt: If the difference between current and estimated daily production is smaller then
    this value, we will use the current value for calculations.
CONTRACT_ESTIMATE_AVERAGE_CONVOY_SUNK_MULTIPLIER_ALPHA:
  def: '0.5'
  type: float
  cmt: How strong effect should have the daily sunk efficiency on the average (1.0 means
    it will use only the new number as average)
CONTRACT_ESTIMATE_AVERAGE_CONVOY_SUNK_MULTIPLIER_SNAP_LIMIT:
  def: '0.05'
  type: float
  cmt: If the difference between current and estimated sunk efficiency convoy count is
    smaller then this value, we will use the current value for calculations.
WARNING_CONVOYS_SUNK_MAX_DAYS:
  def: '30'
  type: int
  cmt: The contracts will show sunk convoy message if there was sunk convoy in this
    amount of days
```
