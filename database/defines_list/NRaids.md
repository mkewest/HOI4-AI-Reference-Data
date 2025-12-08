---
domain: defines_list
concept: NRaids
version: 1.17.2
requires: [defines]
relates: []
---

```yaml
BASE_DAYS_TO_PREPARE:
  def: '7'
  type: int
  cmt: Base number of days required to complete raid preparation phase
MAX_STATE_TARGETS_TO_EVALUATE_PER_HOUR:
  def: '50'
  type: int
  cmt: PERFORMANCE (HOURLY TICK) : higher number = faster state target re-evaulation +
    lower performance
RAID_TARGET_ITEM_POOL_SIZE:
  def: '512'
  type: int
  cmt: PERFORMANCE (UI) : number of entries to reserve in the raid target item pool
RAID_TYPE_ICON_ITEM_POOL_SIZE:
  def: '512'
  type: int
  cmt: PERFORMANCE (UI) : number of entries to reserve in the raid type icon item pool
RAID_LOW_RISK_SETTING_DISASTER_MODIFIER:
  def: '0'
  type: int
  cmt: How much the disaster risk is modified when the dial is set to "low"
RAID_MEDIUM_RISK_SETTING_DISASTER_MODIFIER:
  def: '0.1'
  type: float
  cmt: How much the disaster risk is modified when the dial is set to "medium"
RAID_HIGH_RISK_SETTING_DISASTER_MODIFIER:
  def: '0.25'
  type: float
  cmt: How much the disaster risk is modified when the dial is set to "high"
RAID_SUCCESS_MODIFIER_THRESHOLD_BAD:
  def: '-10.0'
  type: float
  cmt: If a success chance modifier is below this value, it will be displayed in red
RAID_SUCCESS_MODIFIER_THRESHOLD_NEUTRAL:
  def: '0.0'
  type: float
  cmt: If a success chance modifier is below this value, it will be displayed in yellow
MAX_DETECTED_TARGETS_PER_HOUR:
  def: '1'
  type: int
  cmt: PERFORMANCE (HOURLY TICK) : max number of targets to be detected per hour, NOTE :
    keep this low because detection is checked against every country!
RAID_DEFAULT_TARGET_COOLDOWN_DAYS:
  def: '365'
  type: int
  cmt: The default cooldown (in days) for raiding the same target, can be overriden for
    specific raid types through script
RAID_UNIT_SPEED_MULTIPLIER:
  def: '0.1'
  type: float
  cmt: Global speed control
BASE_NAVAL_COMMANDO_RAID_DISTANCE:
  def: '1500'
  type: int
  cmt: Max distance in kilometers
RAID_LOW_RISK_SETTING_SUCCESS_MODIFIER:
  def: '0.0'
  type: float
  cmt: How much the success chance is modified when the dial is set to "low"
RAID_MEDIUM_RISK_SETTING_SUCCESS_MODIFIER:
  def: '0.1'
  type: float
  cmt: How much the success chance is modified when the dial is set to "low"
RAID_HIGH_RISK_SETTING_SUCCESS_MODIFIER:
  def: '0.25'
  type: float
  cmt: How much the success chance is modified when the dial is set to "low"
TARGET_DETECTION_INTEL_TRESHOLD:
  def: '20.0'
  type: float
  cmt: How much intel is needed for a target to be detected?
TARGET_INTEL_PER_CIVILIAN_INTEL_OVER_COUNTRY:
  def: '0.5'
  type: float
  cmt: Intel level over target country is scaled by this value
TARGET_INTEL_PER_ARMY_INTEL_OVER_COUNTRY:
  def: '0.5'
  type: float
  cmt: Intel level over target country is scaled by this value
TARGET_INTEL_PER_NAVY_INTEL_OVER_COUNTRY:
  def: '0.5'
  type: float
  cmt: Intel level over target country is scaled by this value
TARGET_INTEL_PER_AIRFORCE_INTEL_OVER_COUNTRY:
  def: '0.5'
  type: float
  cmt: Intel level over target country is scaled by this value
TARGET_INTEL_PER_NETWORK_STRENGTH:
  def: '0.5'
  type: float
  cmt: Intel network strength in target state is scaled by this value
TARGET_INTEL_FROM_CONTROLLED_NEIGHBOUR_STATES:
  def: '15.0'
  type: float
  cmt: Flat bonus for having control over at least one neighbour state
TARGET_INTEL_PER_AIR_SUPERIORITY:
  def: '0.5'
  type: float
  cmt: Air superiority over target region is scaled by this value
TARGET_INTEL_FROM_DECRYPTION:
  def: '25.0'
  type: float
  cmt: Flat bonus for having fully decrypted their ciphers
TARGET_INTEL_PENALTY_PER_ENEMY_COUNTER_INTEL:
  def: '5.0'
  type: float
  cmt: Enemy counter intel is scaled by this value
RAID_OUTCOME_REPORT_DAYS_TO_LIVE:
  def: '30'
  type: int
  cmt: How many days after a raid has ended will the raid outcome report be visible on
    the map before being automatically dismissed
NUCLEAR_BOMB_PRODUCTION_SCALE:
  def: '2555.0'
  type: float
  cmt: +1 nuclear_production gives 1 nuke per 7 years
THERMONUCLEAR_BOMB_PRODUCTION_SCALE:
  def: '2555.0'
  type: float
  cmt: +1 nuclear_production gives 1 nuke per 7 years
NUCLEAR_BOMB_MIN_DAMAGE_PERCENT:
  def: '0.1'
  type: float
  cmt: Minimum damage from nukes as a percentage of current strength/organisation
NUCLEAR_BOMB_MAX_DAMAGE_PERCENT:
  def: '0.9'
  type: float
  cmt: Minimum damage from nukes as a percentage of current strength/organisation
THERMONUCLEAR_BOMB_MIN_DAMAGE_PERCENT:
  def: '0.6'
  type: float
  cmt: Minimum damage from nukes as a percentage of current strength/organisation
THERMONUCLEAR_BOMB_MAX_DAMAGE_PERCENT:
  def: '0.9'
  type: float
  cmt: Minimum damage from nukes as a percentage of current strength/organisation
NUCLEAR_RAID_CATEGORY_NAME:
  def: 'nuclear_raids'
  type: string
  cmt: The raid category to activate when clicking on the "nuclear" mission button for a
    rocket
ARMY_TRANSFER_MOVE_SAFELY:
  def: 'true'
  type: bool
  cmt: Whether to move safely when transferring divisions to the raid source
ARMY_TRANSFER_AVOID_ENEMY:
  def: 'true'
  type: bool
  cmt: Whether to avoid enemy when transferring divisions to the raid source
MAX_TARGETS_TO_UPDATE_PER_FRAME:
  def: '100'
  type: int
  cmt: PERFORMANCE (FRAME) : max raid targets to evaluate per frame (affects raid map
    icon refresh rate)
```
