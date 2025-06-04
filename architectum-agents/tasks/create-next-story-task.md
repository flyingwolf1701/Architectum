# Create Next Story Task

## Purpose

Identify next logical story based on project progress and epic definitions. Prepare comprehensive, self-contained story file using Story Template with technical context for efficient Developer Agent implementation.

## Inputs

**Required:**
- `project_docs/index.md` (navigation hub)
- Epic files (`project_docs/epics/epic_{n}/epic-{n}.md`)
- Existing story files (`project_docs/epics/epic_{n}/story-{n}.{n}.md`)
- Main PRD, Architecture Documents, Frontend Architecture
- Supporting docs: Project Structure, Operational Guidelines, Tech Stack, Data Models, API Reference
- UI/UX Specs, Style Guides (if relevant)
- Story Template (`architectum-agents/templates/story-tmpl.md`)
- Story Draft Checklist (`architectum-agents/checklists/story-draft-checklist.md`)

## Instructions

### 1. Identify Next Story

**Process:**
- Find highest-numbered story file in `project_docs/epics/epic_{n}/`
- **If highest story exists:**
  - Verify Status is 'Done'
  - **If not Done:** Present alert with options:
    1. View incomplete story details
    2. Cancel new story creation
    3. Accept risk & Override to create next story
  - **If Done/Override:** Check Epic File for next story number
  - **If no next story in epic:** Find first story in next Epic with met prerequisites
- **If no story files exist:** Start with first story in `epic_1` with met prerequisites
- **If no suitable story found:** Report blocked prerequisites and HALT

**Output:** "Identified next story: {epicNum}.{storyNum} - {Story Title}"

### 2. Gather Story Requirements

**From Epic File:**
- Extract exact Title, Goal/User Story, Requirements, Acceptance Criteria, predefined Tasks
- Record original epic-defined scope for deviation analysis

### 3. Synthesize Technical Context

**Using `project_docs/index.md` as guide:**
- Review PRD, Architecture Documents thoroughly
- Extract specific relevant information:
  - Data Models (structure, validation)
  - API Reference (endpoints, schemas, auth)
  - Architectural patterns, component designs
  - UI/UX Specs, Style Guides (for UI stories)
  - Tech Stack specifics
  - Operational Guidelines (error handling, security)
- **Goal:** Collect details to avoid extensive Developer Agent searching
- Note discrepancies between epic and technical details

### 4. Verify Project Structure

- Cross-reference story requirements with Project Structure Guide
- Ensure file paths, component locations, module names align
- Document structural conflicts or undefined components
- Add "Project Structure Notes" section to story draft

### 5. Populate Story Template

**Create:** `project_docs/epics/epic_{epicNum}/story-{epicNum}.{storyNum}.md`

**Fill Template:**
- Story title, status (Draft), user story statement, ACs from epic
- **Dev Technical Guidance (CRITICAL):**
  - Embed critical technical snippets
  - Specific data structures, API details
  - References to specific document sections
  - UI Component/Style Guide references (for UI stories)
  - Make this Developer Agent's primary technical context source
- **Tasks/Subtasks:**
  - Generate detailed, sequential technical tasks
  - Link to ACs where applicable
  - Informed by gathered context
- Project structure alignment notes
- Deviation analysis from epic vs technical details
