---
domain: defines_list
concept: NMilitary
version: 1.17.2
requires: [defines]
relates: [units, combat]
---

```yaml
COMBAT_VALUE_ORG_IMPORTANCE:
  def: '1'
  type: int
  cmt: Multiplier on TotalOrganisation when determining the combat value of a division
COMBAT_VALUE_STR_IMPORTANCE:
  def: '1'
  type: int
  cmt: Multiplier on TotalStrength when determining the combat value of a division
SOFT_ATTACK_TARGETING_FACTOR:
  def: '1.0'
  type: float
  cmt: How much we care about potential soft attacks when evaluating priority combat
    target
HARD_ATTACK_TARGETING_FACTOR:
  def: '1.2'
  type: float
  cmt: How much we care about potential hard attacks when evaluating priority combat
    target
CASUALTIES_WS_P_PENALTY_DIVISOR:
  def: '200'
  type: int
  cmt: Divisor for casualties WS penalty
CASUALTIES_WS_A_PENALTY_DIVISOR:
  def: '600'
  type: int
  cmt: Divisor for casualties WS penalty
PIERCING_THRESHOLDS:
  def:
    - [1.00]
    - [0.75]
    - [0.50]
    - [0.00]  # there isn't much point setting this higher than 0
  type: table
  cmt: Our piercing / their armor must be this value to deal damage fraction equal to
    the index in the array below [higher number = higher penetration]. If armor is 0,
    1.00 will be returned.
PIERCING_THRESHOLD_DAMAGE_VALUES:
  def:
    - [1.00]
    - [0.80]
    - [0.65]
    - [0.50]
  type: table
  cmt: 0 armor will always receive maximum damage (so add overmatching at your own
    peril). the system expects at least 2 values, with no upper limit.
DIVISIONAL_COMMANDER_TRAIT_XP_REQUIREMENT:
  def: '400.0'
  type: float
  cmt: Get a trait if any valid options & xp gained >= this
NUM_DAYS_FOR_OPERATION_ENTRY:
  def: '60'
  type: int
  cmt: Number of days that a unit must have been on a particular active order instance
    to receive a history entry.
MAX_LEADERS_TO_SHOW:
  def: '50'
  type: int
  cmt: Max officers to show in field officers list, sorted by field EXP. Divisions with
    awardable entries will potentially supercede this limit
BASE_FEMALE_DIVISIONAL_COMMANDER_CHANCE:
  def: '0'
  type: int
  cmt: Chance to receive a female divisonal commander. This is set to zero in the base
    game, as we do not have generic female portraits for many graphical culture groups.
DIVISIONAL_COMMANDER_RANK_XP_THRESHOLD:
  def:
    - [0]
    - [100.0]
    - [200.0]
    - [400.0]
    - [800.0]
  type: table
  cmt: XP thresholds for divisional commander ranks.
    [TAG]_DIVISION_EXPERIENCE_TITLE_ARMY_EXPERIENCE_[array index]
USE_MULTIPLICATIVE_ORG_LOSS_WHEN_MOVING:
  def: 'true'
  type: bool
  cmt: whether to apply org_loss_when_moving modifiers additively or multiplicatively
    (hardcoded multiplicative pre-2021)
HOURLY_ORG_MOVEMENT_IMPACT:
  def: '-0.2'
  type: float
  cmt: how much org is lost every hour while moving an army.
ZERO_ORG_MOVEMENT_MODIFIER:
  def: '-0.8'
  type: float
  cmt: speed impact at 0 org.
INFRA_ORG_IMPACT:
  def: '0.5'
  type: float
  cmt: scale factor of infra on org regain.
ENGAGEMENT_WIDTH_PER_WIDTH:
  def: '2.0'
  type: float
  cmt: how much enemy combat width we are allowed to engage per width of our own
INFRASTRUCTURE_MOVEMENT_SPEED_IMPACT:
  def: '-0.05'
  type: float
  cmt: speed penalty per infrastucture below maximum.
VPS_FOR_HISTORY_ENTRY:
  def: '3'
  type: int
  cmt: Minimum VPs required to receive an entry in divisional history
VPS_FOR_HIGH_HISTORY_ENTRY:
  def: '8'
  type: int
  cmt: VPs required for high-level history entry
ENTRIES_TO_CHECK_FOR_DUPLICATE:
  def: '2'
  type: int
  cmt: Max number of history entries to check back to see if we're being awarded the
    same entry
COST_INCREASE_PER_ACTIVE_MEDAL:
  def: '0.25'
  type: float
  cmt: Additional cost factor per active medal
MAX_ENTRY_ELISION_COUNT:
  def: '4'
  type: int
  cmt: If we do the same type of thing consecutively, each entry will stack locations up
    to this number
GENERATE_AI_DIV_COMMAND_HISTORY_ENTRIES:
  def: 'true'
  type: bool
  cmt: Should we generate history entries for the AI (may cause savegame bloat)
GENERATE_AI_DIV_COMMAND_MEDALS:
  def: '0.10'
  type: float
  cmt: Chance for AI to award a medal when receiving a history entry that allows it.
    Also gives a chance for AI to gain history entries irrespective of the setting above
MAX_NUM_AUTOMEDALS:
  def: '6'
  type: int
  cmt: You can't get more medals from the automedal system than this.
FIELD_EXPERIENCE_ON_DIVISION_MULT:
  def: '0.04'
  type: float
  cmt: Multiply field experience gained by this, when applying to divisional commander
MAX_FIELD_EXPERIENCE_ON_DIVISION:
  def: '8000'
  type: int
  cmt: Max experience that can be gained on divisional commanders
FIELD_EXPERIENCE_ON_DIVISION_PER_MEDAL_MULT:
  def: '0.1'
  type: float
  cmt: Multiply officer field experience gain by this * number of division medals on
    application
HISTORY_OPERATION_RANDOM_MAX:
  def: '24'
  type: int
  cmt: max random int to roll when determining whether to grant an awardable entry for
    operations. 1/N chances.
CASUALTY_COUNT_FOR_HISTORY_ENTRY:
  def: '40000'
  type: int
  cmt: number of received casualties to receive a history entry (one only)
FIELD_OFFICER_PROMOTION_PENALTY:
  def: '0.25'
  type: float
  cmt: Amount of division experience lost when promoting a commander (reduced by
    modifiers)
HISTORICAL_ORDER_NAME_EXHAUSTION:
  def: 'false'
  type: bool
  cmt: Do historically chosen order instances exhaust their case names? If false ie,
    Operation Barbarossa will appear for any orders fulfilling the conditions for
    Germany
SHORE_BOMBARDMENT_COLLATERAL_DAMAGE_MULTIPLIER:
  def: '40.0'
  type: float
  cmt: Factor on shore bombardment damage purposes, for collateral damage.
SHORE_BOMBARDMENT_COLLATERAL_DAMAGE_CRIT_CHANCE_FACTOR:
  def: '0.0025'
  type: float
  cmt: Chance for crit (ie, high single building damage) to occur.
WAR_SCORE_LOSSES_RATIO:
  def: '0.5'
  type: float
  cmt: war score gained for every 1000 casualties
WAR_SCORE_LOSSES_MULT_IF_CAPITULATED:
  def: '0.25'
  type: float
  cmt: factor applied to war score gained from casualties if capitulated
WAR_SCORE_STRATEGIC_BOMBING_FACTOR:
  def: '0.02'
  type: float
  cmt: war score gained for every damage made to enemy's building with strategic bombing
WAR_SCORE_STRAT_BOMBING_DECAY_PER_CIVILIAN_FACTORY:
  def: '0.10'
  type: float
  cmt: monthly war score deducted from strategic bombing for every civilian factory in
    service on the bombed enemy side
WAR_SCORE_AIR_IC_LOSS_FACTOR:
  def: '0.08'
  type: float
  cmt: war score gained for every IC of damage done to an enemy's air mission
WAR_SCORE_LAND_DAMAGE_FACTOR:
  def: '0.1'
  type: float
  cmt: war score gained for every strengh damage done to an enemy's army
WAR_SCORE_ATTACKER_AND_WINNER_FACTOR:
  def: '1.2'
  type: float
  cmt: factor applied to war score gained for strength damage done when being the
    attacker and the winner
WAR_SCORE_LAND_IC_LOSS_FACTOR:
  def: '0.08'
  type: float
  cmt: war score gained for every IC damage done to an enemy's army
WAR_SCORE_PROVINCE_FACTOR:
  def: '4.0'
  type: float
  cmt: war score gained when capturing a province for the first time, multiplied by
    province's worth
WAR_SCORE_LEND_LEASE_GIVEN_IC_FACTOR:
  def: '0.003'
  type: float
  cmt: war score gained for every IC of lend lease sent to allies
WAR_SCORE_LEND_LEASE_GIVEN_FUEL_FACTOR:
  def: '0.003'
  type: float
  cmt: war score gained for every 100 units of fuel lend lease sent to allies
WAR_SCORE_LEND_LEASE_RECEIVED_IC_FACTOR:
  def: '0.002'
  type: float
  cmt: war score deducted for every IC of lend lease received from allies
WAR_SCORE_LEND_LEASE_RECEIVED_FUEL_FACTOR:
  def: '0.002'
  type: float
  cmt: war score deducted for every 100 units of fuel lend lease received from allies
CORPS_COMMANDER_DIVISIONS_CAP:
  def: '24'
  type: int
  cmt: how many divisions a corps commander is limited to. 0 = inf, < 0 = blocked
DIVISION_SIZE_FOR_XP:
  def: '8'
  type: int
  cmt: how many battalions should a division have to count as a full divisions when
    calculating XP stuff
CORPS_COMMANDER_ARMIES_CAP:
  def: '-1'
  type: int
  cmt: how many armies a corps commander is limited to. 0 = inf, < 0 = blocked
FIELD_MARSHAL_DIVISIONS_CAP:
  def: '24'
  type: int
  cmt: how many divisions a field marshall is limited to. 0 = inf, < 0 = blocked
FIELD_MARSHAL_ARMIES_CAP:
  def: '5'
  type: int
  cmt: how many armies a field marshall is limited to. 0 = inf, < 0 = blocked
UNIT_LEADER_GENERATION_CAPITAL_CONTINENT_FACTOR:
  def: '100'
  type: int
  cmt: Integer factor to multiply manpower.
RECON_SKILL_IMPACT:
  def: '5'
  type: int
  cmt: how many skillpoints is a recon advantage worth when picking a tactic.
MAX_DIVISION_BRIGADE_WIDTH:
  def: '5'
  type: int
  cmt: Max width of regiments in division designer.
MAX_DIVISION_BRIGADE_HEIGHT:
  def: '5'
  type: int
  cmt: Max height of regiments in division designer.
MIN_DIVISION_BRIGADE_HEIGHT:
  def: '4'
  type: int
  cmt: Min height of regiments in division designer.
MAX_DIVISION_SUPPORT_WIDTH:
  def: '1'
  type: int
  cmt: Max width of support in division designer.
MAX_DIVISION_SUPPORT_HEIGHT:
  def: '5'
  type: int
  cmt: Max height of support in division designer.
BASE_DIVISION_BRIGADE_GROUP_COST:
  def: '20'
  type: int
  cmt: Base cost to unlock a regiment slot
BASE_DIVISION_BRIGADE_CHANGE_COST:
  def: '5'
  type: int
  cmt: Base cost to change a regiment column.
BASE_DIVISION_SUPPORT_SLOT_COST:
  def: '10'
  type: int
  cmt: Base cost to unlock a support slot
MAX_ARMY_EXPERIENCE:
  def: '500'
  type: int
  cmt: Max army experience a country can store
MAX_NAVY_EXPERIENCE:
  def: '500'
  type: int
  cmt: Max navy experience a country can store
MAX_AIR_EXPERIENCE:
  def: '500'
  type: int
  cmt: Max air experience a country can store
COMBAT_MINIMUM_TIME:
  def: '4'
  type: int
  cmt: Shortest time possible for a combat in hours
SPOTTING_QUALITY_DROP_HOURS:
  def: '4'
  type: int
  cmt: Each X hours the intel quality drops after unit was spotted.
SPOTTING_QUALITY_NAVAL_RECON_DROP_HOURS:
  def: '12'
  type: int
  cmt: Each X hours the intel quality drops after unit was spotted by naval recon air
    mission.
LEADER_GROUP_MAX_SIZE:
  def: '1000'
  type: int
  cmt: 5,                      -- Max slots for leader groups.
MIN_SUPPLY_CONSUMPTION:
  def: '0.05'
  type: float
  cmt: minimum value of supply consumption that a unit can get
LAND_COMBAT_ORG_DICE_SIZE:
  def: '4'
  type: int
  cmt: nr of damage dice
LAND_COMBAT_STR_DICE_SIZE:
  def: '2'
  type: int
  cmt: nr of damage dice
LAND_COMBAT_STR_DAMAGE_MODIFIER:
  def: '0.060'
  type: float
  cmt: global damage modifier... but some equipment is returned at end of battles see :
    EQUIPMENT_COMBAT_LOSS_FACTOR
LAND_COMBAT_ORG_DAMAGE_MODIFIER:
  def: '0.053'
  type: float
  cmt: global damage modifier
LAND_AIR_COMBAT_STR_DAMAGE_MODIFIER:
  def: '0.08'
  type: float
  cmt: air global strength damage modifier
LAND_AIR_COMBAT_ORG_DAMAGE_MODIFIER:
  def: '0.10'
  type: float
  cmt: air global organization damage modifier
LAND_AIR_COMBAT_MAX_PLANES_PER_ENEMY_WIDTH:
  def: '3'
  type: int
  cmt: how many CAS/TAC can enter a combat depending on enemy width there
LAND_COMBAT_STR_ARMOR_ON_SOFT_DICE_SIZE:
  def: '2'
  type: int
  cmt: extra damage dice if our armor outclasses enemy
LAND_COMBAT_ORG_ARMOR_ON_SOFT_DICE_SIZE:
  def: '6'
  type: int
  cmt: extra damage dice if our armor outclasses enemy
LAND_COMBAT_STR_ARMOR_DEFLECTION_FACTOR:
  def: '0.5'
  type: float
  cmt: damage reduction if armor outclassing enemy
LAND_COMBAT_ORG_ARMOR_DEFLECTION_FACTOR:
  def: '0.5'
  type: float
  cmt: damage reduction if armor outclassing enemy
LAND_COMBAT_COLLATERAL_FORT_FACTOR:
  def: '0.005'
  type: float
  cmt: Factor to scale collateral damage to forts with.
LAND_COMBAT_COLLATERAL_INFRA_FACTOR:
  def: '0.0022'
  type: float
  cmt: Factor to scale collateral damage to infra with.
LAND_COMBAT_FORT_DAMAGE_CHANCE:
  def: '5'
  type: int
  cmt: chance to get a hit to damage on forts. (out of 100)
ATTRITION_DAMAGE_ORG:
  def: '0.08'
  type: float
  cmt: damage from attrition to Organisation
ATTRITION_EQUIPMENT_LOSS_CHANCE:
  def: '0.005'
  type: float
  cmt: Chance for loosing equipment when suffer attrition. Scaled up the stronger
    attrition is. Then scaled down by equipment reliability.
ATTRITION_WHILE_MOVING_FACTOR:
  def: '1.2'
  type: float
RELIABILITY_ORG_REGAIN:
  def: '-0.3'
  type: float
  cmt: how much reliability affects org regain
RELIABILITY_ORG_MOVING:
  def: '-1.0'
  type: float
  cmt: how much reliability affects org loss on moving
RELIABILITY_WEATHER:
  def: '3.0'
  type: float
  cmt: how much reliability is afffecting weather impact
RELIABILTY_RECOVERY:
  def: '0.40'
  type: float
  cmt: factor affecting how much equipment is returned "from the dead"
BASE_CHANCE_TO_AVOID_HIT:
  def: '90'
  type: int
  cmt: Base chance to avoid hit if defences left.
CHANCE_TO_AVOID_HIT_AT_NO_DEF:
  def: '60'
  type: int
  cmt: chance to avoid hit if no defences left.
COMBAT_MOVEMENT_SPEED:
  def: '0.33'
  type: float
  cmt: speed reduction base modifier in combat
TACTIC_SWAP_FREQUENCEY:
  def: '12'
  type: int
  cmt: hours between tactic swaps
PREFERRED_TACTIC_CHARACTER_SKILL_LEVEL_REQUIRED:
  def: '5'
  type: int
  cmt: Which level a field marhal or general has to be before they can pick their
    preferred tactic
COUNTRY_PREFERRED_TACTIC_WEIGHT_FACTOR:
  def: '0.25'
  type: float
  cmt: extra weight multiplier for the country preferred tactic when doing weighted
    random
ARMY_GENERAL_PREFERRED_TACTIC_WEIGHT_FACTOR:
  def: '0.5'
  type: float
  cmt: extra weight multiplier for the army general preferred tactic when doing weighted
    random
FIELD_MARSHAL_PREFERRED_TACTIC_WEIGHT_FACTOR:
  def: '0.25'
  type: float
  cmt: extra weight multiplier for the field marhsal preferred tactic when doing
    weighted random
PREFERRED_TACTIC_COMMAND_POWER_COST:
  def: '20'
  type: int
  cmt: command point cost for changing preferred tactic
INITIATIVE_PICK_COUNTER_ADVANTAGE_FACTOR:
  def: '0.35'
  type: float
  cmt: advantage per leader level for picking a counter
AMPHIBIOUS_INVADE_MOVEMENT_COST:
  def: '24.0'
  type: float
  cmt: total progress cost of movement while amphibious invading
LAND_SPEED_MODIFIER:
  def: '0.05'
  type: float
  cmt: basic speed control
RIVER_CROSSING_PENALTY:
  def: '-0.3'
  type: float
  cmt: small river crossing
RIVER_CROSSING_PENALTY_LARGE:
  def: '-0.6'
  type: float
  cmt: large river crossing
RIVER_CROSSING_SPEED_PENALTY:
  def: '-0.25'
  type: float
  cmt: small river crossing
RIVER_CROSSING_SPEED_PENALTY_LARGE:
  def: '-0.5'
  type: float
  cmt: large river crossing
RIVER_SMALL_START_INDEX:
  def: '0'
  type: int
  cmt: color indices for rivers
RIVER_SMALL_STOP_INDEX:
  def: '6'
  type: int
RIVER_LARGE_STOP_INDEX:
  def: '11'
  type: int
BASE_FORT_PENALTY:
  def: '-0.15'
  type: float
  cmt: fort penalty
MULTIPLE_COMBATS_PENALTY:
  def: '-0.5'
  type: float
  cmt: defender penalty if attacked from multiple directions
DIG_IN_FACTOR:
  def: '0.02'
  type: float
  cmt: bonus factor for each dug-in level
ARMY_LEADER_XP_GAIN_PER_UNIT_IN_COMBAT:
  def: '0.1'
  type: float
  cmt: XP gain per unit in combat
CONSTANT_XP_RATIO_FOR_MULTIPLE_LEADERS_IN_SAME_COMBAT:
  def: '0.5'
  type: float
  cmt: if there are multiple leaders in same combat, each one gets thisratio +
    (1-thisratio)/num leaders. amount of xp each general gets scales 1 0.75 0.66 etc for
    1 2 3 generals
BASE_LEADER_TRAIT_GAIN_XP:
  def: '0.45'
  type: float
  cmt: Base xp gain for traits per hour for armies
MAX_NUM_TRAITS:
  def: '-1'
  type: int
  cmt: cant have more, -1 to disable
ENEMY_AIR_SUPERIORITY_IMPACT:
  def: '-0.35'
  type: float
  cmt: effect on defense due to enemy air superiorty
ENEMY_AIR_SUPERIORITY_DEFENSE:
  def: '0.70'
  type: float
  cmt: more AA attack will approach this amount of help (diminishing returns)
ENEMY_AIR_SUPERIORITY_DEFENSE_STEEPNESS:
  def: '112'
  type: int
  cmt: how quickly defense approaches the max impact diminishing returns curve
ENEMY_AIR_SUPERIORITY_SPEED_IMPACT:
  def: '-0.3'
  type: float
  cmt: effect on speed due to enemy air superiority
ANTI_AIR_TARGETTING_TO_CHANCE:
  def: '0.07'
  type: float
  cmt: Balancing value to determine the chance of ground AA hitting an attacking
    airplane, affecting both the effective average damage done by AA to airplanes, and
    the reduction of damage done by airplanes due to AA support
ANTI_AIR_ATTACK_TO_AMOUNT:
  def: '0.005'
  type: float
  cmt: Balancing value to convert equipment stat anti_air_attack to the random % value
    of airplanes being hit.
ENCIRCLED_PENALTY:
  def: '-0.3'
  type: float
  cmt: penalty when completely encircled
UNIT_EXPERIENCE_PER_COMBAT_HOUR:
  def: '0.0001'
  type: float
UNIT_EXPERIENCE_SCALE:
  def: '1.0'
  type: float
UNIT_EXPERIENCE_PER_TRAINING_DAY:
  def: '0.0015'
  type: float
TRAINING_MAX_LEVEL:
  def: '2'
  type: int
DEPLOY_TRAINING_MAX_LEVEL:
  def: '1'
  type: int
TRAINING_EXPERIENCE_SCALE:
  def: '62.0'
  type: float
TRAINING_ORG:
  def: '0.2'
  type: float
ARMY_EXP_BASE_LEVEL:
  def: '1'
  type: int
UNIT_EXP_LEVELS:
  def:
    - [0.1, 0.3, 0.75, 0.9]
  type: table
  cmt: Experience needed to progress to the next level
FIELD_EXPERIENCE_SCALE:
  def: '0.0008'
  type: float
  cmt: (Country) Army experience gain factor
FIELD_EXPERIENCE_MAX_PER_DAY:
  def: '1.2'
  type: float
  cmt: Most xp you can gain per day
EXPEDITIONARY_FIELD_EXPERIENCE_SCALE:
  def: '0.3'
  type: float
  cmt: reduction factor in Xp from expeditionary forces
LEND_LEASE_FIELD_EXPERIENCE_SCALE:
  def: '0.0005'
  type: float
  cmt: Experience scale for lend leased equipment used in combat.
LEADER_EXPERIENCE_SCALE:
  def: '1.0'
  type: float
SLOWEST_SPEED:
  def: '4'
  type: int
REINFORCEMENT_REQUEST_MAX_WAITING_DAYS:
  def: '14'
  type: int
  cmt: Every X days the equipment will be sent, regardless if still didn't produced all
    that has been requested.
REINFORCEMENT_REQUEST_DAYS_FREQUENCY:
  def: '7'
  type: int
  cmt: How many days must pass until we may give another reinforcement request
EXPERIENCE_COMBAT_FACTOR:
  def: '0.25'
  type: float
UNIT_DIGIN_CAP:
  def: '5'
  type: int
  cmt: how "deep" you can dig you can dig in until hitting max bonus
UNIT_DIGIN_SPEED:
  def: '1'
  type: int
  cmt: how "deep" you can dig a day.
PARACHUTE_FAILED_EQUIPMENT_DIV:
  def: '50.0'
  type: float
  cmt: When the transport plane was shot down, we drop unit with almost NONE equipment
PARACHUTE_FAILED_MANPOWER_DIV:
  def: '100.0'
  type: float
  cmt: When the transport plane was shot down, we drop unit with almost NONE manpower
PARACHUTE_FAILED_STR_DIV:
  def: '10.0'
  type: float
  cmt: When the transport plane was shot down, we drop unit with almost NONE strenght
PARACHUTE_DISRUPTED_EQUIPMENT_DIV:
  def: '1.5'
  type: float
  cmt: When the transport plane was hit, we drop unit with reduced equipment. Penalty is
    higher as more hits was received (and AA guns was in the state).
PARACHUTE_DISRUPTED_MANPOWER_DIV:
  def: '1.9'
  type: float
  cmt: When the transport plane was hit, we drop unit with reduced manpower. Penalty is
    higher as more hits was received (and AA guns was in the state).
PARACHUTE_DISRUPTED_STR_DIV:
  def: '2.2'
  type: float
  cmt: When the transport plane was hit, we drop unit with reduced strength. Penalty is
    higher as more hits was received (and AA guns was in the state).
PARACHUTE_PENALTY_RANDOMNESS:
  def: '0.1'
  type: float
  cmt: Random factor for str,manpower,eq penalties.
PARACHUTE_DISRUPTED_AA_PENALTY:
  def: '1'
  type: int
  cmt: How much the Air defence in the state (from AA buildings level * air_defence) is
    scaled to affect overall disruption (equipment,manpower,str).
PARACHUTE_COMPLETE_ORG:
  def: '0.4'
  type: float
  cmt: Organisation value (in %) after unit being dropped, regardless if failed,
    disrupted, or successful.
PARACHUTE_ORG_REGAIN_PENALTY_DURATION:
  def: '120'
  type: int
  cmt: penalty in org regain after being parachuted. Value is in hours.
PARACHUTE_ORG_REGAIN_PENALTY_MULT:
  def: '-0.8'
  type: float
  cmt: penalty to org regain after being parachuted.
SHIP_MORALE_TO_ORG_REGAIN_BASE:
  def: '0.2'
  type: float
  cmt: Base org regain per hour
BASE_NIGHT_ATTACK_PENALTY:
  def: '-0.5'
  type: float
EXILE_EQUIPMENT:
  def: '1.0'
  type: float
  cmt: Amount of equipment to keep
EXILE_ORG:
  def: '0.0'
  type: float
  cmt: Amount of org to keep
EXPERIENCE_LOSS_FACTOR:
  def: '1.00'
  type: float
  cmt: percentage of experienced solders who die when manpower is removed
EQUIPMENT_COMBAT_LOSS_FACTOR:
  def: '0.70'
  type: float
  cmt: % of equipment lost to strength ratio in combat, so some % is returned if below 1
SUPPLY_USE_FACTOR_MOVING:
  def: '1.5'
  type: float
  cmt: Deprecated/Unused
SUPPLY_USE_FACTOR_INACTIVE:
  def: '0.95'
  type: float
  cmt: Deprecated/Unused
SUPPLY_GRACE:
  def: '72'
  type: int
  cmt: troops always carry 3 days of food and supply
SUPPLY_GRACE_MAX_REDUCE_PER_HOUR:
  def: '2'
  type: int
  cmt: supply grace is not decreased instantly when it is buffed temporarily and buff is
    removed
SUPPLY_ORG_MAX_CAP:
  def: '0.35'
  type: float
  cmt: Max organization is factored by this if completely out of supply
MAX_OUT_OF_SUPPLY_DAYS:
  def: '30'
  type: int
  cmt: how many days of shitty supply until max penalty achieved
OUT_OF_SUPPLY_ATTRITION:
  def: '0.20'
  type: float
  cmt: max attrition when out of supply
OUT_OF_SUPPLY_SPEED:
  def: '-0.8'
  type: float
  cmt: max speed reduction from supply
NON_CORE_SUPPLY_SPEED:
  def: '-0.5'
  type: float
  cmt: we are not running on our own VP supply so need to steal stuff along the way
NON_CORE_SUPPLY_AIR_SPEED:
  def: '-0.25'
  type: float
  cmt: we are not running on our own VP supply so need to steal stuff along the way, a
    bit less due to air supply
OUT_OF_SUPPLY_MORALE:
  def: '-0.2'
  type: float
  cmt: max org regain reduction from supply
TRAINING_ATTRITION:
  def: '0.05'
  type: float
  cmt: amount of extra attrition from being in training
TRAINING_MIN_STRENGTH:
  def: '0.1'
  type: float
  cmt: if strength is less than this, the unit will pause training until it's been
    reinforced
TRAINING_MAX_DAILY_COUNTRY_EXP:
  def: '0.08'
  type: float
  cmt: Maximum army XP gained per day from training
AIR_SUPPORT_BASE:
  def: '0.25'
  type: float
  cmt: CAS bonus factor for air support moddifier for land unit in combat
LOW_SUPPLY:
  def: '0.99'
  type: float
  cmt: When the supply status of an unit becomes low.
BORDER_WAR_ATTRITION_FACTOR:
  def: '0.1'
  type: float
  cmt: How much of borderwar balance of power makes it into attrition
BORDER_WAR_VICTORY:
  def: '0.8'
  type: float
  cmt: At wich border war balance of power is victory declared
REINFORCE_CHANCE:
  def: '0.02'
  type: float
  cmt: base chance to join combat from back line when empty
SPEED_REINFORCEMENT_BONUS:
  def: '0.01'
  type: float
  cmt: chance to join combat bonus by each 100% larger than infantry base (up to 200%)
OVERSEAS_LOSE_EQUIPMENT_FACTOR:
  def: '0.75'
  type: float
  cmt: percentage of equipment lost disbanded overseas
NAVAL_TRANSFER_DISBAND_MANPOWER_FACTOR:
  def: '0.5'
  type: float
  cmt: percentage of manpower returned when a naval transfering unit is disbanded
ENCIRCLED_DISBAND_MANPOWER_FACTOR:
  def: '0.2'
  type: float
  cmt: percentage of manpower returned when an encircled unit is disbanded
ORG_LOSS_FACTOR_ON_CONQUER:
  def: '0.2'
  type: float
  cmt: percentage of (max) org loss on takign enemy province
LOW_ORG_FOR_ATTACK:
  def: '0.3'
  type: float
  cmt: at what org % we start affecting speed when doign hostile moves. scales down
    ZERO_ORG_MOVEMENT_MODIFIER
PLANNING_DECAY:
  def: '0.01'
  type: float
PLAYER_ORDER_PLANNING_DECAY:
  def: '0.03'
  type: float
  cmt: Amount of planning lost due to player manual order
PLANNING_GAIN:
  def: '0.02'
  type: float
NAVAL_INVASION_PLANNING_BONUS_GAIN:
  def: '0.02'
  type: float
  cmt: Planning Bonus gain per day for naval invasions
NAVAL_INVASION_PLANNING_BONUS_MALUS:
  def: '-1'
  type: int
  cmt: Malus in percentage for the planning bonus gain for naval invasions
PLANNING_MAX:
  def: '0.3'
  type: float
  cmt: can get more from techs
CIVILWAR_ORGANIZATION_FACTOR:
  def: '0.3'
  type: float
  cmt: Multiplier of org for both sides when civilwar.
PLAN_CONSIDERED_GOOD:
  def: '0.25'
  type: float
  cmt: Plan evaluations above this value are considered more or less safe
PLAN_CONSIDERED_BAD:
  def: '-0.25'
  type: float
  cmt: Plan evaluations below this value are considered unsafe
PLAN_MIN_AUTOMATED_EMPTY_POCKET_SIZE:
  def: '2'
  type: int
  cmt: The battle plan system will only automatically attack provinces in pockets that
    has no resistance and are no bigger than these many provinces
PLAN_SPREAD_ATTACK_WEIGHT:
  def: '12.0'
  type: float
  cmt: The higher the value, the less it should crowd provinces with multiple attacks.
PLAN_NEIGHBORING_ENEMY_PROVINCE_FACTOR:
  def: '0.7'
  type: float
  cmt: When calculating the importance of provinces, it takes number of enemy provinces
    into account, factored by this
PLAN_PROVINCE_BASE_IMPORTANCE:
  def: '2.0'
  type: float
  cmt: Used when calculating the calue of front and defense area provinces for the
    battle plan system
PLAN_PROVINCE_LOW_VP_DEFENSE_THRESHOLD:
  def: '2.0'
  type: float
  cmt: For area defense VP orders, what are the thresholds for "low", "medium" and
    "high" VP values
PLAN_PROVINCE_MEDIUM_VP_DEFENSE_THRESHOLD:
  def: '8.0'
  type: float
  cmt: see above
PLAN_PROVINCE_HIGH_VP_DEFENSE_THRESHOLD:
  def: '25.0'
  type: float
  cmt: see above
PLAN_PROVINCE_LOW_VP_DEFENSE_IMPORTANCE:
  def: '2.0'
  type: float
  cmt: For area defense VP orders, use this value for relative importance
PLAN_PROVINCE_MEDIUM_VP_DEFENSE_IMPORTANCE:
  def: '5.0'
  type: float
  cmt: see above
PLAN_PROVINCE_HIGH_VP_DEFENSE_IMPORTANCE:
  def: '10.0'
  type: float
  cmt: see above
PLAN_PROVINCE_CAPITAL_DEFENSE_IMPORTANCE:
  def: '50.0'
  type: float
  cmt: For area defense VP orders, boost importance value with this if it's the capital
MIN_VP_NEEDED_FOR_DEFENSE_ORDER_ASSIGNMENTS:
  def: '1.0'
  type: float
  cmt: For area devense VP orders, ignore provinces with VP <= this value
PLAN_PROVINCE_LOW_VP_IMPORTANCE_FRONT:
  def: '2.0'
  type: float
  cmt: Used when calculating the calue of fronts in the battle plan system
PLAN_PROVINCE_MEDIUM_VP_IMPORTANCE_FRONT:
  def: '2.25'
  type: float
  cmt: Used when calculating the calue of fronts in the battle plan system
PLAN_PROVINCE_HIGH_VP_IMPORTANCE_FRONT:
  def: '2.75'
  type: float
  cmt: Used when calculating the calue of fronts in the battle plan system
PLAN_SHARED_FRONT_PROV_IMPORTANCE_FACTOR:
  def: '0.8'
  type: float
  cmt: If fornt orders share end provinces, they should each have a somewhat reduced
    prio due to it being shared.
PLAN_PORVINCE_PORT_BASE_IMPORTANCE:
  def: '12.0'
  type: float
  cmt: Added importance for area defense province with a port
PLAN_PORVINCE_PORT_LEVEL_FACTOR:
  def: '1.5'
  type: float
  cmt: Bonus factor for port level
PLAN_PORVINCE_AIRFIELD_BASE_IMPORTANCE:
  def: '3.0'
  type: float
  cmt: Added importance for area defense province with air field
PLAN_PORVINCE_AIRFIELD_POPULATED_FACTOR:
  def: '1.5'
  type: float
  cmt: Bonus factor when an airfield has planes on it
PLAN_PORVINCE_AIRFIELD_LEVEL_FACTOR:
  def: '0.25'
  type: float
  cmt: Bonus factor for airfield level
PLAN_PORVINCE_RESISTANCE_BASE_IMPORTANCE:
  def: '10.0'
  type: float
  cmt: Used when calculating the calue of defense area provinces for the battle plan
    system (factored by resistance level)
PLAN_PROVINCE_VP_PORT_FACTOR:
  def: '0.25'
  type: float
PLAN_AREA_DEFENSE_ENEMY_CONTROLLER_SCORE:
  def: '25.0'
  type: float
  cmt: Score applied to provinces in the defense area order controlled by enemies
PLAN_AREA_DEFENSE_ENEMY_UNIT_FACTOR:
  def: '-2.0'
  type: float
  cmt: Factor applied to province score in area defense order per enemy unit in that
    province
PLAN_AREA_DEFENSE_FORT_IMPORTANCE:
  def: '0.25'
  type: float
  cmt: Used when calculating the value of defense area provinces for the battle plan
    system, works as multipliers on the rest
PLAN_AREA_DEFENSE_COASTAL_FORT_IMPORTANCE:
  def: '3.0'
  type: float
  cmt: Used when calculating the value of defense area provinces for the battle plan
    system
PLAN_AREA_DEFENSE_COAST_NO_FORT_IMPORTANCE:
  def: '1.1'
  type: float
  cmt: Used when calculating the value of defense area provinces for the battle plan
    system
PLAN_AREA_DEFENSE_HAS_RAIL_IMPORTANCE:
  def: '1.5'
  type: float
  cmt: Used when calculating the value of defense area provinces for the battle plan
    system
PLAN_AREA_DEFENSE_HAS_SUPPLY_NODE:
  def: '20.0'
  type: float
  cmt: Used when calculating the value of defense area provinces for the battle plan
    system
PLAN_AREA_DEFENSE_FACILITY:
  def: '15.0'
  type: float
  cmt: Used when calculating the value of defense area provinces for the battle plan
    system
PLAN_STICKINESS_FACTOR:
  def: '100.0'
  type: float
  cmt: Factor used in unitcontroller when prioritizing units for locations
PLAN_PROVINCE_PRIO_DISTRIBUTION_MIN:
  def: '0.7'
  type: float
  cmt: Lowest fraction of divisions that will be distributed based on province priority
PLAN_PROVINCE_PRIO_DISTRIBUTION_MAX:
  def: '1.0'
  type: float
  cmt: Highest fraction of divisions that will be distributed based on province priority
PLAN_PROVINCE_PRIO_DISTRIBUTION_DPP_HIGH:
  def: '3.0'
  type: float
  cmt: At what divisions per province should we use PLAN_PROVINCE_PRIO_DISTRIBUTION_MIN
PLAN_PROVINCE_PRIO_DISTRIBUTION_DPP_LOW:
  def: '2.0'
  type: float
  cmt: At what divisions per province should we use PLAN_PROVINCE_PRIO_DISTRIBUTION_MAX
PLAN_EXECUTE_CAREFUL_LIMIT:
  def: '25'
  type: int
  cmt: When looking for an attack target, this score limit is required in the battle
    plan to consider province for attack
PLAN_EXECUTE_BALANCED_LIMIT:
  def: '0'
  type: int
  cmt: When looking for an attack target, this score limit is required in the battle
    plan to consider province for attack
PLAN_EXECUTE_RUSH:
  def: '-200'
  type: int
  cmt: When looking for an attack target, this score limit is required in the battle
    plan to consider province for attack
PLAN_EXECUTE_CAREFUL_MAX_FORT:
  def: '5'
  type: int
  cmt: If execution mode is set to careful, units will not attack provinces with fort
    levels greater than or equal to this
PLAN_EXECUTE_SUPPLY_CHECK:
  def:
    - [1.0, 0.0, 0.0, 1.0, 0.0]
  type: table
  cmt: for each execution mode how careful should we be with supply (1.0 means full
    required supply available, zero is no limit).
PLAN_MAX_PROGRESS_TO_JOIN:
  def: '0.50'
  type: float
  cmt: If Lower progress than this, probably needs support
COHESION_IMMOBILE_PLANNING_SPEED_MULTIPLIER:
  def: '0.50'
  type: float
  cmt: If using the 'immobile' cohesion setting, factor ALL planning speed growth by
    this
PLAN_COHESION_WEIGHTS:
  def:
    - [1.0, 40.0, 80.0, 100.0]
  type: table
  cmt: for each cohesion setting, how keen on relocating from distance should we be?
    (default 1.0), higher weight = shorter max distance. The last entry is special-
    cased, the value should have no effect and units will just not move anywhere, ever.
PLAN_COHESION_DISTANCE_MAX_WHEN_LEFT_BEHIND:
  def: '38'
  type: int
  cmt: Unused and deprecated - will be removed in next major version.
PLAN_BLITZ_OPTIMISM:
  def: '0.2'
  type: float
  cmt: Additional combat balance value in favor of blitzing side when considering
    targets (not a combat bonus, just offsets planning)
MIN_BALANCE_SCORE_TO_PROCEED_ATTACK:
  def: '0.2'
  type: float
  cmt: A combat balance score of less than this will prevent auto attacking
DYNAMIC_MODIFIER_ATTACK_BIAS:
  def: '1.0'
  type: float
  cmt: This factors the weighting bias of dynamic attack modifiers
FLANKED_PROVINCES_COUNT:
  def: '3'
  type: int
  cmt: Attacker has to attack from that many provinces for the attack to be considered
    as flanking
EQUIPMENT_REPLACEMENT_RATIO:
  def: '0.1'
  type: float
  cmt: Equipment min ratio after blocking the equipment type
NUKE_DELAY_HOURS:
  def: '2'
  type: int
  cmt: How many hours does it take for the nuclear drop to happen
PARADROP_PENALTY:
  def: '-0.3'
  type: float
  cmt: Combat penalty when recently paradropped
PARADROP_HOURS:
  def: '48'
  type: int
  cmt: time paratroopers suffer penalties in combat
COMBAT_SUPPLY_LACK_ATTACKER_ATTACK:
  def: '-0.25'
  type: float
  cmt: attack combat penalty for attacker if out of supply
COMBAT_SUPPLY_LACK_ATTACKER_DEFEND:
  def: '-0.65'
  type: float
  cmt: defend combat penalty for attacker if out of supply
COMBAT_SUPPLY_LACK_DEFENDER_ATTACK:
  def: '-0.35'
  type: float
  cmt: attack combat penalty for defender if out of supply
COMBAT_SUPPLY_LACK_DEFENDER_DEFEND:
  def: '-0.15'
  type: float
  cmt: defend combat penalty for defender if out of supply
COMBAT_STACKING_START:
  def: '5'
  type: int
  cmt: at what nr of divisions stacking penalty starts
COMBAT_STACKING_EXTRA:
  def: '3'
  type: int
  cmt: extra stacking from directions
COMBAT_STACKING_PENALTY:
  def: '-0.02'
  type: float
  cmt: how much stackign penalty per division
COMBAT_OVER_WIDTH_PENALTY:
  def: '-1'
  type: int
  cmt: over combat width penalty per %.
COMBAT_OVER_WIDTH_PENALTY_MAX:
  def: '-0.33'
  type: float
  cmt: over combat width max (when you cant join no more).
RETREAT_SPEED_FACTOR:
  def: '0.25'
  type: float
  cmt: speed bonus when retreating
WITHDRAWING_SPEED_FACTOR:
  def: '0.15'
  type: float
  cmt: speed bonus when withdrawing
STRATEGIC_SPEED_INFRA_BASE:
  def: '5.0'
  type: float
  cmt: Base speed of strategic redeployment when not on railways
STRATEGIC_SPEED_INFRA_MAX:
  def: '10.0'
  type: float
  cmt: Additional speed of strategic redeployment on max-level infrastructure
STRATEGIC_SPEED_RAIL_BASE:
  def: '10.0'
  type: float
  cmt: Base speed of strategic redeployment when on railways
STRATEGIC_SPEED_RAIL_MAX:
  def: '25.0'
  type: float
  cmt: Additional speed of strategic redeployment on max-level railways
STRATEGIC_REDEPLOY_ORG_RATIO:
  def: '0.1'
  type: float
  cmt: Ratio of max org while strategic redeployment
BATALION_NOT_CHANGED_EXPERIENCE_DROP:
  def: '0.0'
  type: float
  cmt: Division experience drop if unit has same batalion
BATALION_CHANGED_EXPERIENCE_DROP:
  def: '0.5'
  type: float
  cmt: Division experience drop if unit has different batalion
ARMOR_VS_AVERAGE:
  def: '0.4'
  type: float
  cmt: how to weight in highest armor & pen vs the division average
PEN_VS_AVERAGE:
  def: '0.4'
  type: float
LAND_EQUIPMENT_BASE_COST:
  def: '10'
  type: int
  cmt: Cost in XP to upgrade a piece of equipment one level is base + ( total levels *
    ramp )
LAND_EQUIPMENT_RAMP_COST:
  def: '5'
  type: int
NAVAL_EQUIPMENT_BASE_COST:
  def: '25'
  type: int
NAVAL_EQUIPMENT_RAMP_COST:
  def: '5'
  type: int
AIR_EQUIPMENT_BASE_COST:
  def: '25'
  type: int
AIR_EQUIPMENT_RAMP_COST:
  def: '5'
  type: int
FASTER_ORG_REGAIN_LEVEL:
  def: '0.25'
  type: float
FASTER_ORG_REGAIN_MULT:
  def: '1.0'
  type: float
SLOWER_ORG_REGAIN_LEVEL:
  def: '0.80'
  type: float
SLOWER_ORG_REGAIN_MULT:
  def: '-0.5'
  type: float
DISBAND_MANPOWER_LOSS:
  def: '0.0'
  type: float
MIN_DIVISION_DEPLOYMENT_TRAINING:
  def: '0.2'
  type: float
  cmt: Min level of division training
FRONTLINE_EXPANSION_FACTOR:
  def: '0.6'
  type: float
  cmt: When attacking along a frontline, how much should units spread out as they
    advance. 0.0 means head (more or less) directly to the drawn frontline, with no
    distractions
FRONT_MIN_PATH_TO_REDEPLOY:
  def: '8'
  type: int
  cmt: If a units path is at least this long to reach its front location, it will
    strategically redeploy.
ARMY_INITIATIVE_REINFORCE_FACTOR:
  def: '0.25'
  type: float
  cmt: scales initiative for reinforce chance
BASE_CAPTURE_EQUIPMENT_RATIO:
  def: '0.0'
  type: float
  cmt: after a successful land combat, ratio of the equipments that are being
    captured/salvaged from enemy's lost equipment
ACCLIMATIZATION_IN_COMBAT_SPEED_FACTOR:
  def: '3'
  type: int
  cmt: Acclimatization speed multiplier while being in combat.
ACCLIMATIZATION_SPEED_GAIN:
  def: '0.15'
  type: float
  cmt: A variable used to balance the overall speed of gaining the acclimatization
ACCLIMATIZATION_LOSS_SPEED_FACTOR:
  def: '2.0'
  type: float
  cmt: Loosing one acclimatization while being under affect of the opposite climate
    should cause it to drop down much faster than gaining.
PROMOTE_LEADER_CP_COST:
  def: '40.0'
  type: float
  cmt: cost of promoting a leader
FIELD_MARSHAL_ARMY_BONUS_RATIO:
  def: '0.5'
  type: float
  cmt: ratio to apply regular bonuses FM bonuses to armies
FIELD_MARSHAL_XP_RATIO:
  def: '0.3'
  type: float
  cmt: xp gain ratio for army group leaders
GARRISON_ORDER_ARMY_CAP_FACTOR:
  def: '3.0'
  type: float
  cmt: armies gets increased cap when they are garrisoned
COMMANDER_LEVEL_UP_STAT_COUNT:
  def: '3'
  type: int
  cmt: num stats gained on level up
COMMANDER_LEVEL_UP_STAT_WEIGHTS:
  def:
    - [5, 5, 5, 5]
  type: table
  cmt: level up stat random base weights attack, defense, planning, logistics
NAVY_LEADER_LEVEL_UP_STAT_WEIGHTS:
  def:
    - [5, 5, 5, 5]
  type: table
  cmt: level up stat random base weights attack, defense, maneuvering, coordination
UNIT_LEADER_INITIAL_TRAIT_SLOT:
  def:
    - [1.0]  # field marshal
    - [0.0]  # corps commander
    - [1.0]  # navy general
    - [0.0]  # operative
  type: table
  cmt: trait slot for 0 level leader
UNIT_LEADER_TRAIT_SLOT_PER_LEVEL:
  def:
    - [0.5]  # field marshal
    - [0.5]  # corps commander
    - [0.5]  # navy general
    - [0.0]  # operative
  type: table
  cmt: num extra traits on each level
UNIT_LEADER_USE_NONLINEAR_XP_GAIN:
  def: 'true'
  type: bool
  cmt: Whether unit leader XP gain is scaled by 1/<nr_of_traits>
HOURS_REQ_REJOIN_BORDER_WAR_FOR_INJURED_UNITS:
  def: '-1'
  type: int
  cmt: minimum hours required for units to rejoin border wars, values below zero will
    make units never return
NEW_COMMANDER_RANDOM_PERSONALITY_TRAIT_CHANCES:
  def:
    - [0.5]  # 50% for first trait
    - [0.15]  # 15% for second trait after that
  type: table
  cmt: chances to gain a personality trait for new generals
NEW_COMMANDER_RANDOM_BASIC_TRAIT_CHANCES:
  def: ''
  type: table
  cmt: chances to gain a basic trait for new generals
NEW_COMMANDER_RANDOM_STATUS_TRAIT_CHANCES:
  def: ''
  type: table
  cmt: chances to gain a status trait for new generals
NEW_OPERATIVE_RANDOM_PERSONALITY_TRAIT_CHANCES:
  def:
    - [0.5]  # 50% for first trait
    - [0.1]  # 10% for second trait after that
  type: table
  cmt: chances to gain a personality trait for new operatives
NEW_OPERATIVE_RANDOM_BASIC_TRAIT_CHANCES:
  def:
    - [0.25]  # 25% for first trait
    - [0.05]  # 5% for second trait after that
  type: table
  cmt: chances to gain a basic trait for new operatives
NEW_OPERATIVE_RANDOM_STATUS_TRAIT_CHANCES:
  def: ''
  type: table
  cmt: chances to gain a status trait for new operatives
NEW_COMMANDER_RANDOM_SKILL_CHANCES:
  def: ''
  type: table
  cmt: chances to give a random stat skill for new operatives
NEW_NAVY_LEADER_RANDOM_SKILL_CHANCES:
  def: ''
  type: table
  cmt: chances to give a random stat skill point for a new admiral
UNIT_LEADER_MODIFIER_COOLDOWN_ON_GROUP_CHANGE:
  def: '15'
  type: int
  cmt: time in days for a unit leader to regain its modifiers
UNIT_LEADER_ASSIGN_TRAIT_COST:
  def: '15.0'
  type: float
  cmt: cost to assign a new trait to a unit leader
ATTACHED_WINGS_ORDER_UPDATE_DAYS:
  def: '5'
  type: int
  cmt: Days untill the attached wing will update the order
BORDER_WAR_WIN_DAYS_AGAINST_EMPTY_OPPONENTS:
  def: '14'
  type: int
  cmt: border wars will be automatically won if no opponent shows up for this duration
MAX_RELATIVE_COMBAT_DAMAGE_TO_MODIFY_XP:
  def: '4.0'
  type: float
  cmt: you gain more XP if you are doing more damage relative to enemy, this is the max
    relative amount to gain following RATe
XP_GAIN_FACTOR_FOR_MAX_RELATIVE_COMBAT_DAMAGE:
  def: '4.0'
  type: float
  cmt: XP factor scaling for max relative combat damage
XP_DECAY_RATE_PER_HOUR_IN_COMBAT:
  def: '0.03'
  type: float
  cmt: you get reduced XP as combat drags
MIN_XP_RATE_TO_DECAY:
  def: '0.1'
  type: float
  cmt: minimum XP factor for dragged combats
XP_GAIN_PER_OVERRUN_UNIT:
  def: '35.0'
  type: float
  cmt: fixed XP gain per overrun unit
XP_GAIN_FOR_SHATTERING:
  def: '35.0'
  type: float
  cmt: fixed XP gain per shattered unit
UNIT_UPKEEP_ATTRITION:
  def: '0.00'
  type: float
  cmt: Constant attrition value applied to armies.
FUEL_PENALTY_START_RATIO:
  def: '0.25'
  type: float
  cmt: ratio of fuel in an army to start getting penalties
FUEL_PENALTY_START_RATIO_BUFFER:
  def: '0.1'
  type: float
  cmt: buffer that keeps the out-of-fuel alert open even when above the
    FUEL_PENALTY_START_RATIO threshold, so that it doesn't spam-ping when fluctuating
SURPLUS_SUPPLY_RATIO_FOR_ZERO_FUEL_FLOW:
  def: '0.5'
  type: float
  cmt: if a supply chunk has more supply needed than this ratio + 1 compared to its max
    supply flow, the units inside the chiunk will get no fuel
ARMY_MAX_FUEL_FLOW_MULT:
  def: '2.0'
  type: float
  cmt: max fuel ratio that an army can get per hour, multiplied by supply situation
ARMY_FUEL_COST_MULT:
  def: '0.5'
  type: float
  cmt: fuel cost multiplier for all army related stuff
ARMY_COMBAT_FUEL_MULT:
  def: '1.0'
  type: float
  cmt: fuel consumption ratio in combat (plus ARMY_MOVEMENT_FUEL_MULT if you are also
    moving. ie offensive combat)
ARMY_TRAINING_FUEL_MULT:
  def: '1.0'
  type: float
  cmt: fuel consumption ratio while training
ARMY_MOVEMENT_FUEL_MULT:
  def: '1.0'
  type: float
  cmt: fuel consumption ratio while moving
ARMY_NAVAL_TRANSFER_FUEL_MULT:
  def: '0.0'
  type: float
  cmt: fuel consumption ratio while naval transferring
ARMY_STRATEGIC_DEPLOYMENT_FUEL_MULT:
  def: '0.0'
  type: float
  cmt: fuel consumption ratio while doing strategic deployment
ARMY_IDLE_FUEL_MULT:
  def: '0.0'
  type: float
  cmt: fuel consumption ratio while just existing
FUEL_EFFICIENCY_RAID_MULTIPLIER:
  def: '1.0'
  type: float
  cmt: convoy raid multiplier for fuel sunk
FUEL_FLOW_PENALTY_FOR_SUPPLY_CHUNK_EDGE_RATIO:
  def: '0.5'
  type: float
  cmt: supply flow that is limited by control of incoming edge provinces will have
    lesser effect on fuel flow
OUT_OF_FUEL_EQUIPMENT_MULT:
  def: '0.1'
  type: float
  cmt: ratio of the stats that you get from equipments that uses fuel and you lack it
OUT_OF_FUEL_SPEED_MULT:
  def: '0.4'
  type: float
  cmt: speed mult that armies get when out of fuel
OUT_OF_FUEL_TRAINING_XP_GAIN_MULT:
  def: '0.0'
  type: float
  cmt: xp gain mult from training when a unit is out of fuel
FUEL_CAPACITY_DEFAULT_HOURS:
  def: '96'
  type: int
  cmt: default capacity if not specified
MAX_ESTIMATED_PLAN_UNITS_NOT_IN_PLACE_FACTOR:
  def: '-0.6'
  type: float
  cmt: Scaled by % of units not in place. Used to be a flat -50%
DAMAGE_SPLIT_ON_FIRST_TARGET:
  def: '0.35'
  type: float
  cmt: % of damage dealt to the first target in a combat. The rest will be split amongst
    subsequent targets. Modifiers can affect this up to a maximum of 0.9. That value
    must not be exposed as a define.
NEW_ARMY_LEADER_LEVEL_CHANCES:
  def:
    - [0.95]  # 95% for level one
    - [0.05]  # 5% for level two
  type: table
  cmt: chances for new army leaders to start at a given level
```
