---
domain: core
concept: debug_tools
version: 1.14+
requires: [file_syntax, mod_structure]
relates: [console_commands, troubleshooting]
---

# Debug Tools

HOI4 provides several debugging systems for development and troubleshooting. Understanding these tools and their limitations helps diagnose issues efficiently.

## Debug Mode

Debug mode is activated by launching the game with the `-debug` flag. This enables extensive development features but comes with performance costs.

### Debug Features

When debug mode is active, the following features become available:

**Auto-reload:** Existing files reload automatically when modified (excluding certain directories)

**No map crash:** The game continues running despite map errors that would normally crash

**Extended logging:** More detailed information appears in log files

**Auto-open log:** Error and game logs open automatically when errors occur

**Nudge menu:** Access the nudger tool from the main menu

**GUI info:** Press the `` ` `` key to display GUI element information

**GUI file access:** Ctrl+Alt+Right-click GUI elements to open their definition files

**Hover IDs:** Mouse hover displays internal IDs for focuses, ideas, technologies, states, and provinces

**Dev commands:** Unlock development-only console commands

**Save peace:** Create saves during peace conferences

Debug mode disables multiplayer access and reduces overall game performance. The performance impact is noticeable during normal gameplay.

### Auto-Reload Limitations

> [!CRITICAL] Files in history/countries, history/states, and map/ do NOT auto-reload in debug mode. You must restart the game to see changes to these directories.

Image loading in debug mode appears distorted until a full restart occurs - simple reload is insufficient for graphics changes.

Empty files are skipped entirely by the game reader, which can mislead crash debugging. A completely empty file behaves as if it doesn't exist at all.

## Crash Data Log

The `-crash_data_log` flag creates detailed crash information in `crashes/meta.yml` at the game root directory (not in logs/).

### Crash Log Contents

The crash data log includes:

**LastRead:** The file and line number where parsing stopped before the crash

**debug_enabled:** Whether debug mode was active

### Critical Limitation

> [!CRITICAL] If the last read line is the LAST line of a file, the crash likely occurred during the NEXT file's loading. The crash data log shows where parsing stopped, not necessarily where it crashed.

The game can show "script" instead of a filename, indicating the crash occurred in savefile processing or client_ping events rather than file loading.

### Debug Mode Interaction

The `-crash_data_log` flag enables debug mode but does not provide all `-debug` benefits automatically. Specifically, indexed files during main menu loading don't auto-reload with only crash data logging active. Use both flags together for full debugging capability.

### Performance Impact

Crash data logging significantly slows game performance. Only use it when actively debugging crashes, not for regular testing.

## Log Files

All log files are located at `<user_dir>/logs/` and are overwritten every time the game starts. Logs do not persist between sessions.

### Essential Logs

**error.log (high priority):** Contains non-fatal mod errors. MAP_ERROR entries require `-debug` flag to appear. This is the primary source for identifying content issues.

**game.log (high priority):** Records runtime actions and effect execution. When using the `log` effect, output appears here.

**setup.log (high priority):** Shows loading completion progress. Essential for identifying which file caused loading crashes - check this log to find the last successfully loaded file.

**memory.log (high priority):** Records memory usage during setup phase. Useful for diagnosing loading crashes caused by memory exhaustion.

### Supplementary Logs

**time.log (medium priority):** Loading times and tick intervals for performance analysis

**text.log (medium priority):** Localisation key assertion failures

**system_debug.log (medium priority):** Interface rendering errors and GUI issues

**ai.log (medium priority):** AI decision-making choices and evaluation

### Low-Priority Logs

**exceptions.log (low priority):** CTD stack traces for fatal crashes

**graphics.log (low priority):** Graphics-related errors and warnings

### Log Analysis

The error log auto-opens only if errors are present when loading or selecting a country. Silent failures (encoding mismatches, missing dependencies) may not generate log entries.

MAP_ERROR entries sometimes only appear after selecting a country and starting a playthrough, not at main menu. If investigating map definition crashes, always load into a country before checking the error log.

The `-debug` flag must be set before launching to capture full error logging. Adding it to an already-running game doesn't retroactively log earlier errors.

## Debugging Effects

Two scripting effects output state information for analysis:

### Log Effect

```hoi4
log = "Debug message here"
```

Writes the string to `logs/game.log`. If the console is open and debug mode is active, the message also appears in the console output.

### Print Variables Effect

```hoi4
print_variables = {
    file = log  # Optional: filename
    text = log  # Optional: text to include
    append = yes  # Optional: append to existing file
    print_global = yes  # Optional: include global variables
    var_list = { var1 var2 }  # Optional: specific variables
}
```

Outputs variable values to `logs/variable_dumps/` in the user directory. All parameters are optional - calling with no parameters dumps all variables in the current scope.

This is essential for debugging complex variable calculations and verifying state during scripting.

### Console Variable Commands

The console provides direct variable access:

**list_vars:** Lists all variables in the currently selected scope. Selection context determines which scope is queried - no selection shows global, country selected shows that country's variables, etc.

**get_var [<variable>]:** Displays a specific variable's value

**set_var [<variable>] [<value>]:** Modifies a variable in the current scope

Console scope defaults to the player country but changes based on current selection (diplomacy screen country, selected state, selected unit leader).

## Related Systems

- Console commands: See [Console Commands](/core/console_commands.md)
- Crash diagnosis: See [Troubleshooting](/core/troubleshooting.md)
- Nudger tool: See [Nudger](/core/nudger.md)
- Variable system: See [Scripting Data Types](/core/scripting_data_types.md#variables)
