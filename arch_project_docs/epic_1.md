# Epic 1: Core Blueprint Generation Framework and Graph Model Implementation

**Goal:** To establish the foundational infrastructure for Architectum's graph-based blueprint generation and deliver the `DirectoryBlueprint` capability, enabling AI agents and visualization tools to analyze specified directory structures at varying levels of detail through a relationship-oriented view.

## Story List

### Story 1.1: Setup Blueprint Generation Core Module and Graph Model

- **User Story / Goal:** As a system architect, I want a core module for blueprint generation established with a graph-based data model, so that different blueprint types can be developed and integrated in a consistent and maintainable manner within the existing Architectum repository.
- **Detailed Requirements:**
  - **Establish a new module or package named `arch_blueprint_generator` within the existing `Architectum` repository to house the blueprint generation capabilities.**
  - Design and implement the core graph data model that will represent code as a network of nodes and relationships:
    - Define node types (files, functions, classes, methods, features)
    - Define relationship types (contains, calls, implements, imports, inherits)
    - Create base classes/interfaces for nodes and relationships with appropriate metadata fields
  - Implement basic graph operations (creation, traversal, subgraph extraction)
  - Create serialization/deserialization support for the graph model
  - Implement a basic command-line interface (CLI) or an API endpoint structure that can later be used to invoke different blueprint generators from within the Architectum system.
  - Set up initial logging and error handling mechanisms for the module.
  - Include a basic README for this new module, outlining its purpose and how to use it.
- **Acceptance Criteria (ACs):**
  - AC1: The new module/package `arch_blueprint_generator` is created within the `Architectum` repository and is buildable/integrable with the main project.
  - AC2: The graph data model is implemented with support for nodes, relationships, and metadata.
  - AC3: Basic graph operations (creation, traversal, subgraph extraction) are functional.
  - AC4: A placeholder CLI command or API endpoint for blueprint generation exists and returns a "not yet implemented" message or basic help.
  - AC5: Basic logging for module initialization and errors is functional.
  - AC6: The module includes a README with a graph-based overview of the system.
  - **AC7: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the graph data model and core operations
    - **Framework:** Implementation using pytest for unit testing
    - **Property Testing:** Use hypothesis to test graph model operations with property-based tests for robustness across random inputs
    - **Test Cases:** Must include tests for node creation, relationship establishment, and graph operations
    - **Documentation:** Test cases must document expected behavior through descriptive test names and docstrings

### Story 1.2: Implement DirectoryBlueprint Logic with Graph Structure

- **User Story / Goal:** As an AI agent (via Architectum), I want to request a `DirectoryBlueprint`, so that I can receive a graph-based structural representation of a specified directory.
- **Detailed Requirements:**
  - Implement the logic to traverse a directory structure based on a given path and depth parameter.
  - For each directory and file encountered, create appropriate nodes in the graph model.
  - Establish "contains" relationships between directories and their contents.
  - For each file encountered, extract basic information (e.g., filename, path, extension) and store as node metadata.
  - Implement subgraph extraction based on the specified directory scope.
  - Handle cases where the provided path is invalid or inaccessible.
  - The output should be a structured graph object representing the directory tree and its contents, serializable to JSON.
- **Acceptance Criteria (ACs):**
  - AC1: Given a valid directory path and depth, the system generates a graph output representing the directory structure (filenames and subdirectories) down to the specified depth.
  - AC2: Given an invalid directory path, the system returns an appropriate error.
  - AC3: The graph output correctly represents nested structures of directories and files with "contains" relationships.
  - AC4: Scan depth 0 correctly scans all subdirectories and files.
  - AC5: Scan depth 1 correctly scans only the immediate files and folders in the specified directory.
  - AC6: The output graph can be serialized to JSON format.
  - **AC7: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the directory traversal and graph construction functionality
    - **Framework:** Implementation using pytest with appropriate fixtures for file system operations
    - **Mocking:** Tests should use mock file systems to avoid external dependencies
    - **Contract Testing:** Use pact to verify the JSON output matches the expected schema for consumers
    - **Snapshot Testing:** Create snapshot tests for representative directory structures
    - **Edge Cases:** Tests must cover error conditions, empty directories, and unusual file names

### Story 1.3: Integrate 'Minimal' Detail Level for DirectoryBlueprint with Basic Code Analysis

- **User Story / Goal:** As an AI agent, I want to request a `DirectoryBlueprint` with `Minimal` detail, so that I can quickly get a high-level graph view of functions/classes and their relationships within the directory scope.
- **Detailed Requirements:**
  - For files identified by `DirectoryBlueprint` (Story 1.2), parse them (initially for supported languages like Python/JavaScript - specific languages TBD by Architect) to identify function and class declarations.
  - Create function and class nodes in the graph model.
  - Establish "contains" relationships between files and their functions/classes.
  - Capture high-level relationships if easily identifiable (e.g., a function defined within a class).
  - The JSON output for `DirectoryBlueprint` with `Minimal` detail should include this graph structure for each relevant code element.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `DirectoryBlueprint` with `Minimal` detail includes nodes for functions and classes within files in the specified scope.
  - AC2: The graph clearly distinguishes between different node types (files, directories, classes, functions).
  - AC3: Relationships (e.g., "contains" relationships between classes and methods) are represented in the graph.
  - AC4: Output does not include detailed parameter types, return types, or code comments for `Minimal` detail level.
  - AC5: The graph structure is serializable to JSON.
  - **AC6: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the code parsing and node generation functionality
    - **Framework:** Implementation using pytest with language-specific test files
    - **Snapshot Testing:** Create snapshots for each supported language showing the minimal detail level
    - **Contract Testing:** Ensure the JSON output consistently meets the defined schema contract
    - **Language Coverage:** Tests must cover all supported languages with their specific constructs

### Story 1.4: Integrate 'Standard' Detail Level for DirectoryBlueprint with Enhanced Relationship Data

- **User Story / Goal:** As an AI agent, I want to request a `DirectoryBlueprint` with `Standard` detail, so that I can get a graph representation with more specific information like parameter types and return types for elements within the directory scope.
- **Detailed Requirements:**
  - Extend the parsing logic from Story 1.3 to extract additional node metadata.
  - For function/method nodes, add parameter names and their types (if available/type-hinted) as metadata.
  - Add return types (if available/type-hinted) as metadata on function/method nodes.
  - For class nodes, add properties/attributes with their types (if available) as metadata.
  - Begin establishing more relationship types in the graph (e.g., "calls" relationships between functions if detectable without full LSP analysis).
  - The JSON output for `DirectoryBlueprint` with `Standard` detail should include this enhanced graph structure.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `DirectoryBlueprint` with `Standard` detail includes all `Minimal` graph elements plus enhanced metadata.
  - AC2: The graph nodes include metadata for parameter names and types for functions/methods.
  - AC3: The graph nodes include metadata for return types for functions/methods.
  - AC4: The graph nodes include metadata for class properties/attributes and their types.
  - AC5: Basic "calls" relationships are included in the graph if easily detectable.
  - AC6: Output does not include detailed code comments or annotations beyond what's necessary for type/signature information.
  - **AC7: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the enhanced metadata extraction and relationship detection functionality
    - **Framework:** Implementation using pytest with parameterized tests for different language constructs
    - **Snapshot Testing:** Create snapshots comparing standard vs. minimal detail levels
    - **Contract Testing:** Verify the enhanced JSON output continues to meet schema requirements
    - **Property Testing:** Use hypothesis to test type extraction across various function signatures

### Story 1.5: Integrate 'Detailed' Detail Level for DirectoryBlueprint with Documentation Data

- **User Story / Goal:** As an AI agent, I want to request a `DirectoryBlueprint` with `Detailed` detail, so that I can obtain a comprehensive graph representation, including code comments and annotations, for elements within the directory scope.
- **Detailed Requirements:**
  - Extend the parsing logic from Story 1.4 for the graph nodes.
  - Extract code comments (e.g., docstrings, block comments) associated with classes, functions, and methods and add as node metadata.
  - Extract relevant annotations/decorators and add as node metadata.
  - Add any additional metadata that would be valuable for detailed understanding.
  - Enhance the relationship detection for the graph model where possible.
  - The JSON output for `DirectoryBlueprint` with `Detailed` detail should include this information-rich graph structure.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `DirectoryBlueprint` with `Detailed` detail includes all `Standard` graph elements and their relationships.
  - AC2: The graph nodes include associated code comments/docstrings as metadata.
  - AC3: The graph nodes include relevant annotations/decorators as metadata.
  - AC4: The relationship structure is as complete as possible without full LSP integration (which will come in later epics).
  - **AC5: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the documentation extraction and enhanced relationship detection functionality
    - **Framework:** Implementation using pytest with specific test cases for docstring formats and annotations
    - **Snapshot Testing:** Create snapshots showing the detailed level output for well-documented code
    - **Contract Testing:** Verify the detailed output format meets schema requirements
    - **Language Specifics:** Test language-specific documentation formats (e.g., Python docstrings, JSDoc)

### Story 1.6: Expose DirectoryBlueprint via Initial API/CLI with Graph Output Options

- **User Story / Goal:** As a developer or another service, I want to trigger the generation of a `DirectoryBlueprint` graph via a defined API endpoint or CLI command within Architectum, so that I can integrate this capability into other tools or workflows.
- **Detailed Requirements:**
  - If API-based: Define and implement an endpoint (e.g., `POST /blueprints/directory` accessible within Architectum) that accepts `targetDirectoryPath`, `scanDepth`, and `detailLevel` as parameters.
  - If CLI-based: Define and implement a command (e.g., `architectum generate directory-blueprint --path <path> --depth <depth> --level <level>`, where `architectum` is the main CLI entry point) that accepts `targetDirectoryPath`, `scanDepth`, and `detailLevel` as parameters.
  - The endpoint/command should invoke the `DirectoryBlueprint` generation logic with the specified parameters.
  - Add options for output format (e.g., JSON, potentially other formats like XML for AI consumption).
  - Add options for output destination (stdout, file, etc.).
  - The generated graph blueprint should be returned as the response (API) or output to stdout/file (CLI).
- **Acceptance Criteria (ACs):**
  - AC1: The API endpoint or CLI command successfully triggers `DirectoryBlueprint` graph generation.
  - AC2: All required parameters (`targetDirectoryPath`, `scanDepth`, `detailLevel`) can be passed and are correctly used.
  - AC3: The generated graph blueprint is returned correctly via the API response or CLI output.
  - AC4: Output format options are functional (at minimum, JSON output).
  - AC5: Proper error handling is implemented for invalid inputs or generation failures.
  - **AC6: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the API/CLI implementation and output formatting options
    - **Framework:** Implementation using pytest with CLI invocation testing
    - **Integration Testing:** End-to-end tests calling the API/CLI with various parameters
    - **Contract Testing:** Verify the output format options produce valid outputs
    - **Parameter Testing:** Test all parameter combinations and error handling
    - **Output Format Testing:** Test different output formats if implemented

---

## Change Log

| Change        | Date       | Version | Description                    | Author         |
| ------------- | ---------- | ------- | ------------------------------ | -------------- |
| Initial draft | 05-16-2025 | 0.1     | Initial draft of Epic 1        | Product Manager |
| Updated with graph approach | 05-17-2025 | 0.2 | Enhanced Epic 1 with graph-based model | Technical Scrum Master |
| Added testing requirements | 05-17-2025 | 0.3 | Added comprehensive testing strategy | Technical Scrum Master |