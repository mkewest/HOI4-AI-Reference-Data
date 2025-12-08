---
domain: defines_list
concept: NResistance
version: 1.17.2
requires: [defines]
relates: [resistance, compliance]
---

```yaml
INITIAL_STATE_RESISTANCE:
  def: '1.0'
  type: float
  cmt: initial resistance percentage of a state once it is captured
INITIAL_STATE_COMPLIANCE:
  def: '0.0'
  type: float
  cmt: initial compliance percentage of a state once it is captured
COMPLIANCE_FACTOR_ON_STATE_CONTROLLER_CHANGE:
  def: '-0.5'
  type: float
  cmt: compliance factor that applies when the state controller changes (in between
    allies, compliance is zeroed if it is taken by original country)
RESISTANCE_COOLDOWN_WHEN_DISABLED:
  def: '-0.25'
  type: float
  cmt: resistance cooldown when the state is taken back by its original owner
    (compliance is zeroed in that case)
RESISTANCE_TARGET_BASE:
  def: '35.0'
  type: float
  cmt: base resistance target percentage
RESISTANCE_TARGET_MODIFIER_HAS_CLAIM:
  def: '-5.0'
  type: float
  cmt: resistance target modifier in % for states we have claim
RESISTANCE_TARGET_MODIFIER_PER_STABILITY_LOSS:
  def: '0.2'
  type: float
  cmt: resistance target modifier per stability below 100%
RESISTANCE_TARGET_MODIFIER_PER_COMPLIANCE:
  def: '-0.5'
  type: float
  cmt: resistance target modifier per compliance %
RESISTANCE_TARGET_MODIFIER_IS_AT_PEACE:
  def: '-10.0'
  type: float
  cmt: resistance target modifier when we are at peace
RESISTANCE_TARGET_MODIFIER_STATE_VP:
  def:
    - [0, 0.0]  # 0 - 5
    - [5, 5.0]  # 5 - 20
    - [20, 10.0]  # 20 - 50
    - [50, 20.0]  # 50 - ...
  type: table
  cmt: resistance target modifier pairs for vp. first entry is total vp in state and
    second entry is amount of target modifier that applies for that threshold
RESISTANCE_TARGET_MODIFIER_OCCUPIED_CAPITULATED:
  def: '10.0'
  type: float
  cmt: resistance target modifier when the enemy is capitulated
RESISTANCE_TARGET_MODIFIER_OCCUPIED_IS_EXILE_MIN:
  def: '2.0'
  type: float
  cmt: min & max resistance target modifier resistance target modifier for exile
    countries. interpolated using legitimacy
RESISTANCE_TARGET_MODIFIER_OCCUPIED_IS_EXILE_MAX:
  def: '20.0'
  type: float
RESISTANCE_TARGET_MODIFIER_POP_LOW:
  def: '-20.0'
  type: float
  cmt: how much we reduce the resistance target
RESISTANCE_TARGET_MODIFIER_POP_VERY_LOW:
  def: '-50.0'
  type: float
  cmt: resistance target modifier in % for states we have claim
RESISTANCE_POP_LOW_CUTOFF:
  def: '10000'
  type: int
RESISTANCE_POP_VERY_LOW_CUTOFF:
  def: '1000'
  type: int
RESISTANCE_TARGET_MIN_CAP_FOR_NON_COMPLIANCE:
  def: '10'
  type: int
  cmt: min resistance target will be capped to this percentage for non-compliance
    sources
RESISTANCE_DECAY_BASE:
  def: '0.1'
  type: float
  cmt: base resistance decay
RESISTANCE_DECAY_MIN:
  def: '0.01'
  type: float
  cmt: min resistance decay
RESISTANCE_DECAY_MAX:
  def: '100.0'
  type: float
  cmt: nax resistance decay
RESISTANCE_DECAY_MODIFIER_HAS_CLAIM:
  def: '25.0'
  type: float
  cmt: resistance decay modifier for our claims
RESISTANCE_DECAY_MODIFIER_FACTORS:
  def:
    - [10, -50]  # below 10% it has a -50% modifier on decay
    - [20, -25]  # below 20% it has a -25% modifier on decay
  type: table
  cmt: resistance decay modifier when resistance hits a certain percentage
MIN_DAMAGE_TO_GARRISONS_MODIFIER:
  def: '0.1'
  type: float
  cmt: modifier that applies to losses from resistance attack to garrisons at most can
    be reduced to this amount
RESISTANCE_GROWTH_BASE:
  def: '0.2'
  type: float
  cmt: base resistance grow
RESISTANCE_GROWTH_MIN:
  def: '0.01'
  type: float
  cmt: min resistance grow
RESISTANCE_GROWTH_MAX:
  def: '100.0'
  type: float
  cmt: max resistance grow
COMPLIANCE_GROWTH_BASE:
  def: '0.075'
  type: float
  cmt: base compliance grow
COMPLIANCE_GROWTH_MIN:
  def: '-100.0'
  type: float
  cmt: min compliance grow
COMPLIANCE_GROWTH_MAX:
  def: '100.0'
  type: float
  cmt: max compliance grow
COMPLIANCE_GROWTH_IS_AT_PEACE:
  def: '10'
  type: int
  cmt: compliance growth buff at peace
COMPLIANCE_GROWTH_HAS_CLAIM:
  def: '5'
  type: int
  cmt: compliance growth buff if state has a claim
COMPLIANCE_DECAY_AT_MAX_COMPLIANCE:
  def: '-0.083'
  type: float
  cmt: as compliance increases, it gets a decay rate depending on its value. compliance
    should stabilize at some value until its growth changes
COMPLIANCE_DECAY_PER_EXILE_LEGITIMACY:
  def: '-0.015'
  type: float
  cmt: higher legitimacy will give higher decay to compliance
RESISTANCE_RATIO_DIFF_TO_SPREAD:
  def: '0.5'
  type: float
  cmt: resistance diff between two neighbour states will spread by this ratio ( from
    highest resistance states to lower ones and it will only spread once to a state)
RESISTANCE_ACTIVITY_CHANCE_AT_MAX_RESISTANCE:
  def: '0.312'
  type: float
RESISTANCE_ACTIVITY_MIN_GARRISON_PENETRATE_CHANCE:
  def: '0.02'
  type: float
RESISTANCE_TARGET_TO_REENABLE_RESISTANCE:
  def: '10'
  type: int
  cmt: resistance will be disabled once it reaches zero and will not be reenabled until
    resistance target reaches above this value
GARRISON_LOG_MAX_MONTHS:
  def: '12'
  type: int
NO_COMPLIANCE_GAIN_ENABLE_LIMIT:
  def: '0.5'
  type: float
  cmt: at least this ratio of no garrison law should be active in order to no compliance
    gain to take effect
GARRISON_MANPOWER_MIN_DELIVERY_SPEED:
  def: '0.7'
  type: float
  cmt: Minimum base delivery speed if the chunk can't be calculated.
GARRISON_MANPOWER_REINFORCEMENT_SPEED:
  def: '2000.0'
  type: float
  cmt: Modifier for garrison manpower reinforcement.  This value is the maximum to be
    delivered which is then modified by distance
GARRISON_EQUIPMENT_DELIVERY_SPEED:
  def: '4.0'
  type: float
  cmt: Modifier for garrison equipment reinforcement speed
GARRISON_STR_POW_MANPOWER:
  def: '2'
  type: int
  cmt: Scales impact of manpower deficiency by raising that deficiency to the number
    here. Formula: efficiency = 1.0 - manpower_deficiency^GARRISON_STR_POW_MANPOWER
GARRISON_STR_POW_EQUIPMENT:
  def: '3'
  type: int
  cmt: Scales impact of euqipment deficiency by raising that deficiency to the number
    here. Formula: efficiency = 1.0 - equipment_deficiency^GARRISON_STR_POW_EQUIPMENT
SUPPRESSION_NEEDED_BY_RESISTANCE_POINT:
  def: '0.75'
  type: float
  cmt: Number of suppression point we need for each 1% of resistance
SUPPRESSION_NEEDED_LOWER_CAP:
  def: '10.0'
  type: float
  cmt: if resistance is lower than this value then we always act as though it is at the
    define for the purpose of suppresion requirements
SUPPRESSION_NEEDED_UPPER_CAP:
  def: '50.0'
  type: float
  cmt: if resistance is greater than this value then we always act as though it is at
    the define for the purpose of suppresion requirements
GARRISON_MANPOWER_LOST_BY_ATTACK:
  def: '0.016'
  type: float
  cmt: Ratio of manpower lost by garrison at each attack on garrison (this number will
    be reduced by the hardness of garrison template)
GARRISON_EQUIPMENT_LOST_BY_ATTACK:
  def: '0.02'
  type: float
  cmt: Ratio of equipment lost by garrison at each attack on garrison (this number will
    be reduced by the hardness of garrison template)
MAXIMUM_GARRISON_HARDNESS_WHEN_ATTACKED:
  def: '0.90'
  type: float
  cmt: Cap to be sure that garrison will suffer lost in attack, even with a almost 100%
    hardness
FOREIGN_MANPOWER_MIN_THRESHOLD:
  def: '5000'
  type: int
  cmt: The minimum number of Manpower that AI will accept to give at once, in order to
    avoid many weird little transfer.
MANPOWER_BUFFER_TO_NOT_GIVE_MINOR:
  def: '0.3'
  type: float
  cmt: To determine how much AI can give as foreign manpower, we calculate how much
    manpower we use, and add this buffer. The result is what we want to keep, for minor
    countries. So higher this number is, lower we will give Manpower.
MANPOWER_BUFFER_TO_NOT_GIVE_MAJOR:
  def: '0.6'
  type: float
  cmt: To determine how much AI can give as foreign manpower, we calculate how much
    manpower we use, and add this buffer. The result is what we want to keep, for major
    countries. So higher this number is, lower we will give Manpower.
MAX_GARRISON_RATIO_WE_AGREE_TO_SUPPORT:
  def: '3.0'
  type: float
  cmt: The part of the manpower needed by the foreign garrison, that AI will agree to
    support with our manpower. If negative number, AI will not take into consideration
    the need, and just calculate how much they can give.
FOREIGN_MANPOWER_AI_COOLDOWN_DAYS:
  def: '30'
  type: int
  cmt: Number of days after an AI give us manpower before the AI accept to give more.
INITIAL_HISTORY_RESISTANCE:
  def: '0.0'
  type: float
  cmt: resistance value for initial colony states
INITIAL_HISTORY_COMPLIANCE:
  def: '70.0'
  type: float
  cmt: compliance value for initial colony states
INITIAL_GARRISON_STRENGTH:
  def: '1'
  type: int
  cmt: garrison value for initial colony states
STATE_COMPLIANCE_DECAY_FOR_LOST_STATES:
  def: '0.05'
  type: float
  cmt: daily compliance decay for the states you lost control of
```
