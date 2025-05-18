# Architectum Project Brief

## Introduction

Architectum addresses two parallel challenges in modern software development: AI comprehension limitations and human navigation difficulties in complex codebases. While these challenges manifest differently, they share a common solution in a graph-based representation of code relationships.

## Problem #1: AI Comprehension Barriers

AI assistants face significant challenges when working with modern codebases:

- **Context Window Limitations**: AI models have fixed token limits, making it impossible to load entire codebases into context.
- **Architectural Mismatch**: Production code typically uses layered or modular architectures that distribute feature code across multiple files and directories.
- **Feature Fragmentation**: Understanding a complete feature often requires seeing dozens of scattered files simultaneously.
- **Implementation Noise**: Raw code contains too much implementation detail, diluting the architectural signal AI needs.

This creates an inherent tension: the architectures best for human development teams are often worst for AI comprehension.

## Problem #2: Human Navigation Challenges

Developers struggle with their own navigation and comprehension difficulties:

- **Mental Model Limitations**: Humans cannot hold complex multi-dimensional relationships in memory.
- **Call Flow Tracing**: Following execution paths across architectural boundaries is mentally taxing.
- **Feature Discovery**: Identifying all code elements related to a specific feature is time-consuming.
- **Relationship Visualization**: Standard file trees fail to represent the network nature of code relationships.
- **Onboarding Friction**: New team members face steep learning curves understanding how code connects.

Current tools primarily offer hierarchical views (file trees) that fail to capture the network of relationships that define how code actually functions.

## A Unified Solution

Architectum addresses both AI and human challenges through a graph-based code representation that:

1. Models code as a network of nodes and relationships
2. Enables "virtual feature slices" across architectural boundaries
3. Provides multiple perspectives on the same underlying structure
4. Maintains the actual codebase in its optimal architecture

This approach bridges the gap between human-optimized code organization and comprehension patterns for both AI and humans.

## Vision & Goals

### Vision

To transform how both AI assistants and humans understand and interact with software systems by revealing the invisible network of relationships that define a codebase's true structure. Architectum aims to make any codebase comprehensible, navigable, and adaptable regardless of its underlying architectural pattern, enabling more efficient collaboration between humans and AI.

### Primary Goals (MVP)

1. **Graph-Based Blueprint Generation**: Create a system that models codebases as networks with explicit nodes (files, functions, classes, features) and relationships (contains, calls, implements, depends-on), representing the multi-dimensional nature of code.

2. **LSP-Powered Relationship Extraction**: Leverage Language Server Protocol to extract precise relationship data, including line numbers, call hierarchies, and type information, while minimizing processing overhead.

3. **Intelligent Caching & Incremental Updates**: Implement a blueprint caching strategy that only regenerates affected portions when code changes, maintaining blueprint accuracy without constant full reprocessing.

4. **Multiple Blueprint Perspectives**: Support directory-based, file-based, and element-based blueprint generation, with all views derived from the underlying graph model.

5. **Virtual Feature Slicing**: Enable the extraction of subgraphs representing logical features regardless of their physical distribution across the codebase.

6. **Format Optimization**: Generate blueprints in formats optimized for both AI consumption and human visualization.

7. **Proof-of-Concept Visualizer**: Develop a rudimentary web-based graph visualization that demonstrates the power of the relationship-centric approach.

### Success Metrics

- **AI Context Efficiency**: Reduction in token count required to provide equivalent architectural context to an AI model compared to raw source code.

- **AI Task Performance**: Measurable improvement in an AI's ability to perform code-related tasks when using Architectum blueprints versus traditional context.

- **Developer Comprehension Speed**: Reduction in time required for developers to understand unfamiliar code structures when using Architectum visualizations.

- **Relationship Accuracy**: Percentage of function calls and relationships correctly identified across architectural boundaries.

- **Update Performance**: Time taken to update blueprints after code changes, with particular focus on incremental update efficiency.

- **Feature Slice Completeness**: Coverage of virtual feature slices as measured by the inclusion of all relevant code elements.

## Target Audience & Use Cases

### For AI Assistants

- **Profile**: LLM-based coding assistants operating with limited context windows
- **Needs**:
  - Precise structural context without implementation noise
  - Ability to follow relationships across architectural boundaries
  - Feature-oriented views regardless of physical code organization
  - Token-efficient representation of code structure
- **Use Cases**:
  - **Feature Analysis**: "Explain how the authentication feature works across the codebase"
  - **Impact Assessment**: "What would be affected if I change this function?"
  - **Code Generation**: "Add error handling to this function considering all its callers"
  - **Refactoring Guidance**: "How should I extract this functionality into a separate module?"

### For Developers

- **Profile**: Software engineers working on complex, unfamiliar, or large-scale codebases
- **Needs**:
  - Visual representation of code relationships
  - Easy navigation of call flows and dependencies
  - Feature-centric views across architectural boundaries
  - Quick onboarding to unfamiliar code
- **Use Cases**:
  - **Codebase Exploration**: Visually navigate complex relationships to understand structure
  - **Feature Mapping**: Identify all components related to a specific feature
  - **Impact Analysis**: Visualize what would be affected by changes to a component
  - **Architecture Communication**: Share and discuss system architecture through relationship graphs
  - **Onboarding**: Help new team members understand system organization quickly

### For Technical Leads & Architects

- **Profile**: Engineers responsible for system design and architectural decisions
- **Needs**:
  - High-level system visualization
  - Architectural pattern validation
  - Communication tools for team alignment
  - Impact assessment for design changes
  - **Code ownership tagging and mapping**
- **Use Cases**:
  - **Architectural Validation**: Verify implementations match intended design patterns
  - **Dependency Analysis**: Identify problematic dependencies or cycles
  - **Design Communication**: Share and explain architectural decisions visually
  - **Technical Debt Assessment**: Identify areas where implementation diverges from design
  - **Ownership Tagging**: Associate components with specific teams, individuals, or domains
  - **Responsibility Mapping**: Quickly identify who to consult when making changes to specific areas
  - **Contribution Visualization**: See ownership distribution across the system's architecture

## Key Features / Technical Scope (MVP)

### 1. Graph-Based Code Model

- **Node Types**: Files, Functions, Classes, Methods, Features (virtual)
- **Relationship Types**: Contains, Calls, Implements, Imports, Inherits, Depends-On
- **Metadata**: Line numbers, signatures, types, documentation references
- **Subgraph Extraction**: Ability to create focused views based on nodes or relationships
- **Traversal Support**: Methods to navigate the graph in any direction

### 2. Blueprint Generation System

- **DirectoryBlueprint**: Graph representation of a directory with its code elements
- **FileSetBlueprint**: Custom graph slice based on a specific list of files
- **CodeElementBlueprint**: Focused subgraph centered on specific functions or classes
- **Detail Levels**: Minimal (structure), Standard (types), Detailed (documentation)
- **Feature Tagging**: Association of elements with logical features (manual or AI-assisted)

### 3. LSP Integration

- **Smart Querying**: Targeted LSP queries for relationship extraction
- **Parser Bridge**: Abstraction over different language servers
- **Line Information**: Precise location tracking for all elements
- **Call Hierarchy Extraction**: Function-to-function call relationships
- **Initial Language Support**: TypeScript/JavaScript and Python

### 4. Caching & Update System

- **Blueprint Storage**: Efficient storage format for graph representation
- **Change Detection**: File hash-based change tracking
- **Incremental Updates**: Partial graph regeneration for changed components
- **Git Integration**: Support for hooking into version control events

### 5. Output Formats

- **Internal Representation**: JSON-based graph structure for processing
- **AI Consumption Format**: Semantic, structured format (potentially XML)
- **Visualization Format**: Graph-compatible output for rendering tools
- **Format Conversion**: On-demand transformation between formats

### 6. Command-Line Interface

- **Blueprint Generation**: Commands for generating different blueprint types
- **Detail Selection**: Options for controlling output detail level
- **Feature Filtering**: Ability to filter by tagged features
- **Output Control**: Format and destination options

### 7. Proof-of-Concept Visualizer

- **Graph Rendering**: Basic visualization of blueprint graph structure 
- **Relationship Navigation**: Ability to follow connections between nodes
- **Filter Controls**: Options to focus the view on specific aspects
- **Export Capability**: Save or share visualizations

## Technical Approach & Constraints

### Implementation Strategy

- **Progressive Enhancement**:
  1. Start with file-level analysis and basic graph structure
  2. Add function relationship mapping
  3. Implement feature tagging
  4. Build visualization capabilities

- **Hybrid Processing Model**:
  - Use LSP for accurate relationship extraction
  - Leverage scripts and automation for efficiency
  - Implement caching to minimize redundant processing
  - Integrate with development workflows for automatic updates

- **Format Flexibility**:
  - JSON for internal processing
  - Potentially XML for AI consumption (evaluating token efficiency vs. semantic clarity)
  - Visualization-optimized formats for human consumption

### Technical Constraints

- **Initial Language Focus**: TypeScript/JavaScript and Python for MVP
- **LSP Dependency**: Reliance on language server quality and capabilities
- **Performance Considerations**: Balanced approach for large codebases
- **Token Efficiency**: Optimizing for AI context window limitations
- **Visualization Limits**: Managing complexity in graph visualization

### Potential Risks

- **Graph Complexity Management**: Ensuring the representation remains manageable
- **Update Efficiency**: Maintaining accuracy with incremental updates
- **Language Support Variability**: Differences in LSP implementation quality
- **Feature Association Maintenance**: Keeping feature tags current
- **Visualization Scalability**: Rendering large graphs effectively

## Roadmap Overview

### Phase 1: Core Blueprint Generation

- Establish graph data model
- Implement basic LSP integration
- Create directory blueprint generation
- Set up caching framework
- Implement CLI interface

### Phase 2: Relationship Mapping

- Implement function-to-function relationship extraction
- Add file dependency mapping
- Create file set blueprint functionality
- Enhance detail levels

### Phase 3: Feature Slicing & Element Blueprint

- Implement feature tagging system
- Create virtual feature slice capability
- Add code element blueprint generation
- Optimize for AI consumption

### Phase 4: Visualization & Enhancement

- Create proof-of-concept visualizer
- Implement format transformations
- Add CI/CD integration
- Expand language support

## Conclusion

Architectum represents a fundamental shift in how we think about code representation for both AI and human consumption. By modeling code as a graph of relationships rather than a hierarchy of files, it enables both AI assistants and human developers to understand and navigate complex codebases with greater efficiency and clarity. The system bridges the gap between human-optimized architectures and AI-optimized comprehension patterns, creating a unified view that serves both audiences without compromising the underlying code organization.

---

_"Structure first, implementation second. Architectum reveals the invisible relationships that define how software really works."_