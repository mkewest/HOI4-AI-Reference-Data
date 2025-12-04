```yaml
FABRICATE_CLAIM_SELECTED_SECONDARY_COLOR:
  def: '{ 0, 1, 0, 1 }'
  type: array
FABRICATE_CLAIM_NON_TARGET_COUNTRY_SECONDARY_COLOR:
  def: '{ 0, 0, 0, 0 }'
  type: array
FABRICATE_CLAIM_ALREADY_CORE_SECONDARY_COLOR:
  def: '{ 0.5, 0, 0, 1 }'
  type: array
CONSTRUCTION_MAP_MODE_BUILDING_MAX_LEVEL_COLOR:
  def: '{ 0.05, 0.1, 0.7, 0.4 }'
  type: array
  cmt: Color of states/provinces where current building level is maxed out (max is
    current max level, not final max level) of a building type
CONSTRUCTION_MAP_MODE_BUILDING_LEVEL_HI_COLOR:
  def: '{ 0.4, 0.9, 0.0, 0.5 }'
  type: array
CONSTRUCTION_MAP_MODE_BUILDING_QUEUED_COLOR:
  def: '{ 1.0, 0.85, 0.0 }'
  type: array
  cmt: Color of states/provinces when building queue contains one or more of a building
    type.
MAP_MODE_MANPOWER_RANGE_COLOR_FROM:
  def: '{ 0.2, 0.2, 0.7, 0.18 }'
  type: array
  cmt: Color range for manpower map mode.
MAP_MODE_INFRA_RANGE_COLOR_FROM:
  def: '{ 1, 0.125, 0.0, 0.1 }'
  type: array
  cmt: Color range for infrastructure map mode.
MAP_MODE_IDEOLOGY_COLOR_TRANSPARENCY:
  def: '1'
  type: int
  cmt: In the Ideology map mode, the colors on the map are taken from the scriptable
    file 00_ideologies.txt for each group. We use them in the interfaces (pie-charts)
    where transparency is not used, but 100% opaque looks bad on the map. This is
    a variable to control the transparency of the color.
PEACE_CONFERENCE_CURRENT_SELECTED_SECONDARY_COLOR:
  def: '{ 0, 0, 1, 0.25 }'
  type: array
PEACE_CONFERENCE_CONTESTED_SECONDARY_COLOR:
  def: '{ 1, 0, 0, 0.25 }'
  type: array
PEACE_CONFERENCE_DIFFERENT_STACKABLE_SECONDARY_COLOR:
  def: '{ 1, 1, 0, 0.25 }'
  type: array
FACTIONS_MEMBER_TRANSPARENCY:
  def: '1.0'
  type: float
SELECTED_COUNTRY_HIGHLIGHT_THICKNESS_MULT:
  def: '1.5'
  type: float
  cmt: When a country is selected (blinking/highlighted) it's borders becomes a bit
    thicker, to make stand out even more. 1.0 is default thickness.
STRATEGIC_MODE_ENEMY_STRIPES_COLOR:
  def: '{ 0.827, 0.172, 0.184, 0.0 }'
  type: array
STRATEGIC_MODE_ALLY_STRIPES_COLOR:
  def: '{ 0.427, 0.619, 0.858, 0.0 }'
  type: array
RADAR_RANGE_COLOR:
  def: '{ 0.039, 0.627, 0.0, 1.0 }'
  type: array
RADAR_RANGE_SELECTED_COLOR:
  def: '{ 1.0, 1.0, 0.0, 1.0 }'
  type: array
AIR_RANGE_CAN_ASSIGN_MISSION_STRIPES_COLOR:
  def: '{ 0, 0.8, 0, 0.0 }'
  type: array
  cmt: Stripes over the regions indicating if the currently selected air wings can
    have assigned mission there or not.
AIR_RANGE_INDICATOR_DEFAULT_COLOR:
  def: '{ 1.0, 1.0, 0, 1 }'
  type: array
  cmt: On map circle indicating the air wings range.
AIR_RANGE_INDICATOR_ROTATION_SPEED:
  def: '0.001'
  type: float
  cmt: How quickly is that indicator rotating
AIR_MISSION_ARROW_NONACTIVE_COLOR:
  def: '{ 1.0, 1.0, 1.0, 0.2 }'
  type: array
  cmt: Same as above, but for non active missions (when no air wing has any mission
    active)
AIR_TRANSFER_ARROW_COLOR:
  def: '{ 1, 1, 0, 0.75 }'
  type: array
  cmt: Same as above, but for the arrows drawn between airbases for current transfers
NAVAL_REGION_ACCESS_BLOCK_COLOR:
  def: '{ 1, 0, 0, 0.45 }'
  type: array
  cmt: Color for the map stripes on naval regions that has set an access level = BLOCK
AIR_REGION_FADE_WHEN_WING_SELECTED:
  def: '0.15'
  type: float
UI_CONFIGURABLE_SLOT_TO:
  def: '10'
  type: int
MAP_MODE_NAVAL_TERRAIN_TRANSPARENCY:
  def: '0.8'
  type: float
  cmt: How much transparent are the SEA province colors in the simplified terrain
    map mode
MAP_MODE_INTEL_NETWORK_STRENGTH_COLOR_HIGH:
  def: '{ 0.4, 0.3, 0.9, 1.0 }'
  type: array
  cmt: Color of a state with the lowest intel network strength
MAP_MODE_INTEL_NETWORK_STRENGTH_QUIET_COLOR_HIGH:
  def: '{ 0.4, 0.9, 0.3, 1.0 }'
  type: array
  cmt: Color of a state with the highest possible intel network strength in a quiet
    network
RAILWAY_GUN_RANGE_INDICATOR_DEFAULT_COLOR:
  def: '{ 1.0, 1.0, 1.0, 1.0 }'
  type: array
  cmt: On map circle indicating the railway gun bombardment range.
RAILWAY_GUN_RANGE_STRIPES_COLOR:
  def: '{ 1.0, 0.5, 0.0, 0.2 }'
  type: array
  cmt: Color of the railway gun range stripes (when hovered)
OPERATIVE_MAP_MODE_INVALID_COUNTRY_TARGET_TRANSPARENCY:
  def: '0.15'
  type: float
  cmt: alpha of country which cannot be targeted by the selected operative mission
SUPPLY_MAP_MODE_COUNTRY_BORDER_OUTLINE_CUTOFF:
  def: '0.973'
  type: float
SUPPLY_COUNTRY_BORDER_PLAYER_COLOR:
  def: '{ 0.1, 0.66, 0.1, 1.0 }'
  type: array
SUPPLY_COUNTRY_BORDER_ACCESS_COLOR:
  def: '{ 0.1, 0.66, 0.1, 1.0 }'
  type: array
SUPPLY_MAP_MODE_BEST_FLOW_DISPLAY:
  def: '12'
  type: int
  cmt: Which supply cap availibility corresponds to best heatmap color
SUPPLY_STATUS_DISPLAY_THRESHOLD:
  def: '0.9'
  type: float
  cmt: at what average supply status we move to show status colors instead of flow
SUPPLY_HOVERED_PROVINCE_COLOR_INDEX:
  def: '4'
  type: int
  cmt: Border color of hovered province. Refers to the colors in BORDER_COLOR_CUSTOM_HIGHLIGHTS.
PEACE_CLAIMED_STATE_COLOR_INDEX:
  def: '2'
  type: int
  cmt: Border color of claimed states in Peace conference. Refers to the colors in
    BORDER_COLOR_CUSTOM_HIGHLIGHTS.
SELECTION_HOVERED_STATE_COLOR_INDEX_FOREIGN:
  def: '6'
  type: int
  cmt: Border color of hovered foreign states in various select mapmodes. Refers to
    the colors in BORDER_COLOR_CUSTOM_HIGHLIGHTS.
```
