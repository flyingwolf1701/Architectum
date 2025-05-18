# Architectum Testing Strategy

## Introduction

This document outlines the testing strategy for Architectum, a graph-based code comprehension system. The testing approach reflects Architectum's core principles: accuracy, reliability, and a relationship-centric view of code. As Architectum itself is designed to reveal the true structure of codebases, its testing strategy must similarly ensure that the system accurately represents and navigates complex code relationships.

## Testing Philosophy

Our testing philosophy for Architectum is guided by these principles:

1. **Graph Model Integrity**: Ensure the accuracy of the fundamental graph structure that represents code relationships
2. **Contract Reliability**: Verify that blueprint outputs maintain consistent interfaces for AI agents and visualization tools
3. **Performance Awareness**: Test for both correctness and reasonable performance with varying codebase sizes
4. **Cross-Language Consistency**: Maintain uniform behavior across supported programming languages
5. **Snapshot Verification**: Use reference outputs to detect unexpected changes in blueprint structure

## Testing Frameworks and Tools

### Core Testing Stack

- **pytest**: Primary testing framework for unit and integration tests
  - pytest-cov: For measuring code coverage
  - pytest-benchmark: For performance testing critical operations
  - pytest-snapshot: For output verification against reference blueprints

- **hypothesis**: Property-based testing for complex graph operations
  - Used to verify graph model consistency across random inputs and edge cases
  - Particularly valuable for testing traversal and relationship operations

- **pact**: Contract testing for blueprint outputs
  - Ensures consistent JSON/XML schema for consumers
  - Maintains backward compatibility as formats evolve

### Additional Tools

- **mock**: For isolating components and simulating file systems
- **tox**: For testing across different Python versions
- **mypy**: For static type checking (preventative testing)

## Types of Tests

### 1. Unit Tests

- **Scope**: Individual functions, classes, and methods
- **Framework**: pytest
- **Coverage Target**: 80% minimum code coverage
- **Implementation**: Test isolated components with appropriate mocking

### 2. Integration Tests

- **Scope**: Interactions between components (e.g., parser to graph model)
- **Framework**: pytest with appropriate fixtures
- **Coverage**: Critical component interactions
- **Implementation**: Test interaction points between major subsystems

### 3. Contract Tests

- **Scope**: Blueprint output schemas and formats
- **Framework**: pact
- **Coverage**: All blueprint types and detail levels
- **Implementation**: Define consumer contracts and verify output conformance

### 4. Property-Based Tests

- **Scope**: Graph model operations and data transformations
- **Framework**: hypothesis
- **Coverage**: Core graph functionality and relationship mapping
- **Implementation**: Define property invariants that must hold true across random inputs

### 5. Snapshot Tests

- **Scope**: Blueprint outputs for reference cases
- **Framework**: pytest-snapshot
- **Coverage**: Representative examples of each blueprint type
- **Implementation**: Create reference outputs and automatically compare with generated blueprints

## Test Coverage Requirements

### Overall Coverage Target

- **Minimum Code Coverage**: 80% line coverage across the codebase
- **Critical Component Coverage**: 90% coverage for core graph model and blueprint generators
- **Edge Case Coverage**: Explicit tests for error conditions and boundary cases

### Component-Specific Coverage

| Component | Minimum Coverage | Key Testing Focus |
|-----------|-----------------|-------------------|
| Graph Model | 90% | Node/relationship integrity, traversal operations |
| Blueprint Generators | 85% | Correct graph construction, detail level implementation |
| Parsers | 85% | Accurate extraction of code elements and relationships |
| CLI/API | 80% | Parameter validation, output formatting |
| Caching/Incremental Update | 85% | Change detection, partial regeneration |

## Testing Strategy by Component

### 1. Graph Model Testing

- **Unit Testing**: Test each node and relationship type, graph operations, serialization/deserialization
- **Property Testing**: Use hypothesis to verify graph properties across random structures
- **Examples**:
  ```python
  @given(st.lists(st.tuples(st.text(), st.text(), st.text())))
  def test_graph_relationships_consistency(self, relationships):
      # Create graph with random relationships
      # Verify relationship integrity is maintained
  ```

### 2. Directory Blueprint Testing

- **Unit Testing**: Test directory traversal, file detection, graph node creation
- **Integration Testing**: Test complete blueprint generation for test directories
- **Snapshot Testing**: Compare outputs with reference blueprints for known directory structures
- **Contract Testing**: Verify JSON output matches schema contract
- **Examples**:
  ```python
  def test_directory_traversal_depth(self):
      # Test with various depth parameters
      
  def test_directory_blueprint_minimal_detail(snapshot):
      # Generate blueprint and compare with snapshot
  ```

### 3. File Set Blueprint Testing

- **Unit Testing**: Test file path validation, multi-file handling
- **Integration Testing**: Test cross-file relationship detection
- **Contract Testing**: Verify output schema consistency
- **Examples**:
  ```python
  def test_fileset_with_invalid_paths():
      # Verify proper error handling
      
  def test_cross_file_relationship_detection():
      # Verify detection of imports, function calls across files
  ```

### 4. Code Element Blueprint Testing

- **Unit Testing**: Test element selection and extraction
- **Snapshot Testing**: Verify focused blueprint outputs match references
- **Examples**:
  ```python
  def test_function_selection_in_blueprint():
      # Test extraction of specific functions
      
  def test_relationship_mapping_for_elements():
      # Verify related elements are included
  ```

### 5. Parser Testing

- **Unit Testing**: Test parsing accuracy for different language constructs
- **Property Testing**: Test parsing robustness with hypothesis
- **Examples**:
  ```python
  @pytest.mark.parametrize("code_snippet,expected_elements", [
      # Various language constructs
  ])
  def test_parser_element_extraction(code_snippet, expected_elements):
      # Verify elements are correctly extracted
  ```

### 6. CLI/API Testing

- **Unit Testing**: Test parameter validation, command registration
- **Integration Testing**: Test end-to-end functionality
- **Examples**:
  ```python
  def test_cli_parameter_validation():
      # Test handling of valid and invalid parameters
      
  def test_api_endpoint_response():
      # Test API response format and status codes
  ```

## Snapshot Testing Strategy

Snapshot testing is particularly valuable for Architectum's blueprint outputs. This approach captures the expected structure of blueprint outputs and detects any unintended changes.

### Implementation

1. **Reference Cases**: Create representative test cases for each blueprint type and detail level
2. **Initial Snapshot Creation**: Generate and save reference outputs for each case
3. **Automated Comparison**: During testing, compare generated outputs with snapshots
4. **Visualization**: When differences are detected, display clear difference information
5. **Update Process**: Include a documented process for updating snapshots when changes are intentional

### Example Snapshot Test

```python
def test_directory_blueprint_detailed_output(snapshot):
    # Setup test directory structure
    blueprint = generate_directory_blueprint('test_dir', detail_level='detailed')
    
    # Compare with stored snapshot
    snapshot.assert_match(blueprint.to_json(), 'directory_detailed.json')
```

## Contract Testing Strategy

Contract testing ensures that blueprint outputs maintain a consistent structure that consumers can rely on.

### Implementation

1. **Consumer Contracts**: Define expected schema for each blueprint type
2. **Provider Verification**: Verify that generated blueprints match the contract
3. **Evolution Strategy**: Clear process for evolving contracts while maintaining compatibility

### Example Contract Test

```python
def test_directory_blueprint_contract():
    # Generate blueprint
    blueprint = generate_directory_blueprint('test_dir')
    
    # Verify against contract
    pact.verify(blueprint.to_json(), 'directory_blueprint_contract')
```

## Test Organization

### Directory Structure

```
tests/
  unit/              # Unit tests mirroring source structure
    graph/           # Tests for graph model
    blueprints/      # Tests for blueprint generators
    parsers/         # Tests for language parsers
    cli/             # Tests for CLI interface
  integration/       # Integration tests
  contracts/         # Contract definitions and tests
  snapshots/         # Snapshot reference files
  fixtures/          # Test fixtures (sample code, directories)
```

### Naming Conventions

- Test files: `test_<module_name>.py`
- Test functions: `test_<functionality>_<scenario>.py`
- Snapshot files: `<blueprint_type>_<detail_level>_<scenario>.json`

## Test Automation and CI/CD Integration

### Automated Test Execution

- Run unit and integration tests on every commit
- Run contract and snapshot tests on pull requests
- Run performance tests on scheduled basis

### CI/CD Pipeline Integration

```yaml
# Example CI/CD configuration
stages:
  - lint
  - test
  - integration
  - contract_testing
  - snapshot_testing
  - performance_testing

unit_tests:
  stage: test
  script:
    - pytest tests/unit --cov=arch_blueprint_generator

integration_tests:
  stage: integration
  script:
    - pytest tests/integration

contract_tests:
  stage: contract_testing
  script:
    - pytest tests/contracts

snapshot_tests:
  stage: snapshot_testing
  script:
    - pytest tests/snapshots

performance_tests:
  stage: performance_testing
  script:
    - pytest tests/performance --benchmark-only
  only:
    - scheduled_jobs
```

## Guidelines for Writing Effective Tests

### General Guidelines

1. **Test One Thing**: Each test should verify one specific piece of functionality
2. **Descriptive Names**: Test names should clearly describe what is being tested
3. **Arrange-Act-Assert**: Structure tests with clear setup, action, and verification
4. **Independence**: Tests should not depend on the order of execution
5. **Repeatability**: Tests should produce the same result when run multiple times
6. **Speed**: Tests should run quickly (use appropriate mocking)

### Graph Model Testing Guidelines

1. **Test Isolated Components**: Test nodes and relationships independently before testing together
2. **Verify Consistency**: Ensure relationship integrity is maintained across operations
3. **Test Traversal**: Verify graph traversal from different starting points

### Blueprint Testing Guidelines

1. **Test Blueprint Structure**: Verify correct node and relationship creation
2. **Test Detail Levels**: Verify appropriate information is included at each detail level
3. **Test Error Cases**: Verify proper handling of invalid inputs
4. **Test Large Inputs**: Verify performance with larger codebases

## Test Data Management

### Test Fixtures

- Create representative sample codebases for different languages
- Provide fixtures for different architectural patterns (layered, microservices, etc.)
- Include fixtures with known relationships for verification

### Mock Language Servers

- Create mock LSP responses for testing without actual language servers
- Simulate various LSP responses including errors

## Conclusion

This testing strategy provides a comprehensive approach for ensuring Architectum's quality and reliability. By focusing on the graph-based nature of the system, we can ensure that code relationships are accurately captured and represented in the generated blueprints. The combination of contract testing, snapshot testing, and property-based testing provides a robust verification framework for this critical tool.

---

## Change Log

| Change        | Date       | Version | Description                  | Author         |
| ------------- | ---------- | ------- | ---------------------------- | -------------- |
| Initial draft | 05-17-2025 | 0.1     | Initial testing strategy     | Technical Scrum Master |