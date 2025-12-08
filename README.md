# **WIP!** Nowhere near complete

Inaccurate and poorly optimized

## HOI4 Modding AI Reference Database

**HOI4-AI-Reference-Data** is a high-density, structured reference for Hearts of Iron IV modding, designed from the ground up for **LLMs and humans** to use together.

Instead of being a loose wiki clone, this repo is a **Hybrid-RAG knowledge base**:

- Markdown files are written for **semantic cohesion** (one complete concept per file).
- Typed metadata and a **master JSON index** enable **graph-style routing** (intents → domains/files).
- All important **edge cases and gotchas are inline**, right where they matter.

If you only read this README, you should understand:

- **How the repo is organized**
- **How an AI or human should navigate it**
- **How special domains (defines/modifiers) work**
- **Where to start for maintenance tasks**

---

## High-Level Architecture

- **Domains as folders**  
  Each top-level folder is a **domain** (e.g. `core`, `scripting`, `map`, `military`, `content`, `database`, `assets`, `entities`, `modifiers_list`, `defines_list`).

- **One concept per file**  
  Files follow the rules in `Initial Creation Instructions/architecture_rules.md`:
  - Each `.md` covers a **single semantic concept** (e.g. `map/terrain.md`, `content/events.md`).
  - Edge cases are integrated into the relevant sections instead of being in separate “warning” files.

- **Per-domain overview files**  
  Every domain has a `00_overview.md` at its root, summarizing:
  - What files exist and what they cover.
  - Semantic groupings and dependency graphs.
  - Which files have especially dense/critical edge cases.

  Example:
  - `core/00_overview.md`
  - `scripting/00_overview.md`
  - `map/00_overview.md`
  - `military/00_overview.md`, etc.

- **Master index for routing**  
  The root file `master_index.json` is a **router**:
  - Groups domains under `"domains"`.
  - For each domain, defines:
    - `"path"` – folder path.
    - `"overview"` – overview filename.
    - `"routes"` – an array of **routing rules**, each with:
      - `intent`: a short name describing a **question/problem type** (e.g. `"map_error"`, `"modifier_lookup"`, `"define_lookup"`, `"events_system_help"`).
      - `description`: natural-language explanation of when to use this route.
      - `signals`: **hints an AI can match against a user query**, such as:
        - `keywords`: substrings or concepts.
        - `error_log_contains`: log fragments (e.g. `"MAP_ERROR"`, `"X4008"`).
        - `file_hint`: filenames/extensions that appear in a query.
      - `primary_targets`: **best file(s)** to answer this kind of question.
      - `secondary_targets`: related or supporting files.

This means an agent **does not need to know the repo layout** in advance: it can map a query → intent → domain → file(s).

---

## How an AI Should Use the Database

### 1. Interpret the user query

- Extract:
  - **Problem type**: error vs. design vs. tuning vs. lookup.
  - **Keywords**: log lines, file names, mechanic names (e.g. `supply node`, `focus_tree`, `NDefines.NMilitary`).

### 2. Match against `master_index.json`

- Load `master_index.json` and:
  - Find one or more **`routes`** whose `intent` and `signals` best match the query.
  - Example mappings:
    - Map crash mentioning `MAP_ERROR` and `provinces.bmp` → intent `map_error` → domain `map` → `map/troubleshooting.md`, `map/provinces.md`.
    - User asks “what modifiers help naval detection?” → intent `modifier_lookup` → domain `modifiers_list` → `modifiers_list/00_overview.md` + `modifiers_list/military_naval.md`.
    - User asks “how do I safely change defines?” → intent `defines_tuning` → domain `scripting` → `scripting/defines.md`.
    - User asks “where is `COMBAT_WIDTH` defined?” → intent `define_lookup` → domain `defines_list` → `defines_list/NMilitary.md`.

### 3. Use per-domain overviews

- Once a domain is selected, use its `00_overview.md` to:
  - See **which files exist** and how they relate.
  - Understand which file is likely to contain the **answer with enough surrounding context**.
  - Navigate to the specific `.md` file and search within it (vector search or keyword search).

### 4. Respect the mechanics vs. enumeration split

- **Modifiers**:
  - `/scripting/modifiers.md` – **how modifiers work**:
    - Types (percentual / flat / boolean / multiplicative).
    - Application methods (ideas, traits, dynamic, static, targeted, opinion).
    - Critical edge cases and broken modifiers.
  - `/modifiers_list/*.md` – **what modifiers exist**:
    - Category files (land, naval, air, politics, economy, etc.).
    - Each entry has name, behavior, and edge cases.
  - Use:
    - `modifier_system_help` (scripting domain) for **mechanics** questions.
    - `modifier_lookup` (modifiers_list domain) for **lookup** questions.

- **Defines**:
  - `/scripting/defines.md` – **how defines work**:
    - Lua structure, partial overrides, NO COMMAS rule, limits like `MAX_EFFECT_ITERATION`.
  - `/defines_list/*.md` – **what defines exist**:
    - One file per `NDefines` category (e.g. `NGame.md`, `NMilitary.md`, `NGraphics.md`).
  - Use:
    - `defines_tuning` (scripting domain) for **how to change defines** safely.
    - `define_lookup` (defines_list domain) for **enumeration / value lookup**.

### 5. Follow typed relationships and crosslinks

- Each `.md` file starts with **YAML frontmatter**:

```yaml
---
domain: map
concept: provinces
version: 1.14+
requires: [definition_format, continents]
relates: [terrain, strategic_regions, states]
---
```

- Keys:
  - **`requires`** – hard dependencies (“read these first for full understanding”).
  - **`relates`** – soft links to related systems.
  - **`conflicts`** – mutually exclusive or deprecated systems (e.g. pre-1.11 vs 1.11+ supply).

An AI can use these to:

- Plan multi-step reasoning (e.g. `events` → `scopes` → `triggers`).
- Find which **other domains** matter for a given problem (e.g. map crashes often involve `core/debug_tools.md`).

---

## How a Human Should Use the Database

- **If you are new to HOI4 modding**:
  - Start with `core/00_overview.md` (file structure, load order, syntax).
  - Then `scripting/00_overview.md` (scopes, triggers, effects, defines, modifiers).
  - After that, jump to the domain you care about:
    - `map/00_overview.md` for map work.
    - `military/00_overview.md` for divisions/OOB/equipment systems.
    - `content/00_overview.md` for events, focuses, decisions, AI behavior.

- **If you are debugging a specific issue**:
  - Check your logs / symptoms.
  - Find the closest **intent** in `master_index.json` and follow its primary/secondary targets.
  - Use linked domains and the YAML `requires` metadata to follow dependencies.

- **If you want reference data**:
  - For modifiers: `modifiers_list/00_overview.md` then the relevant category file.
  - For defines: `defines_list/00_overview.md` then the relevant `N*.md` file.

---

## Design Philosophy (Why It Looks Like This)

- **Semantic cohesion over file mirroring**
  - Files are grouped by **concept**, not 1:1 with game directories.
  - Example: `map/terrain.md` covers both **provincial** and **graphical** terrain because they are behaviorally coupled.

- **Edge cases inline, not siloed**
  - Every critical gotcha (e.g., province ID gaps, zero-value modifier behavior, scope bugs) is documented **at the exact place** where the mechanic is described.
  - A small number of “troubleshooting” files exist where it materially reduces duplication (e.g. `map/troubleshooting.md`).

- **Typed relationships for graph reasoning**
  - Frontmatter `requires` / `relates` / `conflicts` enable:
    - **Backward traversal** for error diagnosis (e.g. find preconditions).
    - **Version-aware guidance** when systems change.

- **Mechanics vs. enumeration**
  - For large enumerations (defines, modifiers), mechanics live in one place, lists live in another.
  - This avoids repeating system explanations hundreds of times and keeps RAG chunks focused.

---

## Quick Start Checklist for New Agents

- **Step 1** – Read this `README.md` fully.
- **Step 2** – Skim `index_master_plan.md` for the high-level indexing strategy and the current **intent taxonomy**.
- **Step 3** – For answering user queries:
  - Use `master_index.json` → find **intent** → domain → `00_overview.md` → specific file.

With just this README and the above files, a new human or AI agent should be able to understand **how the database works, how to navigate it, and how to extend or audit it safely**.
