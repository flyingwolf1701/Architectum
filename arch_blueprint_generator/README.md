# Architectum Blueprint Generator

The Blueprint Generator is a core module of Architectum that creates structured JSON blueprints of codebases for consumption by AI agents and visualization tools.

## Key Features

- **Multiple Blueprint Types**:
  - `DirectoryBlueprint`: Represent a directory structure with configurable traversal depth
  - `FileSetBlueprint`: Represent a curated collection of files that may be logically related but not co-located
  - `CodeElementBlueprint`: Provide detailed view of specific code elements (functions, classes, methods) within a file

- **Configurable Detail Levels**:
  - `Minimal`: Basic structure and signatures
  - `Standard`: Types, parameters, returns, and properties
  - `Detailed`: Comments, annotations, and documentation

- **Flexible Integration**:
  - CLI for direct invocation
  - API for integration with other tools
  - Extensible design for supporting additional languages and blueprint types

## Usage

### Command Line Interface

```bash
# Generate directory blueprint
python scripts/blueprint/arch_blueprint.py directory-blueprint --path /path/to/directory --depth 1 --level minimal

# Generate file set blueprint
python scripts/blueprint/arch_blueprint.py fileset-blueprint --files file1.py,file2.py,file3.py --level standard

# Generate code element blueprint
python scripts/blueprint/arch_blueprint.py codeelement-blueprint --file /path/to/file.py --elements MyClass,my_function --level detailed

# Output to file
python scripts/blueprint/arch_blueprint.py directory-blueprint --path /path/to/directory --output output.json

# Help
python scripts/blueprint/arch_blueprint.py --help
```

## Architecture

The module follows a clean, modular design with clear separation of concerns:

- `models`: Core data structures and serialization logic
- `blueprints`: Blueprint implementations for different types
- `parsers`: Language-specific parsing logic
- `cli.py`: Command line interface
- `logging_config.py`: Logging configuration

## Development

### Testing

Run tests with pytest:

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/unit/models/test_base.py

# Run with coverage
pytest --cov=arch_blueprint_generator tests/
```

## Extending

The module is designed to be extensible in several ways:

- **Adding New Blueprint Types**: Extend `BlueprintBase` class
- **Supporting New Languages**: Add a parser for the language
- **Adding New Detail Levels**: Enhance existing parsers with new extraction capabilities

## Status

The Blueprint Generator is under active development as part of the Architectum project.
