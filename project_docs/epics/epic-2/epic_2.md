# Epic 2: Language Parsing & Relationship Extraction

> This document is a granulated shard from the main "Architectum Product Requirements Document" focusing on "Epic 2: Language Parsing & Relationship Extraction".

## Epic Goal
Implement language-specific parsers and LSP integration to extract accurate code relationships and populate the core representations.

## User Stories

### Story 2.1: Python Parser Implementation
**As a system, I want to implement a Python parser so that Python codebases can be analyzed and relationships extracted.**

**Acceptance Criteria:**
- Python AST parsing extracts functions, classes, methods, and their relationships
- Import statements are tracked for dependency relationships
- Inheritance relationships are captured accurately
- Function calls within code are identified and mapped
- Line number information is preserved for all extracted elements
- Error handling gracefully manages syntax errors or incomplete files
- Parser supports Python 3.13+ syntax features

### Story 2.2: TypeScript/JavaScript Parser Implementation
**As a system, I want to implement a TypeScript/JavaScript parser so that frontend codebases can be analyzed.**

**Acceptance Criteria:**
- TypeScript/JavaScript AST parsing extracts functions, classes, methods, and relationships
- ES6+ module imports/exports are tracked correctly
- Component relationships (React, Vue, etc.) are identified
- Function calls and method invocations are mapped
- Type information is extracted when available (TypeScript)
- JSX/TSX files are properly parsed
- Node.js and browser-style imports are both supported

### Story 2.3: LSP Integration
**As a system, I want to integrate with Language Server Protocol so that I can leverage LSP as an alternative method for extracting both relationship data and JSON Mirror content, allowing comparison with custom parsers to determine the optimal approach.**

**Acceptance Criteria:**
- LSP client can communicate with TypeScript/JavaScript language servers
- LSP client can communicate with Python language servers  
- Relationship extraction via LSP provides call hierarchy information
- Type information is retrieved through LSP capabilities
- Performance comparison between LSP and custom parsers is measurable
- Fallback mechanism exists when LSP is unavailable
- LSP errors are handled gracefully without system failure

### Story 2.4: Sync Command Implementation
**As a developer, I want an `arch sync` command so that my codebase can be processed and representations updated.**

**Acceptance Criteria:**
- `arch sync` command processes entire codebase or specified directories
- Progress indication shows processing status for large codebases
- Both System Map and JSON Mirrors are populated from parsed data
- Command respects configuration settings (whitelist/blacklist, .gitignore)
- Error summary reports files that failed to parse
- Incremental processing only updates changed files when possible
- Command completes successfully on sample codebases

## Dependencies
- Epic 1: Foundation & Core Infrastructure (must be completed)
- System Map and JSON Mirrors data structures must be available
- CLI framework must be functional

## Success Criteria
- Both Python and TypeScript/JavaScript codebases can be accurately parsed
- LSP integration provides reliable alternative to custom parsing
- `arch sync` command enables full codebase processing
- Relationship extraction accuracy exceeds 95% for standard code patterns
- Performance is acceptable for codebases up to 10,000 files
- All parsing components have ≥80% test coverage