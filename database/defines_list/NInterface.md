---
domain: defines_list
concept: NInterface
version: 1.17.2
requires: [defines]
relates: [interface]
---

```yaml
MAX_NO_FACTION_FILTER_BUTTONS:
  def: '40'
  type: int
  cmt: Max number of faction filter buttons that can be generated in diplomacy view.
LOGISTICS_PAST_WEEK:
  def: '7'
  type: int
  cmt: Number of days from the past (including current day) we want logistics data for
    (Max 30 days)
COMBAT_SOME_PIERCING:
  def: '0.25'
  type: float
  cmt: How many % of enemy units the unit have to pierce in order for the some piercing
    icon to be displayed
COMBAT_GOOD_PIERCING:
  def: '0.6'
  type: float
  cmt: How many % of enemy units the unit have to pierce in order for the good piercing
    icon to be displayed
COMBAT_SOME_ARMOR:
  def: '0.25'
  type: float
  cmt: How many % of enemy units have to be unable to pierce the unit in order for the
    some armor icon to be displayed
COMBAT_GOOD_ARMOR:
  def: '0.6'
  type: float
  cmt: How many % of enemy units have to be unable to pierce the unit in order for the
    good armor icon to be displayed
MIN_FOCUS_TREE_ZOOM:
  def: '0.2'
  type: float
  cmt: min zoom in scale
MAX_FOCUS_TREE_ZOOM:
  def: '1.0'
  type: float
  cmt: max zoom out scale
FOCUS_TREE_ZOOM_SPEED:
  def: '0.16'
  type: float
  cmt: zooming speed
FOCUS_TREE_ZOOM_FACTOR:
  def: '0.5'
  type: float
  cmt: zooming factor that will be factored while player scrolls too fast
TOOLTIP_SCREEN_LEFT_OFFSET_X:
  def: '0'
  type: int
  cmt: Tooltip offset on x axis from left screen border
TOOLTIP_SCREEN_RIGHT_OFFSET_X:
  def: '0'
  type: int
  cmt: Tooltip offset on x axis from right screen border
TOOLTIP_SCREEN_TOP_OFFSET_Y:
  def: '0'
  type: int
  cmt: Tooltip offset on y axism from top screen border
TOOLTIP_SCREEN_BOTTOM_OFFSET_Y:
  def: '0'
  type: int
  cmt: Tooltip offset on y axis from bottom screen border
NO_COMBATS_COLOR:
  def:
    - [0.0, 0.0, 0.8]
  type: table
  cmt: Color for icons if all combats are successful
SUCCESFUL_COMBATS_COLOR:
  def:
    - [120.0/360.0, 0.95, 0.86]
  type: table
  cmt: Color for icons if all combats are successful
MIN_NON_SUCCESSFUL_COMBAT_COLOR:
  def:
    - [100.0/360.0, 0.95, 0.86]
  type: table
  cmt: Color for icons if some of combats are not successful
MID_NON_SUCCESSFUL_COMBAT_COLOR:
  def:
    - [50.0/360.0, 0.95, 0.86]
  type: table
MAX_NON_SUCCESSFUL_COMBAT_COLOR:
  def:
    - [00.0/360.0, 0.95, 0.86]
  type: table
  cmt: Color for icons if all of combats are not successful
UNIT_SELECT_DOUBLE_CLICK_TIME:
  def: '0.1'
  type: float
  cmt: Delay before double click event for unit selection
SHIP_SELECT_DOUBLE_CLICK_TIME:
  def: '1.0'
  type: float
  cmt: Delay before double click event for ship selection
MINIMAP_TOGGLE_DURATION:
  def: '0.5'
  type: float
  cmt: Delay for minimap toggle
MINIMAP_TOGGLE_SHIFT:
  def: '270'
  type: int
  cmt: horizontal shift for minimap to close it
TIMED_MESSAGE_TIMEOUT:
  def: '0.35'
  type: float
  cmt: Timeout for timed message
MINIMAP_PING_DURATION:
  def: '12.0'
  type: float
  cmt: timeout for pings
MINIMAP_PING_SPEEDUP_ON_SCREEN:
  def: '2.0'
  type: float
  cmt: speed up for timeout if ping is visible on screen
MINIMAP_PING_DELAY_BETWEEN_PINGS:
  def: '0.3'
  type: float
  cmt: delay between consecative pings
DRAG_AND_DROP_SCROLLING_SENSITIVITY:
  def: '12.5'
  type: float
  cmt: Speed multiplier for components scrolling while drag'n dropping elements
GRIDBOX_ELEMENTS_INTERPOLATION_SPEED:
  def: '0.5'
  type: float
  cmt: A value used to determine how fast the elements within the gridbox are
    interpolating while drag'n dropping.
ARMY_GROUP_PORTRAIT_SPACING:
  def: '6'
  type: int
  cmt: Extra space added between portraits of different army groups
ARMY_GROUP_FIRST_MEMBER_SPACING:
  def: '5'
  type: int
  cmt: Extra spacing between the army group portrait and the first member of the army
    group
ARMY_GROUP_COLLAPSE_EXTRA_SPACING:
  def: '5'
  type: int
  cmt: Extra spacing between the army group portrait when army group is collapsed
ARMY_LIST_BOTTOM_PADDING:
  def: '165'
  type: int
  cmt: Bottom padding for army list on left
ARMY_LIST_BOTTOM_PADDING_WITH_EXPEDITIONARIES:
  def: '240'
  type: int
  cmt: Bottom padding for army list on left when expeditionaries are open
MILITARY_FACTORIES_SCALE:
  def:
    - [1, 5, 10]
  type: table
FLEET_BOTTOM_BAR_HEIGHT:
  def: '110'
  type: int
  cmt: Height of the list of fleet at the bottom of the screen
FLEET_BOTTOM_BAR_PADDING_RIGHT:
  def: '110'
  type: int
  cmt: Width of the Rhs panel at the bottom of the screen where map mode are selected
PICKED_UP_NAVY_OFFSET_X:
  def: '26'
  type: int
  cmt: Amount of pixels to shift the picked up navy window on the x axis
PICKED_UP_NAVY_OFFSET_Y:
  def: '-14'
  type: int
  cmt: Amount of pixels to shift the picked up navy window on the y axis
TASK_FORCE_ENTRY_OFFSET_Y:
  def: '-2'
  type: int
  cmt: Adjust the position of a task force entry. Added to the height of the background
    image.
TASK_FORCE_COMPOSITION_EDITOR_PADDING_TO_NAVIES_VIEW:
  def: '20'
  type: int
  cmt: Padding on the x axis between the navies view and the task force composition
    editor window
FUEL_STOCKPILE_DURATION_MAX:
  def: '365*5'
  type: string
  cmt: our max for stockpile duration display
SHIP_REFIT_TOOLTIP_MAX_DIFF_LINES:
  def: '20'
  type: int
  cmt: Maximum number of lines to show in the tooltip describing stat differences from
    all the source equipment variants to the target being considered.
DEFAULT_TASKFORCE_ICON:
  def: '6'
  type: int
  cmt: newly created taskforces will use this icon
DEFAULT_FLEET_ICON:
  def: '4'
  type: int
  cmt: newly created fleets will use this icon
DEFAULT_NAVAL_EQUIPMENT_ROLE_ICON:
  def: '1'
  type: int
  cmt: newly created naval equipment variants will use this icon, if the AI equipment
    designs do not propose a better one.
FUEL_GRAPH_COLOR:
  def:
    - [0.8, 0.8, 0.8]  # stockpile
    - [0.8, 0.0, 0.0]  # total consumption
    - [0.0, 0.8, 0.0]  # army consumption
    - [0.0, 0.0, 0.8]  # navy consumption
    - [0.0, 0.8, 0.8]  # air consumption
    - [0.8, 0.8, 0.0]  # other consumption
    - [0.8, 0.8, 0.8]  # produced
  type: table
PRODUCTION_SHIP_FILTERS_ROLE_SELECTION_WINDOW_OFFSET_X:
  def: '4'
  type: int
  cmt: offset of the role icon selection window shown in the filters of ship design in
    the production tab
PRODUCTION_SHIP_FILTERS_ROLE_SELECTION_WINDOW_OFFSET_Y:
  def: '-8'
  type: int
SHIP_FUEL_EFFICIENCY_WARNING_THRESHOLD:
  def: '60.0'
  type: float
  cmt: Fuel usage threshold above which a ship is considered fuel inefficient for always
    on missions
NAVAL_STRIKE_FORCE_ATTACK_LIKELYHOOD_THR_VERY_LIKELY:
  def: '0.8'
  type: float
  cmt: threshold above which to show that a strike force is "very likely" to engage an
    enemy
NAVAL_STRIKE_FORCE_ATTACK_LIKELYHOOD_THR_LIKELY:
  def: '0.6'
  type: float
  cmt: same, for "likely"
NAVAL_STRIKE_FORCE_ATTACK_LIKELYHOOD_THR_UNLIKELY:
  def: '0.3'
  type: float
  cmt: same, for "unlikely"
CONVOY_ESCORT_PRESENCE_WARNING_THRESHOLD:
  def: '0.95'
  type: float
  cmt: Value for the Escort Presence below which a warning will be shown on the naval
    mission map icon
MISSION_PATROL_SOFT_REQ_THRESHOLD_SURFACE_DETECTION:
  def: '22'
  type: int
  cmt: Value below which the mission icon for the patrol mission is showing a warning
MISSION_PATROL_SOFT_REQ_THRESHOLD_SPEED:
  def: '30'
  type: int
  cmt: (kph) Same, but for Speed of the task force
MISSION_PATROL_SOFT_REQ_THRESHOLD_SURFACE_VISIBILITY:
  def: '1.4'
  type: float
  cmt: Same, but for the surface visibility of the task force (lower means more fit for
    the mission for this one)
MISSION_CONVOY_ESCORT_SOFT_REQ_THRESHOLD_SUB_DETECTION:
  def: '2'
  type: int
  cmt: Same, for convoy escort
MISSION_CONVOY_ESCORT_SOFT_REQ_THRESHOLD_DEPTH_CHARGES_AVG:
  def: '8'
  type: int
  cmt: Average of the stat Depth Charges in the task force
MISSION_CONVOY_ESCORT_SOFT_REQ_THRESHOLD_DEPTH_CHARGES_SUM:
  def: '8'
  type: int
  cmt: Sum of the stat Depth Charges in the task force
MISSION_NAVAL_INVASION_SUPPORT_SOFT_REQ_THRESHOLD_SHORE_BOMBARDMENT:
  def: '3'
  type: int
  cmt: Same, for naval invasion. Sum of the stat Shore Bombardment in the task force
OPERATIVE_MISSION_EFFICIENCY_ANIMATION_TIME_MIN:
  def: '0.2'
  type: float
  cmt: the minimum duration of a loop in seconds
OPERATIVE_MISSION_EFFICIENCY_ANIMATION_TIME_MAX:
  def: '3.0'
  type: float
  cmt: the maximum duration of a loop in seconds
OPERATIVE_COUNTER_INTELLIGENCE_DEFENSE_TO_EFFICIENCY_FACTOR:
  def: '40.0'
  type: float
  cmt: Factor multiplied to the defense provided by the operative while on counter
    intelligence mission to get a score in the range [0,100] that is then used to scale
    the animation speed
OPERATIVE_NETWORK_STRENGTH_GAIN_TO_EFFICIENCY_FACTOR:
  def: '12.0'
  type: float
  cmt: Factor multiplied to the network strength the operative provides while on build
    network mission to get a score in the range [0,100] that is then used to scale the
    animation speed
OPERATIVE_PROPAGANDA_DRIFT_TO_EFFICIENCY_FACTOR:
  def: '130000.0'
  type: float
  cmt: Factor multiplied to the war support and stability drift to obtain the efficiency
    score (expected to be in range [0,100])
OPERATIVE_BOOST_IDEOLOGY_DRIFT_TO_EFFICIENCY_FACTOR:
  def: '500.0'
  type: float
  cmt: Factor multiplied to the ideology drift caused by the operative in order to get a
    score in the range [0,100] used to determine the speed of the animation
OPERATIVE_ROOT_OUT_RESISTANCE_EFFICIENCY_TO_EFFICIENCY_FACTOR:
  def: '80.0'
  type: float
  cmt: Factor multiplied to the operative's efficiency at the RootOutResistance mission
    to determine the animation speed
OPERATIVE_TRADE_INFLUENCE_DRIFT_TO_EFFICIENCY_FACTOR:
  def: '135'
  type: int
  cmt: Factor multiplied to the operative's trade influence drift to determine the
    animation speed
OPERATIVE_OPINION_DRIFT_TO_EFFICIENCY_FACTOR:
  def: '400'
  type: int
  cmt: Factor multiplied to the operative's trade influence drift to determine the
    animation speed
OPERATIVE_TENSION_DRIFT_TO_EFFICIENCY_FACTOR:
  def: '400'
  type: int
  cmt: Factor multiplied to the operative's trade influence drift to determine the
    animation speed
AIR_WING_REINFORCEMENT_ICON_SCALE:
  def: '0.9'
  type: float
  cmt: Scale of the reinforcement icon for reinforcement strip on airwing toolbar
AIR_WING_NICHE_ICON_SCALE:
  def: '0.8'
  type: float
  cmt: Scale of the niche icon for strip on airwing toolbar
COUNTERINTELLIGENCE_ACTIVITY_LEVEL_THRESHOLD_VALUES:
  def:
    - [10]
    - [20]
    - [50]
    - [100]
  type: table
COUNTERINTELLIGENCE_ACTIVITY_LEVEL_THRESHOLD_COLORS:
  def:
    - [{ 0.1, 0.9, 0.2, 1.0]
  type: table
```
