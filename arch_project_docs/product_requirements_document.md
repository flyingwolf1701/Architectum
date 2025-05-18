# Architectum Product Requirements Document (PRD)

## Intro

Architectum aims to revolutionize how both AI assistants and humans understand and interact with complex codebases by providing a graph-based representation of code relationships. Rather than treating code as a hierarchy of files and directories, Architectum reveals the true network of relationships between code elements, enabling "virtual feature slices" that transcend the physical organization of code. This initial version (MVP) focuses on establishing the core capability of generating structured, graph-based blueprints that can be consumed by AI agents and visualized by human developers.

## Goals and Context

- **Project Objectives:**
    - To create a graph-based representation system that models code as a network of nodes and relationships
    - To enable AI agents to understand code structure and relationships across architectural boundaries
    - To provide developers with visualization tools for navigating complex code relationships
    - To implement "virtual feature slicing" that creates feature-oriented views regardless of physical code organization
    - To establish a foundation for intelligent, incremental updating of blueprints when code changes

- **Measurable Outcomes:**
    - Reduction in tokens required for AI to understand code structure (target: 70% reduction compared to raw code)
    - Improvement in AI task completion accuracy when using blueprints (target: 30% improvement)
    - Reduction in time required for developers to understand unfamiliar code (target: 40% reduction)
    - Relationship extraction accuracy (target: >90% of function calls correctly identified)
    - Blueprint update performance (target: <5 seconds for incremental updates on 100-file projects)

- **Success Criteria:**
    - The system successfully generates graph-based blueprints across all three types (Directory, FileSet, CodeElement)
    - Incremental updates correctly maintain blueprint accuracy after code changes
    - Generated blueprints can be consumed by AI agents to answer structure-related questions
    - Proof-of-concept visualization demonstrates the graph-based relationships

- **Key Performance Indicators (KPIs):**
    - Blueprint generation success rate
    - Relationship extraction accuracy percentage
    - Token efficiency ratio (tokens in blueprint vs. tokens in raw code)
    - Update performance metrics (time to regenerate after changes)
    - AI task performance improvement metrics

## Scope and Requirements (MVP / Current Version)

### Functional Requirements (High-Level)

#### 1. Graph-Based Code Model

- **1.1 Node Types**
  - The system must support representing files, functions, classes, methods, and features as nodes in the graph
  - Each node must have a unique identifier and type designation
  - Nodes must contain metadata appropriate to their type (e.g., line numbers, signatures)
  - The system must allow for tagging nodes with feature associations

- **1.2 Relationship Types**
  - The system must support explicit relationships between nodes:
    - Contains (file contains function, class contains method)
    - Calls (function calls function)
    - Implements (function implements feature)
    - Imports (file imports file)
    - Inherits (class extends class)
    - Depends-On (various dependency types)
  - Relationships must be directional with clear source and target
  - Relationships must include relevant metadata (e.g., line numbers where calls occur)

- **1.3 Graph Operations**
  - The system must support subgraph extraction based on nodes, relationships, or patterns
  - The system must enable traversal of the graph in any direction
  - The system must support filtering operations on the graph
  - The system must maintain referential integrity between nodes and relationships

#### 2. Blueprint Generation System

- **2.1 DirectoryBlueprint Generation**
  - The system must generate a graph representation of a specified directory structure
  - Users must be able to specify scan depth (e.g., 0 for all descendants, 1 for immediate children)
  - The blueprint must include file nodes and their contained code elements
  - Relationships between elements within the directory scope must be captured

- **2.2 FileSetBlueprint Generation**
  - The system must generate a graph based on a list of specified file paths
  - The blueprint must include the specified files and their contained code elements
  - Relationships between elements across the specified files must be captured
  - The system must handle invalid or missing files gracefully

- **2.3 CodeElementBlueprint Generation**
  - The system must generate a focused graph centered on specified code elements (functions, classes)
  - The blueprint must include the specified elements and their immediate relationships
  - The system must capture both callers and callees of the specified elements
  - The system must handle elements that cannot be found gracefully

- **2.4 Detail Level Configuration**
  - All blueprint types must support three detail levels:
    - **Minimal**: Basic structure and relationship information
    - **Standard**: Additional type information and signatures
    - **Detailed**: Comprehensive information including documentation
  - Detail levels must be applied consistently across all blueprint types
  - The system must respect detail level settings when generating output

#### 3. LSP Integration & Code Analysis

- **3.1 Language Server Protocol (LSP) Integration**
  - The system must connect to language servers for accurate code analysis
  - The system must extract precise relationship data, including line numbers
  - The system must leverage LSP for call hierarchy information
  - Initial support must focus on TypeScript/JavaScript and Python

- **3.2 Smart Querying**
  - The system must use targeted LSP queries to minimize analysis overhead
  - The system must detect file types and use appropriate language servers
  - The system must handle unsupported languages gracefully
  - The system must optimize query patterns for performance

- **3.3 Parser Abstraction**
  - The system must provide a consistent interface across different language parsers
  - The system must be extensible to support additional languages in the future
  - The system must normalize language-specific constructs into the common graph model
  - The system must handle language-specific features appropriately

#### 4. Caching & Incremental Updates

- **4.1 Blueprint Storage**
  - The system must store generated blueprints in a structured format
  - The system must include metadata about the generation process in stored blueprints
  - The storage format must efficiently represent the graph structure
  - The storage format must support incremental updates

- **4.2 Change Detection**
  - The system must track file hashes to detect changes
  - The system must identify which parts of the graph are affected by file changes
  - The system must support Git integration for change detection
  - The system must handle renamed or moved files appropriately

- **4.3 Incremental Updates**
  - The system must regenerate only affected portions of the graph when files change
  - The system must maintain relationship integrity during partial updates
  - The system must handle cascading effects of changes
  - The system must validate the consistency of the updated graph

#### 5. Output & Format Optimization

- **5.1 Internal Representation**
  - The system must use JSON for internal graph processing
  - The internal representation must be optimized for processing efficiency
  - The representation must preserve all node and relationship metadata
  - The representation must support serialization and deserialization

- **5.2 AI Consumption Format**
  - The system must generate output optimized for AI token efficiency
  - The system must support transformation to XML if it proves more efficient for AI
  - The output must be structured for easy traversal by AI
  - The output must include sufficient metadata for AI comprehension

- **5.3 Visualization Format**
  - The system must generate output suitable for graph visualization tools
  - The visualization format must support rendering nodes, edges, and labels
  - The format must include visual metadata (e.g., node types, relationship types)
  - The format must support interactive navigation

#### 6. Command-Line Interface & API

- **6.1 CLI Implementation**
  - The system must provide a command-line interface for blueprint generation
  - The CLI must support all blueprint types and detail levels
  - The CLI must include options for output format and destination
  - The CLI must provide clear error messages and help documentation

- **6.2 API Design**
  - The system must provide a programmatic API for integration
  - The API must support all blueprint generation capabilities
  - The API must follow consistent patterns and naming conventions
  - The API must include proper error handling and validation

#### 7. Proof-of-Concept Visualizer

- **7.1 Graph Rendering**
  - The system must include a basic web-based graph visualization component
  - The visualizer must render nodes and relationships from blueprint data
  - The visualizer must visually distinguish between node and relationship types
  - The visualizer must support zooming and panning operations

- **7.2 Interactive Features**
  - The visualizer must support clicking on nodes to view details
  - The visualizer must support following relationships between nodes
  - The visualizer must include basic filtering capabilities
  - The visualizer must support graph navigation operations

### Non-Functional Requirements (NFRs)

- **Performance:**
  - Blueprint generation must complete within reasonable time (target: <10s for 100-file projects)
  - Incremental updates must be significantly faster than full regeneration
  - The system must be memory-efficient when processing large codebases
  - The visualizer must handle rendering at least 200 nodes without performance degradation

- **Scalability:**
  - The architecture must support extension to additional programming languages
  - The graph model must scale to handle projects with thousands of files
  - The caching system must efficiently handle large blueprint storage
  - Processing overhead must grow sub-linearly with codebase size

- **Reliability/Availability:**
  - The system must handle malformed or unparseable code gracefully
  - Invalid inputs or parameters must result in clear error messages
  - The system must be resilient to LSP server failures
  - The caching system must maintain data integrity

- **Security:**
  - The system must handle code access according to repository permissions
  - The system must not compromise code privacy or intellectual property
  - The visualization must respect access controls on code elements
  - Blueprint storage must follow security best practices

- **Maintainability:**
  - The codebase must be modular and well-documented
  - The graph model must be extensible for future enhancements
  - The system must include comprehensive logging for troubleshooting
  - The architecture must allow for component upgrades or replacements

### User Experience (UX) Requirements

- **CLI Experience:**
  - Command structure must be intuitive and consistent
  - Parameters must follow standard CLI conventions
  - Help documentation must be comprehensive and accessible
  - Output formatting must be clear and readable

- **API Experience:**
  - API calls must be consistent and predictable
  - Method names must be descriptive and unambiguous
  - Documentation must include examples for common operations
  - Error messages must be actionable

- **Visualization Experience:**
  - The graph layout must present relationships clearly
  - Visual encoding must distinguish different node and relationship types
  - Navigation controls must be intuitive
  - Performance must remain smooth during interaction

### Integration Requirements

- **Version Control Integration:**
  - The system should support integration with Git for change detection
  - Blueprint updates can be triggered by Git hooks
  - Blueprints can be stored alongside code or in a separate repository

- **CI/CD Integration:**
  - The system should support integration with CI/CD pipelines
  - Blueprint generation can be triggered by continuous integration
  - Blueprint validation can be part of continuous delivery checks

- **IDE Integration (Future):**
  - The architecture should enable future IDE plugin development
  - The API should expose capabilities needed for IDE integration
  - The visualization format should be compatible with IDE rendering

## Epic Overview (MVP / Current Version)

### Epic 1: Core Blueprint Generation Framework and DirectoryBlueprint Implementation

**Goal:** To establish the foundational infrastructure for Architectum's codebase blueprint generation and deliver the `DirectoryBlueprint` capability, enabling AI agents and visualization tools to analyze specified directory structures at varying levels of detail.

### Epic 2: FileSetBlueprint Implementation

**Goal:** To enable Architectum to generate blueprints based on an explicit list of user-specified files (`FileSetBlueprint`), allowing AI agents and visualization tools to analyze a curated collection of code files at varying levels of detail.

### Epic 3: CodeElementBlueprint Implementation

**Goal:** To empower Architectum with the ability to generate highly focused blueprints detailing specific code elements (like functions, classes, methods) within a single file (`CodeElementBlueprint`), enabling AI agents to perform granular analysis.

### Epic 4: Graph Model Enhancement and Relationship Extraction

**Goal:** To implement the comprehensive graph-based code model with nodes and relationships, enhancing the blueprint types with rich relationship data extracted through LSP.

### Epic 5: Caching and Incremental Updates

**Goal:** To implement an intelligent caching system that stores blueprints and supports efficient incremental updates when code changes.

### Epic 6: Proof-of-Concept Visualization

**Goal:** To develop a basic web-based visualization component that renders blueprint graphs for human navigation and comprehension.

## Key Reference Documents

- `docs/project-brief.md`
- `docs/architecture.md`
- `docs/epic1.md`, `docs/epic2.md`, ...
- `docs/tech-stack.md`
- `docs/api-reference.md`
- `docs/graph-model.md`
- `docs/output-formats.md`

## Post-MVP / Future Enhancements

- **Enhanced Language Support:**
  - Expand to additional programming languages (Java, C#, Ruby, etc.)
  - Improve language-specific feature detection
  - Support multi-language projects

- **Advanced Graph Operations:**
  - Impact analysis (what would break if X changes)
  - Similarity detection between code elements
  - Pattern detection and architectural conformance checking

- **Advanced Feature Tagging:**
  - AI-assisted feature association
  - Feature boundary detection
  - Automatic tagging based on naming conventions or comments

- **Enhanced Visualization:**
  - Interactive 3D graph visualization
  - Time-based animation of code evolution
  - Customizable visual encoding

- **Collaboration Features:**
  - Shared annotations on the graph
  - Team-based feature ownership
  - Code review integration

- **Deeper Integration:**
  - IDE plugins
  - Code generation support
  - Integration with code quality tools

## Change Log

| Change        | Date       | Version | Description                  | Author         |
| ------------- | ---------- | ------- | ---------------------------- | -------------- |
| Initial draft | 05-17-2025 | 0.1     | Initial PRD with graph focus | Product Manager |

## Initial Architect Prompt

Based on our discussions and requirements analysis for the Architectum platform, I've compiled the following technical guidance to inform your architecture decisions:

### Technical Infrastructure

- **Module Integration:** The `arch_blueprint_generator` module should be integrated within the existing `Architectum` repository while maintaining clear separation of concerns.
- **Core Graph Model:** The foundation of the system should be a robust graph data model that represents code as a network of nodes and relationships.
- **LSP Integration:** The system should leverage Language Server Protocol for accurate code analysis, but with smart querying patterns to minimize overhead.
- **Caching Strategy:** Implement an efficient caching system that enables incremental updates rather than full regeneration.

### Key Architectural Decisions

1. **Graph Representation:** Design a flexible, extensible graph structure that can model the multi-dimensional nature of code relationships.
2. **Parser Abstraction:** Create a clean abstraction layer over language-specific parsing to enable future language support.
3. **Format Transformation:** Separate internal processing format (JSON) from AI consumption format (potentially XML) and visualization format.
4. **Update Strategy:** Design an intelligent, incremental update system that minimizes processing overhead.

### Technical Constraints

- **LSP Efficiency:** The system must use LSP judiciously to avoid performance bottlenecks.
- **Language Support:** Initial focus should be on TypeScript/JavaScript and Python.
- **Visualization Performance:** Graph rendering must handle at least 200 nodes smoothly.
- **Token Efficiency:** Output format must prioritize AI token efficiency.

### Deployment Considerations

- **Integration:** The system should support integration with Git, CI/CD, and potentially IDE plugins.
- **Automation:** Blueprint generation should be automatable through hooks and pipelines.
- **Standalone Operations:** The system should be usable both within and independent of the main Architectum application.

Please design an architecture that emphasizes the graph-based approach, with a focus on relationship extraction, incremental updates, and format optimization. The system should be modular, extensible, and performance-oriented, with clear boundaries between components. Consider both immediate implementation needs and future scalability as the system grows.