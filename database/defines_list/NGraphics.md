---
domain: defines_list
concept: NGraphics
version: 1.14+
requires: [defines]
relates: [graphics]
---

```yaml
COUNTER_MODE_ALLEGIANCE_OURS:
  def: '{ 0.32, 0.71, 0.39, 1.0 }'
  type: array
COUNTER_MODE_ALLEGIANCE_ENEMY:
  def: '{ 0.91, 0.3, 0.3, 1.0 }'
  type: array
MAX_NUMBER_OF_TEXTURES:
  def: '10000'
  type: int
  cmt: increase if you have more than this textures
MAX_TRAIN_WAGON_COUNT:
  def: '6'
  type: int
RAILWAY_BRIDGE_LARGE_ENTITY:
  def: '"bridge_railway_large_entity"'
  type: str
RAILWAY_BRIDGE_Y_OFFSET:
  def: '0.6'
  type: float
  cmt: Railway bridges are offset by this amount vertically from the map
RAILWAY_BRIDGE_LARGE_WIDTH:
  def: '4.5'
  type: float
  cmt: Railways will have straight segments of this length for large bridges
RAILWAY_BRIDGE_GAP_LARGE_WIDTH:
  def: '2.6'
  type: float
  cmt: Railways will have gaps of this length for large bridges
TUNNELBANA_TIMETABLE:
  def: '{ 9200, 12000 }'
  type: array
  cmt: Frequency range in milliseconds for regular train service. Adjust this if changing
    speed to avoid LONGTRAIN
MESH_POPUP_SCALE_UP_SPEED:
  def: '5.0'
  type: float
SHIP_POPUP_SCALE_DOWN_SPEED:
  def: '4.1'
  type: float
SHIP_IN_PORT_SCALE:
  def: '0.25'
  type: float
CITY_SPRAWL_SHRINK_DISTANCE:
  def: '220.0'
  type: float
  cmt: Start shrinking at this distance
PROVINCE_NAME_DRAW_DISTANCE:
  def: '500.0'
  type: float
  cmt: Remove province names beyond this distance
DIRECTION_POINTER_INTERPOLATION_SPEED:
  def: '0.275'
  type: float
  cmt: How fast the arrow is interpolating
DIRECTION_POINTER_SCREEN_AREA_MIN:
  def: '0.91'
  type: float
  cmt: The moment when the arrow starts getting closer to the target before it snaps.
DIRECTION_POINTER_SIZE_MAX:
  def: '10.0'
  type: float
LIGHT_DIRECTION_X:
  def: '-1.0'
  type: float
LIGHT_DIRECTION_Z:
  def: '0.5'
  type: float
LIGHT_SHADOW_DIRECTION_Y:
  def: '-8.0'
  type: float
LIGHT_HDR_RANGE:
  def: '1.0'
  type: float
PROVINCE_BORDER_FADE_NEAR:
  def: '200'
  type: int
STATE_BORDER_FADE_NEAR:
  def: '400'
  type: int
LAND_UNIT_MOVEMENT_SPEED:
  def: '12'
  type: int
ARROW_MOVEMENT_SPEED:
  def: '2'
  type: int
TRADEROUTE_SMOOTHNESS:
  def: '0.65'
  type: float
SUPPLYFLOW_SMOOTHNESS:
  def: '0.25'
  type: float
SNAPPED_OFF_FRONT_SMOOTHNESS:
  def: '0.5'
  type: float
ROOT_FRONT_SMOOTHNESS:
  def: '0.5'
  type: float
ROOT_FRONT_OFFSET:
  def: '1.5'
  type: float
  cmt: How far the defensive line is offset from the front.
ROOT_FRONT_MAX_INTERSECTION_TESTS_ORDER:
  def: '25'
  type: int
  cmt: How many points before the current one to check for intersections against (optimization)
ORDER_FRONT_SMOOTHNESS:
  def: '0.5'
  type: float
ORDER_MOVE_SMOOTHNESS:
  def: '0.99'
  type: float
UNIT_TURN_SPEED:
  def: '3'
  type: int
BORDER_COLOR_SELECTION_STATE_G:
  def: '0.62'
  type: float
BORDER_COLOR_SELECTION_STATE_A:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_SUPPLY_AREA_G:
  def: '0.2'
  type: float
BORDER_COLOR_SELECTION_SUPPLY_AREA_A:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_ADJACENCY_RULE_AREA_G:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_ADJACENCY_RULE_AREA_A:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_BUILDING_AREA_G:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_BUILDING_AREA_A:
  def: '1.0'
  type: float
BORDER_COLOR_SELECTION_PROVINCE_G:
  def: '0.8'
  type: float
BORDER_COLOR_SELECTION_PROVINCE_A:
  def: '1.0'
  type: float
BORDER_COLOR_TUTORIAL_HIGHLIGHT_R:
  def: '0.0'
  type: float
BORDER_COLOR_TUTORIAL_HIGHLIGHT_B:
  def: '0.75'
  type: float
BORDER_COLOR_DEMILITARIZED_R:
  def: '1.0'
  type: float
BORDER_COLOR_DEMILITARIZED_B:
  def: '0.0'
  type: float
BORDER_COLOR_BORDER_CONFLICT_EDGE_R:
  def: '1.0'
  type: float
BORDER_COLOR_BORDER_CONFLICT_EDGE_B:
  def: '0.0'
  type: float
BORDER_COLOR_BORDER_CONFLICT_NON_EDGE_R:
  def: '0.7'
  type: float
BORDER_COLOR_BORDER_CONFLICT_NON_EDGE_B:
  def: '0.0'
  type: float
DRAW_REFRACTIONS_CUTOFF:
  def: '250'
  type: int
DRAW_SHADOWS_FADE_LENGTH:
  def: '50'
  type: int
DRAW_FOW_FADE_LENGTH:
  def: '350'
  type: int
GRADIENT_BORDERS_FIELD_COUNTRY_LOW:
  def: '300.0'
  type: float
  cmt: country area in sum of pixels ...
GRADIENT_BORDERS_THICKNESS_COUNTRY_LOW:
  def: '5.0'
  type: float
  cmt: thickness in pixels
GRADIENT_BORDERS_THICKNESS_COUNTRY_HIGH:
  def: '25.0'
  type: float
GRADIENT_BORDERS_THICKNESS_RESISTANCE:
  def: '5.0'
  type: float
GRADIENT_BORDERS_THICKNESS_SUPPLY_AREA_A:
  def: '2.0'
  type: float
GRADIENT_BORDERS_THICKNESS_STRATEGIC_REGIONS:
  def: '150.0'
  type: float
GRADIENT_BORDERS_THICKNESS_DIPLOMACY_ON_INTEL_LEDGER:
  def: '3.0'
  type: float
GRADIENT_BORDERS_THICKNESS_PEACE_CONFERENCE_B:
  def: '6.0'
  type: float
  cmt: increasing transparency up to 100% when at B
GRADIENT_BORDERS_OUTLINE_CUTOFF_DIPLOMACY:
  def: '0.973'
  type: float
GRADIENT_BORDERS_OUTLINE_CUTOFF_STATE:
  def: '0.973'
  type: float
GRADIENT_BORDERS_OUTLINE_CUTOFF_STRATEGIC_REGIONS:
  def: '0.98'
  type: float
GRADIENT_BORDERS_OUTLINE_CUTOFF_FACTIONS:
  def: '0.973'
  type: float
GRADIENT_BORDERS_OUTLINE_CUTOFF_PEACE_CONFERENCE:
  def: '0.973'
  type: float
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_STATE:
  def: '0.4'
  type: float
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_STRATEGIC_REGIONS:
  def: '1.0'
  type: float
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_FACTIONS:
  def: '0.0'
  type: float
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_INTEL_LEDGER:
  def: '0.2'
  type: float
GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_DIPLOMACY_ON_INTEL_LEDGER:
  def: '1.0'
  type: float
GRADIENT_BORDERS_ACTIVATE_FOR_PEACE_CONFERENCE:
  def: 'false'
  type: bool
GRADIENT_BORDERS_OPTIMIZATION_RANGE:
  def: '30.0'
  type: float
  cmt: smaller value = faster gradient borders but may have artifacts on large provinces
    (value to balance)
STRATEGIC_AIR_COLOR_BAD:
  def: '{ 0.8, 0, 0, 1 }'
  type: array
  cmt: rgb
STRATEGIC_AIR_COLOR_AVERAGE:
  def: '{ 0.8, 0.8, 0, 1 }'
  type: array
STRATEGIC_AIR_COLOR_GOOD_WHILE_HIGHLIGHTING_HOLD:
  def: '{ 0, 0.8, 0, 1 }'
  type: array
STRATEGIC_AIR_COLOR_NEUTRAL_WHILE_HIGHLIGHTING_HOLD:
  def: '{ 140.0/255, 131.0/255, 119.0/255, 1 }'
  type: array
STRATEGIC_NAVY_COLOR_ON_HOLD:
  def: '{ 0.2, 0.5, 0.6, 0.5 }'
  type: array
  cmt: zones with only hold mission
STRATEGIC_NAVY_COLOR_BAD:
  def: '{ 0.8, 0, 0, 1 }'
  type: array
  cmt: zones has missions with bad suppremacy
STRATEGIC_NAVY_COLOR_AVERAGE:
  def: '{ 0.8, 0.8, 0, 1 }'
  type: array
  cmt: zones has missions with average suppremacy
STRATEGIC_NAVY_COLOR_BAD_WHILE_HIGHLIGHTING_HOLD:
  def: '{ 0.7, 0.0, 0.4, 0.5 }'
  type: array
  cmt: zones has missions with bad suppremacy on highlighted regions with a hold mission
    selected
STRATEGIC_NAVY_COLOR_AVERAGE_WHILE_HIGHLIGHTING_HOLD:
  def: '{ 0.5, 0.5, 0.6, 1 }'
  type: array
  cmt: zones has missions with average suppremacy on highlighted regions with a hold
    mission selected
RESISTANCE_COLOR_GOOD:
  def: '{ 0.8, 0.8, 0, 0.3 }'
  type: array
  cmt: rgba
RESISTANCE_COLOR_BAD:
  def: '{ 0.8, 0, 0, 0.9 }'
  type: array
CONSTRUCTION_CONVERSION_IN_PROGRESS_COLOR:
  def: '{ 0.3, 0.3, 0.9, 0.1 }'
  type: array
ALLIED_BATTLEPLANS_COLOR:
  def: '{ 0.3, 0.4, 1.0, 1 }'
  type: array
DEFENSIVE_PING_CIRCLE_COLOR:
  def: '{ 0.4, 0.55, 0.66 }'
  type: array
DAY_NIGHT_FEATHER:
  def: '0.024'
  type: float
  cmt: Feather value between complete darkness and the day (see also in shader daynight.fxh)
NORTH_POLE_OFFSET:
  def: '0.93'
  type: float
COUNTRY_FLAG_TEX_HEIGHT:
  def: '52'
  type: int
COUNTRY_FLAG_MEDIUM_TEX_WIDTH:
  def: '41'
  type: int
COUNTRY_FLAG_MEDIUM_TEX_MAX_SIZE:
  def: '1024'
  type: int
  cmt: Tweak dependly on amount of countries. Must be power of 2. No more then 2048.
COUNTRY_FLAG_SMALL_TEX_HEIGHT:
  def: '7'
  type: int
VICTORY_POINT_LEVELS:
  def: '3'
  type: int
VICTORY_POINT_MAP_ICON_CAPITAL_CUTOFF_MAX:
  def: '1000.0'
  type: float
  cmt: Capitals are special snowflakes, they need their own number
VICTORY_POINT_MAP_ICON_TEXT_CUTOFF_MIN:
  def: '100.0'
  type: float
  cmt: Min range for victory point text
VICTORY_POINT_MAP_ICON_DOT_CUTOFF_MIN:
  def: '100.0'
  type: float
  cmt: Min range for victory point dot
VICTORY_POINT_MAP_ICON_MAX_VICTORY_POINTS_FOR_PERCENT:
  def: '22'
  type: int
  cmt: Default max value for point on the above range. It doesn't matter much if the
    VP value exceeds this, it'll be treated as max.
NAVALBASE_ICON_DISTANCE_CUTOFF:
  def: '900'
  type: int
  cmt: 1300, -- At what distance naval bases are hidden
RESOURCE_MAP_ICON_TEXT_CUTOFF:
  def: '800'
  type: int
  cmt: At what camera distance the resource name/amount text disappears.
RESISTANCE_MAP_ICON_DISTANCE_CUTOFF:
  def: '1200'
  type: int
  cmt: At what camera distance the resistance/compliance map icons are hidden
CAPITAL_ICON_CUTOFF:
  def: '1100'
  type: int
  cmt: At what camera distance capital icons disappears
SHIPS_DISTANCE_CUTOFF:
  def: '240'
  type: int
UNITS_ICONS_DISTANCE_CUTOFF:
  def: '900'
  type: int
ADJACENCY_RULE_DISTANCE_CUTOFF:
  def: '1700'
  type: int
PROV_CONSTRUCTION_ICON_DISTANCE_CUTOFF:
  def: '400'
  type: int
DECISION_MAP_ICON_DISTANCE_CUTOFF:
  def: '1000'
  type: int
NAVAL_MISSION_TASK_FORCES_GROUP_BY_ALLEGIANCE_CUTOFF:
  def: '500'
  type: int
NAVAL_MINES_DISTANCE_CUTOFF:
  def: '800'
  type: int
PEACE_CONFERENCE_MAP_ICON_DISTANCE_CUTOFF:
  def: '500'
  type: int
NAVAL_MINES_CLUMP_NEAR_TERRITORY:
  def: '25'
  type: int
  cmt: Higher chance to spawn 3d naval mine near our territory
MAP_ICONS_GROUP_CAM_DISTANCE:
  def: '90.0'
  type: float
  cmt: camera distance at which the icons begin to group up
MAP_ICONS_STRATEGIC_GROUP_CAM_DISTANCE:
  def: '350'
  type: int
  cmt: second camera distance at which the icons begin to group up
MAP_ICONS_STATE_HUGE:
  def: '100'
  type: int
MAP_ICONS_GROUP_SPLIT_SELECTED_LIMIT:
  def: '12'
  type: int
  cmt: Maximum number of units selected that will cause icon stacks to split
MAP_ICONS_COARSE_COUNTRY_GROUPING_DISTANCE_STRATEGIC:
  def: '350'
  type: int
  cmt: Distance at which icon grouping becomes very coarse and merges different types
    of units for strategic mapmodes
RIVER_FADE_TO:
  def: '3.0'
  type: float
TOOLTIP_SHOW_DELAY:
  def: '0.05'
  type: float
  cmt: How long before showing delayed tooltip.
INTEL_LEDGER_CIVILIAN_ICON_STATE_CUTOFF:
  def: '250.0'
  type: float
RAILWAY_CAMERA_CUTOFF:
  def: '200.0'
  type: float
  cmt: railways are cut off above this camera height
DIVISION_NAMES_GROUP_MAX_TOOLTIP_ENTRIES:
  def: '15'
  type: int
  cmt: Max entries to display the names in the tooltip, when mouse over the division-names-group
    in the division template designer.
WEATHER_DISTANCE_CUTOFF:
  def: '1500'
  type: int
  cmt: At what distance weather effects are hidden
WEATHER_ZOOM_IN_CUTOFF:
  def: '358'
  type: int
  cmt: At what distance weather effects are faded out the most when zooming in
WEATHER_ZOOM_IN_FADE_FACTOR:
  def: '0.0'
  type: float
  cmt: How much the weather effects should fade out when maximum zoomed in
WEATHER_PLAYBACK_RATE_CUTOFF:
  def: '500'
  type: int
  cmt: Playback rate maximum distance
POSTEFFECT_PER_PROVINCE_MIN_SNOW:
  def: '0.1'
  type: float
POSTEFFECT_TOTAL_MIN_SNOW:
  def: '0.0'
  type: float
POSTEFFECT_FEATHER_MIN_DISTANCE:
  def: '300.0'
  type: float
POSTEFFECT_FEATHER_AT_MIN:
  def: '0.03'
  type: float
LAND_COMBAT_BALANCED_COLOR:
  def: '{ 1.0, 1.0, 0.0, 1.0 }'
  type: array
LAND_COMBAT_WINNING_COLOR:
  def: '{ 0.0, 1.0, 0.0, 1.0 }'
  type: array
BLOOM_SCALE:
  def: '0.9'
  type: float
  cmt: BLOOM_WIDTH = 1.0, -- night
EMISSIVE_BLOOM_STRENGTH:
  def: '1.0'
  type: float
  cmt: BRIGHT_THRESHOLD = 0.9, -- night
MAX_HDR_ADJUSTMENT:
  def: '1.0'
  type: float
  cmt: 0.8 0.8 jätte högt värde så ser du bra trots att du står inuti solen och tittar.
TONE_MAP_MIDDLE_GREY:
  def: '0.5'
  type: float
  cmt: '0.7'
MOON_HEIGHT:
  def: '600'
  type: int
  cmt: higher means softer shadows and more intense light
MOON_HEIGHT_WATER:
  def: '550'
  type: int
  cmt: higher means softer shadows and more intense light
MOON_LATITUDE:
  def: '0'
  type: int
  cmt: NOT USED
SECOND_MOON_LATITUDE:
  def: '100'
  type: int
  cmt: Used to put a "fake" sun/moon on the other side of the globe to hide the seem
    that would otherwise appear there
AMBIENT_LIGHT_POS_X:
  def: '{ 0.2, 0.2, 0.2 }'
  type: array
  cmt: hsv color ambient light right
AMBIENT_LIGHT_POS_Y:
  def: '{ 0.0, 0.0, 0.0 }'
  type: array
  cmt: kills everything
AMBIENT_LIGHT_POS_Z:
  def: '{ 0.6, 0.2, 0.924 }'
  type: array
  cmt: top
SUN_DIFFUSE_COLOR:
  def: '{ 0.14, 0.0, 1.0 }'
  type: array
SUN_SPECULAR_INTENSITY:
  def: '1.0'
  type: float
MOON_INTENSITY:
  def: '2.5'
  type: float
TREE_FADE_NEAR:
  def: '250.0'
  type: float
TRADE_ROUTE_NUM_CONVOYS_SCALE_FACTOR:
  def: '0.3'
  type: float
TRADE_ROUTE_CONVOY_SPEED:
  def: '0.6'
  type: float
TRADE_ROUTE_CONVOY_ROUTE_OFFSET:
  def: '0.5'
  type: float
SHIP_IN_MISSION_TURN_RADIUS:
  def: '5.0'
  type: float
SHIP_IN_MISSION_SCALE:
  def: '0.6'
  type: float
TRADE_ROUTE_MAX_LINES:
  def: '6'
  type: int
TRADE_ROUTE_REGIONAL_BAD_EFFICIENCY_THRESHOLD:
  def: '0.9'
  type: float
TRADE_ROUTE_BAD_EFFICIENCY_HOTSPOT_COLOR:
  def: '{ 1.0, 0.0, 0.0, 0.75 }'
  type: array
TRADE_ROUTE_SUPPLIES_TRANSFER_COLOR:
  def: '{ 1.0, 1.0, 1.0, 0.75 }'
  type: array
TRADE_ROUTE_RESOURCE_IMPORT_COLOR:
  def: '{ 0.2, 0.9, 1.0, 0.75 }'
  type: array
TRADE_ROUTE_LEND_LEASE_IMPORT_COLOR:
  def: '{ 0.5, 1.0, 0.0, 0.75 }'
  type: array
TRAIT_GRID_COLUMN_OFFSET:
  def: '3'
  type: int
TRAIT_GRID_ROW_SHIFT:
  def: '48'
  type: int
TRAIT_LINE_NON_ASSIGNED_COLOR:
  def: '{ 0.67, 0.75, 0.93 }'
  type: array
  cmt: Color for parent dependency lines when the parent is not assigned assigned.
TRAIT_INVALID_FOR_ASSIGNMENT_COLOR:
  def: '{ 0.8, 0.3, 0.3 }'
  type: array
RAILWAY_MAP_ARROW_THIN_LEVEL_THRESHOLD:
  def: '1'
  type: int
  cmt: Railway level 1 uses thin map arrow in supply map mode
RAILWAY_MAP_ARROW_THICK_LEVEL_THRESHOLD:
  def: '5'
  type: int
  cmt: Railway level 4-5 uses thick map arrow in supply map mode
RAILWAY_MAP_ARROW_COLOR_CONSTRUCTION:
  def: '{ 1.0, 0.8, 0.0, 1.0 }'
  type: array
  cmt: orange, railways that are currently under construction
RAILWAY_MAP_ARROW_COLOR_CONSTRUCTION_INVALID:
  def: '{ 1.0, 0.0, 0.0, 1.0 }'
  type: array
  cmt: red, in constructionmode, railways that are invalid to build
RAILWAY_MAP_ARROW_COLOR_HIGHLIGHTED_DAMAGED:
  def: '{ 1.0, 1.0, 0.2, 1.0 }'
  type: array
  cmt: color of highlighted railways which were damaged
RAILWAY_MAP_ARROW_COLOR_HIGHLIGHTED_CONSTRUCTION:
  def: '{ 0.957, 0.871, 0.51, 1.0 }'
  type: array
  cmt: orange, shown for highlighted railways that are under construction
RAILWAY_MAP_ARROW_COLOR_HIGHLIGHTED_BOTTLENECK_MAXLEVEL:
  def: '{ 0.761, 0.647, 0.812, 1.0 }'
  type: array
  cmt: purple, shown for maxlevel railways that are the bottleneck when highlighting
RAILWAY_MAP_ARROW_COLOR_ONCOOLDOWN:
  def: '{ 0.5, 0.5, 0.5, 1.0 }'
  type: array
  cmt: color of railways which are on cooldown (captured recently)
FLOWING_RIVER_SUPPLY_MAP_ARROW_COLOR:
  def: '{ 0.8, 0.8, 1.0, 0.8 }'
  type: array
SUPPLY_TO_CONSUMERS_MAP_ARROW_TRANSPARENCY:
  def: '0.8'
  type: float
NODE_FLOW_IN_HALF_RANGE_COLOR:
  def: '{ 0.9686, 0.4078, 0.6314, 0.6 }'
  type: array
  cmt: At Half Motorization, if currently set to less than that
RAILWAY_ICON_SHIFT:
  def: '{ 0.0, 0.0, 0.0 }'
  type: array
SUPPLY_ICON_SWITCH:
  def: '200'
  type: int
SUPPLY_ICON_UNUSED_CUTOFF:
  def: '400.0'
  type: float
  cmt: where we stop showing unused nodes
SUPPLY_ICON_OK_CUTOFF:
  def: '750.0'
  type: float
  cmt: where we stop showing nodes with no issues, e.g non-red
SUPPLY_ICON_END_CUTOFF:
  def: '200.0'
  type: float
  cmt: where we stop showing line end icons
SUPPLY_SELECTED_NODE_COLOR:
  def: '{ 0.0, 1.0, 1.0, 1.0 }'
  type: array
SUPPLY_NAVAL_NODE_COLOR:
  def: '{ 0.1, 0.6, 0.8, 1.0 }'
  type: array
SUPPLY_CONSUMER_ARROW_HEIGHT_TO_LEN:
  def: '0.1'
  type: float
SUPPLY_UNIT_COUNTER_SHOW_THRESHOLD:
  def: '0.5'
  type: float
  cmt: At what supply threshold will the normal crate be shown on unit counters
SUPPLY_UNIT_COUNTER_VERY_LOW_THRESHOLD:
  def: '0.2'
  type: float
  cmt: At what supply threshold will the red crate with ! will be shown on unit counters
COUP_RED:
  def: '{ 1.0, 0.0, 0.0, 1.0 }'
  type: array
ENEMY_COLOR:
  def: '{ 1.0, 0.7, 0.7 }'
  type: array
COUNTRY_COLOR_HUE_MODIFIER:
  def: '0.0'
  type: float
COUNTRY_COLOR_BRIGHTNESS_MODIFIER:
  def: '0.8'
  type: float
COUNTRY_UI_COLOR_SATURATION_MODIFIER:
  def: '1.0'
  type: float
COMMANDGROUP_PRESET_COLORS_HSV:
  def: '{ 90.0/360.0, 0.95, 0.86, 60.0/360.0, 0.95, 0.86, 30.0/360.0, 0.95, 0.86,
    0.0/360.0, 0.95, 0.86, 330.0/360.0, 0.95, 0.86, 300.0/360.0, 0.95, 0.86, 270.0/360.0,
    0.95, 0.86, 240.0/360.0, 0.95, 0.86, 210.0/360.0, 0.95, 0.86, 180.0/360.0, 0.95,
    0.86 }'
  type: array
CAMERA_OUTSIDE_MAP_DISTANCE_BOTTOM:
  def: '200.0'
  type: float
CAMERA_ZOOM_KEY_SCALE:
  def: '0.02'
  type: float
ORDERS_MOUSE_INTERSECT_DISTANCE_MULT:
  def: '2.6'
  type: float
  cmt: For balancing the collision distance with painted arrows and fronts.
MOVE_ORDERS_MOUSE_INTERSECT_DISTANCE_MULT:
  def: '0.5'
  type: float
  cmt: For balancing the collision distance with painted arrows and fronts.
RAILWAY_INTERSECT_DISTANCE_MULT:
  def: '3.0'
  type: float
  cmt: For balancing the collision distance with painted arrows and railways.
NATIONAL_FOCUS_SHINE_DISTANCE_SCALE:
  def: '0.03'
  type: float
NATIONAL_FOCUS_PULSE_RANDOM:
  def: '10.0'
  type: float
SETUP_SPIRIT_GRID_BOX_LIMIT:
  def: '3'
  type: int
  cmt: Limit for gridbox in game setup before it will be replaced with extended gridbox
POLITICAL_PULSE_RANDOM:
  def: '10.0'
  type: float
ARROW_PARADROP_HEIGHT_TO_LEN:
  def: '0.3'
  type: float
ARROW_MIN_TEXT_POINTS_LIMIT:
  def: '10'
  type: int
  cmt: Amount of points when arrow gets first detailed text
ARMY_DEFENSIVE_LINE_BUTTON_SIZE:
  def: '0.7'
  type: float
  cmt: The size of the "edit" button drawn at the endings of the def.lines (for army)
SHOW_FOREIGN_SUPPLY_BELOW:
  def: '300.0'
  type: float
  cmt: Below this camera height all supply icons will be shown
ACCLIMATIZATION_CAMO_SHOW_AT:
  def: '0.5'
  type: float
  cmt: The moment at which the division gains enough acclimatization to change it's
    model to the camouflage one.
INTEL_NETWORK_VALID_TARGET_STRIPE_COLOR:
  def: '{ 0.1, 0.5, 0.8, 1.0 }'
  type: array
  cmt: Color of the stripes of painted over a valid state to start building an intel
    network
OCCUPATION_RESISTANCE_NON_INITIALIZED_COLOR:
  def: '{ 1.0, 1.0, 1.0, 0.05 }'
  type: array
  cmt: player owned state color with no resistance
OCCUPATION_COMPLIANCE_MAP_MODE_COLORS:
  def: '{ 0.0, 0.3, 0.6, 0.6, 0.05, 0.0, 0.3, 0.7, 1.0, 0.05, 10.0, 0.3, 0.7, 1.0,
    0.2, 50.0, 0.3, 0.7, 1.0, 0.3, 100.0, 0.3, 0.9, 1.0, 0.5 }'
  type: array
INTEL_LEDGER_NAVAL_FORT_LEVEL_COLORS:
  def: '{ 0.0, 0.3, 0.3, 0.3, 0.2, 0.0, 0.7, 0.7, 0.2, 0.3, 1.0, 0.7, 0.2, 0.2, 0.5
    }'
  type: array
RAILWAY_GUN_ASSIGNMENTS_MAP_MODE_COLORS:
  def: '{ 0.0, 1.0, 0.0, 0.0, 1.0, 0.25, 1.0, 0.65, 0.0, 1.0, 0.75, 1.0, 1.0, 0.0,
    1.0, 1.0, 0.0, 1.0, 0.45, 0.45 }'
  type: array
INTEL_LEDGER_NAVY_REGION_COLOR_WITH_MISSION_AND_TASKFORCES_IN_REGION:
  def: '{ 0.8, 0.8, 0.4, 0.9 }'
  type: array
INTEL_LEDGER_GRAPH_RED:
  def: '{ 1.0, 0.0, 0.0, 1.0 }'
  type: array
DEFAULT_NUDGE_FLOATING_HARBOR_DIST:
  def: '7.0'
  type: float
  cmt: Default distance of floating harbors from the coast in pixels, for nudger
```
