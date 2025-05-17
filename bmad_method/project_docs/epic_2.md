# Epic 2: FileSetBlueprint Implementation

**Goal:** To enable Architectum to generate blueprints based on an explicit list of user-specified files (`FileSetBlueprint`), allowing AI agents and visualization tools to analyze a curated collection of code files at varying levels of detail. This supports targeted analysis of logically related files that may not be co-located.

## Story List

### Story 2.1: Implement FileSetBlueprint Logic
- **User Story / Goal:** As an AI agent (via Architectum), I want to request a `FileSetBlueprint` by providing a list of specific file paths, so that I can receive a structural representation of exactly those files.
- **Detailed Requirements:**
  - Implement logic within the `arch_blueprint_generator` module to accept a list of relative file paths.
  - For each valid file path in the list:
    - Access and read the file content.
    - Extract basic information (e.g., filename, full path, extension) initially, with placeholders for deeper analysis based on detail level.
  - Handle cases where file paths are invalid, inaccessible, or not actual files.
  - Aggregate the information for all valid files into a single structured JSON output.
  - The output should clearly distinguish information from each file.
- **Acceptance Criteria (ACs):**
  - AC1: Given a list of valid file paths, the system generates a JSON output containing basic information for each specified file.
  - AC2: Given a list containing invalid file paths, the system processes valid files and reports errors for invalid ones.
  - AC3: If all provided paths are invalid, an appropriate error or empty success state is returned.
  - AC4: The JSON output clearly delineates data for each processed file.

### Story 2.2: Integrate 'Minimal' Detail Level for FileSetBlueprint
- **User Story / Goal:** As an AI agent, I want to request a `FileSetBlueprint` with `Minimal` detail, so that I can quickly get a high-level overview of functions/classes and their relationships within the specified set of files.
- **Detailed Requirements:**
  - For each file processed by `FileSetBlueprint` (Story 2.1), apply parsing logic (similar to Epic 1, Story 1.3, for supported languages) to identify function and class names/signatures.
  - Capture high-level relationships within each file (e.g., a function defined within a class).
  - The JSON output for `FileSetBlueprint` with `Minimal` detail should include this information for each relevant code element within each file.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `FileSetBlueprint` with `Minimal` detail includes names/signatures of functions and classes for each file in the set.
  - AC2: The output clearly distinguishes between files, and within each file, between classes and functions.
  - AC3: Output does not include detailed parameter types, return types, or code comments for `Minimal` detail.

### Story 2.3: Integrate 'Standard' Detail Level for FileSetBlueprint
- **User Story / Goal:** As an AI agent, I want to request a `FileSetBlueprint` with `Standard` detail, so that I can get more specific information like parameter types and return types for elements within the specified files.
- **Detailed Requirements:**
  - Extend the parsing logic from Story 2.2.
  - For functions/methods in each file, extract parameter names and their types (if available/type-hinted).
  - Extract return types (if available/type-hinted).
  - For classes in each file, identify properties/attributes with their types (if available).
  - The JSON output for `FileSetBlueprint` with `Standard` detail should include this information.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `FileSetBlueprint` with `Standard` detail includes all `Minimal` information for each file.
  - AC2: The output includes parameter names and types for functions/methods in each file.
  - AC3: The output includes return types for functions/methods in each file.
  - AC4: The output includes class properties/attributes and their types in each file.
  - AC5: Output does not include detailed code comments or annotations beyond what's necessary for type/signature information.

### Story 2.4: Integrate 'Detailed' Detail Level for FileSetBlueprint
- **User Story / Goal:** As an AI agent, I want to request a `FileSetBlueprint` with `Detailed` detail, so that I can obtain comprehensive information, including code comments and annotations, for elements within the specified files.
- **Detailed Requirements:**
  - Extend the parsing logic from Story 2.3.
  - For each file, extract code comments (e.g., docstrings, block comments) associated with classes, functions, and methods.
  - Extract relevant annotations/decorators for elements in each file.
  - The JSON output for `FileSetBlueprint` with `Detailed` detail should include this information.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `FileSetBlueprint` with `Detailed` detail includes all `Standard` information for each file.
  - AC2: The output includes associated code comments/docstrings for classes and functions/methods in each file.
  - AC3: The output includes relevant annotations/decorators for elements in each file.

### Story 2.5: Expose FileSetBlueprint via API/CLI
- **User Story / Goal:** As a developer or another service, I want to trigger the generation of a `FileSetBlueprint` via a defined API endpoint or CLI command within Architectum, so that I can request blueprints for specific collections of files.
- **Detailed Requirements:**
  - If API-based: Define and implement an endpoint (e.g., `POST /blueprints/fileset`) that accepts a `listOfFilePaths` (array of strings) and `detailLevel` as parameters.
  - If CLI-based: Define and implement a command (e.g., `architectum generate fileset-blueprint --files <path1>,<path2> --level <level>`) that accepts a list of file paths and the detail level.
  - The endpoint/command should invoke the `FileSetBlueprint` generation logic.
  - The generated JSON blueprint should be returned.
- **Acceptance Criteria (ACs):**
  - AC1: The API endpoint or CLI command successfully triggers `FileSetBlueprint` generation.
  - AC2: All required parameters (`listOfFilePaths`, `detailLevel`) can be passed and are correctly used.
  - AC3: The generated JSON blueprint is returned correctly via the API response or CLI output.
  - AC4: Proper error handling is implemented for invalid inputs (e.g., malformed list, issues during generation).

---

## Change Log

| Change        | Date       | Version | Description                    | Author         |
| ------------- | ---------- | ------- | ------------------------------ | -------------- |
| Initial draft | 05-16-2025 | 0.1     | Initial draft of Epic 2        | Product Manager |
