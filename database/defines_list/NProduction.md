---
domain: defines_list
concept: NProduction
version: 1.17.2
requires: [defines]
relates: [production, equipment]
---

```yaml
MAX_EQUIPMENT_RESOURCES_NEED:
  def: '3'
  type: int
  cmt: Max number of different strategic resources an equipment can be dependent on.
MAX_CIV_FACTORIES_PER_LINE:
  def: '15'
  type: int
  cmt: Max number of factories that can be assigned a single production line.
DEFAULT_MAX_NAV_FACTORIES_PER_LINE:
  def: '10'
  type: int
FLOATING_HARBOR_MAX_NAV_FACTORIES_PER_LINE:
  def: '5'
  type: int
CONVOY_MAX_NAV_FACTORIES_PER_LINE:
  def: '15'
  type: int
CAPITAL_SHIP_MAX_NAV_FACTORIES_PER_LINE:
  def: '5'
  type: int
MAX_MIL_FACTORIES_PER_LINE:
  def: '150'
  type: int
MAX_MIL_FACTORIES_VISIBLE_FOR_MIL_EQUIPMENT_LINE:
  def: '15'
  type: int
RAILWAY_GUN_MAX_MIL_FACTORIES_PER_LINE:
  def: '5'
  type: int
RAILWAY_GUN_REPAIR_SPEED:
  def: '8.0'
  type: float
  cmt: Railway gun strength repair speed per factory
EFFICIENCY_LOSS_PER_UNUSED_DAY:
  def: '1'
  type: int
  cmt: Daily loss of efficiency for unused factory slots ( efficiency is tracked per
    factory slot in the production line )
RESOURCE_PENALTY_WARNING_CRITICAL_RATIO:
  def: '0.8'
  type: float
  cmt: Switch to red progress bar if penalty is over threshold
RESOURCE_TO_ENERGY_COEFFICIENT:
  def: '9.0'
  type: float
  cmt: How much energy per coal produces
BASE_COUNTRY_ENERGY_PRODUCTION:
  def: '10.0'
  type: float
  cmt: The base energy production of a country
ENERGY_SCALING_COST_BY_FACTORY_COUNT:
  def: '0.0225'
  type: float
  cmt: Scales energy cost based on the total number of factories
BASE_ENERGY_COST:
  def: '0.25'
  type: float
  cmt: How much energy per factory consumes
ENERGY_COST_CAP:
  def: '6'
  type: int
  cmt: Maximum energy cost per factory
ENERGY_SCALE_PER_TRADE_FACTORY_EXPORT:
  def: '0.25'
  type: float
  cmt: Factor of how many of the factories gained from trade is affects the energy cost
    scaling
BASE_FACTORY_SPEED:
  def: '4'
  type: int
  cmt: Base factory speed multiplier (how much hoi3 style IC each factory gives).
BASE_FACTORY_SPEED_MIL:
  def: '3.5'
  type: float
  cmt: Base factory speed multiplier (how much hoi3 style IC each factory gives).
BASE_FACTORY_SPEED_NAV:
  def: '2.0'
  type: float
  cmt: Base factory speed multiplier (how much hoi3 style IC each factory gives).
BASE_FACTORY_START_EFFICIENCY_FACTOR:
  def: '10'
  type: int
  cmt: Base start efficiency for factories expressed in %.
POWERED_FACTORY_SPEED:
  def: '5'
  type: int
  cmt: Powered factory speed multiplier.
POWERED_FACTORY_SPEED_MIL:
  def: '4.5'
  type: float
  cmt: Powered factory speed multiplier.
POWERED_FACTORY_SPEED_NAV:
  def: '2.5'
  type: float
  cmt: Powered factory speed multiplier.
BASE_FACTORY_MAX_EFFICIENCY_FACTOR:
  def: '50'
  type: int
  cmt: Base max efficiency for factories expressed in %.
BASE_FACTORY_EFFICIENCY_GAIN:
  def: '1'
  type: int
  cmt: Base efficiency factor.
BASE_FACTORY_EFFICIENCY_BALANCE_FACTOR:
  def: '0.1'
  type: float
  cmt: Factory efficiency balancing factor
BASE_FACTORY_EFFICIENCY_VARIANT_CHANGE_FACTOR:
  def: '90'
  type: int
  cmt: Base factor for changing production variants in %.
BASE_FACTORY_EFFICIENCY_PARENT_CHANGE_FACTOR:
  def: '30'
  type: int
  cmt: Base factor for changing production parent<->children in %.
BASE_FACTORY_EFFICIENCY_FAMILY_CHANGE_FACTOR:
  def: '70'
  type: int
  cmt: Base factor for changing production with same family in %.
BASE_FACTORY_EFFICIENCY_ARCHETYPE_CHANGE_FACTOR:
  def: '20'
  type: int
  cmt: Base factor for changing production with same archetype in %.
EQUIPMENT_BASE_LEND_LEASE_WEIGHT:
  def: '1.0'
  type: float
  cmt: Base equipment lend lease weight
EQUIPMENT_LEND_LEASE_WEIGHT_FACTOR:
  def: '0.01'
  type: float
  cmt: Base equipment lend lease factor
LEND_LEASE_DELIVERY_TOTAL_DAYS:
  def: '30'
  type: int
  cmt: Nr of days between lend lease deliveries
ANNEX_STOCKPILES_RATIO:
  def: '1.0'
  type: float
  cmt: How much stockpiled equipment will be transferred on annexation
ANNEX_FIELD_EQUIPMENT_RATIO:
  def: '0.25'
  type: float
  cmt: How much equipment from deployed divisions will be transferred on annexation
ANNEX_FUEL_RATIO:
  def: '0.25'
  type: float
  cmt: How much fuel will be transferred on annexation
ANNEX_CONVOYS_RATIO:
  def: '0.15'
  type: float
  cmt: How many convoys will be transferred on annexation
MIN_POSSIBLE_TRAINING_MANPOWER:
  def: '100000'
  type: int
  cmt: How many deployment lines minimum can be training
MIN_FIELD_TO_TRAINING_MANPOWER_RATIO:
  def: '0.75'
  type: float
  cmt: Ratio which % of army in field can be trained
CAPITULATE_STOCKPILES_RATIO:
  def: '0.5'
  type: float
  cmt: How much equipment from deployed divisions will be transferred on capitulation
CAPITULATE_FUEL_RATIO:
  def: '0.5'
  type: float
  cmt: How much fuel will be transferred on capitulation
INFRA_MAX_CONSTRUCTION_COST_EFFECT:
  def: '1'
  type: int
  cmt: Building in a state with higher infrastructure will reduce the cost of shared
    buildings.
PRODUCTION_RESOURCE_LACK_PENALTY:
  def: '-0.05'
  type: float
  cmt: Penalty decrease while lack of resource per factory
CIC_BANK_SPEED_BOOST_FACTOR:
  def: '0.25'
  type: float
  cmt: The CIC bank can boost production speed with this factor (0.5 means 50 %)
MIN_LICENSE_ACTIVE_DAYS:
  def: '30'
  type: int
  cmt: Min days for license to be active
BASE_LICENSE_IC_COST:
  def: '1'
  type: int
  cmt: Base IC cost for lended license
LICENSE_IC_COST_YEAR_INCREASE:
  def: '1'
  type: int
  cmt: IC cost equipment for every year of equipment after 1936
LICENSE_EQUIPMENT_BASE_SPEED:
  def: '-0.25'
  type: float
  cmt: base MIC speed modifier for licensed equipment
LICENSE_EQUIPMENT_TECH_SPEED_PER_YEAR:
  def: '-0.05'
  type: float
  cmt: MIC speed modifier for licensed equipment for each year of difference between
    actual and latest equipment
LICENSE_EQUIPMENT_TECH_SPEED_MAX_YEARS:
  def: '4'
  type: int
  cmt: Maximum years for MIC speed modifier
LICENSE_EQUIPMENT_SPEED_NOT_FACTION:
  def: '-0.10'
  type: float
  cmt: MIC speed modifier for licensed equipment for not being in faction
LICENSE_EQUIPMENT_UPGRADE_XP_FACTOR:
  def: '2.0'
  type: float
  cmt: XP cost for upgrading licensed equipment
LICENSE_EQUIPMENT_SPEED_NO_LICENSE:
  def: '-0.50'
  type: float
  cmt: Penalty for producing non licensed equipment
CONVERSION_SPEED_BONUS:
  def: '0'
  type: int
  cmt: Modifier to the production speed when converting equipment
EQUIPMENT_MODULE_ADD_XP_COST:
  def: '5.0'
  type: float
  cmt: XP cost for adding a new equipment module in an empty slot when creating an
    equipment variant.
EQUIPMENT_MODULE_REPLACE_XP_COST:
  def: '6.0'
  type: float
  cmt: XP cost for replacing one equipment module with an unrelated module when creating
    an equipment variant.
EQUIPMENT_MODULE_CONVERT_XP_COST:
  def: '3.0'
  type: float
  cmt: XP cost for converting one equipment module to a related module when creating an
    equipment variant.
EQUIPMENT_MODULE_REMOVE_XP_COST:
  def: '1.0'
  type: float
  cmt: XP cost for removing an equipment module and leaving the slot empty when creating
    an equipment variant.
BASE_NAVAL_EQUIPMENT_CONVERSION_IC_COST_FACTOR:
  def: '0.2'
  type: float
  cmt: Fraction of the hull industry cost which is always included in the refitting
    cost.
BASE_LAND_EQUIPMENT_CONVERSION_IC_COST_FACTOR:
  def: '0.9'
  type: float
  cmt: Fraction of the chassis industry cost which is always included in the conversion
    cost.
MIN_NAVAL_EQUIPMENT_CONVERSION_RESOURCE_COST_FACTOR:
  def: '0.2'
  type: float
  cmt: Minimum fraction of a naval equipment's strategic resource cost that any
    conversion will cost.
MIN_LAND_EQUIPMENT_CONVERSION_RESOURCE_COST_FACTOR:
  def: '0'
  type: int
  cmt: Minimum fraction of a land equipment's strategic resource cost that any
    conversion will cost.
SHIP_REFIT_MAX_PROGRESS_TO_CANCEL:
  def: '0.2'
  type: float
  cmt: Maximum refitting progress % that we still allow to cancel wihtout having to
    scuttle the ship.
SHIP_REFIT_DAMAGE_TO_PROGRESS_FACTOR:
  def: '0.5'
  type: float
  cmt: When a ship is being damaged (for example port strike) while refitting, the
    damage is transferred to the production line progress instead. This variable is used
    to balance it.
MINIMUM_NUMBER_OF_FACTORIES_TAKEN_BY_CONSUMER_GOODS_VALUE:
  def: '1'
  type: int
  cmt: The minimum number of factories we have to put on consumer goods, by value.
MINIMUM_NUMBER_OF_FACTORIES_TAKEN_BY_CONSUMER_GOODS_PERCENT:
  def: '0.1'
  type: float
  cmt: The minimum number of factories we have to put on consumer goods, in percent.
INITIAL_ALLOWED_FACTORY_RATIO_FOR_REPAIRS:
  def: '1.0'
  type: float
  cmt: max % of factories allowed on autorepairs
MILITARY_FACTORY_COHERENCY_BONUS:
  def: '250'
  type: int
  cmt: Value we add to the weight of a production line already in progress, if we only
    have one military factory. (to reduce fluctuating AI production)
```
