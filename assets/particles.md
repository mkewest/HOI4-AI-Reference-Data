---
domain: assets
concept: particles
version: 1.14+
requires: []
relates: [entities]
---

# Particle System

Particles create visual effects like smoke, fire, explosions, and environmental effects. The particle editor enables visual creation and tuning of effect parameters.

## Particle Editor

> [!CRITICAL] The particle editor requires exactly version 1.11 of Hearts of Iron IV. Earlier versions have non-functional launchers, and later versions crash the editor. This is not a preference but an absolute technical requirement - only 1.11 works.

### Editor Access

Launch the editor using the `-editor` flag exclusively:

```
hoi4.exe -editor
```

No other launch flags can be combined with `-editor`. Multiple flags cause the editor to fail initialization. The flag must be used alone.

### Editing Workflow Limitations

The editor cannot access mod-created particles directly. Attempting to open particle files from mod directories fails without error message - the editor simply shows an empty state.

Workaround for editing mod particles:

1. Locate vanilla particle file to overwrite (temporary working copy)
2. Copy mod particle data into vanilla file location
3. Launch editor and open the vanilla file
4. Make edits in the editor
5. Save changes
6. Copy modified file to mod directory
7. Verify game integrity through Steam to restore vanilla files

This workflow is required because the editor only recognizes particles in the base game directory structure. After completing edits and copying to mod, Steam's "verify integrity" restores original vanilla files without affecting the mod.

### Editor Limitations

The particle editor provides visual preview and parameter adjustment but has significant limitations:

- Cannot create new particle types from scratch without template
- No batch editing capabilities for multiple particles
- No undo/redo functionality
- Changes save immediately to file with no confirmation
- No version control or backup system

These limitations make the workaround workflow even more critical - always maintain backup copies before editing since the editor provides no recovery options.

## Particle Integration

Particles integrate with entity events for triggered effects and with map scripts for environmental effects. Entity states can spawn particles at specific animation times, while map-based particle systems create weather, smoke, and environmental ambiance.

See [Entities](/assets/entities.md) for particle event triggering in animation states.
