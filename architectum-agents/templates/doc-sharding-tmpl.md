# Document Sharding Plan Template

This plan directs the agent on how to break down large source documents into smaller, granular files during its Librarian Phase. The agent will refer to this plan to identify source documents, the specific sections to extract, and the target filenames for the sharded content.

---

## 1. Source Document: PRD (Project Requirements Document)

- **Note to Agent:** The exact filename of the PRD is `project_docs/core_documents/prd.md`.

### 1.1. Epic Granulation

- **Instruction:** For each Epic identified within the PRD:
- **Source Section(s) to Copy:** The complete text for the Epic, including its main description, goals, and all associated user stories or detailed requirements under that Epic. Ensure to capture content starting from a heading like "**Epic X:**" up to the next such heading or end of the "Epic Overview" section.
- **Target File Pattern:** `project_docs/epics/epic_<id>/epic-<id>.md`
  - _Agent Note: `<id>` should correspond to the Epic number._

---

## 2. Source Document: Main Architecture Document

- **Note to Agent:** The exact filename is `project_docs\core_documents\architecture.md`.

### 2.1. Core Architecture Granules

- **Source Section(s) to Copy:** Section(s) detailing "API Reference", "API Endpoints", or "Service Interfaces".
- **Target File:** `project_docs/supporting_documents/api-reference.md`

- **Source Section(s) to Copy:** Section(s) detailing "Data Models", "Database Schema", "Entity Definitions".
- **Target File:** `project_docs/supporting_documents/data-models.md`

- **Source Section(s) to Copy:** Section(s) titled "Environment Variables Documentation", "Configuration Settings", "Deployment Parameters", or relevant subsections within "Infrastructure and Deployment Overview" if a dedicated section is not found.
- **Target File:** `project_docs/supporting_documents/environment-vars.md`

  - _Agent Note: Prioritize a dedicated 'Environment Variables' section or linked 'environment-vars.md' source if available. If not, extract relevant configuration details from 'Infrastructure and Deployment Overview'. This shard is for specific variable definitions and usage._

- **Source Section(s) to Copy:** Section(s) detailing "Project Structure".
- **Target File:** `project_docs/supporting_documents/project-structure.md`

  - _Agent Note: If the project involves multiple repositories (not a monorepo), ensure this file clearly describes the structure of each relevant repository or links to sub-files if necessary._

- **Source Section(s) to Copy:** Section(s) detailing "Technology Stack", "Key Technologies", "Libraries and Frameworks", or "Definitive Tech Stack Selections".
- **Target File:** `project_docs/supporting_documents/tech-stack.md`

- **Source Section(s) to Copy:** Sections detailing "Coding Standards", "Development Guidelines", "Best Practices", "Testing Strategy", "Testing Decisions", "QA Processes", "Overall Testing Strategy", "Error Handling Strategy", and "Security Best Practices".
- **Target File:** `project_docs/supporting_documents/operational-guidelines.md`

  - _Agent Note: This file consolidates several key operational aspects. Ensure that the content from each source section ("Coding Standards", "Testing Strategy", "Error Handling Strategy", "Security Best Practices") is clearly delineated under its own H3 (###) or H4 (####) heading within this document._

- **Source Section(s) to Copy:** Section(s) titled "Component View" (including sub-sections like "Architectural / Design Patterns Adopted").
- **Target File:** `project_docs/supporting_documents/component-view.md`

- **Source Section(s) to Copy:** Section(s) titled "Core Workflow / Sequence Diagrams" (including all sub-diagrams).
- **Target File:** `project_docs/supporting_documents/sequence-diagrams.md`

- **Source Section(s) to Copy:** Section(s) titled "Infrastructure and Deployment Overview".
- **Target File:** `project_docs/supporting_documents/infra-deployment.md`

  - _Agent Note: This is for the broader overview, distinct from the specific `project_docs/supporting_documents/environment-vars.md`._

- **Source Section(s) to Copy:** Section(s) titled "Key Reference Documents".
- **Target File:** `project_docs/supporting_documents/key-references.md`

---

## 3. Source Document(s): Front-End Specific Documentation

- **Note to Agent:** The primary filename for frontend architecture is `project_docs/core_documents/frontend-architecture.md`. Multiple FE documents might exist. Confirm with user that this is the only one.

### 3.1. Front-End Granules

- **Source Section(s) to Copy:** Section(s) detailing "Front-End Project Structure" or "Detailed Frontend Directory Structure".
- **Target File:** `project_docs/supporting_documents/frontend-project-structure.md`

- **Source Section(s) to Copy:** Section(s) detailing "UI Style Guide", "Brand Guidelines", "Visual Design Specifications", or "Styling Approach".
- **Target File:** `project_docs/supporting_documents/frontend-style-guide.md`

  - _Agent Note: This section might be a sub-section or refer to other documents (e.g., `ui-ux-spec.txt`). Extract the core styling philosophy and approach defined within the frontend architecture document itself._

- **Source Section(s) to Copy:** Section(s) detailing "Component Library", "Reusable UI Components Guide", "Atomic Design Elements", or "Component Breakdown & Implementation Details".
- **Target File:** `project_docs/supporting_documents/frontend-component-guide.md`

- **Source Section(s) to Copy:** Section(s) detailing "Front-End Coding Standards" (specifically for UI development, e.g., JavaScript/TypeScript style, CSS naming conventions, accessibility best practices for FE).
- **Target File:** `project_docs/supporting_documents/frontend-coding-standards.md`

  - _Agent Note: A dedicated top-level section for this might not exist. If not found, this shard might be empty or require cross-referencing with the main architecture's coding standards. Extract any frontend-specific coding conventions mentioned._

- **Source Section(s) to Copy:** Section(s) titled "State Management In-Depth".
- **Target File:** `project_docs/supporting_documents/frontend-state-management.md`

- **Source Section(s) to Copy:** Section(s) titled "API Interaction Layer".
- **Target File:** `project_docs/supporting_documents/frontend-api-interaction.md`

- **Source Section(s) to Copy:** Section(s) titled "Routing Strategy".
- **Target File:** `project_docs/supporting_documents/frontend-routing-strategy.md`

- **Source Section(s) to Copy:** Section(s) titled "Frontend Testing Strategy".
- **Target File:** `project_docs/supporting_documents/frontend-testing-strategy.md`

---

CRITICAL: **Index Management:** After creating the files, update `project_docs/index.md` as needed to reference and describe each doc - do not mention granules or where it was sharded from, just doc purpose - as the index also contains other doc references potentially.
