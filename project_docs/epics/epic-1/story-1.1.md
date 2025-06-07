# Story 1.1: Project Structure Setup

## Status: Draft

## Story

- As a developer
- I want to set up the basic project structure with UV package management
- so that the development environment is ready for implementation.

## Acceptance Criteria (ACs)

1. Project directory structure is created following the defined architecture
2. UV package manager is configured and functional
3. Basic Python 3.13+ environment is established
4. Initial dependencies are defined and installable
5. Project can be built and basic commands execute successfully

## Tasks / Subtasks

- [ ] **Initialize Project Structure** (AC: 1)
  - [ ] Create main `src/architectum/` package structure
  - [ ] Create core modules: `core/`, `parsers/`, `blueprints/`, `caching/`, `cli/`, `services/`, `utils/`
  - [ ] Set up `tests/` directory with `unit/`, `integration/`, `e2e/`, `fixtures/`
  - [ ] Create `scripts/` directory for utility scripts
  - [ ] Create `config/` directory for default configurations

- [ ] **Configure UV Package Management** (AC: 2)
  - [ ] Initialize `pyproject.toml` with project metadata and UV configuration
  - [ ] Set up UV virtual environment with Python 3.13+
  - [ ] Configure `uv.lock` for dependency locking
  - [ ] Create `requirements.txt` for development dependencies

- [ ] **Define Core Dependencies** (AC: 4)
  - [ ] Add Click 8.x for CLI framework
  - [ ] Add NetworkX 3.x for graph processing
  - [ ] Add PyYAML for configuration management
  - [ ] Add pytest for testing framework
  - [ ] Add development dependencies: mypy, ruff

- [ ] **Create Essential Configuration Files** (AC: 1)
  - [ ] Configure `.gitignore` with Python/UV patterns
  - [ ] Set up `pyproject.toml` with tool configurations (pytest, mypy, ruff)
  - [ ] Create `.env.example` for environment variable template
  - [ ] Add basic `README.md` with setup instructions

- [ ] **Establish Entry Points** (AC: 5)
  - [ ] Create `main.py` as application entry point
  - [ ] Set up `src/architectum/__init__.py` with version info
  - [ ] Create basic CLI stub in `src/architectum/cli/__init__.py`
  - [ ] Configure console script entry point in `pyproject.toml`

- [ ] **Verify Installation and Build** (AC: 3, 5)
  - [ ] Test UV environment creation and activation
  - [ ] Verify all dependencies install correctly
  - [ ] Test that `python -m architectum` executes without errors
  - [ ] Verify `arch` command is available after installation
  - [ ] Run basic smoke test to ensure Python 3.13+ features work

- [ ] **Catalog System Maintenance (REQUIRED)**
  - [ ] Add new files to `project_docs/catalogs/project_catalog.yaml`
  - [ ] Update class/function listings for modified files in `project_catalog.yaml`
  - [ ] Update feature relationships in `project_docs/catalogs/feature_catalog.yaml`
  - [ ] Update tracking status for all modified files
  - [ ] Verify catalog entries align with implemented code

## Dev Technical Guidance

### Project Structure Alignment

This story implements the project structure defined in `project_docs/supporting_documents/project_structure.md`. Key structural requirements:

**Monorepo Structure:**
```
architectum/
├── src/architectum/           # Main application package
│   ├── core/                  # Business logic (System Map, JSON Mirrors)
│   ├── parsers/               # Language parsers and LSP integration
│   ├── blueprints/            # Blueprint generation system
│   ├── caching/               # Caching and performance optimization
│   ├── cli/                   # Command-line interface
│   ├── services/              # Application services and workflows
│   └── utils/                 # Shared utilities
├── tests/                     # Test suites (unit, integration, e2e)
├── scripts/                   # Utility scripts
├── config/                    # Default configurations
└── project_docs/              # Project documentation
```

### Technology Stack Requirements

From `project_docs/supporting_documents/tech_stack.md`:

**Core Technologies:**
- **Python 3.13+**: Latest stable Python with modern typing features
- **UV Package Manager**: Fast, reliable dependency management
- **Click 8.x**: CLI framework for command-line interface
- **NetworkX 3.x**: Graph processing for System Map
- **PyYAML**: Configuration file management
- **SQLite**: Embedded database (to be added in Epic 4)


### Catalog System Context

This story creates the foundational project structure that will house all future features. Key catalog entries to create:

**project_catalog.yaml entries:**
- Core package modules and their purposes
- Configuration files and their roles
- Test structure and organization
- Entry points and CLI setup

**feature_catalog.yaml entries:**
- Project initialization feature
- Package management setup feature
- Development environment configuration feature

### Architecture & Standards References

- **Project Structure**: `project_docs/supporting_documents/project_structure.md` - Section "Monorepo Structure"
- **Technology Stack**: `project_docs/supporting_documents/tech_stack.md` - Section "Core Technologies"
- **Development Workflow**: `project_docs/supporting_documents/project_structure.md` - Section "Development Workflow"

### Implementation Notes

1. **UV Best Practices**: Use `uv sync` for dependency installation, `uv run` for command execution
2. **Python 3.13 Features**: Leverage modern typing features and performance improvements
3. **Module Organization**: Follow the defined architecture with clear separation of concerns
4. **Testing Structure**: Mirror source structure in tests for maintainability
5. **Configuration Management**: Set up for hierarchical configuration (defaults → env vars → local config → CLI options)

## Story Progress Notes

### Agent Model Used: `<Agent Model Name/Version>`

### Completion Notes List

{Any notes about implementation choices, difficulties, or follow-up needed}

### Change Log

| Date | Change | Author | Notes |
|------|--------|---------|-------|
| | Initial story creation | PO Agent | Complete story definition for Epic 1.1 |