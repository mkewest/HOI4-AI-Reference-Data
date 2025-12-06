---
domain: defines_list
concept: NProduction
version: 1.14+
requires: [defines]
relates: [production, equipment]
---

```yaml
MAX_EQUIPMENT_RESOURCES_NEED:
  def: '3'
  type: int
  cmt: Max number of different strategic resources an equipment can be dependent on.
DEFAULT_MAX_NAV_FACTORIES_PER_LINE:
  def: '10'
  type: int
CONVOY_MAX_NAV_FACTORIES_PER_LINE:
  def: '15'
  type: int
MAX_MIL_FACTORIES_PER_LINE:
  def: '150'
  type: int
RAILWAY_GUN_REPAIR_SPEED:
  def: '8.0'
  type: float
  cmt: Railway gun strength repair speed per factory
RESOURCE_PENALTY_WARNING_CRITICAL_RATIO:
  def: '0.8'
  type: float
  cmt: Switch to red progress bar if penalty is over threshold
BASE_FACTORY_SPEED_MIL:
  def: '4.50'
  type: float
  cmt: Base factory speed multiplier (how much hoi3 style IC each factory gives).
BASE_FACTORY_START_EFFICIENCY_FACTOR:
  def: '10'
  type: int
  cmt: Base start efficiency for factories expressed in %.
BASE_FACTORY_EFFICIENCY_GAIN:
  def: '1'
  type: int
  cmt: Base efficiency factor.
BASE_FACTORY_EFFICIENCY_VARIANT_CHANGE_FACTOR:
  def: '90'
  type: int
  cmt: Base factor for changing production variants in %.
BASE_FACTORY_EFFICIENCY_FAMILY_CHANGE_FACTOR:
  def: '70'
  type: int
  cmt: Base factor for changing production with same family in %.
EQUIPMENT_BASE_LEND_LEASE_WEIGHT:
  def: '1.0'
  type: float
  cmt: Base equipment lend lease weight
LEND_LEASE_DELIVERY_TOTAL_DAYS:
  def: '30'
  type: int
  cmt: Nr of days between lend lease deliveries
ANNEX_FIELD_EQUIPMENT_RATIO:
  def: '0.25'
  type: float
  cmt: How much equipment from deployed divisions will be transferred on annexation
ANNEX_CONVOYS_RATIO:
  def: '0.15'
  type: float
  cmt: How many convoys will be transferred on annexation
MIN_FIELD_TO_TRAINING_MANPOWER_RATIO:
  def: '0.75'
  type: float
  cmt: Ratio which % of army in field can be trained
CAPITULATE_FUEL_RATIO:
  def: '0.5'
  type: float
  cmt: How much fuel will be transferred on capitulation
PRODUCTION_RESOURCE_LACK_PENALTY:
  def: '-0.05'
  type: float
  cmt: Penalty decrease while lack of resource per factory
MIN_LICENSE_ACTIVE_DAYS:
  def: '30'
  type: int
  cmt: Min days for license to be active
LICENSE_IC_COST_YEAR_INCREASE:
  def: '1'
  type: int
  cmt: IC cost equipment for every year of equipment after 1936
LICENSE_EQUIPMENT_TECH_SPEED_PER_YEAR:
  def: '-0.05'
  type: float
  cmt: MIC speed modifier for licensed equipment for each year of difference between
    actual and latest equipment
LICENSE_EQUIPMENT_SPEED_NOT_FACTION:
  def: '-0.10'
  type: float
  cmt: MIC speed modifier for licensed equipment for not being in faction
LICENSE_EQUIPMENT_SPEED_NO_LICENSE:
  def: '-0.50'
  type: float
  cmt: Penalty for producing non licensed equipment
EQUIPMENT_MODULE_ADD_XP_COST:
  def: '5.0'
  type: float
  cmt: XP cost for adding a new equipment module in an empty slot when creating an
    equipment variant.
EQUIPMENT_MODULE_CONVERT_XP_COST:
  def: '3.0'
  type: float
  cmt: XP cost for converting one equipment module to a related module when creating
    an equipment variant.
BASE_NAVAL_EQUIPMENT_CONVERSION_IC_COST_FACTOR:
  def: '0.2'
  type: float
  cmt: Fraction of the hull industry cost which is always included in the refitting
    cost.
MIN_NAVAL_EQUIPMENT_CONVERSION_RESOURCE_COST_FACTOR:
  def: '0.2'
  type: float
  cmt: Minimum fraction of a naval equipment's strategic resource cost that any conversion
    will cost.
SHIP_REFIT_MAX_PROGRESS_TO_CANCEL:
  def: '0.2'
  type: float
  cmt: Maximum refitting progress % that we still allow to cancel wihtout having to
    scuttle the ship.
MINIMUM_NUMBER_OF_FACTORIES_TAKEN_BY_CONSUMER_GOODS_VALUE:
  def: '1'
  type: int
  cmt: The minimum number of factories we have to put on consumer goods, by value.
INITIAL_ALLOWED_FACTORY_RATIO_FOR_REPAIRS:
  def: '1.0'
  type: float
  cmt: max % of factories allowed on autorepairs
```
