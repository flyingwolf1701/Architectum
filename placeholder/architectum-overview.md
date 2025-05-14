# Architectum Project Overview

## Vision

Architectum is an AI-first code comprehension system that transforms complex codebases into structured XML blueprints. By extracting and maintaining the architectural essence of code—without implementation details—Architectum optimizes AI-human collaboration for software development, making AI assistants more effective partners in understanding, planning, and modifying code.

## Core Concepts

- **Component-Based XML Extraction**: Each source file becomes a `<Component>` with structured representation of functions, types, and relationships
- **Plan-Driven Focus**: Development phases in `plan.yaml` control what's actively being worked on
- **Language-Neutral Architecture**: Cross-language support provides unified representation across technology stacks
- **Relationship Mapping**: Track dependencies, imports, and interactions between components
- **Visualizable Structure**: Generate navigable views of system architecture

## System Pillars

### 1. Structure Extraction

- Extract code structure into XML components from:
  - Python (using AST)
  - TypeScript (using TS Compiler API)
  - Kotlin (regex-based, to be enhanced)
  - Flutter/Dart (regex-based, to be enhanced)
- Capture functions, types, parameters, and return values
- Extract documentation comments to provide context
- Map relationships between components

### 2. Index Management

- Generate focused XML indexes for different parts of the system
- Merge component XMLs based on configuration in `plan.yaml`
- Track architectural evolution through XML diffing
- Provide targeted context for AI assistance

### 3. Relationship Mapping

- Track dependencies between components
- Map function calls across module boundaries
- Visualize inheritance and composition relationships
- Generate dependency graphs for system understanding

### 4. Type Information

- Extract detailed type signatures
- Map parameter types and return values
- Track generics and type constraints
- Document data flow through the system

### 5. Visualization Layer

- Web-based interface for exploring component relationships
- Interactive dependency graphs
- Code structure navigation
- Timeline view of architectural evolution

## Applications

### AI Assistance Enhancement

- Provide AI with focused structural context without implementation details
- Enable precise contextual understanding for code generation
- Support planning and architectural discussions
- Optimize token usage in AI context windows

### Developer Tools

- Visualize system architecture and dependencies
- Track architectural drift over time
- Document code structure automatically
- Onboard new team members quickly

### Technical Documentation

- Generate structural documentation from code
- Maintain living architecture diagrams
- Track API evolution over time
- Support technical decision making

## Implementation Roadmap

### Phase 1: Core Extraction (Current)

- ✅ Basic extractors for Python, TypeScript, Kotlin, and Flutter
- ✅ Component-based XML structure
- ✅ Index generation and diffing
- ✅ Plan-based workflow

### Phase 2: Enhanced Structure Extraction

- Language Server Protocol integration for more accurate parsing
- Enhanced type information extraction
- Documentation comment extraction
- Improved relationship mapping between components

### Phase 3: Visualization and Navigation

- Web-based visualization of component relationships
- Interactive dependency graphs
- Timeline view of architectural evolution
- Component and relationship navigation

### Phase 4: Integration and Ecosystem

- Editor/IDE plugins
- CI/CD integration for tracking architectural changes
- API for third-party tool integration
- Extensible plugin system for custom extractors

## Technical Stack

### Current

- Python for CLI tools and orchestration
- TypeScript for web-based extractors
- XML for structure representation
- YAML for configuration

### Planned Extensions

- LSP integration for improved parsing
- Web-based visualization layer (React/TypeScript)
- Graph database for relationship queries
- Language-specific parser improvements

## Engineering Principles

- Explicit structure over inferred behavior
- Component-aligned mapping
- Black box testability
- Separation of structure from implementation
- Composable, declarative formats
- Visualizable architecture

## Status

Architectum's core extraction and indexing capabilities are functional. The system is actively evolving toward richer relationship mapping, enhanced type information, and visualization capabilities.

---

_"Architectum transforms code into conversation, making systems comprehensible to both humans and AI."_
