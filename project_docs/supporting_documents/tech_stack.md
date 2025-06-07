# Technology Stack

> This document is a granulated shard from the main "Architectum Architecture Document" focusing on "Definitive Tech Stack Selections".

## Definitive Technology Selections

This document serves as the **single source of truth** for all technology selections in the Architectum project. All components must adhere to these choices.

### Core Languages & Runtime

| Category | Technology | Version | Description | Justification |
|----------|------------|---------|-------------|---------------|
| **Primary Language** | Python | 3.13+ | Core system implementation | Modern features, excellent AST support, strong ecosystem |
| **Package Management** | UV | Latest | Fast Python package management | Superior performance over pip/poetry, reliable dependency resolution |
| **Runtime Environment** | Python 3.13 | 3.13+ | System execution environment | Latest stable Python with modern typing features |

### Core Frameworks & Libraries

| Category | Technology | Version | Description | Justification |
|----------|------------|---------|-------------|---------------|
| **CLI Framework** | Click | 8.x | Command-line interface development | Intuitive API, excellent help generation, widely adopted |
| **Graph Processing** | NetworkX | 3.x | System Map relationship modeling | Mature graph algorithms, extensive documentation |
| **Database** | SQLite | 3.x | Embedded database for persistence | Zero-configuration, reliable, sufficient for local tool |
| **Async Framework** | asyncio | Built-in | Asynchronous operations (LSP) | Native Python async support, no external dependencies |

### Language Server Integration

| Category | Technology | Version | Description | Justification |
|----------|------------|---------|-------------|---------------|
| **TypeScript LSP** | TypeScript Language Server | Latest | JavaScript/TypeScript analysis | Official Microsoft implementation, comprehensive features |
| **Python LSP** | Pylsp | Latest | Python language analysis | Reliable Python LSP implementation, good performance |
| **LSP Client** | python-lsp-jsonrpc | Latest | LSP communication protocol | Standard LSP JSON-RPC implementation |

### Development & Testing

| Category | Technology | Version | Description | Justification |
|----------|------------|---------|-------------|---------------|
| **Testing Framework** | pytest | 7.x | Unit and integration testing | Industry standard, excellent plugin ecosystem |
| **Test Coverage** | pytest-cov | Latest | Code coverage measurement | Seamless pytest integration, detailed reporting |
| **Property Testing** | Hypothesis | 6.x | Property-based testing | Robust validation for complex algorithms |
| **Code Formatting & Linting** | Ruff | Latest | Fast Python formatter and linter | Modern all-in-one Python code quality tool |
| **Type Checking** | MyPy | 1.x | Static type checking | Best-in-class Python type checker |

### Data & Serialization

| Category | Technology | Version | Description | Justification |
|----------|------------|---------|-------------|---------------|
| **Configuration** | PyYAML | 6.x | YAML configuration parsing | Human-readable config format, standard library |
| **JSON Processing** | Built-in json | Built-in | JSON serialization | No external dependency needed, sufficient performance |
| **Data Classes** | dataclasses | Built-in | Structured data representation | Clean API, type-friendly, no external dependencies |

### Performance & Caching

| Category | Technology | Version | Description | Justification |
|----------|------------|---------|-------------|---------------|
| **File Hashing** | hashlib | Built-in | Change detection via file hashing | Cryptographically secure, fast performance |
| **Caching** | functools.lru_cache | Built-in | In-memory caching | Built-in, efficient, no external dependencies |
| **Parallel Processing** | concurrent.futures | Built-in | Multi-threaded file processing | Built-in thread pool, simple API |

### Future Extensions (Post-MVP)

| Category | Technology | Version | Description | Notes |
|----------|------------|---------|-------------|-------|
| **Web Visualizer** | FastAPI | 0.1x | Web API for visualizer | When web interface is needed |
| **Frontend Framework** | React | 18.x | Visualization interface | If web UI becomes priority |
| **Graph Visualization** | D3.js | 7.x | Interactive graph rendering | For advanced visualization features |

## Technology Selection Principles

### 1. Minimize External Dependencies
- Prefer Python built-in libraries when sufficient
- Each external dependency must provide significant value
- Avoid dependencies with large dependency trees
- Pin versions to prevent unexpected breaking changes

### 2. Reliability Over Optimization
- Choose mature, well-tested libraries over cutting-edge alternatives
- NetworkX for graph operations due to comprehensive API and stability
- SQLite for persistence due to zero-configuration reliability
- Standard library solutions when they meet requirements

### 3. Developer Experience Priority
- Tools must work well together
- Clear error messages and good documentation required
- IDE support and type checking compatibility essential
- Testing frameworks must be easy to use and maintain

### 4. Long-term Stability
- Prefer mature, widely-adopted technologies
- Avoid experimental or rapidly-changing libraries
- Consider Python ecosystem compatibility
- Ensure technologies align with Python's development direction

## Dependency Management Strategy

### Version Pinning Policy
- **Major versions**: Pin to prevent breaking changes (click>=8.0.0,<9.0.0)
- **Minor versions**: Allow for bug fixes and features within major version
- **Patch versions**: Generally allow automatic updates
- **Critical dependencies**: Pin exact versions if stability is paramount

### Dependency Audit Process
1. **Weekly dependency check**: `uv pip list --outdated`
2. **Security scanning**: Regular audit for known vulnerabilities
3. **Testing before updates**: Run full test suite before accepting updates
4. **Documentation**: Update docs when dependencies change behavior

### Approved Alternatives

If primary choices become unavailable, these alternatives are pre-approved:

| Primary | Alternative | Reason |
|---------|-------------|---------|
| NetworkX | igraph | If performance becomes critical |
| Click | argparse | If dependency reduction needed |
| PyYAML | tomllib | If moving to TOML configuration |
| pytest | unittest | If removing external test dependencies |

## Platform Compatibility

### Supported Platforms
- **Primary**: Linux (Ubuntu 22.04+, RHEL 8+)
- **Primary**: macOS (12.0+)  
- **Primary**: Windows (10+, Windows Server 2019+)

### Platform-Specific Considerations

**Windows**:
- Use `pathlib` for all path operations
- Handle case-insensitive file systems appropriately
- Test with both PowerShell and Command Prompt

**macOS**:
- Handle case-sensitive/insensitive file system variants
- Test with both Intel and Apple Silicon Macs
- Ensure compatibility with macOS security restrictions

**Linux**:
- Test with multiple distributions (Ubuntu, RHEL, Alpine)
- Handle different Python installation locations
- Ensure compatibility with various shell environments

## Security Considerations

### Dependency Security
- **Vulnerability scanning**: Regular checks for CVEs in dependencies
- **Supply chain security**: Verify package integrity and maintainer reputation
- **Minimal permissions**: Dependencies should not require elevated privileges
- **Audit trail**: Track when and why each dependency was added

### Version Security
- **Stay current**: Regularly update to latest patch versions
- **Security patches**: Prioritize security updates over feature updates
- **EOL tracking**: Monitor end-of-life dates for all dependencies
- **Fallback plans**: Maintain alternatives for critical dependencies

## Performance Characteristics

### Expected Performance Profiles

**Memory Usage**:
- Base system: <100MB
- Per 1K files: +50MB
- Large codebases (10K files): <2GB total

**Processing Speed**:
- Small files (<100 lines): <10ms each
- Medium files (100-1000 lines): <100ms each  
- Large files (1000+ lines): <1s each
- Full sync (1K files): <30s

**Storage Requirements**:
- System Map database: ~1MB per 1K files
- JSON Mirrors: ~2x source code size
- Blueprint cache: ~10MB per 100 blueprints
- Total overhead: ~3-5x source code size

### Performance Monitoring

Track these metrics in production:
- Parse time per file by language and size
- Memory usage during large codebase processing
- Database query performance for common operations
- Blueprint generation time by type and complexity
- Cache hit rates for frequently accessed data