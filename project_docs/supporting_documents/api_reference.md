# API Reference

> This document is a granulated shard from the main "Architectum Architecture Document" focusing on "API Reference and CLI Commands".

## Command-Line Interface (CLI) API

### Core Commands

#### `arch sync`
Processes codebase and updates System Map and JSON Mirror representations.

**Usage:**
```bash
arch sync [OPTIONS] [PATH]
```

**Parameters:**
- `PATH` (optional): Target directory to analyze (defaults to current directory)

**Options:**
- `--config-file`: Specify custom configuration file
- `--force`: Force full reprocessing, ignore cache
- `--verbose`: Enable detailed progress output
- `--dry-run`: Show what would be processed without making changes

**Examples:**
```bash
# Sync entire project
arch sync

# Sync specific directory
arch sync ./src

# Force full rebuild
arch sync --force

# Verbose output
arch sync --verbose
```

#### `arch blueprint`
Generates blueprint views from System Map and JSON Mirror data.

**Usage:**
```bash
arch blueprint [TYPE] [OPTIONS]
```

**Blueprint Types:**
- `path`: Generate path-based blueprint
- `method`: Generate method-focused blueprint  
- `yaml`: Generate from YAML definition file

**Global Options:**
- `--output`: Output file path
- `--format`: Output format (json, xml, markdown, dot)
- `--cache`: Enable/disable blueprint caching

#### `arch blueprint path`
Generate path-based blueprint analyzing directory structure.

**Usage:**
```bash
arch blueprint path [OPTIONS] <PATH>
```

**Options:**
- `--depth`: Analysis depth (0=unlimited, 1=immediate children, etc.)
- `--include-tests`: Include test files in analysis
- `--exclude-pattern`: Exclude files matching pattern

**Examples:**
```bash
# Analyze src directory with depth 2
arch blueprint path --depth 2 ./src

# Include tests in analysis
arch blueprint path --include-tests ./src

# Exclude node_modules
arch blueprint path --exclude-pattern "**/node_modules/**" ./
```

#### `arch blueprint method`
Generate method-focused blueprint for specific functions or classes.

**Usage:**
```bash
arch blueprint method [OPTIONS] <METHOD_IDENTIFIER>
```

**Options:**
- `--include-callers`: Include functions that call this method
- `--include-dependencies`: Include methods this method calls
- `--max-depth`: Maximum relationship traversal depth

**Examples:**
```bash
# Analyze specific function
arch blueprint method "UserService.authenticate"

# Include caller context
arch blueprint method --include-callers "processPayment"

# Deep dependency analysis
arch blueprint method --max-depth 3 "DataProcessor.transform"
```

#### `arch blueprint yaml`
Generate blueprint from YAML definition file.

**Usage:**
```bash
arch blueprint yaml [OPTIONS] <YAML_FILE>
```

**Options:**
- `--validate`: Validate YAML without generating blueprint
- `--save-as`: Save as persistent Feature Blueprint

**Examples:**
```bash
# Generate from YAML definition
arch blueprint yaml ./blueprints/auth-system.yaml

# Validate YAML file
arch blueprint yaml --validate ./blueprints/payment-flow.yaml

# Save as Feature Blueprint
arch blueprint yaml --save-as "Authentication System" ./blueprints/auth.yaml
```

### Utility Commands

#### `arch config`
Manage Architectum configuration.

**Usage:**
```bash
arch config [SUBCOMMAND] [OPTIONS]
```

**Subcommands:**
- `show`: Display current configuration
- `set`: Set configuration value
- `init`: Initialize default configuration

**Examples:**
```bash
# Show current config
arch config show

# Set configuration value  
arch config set cache.enabled true

# Initialize config file
arch config init
```

#### `arch cache`
Manage blueprint and processing cache.

**Usage:**
```bash
arch cache [SUBCOMMAND]
```

**Subcommands:**
- `clear`: Clear all cached data
- `status`: Show cache statistics
- `cleanup`: Remove stale cache entries

**Examples:**
```bash
# Clear all cache
arch cache clear

# Show cache statistics
arch cache status

# Clean up stale entries
arch cache cleanup
```

#### `arch version`
Display version information.

**Usage:**
```bash
arch version [OPTIONS]
```

**Options:**
- `--verbose`: Show detailed version and dependency information

## Internal API Interfaces

### System Map API
Core interfaces for interacting with the relationship graph.

#### Node Operations
```python
# Add node to System Map
add_node(node_id: str, node_type: NodeType, metadata: Dict[str, Any]) -> None

# Get node information
get_node(node_id: str) -> Optional[Node]

# Find nodes by type
find_nodes_by_type(node_type: NodeType) -> List[Node]

# Find nodes by pattern
find_nodes_by_pattern(pattern: str) -> List[Node]
```

#### Relationship Operations
```python
# Add relationship between nodes
add_relationship(from_node: str, to_node: str, relationship_type: RelationshipType, metadata: Dict[str, Any]) -> None

# Get relationships for node
get_relationships(node_id: str, direction: Direction = Direction.BOTH) -> List[Relationship]

# Traverse relationships
traverse_relationships(start_node: str, max_depth: int = None, relationship_filter: List[RelationshipType] = None) -> List[Path]
```

### JSON Mirrors API
Interfaces for accessing detailed file content representations.

#### Content Access
```python
# Get file content representation
get_file_content(file_path: str) -> Optional[FileContent]

# Get function definition
get_function_definition(file_path: str, function_name: str) -> Optional[FunctionDefinition]

# Get class definition  
get_class_definition(file_path: str, class_name: str) -> Optional[ClassDefinition]

# Search content by pattern
search_content(pattern: str, content_type: ContentType = None) -> List[SearchResult]
```

### Blueprint API
Interfaces for blueprint generation and management.

#### Blueprint Generation
```python
# Generate path-based blueprint
generate_path_blueprint(path: str, depth: int = 0, options: PathBlueprintOptions = None) -> Blueprint

# Generate method-based blueprint
generate_method_blueprint(method_identifier: str, options: MethodBlueprintOptions = None) -> Blueprint

# Generate from YAML definition
generate_yaml_blueprint(yaml_file: str, options: YamlBlueprintOptions = None) -> Blueprint
```

#### Blueprint Management
```python
# Save blueprint as Feature Blueprint
save_feature_blueprint(blueprint: Blueprint, name: str, description: str = None) -> str

# Load Feature Blueprint
load_feature_blueprint(name: str) -> Optional[Blueprint]

# List Feature Blueprints
list_feature_blueprints() -> List[FeatureBlueprintInfo]

# Delete Feature Blueprint
delete_feature_blueprint(name: str) -> bool
```

## Configuration API

### Configuration Schema
The configuration system uses YAML format with the following structure:

```yaml
# Core analysis settings
analysis:
  languages: ["python", "typescript", "javascript"]
  root_directories:
    frontend: "./src/frontend"
    backend: "./src/backend"
  
# File filtering
filters:
  include_patterns:
    - "**/*.py"
    - "**/*.ts"
    - "**/*.js"
  exclude_patterns:
    - "**/node_modules/**"
    - "**/__pycache__/**"
    - "**/dist/**"
  respect_gitignore: true

# Performance settings
performance:
  max_file_size: "10MB"
  parallel_processing: true
  max_workers: 4

# Caching configuration
cache:
  enabled: true
  location: "./.architectum/cache"
  max_size: "1GB"
  ttl_hours: 24

# Blueprint settings
blueprints:
  default_format: "json"
  token_optimization: true
  include_metadata: true
  
# Database settings
database:
  location: "./.architectum/system.db"
  backup_enabled: true
  backup_frequency: "daily"
```

### Environment Variables
- `ARCHITECTUM_CONFIG_FILE`: Override default configuration file location
- `ARCHITECTUM_CACHE_DIR`: Override cache directory location
- `ARCHITECTUM_LOG_LEVEL`: Set logging level (DEBUG, INFO, WARN, ERROR)
- `ARCHITECTUM_MAX_WORKERS`: Override parallel processing worker count