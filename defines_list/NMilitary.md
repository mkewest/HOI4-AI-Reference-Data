---
domain: defines_list
concept: NMilitary
version: 1.14+
requires: [defines]
relates: [units, combat]
---

```yaml
COMBAT_VALUE_ORG_IMPORTANCE:
  def: '1'
  type: int
  cmt: Multiplier on TotalOrganisation when determining the combat value of a division
SOFT_ATTACK_TARGETING_FACTOR:
  def: '1.0'
  type: float
  cmt: How much we care about potential soft attacks when evaluating priority combat
    target
CASUALTIES_WS_P_PENALTY_DIVISOR:
  def: '200'
  type: int
  cmt: Divisor for casualties WS penalty
PIERCING_THRESHOLDS:
  def: '{ 1.00, 0.75, 0.50, 0.00 }'
  type: array
  cmt: Our piercing / their armor must be this value to deal damage fraction equal
    to the index in the array below [higher number = higher penetration]. If armor
    is 0, 1.00 will be returned. there isn't much point setting this higher than 0
DIVISIONAL_COMMANDER_TRAIT_XP_REQUIREMENT:
  def: '400.0'
  type: float
  cmt: Get a trait if any valid options & xp gained >= this
MAX_LEADERS_TO_SHOW:
  def: '50'
  type: int
  cmt: Max officers to show in field officers list, sorted by field EXP. Divisions
    with awardable entries will potentially supercede this limit
DIVISIONAL_COMMANDER_RANK_XP_THRESHOLD:
  def: '{ 0, 100.0, 200.0, 400.0, 800.0 }'
  type: array
  cmt: this expects a value between 0 and 1 and is added to by female_divisional_commander_chance.
    If you don't have female generic portraits defined, you -will- get silhouettes.XP
    thresholds for divisional commander ranks. [TAG]_DIVISION_EXPERIENCE_TITLE_ARMY_EXPERIENCE_[array
    index]
HOURLY_ORG_MOVEMENT_IMPACT:
  def: '-0.2'
  type: float
  cmt: how much org is lost every hour while moving an army.
INFRA_ORG_IMPACT:
  def: '0.5'
  type: float
  cmt: scale factor of infra on org regain.
INFRASTRUCTURE_MOVEMENT_SPEED_IMPACT:
  def: '-0.05'
  type: float
  cmt: speed penalty per infrastucture below maximum.
VPS_FOR_HIGH_HISTORY_ENTRY:
  def: '8'
  type: int
  cmt: VPs required for high-level history entry
COST_INCREASE_PER_ACTIVE_MEDAL:
  def: '0.25'
  type: float
  cmt: Additional cost factor per active medal
GENERATE_AI_DIV_COMMAND_HISTORY_ENTRIES:
  def: 'true'
  type: bool
  cmt: Should we generate history entries for the AI (may cause savegame bloat)
MAX_FIELD_EXPERIENCE_ON_DIVISION:
  def: '8000'
  type: int
  cmt: Max experience that can be gained on divisional commanders
HISTORY_OPERATION_RANDOM_MAX:
  def: '24'
  type: int
  cmt: max random int to roll when determining whether to grant an awardable entry
    for operations. 1/N chances.
FIELD_OFFICER_PROMOTION_PENALTY:
  def: '0.25'
  type: float
  cmt: Amount of division experience lost when promoting a commander (reduced by modifiers)
WAR_SCORE_LOSSES_RATIO:
  def: '0.5'
  type: float
  cmt: war score gained for every 1000 casualties
WAR_SCORE_STRATEGIC_BOMBING_FACTOR:
  def: '0.02'
  type: float
  cmt: war score gained for every damage made to enemy's building with strategic bombing
WAR_SCORE_AIR_IC_LOSS_FACTOR:
  def: '0.08'
  type: float
  cmt: war score gained for every IC of damage done to an enemy's air mission
WAR_SCORE_ATTACKER_AND_WINNER_FACTOR:
  def: '1.2'
  type: float
  cmt: factor applied to war score gained for strength damage done when being the
    attacker and the winner
WAR_SCORE_PROVINCE_FACTOR:
  def: '4.0'
  type: float
  cmt: war score gained when capturing a province for the first time, multiplied by
    province's worth
WAR_SCORE_LEND_LEASE_GIVEN_FUEL_FACTOR:
  def: '0.003'
  type: float
  cmt: war score gained for every 100 units of fuel lend lease sent to allies
WAR_SCORE_LEND_LEASE_RECEIVED_FUEL_FACTOR:
  def: '0.002'
  type: float
  cmt: war score deducted for every 100 units of fuel lend lease received from allies
DIVISION_SIZE_FOR_XP:
  def: '8'
  type: int
  cmt: how many battalions should a division have to count as a full divisions when
    calculating XP stuff
FIELD_MARSHAL_DIVISIONS_CAP:
  def: '24'
  type: int
  cmt: how many divisions a field marshall is limited to. 0 = inf, < 0 = blocked
UNIT_LEADER_GENERATION_CAPITAL_CONTINENT_FACTOR:
  def: '100'
  type: int
  cmt: Integer factor to multiply manpower.
MAX_DIVISION_BRIGADE_WIDTH:
  def: '5'
  type: int
  cmt: Max width of regiments in division designer.
MIN_DIVISION_BRIGADE_HEIGHT:
  def: '4'
  type: int
  cmt: Min height of regiments in division designer.
MAX_DIVISION_SUPPORT_HEIGHT:
  def: '5'
  type: int
  cmt: Max height of support in division designer.
BASE_DIVISION_BRIGADE_CHANGE_COST:
  def: '5'
  type: int
  cmt: Base cost to change a regiment column.
MAX_ARMY_EXPERIENCE:
  def: '500'
  type: int
  cmt: Max army experience a country can store
MAX_AIR_EXPERIENCE:
  def: '500'
  type: int
  cmt: Max air experience a country can store
SPOTTING_QUALITY_DROP_HOURS:
  def: '4'
  type: int
  cmt: Each X hours the intel quality drops after unit was spotted.
MIN_SUPPLY_CONSUMPTION:
  def: '0.05'
  type: float
  cmt: minimum value of supply consumption that a unit can get
LAND_COMBAT_STR_DICE_SIZE:
  def: '2'
  type: int
  cmt: nr of damage dice
LAND_COMBAT_ORG_DAMAGE_MODIFIER:
  def: '0.053'
  type: float
  cmt: global damage modifier
LAND_AIR_COMBAT_ORG_DAMAGE_MODIFIER:
  def: '0.032'
  type: float
  cmt: global damage modifier
LAND_COMBAT_STR_ARMOR_ON_SOFT_DICE_SIZE:
  def: '2'
  type: int
  cmt: extra damage dice if our armor outclasses enemy
LAND_COMBAT_STR_ARMOR_DEFLECTION_FACTOR:
  def: '0.5'
  type: float
  cmt: damage reduction if armor outclassing enemy
LAND_COMBAT_COLLATERAL_FORT_FACTOR:
  def: '0.005'
  type: float
  cmt: Factor to scale collateral damage to forts with.
LAND_COMBAT_FORT_DAMAGE_CHANCE:
  def: '5'
  type: int
  cmt: chance to get a hit to damage on forts. (out of 100)
ATTRITION_EQUIPMENT_LOSS_CHANCE:
  def: '0.1'
  type: float
  cmt: Chance for loosing equipment when suffer attrition. Scaled up the stronger
    attrition is. Then scaled down by equipment reliability.
ATTRITION_WHILE_MOVING_FACTOR:
  def: '1'
  type: int
RELIABILITY_ORG_MOVING:
  def: '-1.0'
  type: float
  cmt: how much reliability affects org loss on moving
RELIABILTY_RECOVERY:
  def: '0.4'
  type: float
  cmt: factor affecting how much equipment is returned "from the dead"
CHANCE_TO_AVOID_HIT_AT_NO_DEF:
  def: '60'
  type: int
  cmt: chance to avoid hit if no defences left.
TACTIC_SWAP_FREQUENCEY:
  def: '12'
  type: int
  cmt: hours between tactic swaps
COUNTRY_PREFERRED_TACTIC_WEIGHT_FACTOR:
  def: '0.25'
  type: float
  cmt: extra weight multiplier for the country preferred tactic when doing weighted
    random
FIELD_MARSHAL_PREFERRED_TACTIC_WEIGHT_FACTOR:
  def: '0.25'
  type: float
  cmt: extra weight multiplier for the field marhsal preferred tactic when doing weighted
    random
INITIATIVE_PICK_COUNTER_ADVANTAGE_FACTOR:
  def: '0.35'
  type: float
  cmt: advantage per leader level for picking a counter
LAND_SPEED_MODIFIER:
  def: '0.05'
  type: float
  cmt: basic speed control
RIVER_CROSSING_PENALTY_LARGE:
  def: '-0.6'
  type: float
  cmt: large river crossing
RIVER_CROSSING_SPEED_PENALTY_LARGE:
  def: '-0.5'
  type: float
  cmt: large river crossing
RIVER_SMALL_STOP_INDEX:
  def: '6'
  type: int
BASE_FORT_PENALTY:
  def: '-0.15'
  type: float
  cmt: fort penalty
DIG_IN_FACTOR:
  def: '0.02'
  type: float
  cmt: bonus factor for each dug-in level
CONSTANT_XP_RATIO_FOR_MULTIPLE_LEADERS_IN_SAME_COMBAT:
  def: '0.5'
  type: float
  cmt: if there are multiple leaders in same combat, each one gets thisratio + (1-thisratio)/num
    leaders. amount of xp each general gets scales 1 0.75 0.66 etc for 1 2 3 generals
MAX_NUM_TRAITS:
  def: '-1'
  type: int
  cmt: cant have more, -1 to disable
ENEMY_AIR_SUPERIORITY_DEFENSE:
  def: '0.70'
  type: float
  cmt: more AA attack will approach this amount of help (diminishing returns)
ENEMY_AIR_SUPERIORITY_SPEED_IMPACT:
  def: '-0.3'
  type: float
  cmt: effect on speed due to enemy air superiority
ANTI_AIR_ATTACK_TO_AMOUNT:
  def: '0.005'
  type: float
  cmt: Balancing value to convert equipment stat anti_air_attack to the random % value
    of airplanes being hit.
UNIT_EXPERIENCE_PER_COMBAT_HOUR:
  def: '0.0001'
  type: float
UNIT_EXPERIENCE_PER_TRAINING_DAY:
  def: '0.0015'
  type: float
DEPLOY_TRAINING_MAX_LEVEL:
  def: '1'
  type: int
TRAINING_ORG:
  def: '0.2'
  type: float
UNIT_EXP_LEVELS:
  def: '{ 0.1, 0.3, 0.75, 0.9 }'
  type: array
  cmt: Experience needed to progress to the next level
FIELD_EXPERIENCE_MAX_PER_DAY:
  def: '1.2'
  type: float
  cmt: Most xp you can gain per day
LEND_LEASE_FIELD_EXPERIENCE_SCALE:
  def: '0.0005'
  type: float
  cmt: Experience scale for lend leased equipment used in combat.
SLOWEST_SPEED:
  def: '4'
  type: int
REINFORCEMENT_REQUEST_DAYS_FREQUENCY:
  def: '7'
  type: int
  cmt: How many days must pass until we may give another reinforcement request
UNIT_DIGIN_CAP:
  def: '5'
  type: int
  cmt: how "deep" you can dig you can dig in until hitting max bonus
PARACHUTE_FAILED_EQUIPMENT_DIV:
  def: '50.0'
  type: float
  cmt: When the transport plane was shot down, we drop unit with almost NONE equipment
PARACHUTE_FAILED_STR_DIV:
  def: '10.0'
  type: float
  cmt: When the transport plane was shot down, we drop unit with almost NONE strenght
PARACHUTE_DISRUPTED_MANPOWER_DIV:
  def: '1.9'
  type: float
  cmt: When the transport plane was hit, we drop unit with reduced manpower. Penalty
    is higher as more hits was received (and AA guns was in the state).
PARACHUTE_PENALTY_RANDOMNESS:
  def: '0.1'
  type: float
  cmt: Random factor for str,manpower,eq penalties.
PARACHUTE_COMPLETE_ORG:
  def: '0.4'
  type: float
  cmt: Organisation value (in %) after unit being dropped, regardless if failed, disrupted,
    or successful.
PARACHUTE_ORG_REGAIN_PENALTY_MULT:
  def: '-0.8'
  type: float
  cmt: penalty to org regain after being parachuted.
BASE_NIGHT_ATTACK_PENALTY:
  def: '-0.5'
  type: float
EXILE_ORG:
  def: '0.0'
  type: float
  cmt: Amount of org to keep
EQUIPMENT_COMBAT_LOSS_FACTOR:
  def: '0.70'
  type: float
  cmt: '% of equipment lost to strength ratio in combat, so some % is returned if
    below 1'
SUPPLY_USE_FACTOR_INACTIVE:
  def: '0.95'
  type: float
  cmt: Deprecated/Unused
SUPPLY_GRACE_MAX_REDUCE_PER_HOUR:
  def: '2'
  type: int
  cmt: supply grace is not decreased instantly when it is buffed temporarily and buff
    is removed
MAX_OUT_OF_SUPPLY_DAYS:
  def: '30'
  type: int
  cmt: how many days of shitty supply until max penalty achieved
OUT_OF_SUPPLY_SPEED:
  def: '-0.8'
  type: float
  cmt: max speed reduction from supply
NON_CORE_SUPPLY_AIR_SPEED:
  def: '-0.25'
  type: float
  cmt: we are not running on our own VP supply so need to steal stuff along the way,
    a bit less due to air supply
TRAINING_ATTRITION:
  def: '0.05'
  type: float
  cmt: amount of extra attrition from being in training
TRAINING_MAX_DAILY_COUNTRY_EXP:
  def: '0.08'
  type: float
  cmt: Maximum army XP gained per day from training
LOW_SUPPLY:
  def: '0.99'
  type: float
  cmt: When the supply status of an unit becomes low.
BORDER_WAR_VICTORY:
  def: '0.8'
  type: float
  cmt: At wich border war balance of power is victory declared
SPEED_REINFORCEMENT_BONUS:
  def: '0.01'
  type: float
  cmt: chance to join combat bonus by each 100% larger than infantry base (up to 200%)
NAVAL_TRANSFER_DISBAND_MANPOWER_FACTOR:
  def: '0.5'
  type: float
  cmt: percentage of manpower returned when a naval transfering unit is disbanded
ORG_LOSS_FACTOR_ON_CONQUER:
  def: '0.2'
  type: float
  cmt: percentage of (max) org loss on takign enemy province
PLANNING_DECAY:
  def: '0.01'
  type: float
PLANNING_GAIN:
  def: '0.02'
  type: float
NAVAL_INVASION_PLANNING_BONUS_MALUS:
  def: '-1'
  type: int
  cmt: Malus in percentage for the planning bonus gain for naval invasions
CIVILWAR_ORGANIZATION_FACTOR:
  def: '0.3'
  type: float
  cmt: Multiplier of org for both sides when civilwar.
PLAN_CONSIDERED_BAD:
  def: '-0.25'
  type: float
  cmt: Plan evaluations below this value are considered unsafe
PLAN_SPREAD_ATTACK_WEIGHT:
  def: '12.0'
  type: float
  cmt: The higher the value, the less it should crowd provinces with multiple attacks.
PLAN_PROVINCE_BASE_IMPORTANCE:
  def: '2.0'
  type: float
  cmt: Used when calculating the calue of front and defense area provinces for the
    battle plan system
PLAN_PROVINCE_MEDIUM_VP_IMPORTANCE_AREA:
  def: '5.0'
  type: float
  cmt: Used when calculating the value of defense area in the battle plan system
PLAN_PROVINCE_CAPITAL_IMPORTANCE_AREA:
  def: '50.0'
  type: float
  cmt: Used when calculating the balue of defense area in the battle plan system
PLAN_PROVINCE_LOW_VP_IMPORTANCE_FRONT:
  def: '2.0'
  type: float
  cmt: Used when calculating the calue of fronts in the battle plan system
PLAN_PROVINCE_HIGH_VP_IMPORTANCE_FRONT:
  def: '2.75'
  type: float
  cmt: Used when calculating the calue of fronts in the battle plan system
PLAN_PORVINCE_PORT_BASE_IMPORTANCE:
  def: '12.0'
  type: float
  cmt: Added importance for area defense province with a port
PLAN_PORVINCE_AIRFIELD_BASE_IMPORTANCE:
  def: '3.0'
  type: float
  cmt: Added importance for area defense province with air field
PLAN_PORVINCE_AIRFIELD_LEVEL_FACTOR:
  def: '0.25'
  type: float
  cmt: Bonus factor for airfield level
PLAN_PROVINCE_VP_PORT_FACTOR:
  def: '0.25'
  type: float
PLAN_AREA_DEFENSE_ENEMY_UNIT_FACTOR:
  def: '-2.0'
  type: float
  cmt: Factor applied to province score in area defense order per enemy unit in that
    province
PLAN_AREA_DEFENSE_COASTAL_FORT_IMPORTANCE:
  def: '3.0'
  type: float
  cmt: Used when calculating the value of defense area provinces for the battle plan
    system
PLAN_AREA_DEFENSE_HAS_RAIL_IMPORTANCE:
  def: '1.5'
  type: float
  cmt: Used when calculating the value of defense area provinces for the battle plan
    system
PLAN_STICKINESS_FACTOR:
  def: '100.0'
  type: float
  cmt: Factor used in unitcontroller when prioritizing units for locations
PLAN_PROVINCE_PRIO_DISTRIBUTION_MAX:
  def: '1.0'
  type: float
  cmt: Highest fraction of divisions that will be distributed based on province priority
PLAN_PROVINCE_PRIO_DISTRIBUTION_DPP_LOW:
  def: '2.0'
  type: float
  cmt: At what divisions per province should we use PLAN_PROVINCE_PRIO_DISTRIBUTION_MAX
PLAN_EXECUTE_BALANCED_LIMIT:
  def: '0'
  type: int
  cmt: When looking for an attach target, this score limit is required in the battle
    plan to consider province for attack
PLAN_EXECUTE_CAREFUL_MAX_FORT:
  def: '5'
  type: int
  cmt: If execution mode is set to careful, units will not attack provinces with fort
    levels greater than or equal to this
PLAN_MAX_PROGRESS_TO_JOIN:
  def: '0.50'
  type: float
  cmt: If Lower progress than this, probably needs support
PLAN_COHESION_DISTANCE_MAX_WHEN_LEFT_BEHIND:
  def: '38'
  type: int
  cmt: Unused and deprecated - will be removed in next major version.
MIN_BALANCE_SCORE_TO_PROCEED_ATTACK:
  def: '0.2'
  type: float
  cmt: A combat balance score of less than this will prevent auto attacking
FLANKED_PROVINCES_COUNT:
  def: '3'
  type: int
  cmt: Attacker has to attack from that many provinces for the attack to be considered
    as flanking
NUKE_MAX_DAMAGE_PERCENT:
  def: '0.9'
  type: float
  cmt: Minimum damage from nukes as a percentage of current strength/organisation
NUKE_DELAY_HOURS:
  def: '2'
  type: int
  cmt: How many hours does it take for the nuclear drop to happen
PARADROP_HOURS:
  def: '48'
  type: int
  cmt: time paratroopers suffer penalties in combat
COMBAT_SUPPLY_LACK_ATTACKER_DEFEND:
  def: '-0.65'
  type: float
  cmt: defend combat penalty for attacker if out of supply
COMBAT_SUPPLY_LACK_DEFENDER_DEFEND:
  def: '-0.15'
  type: float
  cmt: defend combat penalty for defender if out of supply
COMBAT_STACKING_EXTRA:
  def: '3'
  type: int
  cmt: extra stacking from directions
COMBAT_OVER_WIDTH_PENALTY:
  def: '-1'
  type: int
  cmt: over combat width penalty per %.
RETREAT_SPEED_FACTOR:
  def: '0.25'
  type: float
  cmt: speed bonus when retreating
STRATEGIC_SPEED_INFRA_BASE:
  def: '5.0'
  type: float
  cmt: Base speed of strategic redeployment when not on railways
STRATEGIC_SPEED_RAIL_BASE:
  def: '15.0'
  type: float
  cmt: Base speed of strategic redeployment when on railways
STRATEGIC_REDEPLOY_ORG_RATIO:
  def: '0.1'
  type: float
  cmt: Ratio of max org while strategic redeployment
BATALION_CHANGED_EXPERIENCE_DROP:
  def: '0.5'
  type: float
  cmt: Division experience drop if unit has different batalion
PEN_VS_AVERAGE:
  def: '0.4'
  type: float
LAND_EQUIPMENT_RAMP_COST:
  def: '5'
  type: int
NAVAL_EQUIPMENT_RAMP_COST:
  def: '5'
  type: int
AIR_EQUIPMENT_RAMP_COST:
  def: '5'
  type: int
FASTER_ORG_REGAIN_MULT:
  def: '1.0'
  type: float
SLOWER_ORG_REGAIN_MULT:
  def: '-0.5'
  type: float
MIN_DIVISION_DEPLOYMENT_TRAINING:
  def: '0.2'
  type: float
  cmt: Min level of division training
FRONT_MIN_PATH_TO_REDEPLOY:
  def: '8'
  type: int
  cmt: If a units path is at least this long to reach its front location, it will
    strategically redeploy.
BASE_CAPTURE_EQUIPMENT_RATIO:
  def: '0.0'
  type: float
  cmt: after a successful land combat, ratio of the equipments that are being captured/salvaged
    from enemy's lost equipment
ACCLIMATIZATION_SPEED_GAIN:
  def: '0.15'
  type: float
  cmt: A variable used to balance the overall speed of gaining the acclimatization
PROMOTE_LEADER_CP_COST:
  def: '40.0'
  type: float
  cmt: cost of promoting a leader
FIELD_MARSHAL_XP_RATIO:
  def: '0.3'
  type: float
  cmt: xp gain ratio for army group leaders
COMMANDER_LEVEL_UP_STAT_COUNT:
  def: '3'
  type: int
  cmt: num stats gained on level up
NAVY_LEADER_LEVEL_UP_STAT_WEIGHTS:
  def: '{ 5, 5, 5, 5 }'
  type: array
  cmt: level up stat random base weights attack, defense, maneuvering, coordination
UNIT_LEADER_TRAIT_SLOT_PER_LEVEL:
  def: '{ 0.5, 0.5, 0.5, 0.0 }'
  type: array
  cmt: num extra traits on each level field marshal corps commander navy general operative
HOURS_REQ_REJOIN_BORDER_WAR_FOR_INJURED_UNITS:
  def: '1'
  type: int
  cmt: minimum hours required for units to rejoin border wars, values below zero will
    make units never return
NEW_COMMANDER_RANDOM_BASIC_TRAIT_CHANCES:
  def: '{  }'
  type: array
  cmt: chances to gain a basic trait for new generals
NEW_OPERATIVE_RANDOM_PERSONALITY_TRAIT_CHANCES:
  def: '{ 0.5, 0.1 }'
  type: array
  cmt: chances to gain a personality trait for new operatives 50% for first trait
    10% for second trait after that
NEW_OPERATIVE_RANDOM_STATUS_TRAIT_CHANCES:
  def: '{  }'
  type: array
  cmt: chances to gain a status trait for new operatives
NEW_NAVY_LEADER_RANDOM_SKILL_CHANCES:
  def: '{  }'
  type: array
  cmt: chances to give a random stat skill point for a new admiral
UNIT_LEADER_ASSIGN_TRAIT_COST:
  def: '15.0'
  type: float
  cmt: cost to assign a new trait to a unit leader
BORDER_WAR_WIN_DAYS_AGAINST_EMPTY_OPPONENTS:
  def: '14'
  type: int
  cmt: border wars will be automatically won if no opponent shows up for this duration
XP_GAIN_FACTOR_FOR_MAX_RELATIVE_COMBAT_DAMAGE:
  def: '4.0'
  type: float
  cmt: XP factor scaling for max relative combat damage
MIN_XP_RATE_TO_DECAY:
  def: '0.1'
  type: float
  cmt: minimum XP factor for dragged combats
XP_GAIN_FOR_SHATTERING:
  def: '35.0'
  type: float
  cmt: fixed XP gain per shattered unit
FUEL_PENALTY_START_RATIO:
  def: '0.25'
  type: float
  cmt: ratio of fuel in an army to start getting penalties
ARMY_MAX_FUEL_FLOW_MULT:
  def: '2.0'
  type: float
  cmt: max fuel ratio that an army can get per hour, multiplied by supply situation
ARMY_COMBAT_FUEL_MULT:
  def: '1.0'
  type: float
  cmt: fuel consumption ratio in combat (plus ARMY_MOVEMENT_FUEL_MULT if you are also
    moving. ie offensive combat)
ARMY_MOVEMENT_FUEL_MULT:
  def: '1.0'
  type: float
  cmt: fuel consumption ratio while moving
ARMY_STRATEGIC_DEPLOYMENT_FUEL_MULT:
  def: '0.0'
  type: float
  cmt: fuel consumption ratio while doing strategic deployment
FUEL_EFFICIENCY_RAID_MULTIPLIER:
  def: '1.0'
  type: float
  cmt: convoy raid multiplier for fuel sunk
OUT_OF_FUEL_EQUIPMENT_MULT:
  def: '0.1'
  type: float
  cmt: ratio of the stats that you get from equipments that uses fuel and you lack
    it
OUT_OF_FUEL_TRAINING_XP_GAIN_MULT:
  def: '0.0'
  type: float
  cmt: xp gain mult from training when a unit is out of fuel
MAX_ESTIMATED_PLAN_UNITS_NOT_IN_PLACE_FACTOR:
  def: '-0.6'
  type: float
  cmt: Scaled by % of units not in place. Used to be a flat -50%
NEW_ARMY_LEADER_LEVEL_CHANCES:
  def: '{ 0.95, 0.05 }'
  type: array
  cmt: chances for new army leaders to start at a given level 95% for level one 5%
    for level two 0% for level three to ten
```
