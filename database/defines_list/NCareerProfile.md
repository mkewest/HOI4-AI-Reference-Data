---
domain: defines_list
concept: NCareerProfile
version: 1.17.2
requires: [defines]
relates: [career_profile]
---

```yaml
MOD_STATISTICS_GROUP:
  def: '""'
  type: str
  cmt: Mod defines Can be set by mods to collect statistics in a separate data set
    for the mod. Will also be used as the display name if MOD_STATISTICS_GROUP_NAME
    is not set.
NAVAL_INVASION_MEDAL_MAX_DURATION:
  def: '96'
  type: int
  cmt: Statistics parameters Maximum duration in hours to finish naval invasion and
    get a Naval Invasion Medal
NAVAL_INVASION_MEDAL_DIVISION_MIN_BATTALION_COUNT:
  def: '5'
  type: int
  cmt: Minimum count of battalions in the division required to count that division
    for Naval Invasion Medal
LORD_OF_THE_SEAS_MEDAL_MIN_SUPREMACY:
  def: '0.75'
  type: float
  cmt: Minimum supremacy to count current naval region for Lord of the Seas Medal
ORCHESTRA_OF_BOOM_RIBBON_SPECIAL_BATTALION_COUNT:
  def: '4'
  type: int
  cmt: Amount of special battalion types(anti-air, anti-tank, artillery and rocket
    artillery) required for the division for Orchestra of Boom Ribbon
BLITZ_THIS_TACTIC_NAME:
  def: '"tactic_elastic_defense"'
  type: str
  cmt: The tactic required to be applied to a leader or a country for Blitz This Ribbon
ENGINEERING_BEHEMOTH_MEDAL_ARMOR_RATING_SILVER:
  def: '160'
  type: int
  cmt: The armor rating required for the tanks to get the Engineering The Behemoth
    Silver Medal
CASTLES_IN_THE_AIR_MEDAL_AIR_DEFENSE_BRONZE:
  def: '20'
  type: int
  cmt: The air defense required for the airplanes to get the Castles in the Air Bronze
    Medal
CASTLES_IN_THE_AIR_MEDAL_AIR_DEFENSE_GOLD:
  def: '100'
  type: int
  cmt: The air defense required for the airplanes to get the Castles in the Air Gold
    Medal
```
