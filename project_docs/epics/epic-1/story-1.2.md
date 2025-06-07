# Story 1.2: System Map Data Model

## Status: Approved

## Story

As a system I want to implement the core System Map data model so that code relationships can be represented and navigated.

## Acceptance Criteria (ACs)

1. Node types are implemented: Files, Functions, Classes, Methods, Features (virtual)
2. Relationship types are implemented: Contains, Calls, Implements, Imports, Inherits, Depends-On
3. Metadata tracking includes line numbers, signatures, basic type information
4. Methods exist to traverse relationships in any direction
5. Data model supports efficient graph-based navigation

## Tasks / Subtasks

- [ ] **Define Node Type Enumeration** (AC: 1)
  - [ ] Create `NodeType` enum with File, Function, Class, Method, Feature values
  - [ ] Add node type validation and serialization methods
  - [ ] Document node type hierarchy and relationships

- [ ] **Define Relationship Type Enumeration** (AC: 2)
  - [ ] Create `RelationshipType` enum with Contains, Calls, Implements, Imports, Inherits, Depends-On
  - [ ] Add relationship type validation and constraints
  - [ ] Document valid relationship combinations between node types

- [ ] **Implement Node Data Model** (AC: 1, 3)
  - [ ] Create `Node` class with id, type, name, metadata attributes
  - [ ] Add metadata fields: line_numbers, signatures, type_info, file_path
  - [ ] Implement node serialization/deserialization (JSON)
  - [ ] Add node validation and equality methods

- [ ] **Implement Relationship Data Model** (AC: 2, 3)
  - [ ] Create `Relationship` class with source, target, type, metadata
  - [ ] Add relationship metadata: confidence, line_numbers, context
  - [ ] Implement relationship validation (valid type combinations)
  - [ ] Add relationship serialization/deserialization

- [ ] **Create System Map Core Class** (AC: 4, 5)
  - [ ] Implement `SystemMap` class using NetworkX DiGraph
  - [ ] Add methods: add_node(), add_relationship(), get_node(), remove_node()
  - [ ] Implement relationship traversal: get_relationships(), get_neighbors()
  - [ ] Add graph navigation: find_path(), get_subgraph(), get_dependencies()

- [ ] **Implement Graph Traversal Methods** (AC: 4, 5)
  - [ ] Add bidirectional relationship traversal
  - [ ] Implement filtered traversal by relationship type
  - [ ] Add depth-limited traversal methods
  - [ ] Create relationship query interface (find all calls to X, etc.)

- [ ] **Add Metadata Management** (AC: 3)
  - [ ] Implement metadata update and merge operations
  - [ ] Add metadata validation and schema enforcement
  - [ ] Create metadata search and filtering capabilities
  - [ ] Add metadata serialization for persistence

- [ ] **Create Performance Optimizations** (AC: 5)
  - [ ] Add node and relationship indexing
  - [ ] Implement efficient lookup by node type and name
  - [ ] Add relationship caching for frequent queries
  - [ ] Optimize memory usage for large graphs

- [ ] **Catalog System Maintenance (REQUIRED)**
  - [ ] Add new files to `project_docs/catalogs/project_catalog.yaml`
  - [ ] Update class/function listings for modified files in `project_catalog.yaml`
  - [ ] Update feature relationships in `project_docs/catalogs/feature_catalog.yaml`
  - [ ] Update tracking status for all modified files
  - [ ] Verify catalog entries align with implemented code

## Dev Technical Guidance

### Data Model Architecture

From `project_docs/supporting_documents/data-models.md`, the System Map implements a graph-based relationship model:

**Core Components:**
```python
# Node Types
class NodeType(Enum):
    FILE = "file"
    FUNCTION = "function" 
    CLASS = "class"
    METHOD = "method"
    FEATURE = "feature"  # Virtual nodes for feature boundaries

# Relationship Types
class RelationshipType(Enum):
    CONTAINS = "contains"       # File contains class, class contains method
    CALLS = "calls"            # Function calls another function
    IMPLEMENTS = "implements"   # Class implements interface
    IMPORTS = "imports"        # File imports from another file
    INHERITS = "inherits"      # Class inherits from another class
    DEPENDS_ON = "depends_on"  # General dependency relationship
```

### NetworkX Integration

From `project_docs/supporting_documents/tech_stack.md`:

**Graph Processing Requirements:**
- Use NetworkX 3.x DiGraph for directed relationship modeling
- Leverage NetworkX algorithms for path finding and traversal
- Implement efficient node and edge attribute storage
- Use NetworkX serialization for graph persistence

**Example Implementation Pattern:**
```python
import networkx as nx

class SystemMap:
    def __init__(self):
        self.graph = nx.DiGraph()
        self._node_index = {}  # Fast lookup by (type, name)
    
    def add_node(self, node: Node) -> None:
        self.graph.add_node(node.id, **node.to_dict())
        self._node_index[(node.type, node.name)] = node.id
```

### Metadata Schema

**Node Metadata Structure:**
```python
node_metadata = {
    "line_numbers": [start_line, end_line],
    "signature": "function_signature_string",
    "type_info": {
        "parameters": [...],
        "return_type": "...",
        "decorators": [...]
    },
    "file_path": "relative/path/to/file.py",
    "visibility": "public|private|protected"
}
```

**Relationship Metadata Structure:**
```python
relationship_metadata = {
    "confidence": 0.95,  # Parser confidence level
    "line_numbers": [call_site_line],
    "context": "method_call|import_statement|inheritance",
    "call_type": "direct|indirect|dynamic"
}
```

### Performance Considerations

From `project_docs/core_documents/architecture.md`:

**Scalability Requirements:**
- Support graphs with 10,000+ nodes efficiently
- Sub-second response for relationship queries
- Memory usage under 2GB for large codebases
- Incremental updates without full graph rebuild

### File Organization

**Module Structure:**
- `src/architectum/core/models/nodes.py` - Node and NodeType definitions
- `src/architectum/core/models/relationships.py` - Relationship models
- `src/architectum/core/system_map.py` - Main SystemMap class
- `src/architectum/core/graph_utils.py` - Graph traversal utilities

### Testing Requirements

**Unit Tests:**
- Node creation, validation, and serialization
- Relationship validation and constraints
- Graph operations (add, remove, query)
- Traversal algorithms and edge cases

**Integration Tests:**
- Large graph performance
- Memory usage validation
- Serialization/deserialization roundtrips

## Story Progress Notes

### Agent Model Used: `<Agent Model Name/Version>`

### Completion Notes List

{Any notes about implementation choices, difficulties, or follow-up needed}

### Change Log

| Date | Change | Author | Notes |
|------|--------|---------|-------|
| | Initial story creation | PO Agent | Complete story definition for Epic 1.2 |