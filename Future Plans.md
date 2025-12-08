# Turning This Repo into a Full RAG Stack

This document outlines what’s left to do to turn **HOI4-AI-Reference-Data** from a static knowledge base into a **full Retrieval-Augmented Generation (RAG) stack** that AIs and tools can use in production.

---
## 1. Goals and Target Behavior
**Primary goal**: When a user asks any HOI4-modding question, the system should:
1. Interpret the question (error vs. design vs. lookup).
2. Route it to the **right domain(s)** using `master_index.json` intents.
3. Retrieve only the **most relevant chunks** from this repo.
4. Feed those chunks into an LLM that:
   - Explains mechanics correctly.
   - Surfaces relevant edge cases.
   - Points to the correct files/sections when needed.

This is **strictly better** than “dump entire repo into context” because:
- Context windows are finite and noisy when overfilled.
- Routing + retrieval improves **precision** and reduces hallucinations.
- It supports **updates** without retraining (just re-indexing).

---
## 2. Data Ingestion and Chunking
### 2.1 Normalizing file metadata
For each `.md` file:
- Extract:
  - `domain`, `concept`, `version` from YAML frontmatter.
  - File path and filename.
- Store as **document-level metadata** in your index (e.g. `{domain: "map", concept: "provinces", version: "1.14+"}`).

This metadata will drive:
- Domain-level filtering (e.g. only search `map` and `core` for map errors).
- Intent-based routing (as defined in `master_index.json`).

### 2.2 Chunking strategy
Because these files are already semantically cohesive:
- Prefer **section-based chunks** rather than naïve fixed-size splits.
- For each file:
  - Split on headings (`#`, `##`, `###`) into logical sections.
  - Keep chunk sizes roughly **500–1500 tokens** (merge smaller sections when needed).
  - Attach **section-level metadata**:
    - `file_path`
    - `section_heading`
    - `section_anchor` (for deep linking in answers)
    - `domain`, `concept` from frontmatter.

For large enumeration files:
- `modifiers_list/*`, `defines_list/*`:
  - Chunk by **logical groups** (tables / YAML blocks per category) to keep lookups atomic and fast.

---
## 3. Embeddings and Indexing
### 3.1 Embedding model
Choose a text embedding model appropriate to your LLM stack (e.g. OpenAI, local embeddings). Requirements:
- Handles **code + prose** reasonably well.
- Supports multilingual text if you expect non-English loc.
### 3.2 Vector index
Create a vector index over all **chunks**, storing:
- The embedding.
- The section text.
- Metadata (domain, concept, file_path, section_heading, section_anchor, version, etc.).

Optional:
- Also maintain a **keyword index** (BM25 or similar) for:
  - Exact define names.
  - Modifier names.
  - Error strings (e.g. `MAP_ERROR`, `X4008`).

A **hybrid retriever** (embeddings + keyword search) works best for:
- Precise identifiers (`COMBAT_WIDTH`, `autonomy_gain_trade`).
- General conceptual questions (“how do supply nodes work?”).

---
## 4. Router Logic Using `master_index.json`
### 4.1 Intent detection
Given a user query:
1. Extract obvious signals:
   - Error lines.
   - Filenames / extensions.
   - Keywords (defines, modifiers, events, map terms, etc.).

1. Compare against `signals` in each route in `master_index.json`:
   - **Score** how many `keywords`, `error_log_contains`, or `file_hint` entries match.
   - Select 1–3 best-matching **intents**.

This can be:
- A simple rules engine, or
- A small classifier that proposes likely intents and then checks signals.
### 4.2 Domain and file narrowing
For each chosen intent:
- Take its `domain` and:
  - Restrict retrieval to chunks where `metadata.domain == domain`.
- Use `primary_targets` and `secondary_targets`:
  - Boost relevance for chunks from `primary_targets` files.
  - Still allow results from `secondary_targets` but with lower weight.

This yields a focused search context for your retriever:
- Example: `map_error` intent:
  - Domain: `map`.
  - High priority: `map/troubleshooting.md`, `map/provinces.md`, `map/coordinates.md`.

---
## 5. Retrieval-Oriented Prompt Orchestration
### 5.1 System prompt design
Your system prompt should:
- Summarize the **design philosophy** (you can lift from `README.md`):
  - Edge cases are inline.
  - Respect mechanics vs enumeration splits.
  - Use file references only when helpful.
- Instruct the model to:
  - Prefer **grounded answers** using retrieved context.
  - Note **version-specific behavior** if relevant.
  - Surface **critical warnings** found in chunks (especially `[!CRITICAL]` blocks)

### 5.2 Context assembly
Pipeline per query:
1. Detect intent(s) via `master_index.json`.
2. Use narrowed filters to retrieve top **N** chunks (e.g. 6–12).
3. Build a prompt:
   - Brief restatement of user question.
   - Short explanation of chosen domain/intent (optional).
   - Selected chunks, each separated and labeled (e.g. by file and heading).
4. Ask the LLM:
   - To answer **only** based on the provided context and its known HOI4 basics.
   - To mention file names/sections when that helps the user navigate.

For **lookup** intents (`modifier_lookup`, `define_lookup`):
- You can implement **two-stage retrieval**:
  - Stage 1: Find likely categories (e.g. `NMilitary`, `military_land.md`).
  - Stage 2: Search only within those category files for the exact name/pattern.

---
## 6. Tooling and API Surface
### 6.1 Core tools
For an agent-style system, you will want at least:
- `search_docs(query, domain_filter?, file_filter?, intent_hint?)`
  - Wraps the vector/keyword retrieval.
  - Uses domain + intent data from `master_index.json`.
- `read_file_snippet(path, anchor_or_range)`
  - For deep dives once the model knows a specific file/section.
- Optional: `list_intents()` / `describe_intent(name)`
  - Reads from `master_index.json`.
  - Helps explain to users why a question was routed a certain way.
### 6.2 Logging for feedback
Log, per query:
- Chosen intent(s) and domain(s).
- Which chunks were retrieved (file + section).
- Whether the answer solved the issue (if you can instrument feedback).

Use this to:
- Refine `signals` in `master_index.json`.
- Adjust chunking parameters.
- Add new intents if you see repeated “odd” routes.

---
## 7. Evaluation and Iteration
### 7.1 Test suites
Create a small but diverse test set:
- **Crashes**: Known CTD patterns and their expected root-cause explanations.
- **Design tasks**: “Add a new doctrine tree”, “create a civil war path”, etc.
- **Lookup tasks**: “What modifiers affect naval detection?”, “Where is COMBAT_WIDTH defined?”.

For each:
- Check that:
  - Routing chooses the right intent/domain.
  - Retrieved chunks include the right files.
  - The LLM’s answer:
    - References correct behavior.
    - Uses warnings and edge cases correctly.
### 7.2 Manual and automated review
- Have human modders review a subset of answers.
- Optionally, add automated checks:
  - Does the answer mention a file that doesn’t exist?
  - Does it suggest a define or modifier name that doesn’t exist?

---
## 8. Optional: UI and Multi-Agent Flows
Once the core RAG stack is stable, you can build:
- **CLI / DevTool integration**
  - A command-line tool where modders paste errors or questions and get grounded answers.
- **IDE assistants**
  - Integrate with your editor (VSCode, etc.) so that:
    - Selecting a piece of script + asking “explain this” uses the right domain.