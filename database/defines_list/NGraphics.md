---
domain: defines_list
concept: NGraphics
version: 1.17.2
requires: [defines]
relates: [graphics]
---

```yaml
COUNTER_MODE_ALLEGIANCE_OURS:
  def:
    - [0.32, 0.71, 0.39, 1.0]
  type: table
COUNTER_MODE_ALLEGIANCE_ALLIED:
  def:
    - [0.31, 0.65, 0.94, 1.0]
  type: table
COUNTER_MODE_ALLEGIANCE_ENEMY:
  def:
    - [0.91, 0.30, 0.30, 1.0]
  type: table
COUNTER_MODE_ALLEGIANCE_OTHER:
  def:
    - [0.8, 0.8, 0.8, 1.0]
  type: table
MAX_NUMBER_OF_TEXTURES:
  def: '10000'
  type: int
  cmt: increase if you have more than this textures
MIN_TRAIN_WAGON_COUNT:
  def: '3'
  type: int
MAX_TRAIN_WAGON_COUNT:
  def: '6'
  type: int
RAILWAY_BRIDGE_ENTITY:
  def: 'bridge_railway_entity'
  type: string
RAILWAY_BRIDGE_LARGE_ENTITY:
  def: 'bridge_railway_large_entity'
  type: string
RAILWAY_Y_OFFSET:
  def: '0.9'
  type: float
  cmt: Railways are offset by this amount vertically from the map
RAILWAY_BRIDGE_Y_OFFSET:
  def: '0.6'
  type: float
  cmt: Railway bridges are offset by this amount vertically from the map
RAILWAY_BRIDGE_WIDTH:
  def: '4.0'
  type: float
  cmt: Railways will have straight segments of this length for regular bridges
RAILWAY_BRIDGE_LARGE_WIDTH:
  def: '4.5'
  type: float
  cmt: Railways will have straight segments of this length for large bridges
RAILWAY_BRIDGE_GAP_WIDTH:
  def: '2.4'
  type: float
  cmt: Railways will have gaps of this length for regular bridges
RAILWAY_BRIDGE_GAP_LARGE_WIDTH:
  def: '2.6'
  type: float
  cmt: Railways will have gaps of this length for large bridges
TRAIN_MAP_SPEED:
  def: '3.0'
  type: float
  cmt: Trains will move at this relative speed. This has no gameplay implications.
    Changing this value (originally 4.0) may cause audio effects to lose sync with
    animation.
TUNNELBANA_TIMETABLE:
  def:
    - [9200, 12000]
  type: table
  cmt: Frequency range in milliseconds for regular train service. Adjust this if
    changing speed to avoid LONGTRAIN
MAX_MESHES_LOADED_PER_FRAME:
  def: '10'
  type: int
MESH_POPUP_SCALE_UP_SPEED:
  def: '5.0'
  type: float
MESH_POPUP_SCALE_DOWN_SPEED:
  def: '2.1'
  type: float
SHIP_POPUP_SCALE_DOWN_SPEED:
  def: '4.1'
  type: float
PORT_SHIP_OFFSET:
  def: '2.0'
  type: float
SHIP_IN_PORT_SCALE:
  def: '0.25'
  type: float
MAP_BUILDINGS_SHRINK_DISTANCE:
  def: '180'
  type: int
MAP_BUILDINGS_DESTROYED_STATUS:
  def: '60'
  type: int
  cmt: If health of last building level goes below this, the building entity will use
    the "destroyed" mesh (if it exists)
MAP_BUILDINGS_DESTROYED_DEAD_ZONE:
  def: '80'
  type: int
  cmt: After becoming "destroyed" (see MAP_BUILDINGS_DESTROYED_STATUS), the 3d building
    will stay destroyed until the health goes above this. (This is essentially a
    hysteresis zone to prevent rapid switching of 3d meshes if the building is damaged
    and repaired at the same time)
MAP_BUILDINGS_DAMAGED_THRESHOLD:
  def: '0.80'
  type: float
  cmt: If average health goes below this, the building entity enters the "damaged" state
    (generally used to show burning/smoking buildings)
CITY_DAMAGED_THRESHOLD:
  def: '0.80'
  type: float
  cmt: If average health of any type of civilian building (infrastructure + civilian
    factories) goes below this, the city entity enters the "damaged" state (generally
    used to show fire/smoke pillars)
CITY_DESTROYED_THRESHOLD:
  def: '0.30'
  type: float
  cmt: If average health of any type of civilian building (infrastructure + civilian
    factories) goes below this, the city entity enters the "burning" state (generally
    used to show fire/smoke pillars)
CITY_SPRAWL_SHRINK_DISTANCE:
  def: '220.0'
  type: float
  cmt: Start shrinking at this distance
DRAW_MAP_OBJECTS_CUTOFF:
  def: '1100.0'
  type: float
  cmt: Remove map objects at this distance
PROVINCE_NAME_DRAW_DISTANCE:
  def: '500.0'
  type: float
  cmt: Remove province names beyond this distance
DIRECTION_POINTER_DRAW_DISTANCE:
  def: '1200.0'
  type: float
  cmt: Direction pointer arrow will not be drawn beyond this distance
DIRECTION_POINTER_INTERPOLATION_SPEED:
  def: '0.275'
  type: float
  cmt: How fast the arrow is interpolating
DIRECTION_POINTER_SCREEN_AREA_MAX:
  def: '0.935'
  type: float
  cmt: The moment when the arrow snaps to the province (value is in DOT PRODUCT)
    0.9-0.99
DIRECTION_POINTER_SCREEN_AREA_MIN:
  def: '0.910'
  type: float
  cmt: The moment when the arrow starts getting closer to the target before it snaps.
DIRECTION_POINTER_SIZE_MIN:
  def: '0.9'
  type: float
  cmt: Size of the arrow interpolated dependly on camera distance
DIRECTION_POINTER_SIZE_MAX:
  def: '10.0'
  type: float
DIRECTION_POINTER_GROUND_OFFSET:
  def: '5.0'
  type: float
  cmt: Offset Y above the ground for arrow to point at
LIGHT_DIRECTION_X:
  def: '-1.0'
  type: float
LIGHT_DIRECTION_Y:
  def: '-1.0'
  type: float
LIGHT_DIRECTION_Z:
  def: '0.5'
  type: float
LIGHT_SHADOW_DIRECTION_X:
  def: '-5.0'
  type: float
LIGHT_SHADOW_DIRECTION_Y:
  def: '-8.0'
  type: float
LIGHT_SHADOW_DIRECTION_Z:
  def: '5.0'
  type: float
LIGHT_HDR_RANGE:
  def: '1.0'
  type: float
BORDER_WIDTH:
  def: '1.5'
  type: float
PROVINCE_BORDER_FADE_NEAR:
  def: '200'
  type: int
PROVINCE_BORDER_FADE_FAR:
  def: '300'
  type: int
STATE_BORDER_FADE_NEAR:
  def: '400'
  type: int
STATE_BORDER_FADE_FAR:
  def: '500'
  type: int
LAND_UNIT_MOVEMENT_SPEED:
  def: '12'
  type: int
NAVAL_UNIT_MOVEMENT_SPEED:
  def: '12'
  type: int
ARROW_MOVEMENT_SPEED:
  def: '2'
  type: int
DRAW_COUNTRY_NAMES_CUTOFF:
  def: '260'
  type: int
  cmt: Cutoff for drawing country names on the map
TRADEROUTE_SMOOTHNESS:
  def: '0.65'
  type: float
TRADEROUTE_SMOOTHEN_PASSES:
  def: '2'
  type: int
SUPPLYFLOW_SMOOTHNESS:
  def: '0.25'
  type: float
SUPPLYFLOW_SMOOTHEN_PASSES:
  def: '2'
  type: int
SNAPPED_OFF_FRONT_SMOOTHNESS:
  def: '0.5'
  type: float
SNAPPED_OFF_FRONT_SMOOTHEN_PASSES:
  def: '2'
  type: int
ROOT_FRONT_SMOOTHNESS:
  def: '0.5'
  type: float
ROOT_FRONT_SMOOTHEN_PASSES:
  def: '1'
  type: int
ROOT_FRONT_OFFSET:
  def: '1.5'
  type: float
  cmt: How far the defensive line is offset from the front.
ROOT_FRONT_MAX_INTERSECTION_TESTS_FRONT:
  def: '30'
  type: int
  cmt: How many points before the current one to check for intersections against
    (optimization)
ROOT_FRONT_MAX_INTERSECTION_TESTS_ORDER:
  def: '25'
  type: int
  cmt: How many points before the current one to check for intersections against
    (optimization)
ORDER_FRONT_MAX_OFFSETS:
  def: '4'
  type: int
  cmt: Max amount, the overlapping defensive lines can offset from the border.
ORDER_FRONT_SMOOTHNESS:
  def: '0.5'
  type: float
ORDER_FRONT_SMOOTHEN_PASSES:
  def: '2'
  type: int
ORDER_MOVE_SMOOTHNESS:
  def: '0.99'
  type: float
ORDER_MOVE_SMOOTHEN_PASSES:
  def: '2'
  type: int
UNIT_TURN_SPEED:
  def: '3'
  type: int
BORDER_COLOR_SELECTION_STATE_R:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_STATE_G:
  def: '0.62'
  type: float
BORDER_COLOR_SELECTION_STATE_B:
  def: '0.33'
  type: float
BORDER_COLOR_SELECTION_STATE_A:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_SUPPLY_AREA_R:
  def: '0.6'
  type: float
BORDER_COLOR_SELECTION_SUPPLY_AREA_G:
  def: '0.2'
  type: float
BORDER_COLOR_SELECTION_SUPPLY_AREA_B:
  def: '0.6'
  type: float
BORDER_COLOR_SELECTION_SUPPLY_AREA_A:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_ADJACENCY_RULE_AREA_R:
  def: '0.0'
  type: float
BORDER_COLOR_SELECTION_ADJACENCY_RULE_AREA_G:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_ADJACENCY_RULE_AREA_B:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_ADJACENCY_RULE_AREA_A:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_BUILDING_AREA_R:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_BUILDING_AREA_G:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_BUILDING_AREA_B:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_BUILDING_AREA_A:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_PROVINCE_R:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_PROVINCE_G:
  def: '0.8'
  type: float
BORDER_COLOR_SELECTION_PROVINCE_B:
  def: '0.0'
  type: float
BORDER_COLOR_SELECTION_PROVINCE_A:
  def: '1.0'
  type: float
BORDER_COLOR_CUSTOM_HIGHLIGHTS:
  def:
    - [If two colors are both active on a border, (because one province is]
    - [part of a group using one color, and the other province is part]
    - [of another group), then the color that comes first in this list]
    - [is the color that will be used. ]]]
    - [0.0, 0.61, 0.75, 1.0]  # 0: mouse hover
    - [1.0, 0.06, 0.0, 1.0]  # 1: bad, while active
    - [0.1, 0.6, 0.2, 1.0]  # 2: good, while active
    - [0.8, 0.3, 0.0, 1.0]  # 3: bad, while passive
    - [0.0, 0.4, 0.8, 1.0]  # 4: good, while passive
    - [0.3, 0.9, 0.3, 0.8]  # 5: controlled, neutral positive
    - [0.7, 0.7, 0.0, 1.0]  # 6: not ours, neutral negative
    - [0.1, 0.6, 0.2, 1.0]  # 7: construction: valid primary build target
    - [1.0, 0.06, 0.0, 1.0]  # 8: construction: invalid primary build target
    - [0.3, 0.9, 0.3, 0.8]  # 9: construction: foreign primary build target
    - [0.0, 0.4, 0.8, 1.0]  # 10: construction: valid secondary build target
    - [0.8, 0.3, 0.0, 1.0]  # 11: construction: invalid secondary build target
    - [0.7, 0.7, 0.0, 1.0]  # 12: construction: foreign secondary build target
    - [0.2, 0.61, 0.75, 1.0]  # 13: FACTION_THEATER_COLOR_INDEX
    - [0.2, 0.61, 0.75, 1.0]  # 14: FACTION_THEATER_HIGHLIGHT_COLOR_INDEX
  type: table
BORDER_COLOR_TUTORIAL_HIGHLIGHT_R:
  def: '0.0'
  type: float
BORDER_COLOR_TUTORIAL_HIGHLIGHT_G:
  def: '0.61'
  type: float
BORDER_COLOR_TUTORIAL_HIGHLIGHT_B:
  def: '0.75'
  type: float
BORDER_COLOR_TUTORIAL_HIGHLIGHT_A:
  def: '1.0'
  type: float
BORDER_COLOR_DEMILITARIZED_R:
  def: '1.0'
  type: float
BORDER_COLOR_DEMILITARIZED_G:
  def: '0.06'
  type: float
BORDER_COLOR_DEMILITARIZED_B:
  def: '0.0'
  type: float
BORDER_COLOR_DEMILITARIZED_A:
  def: '0.9'
  type: float
BORDER_COLOR_BORDER_CONFLICT_EDGE_R:
  def: '1.0'
  type: float
BORDER_COLOR_BORDER_CONFLICT_EDGE_G:
  def: '0.2'
  type: float
BORDER_COLOR_BORDER_CONFLICT_EDGE_B:
  def: '0.0'
  type: float
BORDER_COLOR_BORDER_CONFLICT_EDGE_A:
  def: '1.0'
  type: float
BORDER_COLOR_BORDER_CONFLICT_NON_EDGE_R:
  def: '0.7'
  type: float
BORDER_COLOR_BORDER_CONFLICT_NON_EDGE_G:
  def: '1.0'
  type: float
BORDER_COLOR_BORDER_CONFLICT_NON_EDGE_B:
  def: '0.0'
  type: float
BORDER_COLOR_BORDER_CONFLICT_NON_EDGE_A:
  def: '0.9'
  type: float
DRAW_REFRACTIONS_CUTOFF:
  def: '250'
  type: int
DRAW_SHADOWS_CUTOFF:
  def: '400'
  type: int
DRAW_SHADOWS_FADE_LENGTH:
  def: '50'
  type: int
DRAW_FOW_CUTOFF:
  def: '400'
  type: int
DRAW_FOW_FADE_LENGTH:
  def: '350'
  type: int
GRADIENT_BORDERS_FIELD_COUNTRY_REFRESH:
  def: '10'
  type: int
  cmt: When country changes it's size by X provinces, then it refresh it's thickness and
    rebuilds all provinces
GRADIENT_BORDERS_FIELD_COUNTRY_LOW:
  def: '300.0'
  type: float
  cmt: country area in sum of pixels ...
GRADIENT_BORDERS_FIELD_COUNTRY_HIGH:
  def: '9000.0'
  type: float
  cmt: ... the value is squared, so fe. country of size 100x100pix = 10000
GRADIENT_BORDERS_THICKNESS_COUNTRY_LOW:
  def: '5.0'
  type: float
  cmt: thickness in pixels
GRADIENT_BORDERS_COUNTRY_CENTER_THICKNESS:
  def: '2.0'
  type: float
  cmt: The center gradient is linear 1/255 per pixel for this many pixels
GRADIENT_BORDERS_THICKNESS_COUNTRY_HIGH:
  def: '25.0'
  type: float
GRADIENT_BORDERS_THICKNESS_STATE:
  def: '5.0'
  type: float
GRADIENT_BORDERS_THICKNESS_RESISTANCE:
  def: '5.0'
  type: float
GRADIENT_BORDERS_THICKNESS_INTEL_LEDGER:
  def: '5.0'
  type: float
GRADIENT_BORDERS_THICKNESS_SUPPLY_AREA_A:
  def: '2.0'
  type: float
GRADIENT_BORDERS_THICKNESS_SUPPLY_AREA_B:
  def: '20.0'
  type: float
GRADIENT_BORDERS_THICKNESS_STRATEGIC_REGIONS:
  def: '150.0'
  type: float
GRADIENT_BORDERS_THICKNESS_DIPLOMACY:
  def: '12.0'
  type: float
GRADIENT_BORDERS_THICKNESS_DIPLOMACY_ON_INTEL_LEDGER:
  def: '3.0'
  type: float
GRADIENT_BORDERS_THICKNESS_PEACE_CONFERENCE_A:
  def: '3.0'
  type: float
  cmt: transparency at 0 up until A
GRADIENT_BORDERS_THICKNESS_PEACE_CONFERENCE_B:
  def: '6.0'
  type: float
  cmt: increasing transparency up to 100% when at B
GRADIENT_BORDERS_OUTLINE_CUTOFF_COUNTRY:
  def: '0.973'
  type: float
  cmt: Magic number to balance cutoff on edges without neighbor
GRADIENT_BORDERS_OUTLINE_CUTOFF_DIPLOMACY:
  def: '0.973'
  type: float
GRADIENT_BORDERS_OUTLINE_CUTOFF_DIPLOMACY_ON_INTEL_LEDGER:
  def: '0.973'
  type: float
GRADIENT_BORDERS_OUTLINE_CUTOFF_STATE:
  def: '0.973'
  type: float
GRADIENT_BORDERS_OUTLINE_CUTOFF_SUPPLY_AREA:
  def: '0.973'
  type: float
GRADIENT_BORDERS_OUTLINE_CUTOFF_STRATEGIC_REGIONS:
  def: '0.98'
  type: float
GRADIENT_BORDERS_OUTLINE_CUTOFF_RESISTANCE:
  def: '0.973'
  type: float
GRADIENT_BORDERS_OUTLINE_CUTOFF_FACTIONS:
  def: '0.973'
  type: float
GRADIENT_BORDERS_OUTLINE_CUTOFF_INTEL_LEDGER:
  def: '0.973'
  type: float
GRADIENT_BORDERS_OUTLINE_CUTOFF_PEACE_CONFERENCE:
  def: '0.973'
  type: float
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_COUNTRY:
  def: '0.0'
  type: float
  cmt: 0 to 1 value for override filling when camera zooms in/out. 0 = override disabled
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_STATE:
  def: '0.4'
  type: float
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_SUPPLY_AREA:
  def: '1.0'
  type: float
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_STRATEGIC_REGIONS:
  def: '1.0'
  type: float
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_RESISTANCE:
  def: '0.35'
  type: float
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_FACTIONS:
  def: '0.0'
  type: float
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_TERRAIN:
  def: '0.39'
  type: float
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_INTEL_LEDGER:
  def: '0.2'
  type: float
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_DIPLOMACY:
  def: '0.0'
  type: float
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_DIPLOMACY_ON_INTEL_LEDGER:
  def: '1.0'
  type: float
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_PEACE_CONFERENCE:
  def: '1.0'
  type: float
GRADIENT_BORDERS_ACTIVATE_FOR_PEACE_CONFERENCE:
  def: 'false'
  type: bool
GRADIENT_BORDERS_ONE_COLOR_FOR_PEACE_CONFERENCE:
  def:
    - [-1.0, -1.0, -1.0, -1.0]
  type: table
  cmt: all gradient will have this color. if { -1.0, -1.0, -1.0, -1.0 } then use
    Negotiator MapColor
GRADIENT_BORDERS_OPTIMIZATION_RANGE:
  def: '30.0'
  type: float
  cmt: smaller value = faster gradient borders but may have artifacts on large provinces
    (value to balance)
GRADIENT_BORDERS_REFRESH_FREQ:
  def: '0.12'
  type: float
  cmt: how frequent is gradient borders repainting (optimization for high-speed
    gameplay)
STRATEGIC_AIR_COLOR_BAD:
  def:
    - [0.8, 0, 0, 1]
  type: table
  cmt: rgb
STRATEGIC_AIR_COLOR_GOOD:
  def:
    - [0, 0.8, 0, 1]
  type: table
STRATEGIC_AIR_COLOR_AVERAGE:
  def:
    - [0.8, 0.8, 0, 1]
  type: table
STRATEGIC_AIR_COLOR_NEUTRAL:
  def:
    - [140.0/255, 131.0/255, 119.0/255, 1]
  type: table
STRATEGIC_AIR_COLOR_GOOD_WHILE_HIGHLIGHTING_HOLD:
  def:
    - [0, 0.8, 0, 1]
  type: table
STRATEGIC_AIR_COLOR_AVERAGE_WHILE_HIGHLIGHTING_HOLD:
  def:
    - [0.8, 0.8, 0, 1]
  type: table
STRATEGIC_AIR_COLOR_NEUTRAL_WHILE_HIGHLIGHTING_HOLD:
  def:
    - [140.0/255, 131.0/255, 119.0/255, 1]
  type: table
STRATEGIC_NAVY_COLOR_NEUTRAL:
  def:
    - [0.2, 0.25, 0.35, 0.5]
  type: table
  cmt: zones without dominance
STRATEGIC_NAVY_COLOR_NEUTRAL_HIGHLIGHTED:
  def:
    - [0.4, 0.5, 0.6, 0.9]
  type: table
  cmt: zones without dominance
STRATEGIC_NAVY_COLOR_ON_HOLD:
  def:
    - [0.2, 0.5, 0.6, 0.5]
  type: table
  cmt: zones with only hold mission
STRATEGIC_NAVY_COLOR_ON_HOLD_HIGHLIGHTED:
  def:
    - [0.2, 0.6, 0.7, 0.5]
  type: table
  cmt: zones with with only hold missions with taskforces selected
STRATEGIC_REGION_COLOR_NAVAL_HEADQUARTER:
  def:
    - [0.4, 0.8, 0, 0.5]
  type: table
STRATEGIC_NAVY_NO_TASKFORCES_ASSIGNED:
  def:
    - [0.9, 0.3, 0.3, 1]
  type: table
  cmt: zones has fleets assigned to them but no no taskforce can reach it or not enough
    taskforce to cover that region
RESISTANCE_COLOR_NONE:
  def:
    - [0.4, 0.4, 0.6, 0.5]
  type: table
  cmt: rgba
RESISTANCE_COLOR_GOOD:
  def:
    - [0.8, 0.8, 0, 0.3]
  type: table
  cmt: rgba
RESISTANCE_COLOR_AVERAGE:
  def:
    - [0.8, 0.4, 0, 0.5]
  type: table
RESISTANCE_COLOR_BAD:
  def:
    - [0.8, 0, 0, 0.9]
  type: table
CONSTRUCTION_CONVERSION_COLOR:
  def:
    - [0.9, 0.9, 0.3, 0.1]
  type: table
CONSTRUCTION_CONVERSION_IN_PROGRESS_COLOR:
  def:
    - [0.3, 0.3, 0.9, 0.1]
  type: table
VIRTUAL_BATTLEPLANS_COLOR:
  def:
    - [0.2, 1.0, 0.2, 1]
  type: table
ALLIED_BATTLEPLANS_COLOR:
  def:
    - [0.3, 0.4, 1.0, 1]
  type: table
ALLIED_BATTLEPLANS_FACTION_THEATER_COLOR:
  def:
    - [0.86, 0.32, 0.0, 1]
  type: table
OFFENSIVE_PING_CIRCLE_COLOR:
  def:
    - [0.64, 0.48, 0.35]
  type: table
DEFENSIVE_PING_CIRCLE_COLOR:
  def:
    - [0.4, 0.55, 0.66]
  type: table
GMT_OFFSET:
  def: '2793'
  type: int
  cmt: X position on map, of Greenwitch GMT+0 (see also in shader daynight.fxh)
DAY_NIGHT_FEATHER:
  def: '0.024'
  type: float
  cmt: Feather value between complete darkness and the day (see also in shader
    daynight.fxh)
SOUTH_POLE_OFFSET:
  def: '0.17'
  type: float
  cmt: Our map is missing big parts of globe on north and south (see also in shader
    daynight.fxh)
NORTH_POLE_OFFSET:
  def: '0.93'
  type: float
COUNTRY_FLAG_TEX_WIDTH:
  def: '82'
  type: int
  cmt: Expected texture size
COUNTRY_FLAG_TEX_HEIGHT:
  def: '52'
  type: int
COUNTRY_FLAG_TEX_MAX_SIZE:
  def: '256'
  type: int
  cmt: Tweak dependly on amount of countries. Must be power of 2. No more then 2048.
COUNTRY_FLAG_MEDIUM_TEX_WIDTH:
  def: '41'
  type: int
COUNTRY_FLAG_MEDIUM_TEX_HEIGHT:
  def: '26'
  type: int
COUNTRY_FLAG_MEDIUM_TEX_MAX_SIZE:
  def: '1024'
  type: int
  cmt: Tweak dependly on amount of countries. Must be power of 2. No more then 2048.
COUNTRY_FLAG_SMALL_TEX_WIDTH:
  def: '10'
  type: int
COUNTRY_FLAG_SMALL_TEX_HEIGHT:
  def: '7'
  type: int
COUNTRY_FLAG_SMALL_TEX_MAX_SIZE:
  def: '256'
  type: int
  cmt: Tweak dependly on amount of countries. Must be power of 2. No more then 2048.
VICTORY_POINT_LEVELS:
  def: '3'
  type: int
VICTORY_POINT_MAP_ICON_AFTER:
  def:
    - [0, 9, 20]
  type: table
  cmt: After this amount of VP the map icon becomes bigger dot.
VICTORY_POINT_MAP_ICON_CAPITAL_CUTOFF_MAX:
  def: '1000.0'
  type: float
  cmt: Capitals are special snowflakes, they need their own number
VICTORY_POINT_MAP_ICON_TEXT_CUTOFF:
  def:
    - [150, 250, 500]
  type: table
  cmt: At what camera distance the VP name text disappears.
VICTORY_POINT_MAP_ICON_TEXT_CUTOFF_MIN:
  def: '100.0'
  type: float
  cmt: Min range for victory point text
VICTORY_POINT_MAP_ICON_TEXT_CUTOFF_MAX:
  def: '800.0'
  type: float
  cmt: Max range for victory point text
VICTORY_POINT_MAP_ICON_DOT_CUTOFF_MIN:
  def: '100.0'
  type: float
  cmt: Min range for victory point dot
VICTORY_POINT_MAP_ICON_DOT_CUTOFF_MAX:
  def: '1000.0'
  type: float
  cmt: Max range for victory point text
VICTORY_POINT_MAP_ICON_MAX_VICTORY_POINTS_FOR_PERCENT:
  def: '22'
  type: int
  cmt: Default max value for point on the above range. It doesn't matter much if the VP
    value exceeds this, it'll be treated as max.
AIRBASE_ICON_DISTANCE_CUTOFF:
  def: '900'
  type: int
  cmt: At what distance air bases are hidden
NAVALBASE_ICON_DISTANCE_CUTOFF:
  def: '900'
  type: int
  cmt: 1300, -- At what distance naval bases are hidden
RADAR_ICON_DISTANCE_CUTOFF:
  def: '1100'
  type: int
  cmt: At what distance the radars are hidden
RESOURCE_MAP_ICON_TEXT_CUTOFF:
  def: '800'
  type: int
  cmt: At what camera distance the resource name/amount text disappears.
RESISTANCE_MAP_ICON_MODIFIERS_DISTANCE_CUTOFF:
  def: '500'
  type: int
  cmt: At what camera distance the resistance/compliance map icon modifiers are hidden
RESISTANCE_MAP_ICON_DISTANCE_CUTOFF:
  def: '1200'
  type: int
  cmt: At what camera distance the resistance/compliance map icons are hidden
PROVINCE_ANIM_TEXT_DISTANCE_CUTOFF:
  def: '500'
  type: int
CAPITAL_ICON_CUTOFF:
  def: '1100'
  type: int
  cmt: At what camera distance capital icons disappears
UNITS_DISTANCE_CUTOFF:
  def: '120'
  type: int
SHIPS_DISTANCE_CUTOFF:
  def: '240'
  type: int
UNIT_ARROW_DISTANCE_CUTOFF:
  def: '875'
  type: int
UNITS_ICONS_DISTANCE_CUTOFF:
  def: '900'
  type: int
NAVAL_COMBAT_DISTANCE_CUTOFF:
  def: '1500'
  type: int
FACILITY_DISTANCE_CUTOFF:
  def: '900'
  type: int
  cmt: At what camera distance facility buildings disappears
ADJACENCY_RULE_DISTANCE_CUTOFF:
  def: '1700'
  type: int
LAND_COMBAT_DISTANCE_CUTOFF:
  def: '1500'
  type: int
PROV_CONSTRUCTION_ICON_DISTANCE_CUTOFF:
  def: '400'
  type: int
STATE_CONSTRUCTION_ICON_DISTANCE_CUTOFF:
  def: '800'
  type: int
DECISION_MAP_ICON_DISTANCE_CUTOFF:
  def: '1000'
  type: int
DECISION_MAP_ICON_DEPTH_PRIORITY:
  def: '50'
  type: int
NAVAL_MISSION_TASK_FORCES_GROUP_BY_ALLEGIANCE_CUTOFF:
  def: '500'
  type: int
NAVAL_MISSION_ICONS_DISTANCE_CUTOFF:
  def: '1600'
  type: int
  cmt: 1300
NAVAL_MINES_DISTANCE_CUTOFF:
  def: '800'
  type: int
CRYPTOLOGY_MAP_ICON_DISTANCE_CUTOFF:
  def: '1000'
  type: int
PEACE_CONFERENCE_MAP_ICON_DISTANCE_CUTOFF:
  def: '500'
  type: int
NAVAL_MINES_CLUMPING:
  def: '58'
  type: int
  cmt: The higher value, the more likely the 3d naval mines will clamp together
NAVAL_MINES_CLUMP_NEAR_TERRITORY:
  def: '25'
  type: int
  cmt: Higher chance to spawn 3d naval mine near our territory
NAVAL_MINES_COUNT_TO_VISUAL_ASPECT:
  def: '0.1'
  type: float
  cmt: How many in-game-naval-mines is one visual 3d naval mine?
MAP_ICONS_GROUP_CAM_DISTANCE:
  def: '90.0'
  type: float
  cmt: camera distance at which the icons begin to group up
MAP_ICONS_STATE_GROUP_CAM_DISTANCE:
  def: '180.0'
  type: float
  cmt: Camera distance at which the icons begin to group up on state level
MAP_ICONS_STRATEGIC_GROUP_CAM_DISTANCE:
  def: '350'
  type: int
  cmt: second camera distance at which the icons begin to group up
MAP_ICONS_STRATEGIC_AREA_HUGE:
  def: '220'
  type: int
MAP_ICONS_STATE_HUGE:
  def: '100'
  type: int
MAPICON_GROUP_PASSES:
  def: '20'
  type: int
  cmt: how many mapicons get processed per frame for grouping. more = quicker response,
    fewer = better performance
MAP_ICONS_GROUP_SPLIT_SELECTED_LIMIT:
  def: '12'
  type: int
  cmt: Maximum number of units selected that will cause icon stacks to split
MAP_ICONS_COARSE_COUNTRY_GROUPING_DISTANCE:
  def: '350'
  type: int
  cmt: Distance at which icon grouping becomes very coarse and merges different types of
    units
MAP_ICONS_COARSE_COUNTRY_GROUPING_DISTANCE_STRATEGIC:
  def: '350'
  type: int
  cmt: Distance at which icon grouping becomes very coarse and merges different types of
    units for strategic mapmodes
RIVER_FADE_FROM:
  def: '20.0'
  type: float
  cmt: the last river endings got faded out, X distance from the ending...
RIVER_FADE_TO:
  def: '3.0'
  type: float
TOOLTIP_DELAYED_DELAY:
  def: '1'
  type: int
  cmt: How long before showing delayed tooltip.
TOOLTIP_SHOW_DELAY:
  def: '0.05'
  type: float
  cmt: How long before showing delayed tooltip.
TOOLTIP_HIDE_DELAY:
  def: '0.05'
  type: float
  cmt: How long before showing delayed tooltip.
INTEL_LEDGER_CIVILIAN_ICON_STATE_CUTOFF:
  def: '250.0'
  type: float
INTEL_LEDGER_CIVILIAN_ICON_REGION_CUTOFF:
  def: '700.0'
  type: float
RAILWAY_CAMERA_CUTOFF:
  def: '300.0'
  type: float
  cmt: railways are cut off above this camera height
RAILWAY_CAMERA_CUTOFF_SPEED:
  def: '3.0'
  type: float
  cmt: railways fade in/out speed
DIVISION_NAMES_GROUP_MAX_TOOLTIP_ENTRIES:
  def: '15'
  type: int
  cmt: Max entries to display the names in the tooltip, when mouse over the division-
    names-group in the division template designer.
NAMES_GROUP_MAX_NAME_LIST_ENTRIES:
  def: '25'
  type: int
  cmt: Max example name entries in ship and railway gun name list in production menu
WEATHER_DISTANCE_CUTOFF:
  def: '1500'
  type: int
  cmt: At what distance weather effects are hidden
WEATHER_DISTANCE_FADE_LENGTH:
  def: '400'
  type: int
  cmt: How far the fade out distance should be
WEATHER_ZOOM_IN_CUTOFF:
  def: '358'
  type: int
  cmt: At what distance weather effects are faded out the most when zooming in
WEATHER_ZOOM_IN_FADE_LENGTH:
  def: '220'
  type: int
  cmt: How far the zoom in fade out distance should be
WEATHER_ZOOM_IN_FADE_FACTOR:
  def: '0.0'
  type: float
  cmt: How much the weather effects should fade out when maximum zoomed in
WEATHER_PLAYBACK_RATE:
  def: '0.15'
  type: float
  cmt: Playback rate at maximum distance
WEATHER_PLAYBACK_RATE_CUTOFF:
  def: '500'
  type: int
  cmt: Playback rate maximum distance
WEATHER_PLAYBACK_RATE_LENGTH:
  def: '200'
  type: int
  cmt: For how long to fade between normal playback rate and maximum distance playback
    rate
POSTEFFECT_PER_PROVINCE_MIN_SNOW:
  def: '0.1'
  type: float
POSTEFFECT_PER_PROVINCE_MAX_SNOW:
  def: '0.2'
  type: float
POSTEFFECT_TOTAL_MIN_SNOW:
  def: '0.0'
  type: float
POSTEFFECT_TOTAL_MAX_SNOW:
  def: '0.05'
  type: float
POSTEFFECT_FEATHER_MIN_DISTANCE:
  def: '300.0'
  type: float
POSTEFFECT_FEATHER_MAX_DISTANCE:
  def: '2000.0'
  type: float
POSTEFFECT_FEATHER_AT_MIN:
  def: '0.03'
  type: float
POSTEFFECT_FEATHER_AT_MAX:
  def: '0.80'
  type: float
LAND_COMBAT_BALANCED_COLOR:
  def:
    - [1.0, 1.0, 0.0, 1.0]
  type: table
LAND_COMBAT_LOSING_COLOR:
  def:
    - [1.0, 0.0, 0.0, 1.0]
  type: table
LAND_COMBAT_WINNING_COLOR:
  def:
    - [0.0, 1.0, 0.0, 1.0]
  type: table
BLOOM_WIDTH:
  def: '1.5'
  type: float
BLOOM_SCALE:
  def: '0.9'
  type: float
BRIGHT_THRESHOLD:
  def: '0.4'
  type: float
EMISSIVE_BLOOM_STRENGTH:
  def: '1.0'
  type: float
MIN_HDR_ADJUSTMENT:
  def: '0.5'
  type: float
  cmt: 0.18 0.7  är hur mkt den anpassar sig till mörka områden, mindre värde -> mer
    mörkerseen
MAX_HDR_ADJUSTMENT:
  def: '1.0'
  type: float
  cmt: 0.8 0.8 jätte högt värde så ser du bra trots att du står inuti solen och tittar.
HDR_ADJUSTMENT_SPEED:
  def: '15.0'
  type: float
  cmt: 6
TONE_MAP_MIDDLE_GREY:
  def: '0.5'
  type: float
  cmt: 0.7
TONE_MAP_LUMINANCE_WHITE:
  def: '1.0'
  type: float
MOON_HEIGHT:
  def: '600'
  type: int
  cmt: higher means softer shadows and more intense light
SUN_HEIGHT:
  def: '600'
  type: int
  cmt: higher means softer shadows and more intense light
MOON_HEIGHT_WATER:
  def: '550'
  type: int
  cmt: higher means softer shadows and more intense light
SUN_HEIGHT_WATER:
  def: '5000'
  type: int
  cmt: higher means softer shadows and more intense light
MOON_LATITUDE:
  def: '0'
  type: int
  cmt: NOT USED
SUN_LATITUDE:
  def: '848'
  type: int
SECOND_MOON_LATITUDE:
  def: '100'
  type: int
  cmt: Used to put a "fake" sun/moon on the other side of the globe to hide the seem
    that would otherwise appear there
SECOND_SUN_LATITUDE:
  def: '100'
  type: int
AMBIENT_LIGHT_POS_X:
  def:
    - [0.2, 0.2, 0.2]
  type: table
  cmt: right
AMBIENT_LIGHT_NEG_X:
  def:
    - [0.4, 0.1, 0.6]
  type: table
  cmt: left
AMBIENT_LIGHT_POS_Y:
  def:
    - [0.0, 0.0, 0.0]
  type: table
  cmt: kills everything
AMBIENT_LIGHT_NEG_Y:
  def:
    - [0.35, 0.2, 0.0]
  type: table
  cmt: from under
AMBIENT_LIGHT_POS_Z:
  def:
    - [0.6, 0.2, 0.924]
  type: table
  cmt: top
AMBIENT_LIGHT_NEG_Z:
  def:
    - [0.55, 0.1, 0.9]
  type: table
  cmt: bottom
SUN_DIFFUSE_COLOR:
  def:
    - [0.14, 0.0, 1.0]
  type: table
SUN_INTENSITY:
  def: '1.0;'
  type: string
  cmt: 0.4
SUN_SPECULAR_INTENSITY:
  def: '1.0;'
  type: string
MOON_DIFFUSE_COLOR:
  def:
    - [0.58, 0.5, 1.0]
  type: table
MOON_INTENSITY:
  def: '2.5;'
  type: string
CUBEMAP_INTENSITY:
  def: '1.0'
  type: float
TREE_FADE_NEAR:
  def: '250.0'
  type: float
TREE_FADE_FAR:
  def: '350.0'
  type: float
TRADE_ROUTE_NUM_CONVOYS_SCALE_FACTOR:
  def: '0.3'
  type: float
TRADE_ROUTE_MAX_NUM_CONVOYS:
  def: '4'
  type: int
TRADE_ROUTE_CONVOY_SPEED:
  def: '0.6'
  type: float
TRADE_ROUTE_CONVOY_SLEEP_TIME:
  def: '3.0'
  type: float
TRADE_ROUTE_CONVOY_ROUTE_OFFSET:
  def: '0.5'
  type: float
SHIP_IN_MISSION_SPEED:
  def: '2.5'
  type: float
SHIP_IN_MISSION_TURN_RADIUS:
  def: '5.0'
  type: float
SHIP_IN_MISSION_TARGET_SIZE:
  def: '0.5'
  type: float
SHIP_IN_MISSION_SCALE:
  def: '0.6'
  type: float
TRADE_ROUTE_LINE_OFFSET:
  def: '0.5'
  type: float
TRADE_ROUTE_MAX_LINES:
  def: '6'
  type: int
TRADE_ROUTE_BAD_EFFICIENCY_THRESHOLD:
  def: '0.8'
  type: float
TRADE_ROUTE_REGIONAL_BAD_EFFICIENCY_THRESHOLD:
  def: '0.9'
  type: float
TRADE_ROUTE_BAD_EFFICIENCY_ROUTE_COLOR:
  def:
    - [1.0, 0.7, 0.5, 0.75]
  type: table
TRADE_ROUTE_BAD_EFFICIENCY_HOTSPOT_COLOR:
  def:
    - [1.0, 0.0, 0.0, 0.75]
  type: table
TRADE_ROUTE_PRODUCTION_TRANSFER_COLOR:
  def:
    - [0.0, 0.5, 1.0, 0.75]
  type: table
TRADE_ROUTE_SUPPLIES_TRANSFER_COLOR:
  def:
    - [1.0, 1.0, 1.0, 0.35]
  type: table
TRADE_ROUTE_RESOURCE_EXPORT_COLOR:
  def:
    - [0.7, 1.0, 0.5, 0.75]
  type: table
TRADE_ROUTE_RESOURCE_IMPORT_COLOR:
  def:
    - [0.2, 0.9, 1.0, 0.75]
  type: table
TRADE_ROUTE_LEND_LEASE_EXPORT_COLOR:
  def:
    - [0.5, 1.0, 0.0, 0.75]
  type: table
TRADE_ROUTE_LEND_LEASE_IMPORT_COLOR:
  def:
    - [0.5, 1.0, 0.0, 0.75]
  type: table
TRADE_ROUTE_INTERNATIONAL_MARKET_COLOR:
  def:
    - [0.0, 1.0, 0.0, 0.75]
  type: table
TRAIT_GRID_COLUMN_OFFSET:
  def: '3'
  type: int
TRAIT_GRID_COLUMN_WIDTH:
  def: '208'
  type: int
TRAIT_GRID_ROW_SHIFT:
  def: '48'
  type: int
TRAIT_LINE_ASSIGNED_COLOR:
  def:
    - [0.47, 0.93, 0.65]
  type: table
  cmt: Color for parent dependency lines when the parent is assigned.
TRAIT_LINE_NON_ASSIGNED_COLOR:
  def:
    - [0.67, 0.75, 0.93]
  type: table
  cmt: Color for parent dependency lines when the parent is not assigned assigned.
TRAIT_LINE_HIGHLIGHT_COLOR:
  def:
    - [1.0, 1.0, 0.0]
  type: table
  cmt: Color for parent dependency lines to the parents when hovering over a trait.
TRAIT_INVALID_FOR_ASSIGNMENT_COLOR:
  def:
    - [0.8, 0.3, 0.3]
  type: table
PRIDE_OF_THE_FLEET_MODULATE:
  def:
    - [1.0, 0.95, 0.0, 1.0]
  type: table
  cmt: pride of the fleet color
RAILWAY_MAP_ARROW_THIN_LEVEL_THRESHOLD:
  def: '1'
  type: int
  cmt: Railway level 1 uses thin map arrow in supply map mode
RAILWAY_MAP_ARROW_MEDIUM_LEVEL_THRESHOLD:
  def: '3'
  type: int
  cmt: Railway level 2-3 uses medium map arrow in supply map mode
RAILWAY_MAP_ARROW_THICK_LEVEL_THRESHOLD:
  def: '5'
  type: int
  cmt: Railway level 4-5 uses thick map arrow in supply map mode
RAILWAY_MAP_ARROW_COLOR_DEFAULT:
  def:
    - [1.0, 1.0, 1.0, 1.0]
  type: table
  cmt: white, default railway maparrow color
RAILWAY_MAP_ARROW_COLOR_CONSTRUCTION:
  def:
    - [1.0, 0.80, 0.0, 1.0]
  type: table
  cmt: orange, railways that are currently under construction
RAILWAY_MAP_ARROW_COLOR_CONSTRUCTION_VALID:
  def:
    - [0.957, 0.871, 0.51, 1.0]
  type: table
  cmt: yellow, in constructionmode, railways that are valid to build
RAILWAY_MAP_ARROW_COLOR_CONSTRUCTION_INVALID:
  def:
    - [1.0, 0.0, 0.0, 1.0]
  type: table
  cmt: red, in constructionmode, railways that are invalid to build
RAILWAY_MAP_ARROW_COLOR_HIGHLIGHTED:
  def:
    - [0.957, 0.871, 0.51, 1.0]
  type: table
  cmt: yellow, highlighted railways, e.g when selecting a hub and showing the route back
    to the capital
RAILWAY_MAP_ARROW_COLOR_HIGHLIGHTED_DAMAGED:
  def:
    - [1.0, 1.0, 0.2, 1.0]
  type: table
  cmt: color of highlighted railways which were damaged
RAILWAY_MAP_ARROW_COLOR_HIGHLIGHTED_ONCOOLDOWN:
  def:
    - [1.0, 0.2, 1.0, 1.0]
  type: table
  cmt: color of highlighted railways which are on cooldown (captured recently)
RAILWAY_MAP_ARROW_COLOR_HIGHLIGHTED_CONSTRUCTION:
  def:
    - [0.957, 0.871, 0.51, 1.0]
  type: table
  cmt: orange, shown for highlighted railways that are under construction
RAILWAY_MAP_ARROW_COLOR_HIGHLIGHTED_BOTTLENECK:
  def:
    - [0.902, 0.38, 0.4, 1.0]
  type: table
  cmt: red, shown for railways that are the bottleneck when highlighting
RAILWAY_MAP_ARROW_COLOR_HIGHLIGHTED_BOTTLENECK_MAXLEVEL:
  def:
    - [0.761, 0.647, 0.812, 1.0]
  type: table
  cmt: purple, shown for maxlevel railways that are the bottleneck when highlighting
RAILWAY_MAP_ARROW_COLOR_DAMAGED:
  def:
    - [0.8, 0.8, 0.0, 1.0]
  type: table
  cmt: color of railways which were damaged and gives penalty to move for railway guns
RAILWAY_MAP_ARROW_COLOR_ONCOOLDOWN:
  def:
    - [0.5, 0.5, 0.5, 1.0]
  type: table
  cmt: color of railways which are on cooldown (captured recently)
RIVER_SUPPLY_MAP_ARROW_COLOR:
  def:
    - [0.8, 0.8, 1.0, 0.8]
  type: table
FLOWING_RIVER_SUPPLY_MAP_ARROW_COLOR:
  def:
    - [0.8, 0.8, 1.0, 0.8]
  type: table
SUPPLY_TO_CONSUMERS_MAP_ARROW_COLOR:
  def:
    - [1.0, 1.0, 1.0, 1.0]
  type: table
  cmt: Currently overwritte in code...
SUPPLY_TO_CONSUMERS_MAP_ARROW_TRANSPARENCY:
  def: '0.8'
  type: float
NODE_FLOW_IN_CURRENT_RANGE_COLOR:
  def:
    - [0.68235, 0.0039, 0.4941, 0.55]
  type: table
  cmt: At current motorization level
NODE_FLOW_IN_HALF_RANGE_COLOR:
  def:
    - [0.9686, 0.4078, 0.6314, 0.6]
  type: table
  cmt: At Half Motorization, if currently set to less than that
NODE_FLOW_IN_FULL_RANGE_COLOR:
  def:
    - [0.9843, 0.7059, 0.7255, 0.4]
  type: table
  cmt: At Full Motorization, if currently set to less than that
RAILWAY_ICON_SHIFT:
  def:
    - [0.0, 0.0, 0.0]
  type: table
SUPPLY_ICON_SHIFT:
  def:
    - [0.0, 0.0, 0.0]
  type: table
SUPPLY_ICON_SWITCH:
  def: '200'
  type: int
SUPPLY_ICON_CUTOFF:
  def: '900.0'
  type: float
  cmt: total supply icon cutoff distance for all
SUPPLY_ICON_UNUSED_CUTOFF:
  def: '400.0'
  type: float
  cmt: where we stop showing unused nodes
SUPPLY_ICON_NUMBERS_CUTOFF:
  def: '400.0'
  type: float
  cmt: where we stop showing numbers on hubs (ignored for selected and problem hubs)
SUPPLY_ICON_OK_CUTOFF:
  def: '750.0'
  type: float
  cmt: where we stop showing nodes with no issues, e.g non-red
SUPPLY_ICON_DISCONNECTED_CUTOFF:
  def: '500.0'
  type: float
  cmt: where we stop showing disconnected nodes
SUPPLY_ICON_END_CUTOFF:
  def: '200.0'
  type: float
  cmt: where we stop showing line end icons
RAILWAY_ICON_CUTOFF:
  def: '900.0'
  type: float
SUPPLY_SELECTED_NODE_COLOR:
  def:
    - [0.0, 1.0, 1.0, 1.0]
  type: table
SUPPLY_CAPITAL_COLOR:
  def:
    - [1.0, 0.7, 0.0, 1.0]
  type: table
SUPPLY_NAVAL_NODE_COLOR:
  def:
    - [0.1, 0.6, 0.8, 1.0]
  type: table
SUPPLY_LAND_NODE_COLOR:
  def:
    - [0.5, 0.8, 0.5, 1.0]
  type: table
SUPPLY_CONSUMER_ARROW_HEIGHT_TO_LEN:
  def: '0.1'
  type: float
SUPPLY_CONSUMER_ARROW_HEIGHT_MAX:
  def: '4.0'
  type: float
SUPPLY_UNIT_COUNTER_SHOW_THRESHOLD:
  def: '0.5'
  type: float
  cmt: At what supply threshold will the normal crate be shown on unit counters
SUPPLY_UNIT_COUNTER_LOW_THRESHOLD:
  def: '0.35'
  type: float
  cmt: At what supply threshold will the orange crate be shown on unit counters
SUPPLY_UNIT_COUNTER_VERY_LOW_THRESHOLD:
  def: '0.2'
  type: float
  cmt: At what supply threshold will the red crate with ! will be shown on unit counters
COUP_GREEN:
  def:
    - [0.0, 1.0, 0.0, 1.0]
  type: table
COUP_RED:
  def:
    - [1.0, 0.0, 0.0, 1.0]
  type: table
FRIEND_COLOR:
  def:
    - [0.7, 0.9, 0.7]
  type: table
ENEMY_COLOR:
  def:
    - [1.0, 0.7, 0.7]
  type: table
NEUTRAL_COLOR:
  def:
    - [1.0, 1.0, 1.0]
  type: table
COUNTRY_COLOR_HUE_MODIFIER:
  def: '0.0'
  type: float
COUNTRY_COLOR_SATURATION_MODIFIER:
  def: '0.6'
  type: float
COUNTRY_COLOR_BRIGHTNESS_MODIFIER:
  def: '0.8'
  type: float
COUNTRY_UI_COLOR_HUE_MODIFIER:
  def: '0.0'
  type: float
COUNTRY_UI_COLOR_SATURATION_MODIFIER:
  def: '1.0'
  type: float
COUNTRY_UI_COLOR_BRIGHTNESS_MODIFIER:
  def: '1.0'
  type: float
COMMANDGROUP_PRESET_COLORS_HSV:
  def:
    - [90.0/360.0, 0.95, 0.86]
    - [60.0/360.0, 0.95, 0.86]
    - [30.0/360.0, 0.95, 0.86]
    - [00.0/360.0, 0.95, 0.86]
    - [330.0/360.0, 0.95, 0.86]
    - [300.0/360.0, 0.95, 0.86]
    - [270.0/360.0, 0.95, 0.86]
    - [240.0/360.0, 0.95, 0.86]
    - [210.0/360.0, 0.95, 0.86]
    - [180.0/360.0, 0.95, 0.86]
  type: table
CAMERA_OUTSIDE_MAP_DISTANCE_TOP:
  def: '200.0'
  type: float
CAMERA_OUTSIDE_MAP_DISTANCE_BOTTOM:
  def: '200.0'
  type: float
CAMERA_ZOOM_SPEED:
  def: '50'
  type: int
CAMERA_ZOOM_KEY_SCALE:
  def: '0.02'
  type: float
CAMERA_ZOOM_SPEED_DISTANCE_MULT:
  def: '6.0'
  type: float
  cmt: Zoom speed multiplier. When camera is max zoome out, the zooming in speed will
    get 100% of CAMERA_ZOOM_SPEED_DISTANCE_MULT zooming speed.
ORDERS_MOUSE_INTERSECT_DISTANCE_MULT:
  def: '2.6'
  type: float
  cmt: For balancing the collision distance with painted arrows and fronts.
FRONTS_MOUSE_INTERSECT_DISTANCE_MULT:
  def: '6.6'
  type: float
  cmt: For balancing the collision distance with painted arrows and fronts.
MOVE_ORDERS_MOUSE_INTERSECT_DISTANCE_MULT:
  def: '0.5'
  type: float
  cmt: For balancing the collision distance with painted arrows and fronts.
TRADE_ROUTE_INTERSECT_DISTANCE_MULT:
  def: '10.0'
  type: float
  cmt: For balancing the collision distance with painted arrows and trade routes.
RAILWAY_INTERSECT_DISTANCE_MULT:
  def: '3.0'
  type: float
  cmt: For balancing the collision distance with painted arrows and railways.
MINIMUM_PROVINCE_SIZE_IN_PIXELS:
  def: '8'
  type: int
  cmt: Provinces that are smaller than that are just making the game unplayable. It
    doesn't affect the game, just informs in the error.log
NATIONAL_FOCUS_SHINE_DISTANCE_SCALE:
  def: '0.03'
  type: float
NATIONAL_FOCUS_PULSE_BASE:
  def: '10.0'
  type: float
NATIONAL_FOCUS_PULSE_RANDOM:
  def: '10.0'
  type: float
POLITICAL_GRID_SMALL_BOX_LIMIT:
  def: '6'
  type: int
  cmt: Limit for gridbox in political view before it will be replaced with extended
    gridbox
SETUP_SPIRIT_GRID_BOX_LIMIT:
  def: '3'
  type: int
  cmt: Limit for gridbox in game setup before it will be replaced with extended gridbox
POLITICAL_PULSE_BASE:
  def: '10.0'
  type: float
POLITICAL_PULSE_RANDOM:
  def: '10.0'
  type: float
STRATEGIC_REGION_ZOOM_HEIGHT:
  def: '300.0'
  type: float
  cmt: zooming to a strategic region will make you zoom this further from map
ARROW_PARADROP_HEIGHT_TO_LEN:
  def: '0.3'
  type: float
ARROW_PARADROP_HEIGHT_MAX:
  def: '11.0'
  type: float
ARROW_MIN_TEXT_POINTS_LIMIT:
  def: '10'
  type: int
  cmt: Amount of points when arrow gets first detailed text
ARROW_EXT_TEXT_POINTS_LIMIT:
  def: '20'
  type: int
  cmt: Amount of points when arrow gets extended detailed text
ARMY_DEFENSIVE_LINE_BUTTON_SIZE:
  def: '0.7'
  type: float
  cmt: The size of the "edit" button drawn at the endings of the def.lines (for army)
ARMY_GROUP_DEFENSIVE_LINE_BUTTON_SIZE:
  def: '0.9'
  type: float
  cmt: The size of the "edit" button drawn at the endings of the def.lines (for army
    group)
SHOW_FOREIGN_SUPPLY_BELOW:
  def: '300.0'
  type: float
  cmt: Below this camera height all supply icons will be shown
SHOW_ONLY_PATH_ABOVE:
  def: '500.0'
  type: float
  cmt: Above this only supply icons in the currently shown path are shown
ACCLIMATIZATION_CAMO_SHOW_AT:
  def: '0.5'
  type: float
  cmt: The moment at which the division gains enough acclimatization to change it's
    model to the camouflage one.
ACCLIMATIZATION_CAMO_SHOW_WHEN_IN_STATE:
  def: '0.2'
  type: float
  cmt: The troops camouflage can swap (to the one from acclim.) not only when
    snow/desert is in the location we are in, but also when % of provinces in current
    state has snow/desert.
INTEL_NETWORK_VALID_TARGET_STRIPE_COLOR:
  def:
    - [0.1, 0.5, 0.8, 1.0]
  type: table
  cmt: Color of the stripes of painted over a valid state to start building an intel
    network
INTEL_NETWORK_VALID_COUNTRY_TARGET_STRIPE_COLOR:
  def:
    - [0.1, 0.8, 0.5, 0.5]
  type: table
  cmt: Color of the stripes painted over valid countries
OCCUPATION_RESISTANCE_NON_INITIALIZED_COLOR:
  def:
    - [1.0, 1.0, 1.0, 0.05]
  type: table
  cmt: player owned state color with no resistance
OCCUPATION_RESISTANCE_MAP_MODE_COLORS:
  def:
    - [0.0, 0.0, 1.0, 0.0, 0.0]
    - [0.0, 1.0, 1.0, 0.0, 0.0]
    - [1.0, 1.0, 1.0, 0.0, 0.1]
    - [30.0, 1.0, 1.0, 0.0, 0.3]
    - [100.0, 1.0, 0.0, 0.0, 0.3]
  type: table
OCCUPATION_COMPLIANCE_MAP_MODE_COLORS:
  def:
    - [0.0, 0.3, 0.6, 0.6, 0.05]
    - [0.0, 0.3, 0.7, 1.0, 0.05]
    - [10.0, 0.3, 0.7, 1.0, 0.2]
    - [50.0, 0.3, 0.7, 1.0, 0.3]
    - [100.0, 0.3, 0.9, 1.0, 0.5]
  type: table
INTEL_LEDGER_ARMY_FORT_LEVEL_COLORS:
  def:
    - [0.0, 0.3, 0.3, 0.3, 0.2]
    - [0.0, 0.7, 0.7, 0.2, 0.3]
    - [1.0, 0.7, 0.2, 0.2, 0.5]
  type: table
INTEL_LEDGER_NAVAL_FORT_LEVEL_COLORS:
  def:
    - [0.0, 0.3, 0.3, 0.3, 0.2]
    - [0.0, 0.7, 0.7, 0.2, 0.3]
    - [1.0, 0.7, 0.2, 0.2, 0.5]
  type: table
TEMPERATURE_MAP_MODE_COLORS:
  def:
    - [-35.0, 0.0, 0.0, 0.5, 1.0]
    - [-25.0, 0.0, 0.0, 1.0, 1.0]
    - [-10.0, 0.0, 0.7, 1.0, 1.0]
    - [0.0, 0.0, 1.0, 0.45, 0.45]
    - [15.0, 1.0, 1.0, 0.0, 1.0]
    - [25.0, 1.0, 0.65, 0.0, 1.0]
    - [30.0, 1.0, 0.0, 0.0, 1.0]
    - [35.0, 0.5, 0.0, 0.0, 1.0]
  type: table
RAILWAY_GUN_ASSIGNMENTS_MAP_MODE_COLORS:
  def:
    - [0.0, 1.0, 0.0, 0.0, 1.0]
    - [0.25, 1.0, 0.65, 0.0, 1.0]
    - [0.75, 1.0, 1.0, 0.0, 1.0]
    - [1.0, 0.0, 1.0, 0.45, 0.45]
  type: table
INTEL_LEDGER_NAVY_REGION_COLOR_WITH_MISSION:
  def:
    - [0.7, 0.7, 0.7, 0.9]
  type: table
INTEL_LEDGER_NAVY_REGION_COLOR_WITH_MISSION_AND_TASKFORCES_IN_REGION:
  def:
    - [0.8, 0.8, 0.4, 0.9]
  type: table
INTEL_LEDGER_AIR_REGION_COLOR:
  def:
    - [0.8, 0.8, 0.4, 0.9]
  type: table
INTEL_LEDGER_GRAPH_RED:
  def:
    - [1.0, 0.0, 0.0, 1.0]
  type: table
INTEL_LEDGER_GRAPH_GREEN:
  def:
    - [0.0, 1.0, 0.0, 1.0]
  type: table
RAID_SOURCE_MAP_STRIPES_COLOR:
  def:
    - [0.0, 1.0, 1.0, 0.4]
  type: table
RAID_SOURCE_MAP_STRIPES_HOVERED_COLOR:
  def:
    - [0.3, 1.0, 1.0, 0.7]
  type: table
RAID_ARROW_BALLISTIC_SHAPE:
  def: '0.02'
  type: float
  cmt: Higher value = curved trajectories, lower value = flat trajectories
RAID_ARROW_BALLISTIC_MAX_HEIGHT:
  def: '30'
  type: int
  cmt: Maximum altitude reached by ballistic trajectories
RAID_ARROW_BALLISTIC_MAX_SEGMENT_LENGTH:
  def: '1'
  type: int
  cmt: Maximum length of arrow segment (less = smoother curve)
RAID_ARROW_BALLISTIC_MAX_SEGMENTS:
  def: '100'
  type: int
  cmt: Max segments per arrow (overrides max segment length)
RAID_ARROW_AIR_HEIGHT:
  def: '10.0'
  type: float
  cmt: Highest altitude above max(source, target)
RAID_ARROW_AIR_SLOPE_SOURCE_STEEPNESS:
  def: '0.2'
  type: float
  cmt: Higher value = steeper angle [0,1]
RAID_ARROW_AIR_SLOPE_SOURCE_LENGTH:
  def: '50.0'
  type: float
  cmt: Higher value = more time to reach the highest altitude
RAID_ARROW_AIR_SLOPE_TARGET_STEEPNESS:
  def: '0.2'
  type: float
  cmt: Same as above but for the target
RAID_ARROW_AIR_SLOPE_TARGET_LENGTH:
  def: '0.0'
  type: float
  cmt: Same as above but for the target (a value of zero means it ends above the target)
RAID_ARROW_AIR_MAX_SEGMENT_LENGTH:
  def: '1'
  type: int
  cmt: Maximum length of arrow segment (less = smoother curve)
RAID_ARROW_AIR_MAX_SEGMENTS:
  def: '100'
  type: int
  cmt: Max segments per arrow (overrides max segment length)
RAID_ARROW_NAVAL_SUBDIVISIONS:
  def: '20'
  type: int
  cmt: Number of subdivisions for the path spline (more = smoother, but slower to
    render)
RAID_ARROW_NAVAL_SHARP_TURN_SMOOTHNESS:
  def: '0.10'
  type: float
  cmt: Amount of smoothness that is applied to smooth out sharp turns (0 = off)
RAID_ARROW_NAVAL_USE_MIDPOINTS:
  def: 'true'
  type: bool
  cmt: Whether to use midpoints between provinces to build the path
RAID_ARROW_LAND_SUBDIVISIONS:
  def: '20'
  type: int
  cmt: Number of subdivisions for the path spline (more = smoother, but slower to
    render)
RAID_ARROW_LAND_SHARP_TURN_SMOOTHNESS:
  def: '0.10'
  type: float
  cmt: Amount of smoothness that is applied to smooth out sharp turns (0 = off)
RAID_ARROW_LAND_USE_MIDPOINTS:
  def: 'true'
  type: bool
  cmt: Whether to use midpoints between provinces to build the path
RAID_UNIT_ENTITY_BASE_SCALE:
  def: '2.0'
  type: float
  cmt: Base scale of the raid unit entity used to show the progress of the raid (can be
    further modifier in raid script)
RAID_UNIT_ENTITY_OFFSET:
  def:
    - [0.0, 0.0, 0.0]
  type: table
  cmt: Raid entity offset from the arrow spline position
RAID_UNIT_SECOND_STAGE_PROGRESS:
  def: '0.33'
  type: float
  cmt: Specifies raid progress value on [0,1] where second stage is activated
RAID_UNIT_THIRD_STAGE_PROGRESS:
  def: '0.66'
  type: float
  cmt: Specifies raid progress value on [0,1] where third stage is activated
DEFAULT_NUDGE_FLOATING_HARBOR_DIST:
  def: '7.0'
  type: float
  cmt: Default distance of floating harbors from the coast in pixels, for nudger
RAID_MAP_ICON_DRAW_DISTANCE_MIN:
  def: '10.0'
  type: float
  cmt: Below this distance, raid map icons are hidden
RAID_MAP_ICON_DRAW_DISTANCE_MAX:
  def: '500.0'
  type: float
  cmt: Above this distance, raid map icons are hidden in normal map modes
RAID_MAP_ICON_MAX_DRAW_DISTANCE_IN_RAID_MAP_MODE:
  def: '1600.0'
  type: float
  cmt: Above this distance, raid map icons are hidden in raid map mode
RAID_TARGET_ZOOM_HEIGHT:
  def: '200.0'
  type: float
  cmt: The height for the map carmera to zoom in to a raid target
NAVAL_DOMINANCE_ICON_MAX_DRAW_DISTANCE:
  def: '1000.0'
  type: float
  cmt: The camera distance at which naval dominance map icons are hidden
FACTION_PING_MAP_NONE_SELECT_COLOR:
  def:
    - [0.1, 0.1, 0.3, 0.98]
  type: table
  cmt: Color when you have non selected
FACTION_PING_MAP_AVAILABLE_COLOR:
  def:
    - [0.3, 0.3, 0.3, 0.5]
  type: table
  cmt: Available region color
FACTION_PING_MAP_UNAVAILABLE_COLOR:
  def:
    - [0.1, 0.1, 0.3, 1.0]
  type: table
  cmt: Unavailable region color
FACTION_PING_MAP_COLOR:
  def:
    - [0.99, 0.99, 0.99, 0.05]
  type: table
  cmt: Selected region color
FACTION_PING_MAP_ALREADY_ASSIGNED_COLOR:
  def:
    - [0.5, 0.5, 0.75, 0.15]
  type: table
  cmt: Already assigned to another theater color
FACTION_PING_MAP_GRADIENT:
  def: '150'
  type: int
  cmt: Selected region distance gradient
```
