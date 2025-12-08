---
domain: defines_list
concept: NSupply
version: 1.17.2
requires: [defines]
relates: [supply, logistics]
---

```yaml
MAX_RAILWAY_LEVEL:
  def: '5'
  type: int
  cmt: update railway texture as well, each frame corresponds to a level
CAPITAL_SUPPLY_BASE:
  def: '5.0'
  type: float
  cmt: base supply for capital
CAPITAL_SUPPLY_CIVILIAN_FACTORIES:
  def: '0.3'
  type: float
  cmt: supply from one civilian factory
CAPITAL_SUPPLY_MILITARY_FACTORIES:
  def: '0.6'
  type: float
  cmt: supply from one military factory
CAPITAL_SUPPLY_DOCKYARDS:
  def: '0.4'
  type: float
  cmt: supply from one naval factory
CAPITAL_INITIAL_SUPPLY_FLOW:
  def: '5.0'
  type: float
  cmt: starting supply from
CAPITAL_STARTING_PENALTY_PER_PROVINCE:
  def: '0.5'
  type: float
  cmt: starting penalty that will be added as supply moves away from its origin
    (modified by stuff like terrain)
CAPITAL_ADDED_PENALTY_PER_PROVINCE:
  def: '1.2'
  type: float
  cmt: added penalty as we move away from origin
NODE_INITIAL_SUPPLY_FLOW:
  def: '2.8'
  type: float
NODE_STARTING_PENALTY_PER_PROVINCE:
  def: '0.50'
  type: float
NODE_ADDED_PENALTY_PER_PROVINCE:
  def: '0.70'
  type: float
NAVAL_BASE_INITIAL_SUPPLY_FLOW:
  def: '3.3'
  type: float
NAVAL_BASE_STARTING_PENALTY_PER_PROVINCE:
  def: '0.84'
  type: float
NAVAL_BASE_ADDED_PENALTY_PER_PROVINCE:
  def: '1.1'
  type: float
NAVAL_SUPPLY_HUB_REDUCTION_FACTOR:
  def: '0.0'
  type: float
  cmt: naval supply hub will reduce the supply need to the fleet by this ratio
NODE_FLOW_BONUS_PER_RAIL_LEVEL:
  def: '0.34'
  type: float
RIVER_RAILWAY_LEVEL:
  def: '1'
  type: int
FLOATING_HARBOR_INITIAL_SUPPLY_FLOW:
  def: '2.6'
  type: float
FLOATING_HARBOR_STARTING_PENALTY_PER_PROVINCE:
  def: '0.8'
  type: float
FLOATING_HARBOR_ADDED_PENALTY_PER_PROVINCE:
  def: '0.8'
  type: float
FLOATING_HARBOR_BASE_SUPPLY:
  def: '15.0'
  type: float
  cmt: supply given by a floating harbor
FLOATING_HARBOR_BASE_DURATION:
  def: '21'
  type: int
  cmt: duration of a full hp floating harbor
FLOATING_HARBOR_DURATION_RATIO_AT_MIN_HP:
  def: '0.0'
  type: float
  cmt: duration mult for a harbor that was reduced to 0 hp
FLOATING_HARBOR_MIN_DECAY:
  def: '0.2'
  type: float
  cmt: Always reduce Floating Harbor longevity by this many "hours" per hour
FLOATING_HARBOR_DECAY_MAX_AIR_BONUS:
  def: '-0.1'
  type: float
  cmt: At 100% Friendly Air superiourity, change decay rate by this many "hours" per
    hour
FLOATING_HARBOR_DECAY_MAX_AIR_PENALTY:
  def: '0.4'
  type: float
  cmt: At 100% Enemy Air superiourity, change decay rate by this many "hours" per hour
FLOATING_HARBOR_DECAY_MAX_NAVAL_BONUS:
  def: '-0.2'
  type: float
  cmt: At 100% Friendly naval superiourity, change decay rate by this many "hours" per
    hour
FLOATING_HARBOR_DECAY_MAX_NAVAL_PENALTY:
  def: '0.5'
  type: float
  cmt: At 100% Enemy Naval superiourity, change decay rate by this many "hours" per hour
FLOATING_HARBOR_DECAY_NO_CONTROL_PENALTY:
  def: '1.0'
  type: float
  cmt: If adjacent land province is not held, change decay rate by this many "hours" per
    hour
SUPPLY_FLOW_DROP_REDUCTION_AT_MAX_INFRA:
  def: '0.30'
  type: float
  cmt: max infrastructure level will reduce the supply flow drop off by this ratio
SUPPLY_FLOW_PENALTY_CROSSING_RIVERS:
  def: '0.20'
  type: float
  cmt: crossing rivers introduces additional penalty
SUPPLY_FLOW_DIST_LOGISTICS_FALLOFF_K:
  def: '1.3'
  type: float
  cmt: How steep the curve is
SUPPLY_FLOW_DIST_LOGISTICS_FALLOFF_MIDPOINT:
  def: '2.3'
  type: float
  cmt: sigmoid inflection point
SUPPLY_FLOW_DIST_LOGISTICS_FALLOFF_SCALAR:
  def: '0.9'
  type: float
  cmt: Max Penalty adjustment due to distance
SUPPLY_FLOW_DIST_LOGISTICS_FALLOFF_MIN_PENALTY_SCALE:
  def: '0.25'
  type: float
  cmt: Logistics curve never reduces penalty facor below this limit
SUPPLY_HUB_FULL_MOTORIZATION_BONUS:
  def: '2.2'
  type: float
SUPPLY_HUB_FULL_MOTORIZATION_TRUCK_COST:
  def: '60.0'
  type: float
SUPPLY_HUB_MOTORIZATION_MARGINAL_EFFECT_DECAY:
  def: '1.6'
  type: float
RAILWAY_BASE_FLOW:
  def: '10.0'
  type: float
  cmt: how much base flow railway gives when a node connected to its capital/a naval
    node by a railway
RAILWAY_FLOW_PER_LEVEL:
  def: '5.0'
  type: float
  cmt: how much additional flow a railway level gives
RAILWAY_FLOW_PENALTY_PER_DAMAGED:
  def: '5.0'
  type: float
  cmt: penalty to flow per damaged railway
RAILWAY_MIN_FLOW:
  def: '5.0'
  type: float
  cmt: minimum railway flow can be reduced to
NAVAL_BASE_FLOW:
  def: '5.0'
  type: float
  cmt: max output/input of a naval node is limited by this base value + additional ratio
    for each level
NAVAL_FLOW_PER_LEVEL:
  def: '3.0'
  type: float
  cmt: max output/input of a naval node is limited by previous base value + this define
    per its level
SUPPLY_NODE_MIN_SUPPLY_THRESHOLD:
  def: '1.0'
  type: float
  cmt: if supply of a node is below this value it will be set to 0 -- Currently unused?
    This should happen when enough damage occurs
INFRA_TO_SUPPLY:
  def: '0.3'
  type: float
  cmt: each level of infra gives this many supply
VP_TO_SUPPLY_BASE:
  def: '0.2'
  type: float
  cmt: Bonus to supply from a VP, no matter the level
VP_TO_SUPPLY_BONUS_CONVERSION:
  def: '0.05'
  type: float
  cmt: Bonus to supply local supplies from Victory Points, multiplied by this aspect and
    rounded to closest integer
SUPPLY_FROM_DAMAGED_INFRA:
  def: '0.15'
  type: float
  cmt: damaged infrastructure counts as this in supply calcs
SUPPLY_BASE_MULT:
  def: '0.2'
  type: float
  cmt: multiplier on supply base values
SUPPLY_DISRUPTION_DAILY_RECOVERY:
  def: '1.5'
  type: float
  cmt: every day nodes recover this much of their accumulated disruption.
RAILWAY_CONVERSION_COOLDOWN:
  def: '10'
  type: int
  cmt: railways will be put on cooldown when they are captured by enemy and will not be
    usable during the cooldown
RAILWAY_CONVERSION_COOLDOWN_CORE:
  def: '5'
  type: int
RAILWAY_CONVERSION_COOLDOWN_CIVILWAR:
  def: '0'
  type: int
DEFAULT_STARTING_TRUCK_RATIO:
  def: '1.5'
  type: float
  cmt: countries get this ratio of starting truck in their buffers compared to their
    need
DEFAULT_STARTING_TRAIN_RATIO:
  def: '1'
  type: int
  cmt: countries get this ratio of starting trains in their buffers compared to their
    need
SUPPLY_POINTS_PER_TRAIN:
  def: '1.0'
  type: float
  cmt: old default 1.25 -- Amount of supply that can fit in a train. (Trains distribute
    supply from capital to a supply node.)
NUM_RAILWAYS_TRAIN_FACTOR:
  def: '0.03'
  type: float
  cmt: the train usage is scaled by railway distance between the supply node and the
    capital multiplied by this factor
BASE_SUPPLY_MULT_FOR_TRUCK_DEFAULT_BUFFER:
  def: '1.0'
  type: float
  cmt: initial value for wanted buffers over potential truck usage
BASE_SUPPLY_MULT_FOR_TRUCK_MIN_BUFFER:
  def: '0.0'
  type: float
  cmt: min and max values for buffer ratio
BASE_SUPPLY_MULT_FOR_TRUCK_MAX_BUFFER:
  def: '100.0'
  type: float
TRUCK_ATTRITION:
  def: '0.003'
  type: float
  cmt: base truck attrition
TRUCK_ATTRITION_FACTOR:
  def: '0.65'
  type: float
  cmt: a scale on total truck attrition
BASE_TRUCK_HP:
  def: '100.0'
  type: float
TRUCK_HP_PER_ARMOR:
  def: '2'
  type: int
BASE_TRAIN_HP:
  def: '100.0'
  type: float
TRAIN_ARMOR_TARGETING_WEIGHT:
  def: '0.01'
  type: float
  cmt: For each health point gained by armor_value, enemy bombers are this much more
    likely to target
TRAIN_ANTI_AIR_HIT_CHANCE:
  def: '0.07'
  type: float
  cmt: Balancing value to determine the chance of train anti-air hitting an attacking
    airwing.
TRAIN_ANTI_AIR_HIT_ROLL_COUNT:
  def: '12'
  type: int
  cmt: The air_attack of all attacked trains are accumulated, and then we do this many
    random rolls each with the hit chance set above to determine the fraction of the
    accumulated air_attack that hits.
TRAIN_ANTI_AIR_ATTACK_TO_AMOUNT:
  def: '0.001'
  type: float
  cmt: Balancing value to convert the hitting air_attack to a percentage value of the
    attacking planes that are killed.
MIN_TRAIN_SUPPLY_FACTOR:
  def: '0.5'
  type: float
  cmt: Having 0 trains in stockpile only applies this penalty factor, scaling up to 1.0
    when need is met
MIN_TRAIN_REQUIREMENT:
  def: '2'
  type: int
  cmt: If total train need <= this, then don't apply any supply penalty, even if
    stockpile is insufficient
SUPPLY_FLOW_REDUCTION_THRESHOLD:
  def: '0.1'
  type: float
  cmt: if supply flow is lower than this, it is not applied
BASE_AIR_SUPPLY_MULT_FOR_TRUCK_BUFFER:
  def: '1.0'
  type: float
BASE_ARMY_SUPPLY_MULT_FOR_TRUCK_BUFFER:
  def: '1.0'
  type: float
BASE_NAVY_SUPPLY_MULT_FOR_TRUCK_BUFFER:
  def: '1.0'
  type: float
CAPITAL_NODE_BASE_SUPPLY_ADD:
  def: '0'
  type: int
BUILT_NODE_BASE_SUPPLY_ADD:
  def: '0.6'
  type: float
LOCAL_NODE_BASE_SUPPLY_ADD:
  def: '0.5'
  type: float
NAVAL_NODE_BASE_SUPPLY_ADD:
  def: '0.3'
  type: float
ARMY_SUPPLY_RATIO_STARTING_GAIN:
  def: '0.0'
  type: float
ARMY_SUPPLY_RATIO_SPEED_GAIN_PER_HOUR:
  def: '0.01'
  type: float
ARMY_MAX_SUPPLY_RATIO_GAIN_PER_HOUR:
  def: '0.15'
  type: float
MIN_SURRENDER_LIMIT_TO_MOVE_SUPPLY_CAPITAL:
  def: '0.15'
  type: float
  cmt: country needs to be above thos surrender ratio to be able to move its capital
COOLDOWN_DAYS_AFTER_MOVING_SUPPLY_CAPITAL:
  def: '30'
  type: int
  cmt: cooldown for moving supply again after last move
DAYS_TO_START_GIVING_SUPPLY_AFTER_MOVING_SUPPLY_CAPITAL:
  def: '7'
  type: int
  cmt: the country will start gaining supply after this many days moving its capital
DAYS_TO_START_GIVING_FULL_SUPPLY_AFTER_MOVING_SUPPLY_CAPITAL:
  def: '21'
  type: int
  cmt: the country will reach max supply after this many days moving its capital
MIN_DIFF_FOR_AUTO_UPDATING_EXISTING_RAILWAYS:
  def: '5'
  type: int
  cmt: while building railways, the system will prefer updating existing railway if new
    railway is close enough to existing one
SUPPLY_PATH_MAX_DISTANCE:
  def: '15'
  type: int
  cmt: max time it can take
RAILWAY_DISTANCE_FACTOR_FOR_REINFORCEMENT_SPEED:
  def: '0.3'
  type: float
  cmt: time factor for total railway distance
TRUCK_DISTANCE_FACTOR_FOR_REINFORCEMENT_SPEED:
  def: '0.01'
  type: float
  cmt: time factor for total truck distance
NAVAL_DISTANCE_FACTOR_FOR_REINFORCEMENT_SPEED:
  def: '0.08'
  type: float
  cmt: time factor for total naval distance
ALERT_VERY_LOW_SUPPLY_LEVEL:
  def: '0.2'
  type: float
  cmt: At which point we show up the low and very low supply level alert. Value is in %
    of supplies supported vs required.
ALERT_LOW_SUPPLY_LEVEL:
  def: '0.5'
  type: float
AI_FRONT_MINIMUM_UNITS_PER_PROVINCE_FOR_SUPPLY_CALCULATIONS:
  def: '1'
  type: int
  cmt: AI will try to keep this amount of divisions per province as a minimum when
    evaluating supply limitations for war fronts
AI_FRONT_DIVISIONS_PER_SUPPLY_POINT:
  def: '1.0'
  type: float
  cmt: How many divisions should the AI consider it can supply per available supply
    point
AI_FRONT_MAX_UNITS_ENEMY_COUNT_FACTOR:
  def: '1.2'
  type: float
  cmt: Make sure AI front MaxNrUnits is at least EnemyCount multiplied by this factor
SUPPLY_THRESHOLD_FOR_ARMY_ATTRITION:
  def: '0.35'
  type: float
  cmt: armies will only get attrition below this supply
NUMBER_OF_SHOWN_SUPPLY_SOURCES_IN_SUPPLY_MAPMODE:
  def: '3'
  type: int
  cmt: number of supply flow sources shown in breakdown tooltip
ESTIMATED_DIVISION_WEIGHT_FOR_SUPPLY_ESTIMATIONS_GUI:
  def: '1.0'
  type: float
  cmt: Division supply consumption used for estimating frontline weight for order
    tooltips
AVAILABLE_MANPOWER_STATE_SUPPLY:
  def: '0.18'
  type: float
  cmt: Factor for state supply from max manpower (population)
NON_CORE_MANPOWER_STATE_SUPPLY:
  def: '0.2'
  type: float
  cmt: Factor for population sttate supply when controlled by an occupier (NO TAKE FOOD)
STORED_SUPPLY_CONSUMPTION_RATE_FACTOR:
  def: '0.75'
  type: float
  cmt: Multiplies consumption rate of stored supply (more/less easement)
```
