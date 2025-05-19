# CLI Usage Guide for Architectum

## Overview

Architectum provides a powerful command-line interface (CLI) for generating code comprehension blueprints, synchronizing code changes, and managing blueprint definitions. This guide covers all available commands and common use cases.

## Installation

The CLI is automatically available after installing Architectum:

```bash
# Using uv (recommended)
uv add architectum

# Or using pip
pip install architectum
```

## Basic Commands

### Getting Help

```bash
# Get general help
arch --help

# Get help for a specific command
arch blueprint --help
arch sync --help
```

### Checking Version

```bash
arch --version
```

## Blueprint Commands

Architectum supports several blueprint types, each with its own subcommand.

### File-Based Blueprints

Generate blueprints based on specific files:

```bash
# Basic usage
arch blueprint file src/main.py src/utils.py

# Specify output file
arch blueprint file src/main.py src/utils.py --output blueprint.json

# Change output format
arch blueprint file src/main.py src/utils.py --format xml

# Change detail level
arch blueprint file src/main.py src/utils.py --detail-level detailed
```

### Component-Based Blueprints

Generate blueprints focused on specific components within files:

```bash
# Basic usage
arch blueprint component --file src/auth.py --component authenticate --component validate

# Multiple files
arch blueprint component --file src/auth.py --component authenticate --file src/user.py --component get_user

# With output specification
arch blueprint component --file src/auth.py --component authenticate --output auth-blueprint.json
```

### Feature Blueprints

Generate persistent blueprints from YAML definitions:

```bash
# Create from YAML
arch blueprint feature --yaml feature-definition.yaml

# With custom output
arch blueprint feature --yaml feature-definition.yaml --output auth-feature.json
```

### Temporary Blueprints

Similar to feature blueprints but not persisted:

```bash
arch blueprint temporary --yaml temp-definition.yaml
```

## Synchronization Commands

### Sync Files

Update Architectum's representation when files change:

```bash
# Sync a specific file
arch sync --file src/updated_file.py

# Sync a directory
arch sync --directory src/

# Sync multiple files
arch sync --file src/file1.py --file src/file2.py
```

### Sync Status

Check which files need synchronization:

```bash
arch sync --status
```

## YAML Blueprint Definitions

Blueprints can be defined in YAML files. Example structure:

```yaml
type: feature  # or file, component, temporary
name: user-authentication
description: "All components related to user authentication flow"
persistence: persistent  # or "temporary"
detail_level: standard  # or minimal, detailed

# Components to include
components:
  - file: src/auth/login.py
    # Empty elements means include entire file
    elements: []
  
  - file: src/auth/register.py
    elements: []
  
  - file: src/models/user.py
    elements:
      - validateCredentials
      - hashPassword
      - comparePasswords
```

## Common Workflows

### Analyzing a New Codebase

```bash
# Generate a directory blueprint to understand structure
arch blueprint directory --path /path/to/codebase --depth 2 --output codebase-overview.json

# Visualize the blueprint
arch visualize codebase-overview.json
```

### Creating Documentation for a Feature

```bash
# Define the feature in YAML
# Create feature-auth.yaml with components

# Generate a persistent feature blueprint
arch blueprint feature --yaml feature-auth.yaml

# List all saved feature blueprints
arch blueprint list
```

### Working with AI Assistants

```bash
# Generate a blueprint for AI context
arch blueprint file src/relevant/files/*.py --detail-level minimal --format xml

# The output can be provided to AI assistants for better code understanding
```

## Troubleshooting

### Common Errors

- **File not found**: Verify the file path is correct and accessible
- **Parser error**: Check if the file type is supported (Python, JavaScript/TypeScript)
- **YAML parsing error**: Validate your YAML blueprint definition using a YAML linter
- **Blueprint not found**: Check that the blueprint name is correct and has been created

### Performance Tips

- Use minimal detail level when complete information isn't needed
- Limit directory scans to relevant subdirectories
- Use incremental synchronization rather than full scans
- For large codebases, focus on specific features or components
- Consider using the `--filter` option to include only relevant file types
