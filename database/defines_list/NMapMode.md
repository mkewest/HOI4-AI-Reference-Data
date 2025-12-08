---
domain: defines_list
concept: NMapMode
version: 1.17.2
requires: [defines]
relates: [map_mode]
---

```yaml
FABRICATE_CLAIM_SELECTED_SECONDARY_COLOR:
  def:
    - [0, 1, 0, 1]
  type: table
FABRICATE_CLAIM_TARGET_COUNTRY_SECONDARY_COLOR:
  def:
    - [0, 0, 0, 0]
  type: table
FABRICATE_CLAIM_NON_TARGET_COUNTRY_SECONDARY_COLOR:
  def:
    - [0, 0, 0, 0]
  type: table
FABRICATE_CLAIM_ALREADY_CLAIM_SECONDARY_COLOR:
  def:
    - [0.5, 0, 0, 1]
  type: table
FABRICATE_CLAIM_ALREADY_CORE_SECONDARY_COLOR:
  def:
    - [0.5, 0, 0, 1]
  type: table
CONSTRUCTION_MAP_MODE_BUILDING_DEFAULT_COLOR:
  def:
    - [0.43, 0.22, 0.22, 0.5]
  type: table
  cmt: Color of states/provinces that can't be built on
CONSTRUCTION_MAP_MODE_BUILDING_MAX_LEVEL_COLOR:
  def:
    - [0.05, 0.1, 0.7, 0.8]
  type: table
  cmt: Color of states/provinces where current building level is maxed out (max is
    current max level, not final max level) of a building type
CONSTRUCTION_MAP_MODE_BUILDING_LEVEL_LOW_COLOR:
  def:
    - [0.2, 0.7, 0.0, 0.1]
  type: table
CONSTRUCTION_MAP_MODE_BUILDING_LEVEL_HI_COLOR:
  def:
    - [0.4, 0.9, 0.0, 0.8]
  type: table
CONSTRUCTION_MAP_MODE_BUILDING_MAX_AMOUNT_QUEUED_COLOR:
  def:
    - [0.0, 0.0, 1.0]
  type: table
  cmt: Color of states/provinces when building queue is maxed of a building type
CONSTRUCTION_MAP_MODE_BUILDING_QUEUED_COLOR:
  def:
    - [1.0, 0.85, 0.0]
  type: table
  cmt: Color of states/provinces when building queue contains one or more of a building
    type.
MAP_MODE_MANPOWER_RANGE_MAX:
  def: '20000000'
  type: int
  cmt: When a state has that much manpower, it will be colored with the color
    MAP_MODE_MANPOWER_RANGE_COLOR_TO. Everything below that will have an interpolated
    color.
MAP_MODE_MANPOWER_RANGE_COLOR_FROM:
  def:
    - [0.2, 0.2, 0.7, 0.18]
  type: table
  cmt: Color range for manpower map mode.
MAP_MODE_MANPOWER_RANGE_COLOR_TO:
  def:
    - [1, 0.125, 0.0, 0.6]
  type: table
MAP_MODE_INFRA_RANGE_COLOR_FROM:
  def:
    - [1, 0.125, 0.0, 0.1]
  type: table
  cmt: Color range for infrastructure map mode.
MAP_MODE_INFRA_RANGE_COLOR_TO:
  def:
    - [0.1, 0.9, 0.1, 0.6]
  type: table
MAP_MODE_IDEOLOGY_COLOR_TRANSPARENCY:
  def: '1'
  type: int
  cmt: In the Ideology map mode, the colors on the map are taken from the scriptable
    file 00_ideologies.txt for each group. We use them in the interfaces (pie-charts)
    where transparency is not used, but 100% opaque looks bad on the map. This is a
    variable to control the transparency of the color.
CONSTRUCTION_MAP_MODE_TRANSPARENCY_OVERRIDE:
  def: '241'
  type: int
  cmt: When you use gradient borders to defeat the purpose of gradient borders. Larger
    than 248 seems to make the transparency stronger?
PEACE_CONFERENCE_CURRENT_SELECTED_SECONDARY_COLOR:
  def:
    - [0, 0, 1, 0.25]
  type: table
PEACE_CONFERENCE_SELECTABLE_SECONDARY_COLOR:
  def:
    - [0, 1, 0, 0.25]
  type: table
PEACE_CONFERENCE_CONTESTED_SECONDARY_COLOR:
  def:
    - [1, 0, 0, 0.25]
  type: table
PEACE_CONFERENCE_CHANGE_TARGET_TAG_SECONDARY_COLOR:
  def:
    - [0, 0.8, 0.5, 0.25]
  type: table
PEACE_CONFERENCE_DIFFERENT_STACKABLE_SECONDARY_COLOR:
  def:
    - [1, 1, 0, 0.25]
  type: table
FACTIONS_COLOR_NOT_MEMBER:
  def:
    - [0.6, 0.6, 0.6, 0.25]
  type: table
FACTIONS_MEMBER_TRANSPARENCY:
  def: '1.0'
  type: float
PLAYER_MAPMODE_NOT_SELECTED_COUNTRY_TRANSPARENCY:
  def: '0.15'
  type: float
  cmt: How much is the country colors faded out, for countries that are not occupied by
    the any player.
SELECTED_COUNTRY_HIGHLIGHT_THICKNESS_MULT:
  def: '1.5'
  type: float
  cmt: When a country is selected (blinking/highlighted) it's borders becomes a bit
    thicker, to make stand out even more. 1.0 is default thickness.
STRATEGIC_MODE_COUNTRY_COLOR_STRIPES_TRANSP:
  def: '0.0'
  type: float
STRATEGIC_MODE_ENEMY_STRIPES_COLOR:
  def:
    - [0.827, 0.172, 0.184, 0.0]
  type: table
STRATEGIC_MODE_OUR_STRIPES_COLOR:
  def:
    - [0.427, 0.619, 0.858, 0.0]
  type: table
STRATEGIC_MODE_ALLY_STRIPES_COLOR:
  def:
    - [0.427, 0.619, 0.858, 0.0]
  type: table
RADAR_RANGE_STRIPES_COLOR:
  def:
    - [1.0, 1.0, 0.0, 0.14]
  type: table
RADAR_RANGE_COLOR:
  def:
    - [0.039, 0.627, 0.0, 1.0]
  type: table
RADAR_RANGE_ALLIED_COLOR:
  def:
    - [0.0, 0.647, 1.0, 1.0]
  type: table
RADAR_RANGE_SELECTED_COLOR:
  def:
    - [1.0, 1.0, 0.0, 1.0]
  type: table
RADAR_ROTATION_SPEED:
  def: '0.025'
  type: float
AIR_RANGE_CAN_ASSIGN_MISSION_STRIPES_COLOR:
  def:
    - [0, 0.8, 0, 0.0]
  type: table
  cmt: Stripes over the regions indicating if the currently selected air wings can have
    assigned mission there or not.
AIR_RANGE_CANNOT_ASSIGN_MISSION_STRIPES_COLOR:
  def:
    - [0.8, 0, 0, 0.5]
  type: table
AIR_RANGE_INDICATOR_DEFAULT_COLOR:
  def:
    - [1.0, 1.0, 0, 1]
  type: table
  cmt: On map circle indicating the air wings range.
AIR_RANGE_INDICATOR_NO_WINGS_COLOR:
  def:
    - [1.0, 0, 0, 1]
  type: table
  cmt: Same as above, but for air wings with no airplanes.
AIR_RANGE_INDICATOR_ROTATION_SPEED:
  def: '0.001'
  type: float
  cmt: How quickly is that indicator rotating
AIR_MISSION_ARROW_ACTIVE_COLOR:
  def:
    - [0, 1.0, 0, 0.5]
  type: table
  cmt: Color of the arrow drawn in the strategic air map mode, between the air base and
    the region for the active missions
AIR_MISSION_ARROW_NONACTIVE_COLOR:
  def:
    - [1.0, 1.0, 1.0, 0.2]
  type: table
  cmt: Same as above, but for non active missions (when no air wing has any mission
    active)
AIR_MISSION_ARROW_SELECTED_COLOR:
  def:
    - [1.0, 1.0, 0, 0.8]
  type: table
  cmt: Same as above, but for currently selected air wings/air bases.
AIR_TRANSFER_ARROW_COLOR:
  def:
    - [1, 1, 0, 0.75]
  type: table
  cmt: Same as above, but for the arrows drawn between airbases for current transfers
NAVAL_REGION_ACCESS_AVOID_COLOR:
  def:
    - [1, 1, 0, 0.35]
  type: table
  cmt: Color for the map stripes on naval regions that has set an access level = AVOID
NAVAL_REGION_ACCESS_BLOCK_COLOR:
  def:
    - [1, 0, 0, 0.45]
  type: table
  cmt: Color for the map stripes on naval regions that has set an access level = BLOCK
NAVAL_REGION_FADE_WHEN_FLEET_SELECTED:
  def: '0.25'
  type: float
  cmt: How much all region borders (except those with mission assigned to it) are faded
    out, when a fleet is selected.
NAVAL_REGION_TRANSPARENCY_RATIO_MAX:
  def: '0.8'
  type: float
  cmt: Maximum transparency ratio for the strategic navy region map
NAVAL_REGION_TRANSPARENCY_RATIO_MIN:
  def: '0.5'
  type: float
  cmt: Minimum transparency ratio for the strategic navy region map
NAVAL_REGION_TRANSPARENCY_RANGE:
  def: '2000.0'
  type: float
  cmt: The range of naval dominance to be rendered on the strategic navy region map
NAVAL_DOMINANCE_TREND_BAR_HIDE_RATIO:
  def: '0.72'
  type: float
  cmt: Ratio of the camera height to the maximum camera height, below which the naval
    dominance trend bar is hidden.
AIR_REGION_FADE_WHEN_WING_SELECTED:
  def: '0.15'
  type: float
UI_CONFIGURABLE_SLOT_FROM:
  def: '4'
  type: int
  cmt: Mapmode slots range that may be configurable. Indices are 0-based (first slot is
    0)
UI_CONFIGURABLE_SLOT_TO:
  def: '10'
  type: int
MAP_MODE_TERRAIN_TRANSPARENCY:
  def: '0.5'
  type: float
  cmt: How much transparent are the province colors in the simplified terrain map mode
MAP_MODE_NAVAL_TERRAIN_TRANSPARENCY:
  def: '0.8'
  type: float
  cmt: How much transparent are the SEA province colors in the simplified terrain map
    mode
MAP_MODE_INTEL_NETWORK_STRENGTH_COLOR_LOW:
  def:
    - [0.1, 0.1, 0.5, 0.2]
  type: table
  cmt: Color of a state with the lowest intel network strength
MAP_MODE_INTEL_NETWORK_STRENGTH_COLOR_HIGH:
  def:
    - [0.4, 0.3, 0.9, 1.0]
  type: table
  cmt: Color of a state with the lowest intel network strength
MAP_MODE_INTEL_NETWORK_STRENGTH_QUIET_COLOR_LOW:
  def:
    - [0.1, 0.5, 0.1, 0.2]
  type: table
  cmt: Color of a state with the lowest intel network strength in a quiet network
MAP_MODE_INTEL_NETWORK_STRENGTH_QUIET_COLOR_HIGH:
  def:
    - [0.4, 0.9, 0.3, 1.0]
  type: table
  cmt: Color of a state with the highest possible intel network strength in a quiet
    network
MAP_MODE_INTEL_MAX_HORIZONTAL_STACK:
  def: '3'
  type: int
  cmt: How many intel icons can be shown before the More icon appears for Operations
RAILWAY_GUN_RANGE_INDICATOR_DEFAULT_COLOR:
  def:
    - [1.0, 1.0, 1.0, 1.0]
  type: table
  cmt: On map circle indicating the railway gun bombardment range.
RAILWAY_GUN_RANGE_INDICATOR_ROTATION_SPEED:
  def: '0.001'
  type: float
  cmt: How fast the indicator is rotating.
RAILWAY_GUN_RANGE_STRIPES_COLOR:
  def:
    - [1.0, 0.5, 0.0, 0.2]
  type: table
  cmt: Color of the railway gun range stripes (when hovered)
PREPARING_RAID_ARROW_COLOR:
  def:
    - [0.7, 0.7, 0.7, 1.0]
  type: table
  cmt: Color of the arrow drawn in the raid map mode for raids that are still preparing.
READY_RAID_ARROW_COLOR:
  def:
    - [0.7, 0.7, 0, 0.9]
  type: table
  cmt: Color of the arrow drawn in the raid map mode for raids that can be launched.
ACTIVE_RAID_ARROW_COLOR:
  def:
    - [1, 0, 0, 0.9]
  type: table
  cmt: Color of the arrow drawn in the raid map mode for active raids.
OCCUPATION_MAP_MODE_COUNTRY_STRIPE_ALPHA:
  def: '0.3'
  type: float
  cmt: alpha of occupied country stripes in occupation map mode
OPERATIVE_MAP_MODE_INVALID_COUNTRY_TARGET_TRANSPARENCY:
  def: '0.15'
  type: float
  cmt: alpha of country which cannot be targeted by the selected operative mission
COASTAL_FACILITY_OFFSET:
  def:
    - [-1.5, 0, 1.5]
  type: table
  cmt: Offset from world position CVector3f (x, y, z). So it does not overlap with a
    port map icon or naval headquarter
NAVAL_HEADQUARTER_OFFSET:
  def:
    - [1.5, 0, 1.5]
  type: table
  cmt: Offset from world position CVector3f (x, y, z). So it does not overlap with a
    port map icon or facility
SUPPLY_MAP_MODE_COUNTRY_BORDER_CAMERA_DISTANCE:
  def: '1.0'
  type: float
SUPPLY_MAP_MODE_COUNTRY_BORDER_OUTLINE_CUTOFF:
  def: '0.973'
  type: float
GRADIENT_BORDERS_THICKNESS_SUPPLY_COUNTRY_BORDER:
  def: '10.0'
  type: float
SUPPLY_COUNTRY_BORDER_PLAYER_COLOR:
  def:
    - [0.1, 0.66, 0.1, 1.0]
  type: table
SUPPLY_COUNTRY_BORDER_FRIEND_COLOR:
  def:
    - [0.035, 0.426, 0.91, 1.0]
  type: table
SUPPLY_COUNTRY_BORDER_ACCESS_COLOR:
  def:
    - [0.1, 0.66, 0.1, 1.0]
  type: table
SUPPLY_MAP_MODE_REACH_COLOR:
  def:
    - [0.0, 0.6, 0.0, 0.4, 1.0]  # #990066 dark purple
    - [0.02, 0.2, 0.17, 0.52, 1.0]  # #332B85 dark purple blue
    - [0.12, 0.04, 0.17, 0.60, 1.0]  # #0A2B99 dark blue
    - [0.2, 0.13, 0.36, 0.65, 1.0]  # #215CA6 blue
    - [0.4, 0.11, 0.56, 0.75, 1.0]  # #1C8FBF light blue
    - [0.6, 0.25, 0.71, 0.76, 1.0]  # #40B5C2 teal
    - [0.8, 0.47, 0.8, 0.73, 1.0]  # #78CCBA light teal
    - [1.0, 0.6, 0.82, 0.6, 1.0]  # #99D199 light green
  type: table
  cmt: (last shown when supply flow is >= SUPPLY_MAP_MODE_BEST_FLOW_DISPLAY)
SUPPLY_MAP_MODE_BEST_FLOW_DISPLAY:
  def: '12'
  type: int
  cmt: Which supply cap availibility corresponds to best heatmap color
SUPPLY_MAP_MODE_STATUS_COLOR:
  def:
    - [0.0, 0.9, 0.0, 0.0, 1.0]  # #E60000 red
    - [0.7, 0.98, 0.4, 0.1, 1.0]  # #FA661A orange
    - [1.0, 0.8, 0.64, 0.2, 1.0]  # #CCA333 mustard
  type: table
SUPPLY_STATUS_DISPLAY_THRESHOLD:
  def: '0.90'
  type: float
  cmt: at what average supply status we move to show status colors instead of flow
SUPPLY_HOVERED_STATE_COLOR_INDEX:
  def: '0'
  type: int
  cmt: Border color of hovered state. Refers to the colors in
    BORDER_COLOR_CUSTOM_HIGHLIGHTS.
SUPPLY_HOVERED_PROVINCE_COLOR_INDEX:
  def: '4'
  type: int
  cmt: Border color of hovered province. Refers to the colors in
    BORDER_COLOR_CUSTOM_HIGHLIGHTS.
PEACE_HOVERED_STATE_COLOR_INDEX:
  def: '3'
  type: int
  cmt: Border color of hovered state in Peace conference. Refers to the colors in
    BORDER_COLOR_CUSTOM_HIGHLIGHTS.
PEACE_CLAIMED_STATE_COLOR_INDEX:
  def: '2'
  type: int
  cmt: Border color of claimed states in Peace conference. Refers to the colors in
    BORDER_COLOR_CUSTOM_HIGHLIGHTS.
SELECTION_HOVERED_STATE_COLOR_INDEX_CONTROLLED:
  def: '5'
  type: int
  cmt: Border color of hovered controlled states in various select mapmodes. Refers to
    the colors in BORDER_COLOR_CUSTOM_HIGHLIGHTS.
SELECTION_HOVERED_STATE_COLOR_INDEX_FOREIGN:
  def: '6'
  type: int
  cmt: Border color of hovered foreign states in various select mapmodes. Refers to the
    colors in BORDER_COLOR_CUSTOM_HIGHLIGHTS.
CONSTRUCTION_PRIMARY_VALID_BUILD_TARGET_PROVINCE_COLOR_INDEX:
  def: '7'
  type: int
CONSTRUCTION_PRIMARY_INVALID_BUILD_TARGET_PROVINCE_COLOR_INDEX:
  def: '8'
  type: int
CONSTRUCTION_PRIMARY_FOREIGN_BUILD_TARGET_PROVINCE_COLOR_INDEX:
  def: '9'
  type: int
CONSTRUCTION_SECONDARY_VALID_BUILD_TARGET_PROVINCE_COLOR_INDEX:
  def: '10'
  type: int
CONSTRUCTION_SECONDARY_INVALID_BUILD_TARGET_PROVINCE_COLOR_INDEX:
  def: '11'
  type: int
CONSTRUCTION_SECONDARY_FOREIGN_BUILD_TARGET_PROVINCE_COLOR_INDEX:
  def: '12'
  type: int
FACTION_THEATER_COLOR_INDEX:
  def: '13'
  type: int
  cmt: Border color when editing a faction theater (index in
    BORDER_COLOR_CUSTOM_HIGHLIGHTS)
FACTION_THEATER_HIGHLIGHT_COLOR_INDEX:
  def: '14'
  type: int
  cmt: Border color when hovering a faction theater map icon (index in
    BORDER_COLOR_CUSTOM_HIGHLIGHTS)
```
