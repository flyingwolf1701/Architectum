# Project Brief

## Introduction

Architectum addresses two parallel challenges in modern software development: AI comprehension limitations and human navigation difficulties in complex codebases. While these challenges manifest differently, they share a common solution in a relationship-based representation of code.

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

Architectum addresses both AI and human challenges through a dual representation approach:

1. **Relationship Map**: Models code as a network of nodes and relationships for efficient navigation
2. **JSON Mirrors**: Maintains detailed JSON representations of code files in a parallel structure
3. **Blueprints**: Creates specialized views by assembling elements from both core representations
4. **Feature Tagging**: Enables "virtual feature slices" across architectural boundaries

This approach bridges the gap between human-optimized code organization and comprehension patterns for both AI and humans.

## Vision & Goals

### Vision

To transform how both AI assistants and humans understand and interact with software systems by revealing the invisible network of relationships that define a codebase's true structure. Architectum aims to make any codebase comprehensible, navigable, and adaptable regardless of its underlying architectural pattern, enabling more efficient collaboration between humans and AI.

### Primary Goals (MVP)

1. **Dual Representation System**: Implement both a Relationship Map (for navigation efficiency) and JSON Mirrors (for content detail) to provide complementary views of the codebase.

2. **Blueprint Generation**: Create a system that assembles specialized views from the core representations, including File-Based Blueprints, Component-Based Blueprints, Feature Blueprints, and Temporary Blueprints.

3. **LSP-Powered Relationship Extraction**: Leverage Language Server Protocol to extract precise relationship data, including line numbers, call hierarchies, and type information, while minimizing processing overhead.

4. **Intelligent Caching & Incremental Updates**: Implement a blueprint caching strategy that only regenerates affected portions when code changes, maintaining blueprint accuracy without constant full reprocessing.

5. **YAML-Based Blueprint Definition**: Enable declarative specification of blueprint contents through YAML files, supporting both persistent documentation and ad-hoc exploration.

6. **Virtual Feature Slicing**: Enable the extraction of subgraphs representing logical features regardless of their physical distribution across the codebase.

7. **Format Optimization**: Generate blueprints in formats optimized for both AI consumption and human visualization.

8. **Proof-of-Concept Visualizer**: Develop a rudimentary web-based graph visualization that demonstrates the power of the relationship-centric approach.

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

## Technical Implementation

### Key Features for MVP

1. **Dual Representation Core**
   - Relationship Map: Efficient graph-based representation for navigation
   - JSON Mirrors: Detailed content representation mirroring code files

2. **Blueprint Types**
   - File-Based Blueprint: Combines selected files for comprehensive context
   - Component-Based Blueprint: Focuses on specific functions/classes within files
   - Feature Blueprint: Persistent documentation of a complete feature
   - Temporary Blueprint: Ad-hoc creation for immediate development tasks

3. **YAML-Based Blueprint Definition**
   - Declarative specification of blueprint contents
   - Support for various blueprint types and configurations
   - Persistent or temporary storage options

4. **LSP Integration**
   - Smart querying for relationship extraction
   - Parser abstraction for different languages
   - Initial support for TypeScript/JavaScript and Python

5. **Caching & Synchronization**
   - Blueprint storage for persistence
   - Change detection based on file hashes
   - Incremental updates for changed components
   - `arch sync` command for keeping representations up to date

6. **Output Formats**
   - Internal JSON structure for processing
   - AI-optimized format for consumption
   - Visualization-compatible output format

7. **CLI & API Access**
   - Comprehensive command-line interface
   - Programmatic API for integration

8. **Proof-of-Concept Visualizer**
   - Basic web-based graph visualization
   - Interactive navigation capabilities
   - Filter controls for focused views

### Technology Constraints

- **Initial Language Focus**: TypeScript/JavaScript and Python for MVP
- **LSP Dependency**: Reliance on language server quality and capabilities
- **Performance Considerations**: Balanced approach for large codebases
- **Token Efficiency**: Optimizing for AI context window limitations
- **Visualization Limits**: Managing complexity in graph visualization

## Post-MVP Considerations

1. **Enhanced Language Support**
   - Additional programming languages (Java, C#, Ruby, etc.)
   - Multi-language project support

2. **Advanced Graph Operations**
   - Impact analysis for proposed changes
   - Pattern detection and architectural conformance checking

3. **Advanced Feature Tagging**
   - AI-assisted feature association
   - Automatic boundary detection

4. **Enhanced Visualization**
   - 3D graph visualization
   - Time-based animation of code evolution

5. **IDE Integration**
   - VSCode plugin for inline visualization
   - Real-time blueprint generation

## Conclusion

Architectum represents a fundamental shift in how we think about code representation for both AI and human consumption. By providing a dual representation through both Relationship Maps and JSON Mirrors, along with specialized Blueprint views, it enables AI assistants and human developers to understand and navigate complex codebases with greater efficiency and clarity. The system bridges the gap between human-optimized architectures and AI-optimized comprehension patterns, creating a unified view that serves both audiences without compromising the underlying code organization.

_"Structure first, implementation second. Architectum reveals the invisible relationships that define how software really works."_