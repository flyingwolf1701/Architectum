# Epic 1: Foundation & Core Infrastructure

> This document is a granulated shard from the main "Architectum Product Requirements Document" focusing on "Epic 1: Foundation & Core Infrastructure".

## Epic Goal
Establish the foundational project structure, core data models, configuration system, and basic CLI framework to enable all subsequent development.

## User Stories

### Story 1.1: Project Structure Setup
**As a developer, I want to set up the basic project structure with UV package management so that the development environment is ready for implementation.**

**Acceptance Criteria:**
- Project directory structure is created following the defined architecture
- UV package manager is configured and functional
- Basic Python 3.13+ environment is established
- Initial dependencies are defined and installable
- Project can be built and basic commands execute successfully

### Story 1.2: System Map Data Model
**As a system, I want to implement the core System Map data model so that code relationships can be represented and navigated.**

**Acceptance Criteria:**
- Node types are implemented: Files, Functions, Classes, Methods, Features (virtual)
- Relationship types are implemented: Contains, Calls, Implements, Imports, Inherits, Depends-On
- Metadata tracking includes line numbers, signatures, basic type information
- Methods exist to traverse relationships in any direction
- Data model supports efficient graph-based navigation

### Story 1.3: JSON Mirrors Structure
**As a system, I want to implement the JSON Mirrors structure so that detailed file content can be stored and accessed.**

**Acceptance Criteria:**
- JSON representation structure for code files is defined
- Functions, classes, methods, properties with full signatures are supported
- Type information (parameter types, return types, property types) is captured
- Import/export information and file-level declarations are preserved
- Mirror structure parallels original codebase organization

### Story 1.4: Configuration System
**As a developer, I want a configuration system for the System Map so that I can whitelist/blacklist files and specify root files for frontend and backend analysis.**

**Acceptance Criteria:**
- Configuration file format is defined and documented
- File whitelist/blacklist functionality is implemented
- Root file specification for frontend and backend analysis is supported
- Configuration can be loaded and validated
- Default configuration provides sensible starting values

### Story 1.5: .gitignore Respect
**As a system, I want to respect .gitignore files so that ignored files are excluded from both System Map and JSON Mirrors.**

**Acceptance Criteria:**
- .gitignore files are parsed and rules are applied
- Ignored files are excluded from processing
- Nested .gitignore files are properly handled
- System provides feedback on excluded files when requested
- Configuration can override .gitignore rules when necessary

### Story 1.6: Basic CLI Framework
**As a developer, I want a basic CLI framework with `arch` command so that I can interact with the system from the command line.**

**Acceptance Criteria:**
- `arch` command is available and executable
- Help system provides clear usage information
- Basic command structure is established for future extensions
- Error handling provides helpful messages
- Version information is available
- Command validation prevents invalid usage

## Dependencies
- None (This is the foundational epic)

## Success Criteria
- All core data structures are implemented and tested
- CLI framework is functional and extensible
- Configuration system allows customization of analysis scope
- Foundation supports all subsequent epic requirements
- Code quality meets defined standards with ≥80% test coverage