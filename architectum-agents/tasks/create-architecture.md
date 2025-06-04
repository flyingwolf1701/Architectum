# Architecture Creation Task

## Purpose

- To design a complete, robust, and well-documented technical architecture based on the project requirements (PRD, epics, brief), research findings, and user input.
- To make definitive technology choices and articulate the rationale behind them, leveraging the architecture template as a structural guide.
- To produce all necessary technical artifacts, ensuring the architecture is optimized for efficient implementation, particularly by AI developer agents, and validated against the `architect-checklist`.

## Instructions

### 1. Input Analysis & Setup

**Required Inputs:** PRD (`project_docs/core_documents/prd.md`), project brief (`project_docs/core_documents/project_brief.md`), and optionally `architectum-agents\data\technical-preferences.txt`

**Process:**
- Review all inputs thoroughly
    - Summarize key technical requirements, constraints, NFRs (Non-Functional Requirements), and the decided repository/service architecture derived from the inputs. Present this summary to the user for confirmation and to ensure mutual understanding.
    - Share initial architectural observations, potential challenges, or areas needing clarification based on the inputs.
      **Establish Interaction Mode for Architecture Creation:**
      - Ask the user: "How would you like to proceed with creating the architecture for this project? We can work:
        A. **Incrementally (Default & Recommended):** We'll go through each architectural decision, document section, or design point step-by-step. I'll present drafts, and we'll seek your feedback and confirmation before moving to the next part. This is best for complex decisions and detailed refinement.
        B. **"YOLO" Mode:** I can produce a more comprehensive initial draft of the architecture (or significant portions) for you to review more broadly first. We can then iterate on specific sections based on your feedback. This can be quicker for generating initial ideas but is generally not recommended if detailed collaboration at each step is preferred."
      - Request the user to select their preferred mode (e.g., "Please let me know if you'd prefer A or B.").
      - Once the user chooses, confirm the selected mode (e.g., "Okay, we will proceed in Incremental mode."). This chosen mode will govern how subsequent steps in this task are executed.

### 2. Resolve Ambiguities & Gather Missing Information:

**Key Areas:**
    - If key information is missing or requirements are unclear after initial review, formulate specific, targeted questions.
- **External APIs:** Use Context7 MCP server to read and understand latest docs for any technology we are working with. If you cannot get it from Context7, then request official docs, example requests/responses, schemas if not from deep research
- Present batched questions, document decisions before proceeding

### 3. Iterative Technology Selection & Design (Interactive, if not YOLO mode):

**For each major component/decision:**
- Present 2-3 viable options with pros/cons
- State recommended choice with clear rationale
- Consider `architectum-agents\data\technical-preferences.txt` 
- Get explicit user approval
- Document choice and rationale



### 4. Create Technical Artifacts (Incrementally, unless YOLO mode):

**Using `architectum-agents\templates\architecture-tmpl.md`, for each section:**
      - **Explain Purpose:** Briefly describe the artifact/section's importance and what it will cover.
      - **Draft Section-by-Section:** Present a draft of one logical section at a time.
        - Ensure the 'High-Level Overview' and 'Component View' sections accurately reflect and detail the repository/service architecture decided in the PRD.
      - **Incorporate Feedback:** Discuss the draft with the user, incorporate their feedback, and iterate as needed.
- **Advanced Options** (after initial feedback):
        1.  **Critical Self-Review & Requirements Alignment**
        2.  **Generate & Evaluate Alternative Architectural Approaches**
        3.  **Resilience, Scalability & Performance Stress Test (Conceptual)**
        4.  **Deep Dive into Technical Assumptions, Constraints & Dependencies**
        5.  **Security & Risk Assessment Review & Probing Questions**
        6.  **Collaborative Design Brainstorming & Pattern Exploration**
        7.  **Elicit 'Unforeseen Implications' & Future-Proofing Questions**
        8.  **Proceed to the Next [Architectural Section/Task].**

        After I perform the selected action, we can discuss the outcome and decide on any further revisions.
        When you're satisfied with the current draft of this section, we can move directly to [the next logical step, e.g., 'the next architectural component,' or if all sections are drafted, 'Step 5: Identify Missing Technical Stories / Refine Epics' or 'Step 6: Validate Architecture Against Checklist & Finalize Output']."

      - **Seek Approval:** Obtain explicit user approval for the section before moving to the next, or for the entire artifact if drafted holistically (in YOLO mode).

### 5. Identify Missing Technical Stories / Refine Epics (Interactive):

    - Based on the designed architecture, identify any necessary technical stories/tasks that are not yet captured in the PRD or epics (e.g., "Set up CI/CD pipeline for frontend deployment," "Implement authentication module using JWT," "Create base Docker images for backend services," "Configure initial database schema based on data models").
    - Explain the importance of these technical stories for enabling the functional requirements and successful project execution.
    - Collaborate with the user to refine these stories (clear description, acceptance criteria) and suggest adding them to the project backlog or relevant epics.
    - Review existing epics/stories from the PRD and suggest technical considerations or acceptance criteria refinements to ensure they are implementable based on the chosen architecture. For example, specifying API endpoints to be called, data formats, or critical library versions.
    - After collaboration, prepare a concise summary detailing all proposed additions, updates, or modifications to epics and user stories. If no changes are identified, explicitly state this.

### 6. Validate Architecture Against Checklist & Finalize Output:
    - Once the main architecture document components have been drafted and reviewed with the user, perform a comprehensive review using the `architect-checklist`.
    - Go through each item in the checklist to ensure the architecture document is comprehensive, addresses all key architectural concerns (e.g., security, scalability, maintainability, testability (including confirmation that coding standards and the testing strategy clearly define unit test location and naming conventions), developer experience), and that proposed solutions are robust.
    - For each checklist item, confirm its status (e.g., \[x] Completed, \[ ] N/A, \[!] Needs Attention).
    - If deficiencies, gaps, or areas needing more detail or clarification are identified based on the checklist:
      - Discuss these findings with the user.
      - Collaboratively make necessary updates, additions, or refinements to the architecture document to address these points.
    - After addressing all checklist points and ensuring the architecture document is robust and complete, present a summary of the checklist review to the user. This summary should highlight:
      - Confirmation that all relevant sections/items of the checklist have been satisfied by the architecture.
      - Any items marked N/A, with a brief justification.
      - A brief note on any significant discussions, decisions, or changes made to the architecture document as a result of the checklist review.
    - **Offer Design Architect Prompt (If Applicable):**
      - If the architecture includes UI components, ask the user if they would like to include a dedicated prompt for a "Design Architect" at the end of the main architecture document.
      - Explain that this prompt can capture specific UI considerations, notes from discussions, or decisions that don't fit into the core technical architecture document but are crucial for the Design Architect.
      - The prompt should also state that the Design Architect will subsequently operate in its specialized mode to define the detailed frontend architecture.
      - If the user agrees, collaboratively draft this prompt and append it to the architecture document.
    - Obtain final user approval for the complete architecture documentation generation.
    - **Recommend Next Steps for UI (If Applicable):**
      - After the main architecture document is finalized and approved:
      - If the project involves a user interface (as should be evident from the input PRD and potentially the architecture document itself mentioning UI components or referencing outputs from a Design Architect's UI/UX Specification phase):
        - Strongly recommend to the user that the next critical step for the UI is to engage the **Design Architect** agent.
        - Specifically, advise them to use the Design Architect's **'Frontend Architecture Mode'**.
        - Explain that the Design Architect will use the now-completed main Architecture Document and the detailed UI/UX specifications (e.g., `frontend-spec-tmpl.txt` or enriched PRD) as primary inputs to define the specific frontend architecture, select frontend libraries/frameworks (if not already decided), structure frontend components, and detail interaction patterns.

### Output Deliverables for Architecture Creation Phase

- A comprehensive Architecture Document, structured according to the `architecture-tmpl` (which is all markdown) or an agreed-upon format, including all sections detailed above.
- Clear Mermaid diagrams for architecture overview, data models, etc.
- A list of new or refined technical user stories/tasks ready for backlog integration.
- A summary of any identified changes (additions, updates, modifications) required for existing epics or user stories, or an explicit confirmation if no such changes are needed.
- A completed `architect-checklist` (or a summary of its validation).
- Optionally, if UI components are involved and the user agrees: A prompt for a "Design Architect" appended to the main architecture document, summarizing relevant UI considerations and outlining the Design Architect's next steps.