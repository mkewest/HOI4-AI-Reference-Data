---
domain: defines_list
concept: NSupply
version: 1.14+
requires: [defines]
relates: [supply, logistics]
---

```yaml
MAX_RAILWAY_LEVEL:
  def: '5'
  type: int
  cmt: update railway texture as well, each frame corresponds to a level
CAPITAL_SUPPLY_CIVILIAN_FACTORIES:
  def: '0.3'
  type: float
  cmt: supply from one civilian factory
CAPITAL_SUPPLY_DOCKYARDS:
  def: '0.4'
  type: float
  cmt: supply from one naval factory
CAPITAL_STARTING_PENALTY_PER_PROVINCE:
  def: '0.5'
  type: float
  cmt: starting penalty that will be added as supply moves away from its origin (modified
    by stuff like terrain)
NODE_INITIAL_SUPPLY_FLOW:
  def: '2.8'
  type: float
  cmt: defines that are used for supply reach for built nodes
NODE_ADDED_PENALTY_PER_PROVINCE:
  def: '0.70'
  type: float
NAVAL_BASE_STARTING_PENALTY_PER_PROVINCE:
  def: '0.84'
  type: float
NODE_FLOW_BONUS_PER_RAIL_LEVEL:
  def: '0.34'
  type: float
  cmt: Node Flow (i.e. province caps) increase by this amount per railway level of
    the node's bottleneck
FLOATING_HARBOR_INITIAL_SUPPLY_FLOW:
  def: '2.6'
  type: float
  cmt: defines that are used for supply reach for floating harbors
FLOATING_HARBOR_ADDED_PENALTY_PER_PROVINCE:
  def: '0.8'
  type: float
FLOATING_HARBOR_BASE_DURATION:
  def: '21'
  type: int
  cmt: duration of a full hp floating harbor
FLOATING_HARBOR_MIN_DECAY:
  def: '0.2'
  type: float
  cmt: Always reduce Floating Harbor longevity by this many "hours" per hour
FLOATING_HARBOR_DECAY_MAX_AIR_PENALTY:
  def: '0.4'
  type: float
  cmt: At 100% Enemy Air superiourity, change decay rate by this many "hours" per
    hour
FLOATING_HARBOR_DECAY_MAX_NAVAL_PENALTY:
  def: '0.5'
  type: float
  cmt: At 100% Enemy Naval superiourity, change decay rate by this many "hours" per
    hour
SUPPLY_FLOW_DROP_REDUCTION_AT_MAX_INFRA:
  def: '0.30'
  type: float
  cmt: max infrastructure level will reduce the supply flow drop off by this ratio
SUPPLY_FLOW_DIST_LOGISTICS_FALLOFF_K:
  def: '1.3'
  type: float
  cmt: node flow terrain falloff is scaled by logistics curve based on distance(d)
    (scalar / (1+e^(-k(d-midpoint)))) How steep the curve is
SUPPLY_FLOW_DIST_LOGISTICS_FALLOFF_SCALAR:
  def: '0.9'
  type: float
  cmt: Max Penalty adjustment due to distance
SUPPLY_HUB_FULL_MOTORIZATION_BONUS:
  def: '2.2'
  type: float
  cmt: The range bonus added to a fully motorized hub. This supply is added on top
    of the XXX_INITIAL_SUPPLY_FLOW defined above.
SUPPLY_HUB_MOTORIZATION_MARGINAL_EFFECT_DECAY:
  def: '1.6'
  type: float
  cmt: For each additional level of motorization on a hub (i.e. contry with set motoriazation)
    reduce max bonus for next level by this amount
RAILWAY_FLOW_PER_LEVEL:
  def: '5.0'
  type: float
  cmt: how much additional flow a railway level gives
RAILWAY_MIN_FLOW:
  def: '5.0'
  type: float
  cmt: minimum railway flow can be reduced to
NAVAL_FLOW_PER_LEVEL:
  def: '3.0'
  type: float
  cmt: max output/input of a naval node is limited by previous base value + this define
    per its level
INFRA_TO_SUPPLY:
  def: '0.3'
  type: float
  cmt: each level of infra gives this many supply
VP_TO_SUPPLY_BONUS_CONVERSION:
  def: '0.05'
  type: float
  cmt: Bonus to supply local supplies from Victory Points, multiplied by this aspect
    and rounded to closest integer
SUPPLY_BASE_MULT:
  def: '0.2'
  type: float
  cmt: multiplier on supply base values
RAILWAY_CONVERSION_COOLDOWN:
  def: '10'
  type: int
  cmt: railways will be put on cooldown when they are captured by enemy and will not
    be usable during the cooldown
RAILWAY_CONVERSION_COOLDOWN_CIVILWAR:
  def: '0'
  type: int
DEFAULT_STARTING_TRAIN_RATIO:
  def: '1'
  type: int
  cmt: countries get this ratio of starting trains in their buffers compared to their
    need
NUM_RAILWAYS_TRAIN_FACTOR:
  def: '0.03'
  type: float
  cmt: the train usage is scaled by railway distance between the supply node and the
    capital multiplied by this factor
BASE_SUPPLY_MULT_FOR_TRUCK_MIN_BUFFER:
  def: '0.0'
  type: float
  cmt: min and max values for buffer ratio
TRUCK_ATTRITION:
  def: '0.003'
  type: float
  cmt: base truck attrition
BASE_TRUCK_HP:
  def: '100.0'
  type: float
BASE_TRAIN_HP:
  def: '100.0'
  type: float
TRAIN_ANTI_AIR_HIT_CHANCE:
  def: '0.07'
  type: float
  cmt: Balancing value to determine the chance of train anti-air hitting an attacking
    airwing.
TRAIN_ANTI_AIR_ATTACK_TO_AMOUNT:
  def: '0.001'
  type: float
  cmt: Balancing value to convert the hitting air_attack to a percentage value of
    the attacking planes that are killed.
MIN_TRAIN_REQUIREMENT:
  def: '2'
  type: int
  cmt: If total train need <= this, then don't apply any supply penalty, even if stockpile
    is insufficient
BASE_AIR_SUPPLY_MULT_FOR_TRUCK_BUFFER:
  def: '1.0'
  type: float
  cmt: following values are used for calculating potential truck usage generally potential
    is ~= current usage but as units moves along the map they are assigned to different
    nodes which adds slightly higher usage due to minimum truck needed being 1
BASE_NAVY_SUPPLY_MULT_FOR_TRUCK_BUFFER:
  def: '1.0'
  type: float
BUILT_NODE_BASE_SUPPLY_ADD:
  def: '0.6'
  type: float
NAVAL_NODE_BASE_SUPPLY_ADD:
  def: '0.3'
  type: float
ARMY_SUPPLY_RATIO_SPEED_GAIN_PER_HOUR:
  def: '0.01'
  type: float
MIN_SURRENDER_LIMIT_TO_MOVE_SUPPLY_CAPITAL:
  def: '0.15'
  type: float
  cmt: country needs to be above thos surrender ratio to be able to move its capital
DAYS_TO_START_GIVING_SUPPLY_AFTER_MOVING_SUPPLY_CAPITAL:
  def: '7'
  type: int
  cmt: the country will start gaining supply after this many days moving its capital
MIN_DIFF_FOR_AUTO_UPDATING_EXISTING_RAILWAYS:
  def: '5'
  type: int
  cmt: while building railways, the system will prefer updating existing railway if
    new railway is close enough to existing one
RAILWAY_DISTANCE_FACTOR_FOR_REINFORCEMENT_SPEED:
  def: '0.3'
  type: float
  cmt: time factor for total railway distance
NAVAL_DISTANCE_FACTOR_FOR_REINFORCEMENT_SPEED:
  def: '0.08'
  type: float
  cmt: time factor for total naval distance
ALERT_LOW_SUPPLY_LEVEL:
  def: '0.5'
  type: float
AI_FRONT_DIVISIONS_PER_SUPPLY_POINT:
  def: '1.0'
  type: float
  cmt: How many divisions should the AI consider it can supply per available supply
    point
SUPPLY_THRESHOLD_FOR_ARMY_ATTRITION:
  def: '0.35'
  type: float
  cmt: armies will only get attrition below this supply
ESTIMATED_DIVISION_WEIGHT_FOR_SUPPLY_ESTIMATIONS_GUI:
  def: '1.0'
  type: float
  cmt: Division supply consumption used for estimating frontline weight for order
    tooltips
NON_CORE_MANPOWER_STATE_SUPPLY:
  def: '0.2'
  type: float
  cmt: Factor for population sttate supply when controlled by an occupier (NO TAKE
    FOOD)
```
