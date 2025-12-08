```yaml
DISTANCE_TRADE_FACTOR:
  def: '-0.02'
  type: float
  cmt: Trade factor is modified by distance times this
RELATION_TRADE_FACTOR:
  def: '1'
  type: int
  cmt: Trade factor is modified by Opinion value times this
ALLOW_TRADE_CUT_OFF:
  def: '0'
  type: int
  cmt: If trade factor is less than this, no trade will be allowed
MONTH_TRADE_FACTOR:
  def: '2'
  type: int
  cmt: Each month a trade gets this much boost to it's trade factor
MAX_MONTH_TRADE_FACTOR:
  def: '50'
  type: int
  cmt: This is the maximum bonus that can be gained from time
BASE_TRADE_FACTOR:
  def: '150'
  type: int
  cmt: This is the base trade factor
PUPPET_MASTER_TRADE_FACTOR:
  def: '400'
  type: int
  cmt: This is priority for puppet master
PUPPET_TRADE_FACTOR:
  def: '0'
  type: int
  cmt: This is unpriority for puppets
BASE_LAND_TRADE_RANGE:
  def: '1000'
  type: int
PARTY_SUPPORT_TRADE_FACTOR:
  def: '50'
  type: int
  cmt: Trade factor bonus at the other side having 100 % party popularity for my party
ANTI_MONOPOLY_TRADE_FACTOR_THRESHOLD:
  def: '0.5'
  type: float
  cmt: What percentage of resources has to be sold to the buyer for the anti-monopoly
    factor to take effect
ANTI_MONOPOLY_TRADE_FACTOR:
  def: '-100'
  type: int
  cmt: This is added to the factor value when anti-monopoly threshold is exceeded
NAVAL_ROUTE_ACCESS_AVOID_COST_MULT:
  def: '1'
  type: int
  cmt: Naval pathfinding should avoid certain regions that you mark. High "cost
    multiplier" will make it less willingly go through a specific region.
```
