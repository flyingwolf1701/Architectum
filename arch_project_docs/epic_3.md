# Epic 3: CodeElementBlueprint Implementation with Focused Graph Analysis

**Goal:** To empower Architectum with the ability to generate highly focused graph-based blueprints detailing specific code elements (like functions, classes, methods) within a single file (`CodeElementBlueprint`), enabling AI agents to perform granular analysis of targeted code elements and their immediate relationships.

## Story List

### Story 3.1: Implement CodeElementBlueprint Logic with Graph Structure

- **User Story / Goal:** As an AI agent (via Architectum), I want to request a `CodeElementBlueprint` by providing a file path and a list of specific element names (e.g., function names, class names), so that I can receive a focused graph representation of only those elements within that file.
- **Detailed Requirements:**
  - Implement logic within the `arch_blueprint_generator` module to accept a single relative file path and a list of element names (strings).
  - Create a file node for the specified file in the graph model.
  - Parse the file to identify the specified elements.
  - For each identified element, create appropriate nodes in the graph (function nodes, class nodes, etc.).
  - Establish "contains" relationships between the file node and the identified element nodes.
  - Establish relationships between the identified elements if applicable (e.g., a specified method within a specified class).
  - Include relevant node metadata (element name, type, location in file).
  - Handle cases where the file path is invalid, inaccessible, or elements are not found.
  - Implement subgraph extraction focused specifically on the requested elements.
  - Ensure the output can be serialized to JSON format.
- **Acceptance Criteria (ACs):**
  - AC1: Given a valid file path and a list of existing element names, the system generates a graph with nodes for each specified element.
  - AC2: If the file path is invalid or inaccessible, an appropriate error is returned.
  - AC3: If some specified elements are not found in the file, the system processes found elements and reports on missing ones.
  - AC4: If no specified elements are found, an appropriate error or empty success state is returned.
  - AC5: The graph structure clearly represents each requested and found element with appropriate node metadata.
  - AC6: The output graph can be serialized to JSON format.
  - **AC7: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the element selection and graph construction functionality
    - **Framework:** Implementation using pytest with file fixtures containing known elements
    - **Mocking:** Mock file system for testing file access without dependencies
    - **Contract Testing:** Use pact to verify the JSON output meets the expected schema
    - **Snapshot Testing:** Create snapshots for representative element selections
    - **Error Handling:** Test various error conditions (invalid file, missing elements)

### Story 3.2: Integrate 'Minimal' Detail Level for CodeElementBlueprint with Immediate Relationships

- **User Story / Goal:** As an AI agent, I want to request a `CodeElementBlueprint` with `Minimal` detail, so that I can quickly get a focused graph representation with basic signature information and immediate relationships for the specified code elements.
- **Detailed Requirements:**
  - For each element identified by `CodeElementBlueprint` (Story 3.1), extract basic signature information:
    - For functions/methods: name and parameter names (without types)
    - For classes: name and method names
  - Identify and create nodes for immediate related elements that are directly connected to the specified elements:
    - For functions: functions called directly by the specified functions
    - For methods: other methods called within the same class
    - For classes: parent classes (inheritance)
  - Establish relationship edges between the specified elements and their immediate related elements.
  - Add basic metadata to relationship edges (e.g., relationship type).
  - The JSON output for `CodeElementBlueprint` with `Minimal` detail should include this focused graph structure.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `CodeElementBlueprint` with `Minimal` detail includes basic signature information for the specified elements.
  - AC2: The graph includes nodes for immediate related elements with "calls" or "inherits" relationships.
  - AC3: The output clearly distinguishes between the specifically requested elements and their related elements.
  - AC4: Output does not include detailed parameter types, return types, or code comments for `Minimal` detail.
  - AC5: The graph structure focuses on the requested elements while providing adequate context through immediate relationships.
  - **AC6: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the basic signature extraction and relationship detection functionality
    - **Framework:** Implementation using pytest with parameterized tests for different element types
    - **Snapshot Testing:** Create snapshots showing the minimal detail graph for various element selections
    - **Contract Testing:** Ensure the JSON output consistently meets the defined schema contract
    - **Relationship Testing:** Test detection of immediate relationships for different element types
    - **Language Testing:** Verify functionality across all supported languages

### Story 3.3: Integrate 'Standard' Detail Level for CodeElementBlueprint with Type Information

- **User Story / Goal:** As an AI agent, I want to request a `CodeElementBlueprint` with `Standard` detail, so that I can get a more comprehensive graph representation with type information and expanded relationships for the specified code elements.
- **Detailed Requirements:**
  - Extend the parsing logic from Story 3.2 to extract additional node metadata for the specified elements:
    - For functions/methods: parameter names and their types, return types
    - For classes: properties/attributes with their types
  - Expand the relationship detection to include:
    - Secondary relationships (e.g., functions called by functions that are called by the specified elements)
    - Type usage relationships (e.g., parameter types, return types)
  - Add metadata to nodes and relationships providing context for the connections.
  - The JSON output for `CodeElementBlueprint` with `Standard` detail should include this enhanced graph structure.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `CodeElementBlueprint` with `Standard` detail includes all `Minimal` graph elements plus enhanced metadata.
  - AC2: The graph nodes include metadata for parameter names and types for functions/methods.
  - AC3: The graph nodes include metadata for return types for functions/methods.
  - AC4: The graph nodes include metadata for class properties/attributes and their types.
  - AC5: The relationship network is more extensive than in the `Minimal` detail level, including secondary relationships.
  - AC6: Output does not include detailed code comments or annotations beyond what's necessary for type/signature information.
  - **AC7: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the enhanced metadata extraction and expanded relationship detection functionality
    - **Framework:** Implementation using pytest with specific test cases for type extraction
    - **Snapshot Testing:** Create snapshots comparing standard vs. minimal detail levels
    - **Contract Testing:** Verify the enhanced JSON output continues to meet schema requirements
    - **Property Testing:** Use hypothesis to test type extraction for different function signatures
    - **Relationship Depth Testing:** Verify correct detection of secondary relationships

### Story 3.4: Integrate 'Detailed' Detail Level for CodeElementBlueprint with Documentation and Comprehensive Analysis

- **User Story / Goal:** As an AI agent, I want to request a `CodeElementBlueprint` with `Detailed` detail, so that I can obtain a comprehensive graph representation including code comments, annotations, and a thorough relationship network for the specified code elements.
- **Detailed Requirements:**
  - Extend the parsing logic from Story 3.3 for the specified element nodes:
    - Extract code comments (e.g., docstrings, block comments) and add as node metadata
    - Extract annotations/decorators and add as node metadata
  - Further expand the relationship network to include:
    - Tertiary relationships (relationships of related elements)
    - Data flow relationships where detectable
    - Usage patterns of the specified elements
  - Add comprehensive metadata to both nodes and relationships.
  - Include information about the element's context within the broader codebase if available.
  - The JSON output for `CodeElementBlueprint` with `Detailed` detail should include this information-rich graph structure.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `CodeElementBlueprint` with `Detailed` detail includes all `Standard` graph elements and their relationships.
  - AC2: The graph nodes include associated code comments/docstrings as metadata.
  - AC3: The graph nodes include relevant annotations/decorators as metadata.
  - AC4: The relationship network is comprehensive, showing a detailed view of how the specified elements connect to the broader codebase.
  - AC5: The output provides rich context around the specified elements through metadata and expanded relationships.
  - **AC6: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the documentation extraction and comprehensive relationship mapping functionality
    - **Framework:** Implementation using pytest with specific test cases for documentation formats and complex relationships
    - **Snapshot Testing:** Create snapshots showing the detailed level output for well-documented code elements
    - **Contract Testing:** Verify the detailed output format continues to meet schema requirements
    - **Documentation Testing:** Test extraction of various documentation formats for different languages
    - **Complex Relationship Testing:** Verify detection of multi-level relationships and data flow patterns

### Story 3.5: Expose CodeElementBlueprint via API/CLI with Graph Output Options

- **User Story / Goal:** As a developer or another service, I want to trigger the generation of a `CodeElementBlueprint` graph via a defined API endpoint or CLI command within Architectum, so that I can request focused blueprints for specific code elements.
- **Detailed Requirements:**
  - If API-based: Define and implement an endpoint (e.g., `POST /blueprints/codeelement`) that accepts `filePath` (string), `elementNames` (array of strings), and `detailLevel` as parameters.
  - If CLI-based: Define and implement a command (e.g., `architectum generate codeelement-blueprint --file <path> --elements <el1>,<el2> --level <level>`) that accepts the file path, a list of element names, and the detail level.
  - The endpoint/command should invoke the `CodeElementBlueprint` generation logic with graph output.
  - Add options for output format (e.g., JSON, potentially other formats like XML for AI consumption).
  - Add options for output destination (stdout, file, etc.).
  - The generated graph blueprint should be returned as the response (API) or output to stdout/file (CLI).
- **Acceptance Criteria (ACs):**
  - AC1: The API endpoint or CLI command successfully triggers `CodeElementBlueprint` graph generation.
  - AC2: All required parameters (`filePath`, `elementNames`, `detailLevel`) can be passed and are correctly used.
  - AC3: The generated graph blueprint is returned correctly via the API response or CLI output.
  - AC4: Output format options are functional (at minimum, JSON output).
  - AC5: Proper error handling is implemented for invalid inputs (e.g., file not found, elements not found, malformed list).
  - **AC6: Testing Requirements:**
    - **Coverage:** At least 80% code coverage for the API/CLI implementation and output formatting options
    - **Framework:** Implementation using pytest with CLI invocation and API request testing
    - **Integration Testing:** End-to-end tests calling the API/CLI with various element selections
    - **Contract Testing:** Verify the output format options produce valid outputs
    - **Parameter Testing:** Test complex parameter combinations like multiple elements
    - **Error Handling:** Test error responses for various invalid inputs

---

## Change Log

| Change        | Date       | Version | Description                    | Author         |
| ------------- | ---------- | ------- | ------------------------------ | -------------- |
| Initial draft | 05-16-2025 | 0.1     | Initial draft of Epic 3        | Product Manager |
| Updated with graph approach | 05-17-2025 | 0.2 | Enhanced Epic 3 with graph-based model | Technical Scrum Master |
| Added testing requirements | 05-17-2025 | 0.3 | Added comprehensive testing strategy | Technical Scrum Master |