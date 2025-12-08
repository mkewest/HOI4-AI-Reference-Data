---
domain: defines_list
concept: NCharacter
version: 1.17.2
requires: [defines]
relates: [characters]
---

```yaml
OFFICER_CORP_ADVISOR_ENTRIES_IN_MENU:
  def:
    - ["high_command", "theorist", "army_chief", "air_chief", "navy_chief"]
  type: table
OFFICER_CORP_HIGH_COMMAND_SLOTS_IN_MENU:
  def: '3'
  type: int
  cmt: For Alert manager to count the number of High Command Slots in the UI
POLITICAL_ADVISOR_SLOTS_IN_MENU:
  def: '3'
  type: int
  cmt: For Alert manager to count the number of Political Advisor Slots in the UI
DEFAULT_PP_COST_FOR_MILITARY_ADVISOR:
  def: '50'
  type: int
  cmt: When an advisor does not have cost assigned this is the default used
DEFAULT_PP_COST_FOR_POLITICAL_ADVISOR:
  def: '150'
  type: int
DEFAULT_CP_COST_FOR_ADVISOR:
  def: '0'
  type: int
  cmt: For Starting Advisors
DEFAULT_CP_COST_FOR_DYNAMIC_ADVISORS:
  def: '0'
  type: int
  cmt: For Advisors created during gameplay
ADVISOR_PROMOTION_COST:
  def: '5'
  type: int
  cmt: Cost to promote someone to advisor
COUNTRY_LEADER_BASE_EXPIRE_YEAR_LENGTH:
  def: '5'
  type: int
  cmt: When creating a dynamic country leader if an expire date is not set it will have
    5 years as a base expiration date
COUNTRY_LEADER_BASE_RANDOM_MAX_YEAR_LENGTH:
  def: '15'
  type: int
  cmt: Max random value added to COUNTRY_LEADER_BASE_EXPIRE_YEAR_LENGTH
SPECIALIST_ADVISOR_MIN_RANK:
  def: '4'
  type: int
EXPERT_ADVISOR_MIN_RANK:
  def: '6'
  type: int
GENIUS_ADVISOR_MIN_RANK:
  def: '8'
  type: int
```
