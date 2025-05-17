# Epic 3: CodeElementBlueprint Implementation

**Goal:** To empower Architectum with the ability to generate highly focused blueprints detailing specific code elements (like functions, classes, methods) within a single file (`CodeElementBlueprint`). This will enable AI agents to perform granular analysis, understand intricate logic, or assist in targeted refactoring of these elements at varying levels of detail.

## Story List

### Story 3.1: Implement CodeElementBlueprint Logic
- **User Story / Goal:** As an AI agent (via Architectum), I want to request a `CodeElementBlueprint` by providing a file path and a list of specific element names (e.g., function names, class names), so that I can receive a detailed structural representation of only those elements within that file.
- **Detailed Requirements:**
  - Implement logic within the `arch_blueprint_generator` module to accept a single relative file path and a list of element names (strings).
  - Access and read the specified file content.
  - Parse the file to identify the specified elements.
  - For each identified element:
    - Extract basic identifying information (name, type e.g., function/class/method).
    - Placeholders for deeper analysis based on detail level.
  - Handle cases where the file path is invalid, inaccessible, or elements are not found.
  - Aggregate the information for all valid found elements into a single structured JSON output. The output should clearly focus on the requested elements.
- **Acceptance Criteria (ACs):**
  - AC1: Given a valid file path and a list of existing element names, the system generates a JSON output containing basic information for each specified element.
  - AC2: If the file path is invalid or inaccessible, an appropriate error is returned.
  - AC3: If some specified elements are not found in the file, the system processes found elements and may report on missing ones.
  - AC4: If no specified elements are found, an appropriate error or empty success state (indicating file processed but no elements matched) is returned.
  - AC5: The JSON output clearly delineates data for each requested and found element.

### Story 3.2: Integrate 'Minimal' Detail Level for CodeElementBlueprint
- **User Story / Goal:** As an AI agent, I want to request a `CodeElementBlueprint` with `Minimal` detail, so that I can quickly get a high-level signature and context for the specified code elements.
- **Detailed Requirements:**
  - For each element identified by `CodeElementBlueprint` (Story 3.1), apply parsing logic to extract its name and signature (e.g., function signature with parameter names, class name).
  - If an element is a method within a class, its relationship to the class should be clear.
  - The JSON output for `CodeElementBlueprint` with `Minimal` detail should include this focused information for each specified element.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `CodeElementBlueprint` with `Minimal` detail includes names/signatures for each specified and found element.
  - AC2: The output clearly identifies the type of each element (function, class, method).
  - AC3: For methods, their parent class context is indicated.
  - AC4: Output does not include detailed parameter types (beyond what's in a basic signature), return types, or code comments for `Minimal` detail.

### Story 3.3: Integrate 'Standard' Detail Level for CodeElementBlueprint
- **User Story / Goal:** As an AI agent, I want to request a `CodeElementBlueprint` with `Standard` detail, so that I can get specific information like parameter types and return types for the targeted code elements.
- **Detailed Requirements:**
  - Extend the parsing logic from Story 3.2 for the specified elements.
  - For functions/methods, extract parameter names and their types (if available/type-hinted).
  - Extract return types (if available/type-hinted).
  - For classes, identify properties/attributes with their types (if available), and public method signatures (already covered by function/method parsing).
  - The JSON output for `CodeElementBlueprint` with `Standard` detail should include this information for each specified element.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `CodeElementBlueprint` with `Standard` detail includes all `Minimal` information for each specified element.
  - AC2: The output includes parameter names and types for specified functions/methods.
  - AC3: The output includes return types for specified functions/methods.
  - AC4: For specified classes, the output includes properties/attributes and their types.
  - AC5: Output does not include detailed code comments or annotations beyond what's necessary for type/signature information.

### Story 3.4: Integrate 'Detailed' Detail Level for CodeElementBlueprint
- **User Story / Goal:** As an AI agent, I want to request a `CodeElementBlueprint` with `Detailed` detail, so that I can obtain comprehensive information, including code comments and annotations, for the targeted code elements.
- **Detailed Requirements:**
  - Extend the parsing logic from Story 3.3 for the specified elements.
  - Extract code comments (e.g., docstrings, block comments) associated with the specified classes, functions, and methods.
  - Extract relevant annotations/decorators for the specified elements.
  - The JSON output for `CodeElementBlueprint` with `Detailed` detail should include this information for each specified element.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `CodeElementBlueprint` with `Detailed` detail includes all `Standard` information for each specified element.
  - AC2: The output includes associated code comments/docstrings for the specified elements.
  - AC3: The output includes relevant annotations/decorators for the specified elements.

### Story 3.5: Expose CodeElementBlueprint via API/CLI
- **User Story / Goal:** As a developer or another service, I want to trigger the generation of a `CodeElementBlueprint` via a defined API endpoint or CLI command within Architectum, so that I can request highly focused blueprints for specific code elements.
- **Detailed Requirements:**
  - If API-based: Define and implement an endpoint (e.g., `POST /blueprints/codeelement`) that accepts `filePath` (string), `elementNames` (array of strings), and `detailLevel` as parameters.
  - If CLI-based: Define and implement a command (e.g., `architectum generate codeelement-blueprint --file <path> --elements <el1>,<el2> --level <level>`) that accepts the file path, a list of element names, and the detail level.
  - The endpoint/command should invoke the `CodeElementBlueprint` generation logic.
  - The generated JSON blueprint should be returned.
- **Acceptance Criteria (ACs):**
  - AC1: The API endpoint or CLI command successfully triggers `CodeElementBlueprint` generation.
  - AC2: All required parameters (`filePath`, `elementNames`, `detailLevel`) can be passed and are correctly used.
  - AC3: The generated JSON blueprint is returned correctly via the API response or CLI output.
  - AC4: Proper error handling is implemented for invalid inputs (e.g., file not found, elements not found, malformed list).

---

## Change Log

| Change        | Date       | Version | Description                    | Author         |
| ------------- | ---------- | ------- | ------------------------------ | -------------- |
| Initial draft | 05-16-2025 | 0.1     | Initial draft of Epic 3        | Product Manager |
