# Architectum Product Requirements Document (PRD)

## Goal, Objective and Context

**Primary Goal:** Transform code comprehension for both AI assistants and human developers by creating a relationship-based representation system that reveals the invisible network of connections defining how software actually functions.

**Core Objectives:**
1. **Bridge the AI-Human Gap:** Enable AI assistants to understand complex codebases despite context window limitations and architectural fragmentation
2. **Enhance Developer Navigation:** Provide developers with powerful tools to visualize and navigate code relationships across architectural boundaries
3. **Accelerate Onboarding:** Reduce time required for developers to understand unfamiliar code structures through relationship-centric views

**Problem Context:** 
Modern software development faces parallel challenges - AI models cannot comprehend entire codebases due to token limits and architectural distribution, while developers struggle with mental model limitations when navigating complex relationship networks. Current tools offer only hierarchical views that fail to capture the true network nature of code functionality.

**Solution Approach:**
Architectum addresses these challenges through a three-component architecture: System Map (graph-based navigation), JSON Mirrors (detailed content representation), and Blueprints (specialized AI-optimized views). This unified approach serves both AI comprehension patterns and human navigation needs without compromising underlying code organization.

## Functional Requirements (MVP)

**FR1: System Map Core**
- Maintain graph-based relationship model for efficient navigation
- Support for multiple node types: Files, Functions, Classes, Methods, Features (virtual)
- Support for relationship types: Contains, Calls, Implements, Imports, Inherits, Depends-On
- Metadata tracking including line numbers, signatures, and basic type information
- Methods to traverse relationships in any direction

**FR2: JSON Mirrors Core**
- Maintain detailed content representation mirroring code files
- JSON representation for each code file with functions, classes, methods, properties
- Full signatures with type information (parameter types, return types, property types)
- Context preservation including import/export information and file-level declarations
- Mirror structure that parallels the original codebase organization

**FR3: Blueprint Generation System**
- Generate Path-Based Blueprints with configurable depth settings (0=all depth, 1=current folder, etc.)
- Generate Method-Based Blueprints focusing on specific methods, functions, or classes
- Support both persistent Feature Blueprints (saved as documentation) and temporary blueprints
- Output formats optimized for AI consumption and human visualization

**FR4: LSP-Powered Relationship Extraction**
- Leverage Language Server Protocol for precise relationship data extraction
- Extract line numbers, call hierarchies, and type information
- Initial support for TypeScript/JavaScript and Python
- Minimize processing overhead through targeted LSP queries

**FR5: YAML-Based Blueprint Definition**
- Enable declarative specification of blueprint contents through YAML files
- Support component selection and feature tagging
- Allow persistence control for blueprint documentation

**FR6: Caching & Incremental Updates**
- Implement blueprint caching strategy with change detection via file hashing
- Regenerate only affected portions when code changes
- Maintain blueprint accuracy without constant full reprocessing
- Provide `arch sync` command for synchronization

**FR7: Command-Line Interface**
- Blueprint generation commands for different blueprint types
- YAML-based blueprint creation support
- Synchronization commands for updating representations
- Format and destination output controls

**FR8: Proof-of-Concept Visualizer**
- Basic graph rendering of relationship structure
- Relationship navigation capabilities
- Filter controls for focused views
- Export capability for visualizations

## Non Functional Requirements (MVP)

**NFR1: Performance & Scalability**
- System must handle codebases with up to 10,000 files efficiently
- Blueprint generation should complete within 30 seconds for typical project sizes
- Incremental updates must process changes within 5 seconds of file modification
- Memory usage should remain under 2GB for large codebase analysis

**NFR2: Token Efficiency (AI Optimization)**
- Generated blueprints must achieve significant token reduction compared to raw source code
- AI-optimized output formats should maintain semantic clarity while minimizing token count
- Blueprint representations should enable equivalent architectural context with 60-80% fewer tokens

**NFR3: Accuracy & Reliability**
- Relationship extraction must achieve >95% accuracy for function calls and dependencies
- LSP integration should handle parsing errors gracefully without system failure
- Incremental updates must maintain consistency with full regeneration results
- System should validate blueprint completeness and flag missing relationships

**NFR4: Automation & Scripting Priority**
- Any functionality that can be implemented as a script should be implemented as a script rather than requiring AI agent intervention
- Prefer automated solutions over interactive processes where deterministic outcomes are possible
- Minimize AI token usage by automating repetitive or rule-based operations
- Reserve AI agents for creative, analytical, or complex decision-making tasks

**NFR5: Usability & Developer Experience**
- CLI commands should follow intuitive, consistent patterns
- Error messages must be clear and actionable for developers
- Documentation should enable new users to generate first blueprint within 15 minutes
- System should provide helpful feedback during long-running operations

**NFR6: Extensibility & Maintainability**
- Architecture must support adding new programming languages through parser plugins
- Blueprint types should be extensible without core system modifications
- Output format system should allow new formats without breaking existing functionality
- Codebase should maintain clear separation of concerns for future AI agent optimization

**NFR7: Data Integrity & Consistency**
- Catalog files (project_catalog.yaml, feature_catalog.yaml) must remain synchronized with codebase state
- System should detect and report inconsistencies between representations
- Blueprint cache must invalidate appropriately when source code changes
- JSON Mirrors must accurately reflect current file contents

## User Interaction and Design Goals

**Overall Vision & Experience:** 
Architectum should provide a seamless, efficient experience that feels more like using advanced development tools than complex analysis software. The interaction paradigm should emphasize "instant insight" - users should be able to quickly generate meaningful views of their codebase without extensive configuration or learning curves.

**Key Interaction Paradigms:**
- **Command-line First:** Primary interactions through intuitive CLI commands that follow standard Unix/Git-like patterns (`arch sync`, `arch blueprint path`, `arch blueprint method`)
- **YAML-driven Configuration:** Complex blueprint definitions through declarative YAML files that can be version-controlled and shared
- **Progressive Disclosure:** Simple commands provide immediate value, with advanced options available for power users

**Core Interfaces:**

1. **Command-Line Interface (Primary)**
   - Clean, predictable command structure
   - Helpful error messages and usage hints
   - Progress indicators for long-running operations
   - Consistent output formatting

2. **Proof-of-Concept Visualizer (Secondary)**
   - Interactive graph navigation with smooth panning/zooming
   - Click-to-explore relationship traversal
   - Filter controls that update the view in real-time
   - Export capabilities for sharing insights

**Target Platforms:** 
- Cross-platform CLI (Windows, macOS, Linux)
- Web-based visualizer accessible via local server
- Integration-friendly for IDE extensions (future consideration)

**Usability Priorities:**
- **Immediate Value:** First blueprint generated within 2-3 commands
- **Discoverability:** Built-in help and examples guide users naturally
- **Consistency:** Similar operations follow similar patterns across all interfaces
- **Performance Feedback:** Users always know what the system is doing and how long it will take

## Technical Assumptions

**Repository & Service Architecture Decision:** 
Monorepo structure with Python-based core system. The single repository will contain the complete Architectum system including parsers, blueprint generators, CLI interface, caching system, and proof-of-concept visualizer. This approach supports the MVP's focus on cohesive development and simplified deployment while allowing for future modularization if needed.

**Rationale:** The monorepo approach aligns with the MVP goal of rapid iteration and the need for tight integration between the System Map, JSON Mirrors, and Blueprint components. It simplifies dependency management and enables coordinated development across the three-component architecture.

**Core Technology Foundations:**
- **Primary Language:** Python 3.13 for core system implementation
- **Package Management:** UV for fast, reliable Python package management and virtual environment handling
- **Graph Processing:** NetworkX for System Map implementation and relationship modeling
- **CLI Framework:** Click for command-line interface development
- **API Framework:** FastAPI for any HTTP-based interfaces or future API extensions
- **Language Server Integration:** Python LSP libraries for TypeScript/JavaScript and Python parsing
- **Serialization:** JSON for internal processing, with XML consideration for AI-optimized output
- **Caching:** File-based caching with hash-based change detection

**Development Environment Requirements:**
- Python 3.13+ runtime environment
- UV package manager for dependency management and virtual environments
- Node.js (for TypeScript/JavaScript LSP integration)
- Git for version control and project tracking
- Standard development tools (pytest for testing, black for formatting)

**External Dependencies:**
- Language Server Protocol implementations for target languages
- TypeScript/JavaScript language server for frontend code analysis
- Python language server for backend code analysis
- File system watching capabilities for incremental updates

**Deployment Assumptions:**
- Primarily local development tool installation via UV
- Cross-platform compatibility (Windows, macOS, Linux)
- Self-contained installation with minimal external dependencies
- Future consideration for IDE plugin architecture

**Integration Constraints:**
- Must work with existing development workflows without disruption
- Should integrate with common version control practices
- Must handle large codebases without requiring specialized infrastructure
- Should support both individual developer use and team collaboration scenarios

### Testing requirements

**Unit Testing:**
- Comprehensive unit test coverage for all core components (System Map, JSON Mirrors, Blueprint generators)
- Test coverage target: ≥80% for all Python modules
- Framework: pytest with pytest-cov for coverage reporting
- Property-based testing with Hypothesis for robust validation of core algorithms and data structures
- Mock LSP interactions to ensure reliable, fast unit tests
- Test all parser implementations with sample code snippets

**Property-Based Testing (Hypothesis):**
- Generate diverse code structures to test relationship extraction accuracy
- Validate System Map consistency properties across different input scenarios
- Test blueprint generation with randomized file structures and content
- Verify caching behavior under various file change patterns
- Ensure JSON Mirror accuracy with generated code examples

**Contract Testing (Pact):**
- LSP integration contract testing to verify language server communication protocols
- Define and validate contracts between Architectum and TypeScript/JavaScript language servers
- Define and validate contracts between Architectum and Python language servers
- Ensure backward compatibility when LSP implementations change
- Test error handling and graceful degradation when LSP contracts are violated

**Integration Testing:**
- End-to-end testing of complete blueprint generation workflows
- File system integration testing for caching and incremental updates
- Cross-component testing between System Map and JSON Mirrors
- YAML blueprint definition parsing and execution testing

**CLI Testing:**
- Command-line interface testing for all major commands (`arch sync`, `arch blueprint`)
- Input validation and error handling verification
- Output format consistency testing
- Help system and usage message validation

**Performance Testing:**
- Benchmark testing with codebases of varying sizes (100, 1K, 10K files)
- Memory usage profiling during large codebase processing
- Incremental update performance validation
- Blueprint generation time measurement and optimization

**Language Parser Testing:**
- Comprehensive testing with real-world TypeScript/JavaScript projects
- Python codebase parsing accuracy validation
- Edge case handling (syntax errors, incomplete files, complex inheritance)
- Relationship extraction accuracy verification

**Manual Validation:**
- Proof-of-concept visualizer functionality testing
- Blueprint accuracy validation against known codebases
- User workflow testing for documentation and onboarding
- Cross-platform compatibility verification (Windows, macOS, Linux)

**Continuous Integration:**
- Automated test execution on code changes
- Test result reporting and coverage tracking
- Performance regression detection
- Multi-platform testing in CI environment
- Contract verification in CI pipeline

## Epic Overview

**Epic 1: Foundation & Core Infrastructure**
- Goal: Establish the foundational project structure, core data models, configuration system, and basic CLI framework to enable all subsequent development.
- Story 1.1: As a developer, I want to set up the basic project structure with UV package management so that the development environment is ready for implementation.
- Story 1.2: As a system, I want to implement the core System Map data model so that code relationships can be represented and navigated.
- Story 1.3: As a system, I want to implement the JSON Mirrors structure so that detailed file content can be stored and accessed.
- Story 1.4: As a developer, I want a configuration system for the System Map so that I can whitelist/blacklist files and specify root files for frontend and backend analysis.
- Story 1.5: As a system, I want to respect .gitignore files so that ignored files are excluded from both System Map and JSON Mirrors.
- Story 1.6: As a developer, I want a basic CLI framework with `arch` command so that I can interact with the system from the command line.

**Epic 2: Language Parsing & Relationship Extraction**
- Goal: Implement language-specific parsers and LSP integration to extract accurate code relationships and populate the core representations.
- Story 2.1: As a system, I want to implement a Python parser so that Python codebases can be analyzed and relationships extracted.
- Story 2.2: As a system, I want to implement a TypeScript/JavaScript parser so that frontend codebases can be analyzed.
- Story 2.3: As a system, I want to integrate with Language Server Protocol so that I can leverage LSP as an alternative method for extracting both relationship data and JSON Mirror content, allowing comparison with custom parsers to determine the optimal approach.
- Story 2.4: As a developer, I want an `arch sync` command so that my codebase can be processed and representations updated.

**Epic 3: Blueprint Generation System**
- Goal: Create the blueprint generation capabilities that transform core representations into AI-optimized and human-readable outputs.
- Story 3.1: As a user, I want to generate Path-Based Blueprints so that I can analyze directory structures with configurable depth.
- Story 3.2: As a user, I want to generate Method-Based Blueprints so that I can focus on specific functions or classes.
- Story 3.3: As a user, I want YAML-based blueprint definitions so that I can declaratively specify complex blueprint requirements.
- Story 3.4: As a system, I want multiple output formats so that blueprints can serve both AI consumption and human visualization needs.
- Story 3.5: As a user, I want persistent Feature Blueprints so that important code documentation can be saved and versioned.

**Epic 4: Caching & Performance Optimization**
- Goal: Implement intelligent caching, database storage, and incremental update mechanisms to ensure system performance scales with codebase size.
- Story 4.1: As a system, I want SQLite database storage so that System Map and JSON Mirror data can be efficiently persisted and queried.
- Story 4.2: As a system, I want file-based change detection so that only modified code is reprocessed during updates.
- Story 4.3: As a system, I want blueprint caching so that frequently accessed views load instantly.
- Story 4.4: As a system, I want incremental System Map updates so that large codebases remain responsive to changes.
- Story 4.5: As a developer, I want performance monitoring so that I can understand system behavior with my codebase.

**Epic 5: Proof-of-Concept Visualizer**
- Goal: Deliver a basic but functional visualization capability that demonstrates the power of relationship-based code representation.
- Story 5.1: As a user, I want a web-based graph renderer so that I can visualize code relationships in my browser.
- Story 5.2: As a user, I want interactive navigation so that I can explore relationships by clicking through the graph.
- Story 5.3: As a user, I want filtering controls so that I can focus on specific aspects of my codebase.
- Story 5.4: As a user, I want export capabilities so that I can share visualizations with my team.

## Key Reference Documents

- [Project Brief](project_docs/core_documents/project_brief.md) - Initial project definition and vision
- [Architecture Document](project_docs/core_documents/architecture.md) - Technical architecture and system design  
- [Catalog System Docs](architectum-agents/data/catalog_system.md) - Project, feature and test catalog management documentation
- [Catalog System](architectum-agents/data/catalog_system) - Folder containing catalogs
- [Data Models](project_docs/supporting_documents/data-models.md) - Core data structures and schemas
- [API Reference](project_docs/supporting_documents/api-reference.md) - CLI commands and internal API specifications

## Out of Scope Ideas Post MVP

Anything you and the user agreed it out of scope or can be removed from scope to keep MVP lean. Consider the goals of the PRD and what might be extra gold plating or additional features that could wait until the MVP is completed and delivered to assess functionality and market fit or usage.

### AI-Powered Enhancements:
Automatic feature boundary detection
Code similarity analysis
Intelligent blueprint suggestions
Natural language querying of code relationships

## Change Log

| Change | Date | Version | Description | Author |
| ------ | ---- | ------- | ----------- | ------ |