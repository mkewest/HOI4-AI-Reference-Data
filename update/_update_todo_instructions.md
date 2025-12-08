# Instructions for creating TODO file

File name = "_update_todo.md"

## Scope definitions:
Extreme:
- Deleting existing existing files
- Deleting large sections in existing files
- Making non-trivial changes to a huge number of files

Major:
- Updating or adding entire sections to multiple existing files - Adding new files

Moderate:
- Major updates to one existing file
- Deleting, adding or fundamentally altering whole section
- Minor edits to multiple files

Minor:
- Minor edits to single file
- Tiny edits to multiple files (updating default values etc)

---
## Template:

```markdown
# Planned Changes
---
## Extreme

Extreme changes planned

### file1_documentation.md or changelog patch "patch_number"

**file1_affected.md**
- Planned change 1
  - Links:
    - Update 1 needed due to planned change (none if none needed)
    - Update 2 needed due to planned change
    - ...
  - Index:
    - Update 1 needed due to planned change (none if none needed)
    - Update 2 needed due to planned change
    - ...
      
- Planned change 2
  - ...
    
- ...

**file2_affected.md**
- ...
  
---
### file2_documentation.md or changelog patch "patch_number"
...

---

### Major
...
---
...
```