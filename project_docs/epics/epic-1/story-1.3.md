# Story 1.3: JSON Mirrors Structure

## Status: Draft

## Story

As a system I want to implement the JSON Mirrors structureso that detailed file content can be stored and accessed.

## Acceptance Criteria (ACs)

1. JSON representation structure for code files is defined
2. Functions, classes, methods, properties with full signatures are supported
3. Type information (parameter types, return types, property types) is captured
4. Import/export information and file-level declarations are preserved
5. Mirror structure parallels original codebase organization

## Tasks / Subtasks

- [ ] **Define JSON Mirror Schema** (AC: 1, 5)
  - [ ] Create JSON schema for file representation structure
  - [ ] Define mirror directory structure parallel to source code
  - [ ] Add file metadata: path, language, last_modified, hash
  - [ ] Implement schema validation for mirror consistency

- [ ] **Implement Function Representation** (AC: 2, 3)
  - [ ] Define function JSON structure: name, signature, parameters, return_type
  - [ ] Add function metadata: line_numbers, visibility, decorators, docstring
  - [ ] Capture parameter details: name, type, default_value, annotations
  - [ ] Include function body structure (statements, control flow)

- [ ] **Implement Class Representation** (AC: 2, 3)
  - [ ] Define class JSON structure: name, inheritance, methods, properties
  - [ ] Add class metadata: line_numbers, decorators, docstring, visibility
  - [ ] Capture inheritance hierarchy and implemented interfaces
  - [ ] Include class-level variables and constants

- [ ] **Implement Method Representation** (AC: 2, 3)
  - [ ] Define method JSON structure extending function representation
  - [ ] Add method-specific metadata: static, class method, property indicators
  - [ ] Capture method overrides and super() relationships
  - [ ] Include method visibility and access modifiers

- [ ] **Capture Import/Export Information** (AC: 4)
  - [ ] Define import structure: module, items, aliases, line_numbers
  - [ ] Track export declarations and public API definitions
  - [ ] Capture conditional imports and dynamic imports
  - [ ] Map import relationships to dependency graph

- [ ] **Implement File-Level Declarations** (AC: 4)
  - [ ] Capture module-level variables and constants
  - [ ] Track file-level docstrings and metadata
  - [ ] Include pragma declarations and encoding information
  - [ ] Capture file-level decorators and annotations

- [ ] **Create JSON Mirror Manager** (AC: 1, 5)
  - [ ] Implement `JSONMirror` class for file representation
  - [ ] Add `MirrorManager` for organizing multiple mirrors
  - [ ] Implement mirror creation, update, and deletion operations
  - [ ] Add mirror query interface for content access

- [ ] **Add Type Information Capture** (AC: 3)
  - [ ] Capture explicit type annotations and hints
  - [ ] Infer types from default values and usage patterns
  - [ ] Track generic types and type variables
  - [ ] Include union types and optional types

- [ ] **Implement Mirror Serialization** (AC: 1, 5)
  - [ ] Add JSON serialization/deserialization for mirrors
  - [ ] Implement compression for large mirror files
  - [ ] Add incremental update capabilities
  - [ ] Create mirror integrity validation

- [ ] **Catalog System Maintenance (REQUIRED)**
  - [ ] Add new files to `project_docs/catalogs/project_catalog.yaml`
  - [ ] Update class/function listings for modified files in `project_catalog.yaml`
  - [ ] Update feature relationships in `project_docs/catalogs/feature_catalog.yaml`
  - [ ] Update tracking status for all modified files
  - [ ] Verify catalog entries align with implemented code

## Dev Technical Guidance

### JSON Mirror Schema Design

From `project_docs/core_documents/architecture.md`, JSON Mirrors provide detailed content representation:

**File Mirror Structure:**
```json
{
  "file_info": {
    "path": "src/architectum/core/models.py",
    "language": "python",
    "last_modified": "2025-01-XX",
    "content_hash": "sha256_hash",
    "encoding": "utf-8"
  },
  "imports": [
    {
      "module": "typing",
      "items": ["Dict", "List", "Optional"],
      "line_number": 1,
      "alias": null
    }
  ],
  "functions": [...],
  "classes": [...],
  "module_variables": [...],
  "docstring": "Module-level documentation"
}
```

**Function Representation:**
```json
{
  "name": "process_file",
  "line_numbers": [45, 67],
  "signature": "def process_file(path: Path, config: Config) -> ProcessResult",
  "parameters": [
    {
      "name": "path",
      "type": "Path",
      "default": null,
      "annotation": "Path"
    }
  ],
  "return_type": "ProcessResult",
  "decorators": ["@staticmethod"],
  "docstring": "Process a single file...",
  "visibility": "public",
  "async": false
}
```

**Class Representation:**
```json
{
  "name": "SystemMap",
  "line_numbers": [10, 150],
  "inheritance": ["BaseGraph"],
  "interfaces": ["Serializable"],
  "methods": [...],
  "properties": [...],
  "class_variables": [...],
  "decorators": ["@dataclass"],
  "docstring": "Core system map class...",
  "visibility": "public",
  "abstract": false
}
```

### Mirror Directory Structure

**Parallel Organization:**
```
src/architectum/
├── core/
│   ├── models.py
│   └── system_map.py
└── parsers/
    └── python_parser.py

mirrors/
├── core/
│   ├── models.json      # Mirror of models.py
│   └── system_map.json  # Mirror of system_map.py
└── parsers/
    └── python_parser.json
```

### Type Information Capture

**Type Annotation Handling:**
```json
{
  "type_info": {
    "explicit_annotation": "Dict[str, List[Node]]",
    "inferred_type": "Dict[str, List[Node]]",
    "generic_parameters": ["str", "List[Node]"],
    "optional": false,
    "union_types": null
  }
}
```

### Implementation Architecture

**Core Classes:**
- `src/architectum/core/mirrors/json_mirror.py` - Single file mirror
- `src/architectum/core/mirrors/mirror_manager.py` - Mirror collection management
- `src/architectum/core/mirrors/schema.py` - JSON schema definitions
- `src/architectum/core/mirrors/serialization.py` - Mirror persistence

### Performance Considerations

From `project_docs/core_documents/prd.md`:

**Scalability Requirements:**
- Support mirrors for 10,000+ files
- Fast content lookup and filtering
- Incremental mirror updates
- Memory-efficient mirror loading

### Integration with System Map

**Relationship to System Map:**
- Mirrors provide detailed content for System Map nodes
- System Map provides navigation, Mirrors provide implementation details
- Both systems must maintain consistency during updates
- Mirrors feed detailed information for blueprint generation

## Story Progress Notes

### Agent Model Used: `<Agent Model Name/Version>`

### Completion Notes List

{Any notes about implementation choices, difficulties, or follow-up needed}

### Change Log

| Date | Change | Author | Notes |
|------|--------|---------|-------|
| | Initial story creation | PO Agent | Complete story definition for Epic 1.3 |