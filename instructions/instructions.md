# 🗽 Quickstart

Welcome to the Architectum AI-guided engineering workspace.

**Your primary objective:**  
Build, document, and validate this project using XML-based system mapping and a shape-first workflow.

**Begin by:**
1. Read `project_overview.md`  
2. If approved, read `tech_onepager.md`  
3. If both are approved, continue to `plan.yaml`  
4. If `plan.yaml` is empty, reference `sample_plan.yaml`  
5. If no XML component files exist yet, reference `sample_component.xml`  
6. Load only the XML index named in the current plan's `xml_focus` field

---

# ⚙️ Execution Workflow

1. **Read `project_desc.md`:**
   - If `approved`: proceed to `tech_onepager.md`
   - If `in progress`: prompt user to edit it

2. **Read `tech_onepager.md`:**
   - If missing or incomplete, prompt user to describe the system technically

3. **Read `plan.yaml`:**
   - If empty: load `sample_plan.yaml` and build interactively
   - Skip all phases with `status: complete`
   - If any are `approved`, ask: _“Begin phase X or revise plan?”_
   - If all are `approved`, ask: _“Shall we begin phase X?”_

4. **Phase Setup:**
   - Load only the `docs` listed under current phase
   - Load only the XML index listed in `xml_focus`
   - Use it to locate and work within relevant modules

5. **Implementation:**
   - Generate a `.xml` for every new component
   - Define `<Function>`, `<Calls>`, `<Type>`s, etc.
   - Update the proper XML index using scripts

---

# 🗂 XML Index Strategy

Multiple indexes are defined in `plan.yaml > xml_groups`. Each group:
- Specifies which folders to combine
- Generates a `<group>_index.xml`
- Is selected via `xml_focus` per phase

---

# 📦 Output Requirements

- One `.xml` per file/module
- All function logic and data types documented
- References must be valid
- Use `build_xml_indexes.py` to update indexes

---

# 🧩 Language Support

You can extract structure using:

```bash
python scripts/arch_extract.py extract --lang <language> <path>
```

Supported values for `--lang`:
- `python` – Parses `.py` using AST
- `typescript` – Parses `.ts` using TypeScript compiler API
- `kotlin` – Parses `.kt` using regex
- `flutter` – Parses `.dart` files (Flutter modules)

Examples:
```bash
python scripts/arch_extract.py extract --lang python src/
python scripts/arch_extract.py extract --lang flutter lib/
```

Each file outputs a `.xml` component into your current folder.

---

# ⚖️ Build an XML Index

```bash
python scripts/build_xml_indexes.py
```
Uses `xml_groups` from your `plan.yaml` to create merged `*_index.xml` files.

---

# ✂️ Compare Index Files

```bash
python scripts/arch_extract.py diff-index new_index.xml old_index.xml
```
Generates a unified diff of architecture-level changes between XML snapshots.

---

# 🔹 Script Overview

- `arch_extract.py` – CLI for running extractors and diffs
- `extract_python.py` – Extracts structure from `.py`
- `extract_typescript.js` – Extracts structure from `.ts`
- `extract_kotlin.py` – Extracts structure from `.kt`
- `extract_flutter.py` – Extracts structure from `.dart`
- `build_xml_indexes.py` – Merges per-file XML into a grouped index
- `arch_diff_index.py` – Shows diff between two XML index files

---

# 📂 Reference Samples

- Use `sample_plan.yaml` if `plan.yaml` is missing
- Use `sample_component.xml` if no structure exists yet

---

# 🗃️ Engineering Principles

- Modular, testable, shape-driven architecture
- No business logic in UI or transport layers
- All changes are XML-documented and indexable
- Explicitness and composability favored over cleverness
- Maintain separation of frontend and backend modules unless merging is intentional
