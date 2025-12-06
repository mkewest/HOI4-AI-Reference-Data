---
domain: defines_list
concept: NResistance
version: 1.14+
requires: [defines]
relates: [resistance, compliance]
---

```yaml
INITIAL_STATE_RESISTANCE:
  def: '1.0'
  type: float
  cmt: initial resistance percentage of a state once it is captured
COMPLIANCE_FACTOR_ON_STATE_CONTROLLER_CHANGE:
  def: '-0.5'
  type: float
  cmt: compliance factor that applies when the state controller changes (in between
    allies, compliance is zeroed if it is taken by original country)
RESISTANCE_TARGET_BASE:
  def: '35.0'
  type: float
  cmt: base resistance target percentage
RESISTANCE_TARGET_MODIFIER_PER_STABILITY_LOSS:
  def: '0.2'
  type: float
  cmt: resistance target modifier per stability below 100%
RESISTANCE_TARGET_MODIFIER_IS_AT_PEACE:
  def: '-10.0'
  type: float
  cmt: resistance target modifier when we are at peace
RESISTANCE_TARGET_MODIFIER_OCCUPIED_CAPITULATED:
  def: '10.0'
  type: float
  cmt: resistance target modifier when the enemy is capitulated
RESISTANCE_TARGET_MODIFIER_OCCUPIED_IS_EXILE_MAX:
  def: '20.0'
  type: float
RESISTANCE_TARGET_MODIFIER_POP_VERY_LOW:
  def: '-50.0'
  type: float
  cmt: resistance target modifier in % for states we have claim
RESISTANCE_POP_VERY_LOW_CUTOFF:
  def: '1000'
  type: int
RESISTANCE_DECAY_BASE:
  def: '0.1'
  type: float
  cmt: base resistance decay
RESISTANCE_DECAY_MAX:
  def: '100.0'
  type: float
  cmt: nax resistance decay
RESISTANCE_DECAY_MODIFIER_FACTORS:
  def: '{ 10, -50, 20, -25 }'
  type: array
  cmt: resistance decay modifier when resistance hits a certain percentage below 10%
    it has a -50% modifier on decay below 20% it has a -25% modifier on decay
RESISTANCE_GROWTH_BASE:
  def: '0.2'
  type: float
  cmt: base resistance grow
RESISTANCE_GROWTH_MAX:
  def: '100.0'
  type: float
  cmt: max resistance grow
COMPLIANCE_GROWTH_MIN:
  def: '-100.0'
  type: float
  cmt: min compliance grow
COMPLIANCE_GROWTH_IS_AT_PEACE:
  def: '10'
  type: int
  cmt: compliance growth buff at peace
COMPLIANCE_DECAY_AT_MAX_COMPLIANCE:
  def: '-0.083'
  type: float
  cmt: as compliance increases, it gets a decay rate depending on its value. compliance
    should stabilize at some value until its growth changes
RESISTANCE_RATIO_DIFF_TO_SPREAD:
  def: '0.5'
  type: float
  cmt: resistance diff between two neighbour states will spread by this ratio ( from
    highest resistance states to lower ones and it will only spread once to a state)
RESISTANCE_ACTIVITY_MIN_GARRISON_PENETRATE_CHANCE:
  def: '0.02'
  type: float
GARRISON_LOG_MAX_MONTHS:
  def: '12'
  type: int
GARRISON_MANPOWER_MIN_DELIVERY_SPEED:
  def: '0.7'
  type: float
  cmt: Minimum base delivery speed if the chunk can't be calculated.
GARRISON_EQUIPMENT_DELIVERY_SPEED:
  def: '4.0'
  type: float
  cmt: Modifier for garrison equipment reinforcement speed
GARRISON_STR_POW_EQUIPMENT:
  def: '3'
  type: int
  cmt: 'Scales impact of euqipment deficiency by raising that deficiency to the number
    here. Formula: efficiency = 1.0 - equipment_deficiency^GARRISON_STR_POW_EQUIPMENT'
SUPPRESSION_NEEDED_LOWER_CAP:
  def: '10.0'
  type: float
  cmt: if resistance is lower than this value then we always act as though it is at
    the define for the purpose of suppresion requirements
GARRISON_MANPOWER_LOST_BY_ATTACK:
  def: '0.016'
  type: float
  cmt: Ratio of manpower lost by garrison at each attack on garrison (this number
    will be reduced by the hardness of garrison template)
MAXIMUM_GARRISON_HARDNESS_WHEN_ATTACKED:
  def: '0.90'
  type: float
  cmt: Cap to be sure that garrison will suffer lost in attack, even with a almost
    100% hardness
MANPOWER_BUFFER_TO_NOT_GIVE_MINOR:
  def: '0.3'
  type: float
  cmt: To determine how much AI can give as foreign manpower, we calculate how much
    manpower we use, and add this buffer. The result is what we want to keep, for
    minor countries. So higher this number is, lower we will give Manpower.
MAX_GARRISON_RATIO_WE_AGREE_TO_SUPPORT:
  def: '3.0'
  type: float
  cmt: The part of the manpower needed by the foreign garrison, that AI will agree
    to support with our manpower. If negative number, AI will not take into consideration
    the need, and just calculate how much they can give.
INITIAL_HISTORY_RESISTANCE:
  def: '0.0'
  type: float
  cmt: resistance value for initial colony states
INITIAL_GARRISON_STRENGTH:
  def: '1'
  type: int
  cmt: garrison value for initial colony states
```
