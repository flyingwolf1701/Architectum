Project Brief: Architectum
Introduction / Problem Statement
The fundamental challenge in leveraging AI for code-related tasks is providing it with the right level of contextual understanding of a codebase. Current approaches often overwhelm AI assistants with excessive implementation details or lack the necessary structural insight, leading to inefficient token usage and suboptimal assistance. Developers also struggle with comprehending large, complex codebases, finding it difficult to trace call flows, understand data propagation, and grasp the overall architecture quickly.
Architectum addresses these challenges by acting as an AI-first code comprehension system. It leverages Language Server Protocol (LSP) to accurately analyze codebases and transforms them into structured JSON blueprints. By extracting the architectural essence of code files—focusing on symbols, functional relationships (call flows, data types), and structure without deep implementation details—Architectum enables more effective and token-efficient collaboration between developers and AI assistants. It also aims to provide developers with powerful tools for visualizing and navigating code structure, particularly focusing on call flows and data relationships, thereby improving their own understanding and productivity.
Vision & Goals
Vision: To revolutionize how developers and AI assistants understand, discuss, and interact with complex software systems by transforming code into clear, structured, and actionable architectural blueprints. Architectum aims to make any codebase comprehensible, navigable, and intelligently adaptable, with a focus on clarifying functional relationships and data flows.
Primary Goals (MVP):
Core LSP-to-JSON Blueprint Generation: Successfully parse codebases (initially focusing on TypeScript/JavaScript and Python) using LSP and generate accurate, structured JSON representations of their architectural elements (symbols, methods/functions, call relationships, parameter/return types).
Configurable Multi-Level Indexing: Implement the ability to generate at least two levels of JSON indexes based on YAML configuration: a system-wide overview (high-level functional units and their primary interactions) and a module-based (directory-focused) index detailing functional relationships within that scope.
Basic AI Context Provision: Demonstrate that the generated JSON blueprints/indexes can be provided as context to an AI model (e.g., via a CLI tool or simple interface) to answer structural questions about a sample codebase (e.g., "trace the primary call flow for feature X," "what data does function Y return?") more efficiently than providing raw code.
Proof-of-Concept Visualizer: Develop a rudimentary web-based visualizer that can render a basic graph of function/method calls and their relationships from a generated JSON index for a small to medium-sized project.
Success Metrics (Initial Ideas):
Blueprint Accuracy: Percentage of key architectural elements (functions, methods, call relationships, parameter/return types) correctly identified and represented in the JSON output compared to manual review for set test projects.
Token Efficiency: Reduction in token count required to provide equivalent architectural context (focused on call flows and data types) to an AI model using Architectum's JSON blueprints versus raw source code files.
Indexing Performance: Time taken to generate indexes for codebases of varying sizes.
User Feedback (Developer Alpha): Qualitative feedback from a small group of developers on the clarity of generated JSON and the usefulness of the PoC visualizer for understanding call flows.
AI Task Improvement: Measurable improvement in an AI's ability to perform specific tasks (e.g., "explain the call sequence for X," "identify functions that process Y data type") when using Architectum's output.
Target Audience / Users
Software Developers (General):
Profile: Developers working on medium to large-scale codebases, particularly those involving multiple modules, complex inter-functional relationships, or unfamiliar code, whether individually or as part of a team. This includes individual contributors, tech leads, and architects.
Needs:
Rapidly understand the architecture, call flows, and data propagation paths of new or existing projects.
Easily navigate and visualize code structures, focusing on functional relationships.
Improve collaboration (if in a team) by having a shared, abstracted view of how the code functions.
Enhance their ability to work effectively with AI coding assistants by providing them with precise contextual understanding of functional interactions.
Reduce the cognitive load associated with comprehending intricate system behaviors.
Independent Developers & Entrepreneurs:
Profile: Individuals or very small teams building new software products from scratch, often managing all aspects of development themselves and heavily relying on AI for assistance and productivity.
Needs:
Effectively plan and design robust application architecture, including clear functional interfaces and data flows, from the outset.
Maintain architectural clarity and consistency in terms of functional interactions as the project grows.
Maximize the effectiveness of AI coding assistants for generating, refactoring, and understanding code by providing high-quality, focused context on function calls and data types.
Quickly onboard themselves to different parts of their own codebase by reviewing abstracted functional maps.
AI Coding Assistants / LLM-based Developer Tools:
Profile: AI models and the platforms that host them (e.g., IDE integrations, standalone AI agents).
Needs:
Receive concise, structured, and accurate representations of codebase architecture, emphasizing function-level relationships, call sequences, and data transformations.
Obtain context that is rich enough for meaningful assistance but abstracted enough to fit within token limits.
Understand functional roles, call dependencies, and data types without needing to parse entire code files.
Facilitate more accurate code generation, planning, architectural reasoning, and debugging assistance.
Development Teams / Organizations (Supporting Role):
Profile: Software development teams and organizations looking to improve onboarding, maintain code quality, and facilitate better architectural discussions focused on system behavior.
Needs:
Tools for automated structural documentation, particularly of functional interactions and data flows.
Consistent ways to represent and discuss system behavior at an abstracted level.
Mechanisms to support technical decision-making and assess the impact of changes on functional call chains.
Key Features / Scope (High-Level Ideas for MVP)
LSP-Powered Code Structure Extraction:
Connect to Language Servers (initially for TypeScript/JavaScript and Python) to parse source code.
Extract key architectural elements: classes, functions/methods, interfaces, types, imports/exports, with a strong focus on call relationships between functions/methods and their parameter/return types.
Focus on structure, omitting deep implementation details.
JSON Blueprint Generation:
Transform the extracted structural information into a standardized, well-defined JSON format, emphasizing functional relationships (as designed in technical_overview.md and our discussions).
Each primary code file results in a corresponding JSON blueprint detailing its functional units and their interactions.
Configurable Indexing Engine (via YAML):
Process a YAML configuration file defining index types and their parameters (e.g., files/functions to include/exclude, detail level for relationships).
Generate at least two types of indexes for the MVP:
System-Wide Index: A high-level map of key functional units (e.g., major services, components, or modules) and their primary call relationships across the project.
Module-Based Index: A more detailed view focused on a specific directory or set of directories, mapping out inter-functional calls and data type usage within that scope.
Output these indexes as consolidated JSON files.
Basic AI Context Provisioning Tool:
A command-line interface (CLI) tool that allows a user to:
Specify a project and an Architectum-generated index.
Formulate a query related to call flow or data usage.
Output the relevant JSON context formatted for an AI prompt.
Proof-of-Concept (PoC) Call Flow Visualizer:
A simple web-based viewer that can ingest a generated JSON index.
Render a basic interactive graph showing function/method calls and their relationships.
Store location information (file path, line numbers) in JSON to enable future "click-to-code" functionality.
Focus on demonstrating the concept of visualizing call flows rather than a full feature set. Future considerations include interactive filtering/trimming and hierarchical layouts.
Known Technical Constraints or Preferences
Constraints:
Initial Language Focus: MVP development will prioritize robust support for TypeScript/JavaScript and Python.
LSP Dependency: The core extraction mechanism is dependent on the availability and quality of Language Servers.
Performance for Large Codebases: Performance on extremely large monorepos will need to be benchmarked post-MVP.
Token Limits of AI Models: The generated JSON structures must remain optimized for AI context windows.
Preferences:
Primary Data Format: JSON for code blueprints and indexes, detailing functional relationships.
Configuration Format: YAML for plans and index definitions.
Core Extraction Engine: Leverage Language Server Protocol (LSP).
Development Stack (from technical_overview.md):
JavaScript/TypeScript for LSP communication and potentially visualization.
Python for CLI tools and orchestration.
Agent Execution Environment (Exploration): Interest in Desktop Commander MCP or similar.
Risks:
LSP Variability/Quality: The accuracy of information from different LSPs can vary.
Complexity of Relationship Detection: Accurately detecting all relevant call relationships, especially dynamic ones, can be complex.
Maintaining Token Efficiency vs. Detail: Balancing sufficient detail for call/data flow analysis with AI token limits.
Scalability of Visualization: Rendering and navigating call graphs for very large systems can be challenging.
Adoption Curve: Demonstrating clear value in understanding complex call flows and data interactions.
Relevant Research (Optional)
Initial research and inspiration for Architectum include:
Code Visualization Tools (e.g., Codemap.app, existing IDE features): Exploration of existing tools like Codemap.app highlighted both the potential of code visualization (especially for call flows) and their current limitations. Research into how such tools gather data pointed towards the utility of Language Server Protocol (LSP).
Language Server Protocol (LSP): Identified as the core technology for accurate code parsing. Its standardized approach allows for broad language support over time, crucial for extracting function/method signatures, call relationships, and type information.
AI Code Comprehension Tools (e.g., RepoPrompt): Projects like RepoPrompt demonstrate the value of providing AI with abstracted "code maps." This validates Architectum's aim to improve AI's contextual understanding, specifically for reasoning about functional interactions.
JSON as a Data Interchange Format: Chosen for its lightweight nature, ease of parsing (especially for visualization), native fit with LSP outputs, and good support by AI models for structured data consumption.
Agent Execution Environments (e.g., Desktop Commander MCP): Explored as a potential way for AI agents, informed by Architectum's functional maps, to interact with a developer's local environment.
AI-Driven Development Methodologies (e.g., BMAD-METHOD): Frameworks like BMAD highlight using specialized AI agents. Architectum's outputs detailing call flows and data types could serve as critical inputs.
Contract Testing (e.g., Pact) & Property-Based Testing (e.g., Hypothesis): These are longer-term inspirations for Architectum's potential to innovate in testing, leveraging its structured understanding of functional contracts and data flows.
PM Prompt
PM Agent Handoff Prompt: Architectum MVP

Summary of Key Insights:
This project brief outlines "Architectum," an AI-first code comprehension system. The core problem is the difficulty developers and AI assistants face in understanding complex codebases, specifically in tracing call flows, data propagation, and overall functional architecture efficiently. Architectum addresses this by using Language Server Protocol (LSP) to parse code (initially TypeScript/JavaScript, Python) and generate structured JSON blueprints. These blueprints focus on architectural essence—function/method signatures, call relationships, parameter/return types—omitting deep implementation details.

The MVP aims to:
1.  Reliably extract this structural information into JSON blueprints.
2.  Implement configurable multi-level indexing (system-wide, module-based) via YAML to create focused views.
3.  Provide a basic CLI tool to feed these JSON contexts to AI models for structural queries.
4.  Develop a proof-of-concept web visualizer for basic function call graph rendering.

Key insights indicate:
-   A strong need for tools that clarify functional relationships beyond simple file dependencies.
-   The dual value proposition: enhancing human developer understanding AND improving AI assistant performance/token efficiency.
-   LSP is a viable technology for accurate, programmatic extraction.
-   Independent developers are a key target audience, needing robust architectural understanding from project inception.

Areas Requiring Special Attention for PRD:
-   **JSON Schema Definition:** Define a clear, robust JSON schema for the code blueprints and indexes, ensuring all necessary elements for call flow and data type analysis are captured (function names, paths, parameters with types, return types, call targets).
-   **LSP Integration Strategy:** Detail the specific LSP features to be leveraged for each supported language (TS/JS, Python) to capture call relationships and type information accurately. Address potential inconsistencies between LSPs.
-   **Indexing Logic:** Specify the algorithms for creating system-wide and module-based indexes. How are "key functional units" defined for system-wide views? How is "detail level" controlled for different index types?
-   **CLI Tool User Stories:** Define clear user stories for the AI context provisioning tool, focusing on ease of use for specifying context and formulating queries.
-   **Visualizer PoC Scope:** Clearly define the "basic" features for the call graph visualizer PoC. What interactions are essential (e.g., zoom/pan)? What information density is appropriate for an MVP? Confirm that location data for "click-to-code" is part of the JSON, even if the feature is post-MVP.

Development Context:
This brief was developed through iterative discussion, refining an initial vision that also included XML considerations (now pivoted to JSON as primary) and broader testing/user-tracking features (deferred post-MVP). The focus is squarely on LSP-driven structural extraction for improved AI and human comprehension of functional architecture. Research into tools like Codemap.app has validated the need for better code visualization, particularly for call flows.

Guidance on PRD Detail:
-   Provide detailed user stories for the LSP extraction, JSON generation, and indexing engine features. These are core to the MVP.
-   For the CLI tool and PoC Visualizer, higher-level epics with key user stories are sufficient, emphasizing the "proof of concept" nature for the visualizer.
-   Technical implementation options for the visualizer (e.g., specific graphing libraries) can be presented with pros/cons rather than a single recommendation.

User Preferences:
-   Emphasis on accuracy and token efficiency of the generated JSON for AI consumption.
-   The system should feel intuitive for developers, particularly those familiar with LSP-based tools.
-   Future visualizer development should aim for a clean, uncluttered UI that clearly presents call flows and allows for easy navigation (with features like filtering, click-to-code, and good layouts as future targets).
-   Initial focus on local processing; all user code remains on their machine.