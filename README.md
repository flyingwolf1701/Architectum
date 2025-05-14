# Architectum

**Blueprints of living systems.**

Architectum is a high-efficiency documentation, analysis, and validation system for large codebases. It empowers AI agents and developers to reason about systems at a structural level—across multiple programming languages—by generating and maintaining declarative XML maps of your code.

## Purpose
Architectum is designed for:
- **AI-native code analysis** — minimal token use, high structure-to-noise ratio
- **Phase-based planning** — roadmap-driven execution via `plan.yaml`
- **Code comprehension** — trace relationships, shapes, and changes across files
- **Component visualization** — (future) navigation across modules and APIs

## Key Concepts
- **Component-based XML** — Every source file becomes a `<Component>`
- **Plan-driven focus** — The `xml_focus` field in `plan.yaml` controls what is active
- **Language-neutral architecture** — Supports Python, TypeScript, Kotlin, and Flutter (Dart)
- **Scriptable pipeline** — All tools are CLI-first for agent or dev usage

## Structure Overview
```
architectum/
├── instructions/           # Bootstrap control docs
│   ├── instructions.md     # AI runner script
│   ├── project_overview.md # Product manager's vision
│   ├── tech_onepager.md    # Technical one-pager
│   ├── plan.yaml           # Phase/action XML plan
│   ├── sample_plan.yaml
│   └── sample_component.xml
│
├── scripts/                # Structure and diff utilities
│   ├── arch_extract.py     # CLI wrapper for extract/diff
│   ├── extract_python.py
│   ├── extract_typescript.js
│   ├── extract_kotlin.py
│   ├── extract_flutter.py
│   ├── build_xml_indexes.py
│   └── arch_diff_index.py
│
├── structure/              # Output per component
│   ├── *.xml               # One per file
│   └── *_index.xml         # Merged group views
```

## Usage
```bash
# Extract code structure
python scripts/arch_extract.py extract --lang python path/to/code

# Build XML index from components
python scripts/build_xml_indexes.py

# Compare XML structure diffs
python scripts/arch_extract.py diff-index new_index.xml old_index.xml
```

## Engineering Principles
- Black box testability
- Explicit structure over inferred behavior
- Modular, component-aligned mapping
- Composable, declarative file formats
- Maintainability over cleverness

## Status
Architectum is actively evolving. Visual explorer tooling and editor integration are on the roadmap.

---

_“Architectum doesn’t just document code. It equips systems for intelligent conversation.”_
