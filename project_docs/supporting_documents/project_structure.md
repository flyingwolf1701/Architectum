# Project Structure

> This document is a granulated shard from the main "Architectum Architecture Document" focusing on "Project Structure and File Organization".

## Repository Structure

The Architectum project follows a monorepo structure with clear separation of concerns:

```plaintext
architectum/
├── .github/                    # CI/CD workflows and GitHub configuration
│   └── workflows/
│       ├── ci.yml             # Continuous integration pipeline
│       ├── release.yml        # Release automation
│       └── security.yml       # Security scanning
├── .architectum/              # Architectum workspace data (gitignored)
│   ├── cache/                 # Blueprint and processing cache
│   ├── system.db             # SQLite database for System Map
│   └── config.yaml           # Local configuration overrides
├── docs/                      # Project documentation
│   ├── index.md              # Documentation navigation hub
│   ├── core_documents/       # Core project documentation
│   │   ├── architecture.md   # Technical architecture (this doc family)
│   │   ├── prd.md           # Product Requirements Document
│   │   └── project-brief.md  # Project overview and goals
│   ├── epics/               # Epic-level documentation
│   │   ├── epic_1/          # Foundation & Core Infrastructure
│   │   ├── epic_2/          # Language Parsing & Relationship Extraction
│   │   ├── epic_3/          # Blueprint Generation System
│   │   ├── epic_4/          # Caching & Performance Optimization
│   │   └── epic_5/          # Proof-of-Concept Visualizer
│   ├── catalogs/            # YAML catalog files for tracking
│   │   ├── feature_catalog.yaml  # Feature-to-code mapping
│   │   ├── project_catalog.yaml  # Raw file inventory
│   │   └── test_catalog.yaml     # Test mapping and coverage
│   └── supporting_documents/ # Detailed supporting documentation
│       ├── api-reference.md     # CLI commands and internal APIs
│       ├── data-models.md       # Data structures and schemas
│       ├── operational-guidelines.md # Coding standards, testing, security
│       ├── project-structure.md # This document
│       └── tech-stack.md        # Technology selections and rationale
├── src/                     # Application source code
│   ├── architectum/         # Main application package
│   │   ├── __init__.py
│   │   ├── cli/            # Command-line interface
│   │   │   ├── __init__.py
│   │   │   ├── main.py     # CLI entry point and command routing
│   │   │   ├── sync.py     # 'arch sync' command implementation
│   │   │   ├── blueprint.py # 'arch blueprint' command implementation
│   │   │   ├── config.py   # 'arch config' command implementation
│   │   │   └── cache.py    # 'arch cache' command implementation
│   │   ├── core/           # Core business logic and domain models
│   │   │   ├── __init__.py
│   │   │   ├── models/     # Data models and domain entities
│   │   │   │   ├── __init__.py
│   │   │   │   ├── nodes.py        # Node types and definitions
│   │   │   │   ├── relationships.py # Relationship types and definitions
│   │   │   │   ├── blueprints.py   # Blueprint data models
│   │   │   │   └── content.py      # JSON Mirror content models
│   │   │   ├── system_map.py       # System Map graph implementation
│   │   │   ├── json_mirrors.py     # JSON Mirror content management
│   │   │   └── blueprint_engine.py # Blueprint generation logic
│   │   ├── parsers/        # Language-specific parsers
│   │   │   ├── __init__.py
│   │   │   ├── base.py     # Base parser interface
│   │   │   ├── python_parser.py    # Python AST parser
│   │   │   ├── typescript_parser.py # TypeScript/JavaScript parser
│   │   │   └── lsp_client.py       # Language Server Protocol client
│   │   ├── adapters/       # External system adapters
│   │   │   ├── __init__.py
│   │   │   ├── database.py         # SQLite database adapter
│   │   │   ├── file_system.py      # File system operations
│   │   │   ├── cache_manager.py    # Cache management
│   │   │   └── config_loader.py    # Configuration loading
│   │   ├── services/       # Business services and orchestration
│   │   │   ├── __init__.py
│   │   │   ├── sync_service.py     # Codebase synchronization service
│   │   │   ├── blueprint_service.py # Blueprint generation service
│   │   │   ├── analysis_service.py  # Code analysis coordination
│   │   │   └── cache_service.py     # Cache management service
│   │   └── utils/          # Shared utilities and helpers
│   │       ├── __init__.py
│   │       ├── logging.py          # Logging configuration
│   │       ├── validation.py       # Input validation utilities
│   │       ├── file_utils.py       # File operation utilities
│   │       └── performance.py      # Performance monitoring
│   └── visualizer/         # Proof-of-concept web visualizer (Epic 5)
│       ├── __init__.py
│       ├── app.py          # FastAPI web application
│       ├── static/         # Static web assets
│       ├── templates/      # HTML templates
│       └── api/           # Visualizer API endpoints
├── tests/                  # Test suite
│   ├── unit/              # Unit tests (mirror src structure)
│   │   ├── test_cli/
│   │   ├── test_core/
│   │   ├── test_parsers/
│   │   ├── test_adapters/
│   │   ├── test_services/
│   │   └── test_utils/
│   ├── integration/       # Integration tests
│   │   ├── test_sync_workflow.py
│   │   ├── test_blueprint_generation.py
│   │   └── test_database_persistence.py
│   ├── e2e/              # End-to-end tests
│   │   ├── test_complete_workflow.py
│   │   └── test_cli_commands.py
│   ├── fixtures/         # Test data and fixtures
│   │   ├── sample_projects/
│   │   ├── expected_outputs/
│   │   └── test_configs/
│   └── conftest.py       # Pytest configuration and shared fixtures
├── scripts/              # Utility scripts
│   ├── setup_dev.py      # Development environment setup
│   ├── benchmark.py      # Performance benchmarking
│   ├── migrate_db.py     # Database migration utilities
│   └── release.py        # Release preparation script
├── config/               # Default configuration files
│   ├── default_config.yaml    # Default system configuration
│   ├── logging_config.yaml    # Logging configuration
│   └── blueprints/           # Example blueprint definitions
│       ├── auth_system.yaml
│       └── data_layer.yaml
├── .env.example          # Example environment variables
├── .gitignore           # Git ignore rules
├── .flake8             # Flake8 configuration
├── pyproject.toml      # Project configuration and dependencies
├── requirements.txt    # Production dependencies
├── requirements-dev.txt # Development dependencies
├── LICENSE             # MIT License
└── README.md          # Project overview and setup instructions
```

## Directory Responsibilities

### Core Application (`src/architectum/`)

#### CLI Module (`src/architectum/cli/`)
**Purpose**: Command-line interface implementation
**Key Files**:
- `main.py`: Entry point, command routing, global options
- `sync.py`: Implementation of `arch sync` command
- `blueprint.py`: Implementation of `arch blueprint` commands
- `config.py`: Configuration management commands
- `cache.py`: Cache management commands

**Responsibilities**:
- Parse command-line arguments and options
- Validate user input and provide helpful error messages
- Coordinate with services layer for business logic
- Format and display output to users
- Handle CLI-specific error handling and logging

#### Core Module (`src/architectum/core/`)
**Purpose**: Core business logic and domain models
**Key Components**:
- `models/`: Data structures for nodes, relationships, blueprints
- `system_map.py`: Graph-based relationship management
- `json_mirrors.py`: File content representation management
- `blueprint_engine.py`: Blueprint generation algorithms

**Responsibilities**:
- Define core data structures and domain models
- Implement graph traversal and relationship queries
- Manage JSON Mirror content storage and retrieval
- Orchestrate blueprint generation logic
- Maintain data consistency and integrity

#### Parsers Module (`src/architectum/parsers/`)
**Purpose**: Language-specific code parsing
**Key Files**:
- `base.py`: Abstract parser interface and common functionality
- `python_parser.py`: Python AST-based parser implementation
- `typescript_parser.py`: TypeScript/JavaScript parser implementation
- `lsp_client.py`: Language Server Protocol client

**Responsibilities**:
- Parse source code files into structured representations
- Extract relationships between code elements
- Handle language-specific syntax and semantics
- Provide fallback parsing strategies
- Interface with Language Server Protocol implementations

#### Adapters Module (`src/architectum/adapters/`)
**Purpose**: External system integration
**Key Files**:
- `database.py`: SQLite database operations and schema management
- `file_system.py`: File system operations and path handling
- `cache_manager.py`: Cache storage and retrieval operations
- `config_loader.py`: Configuration file loading and validation

**Responsibilities**:
- Provide abstractions over external systems
- Handle persistence and storage operations
- Manage configuration loading and validation
- Implement caching strategies
- Provide clean interfaces for external dependencies

#### Services Module (`src/architectum/services/`)
**Purpose**: Business process orchestration
**Key Files**:
- `sync_service.py`: Codebase synchronization workflow
- `blueprint_service.py`: Blueprint generation workflow
- `analysis_service.py`: Code analysis coordination
- `cache_service.py`: Cache management workflow

**Responsibilities**:
- Orchestrate complex business workflows
- Coordinate between multiple core components
- Implement transactional operations
- Handle business rule enforcement
- Provide high-level APIs for CLI commands

#### Utils Module (`src/architectum/utils/`)
**Purpose**: Shared utilities and cross-cutting concerns
**Key Files**:
- `logging.py`: Structured logging configuration
- `validation.py`: Input validation and sanitization
- `file_utils.py`: File operation utilities
- `performance.py`: Performance monitoring and metrics

**Responsibilities**:
- Provide common utilities used across modules
- Implement cross-cutting concerns (logging, validation)
- Performance monitoring and metrics collection
- Error handling utilities
- Configuration and environment utilities

### Test Structure (`tests/`)

#### Unit Tests (`tests/unit/`)
**Structure**: Mirrors `src/` directory structure
**Purpose**: Test individual components in isolation
**Coverage**: Must achieve ≥80% line/branch coverage

#### Integration Tests (`tests/integration/`)
**Purpose**: Test component interactions and workflows
**Focus**: Database operations, file processing, service coordination

#### End-to-End Tests (`tests/e2e/`)
**Purpose**: Test complete user workflows through CLI
**Focus**: Real command execution, full system integration

#### Test Data (`tests/fixtures/`)
**Purpose**: Reusable test data and sample projects
**Structure**:
- `sample_projects/`: Complete sample codebases for testing
- `expected_outputs/`: Expected results for validation
- `test_configs/`: Configuration files for various test scenarios

## File Naming Conventions

### Python Files
- **Modules**: `snake_case.py` (e.g., `system_map.py`)
- **Test files**: `test_snake_case.py` (e.g., `test_system_map.py`)
- **Package initialization**: `__init__.py`

### Configuration Files
- **YAML**: `snake_case.yaml` (e.g., `default_config.yaml`)
- **Environment**: `.env.example`, `.env.local`
- **Tool configuration**: `.flake8`, `pyproject.toml`

### Documentation
- **Markdown**: `kebab-case.md` (e.g., `api-reference.md`)
- **Main docs**: `lowercase.md` (e.g., `architecture.md`)

## Import Guidelines

### Import Order
1. **Standard library imports** (alphabetical)
2. **Third-party imports** (alphabetical)
3. **Local application imports** (alphabetical)

### Import Style
```python
# Standard library
import asyncio
import logging
from pathlib import Path
from typing import Dict, List, Optional

# Third-party
import click
import networkx as nx
import yaml

# Local imports
from architectum.core.models.nodes import Node, NodeType
from architectum.core.system_map import SystemMap
from architectum.utils.logging import get_logger
```

### Absolute vs Relative Imports
- **Prefer absolute imports** for clarity and refactoring safety
- **Use relative imports** only within the same package for closely related modules
- **Never use relative imports** across package boundaries

## Development Workflow

### Local Development Setup
1. Clone repository
2. Create virtual environment: `uv venv --python 3.13`
3. Install dependencies: `uv pip install -r requirements-dev.txt`
4. Run tests: `pytest`
5. Run linting: `flake8 src tests`
6. Run type checking: `mypy src`

### Code Quality Gates
- **All tests pass**: `pytest tests/`
- **Linting passes**: `flake8 src tests`
- **Type checking passes**: `mypy src`
- **Coverage threshold**: `pytest --cov=src --cov-fail-under=80`
- **Security scanning**: Regular dependency audits

### Adding New Components

#### New Parser
1. Create parser file in `src/architectum/parsers/`
2. Implement `BaseParser` interface
3. Add unit tests in `tests/unit/test_parsers/`
4. Add integration test in `tests/integration/`
5. Update configuration to support new language

#### New CLI Command
1. Create command module in `src/architectum/cli/`
2. Implement Click command with proper help text
3. Add to command routing in `main.py`
4. Add CLI tests in `tests/e2e/`
5. Update documentation

#### New Service
1. Create service module in `src/architectum/services/`
2. Implement service interface and workflows
3. Add comprehensive unit tests
4. Add integration tests for external dependencies
5. Update API documentation

## Configuration Management

### Configuration Hierarchy
1. **Default configuration**: `config/default_config.yaml`
2. **Environment variables**: `ARCHITECTUM_*`
3. **Local configuration**: `.architectum/config.yaml`
4. **Command-line options**: Override all others

### Environment Variables
- `ARCHITECTUM_CONFIG_FILE`: Override default config location
- `ARCHITECTUM_CACHE_DIR`: Override cache directory
- `ARCHITECTUM_LOG_LEVEL`: Set logging level
- `ARCHITECTUM_MAX_WORKERS`: Override parallel processing workers

### Configuration Validation
All configuration files must be validated against schema on load. Invalid configurations should fail fast with clear error messages pointing to the specific validation failure.