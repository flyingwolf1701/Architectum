status: approved
# Architectum Project Overview

## Vision

Architectum is an AI-first code comprehension system that transforms complex codebases into structured XML blueprints. By extracting and maintaining the architectural essence of code without implementation details, Architectum enables more effective collaboration between developers and AI assistants.

The project addresses the fundamental challenge of providing AI with the right level of contextual understanding of a codebase—detailed enough for meaningful assistance but abstracted enough to fit within token limitations and avoid overwhelming the AI with irrelevant implementation details.

## Core Concepts

- **Component-Based XML**: Every source file becomes a `<Component>` with structured representation of its key elements
- **Plan-Driven Focus**: Development phases in `plan.yaml` control what's actively being worked on
- **Language-Neutral Architecture**: Single unified representation across multiple programming languages
- **Scriptable Pipeline**: All tools are CLI-first for flexible integration into workflows

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

- Enhanced type information extraction
- Documentation comment extraction
- Improved relationship mapping between components
- Language Server Protocol integration

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

## Status

Architectum's core extraction and indexing capabilities are functional. The system is actively evolving toward richer relationship mapping, enhanced type information, and visualization capabilities. The immediate focus is on enhancing extractors to capture more detailed type information and relationships between components.

---

_"Architectum transforms code into conversation, making systems comprehensible to both humans and AI."_