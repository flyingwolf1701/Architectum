# Epic 1: Core Blueprint Generation Framework and DirectoryBlueprint Implementation

**Goal:** To establish the foundational infrastructure for Architectum's codebase blueprint generation and deliver the `DirectoryBlueprint` capability, enabling AI agents and visualization tools to analyze specified directory structures at varying levels of detail. This directly supports the PRD objective of enabling AI agents to understand code structure within a defined scope.

## Story List

### Story 1.1: Setup Blueprint Generation Core Module
- **User Story / Goal:** As a system architect, I want a core module for blueprint generation established, so that different blueprint types can be developed and integrated in a consistent and maintainable manner within the existing Architectum repository.
- **Detailed Requirements:**
  - **Establish a new module or package named `arch_blueprint_generator` within the existing `Architectum` repository to house the blueprint generation capabilities.**
  - Define common data structures and interfaces that will be used by all blueprint generation types (e.g., for representing files, code elements, relationships, detail levels).
  - Implement a basic command-line interface (CLI) or an API endpoint structure that can later be used to invoke different blueprint generators from within the Architectum system.
  - Set up initial logging and error handling mechanisms for the module.
  - Include a basic README for this new module, outlining its purpose and how to use it.
- **Acceptance Criteria (ACs):**
  - AC1: The new module/package `arch_blueprint_generator` is created within the `Architectum` repository and is buildable/integrable with the main project.
  - AC2: Common data structure definitions for basic code entities (file, function stub) are present within the new module.
  - AC3: A placeholder CLI command or API endpoint (callable from Architectum's main entry points) for blueprint generation exists and returns a "not yet implemented" message or basic help.
  - AC4: Basic logging for module initialization and errors is functional.

### Story 1.2: Implement DirectoryBlueprint Logic
- **User Story / Goal:** As an AI agent (via Architectum), I want to request a `DirectoryBlueprint`, so that I can receive a structural representation of a specified directory.
- **Detailed Requirements:**
  - Implement the logic to traverse a directory structure based on a given path and depth parameter.
  - Identify files and subdirectories within the specified scope.
  - For each file encountered, extract basic information (e.g., filename, path, extension) initially, with placeholders for deeper analysis.
  - Handle cases where the provided path is invalid or inaccessible.
  - The output should be a structured JSON object representing the directory tree and its contents.
- **Acceptance Criteria (ACs):**
  - AC1: Given a valid directory path and depth, the system generates a JSON output representing the directory structure (filenames and subdirectories) down to the specified depth.
  - AC2: Given an invalid directory path, the system returns an appropriate error.
  - AC3: The JSON output correctly reflects nested structures of directories and files.
  - AC4: Scan depth 0 correctly scans all subdirectories and files.
  - AC5: Scan depth 1 correctly scans only the immediate files and folders in the specified directory.

### Story 1.3: Integrate 'Minimal' Detail Level for DirectoryBlueprint
- **User Story / Goal:** As an AI agent, I want to request a `DirectoryBlueprint` with `Minimal` detail, so that I can quickly get a high-level overview of functions/classes and their relationships within the directory scope.
- **Detailed Requirements:**
  - For files identified by `DirectoryBlueprint` (Story 1.2), parse them (initially for supported languages like Python/JavaScript - specific languages TBD by Architect) to identify function and class names/signatures.
  - Capture high-level relationships if easily identifiable (e.g., a function defined within a class).
  - The JSON output for `DirectoryBlueprint` with `Minimal` detail should include this information for each relevant code element.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `DirectoryBlueprint` with `Minimal` detail includes names/signatures of functions and classes within files in the specified scope.
  - AC2: The output clearly distinguishes between files, classes, and functions.
  - AC3: Relationships (e.g., methods within classes) are represented if applicable.
  - AC4: Output does not include detailed parameter types, return types, or code comments for `Minimal` detail.

### Story 1.4: Integrate 'Standard' Detail Level for DirectoryBlueprint
- **User Story / Goal:** As an AI agent, I want to request a `DirectoryBlueprint` with `Standard` detail, so that I can get more specific information like parameter types and return types for elements within the directory scope.
- **Detailed Requirements:**
  - Extend the parsing logic from Story 1.3.
  - For functions/methods, extract parameter names and their types (if available/type-hinted).
  - Extract return types (if available/type-hinted).
  - For classes, identify properties/attributes with their types (if available).
  - The JSON output for `DirectoryBlueprint` with `Standard` detail should include this information.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `DirectoryBlueprint` with `Standard` detail includes all `Minimal` information.
  - AC2: The output includes parameter names and types for functions/methods.
  - AC3: The output includes return types for functions/methods.
  - AC4: The output includes class properties/attributes and their types.
  - AC5: Output does not include detailed code comments or annotations beyond what's necessary for type/signature information.

### Story 1.5: Integrate 'Detailed' Detail Level for DirectoryBlueprint
- **User Story / Goal:** As an AI agent, I want to request a `DirectoryBlueprint` with `Detailed` detail, so that I can obtain comprehensive information, including code comments and annotations, for elements within the directory scope.
- **Detailed Requirements:**
  - Extend the parsing logic from Story 1.4.
  - Extract code comments (e.g., docstrings, block comments) associated with classes, functions, and methods.
  - Extract relevant annotations/decorators.
  - The JSON output for `DirectoryBlueprint` with `Detailed` detail should include this information.
- **Acceptance Criteria (ACs):**
  - AC1: Requesting a `DirectoryBlueprint` with `Detailed` detail includes all `Standard` information.
  - AC2: The output includes associated code comments/docstrings for classes and functions/methods.
  - AC3: The output includes relevant annotations/decorators.

### Story 1.6: Expose DirectoryBlueprint via Initial API/CLI
- **User Story / Goal:** As a developer or another service, I want to trigger the generation of a `DirectoryBlueprint` via a defined API endpoint or CLI command within Architectum, so that I can integrate this capability into other tools or workflows.
- **Detailed Requirements:**
  - If API-based: Define and implement an endpoint (e.g., `POST /blueprints/directory` accessible within Architectum) that accepts `targetDirectoryPath`, `scanDepth`, and `detailLevel` as parameters.
  - If CLI-based: Define and implement a command (e.g., `architectum generate directory-blueprint --path <path> --depth <depth> --level <level>`, where `architectum` is the main CLI entry point) that accepts `targetDirectoryPath`, `scanDepth`, and `detailLevel` as parameters.
  - The endpoint/command should invoke the `DirectoryBlueprint` generation logic with the specified parameters.
  - The generated JSON blueprint should be returned as the response (API) or output to stdout/file (CLI).
- **Acceptance Criteria (ACs):**
  - AC1: The API endpoint or CLI command successfully triggers `DirectoryBlueprint` generation.
  - AC2: All required parameters (`targetDirectoryPath`, `scanDepth`, `detailLevel`) can be passed and are correctly used.
  - AC3: The generated JSON blueprint is returned correctly via the API response or CLI output.
  - AC4: Proper error handling is implemented for invalid inputs or generation failures.

---

## Change Log

| Change        | Date       | Version | Description                    | Author         |
| ------------- | ---------- | ------- | ------------------------------ | -------------- |
| Initial draft | 05-16-2025 | 0.1     | Initial draft of Epic 1        | Product Manager |
| Clarified module location | 05-16-2025 | 0.1.1   | Ensured module creation is within existing repo | Product Manager |
| Updated module name | 05-16-2025 | 0.1.2   | Set module name to `arch_blueprint_generator` per user | Product Manager |
