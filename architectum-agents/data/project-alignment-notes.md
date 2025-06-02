# Project Alignment Notes: Architectum & ARCHITECTUM Agent Integration

## Overview

This document outlines the alignment between the Architectum project structure and the ARCHITECTUM agent system, ensuring both approaches work harmoniously.

## Key Alignments Made

### 1. File Path Structure Alignment

**Architectum Project Structure:**

```
docs/
├── catalogs/
│   ├── project_catalog.yaml
│   ├── feature_catalog.yaml
│   └── test_catalog.yaml
├── core_documents/
│   ├── architecture.md
│   ├── prd.md
│   └── project_brief.md
├── epics/
│   ├── epic_1/
│   │   ├── epic-1.md
│   │   ├── story-1.1.md
│   │   ├── story-1.2.md
│   │   ├── story-1.3.md
│   │   ├── story-1.4.md
│   │   └── ...
│   ├── epic_2/
│   │   ├── epic-1.md
│   │   ├── story-1.1.md
│   │   ├── story-1.2.md
│   │   ├── story-1.3.md
│   │   ├── story-1.4.md
│   │   └── ...
│   └── ...
├── supporting_documents/
└── index.md
```

**ARCHITECTUM Agent References Updated:**

- ✅ Updated `create-next-story-task.md` to use `docs/epics/epic_{n}/` structure
- ✅ Updated `dev.ide.md` persona to reference correct paths
- ✅ Updated story file creation to use `docs/epics/epic_{epicNum}/story-{epicNum}.{storyNum}.md`

### 2. Documentation Reference Alignment

**Core Documents Referenced:**

- `docs/core_documents/architecture.md` ✅
- `docs/core_documents/prd.md` ✅
- `docs/core_documents/project-brief.md` ✅
- `docs/supporting_documents/` hierarchy ✅
- `docs/index.md` as navigation hub ✅

### 3. Catalog System Integration

Both approaches now emphasize:

- ✅ Maintaining `project_catalog.yaml` with file inventory
- ✅ Maintaining `feature_catalog.yaml` with feature mapping
- ✅ Maintaining `test_catalog.yaml` with test mapping
- ✅ Updating catalogs as part of story completion
- ✅ Using catalogs for dependency understanding

### 4. Testing & Quality Standards

Aligned requirements:

- ✅ ≥80% unit test coverage (pytest + pytest-cov)
- ✅ Story DoD checklist validation
- ✅ QA Testing Guide creation
- ✅ TODO-revert.md for debug tracking

### 5. Workflow Consistency

**Standalone dev_agent.md approach:**

- Epic ID selection → Load docs → Find incomplete story → Execute → DoD → Review

**ARCHITECTUM Orchestrator approach:**

- Agent selection → Story task loading → Context gathering → Execute → DoD → Review

Both approaches now use the same:

- ✅ Story file structure and location
- ✅ Catalog maintenance requirements
- ✅ DoD checklist validation
- ✅ Testing standards

## Key Differences (By Design)

### Standalone vs Orchestrated

- **dev_agent.md**: Direct, focused developer agent for IDE use
- **ARCHITECTUM agents**: Orchestrated team approach with specialized roles

### Scope & Context

- **dev_agent.md**: Story-focused with minimal context switching
- **ARCHITECTUM agents**: Full project lifecycle with role-based expertise

## Usage Recommendations

### Use Standalone dev_agent.md when:

- Working directly in IDE (Cursor, Windsurf, etc.)
- Focused on story implementation only
- Want minimal agent complexity
- Need maximum implementation focus

### Use ARCHITECTUM Orchestrator when:

- Need full project lifecycle management
- Want role-based agent expertise (PM, Architect, etc.)
- Working in environments supporting agent orchestration
- Need cross-functional team simulation

## Implementation Notes

