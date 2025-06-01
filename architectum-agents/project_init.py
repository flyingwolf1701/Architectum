#!/usr/bin/env python3
"""
Architectum Project Initialization Script (Python Version)
Creates the complete project_docs structure for new projects.
"""

import os
import sys
# The 'yaml' module is provided by the 'pyyaml' package.
# You need to install pyyaml: pip install pyyaml or uv add pyyaml
import yaml
import subprocess
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

def create_project_checklist():
    """
    Creates the master project checklist YAML file.
    """
    checklist_data = {
        'project_status': {
            'current_phase': 'initialization',
            'last_updated': 'auto-generated',
            'agent_context': 'project_planner'
        },
        'phases': {
            '1_ideation': {
                'status': 'pending',
                'artifacts': ['project_brief.md'],
                'completed': False
            },
            '2_requirements': {
                'status': 'pending',
                'artifacts': ['prd.md'],
                'completed': False
            },
            '3_architecture': {
                'status': 'pending',
                'artifacts': ['architecture.md'],
                'completed': False
            },
            '4_epic_breakdown': {
                'status': 'pending',
                'artifacts': ['epic-*.md files'],
                'completed': False
            },
            '5_story_preparation': {
                'status': 'pending',
                'artifacts': ['story-*.md files'],
                'completed': False
            },
            '6_doc_sharding': {
                'status': 'pending',
                'artifacts': ['supporting_documents/*'],
                'completed': False
            },
            '7_ready_for_dev': {
                'status': 'pending',
                'artifacts': ['all artifacts complete'],
                'completed': False
            }
        },
        'current_epic': None,
        'current_story': None,
        'notes': []
    }

    checklist_path = Path('project_docs') / 'project_checklist.yaml'
    # Use default_flow_style=False to prevent in-line dictionary/list representation
    # Use width to control line wrapping; None or a large number for no wrapping
    yaml_content = yaml.dump(checklist_data, sort_keys=False, default_flow_style=False, width=1000)

    with open(checklist_path, 'w', encoding='utf-8') as f:
        f.write(yaml_content)
    print(f"✓ Created {checklist_path}")

def create_catalog_files():
    """
    Creates initial catalog YAML files.
    """
    # Project catalog structure
    project_catalog = {
        'files': []
    }

    # Feature catalog structure
    feature_catalog = {
        'features': []
    }
    
    # Test catalog structure (added to match Node.js script)
    test_catalog = {
        'tests': [] # Assuming 'tests' as the key for consistency
    }

    catalogs_path = Path('project_docs') / 'catalogs'

    # Write project catalog
    project_catalog_path = catalogs_path / 'project_catalog.yaml'
    with open(project_catalog_path, 'w', encoding='utf-8') as f:
        yaml.dump(project_catalog, f, default_flow_style=False)
    print(f"✓ Created {project_catalog_path}")

    # Write feature catalog
    feature_catalog_path = catalogs_path / 'feature_catalog.yaml'
    with open(feature_catalog_path, 'w', encoding='utf-8') as f:
        yaml.dump(feature_catalog, f, default_flow_style=False)
    print(f"✓ Created {feature_catalog_path}")

    # Write test catalog
    test_catalog_path = catalogs_path / 'test_catalog.yaml'
    with open(test_catalog_path, 'w', encoding='utf-8') as f:
        yaml.dump(test_catalog, f, default_flow_style=False)
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

    # Write template files
    templates = [
        ('project_brief.md', project_brief_template),
        ('prd.md', prd_template),
        ('architecture.md', architecture_template)
    ]

    for filename, content in templates:
        file_path = core_docs_path / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created {file_path}")

def create_index_file():
    """
    Creates the master index.md file.
    """
    index_content = """# {Project Name} Documentation Index

## Project Status
See `project_checklist.yaml` for current phase and progress.

## Core Documents
- [Project Brief](core_documents/project_brief.md) - Initial project definition
- [Product Requirements](core_documents/prd.md) - Detailed requirements and epics
- [Architecture](core_documents/architecture.md) - Technical architecture and design

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

def check_dependencies():
    """
    Checks if pyyaml is available.
    """
    try:
        import yaml # This imports the 'yaml' module, which is provided by the 'pyyaml' package.
        return True
    except ImportError:
        print('❌ Required dependency "pyyaml" not found.')
        print('Please install it using: pip install pyyaml or uv add pyyaml')
        return False

def main():
    """
    Main initialization function.
    """
    try:
        print('🚀 Initializing Architectum project structure...')

        # Check dependencies
        if not check_dependencies():
            sys.exit(1)

        # Check if project_docs already exists
        if Path('project_docs').exists():
            response = question('project_docs/ directory already exists. Continue? (y/N): ')
            if response.lower() != 'y':
                print('❌ Initialization cancelled.')
                sys.exit(1)

        # Create structure
        create_directory_structure()
        create_project_checklist()
        create_catalog_files()
        create_template_files()
        create_index_file()

        print('\n✅ Architectum project structure initialized successfully!')
        print('\nNext steps:')
        print('1. Run the project_planner agent')
        print('2. Start with ideation and project brief creation')
        print('3. Follow the project_checklist.yaml for progress tracking')
        print('\nProject structure created in: project_docs/')

    except Exception as error:
        print(f'❌ Error during initialization: {error}', file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

