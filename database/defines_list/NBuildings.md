---
domain: defines_list
concept: NBuildings
version: 1.17.2
requires: [defines]
relates: [buildings]
---

```yaml
ANTI_AIR_SUPERIORITY_MULT:
  def: '5.0'
  type: float
  cmt: How much air superiority reduction to the enemy does our AA guns? Normally each
    building level = -1 reduction. With this multiplier.
SAM_MISSION_SUPERIORITY:
  def: '5.0'
  type: float
  cmt: How much air superiority each SAM mission gives per rocket wing performing SAM
    missions.
MAX_BUILDING_LEVELS:
  def: '15'
  type: int
  cmt: Max levels a building can have.
AIRBASE_CAPACITY_MULT:
  def: '200'
  type: int
  cmt: Each level of airbase building multiplied by this, gives capacity (max
    operational value). Value is int. 1 for each airplane.
ROCKETSITE_CAPACITY_MULT:
  def: '100'
  type: int
  cmt: Each level of rocketsite building multiplied by this, gives capacity (max
    operational value). Value is int. 1 for each rocket.
NAVALBASE_REPAIR_MULT:
  def: '0.05'
  type: float
  cmt: Each level of navalbase building repairs X strength and can repair as many ships
    as its level
RADAR_RANGE_BASE:
  def: '20'
  type: int
  cmt: Radar range base, first level radar will be this + min, best radar will be this +
    max
RADAR_RANGE_MIN:
  def: '20'
  type: int
  cmt: Radar range (from state center to province center) in measure of map pixels.
    Exluding techs.
RADAR_RANGE_MAX:
  def: '200'
  type: int
  cmt: Range is interpolated between building levels 1-15.
RADAR_INTEL_EFFECT:
  def: '40'
  type: int
  cmt: Province covered by radar increases intel by 10 (where 255 is max). Province may
    be covered by multiple radars, then the value sums up.
SABOTAGE_FACTORY_DAMAGE:
  def: '100.0'
  type: float
  cmt: How much damage takes a factory building in sabotage when state is occupied.
    Damage is mult by (1 + resistance strength), i.e. up to 2 x base value.
BASE_FACTORY_REPAIR:
  def: '1.0'
  type: float
  cmt: Default repair rate in percentage before factories are taken into account (1.0
    equals 1%).
BASE_FACTORY_REPAIR_FACTOR:
  def: '2.0'
  type: float
  cmt: Factory speed modifier when repairing.
SUPPLY_PORT_LEVEL_THROUGHPUT:
  def: '3'
  type: int
  cmt: supply throughput per level of naval base
MAX_SHARED_SLOTS:
  def: '25'
  type: int
  cmt: Max slots shared by factories
OWNER_CHANGE_EXTRA_SHARED_SLOTS_FACTOR:
  def: '1'
  type: int
  cmt: Scale factor of extra shared slots when state owner change.
DESTRUCTION_COOLDOWN_IN_WAR:
  def: '30'
  type: int
  cmt: Number of days cooldown between removal of buildings in war times
INFRASTRUCTURE_RESOURCE_BONUS:
  def: '0.15'
  type: float
  cmt: multiplicative resource bonus for each level of (non damaged) infrastructure
SUPPLY_ROUTE_RESOURCE_BONUS:
  def: '0.2'
  type: float
  cmt: multiplicative resource bonus for having a railway/naval connection to the
    capital
INFRASTRUCTURE_MUD_EFFECT:
  def: '-0.8'
  type: float
  cmt: multiplicative effect on mud growth for max infra
```
