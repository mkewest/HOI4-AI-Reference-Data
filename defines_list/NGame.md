---
domain: defines_list
concept: NGame
version: 1.14+
requires: [defines]
relates: [game_rules]
---

```yaml
START_DATE:
  def: '"1936.1.1.12"'
  type: str
  use: Default start date, base for some durations (e.g. license costs, AI construction
    strategy)
END_DATE:
  def: '"1949.1.1.1"'
  type: str
  use: Decides on the date when the final scoreboard is shown, unless a sufficiently
    major war is ongoing
MAP_SCALE_PIXEL_TO_KM:
  def: '7.114'
  type: float
  cmt: Yes, we did the math
  use: Translates the pixel distances from world map bitmaps into distances in-game,
    such as for unit speed
SAVE_VERSION:
  def: '25'
  type: int
  cmt: 1.16.0 (Countenance)
  use: Compatibility version for save files
CHECKSUM_SALT:
  def: '"zwOdv5d9wm9uDSOT"'
  type: str
  cmt: Data to modify generated checksum when game binaries have changed but not any
    content files.
LAG_DAYS_FOR_PAUSE:
  def: '25'
  type: int
  cmt: Days of client lag for pause of gamespeed.
MAJOR_PARTICIPANTS_FOR_MAJOR_WAR:
  def: '3'
  type: int
  cmt: Minimum number of major countries involved in a war to consider it major enough
    to not end the game even though the enddate has been reached.
COMBAT_LOG_MAX_MONTHS:
  def: '12'
  type: int
  use: Non-air combat log data will be pruned after this duration
MESSAGE_TIMEOUT_DAYS:
  def: '60'
  type: int
  cmt: Useful if running the handsoff game. The popup messages that doesn't require
    the player respond will automatically hide after some timeout.
AIR_LOG_TIMEOUT_HOURS:
  def: '24'
  type: int
  cmt: Data storring data
  use: Air combat log data will be pruned after this duration
EVENT_TIMEOUT_DEFAULT:
  def: '13'
  type: int
  cmt: Default days before an event times out if not scripted
DECISION_ALERT_TIMEOUT_DAYS:
  def: '30'
  type: int
  cmt: Days left when player will be alerted about timing out events or decisions
MAX_EFFECT_ITERATION:
  def: '1000'
  type: int
  cmt: maximum allowed iteration for loop effects
HANDS_OFF_START_TAG:
  def: '"HAI"'
  type: str
  cmt: tag for player country for -hands_off runs. use an existing tag that is less
    likely to affect the game
MUSIC_PLAYER_RECENTLY_PLAYED_SIZE:
  def: '10'
  type: int
  cmt: The music player keeps track of recently played music to try and avoid playing
    the same songs too often. This determines the max number of songs in the recently
    played list.
```
