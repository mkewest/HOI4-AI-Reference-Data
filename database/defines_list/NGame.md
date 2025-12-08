---
domain: defines_list
concept: NGame
version: 1.17.2
requires: [defines]
relates: [game_rules]
---

```yaml
START_DATE:
  def: '1936.1.1.12'
  type: string
END_DATE:
  def: '1949.1.1.1'
  type: string
MAP_SCALE_PIXEL_TO_KM:
  def: '7.114'
  type: float
  cmt: Yes, we did the math
SAVE_VERSION:
  def: '30'
  type: int
  cmt: 1.16.0 (Countenance)
MINOR_SAVE_VERSION:
  def: '1'
  type: int
  cmt: Minor save version is used to identifiy different backward compatible savegame
    versions
CHECKSUM_SALT:
  def: 'zwOdv5d9wm9uDSOT'
  type: string
  cmt: Data to modify generated checksum when game binaries have changed but not any
    content files.
LAG_DAYS_FOR_LOWER_SPEED:
  def: '10'
  type: int
  cmt: Days of client lag for decrease of gamespeed
LAG_DAYS_FOR_PAUSE:
  def: '25'
  type: int
  cmt: Days of client lag for pause of gamespeed.
GAME_SPEED_SECONDS:
  def:
    - [2.0, 0.5, 0.2, 0.1, 0.0]
  type: table
  cmt: game speeds for each level. Must be 5 entries with last one 0 for unbound
MAJOR_PARTICIPANTS_FOR_MAJOR_WAR:
  def: '3'
  type: int
  cmt: Minimum number of major countries involved in a war to consider it major enough
    to not end the game even though the enddate has been reached.
TRADE_ROUTE_RECALCULATE_FREQUENCY_DAYS:
  def: '45'
  type: int
  cmt: Max recalculation time for all trade routes (0 means we do not recalucate
    prediodically trade routes)
COMBAT_LOG_MAX_MONTHS:
  def: '12'
  type: int
MESSAGE_TIMEOUT_DAYS:
  def: '60'
  type: int
  cmt: Useful if running the handsoff game. The popup messages that doesn't require the
    player respond will automatically hide after some timeout.
INFO_MESSAGE_TIMEOUT_DAYS:
  def: '3'
  type: int
  cmt: Same but for unimportant messages.
AIR_LOG_TIMEOUT_HOURS:
  def: '24'
  type: int
  cmt: Data storring data
EVENT_TIMEOUT_DEFAULT:
  def: '13'
  type: int
  cmt: Default days before an event times out if not scripted
MISSION_REMOVE_FROM_INTERFACE_DEFAULT:
  def: '13'
  type: int
  cmt: Default days before a mission is removed from the interface after having failed
    or completed
DECISION_ALERT_TIMEOUT_DAYS:
  def: '30'
  type: int
  cmt: Days left when player will be alerted about timing out events or decisions
OIL_RESOURCE:
  def: 'oil'
  type: string
  cmt: Name of the oil resource
FUEL_RESOURCE:
  def: 'oil'
  type: string
  cmt: resource that will give country fuel
ENERGY_RESOURCE:
  def: 'coal'
  type: string
  cmt: resource that will give country energy
MAX_EFFECT_ITERATION:
  def: '1000'
  type: int
  cmt: maximum allowed iteration for loop effects
MAX_SCRIPTED_LOC_RECURSION:
  def: '30'
  type: int
  cmt: max recursion for scripted localizations
HANDS_OFF_START_TAG:
  def: 'HAI'
  type: string
  cmt: tag for player country for -hands_off runs. use an existing tag that is less
    likely to affect the game
ALERT_SFX_COOLDOWN_DAYS:
  def: '14'
  type: int
  cmt: After playing an alert sound, don't play the same sound for XXX days, even if it
    fires again.
MUSIC_PLAYER_RECENTLY_PLAYED_SIZE:
  def: '10'
  type: int
  cmt: The music player keeps track of recently played music to try and avoid playing
    the same songs too often. This determines the max number of songs in the recently
    played list.
```
