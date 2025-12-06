---
domain: defines_list
concept: NBuildings
version: 1.14+
requires: [defines]
relates: [buildings]
---

```yaml
ANTI_AIR_SUPERIORITY_MULT:
  def: '5.0'
  type: float
  cmt: How much air superiority reduction to the enemy does our AA guns? Normally
    each building level = -1 reduction. With this multiplier.
  use: '|-'
MAX_BUILDING_LEVELS:
  def: '15'
  type: int
  cmt: Max levels a building can have.
ROCKETSITE_CAPACITY_MULT:
  def: '100'
  type: int
  cmt: Each level of rocketsite building multiplied by this, gives capacity (max operational
    value). Value is int. 1 for each rocket.
RADAR_RANGE_BASE:
  def: '20'
  type: int
  cmt: Radar range base, first level radar will be this + min, best radar will be
    this + max
RADAR_RANGE_MAX:
  def: '200'
  type: int
  cmt: Range is interpolated between building levels 1-15.
SABOTAGE_FACTORY_DAMAGE:
  def: '100.0'
  type: float
  cmt: How much damage takes a factory building in sabotage when state is occupied.
    Damage is mult by (1 + resistance strength), i.e. up to 2 x base value.
BASE_FACTORY_REPAIR_FACTOR:
  def: '2.0'
  type: float
  cmt: Factory speed modifier when repairing.
MAX_SHARED_SLOTS:
  def: '25'
  type: int
  cmt: Max slots shared by factories
DESTRUCTION_COOLDOWN_IN_WAR:
  def: '30'
  type: int
  cmt: Number of days cooldown between removal of buildings in war times
SUPPLY_ROUTE_RESOURCE_BONUS:
  def: '0.2'
  type: float
  cmt: multiplicative resource bonus for having a railway/naval connection to the
    capital
```
