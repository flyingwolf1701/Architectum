# Operational Guidelines

> This document is a granulated shard from the main "Architectum Architecture Document" focusing on "Coding Standards, Testing Strategy, Error Handling, and Security Best Practices".

## Coding Standards

### Mandatory Standards
These standards are mandatory for all code generation by AI agents and human developers. Deviations are not permitted unless explicitly approved and documented as an exception.

### Core Technology Standards

#### Python 3.13+ Specifics

**Style Guide & Linter:**
- Use Ruff for code formatting and linting
- Line length: 88 characters
- Configuration in pyproject.toml
- Use MyPy for type checking with strict mode enabled

**Naming Conventions:**
- Variables: `snake_case`
- Functions/Methods: `snake_case`
- Classes/Types: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Files: `snake_case.py`
- Modules/Packages: `snake_case`

**Type Safety:**
- All new functions and methods must have full type hints
- Use `from __future__ import annotations` for forward references
- Leverage Python 3.13+ type annotation features
- Run MyPy in CI with `disallow_untyped_defs = True`

**Immutability:**
- Use tuples for immutable sequences
- Consider `@dataclass(frozen=True)` for immutable classes
- Be mindful of mutable default arguments (use `field(default_factory=list)`)

**Error Handling:**
- Always raise specific, custom exceptions inheriting from base `ArchitectumException`
- Use `try-except-else-finally` blocks appropriately
- Avoid broad `except Exception:` clauses without re-raising or specific handling

**Resource Management:**
- Always use `with` statements for resources like files or DB connections
- Properly close database connections and file handles

**Asynchronous Operations:**
- Use `async`/`await` for I/O-bound operations
- Properly handle asyncio event loops
- Use `asyncio.gather()` for concurrent operations

#### TypeScript/JavaScript Specifics (for future web components)

**Style Guide & Linter:**
- ESLint with Airbnb config + Prettier
- TypeScript strict mode enabled
- No `any` type usage without explicit justification

**Naming Conventions:**
- Variables: `camelCase`
- Functions/Methods: `camelCase`
- Classes/Types/Interfaces: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Files: `kebab-case.ts`

### File Structure and Organization

**Unit Test File Organization:**
- Test files: `test_*.py` in parallel `tests/` directory
- Maintain mirror structure of source code in tests
- Use descriptive test function names: `test_should_parse_python_file_when_valid_syntax()`

**Project Structure Adherence:**
- Follow the layout defined in the Project Structure document
- Core business logic in `src/core/`
- Adapters and external integrations in `src/adapters/`
- CLI interface in `src/cli/`

**Import Organization:**
- Standard library imports first
- Third-party imports second
- Local application imports last
- Use absolute imports for clarity

### Documentation Standards

**Code Comments:**
- Explain _why_, not _what_, for complex logic
- Avoid redundant comments
- Use Google-style docstrings for Python functions and classes

**Function Documentation:**
```python
def extract_relationships(file_path: str, parser_type: ParserType) -> List[Relationship]:
    """Extract code relationships from a source file.
    
    Args:
        file_path: Path to the source file to analyze
        parser_type: Type of parser to use for extraction
        
    Returns:
        List of relationships found in the file
        
    Raises:
        FileNotFoundError: If the source file doesn't exist
        ParsingError: If the file cannot be parsed
    """
```

**Class Documentation:**
```python
class SystemMap:
    """Graph-based representation of code relationships.
    
    The SystemMap maintains nodes representing code elements (files, functions,
    classes) and edges representing relationships between them (calls, imports,
    inheritance). It provides efficient traversal and querying capabilities.
    
    Attributes:
        nodes: Dictionary mapping node IDs to Node objects
        relationships: List of Relationship objects
    """
```

## Testing Strategy

### Test Coverage Requirements
- Target: ≥80% line/branch coverage for all Python modules
- Measurement: Coverage.py with branch coverage enabled
- CI enforcement: Build fails if coverage drops below threshold

### Testing Framework Setup

#### Unit Testing
**Framework:** pytest with pytest-cov for coverage

**Scope:** Test individual functions, methods, classes, or small modules in isolation

**Location:** `tests/unit/` with mirror structure of `src/`

**Mocking/Stubbing:** 
- Use `unittest.mock` for mocking external dependencies
- Mock all external dependencies (network calls, file system, databases, time)
- Use `pytest.fixture` for common test setup

**Example Test Structure:**
```python
# tests/unit/parsers/test_python_parser.py
import pytest
from unittest.mock import Mock, patch
from src.parsers.python_parser import PythonParser
from src.models.nodes import FunctionNode

class TestPythonParser:
    def test_should_extract_function_when_valid_python_file(self):
        # Given
        parser = PythonParser()
        code_content = "def hello_world():\n    return 'Hello'"
        
        # When
        result = parser.parse_content(code_content, "test.py")
        
        # Then
        assert len(result.functions) == 1
        assert result.functions[0].name == "hello_world"
        
    def test_should_handle_syntax_error_gracefully(self):
        # Given
        parser = PythonParser()
        invalid_code = "def invalid_syntax(\n    # Missing closing parenthesis"
        
        # When/Then
        with pytest.raises(ParsingError) as exc_info:
            parser.parse_content(invalid_code, "invalid.py")
        assert "syntax error" in str(exc_info.value).lower()
        
    @patch('src.parsers.python_parser.ast.parse')
    def test_should_use_ast_parser(self, mock_ast_parse):
        # Given
        parser = PythonParser()
        code_content = "def test(): pass"
        
        # When
        parser.parse_content(code_content, "test.py")
        
        # Then
        mock_ast_parse.assert_called_once()
```

#### Property-Based Testing
**Framework:** Hypothesis for robust validation

**Usage:** Generate diverse code structures to test relationship extraction accuracy

```python
from hypothesis import given, strategies as st

@given(st.text(min_size=1), st.integers(min_value=1, max_value=100))
def test_node_id_generation_is_deterministic(name: str, line_number: int):
    """Node ID generation should be deterministic for same inputs."""
    node_id_1 = generate_node_id(name, line_number)
    node_id_2 = generate_node_id(name, line_number)
    assert node_id_1 == node_id_2
```

#### Integration Testing
**Scope:** Test interaction between several components within the application boundary

**Location:** `tests/integration/`

**Environment:** Use in-memory SQLite for database tests, temporary directories for file operations

**Example:**
```python
class TestSystemMapIntegration:
    def test_should_persist_and_retrieve_nodes(self, temp_db):
        # Given
        system_map = SystemMap(database_path=temp_db)
        node = FunctionNode(
            node_id="test_func_1",
            name="test_function",
            file_path="test.py"
        )
        
        # When
        system_map.add_node(node)
        retrieved_node = system_map.get_node("test_func_1")
        
        # Then
        assert retrieved_node is not None
        assert retrieved_node.name == "test_function"
```

#### End-to-End Testing
**Framework:** pytest with subprocess for CLI testing

**Scope:** Validate complete user workflows through the CLI

```python
def test_complete_sync_and_blueprint_workflow(tmp_path):
    """Test complete workflow from sync to blueprint generation."""
    # Given - Create test project structure
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "main.py").write_text("def hello(): return 'world'")
    
    # When - Run sync command
    result = subprocess.run([
        "arch", "sync", str(tmp_path)
    ], capture_output=True, text=True, cwd=tmp_path)
    
    # Then - Sync should succeed
    assert result.returncode == 0
    
    # When - Generate blueprint
    result = subprocess.run([
        "arch", "blueprint", "path", "--depth", "1", "src"
    ], capture_output=True, text=True, cwd=tmp_path)
    
    # Then - Blueprint should be generated
    assert result.returncode == 0
    assert "hello" in result.stdout
```

### Test Data Management
**Fixtures:** Use pytest fixtures for common test setup

```python
@pytest.fixture
def sample_python_file():
    return '''
class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b
    
    def multiply(self, a: int, b: int) -> int:
        return a * b

def main():
    calc = Calculator()
    result = calc.add(1, 2)
    return result
'''

@pytest.fixture
def temp_project_structure(tmp_path):
    """Create a temporary project with realistic structure."""
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    
    # Create sample files
    (src_dir / "models.py").write_text("class User: pass")
    (src_dir / "services.py").write_text("from models import User\nclass UserService: pass")
    
    return tmp_path
```

## Error Handling Strategy

### Exception Hierarchy
```python
class ArchitectumException(Exception):
    """Base exception for all Architectum errors."""
    pass

class ParsingError(ArchitectumException):
    """Raised when code parsing fails."""
    pass

class ConfigurationError(ArchitectumException):
    """Raised when configuration is invalid."""
    pass

class DatabaseError(ArchitectumException):
    """Raised when database operations fail."""
    pass

class BlueprintGenerationError(ArchitectumException):
    """Raised when blueprint generation fails."""
    pass

class LSPError(ArchitectumException):
    """Raised when LSP communication fails."""
    pass
```

### Logging Strategy
**Library:** Python `logging` module with structured output

**Format:** JSON for structured logging

**Configuration:**
```python
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        
        # Add correlation ID if available
        if hasattr(record, 'correlation_id'):
            log_entry["correlation_id"] = record.correlation_id
            
        # Add additional context
        if hasattr(record, 'file_path'):
            log_entry["file_path"] = record.file_path
            
        return json.dumps(log_entry)
```

**Usage Patterns:**
```python
import logging

logger = logging.getLogger(__name__)

def parse_file(file_path: str) -> FileContent:
    """Parse a source file and extract content."""
    logger.info("Starting file parsing", extra={"file_path": file_path})
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Parse content
        result = _parse_content(content, file_path)
        
        logger.info(
            "File parsing completed successfully", 
            extra={"file_path": file_path, "functions_found": len(result.functions)}
        )
        return result
        
    except SyntaxError as e:
        logger.error(
            "Syntax error in source file",
            extra={"file_path": file_path, "error": str(e)},
            exc_info=True
        )
        raise ParsingError(f"Syntax error in {file_path}: {e}")
        
    except Exception as e:
        logger.error(
            "Unexpected error during parsing",
            extra={"file_path": file_path, "error": str(e)},
            exc_info=True
        )
        raise ParsingError(f"Failed to parse {file_path}: {e}")
```

### External API Error Handling
**LSP Communication:**
```python
import asyncio
from typing import Optional

class LSPClient:
    async def get_call_hierarchy(self, file_path: str, position: Position) -> Optional[CallHierarchy]:
        """Get call hierarchy from LSP server with error handling."""
        max_retries = 3
        base_delay = 1.0
        
        for attempt in range(max_retries):
            try:
                response = await self._send_request("textDocument/callHierarchy", {
                    "textDocument": {"uri": f"file://{file_path}"},
                    "position": position.to_dict()
                })
                
                if response.get("error"):
                    raise LSPError(f"LSP server error: {response['error']}")
                    
                return CallHierarchy.from_dict(response.get("result", {}))
                
            except asyncio.TimeoutError:
                if attempt == max_retries - 1:
                    logger.error(
                        "LSP request timed out after all retries",
                        extra={"file_path": file_path, "attempts": max_retries}
                    )
                    raise LSPError(f"LSP timeout for {file_path}")
                    
                delay = base_delay * (2 ** attempt)  # Exponential backoff
                logger.warning(
                    "LSP request timed out, retrying",
                    extra={"file_path": file_path, "attempt": attempt + 1, "delay": delay}
                )
                await asyncio.sleep(delay)
                
            except Exception as e:
                logger.error(
                    "LSP communication error",
                    extra={"file_path": file_path, "error": str(e)},
                    exc_info=True
                )
                if attempt == max_retries - 1:
                    raise LSPError(f"LSP communication failed: {e}")
                
        return None
```

## Security Best Practices

### Input Validation
**File Path Validation:**
```python
import os
from pathlib import Path

def validate_file_path(file_path: str, allowed_extensions: List[str] = None) -> Path:
    """Validate and sanitize file paths."""
    # Convert to Path object for safe handling
    path = Path(file_path).resolve()
    
    # Prevent directory traversal
    try:
        path.relative_to(Path.cwd())
    except ValueError:
        raise ConfigurationError(f"File path outside project directory: {file_path}")
    
    # Check file exists
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check extension if specified
    if allowed_extensions and path.suffix not in allowed_extensions:
        raise ParsingError(f"Unsupported file type: {path.suffix}")
    
    # Check file size (prevent DoS)
    if path.stat().st_size > 10 * 1024 * 1024:  # 10MB limit
        raise ParsingError(f"File too large: {file_path}")
    
    return path
```

**Configuration Validation:**
```python
from typing import Any, Dict
import yaml

def validate_configuration(config_data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate configuration data."""
    required_fields = ["analysis", "filters", "cache"]
    
    for field in required_fields:
        if field not in config_data:
            raise ConfigurationError(f"Missing required configuration field: {field}")
    
    # Validate file patterns
    if "include_patterns" in config_data.get("filters", {}):
        for pattern in config_data["filters"]["include_patterns"]:
            if not isinstance(pattern, str):
                raise ConfigurationError("Include patterns must be strings")
    
    # Validate cache size
    cache_config = config_data.get("cache", {})
    if "max_size" in cache_config:
        max_size = cache_config["max_size"]
        if not isinstance(max_size, str) or not max_size.endswith(("MB", "GB")):
            raise ConfigurationError("Cache max_size must be in format '100MB' or '1GB'")
    
    return config_data
```

### Secrets Management
**Environment Variables:**
```python
import os
from typing import Optional

def get_secret(key: str, default: Optional[str] = None) -> Optional[str]:
    """Safely retrieve secrets from environment variables."""
    value = os.getenv(key, default)
    
    # Never log secret values
    if value:
        logger.info(f"Retrieved secret for key: {key}")
    else:
        logger.warning(f"Secret not found for key: {key}")
    
    return value

# Configuration module
class Config:
    def __init__(self):
        self.cache_dir = os.getenv("ARCHITECTUM_CACHE_DIR", "./.architectum/cache")
        self.log_level = os.getenv("ARCHITECTUM_LOG_LEVEL", "INFO")
        self.max_workers = int(os.getenv("ARCHITECTUM_MAX_WORKERS", "4"))
        
        # Validate configuration
        if self.max_workers < 1 or self.max_workers > 16:
            raise ConfigurationError("ARCHITECTUM_MAX_WORKERS must be between 1 and 16")
```

### Database Security
**SQLite Security:**
```python
import sqlite3
from contextlib import contextmanager

class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = Path(db_path).resolve()
        
        # Ensure database directory exists and has proper permissions
        self.db_path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    
    @contextmanager
    def get_connection(self):
        """Get database connection with proper security settings."""
        conn = None
        try:
            conn = sqlite3.connect(
                self.db_path,
                timeout=30.0,
                check_same_thread=False
            )
            
            # Enable foreign key constraints
            conn.execute("PRAGMA foreign_keys = ON")
            
            # Set secure permissions on database file
            self.db_path.chmod(0o600)
            
            yield conn
            
        except Exception as e:
            if conn:
                conn.rollback()
            logger.error(f"Database error: {e}", exc_info=True)
            raise DatabaseError(f"Database operation failed: {e}")
            
        finally:
            if conn:
                conn.close()
```

### Code Injection Prevention
**Safe AST Processing:**
```python
import ast
from typing import Any

class SafeASTProcessor:
    """Safely process Python AST without executing code."""
    
    ALLOWED_NODE_TYPES = {
        ast.Module, ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom,
        ast.Call, ast.Name, ast.Attribute, ast.Constant, ast.arg
    }
    
    def parse_safely(self, code: str, filename: str) -> ast.AST:
        """Parse code safely without executing it."""
        try:
            tree = ast.parse(code, filename=filename)
            self._validate_ast_safety(tree)
            return tree
            
        except SyntaxError as e:
            raise ParsingError(f"Syntax error in {filename}: {e}")
    
    def _validate_ast_safety(self, node: ast.AST) -> None:
        """Validate AST contains only safe node types."""
        for child in ast.walk(node):
            if type(child) not in self.ALLOWED_NODE_TYPES:
                logger.warning(f"Skipping potentially unsafe AST node: {type(child).__name__}")
```

## Performance Optimization Guidelines

### Memory Management
**Large File Handling:**
```python
def process_large_file(file_path: Path) -> FileContent:
    """Process large files efficiently."""
    file_size = file_path.stat().st_size
    
    if file_size > 100 * 1024 * 1024:  # 100MB
        logger.warning(f"Processing very large file: {file_path} ({file_size / 1024 / 1024:.1f}MB)")
    
    # Use generator for memory efficiency
    def read_chunks():
        with open(file_path, 'r', encoding='utf-8') as f:
            while True:
                chunk = f.read(8192)  # 8KB chunks
                if not chunk:
                    break
                yield chunk
    
    # Process in chunks to avoid memory exhaustion
    content_parts = []
    for chunk in read_chunks():
        content_parts.append(chunk)
    
    return parse_content(''.join(content_parts), str(file_path))
```

**Caching Strategy:**
```python
from functools import lru_cache
import hashlib

class CacheManager:
    def __init__(self, max_size: int = 1000):
        self.max_size = max_size
        self._cache = {}
    
    def get_content_hash(self, file_path: str) -> str:
        """Generate hash for file content."""
        with open(file_path, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    
    @lru_cache(maxsize=1000)
    def get_parsed_content(self, file_path: str, content_hash: str) -> FileContent:
        """Cache parsed content with content hash for invalidation."""
        cache_key = f"{file_path}:{content_hash}"
        
        if cache_key in self._cache:
            return self._cache[cache_key]
        
        # Parse and cache
        content = parse_file(file_path)
        self._cache[cache_key] = content
        
        # Cleanup old entries if needed
        if len(self._cache) > self.max_size:
            oldest_key = next(iter(self._cache))
            del self._cache[oldest_key]
        
        return content
```