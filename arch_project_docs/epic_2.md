# Epic 2: FileSetBlueprint Implementation with Graph Relationships

**Goal:** To enable Architectum to generate graph-based blueprints from an explicit list of user-specified files (`FileSetBlueprint`), allowing AI agents and visualization tools to analyze a curated collection of code files at varying levels of detail with relationship mapping across file boundaries.

## Story List

### Story 2.1: Implement FileSetBlueprint Logic with Graph Structure

- **User Story / Goal:** As an AI agent (via Architectum), I want to request a `FileSetBlueprint`, so that I can receive a graph-based structural representation of a specific set of files regardless of their directory location.
- **Detailed Requirements:**
  - Implement logic within the `arch_blueprint_generator` module to accept a list of relative file paths.
  - For each valid file path in the list, create a file node in the graph structure.
  - Extract basic information (e.g., filename, full path, extension) and store as node metadata.
  - Establish parent directory nodes and "contains" relationships as needed.
  - Handle cases where file paths are invalid, inaccessible, or not actual files.
  - Implement subgraph extraction based on the set of specified files.
  - Aggregate the information into a single graph structure with clear boundaries.
  - Ensure the output can be serialized to JSON format.
- **Acceptance Criteria (ACs):**
  - AC1: Given a list of valid file paths, the system generates a graph with nodes for each specified file.
  - AC2: Given a list containing invalid file paths, the system processes valid files and reports errors for invalid ones.
  - AC3: If all provided paths are invalid, an appropriate error or empty success state is returned.
  - AC4: The graph structure clearly distinguishes each file node and its parent directory context.
  - AC5: The output graph can be serialized to JSON format.
  - **AC6: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the file set processing and graph construction functionality
    - **Framework:** Implementation using pytest with file system fixtures
    - **Mocking:** Mock file system for testing file access without dependencies
    - **Contract Testing:** Use pact to verify the JSON output meets the expected schema
    - **Snapshot Testing:** Create snapshots for representative file sets and edge cases
    - **Error Handling:** Test various error conditions and invalid file paths

### Story 2.2: Integrate 'Minimal' Detail Level for FileSetBlueprint with Cross-File Relationships

- **User Story / Goal:** As an AI agent, I want to request a `FileSetBlueprint` with `Minimal` detail, so that I can quickly get a high-level graph view of functions/classes and their relationships across the specified set of files.
- **Detailed Requirements:**
  - For each file processed by `FileSetBlueprint` (Story 2.1), parse them (for supported languages) to identify function and class declarations.
  - Create function and class nodes in the graph model.
  - Establish "contains" relationships between files and their functions/classes.
  - Capture basic relationships within each file (e.g., a function defined within a class).
  - Begin identifying cross-file relationships (e.g., imports between files) at a basic level.
  - The JSON output for `FileSetBlueprint` with `Minimal` detail should include this graph structure with relationships spanning across files.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `FileSetBlueprint` with `Minimal` detail includes nodes for functions and classes for each file in the set.
  - AC2: The graph clearly distinguishes between different node types (files, classes, functions).
  - AC3: Basic relationships are represented both within files and between files.
  - AC4: Output does not include detailed parameter types, return types, or code comments for `Minimal` detail.
  - AC5: The graph structure correctly represents the file set as a connected network rather than isolated files.
  - **AC6: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the code parsing and cross-file relationship detection functionality
    - **Framework:** Implementation using pytest with multi-file test cases
    - **Snapshot Testing:** Create snapshots showing cross-file relationships in the graph
    - **Contract Testing:** Ensure the JSON output consistently meets the defined schema contract
    - **Related File Testing:** Test files with known relationships to verify detection
    - **Language Testing:** Ensure cross-file relationship detection works for all supported languages

### Story 2.3: Integrate 'Standard' Detail Level for FileSetBlueprint with Enhanced Relationships

- **User Story / Goal:** As an AI agent, I want to request a `FileSetBlueprint` with `Standard` detail, so that I can get a more detailed graph representation with type information and stronger relationship mapping across the specified files.
- **Detailed Requirements:**
  - Extend the parsing logic from Story 2.2 to extract additional node metadata.
  - For function/method nodes, add parameter names and their types (if available/type-hinted) as metadata.
  - Add return types (if available/type-hinted) as metadata on function/method nodes.
  - For class nodes, add properties/attributes with their types (if available) as metadata.
  - Enhance cross-file relationship detection (imports, potential function calls between files).
  - Implement relationship edge metadata where available.
  - The JSON output for `FileSetBlueprint` with `Standard` detail should include this enhanced graph structure.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `FileSetBlueprint` with `Standard` detail includes all `Minimal` graph elements plus enhanced metadata.
  - AC2: The graph nodes include metadata for parameter names and types for functions/methods.
  - AC3: The graph nodes include metadata for return types for functions/methods.
  - AC4: The graph nodes include metadata for class properties/attributes and their types.
  - AC5: Cross-file relationships are more comprehensively mapped than in the `Minimal` detail level.
  - AC6: Output does not include detailed code comments or annotations beyond what's necessary for type/signature information.
  - **AC7: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the enhanced metadata extraction and relationship mapping functionality
    - **Framework:** Implementation using pytest with parameterized tests for different relationship types
    - **Snapshot Testing:** Create snapshots comparing standard vs. minimal detail levels
    - **Contract Testing:** Verify the enhanced JSON output continues to meet schema requirements
    - **Property Testing:** Use hypothesis to test type extraction across various function declarations
    - **Relationship Testing:** Test various cross-file relationship patterns to ensure detection

### Story 2.4: Integrate 'Detailed' Detail Level for FileSetBlueprint with Documentation and Comprehensive Relationships

- **User Story / Goal:** As an AI agent, I want to request a `FileSetBlueprint` with `Detailed` detail, so that I can obtain a comprehensive graph representation including code comments, annotations, and thorough cross-file relationships.
- **Detailed Requirements:**
  - Extend the parsing logic from Story 2.3 for graph nodes.
  - Extract code comments (e.g., docstrings, block comments) associated with classes, functions, and methods and add as node metadata.
  - Extract relevant annotations/decorators and add as node metadata.
  - Maximize cross-file relationship detection within the limitations of parsing without full LSP integration.
  - Add relationship metadata (e.g., call sites, import details).
  - The JSON output for `FileSetBlueprint` with `Detailed` detail should include this information-rich graph structure.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `FileSetBlueprint` with `Detailed` detail includes all `Standard` graph elements and their relationships.
  - AC2: The graph nodes include associated code comments/docstrings as metadata.
  - AC3: The graph nodes include relevant annotations/decorators as metadata.
  - AC4: Cross-file relationships are mapped as thoroughly as possible within the limitations of the current implementation.
  - AC5: The relationship edges include useful metadata about the nature of the relationships.
  - **AC6: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the documentation extraction and comprehensive relationship mapping functionality
    - **Framework:** Implementation using pytest with specific test cases for docstrings and cross-file relationships
    - **Snapshot Testing:** Create snapshots showing the detailed level output for well-documented code with cross-file dependencies
    - **Contract Testing:** Verify the detailed output format continues to meet schema requirements
    - **Documentation Testing:** Test various documentation styles and formats across supported languages
    - **Relationship Metadata Testing:** Verify relationship edges include appropriate metadata

### Story 2.5: Expose FileSetBlueprint via API/CLI with Graph Output Options

- **User Story / Goal:** As a developer or another service, I want to trigger the generation of a `FileSetBlueprint` graph via a defined API endpoint or CLI command within Architectum, so that I can request blueprints for specific collections of files.
- **Detailed Requirements:**
  - If API-based: Define and implement an endpoint (e.g., `POST /blueprints/fileset`) that accepts a `listOfFilePaths` (array of strings) and `detailLevel` as parameters.
  - If CLI-based: Define and implement a command (e.g., `architectum generate fileset-blueprint --files <path1>,<path2> --level <level>`) that accepts a list of file paths and the detail level.
  - The endpoint/command should invoke the `FileSetBlueprint` generation logic with graph output.
  - Add options for output format (e.g., JSON, potentially other formats like XML for AI consumption).
  - Add options for output destination (stdout, file, etc.).
  - The generated graph blueprint should be returned as the response (API) or output to stdout/file (CLI).
- **Acceptance Criteria (ACs):**
  - AC1: The API endpoint or CLI command successfully triggers `FileSetBlueprint` graph generation.
  - AC2: All required parameters (`listOfFilePaths`, `detailLevel`) can be passed and are correctly used.
  - AC3: The generated graph blueprint is returned correctly via the API response or CLI output.
  - AC4: Output format options are functional (at minimum, JSON output).
  - AC5: Proper error handling is implemented for invalid inputs (e.g., malformed list, issues during generation).
  - **AC6: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the API/CLI implementation and output formatting options
    - **Framework:** Implementation using pytest with CLI invocation and API request testing
    - **Integration Testing:** End-to-end tests calling the API/CLI with various file lists
    - **Contract Testing:** Verify the output format options produce valid outputs
    - **Parameter Testing:** Test various parameter combinations, including edge cases
    - **Error Handling:** Test error responses for invalid inputs and parameters

---

## Change Log

| Change        | Date       | Version | Description                    | Author         |
| ------------- | ---------- | ------- | ------------------------------ | -------------- |
| Initial draft | 05-16-2025 | 0.1     | Initial draft of Epic 2        | Product Manager |
| Updated with graph approach | 05-17-2025 | 0.2 | Enhanced Epic 2 with graph-based model | Technical Scrum Master |
| Added testing requirements | 05-17-2025 | 0.3 | Added comprehensive testing strategy | Technical Scrum Master |