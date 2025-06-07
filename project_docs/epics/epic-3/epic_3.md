# Epic 3: Blueprint Generation System

> This document is a granulated shard from the main "Architectum Product Requirements Document" focusing on "Epic 3: Blueprint Generation System".

## Epic Goal
Create the blueprint generation capabilities that transform System Map and JSON Mirror data into focused JSON outputs optimized for AI consumption, with flexible configuration through YAML definitions and visual selection.

## User Stories

### Story 3.1: Path-Based Blueprint Generation
**As a user, I want to generate path-based blueprints so that I can give AI everything in a folder context limited to a certain depth.**

**Acceptance Criteria:**
- Path-based blueprint command accepts directory path and depth parameters
- Depth 0 includes all subdirectories recursively
- Depth 1 includes only immediate subdirectory contents
- Depth N includes N levels of subdirectories
- JSON output contains all code elements within the specified scope
- Output is optimized for AI token efficiency while maintaining completeness
- Command provides feedback on scope and total elements included
- Large scopes warn user about potential token usage

### Story 3.2: Method-Based Blueprint Generation
**As a user, I want to generate method-based blueprints so that I can provide AI with strategically focused code views using whitelist/blacklist controls.**

**Acceptance Criteria:**
- Method-based blueprint accepts single files or groups of files as input
- Whitelist functionality includes only specified functions, classes, or methods
- Blacklist functionality excludes specified functions, classes, or methods from otherwise included files
- Blueprint includes necessary context (imports, dependencies) for included elements
- Related types and interfaces are automatically included when referenced
- JSON output provides focused view suitable for AI analysis
- Command validates that specified functions/classes exist in target files
- Clear error messages when whitelist/blacklist targets are not found

### Story 3.3: YAML Configuration System
**As a user, I want to define blueprint contents through YAML files so that I can create reusable, precise blueprint configurations.**

**Acceptance Criteria:**
- YAML schema supports file selection by path or pattern
- Include/exclude patterns provide fine-grained control over content
- Function and class filtering can be specified per file or globally
- YAML validation ensures configuration is syntactically and semantically correct
- Configuration can reference files relative to project root
- Error messages clearly indicate YAML syntax or semantic issues
- YAML files can be version-controlled and shared across team
- Documentation and examples are provided for YAML schema

### Story 3.4: Blueprint Persistence and Feature Management
**As a user, I want to save blueprint configurations as Feature Blueprints so that I can maintain and reuse important code views.**

**Acceptance Criteria:**
- YAML configurations can be saved as named Feature Blueprints
- Feature Blueprints can be regenerated with current code state
- Blueprint metadata includes creation date, description, and scope information
- Saved blueprints can be listed, updated, and deleted
- Feature Blueprints integrate with data visualizer for creation and editing
- JSON blueprints are generated fresh from System Map/JSON Mirrors (no caching)
- Command can export blueprint configurations for sharing
- Import functionality allows loading shared blueprint configurations

## Dependencies
- Epic 1: Foundation & Core Infrastructure (must be completed)
- Epic 2: Language Parsing & Relationship Extraction (must be completed)
- System Map and JSON Mirrors must be populated with data
- CLI framework must support command extensions

## Success Criteria
- Path-based blueprints provide complete folder context at any depth
- Method-based blueprints enable precise AI context control through whitelist/blacklist
- YAML configuration system allows complex blueprint definitions
- Feature Blueprints enable reuse of important code views
- JSON output is optimized for AI consumption and token efficiency
- Blueprint generation completes efficiently for typical project scopes
- Data visualizer integration allows intuitive blueprint creation
- All blueprint generation components have ≥80% test coverage

## Design Principles
- **AI-First Output**: JSON format optimized for AI model consumption
- **Strategic Context Control**: Enable precise limitation of AI context window usage
- **Configuration as Code**: YAML definitions are version-controllable and shareable
- **Fresh Generation**: Always generate from current System Map/JSON Mirrors state
- **Visual Integration**: Support creation through data visualizer interaction
- **Reusability**: Feature Blueprints enable saving and reusing important views