#!/usr/bin/env python3
"""
Architectum Project Initialization Script (Python Version)
Creates the complete project_docs structure for new projects.
"""

import os
import sys
from pathlib import Path

def question(query: str) -> str:
    """
    Prompts the user with a query and returns their input.
    """
    return input(query)

def create_directory_structure():
    """
    Creates the project_docs directory structure.
    """
    base_path = Path('project_docs')

    directories = [
        'catalogs',
        'core_documents',
        'epics',
        'supporting_documents'
    ]

    for directory in directories:
        dir_path = base_path / directory
        os.makedirs(dir_path, exist_ok=True) # exist_ok=True prevents error if dir already exists
        print(f"✓ Created {dir_path}")



def create_catalog_files():
    """
    Creates initial catalog YAML files.
    """
    catalogs_path = Path('project_docs') / 'catalogs'

    # Write project catalog
    project_catalog_path = catalogs_path / 'project_catalog.yaml'
    with open(project_catalog_path, 'w', encoding='utf-8') as f:
        f.write('files: []\n')
    print(f"✓ Created {project_catalog_path}")

    # Write feature catalog
    feature_catalog_path = catalogs_path / 'feature_catalog.yaml'
    with open(feature_catalog_path, 'w', encoding='utf-8') as f:
        f.write('features: []\n')
    print(f"✓ Created {feature_catalog_path}")

    # Write test catalog
    test_catalog_path = catalogs_path / 'test_catalog.yaml'
    with open(test_catalog_path, 'w', encoding='utf-8') as f:
        f.write('tests: []\n')
    print(f"✓ Created {test_catalog_path}")

def create_template_files():
    """
    Creates template files for core documents.
    """
    core_docs_path = Path('project_docs') / 'core_documents'

    # Project brief template
    project_brief_template = """# Project Brief: {Project Name}

## Problem Statement
{Describe the core problem being solved}

## Vision & Goals
- **Vision:** {High-level desired future state}
- **Primary Goals:**
  - Goal 1: {Specific, measurable goal}
  - Goal 2: {Another specific goal}

## Target Users
{Describe primary users and their characteristics}

## Key Features (MVP Scope)
- Feature 1: {Core functionality}
- Feature 2: {Essential capability}

## Known Constraints
- Technical: {Any known limitations}
- Timeline: {Time constraints}
- Budget: {Resource constraints}

## Success Metrics
{How will success be measured}
"""

    # PRD template
    prd_template = """# {Project Name} Product Requirements Document

## Status: Draft

## Goals & Context
{Copy from project brief and expand}

## Functional Requirements (MVP)
{Core functionality requirements}

## Non-Functional Requirements
{Performance, security, scalability requirements}

## Technical Assumptions
{Technology choices and constraints}

## Epic Overview
{High-level epic breakdown}

## Out of Scope (Post-MVP)
{Features deliberately excluded from MVP}
"""

    # Architecture template
    architecture_template = """# {Project Name} Architecture Document

## Status: Draft

## Technical Summary
{Brief overview of architecture approach}

## High-Level Overview
{System architecture and key components}

## Technology Stack
{Definitive technology selections}

## Component Architecture
{Detailed component breakdown}

## Data Models
{Core data structures and relationships}

## API Design
{API contracts and interfaces}

## Security & Compliance
{Security approach and requirements}

## Testing Strategy
{Testing approach and coverage}

## Deployment & Operations
{Deployment and operational considerations}
"""

    # Frontend Architecture template
    frontend_architecture_template = """# {Project Name} Frontend Architecture Document

## Status: Draft

## Technical Summary
{Brief overview of frontend architecture approach}

## Frontend Framework & Technology Stack
{Frontend technology selections and frameworks}

## Component Architecture
{Component organization and structure}

## State Management
{State management approach and patterns}

## Routing & Navigation
{Routing strategy and navigation structure}

## Build & Deployment
{Frontend build process and deployment strategy}

## Testing Strategy
{Frontend testing approach and coverage}

## Performance & Optimization
{Frontend performance considerations}
"""

    # Write template files
    templates = [
        ('project_brief.md', project_brief_template),
        ('prd.md', prd_template),
        ('architecture.md', architecture_template),
        ('frontend-architecture.md', frontend_architecture_template)
    ]

    for filename, content in templates:
        file_path = core_docs_path / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created {file_path}")

def create_index_file():
    """
    Creates the master index.md file with integrated project status tracking.
    """
    index_content = """# {Project Name} Documentation Index

## Project Status
**Current Phase:** initialization  
**Last Updated:** auto-generated  
**Agent Context:** project_planner

### Phase Progress
- [ ] **1. Ideation** - project_brief.md
- [ ] **2. Requirements** - prd.md  
- [ ] **3. Architecture** - architecture.md
- [ ] **4. Frontend Architecture** - frontend-architecture.md (if applicable)
- [ ] **5. Epic Breakdown** - epic-*.md files
- [ ] **6. Story Preparation** - story-*.md files
- [ ] **7. Doc Sharding** - supporting_documents/*
- [ ] **8. Ready for Dev** - all artifacts complete

**Current Epic:** None  
**Current Story:** None

### Notes
*Project notes and key decisions will be tracked here*

## Core Documents
- [Project Brief](core_documents/project_brief.md) - Initial project definition
- [Product Requirements](core_documents/prd.md) - Detailed requirements and epics
- [Architecture](core_documents/architecture.md) - Technical architecture and design
- [Frontend Architecture](core_documents/frontend-architecture.md) - Frontend-specific architecture (if applicable)

## Epics & Stories
{Epic directories will be created during planning phase}

## Supporting Documents
{Detailed documentation will be generated during sharding phase}

## Catalogs
- [Project Catalog](catalogs/project_catalog.yaml) - File and component inventory
- [Feature Catalog](catalogs/feature_catalog.yaml) - Feature-to-code mapping
- [Test Catalog](catalogs/test_catalog.yaml) - Test code mapping

---
*This index is automatically maintained by Architectum agents*
"""

    index_path = Path('project_docs') / 'index.md'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print(f"✓ Created {index_path}")



def main():
    """
    Main initialization function.
    """
    try:
        print('🚀 Initializing Architectum project structure...')

        # Check if project_docs already exists
        if Path('project_docs').exists():
            response = question('project_docs/ directory already exists. Continue? (y/N): ')
            if response.lower() != 'y':
                print('❌ Initialization cancelled.')
                sys.exit(1)

        # Create structure
        create_directory_structure()
        create_catalog_files()
        create_template_files()
        create_index_file()

        print('\n✅ Architectum project structure initialized successfully!')
        print('\nNext steps:')
        print('1. Run the project_planner agent')
        print('2. Start with ideation and project brief creation')
        print('3. Track progress using the phase checklist in project_docs/index.md')
        print('\nProject structure created in: project_docs/')

    except Exception as error:
        print(f'❌ Error during initialization: {error}', file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()