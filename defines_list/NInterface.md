---
domain: defines_list
concept: NInterface
version: 1.14+
requires: [defines]
relates: [interface]
---

```yaml
MAX_NO_FACTION_FILTER_BUTTONS:
  def: '40'
  type: int
  cmt: Max number of faction filter buttons that can be generated in diplomacy view.
COMBAT_SOME_PIERCING:
  def: '0.25'
  type: float
  cmt: How many % of enemy units the unit have to pierce in order for the some piercing
    icon to be displayed
COMBAT_SOME_ARMOR:
  def: '0.25'
  type: float
  cmt: How many % of enemy units have to be unable to pierce the unit in order for
    the some armor icon to be displayed
MIN_FOCUS_TREE_ZOOM:
  def: '0.2'
  type: float
  cmt: min zoom in scale
FOCUS_TREE_ZOOM_SPEED:
  def: '0.16'
  type: float
  cmt: zooming speed
TOOLTIP_SCREEN_LEFT_OFFSET_X:
  def: '0'
  type: int
  cmt: Tooltip offset on x axis from left screen border
TOOLTIP_SCREEN_TOP_OFFSET_Y:
  def: '0'
  type: int
  cmt: Tooltip offset on y axism from top screen border
NO_COMBATS_COLOR:
  def: '{ 0.0, 0.0, 0.8 }'
  type: array
  cmt: Color for icons if all combats are successful
MIN_NON_SUCCESSFUL_COMBAT_COLOR:
  def: '{ 100.0/360.0, 0.95, 0.86 }'
  type: array
  cmt: Color for icons if some of combats are not successful
MAX_NON_SUCCESSFUL_COMBAT_COLOR:
  def: '{ 0.0/360.0, 0.95, 0.86 }'
  type: array
  cmt: Color for icons if all of combats are not successful
SHIP_SELECT_DOUBLE_CLICK_TIME:
  def: '1.0'
  type: float
  cmt: Delay before double click event for ship selection
MINIMAP_TOGGLE_SHIFT:
  def: '270'
  type: int
  cmt: horizontal shift for minimap to close it
MINIMAP_PING_DURATION:
  def: '12.0'
  type: float
  cmt: timeout for pings
MINIMAP_PING_DELAY_BETWEEN_PINGS:
  def: '0.3'
  type: float
  cmt: delay between consecative pings
GRIDBOX_ELEMENTS_INTERPOLATION_SPEED:
  def: '0.5'
  type: float
  cmt: A value used to determine how fast the elements within the gridbox are interpolating
    while drag'n dropping.
ARMY_GROUP_FIRST_MEMBER_SPACING:
  def: '5'
  type: int
  cmt: Extra spacing between the army group portrait and the first member of the army
    group
ARMY_LIST_BOTTOM_PADDING:
  def: '165'
  type: int
  cmt: Bottom padding for army list on left
MILITARY_FACTORIES_SCALE:
  def: '{ 1, 5, 10 }'
  type: array
FLEET_BOTTOM_BAR_PADDING_RIGHT:
  def: '110'
  type: int
  cmt: Width of the Rhs panel at the bottom of the screen where map mode are selected
PICKED_UP_NAVY_OFFSET_Y:
  def: '-14'
  type: int
  cmt: Amount of pixels to shift the picked up navy window on the y axis
TASK_FORCE_COMPOSITION_EDITOR_PADDING_TO_NAVIES_VIEW:
  def: '20'
  type: int
  cmt: Padding on the x axis between the navies view and the task force composition
    editor window
SHIP_REFIT_TOOLTIP_MAX_DIFF_LINES:
  def: '20'
  type: int
  cmt: Maximum number of lines to show in the tooltip describing stat differences
    from all the source equipment variants to the target being considered.
DEFAULT_FLEET_ICON:
  def: '4'
  type: int
  cmt: newly created fleets will use this icon
FUEL_GRAPH_COLOR:
  def: '{ 0.8, 0.8, 0.8, 0.8, 0.0, 0.0, 0.0, 0.8, 0.0, 0.0, 0.0, 0.8, 0.0, 0.8, 0.8,
    0.8, 0.8, 0.0, 0.8, 0.8, 0.8 }'
  type: array
  cmt: stockpile total consumption army consumption navy consumption air consumption
    other consumption produced
PRODUCTION_SHIP_FILTERS_ROLE_SELECTION_WINDOW_OFFSET_Y:
  def: '-8'
  type: int
NAVAL_STRIKE_FORCE_ATTACK_LIKELYHOOD_THR_VERY_LIKELY:
  def: '0.8'
  type: float
  cmt: threshold above which to show that a strike force is "very likely" to engage
    an enemy
NAVAL_STRIKE_FORCE_ATTACK_LIKELYHOOD_THR_UNLIKELY:
  def: '0.3'
  type: float
  cmt: same, for "unlikely"
MISSION_PATROL_SOFT_REQ_THRESHOLD_SURFACE_DETECTION:
  def: '22'
  type: int
  cmt: Value below which the mission icon for the patrol mission is showing a warning
MISSION_PATROL_SOFT_REQ_THRESHOLD_SURFACE_VISIBILITY:
  def: '1.4'
  type: float
  cmt: Same, but for the surface visibility of the task force (lower means more fit
    for the mission for this one)
MISSION_CONVOY_ESCORT_SOFT_REQ_THRESHOLD_DEPTH_CHARGES_AVG:
  def: '8'
  type: int
  cmt: Average of the stat Depth Charges in the task force
MISSION_NAVAL_INVASION_SUPPORT_SOFT_REQ_THRESHOLD_SHORE_BOMBARDMENT:
  def: '3'
  type: int
  cmt: Same, for naval invasion. Sum of the stat Shore Bombardment in the task force
OPERATIVE_MISSION_EFFICIENCY_ANIMATION_TIME_MAX:
  def: '3.0'
  type: float
  cmt: the maximum duration of a loop in seconds
OPERATIVE_NETWORK_STRENGTH_GAIN_TO_EFFICIENCY_FACTOR:
  def: '12.0'
  type: float
  cmt: Factor multiplied to the network strength the operative provides while on build
    network mission to get a score in the range [0,100] that is then used to scale
    the animation speed
OPERATIVE_BOOST_IDEOLOGY_DRIFT_TO_EFFICIENCY_FACTOR:
  def: '500.0'
  type: float
  cmt: Factor multiplied to the ideology drift caused by the operative in order to
    get a score in the range [0,100] used to determine the speed of the animation
OPERATIVE_TRADE_INFLUENCE_DRIFT_TO_EFFICIENCY_FACTOR:
  def: '135'
  type: int
  cmt: Factor multiplied to the operative's trade influence drift to determine the
    animation speed
OPERATIVE_TENSION_DRIFT_TO_EFFICIENCY_FACTOR:
  def: '400'
  type: int
  cmt: Factor multiplied to the operative's trade influence drift to determine the
    animation speed
COUNTERINTELLIGENCE_ACTIVITY_LEVEL_THRESHOLD_COLORS:
  def: '{ { 0.1, 0.9, 0.2, 1.0 }, { 0.6, 0.9, 0.2, 1.0 }, { 0.9, 0.7, 0.2, 1.0 },
    { 1.0, 0.5, 0.0, 1.0 }, { 0.9, 0.1, 0.2, 1.0 } }'
  type: array
MAX_DECISIONS_IN_DECISION_ALERT_TOOLTIP:
  def: '5'
  type: int
  cmt: Max number of available decisions we show in the alert tooltip
ARMY_UNIT_LEADER_ICON_SPRITE_ID:
  def: '5'
  type: int
POLITICAL_LEADER_ICON_SPRITE_ID:
  def: '13'
  type: int
EQUIPMENT_DESIGNER_SHOW_MODULE_FORBIDS_SPECIALIZED_ROLE_ICON:
  def: '0'
  type: int
  cmt: If this is set to 0 no icons will be displayed for any forbidden specialized
    roles. If set to 1 the icons will be displayed as normal.
SLOW_INTERFACE_THRESHOLD:
  def: '5000'
  type: int
  cmt: Show warning "SLOW INTERFACE" in debug when interface refresh takes more that
    this (in microseconds)
```
