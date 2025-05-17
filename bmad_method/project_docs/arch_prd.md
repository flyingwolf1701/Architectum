# Architectum Product Requirements Document (PRD)

## Intro

The Architectum platform aims to provide advanced tools for understanding and interacting with software codebases. This initial version (MVP) focuses on establishing a core capability: the generation of structured "blueprints" of a codebase. These blueprints are primarily designed for consumption by AI agents to enable focused analysis, comprehension, and modification of code, with a secondary application in powering visualization tools for human developers.

## Goals and Context

- **Project Objectives:**
    - To enable AI agents to accurately understand the structure and content of specific parts of a software codebase.
    - To provide a flexible mechanism for users (or other systems) to define the scope and granularity of codebase analysis.
    - To lay the foundation for future AI-powered development and maintenance tools.
    - To support developers in visualizing complex code structures.
- **Measurable Outcomes:**
    - AI agents can successfully use generated blueprints to perform defined analysis tasks (e.g., identify dependencies within a module, summarize a function's purpose) with a specified level of accuracy.
    - Reduction in time/effort for specific AI-driven code analysis tasks compared to unassisted analysis.
- **Success Criteria:**
    - The system can generate all three defined blueprint types (`DirectoryBlueprint`, `FileSetBlueprint`, `CodeElementBlueprint`) across all three detail levels (`Minimal`, `Standard`, `Detailed`).
    - Generated blueprints are successfully parsed and utilized by a test AI agent.
    - Generated blueprints provide sufficient information to render a basic structural visualization of the selected code scope.
- **Key Performance Indicators (KPIs):**
    - Blueprint generation success rate.
    - Average time to generate blueprints for various scopes and detail levels.
    - AI task completion rate/accuracy when using blueprints.

## Scope and Requirements (MVP / Current Version)

### Functional Requirements (High-Level)

- **Capability 1: Codebase Blueprint Generation**
    - The system must allow users or other services to request and receive structured JSON representations (blueprints) of a software codebase. These blueprints are primarily intended for AI consumption to facilitate understanding and analysis of the code, and secondarily for visualization.
    - The system must support different methods for defining the scope and granularity of the blueprint.
    - The system must offer configurable levels of detail for the information included in the blueprint.

    - **1.1. `DirectoryBlueprint` Generation**
        - **Purpose & User Value:** Enables an AI agent to gain contextual understanding of a specific module, component library, or bounded context within the codebase by analyzing a directory structure. Allows the AI to narrow its focus for subsequent tasks. Supports visualization of module/folder structures and their high-level contents.
        - **User Configuration Inputs:**
            - `Target Directory Path`: Relative path to the target directory.
            - `Scan Depth`: Integer specifying the depth of directory traversal (e.g., 0 for all descendants, 1 for immediate children files/folders).
            - `Detail Level`: `Minimal`, `Standard`, or `Detailed`.
        - **Expected Output (High-Level):** A JSON blueprint reflecting the files and subdirectories within the specified path, down to the chosen depth. Content details for files/elements within the scope will vary based on the selected `Detail Level`. The structure must be easily navigable by an AI.

    - **1.2. `FileSetBlueprint` Generation**
        - **Purpose & User Value:** Enables an AI agent to analyze a curated collection of code files that may be logically related but not necessarily co-located. Useful for understanding cross-cutting concerns or a specific feature spread across multiple files. Supports visualization of relationships between these selected files.
        - **User Configuration Inputs:**
            - `List of File Paths`: An array of relative paths to the target files.
            - `Detail Level`: `Minimal`, `Standard`, or `Detailed`.
        - **Expected Output (High-Level):** A JSON blueprint representing the analyzed content of each specified file. Content details for files/elements will vary based on the selected `Detail Level`. The output should clearly delineate information for each file in the set for AI processing.

    - **1.3. `CodeElementBlueprint` Generation**
        - **Purpose & User Value:** Provides an AI agent with a focused, detailed view of specific classes, functions, or methods within a single file. Enables granular analysis, understanding of intricate logic, or assistance in targeted refactoring/generation tasks by the AI. Supports detailed visualization of specific code elements and their immediate context.
        - **User Configuration Inputs:**
            - `Target File Path`: Relative path to the target file.
            - `List of Element Names`: An array of specific class names, function names, or method names within the file to be detailed.
            - `Detail Level`: `Minimal`, `Standard`, or `Detailed`.
        - **Expected Output (High-Level):** A JSON blueprint that includes top-level information about the specified file, but provides detailed analysis (according to the chosen `Detail Level`) primarily for the listed code elements. The AI should be able to easily extract information about the targeted elements.

    - **1.4. Blueprint Detail Levels:**
        - The system must apply the selected detail level to the scope defined by the chosen blueprint type.
        - **`Minimal`:** Focuses on functions/classes and their names/signatures and high-level relationships (e.g., calls between functions within the scope, inheritance). Intended for AI to get a quick overview or for high-level architectural visualizations.
        - **`Standard`:** Includes all `Minimal` information plus details like parameter types, return types, class properties, and public method signatures. Provides the AI with sufficient detail for more informed analysis.
        - **`Detailed`:** Includes all `Standard` information plus more comprehensive details such as summaries of code comments (docstrings), annotations, and potentially non-code artifacts like configuration related to the code elements (specifics to be refined with Architect). Equips the AI for deep analysis or complex tasks.

### Non-Functional Requirements (NFRs)

- **Machine Readability & Usability (for AI):**
    - Blueprint JSON output must be well-structured, predictable, and easily parsable by programmatic agents.
    - Schema should be designed to facilitate efficient querying and navigation of codebase information by an AI.
- **Accuracy & Reliability:**
    - Generated blueprints must accurately reflect the state of the codebase (for the selected elements and files) at the time of generation.
    - The system must consistently produce blueprints according to the specified parameters. Error handling for invalid paths or unparseable code should be robust.
- **Performance:**
    - Blueprint generation time should be reasonable to support interactive use by an AI or a developer awaiting visualization. (Specific targets to be defined, e.g., "Generate `Minimal` `DirectoryBlueprint` for a 100-file directory with depth 1 in < X seconds").
- **Scalability:**
    - The system should be designed to handle blueprint generation for codebases of varying sizes, from small projects to larger repositories (initial targets to be defined).
    - Performance should degrade gracefully with increasing scope/detail.
- **Maintainability:**
    - The codebase for the blueprint generation system itself should be well-documented and modular to allow for future enhancements (e.g., support for new languages, new detail levels).
- **Security:**
    - If accessing private repositories or sensitive code, appropriate authentication and authorization mechanisms must be in place (details to be defined based on hosting and access methods).
    - The system should not introduce vulnerabilities through its analysis process.
