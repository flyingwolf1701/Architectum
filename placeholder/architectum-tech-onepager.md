status: approved
# Architectum Technical One-Pager

## System Pillars

### 1. Structure Extraction

Architectum extracts code structure into XML components through language-specific parsers:
- **Python**: Uses native AST module for accurate parsing
- **TypeScript**: Leverages TypeScript Compiler API
- **Kotlin**: Currently uses regex-based extraction (planned for enhancement)
- **Flutter/Dart**: Currently uses regex-based extraction (planned for enhancement)

Each extractor captures functions, types, and their relationships while deliberately omitting implementation details. The system will be enhanced to extract documentation comments and more detailed type information.

### 2. Index Management

The XML indexing system provides selective focus on relevant parts of the codebase:
- Generates focused XML indexes based on configuration in `plan.yaml`
- Combines component XMLs using `build_xml_indexes.py`
- Tracks architectural evolution through XML diffing via `arch_diff_index.py`
- Controls which portions of the codebase are loaded via the `xml_focus` field

### 3. Relationship Mapping

Architectum maps relationships between code components:
- Function calls across component boundaries
- Type dependencies and inheritance relationships
- Module dependencies and imports
- API surface areas and entry points

Relationship mapping will be enhanced to provide more detailed dependency graphs and data flow visualization.

## Technical Stack

### Current Implementation

- **Python**: Primary language for CLI tools and orchestration
- **TypeScript/JavaScript**: Used for TypeScript extraction
- **XML**: Core representation format for code structure
- **YAML**: Configuration format for plans and settings

### Planned Extensions

- **LSP Integration**: Connect to Language Server Protocol for more accurate parsing
- **React/TypeScript**: Web-based visualization layer
- **Graph Database** (optional): For complex relationship queries
- **Language-specific Parsers**: Enhanced extraction for all supported languages

## Pipeline Architecture

```
Source Code → Language Extractors → Component XMLs → XML Indexes → Visualization/Analysis
```

1. `arch_extract.py` serves as the CLI entry point
2. Language-specific extractors process source files
3. Individual component XMLs are generated (one per file)
4. `build_xml_indexes.py` combines components into focused indexes
5. XML indexes are used for AI context and visualization

## Engineering Principles

- **Black Box Testability**: Components must be verifiable through their XML representations
- **Explicit Structure Over Inferred Behavior**: Prioritize clear structural mapping over clever extraction
- **Modular, Component-Aligned Mapping**: Maintain clear boundaries between components
- **Composable, Declarative File Formats**: XML and YAML for maximum interoperability
- **Visualizable Architecture**: All relationships should be representable visually
- **Maintainability Over Cleverness**: Favor straightforward approaches that can evolve with the codebase

## Implementation Details

### XML Schema Design

The XML format follows industry-standard practices for code representation with a hierarchical structure:

#### Current Schema
```xml
<Module name="module_name" namespace="namespace">
  <Component name="component_name" type="class|interface|enum|function" path="file_path">
    <Documentation>Component documentation text</Documentation>
    
    <Method name="method_name" visibility="public|private|protected" static="true|false">
      <Documentation>Method documentation</Documentation>
      <Parameter name="param_name" type="param_type" optional="true|false" />
      <Returns type="return_type" nullable="true|false" />
      <Throws type="exception_type" condition="condition_description" />
      <Dependencies>
        <Calls target="fully.qualified.method.name" />
        <Uses type="fully.qualified.type.name" />
        <Imports module="module_name" />
      </Dependencies>
    </Method>
    
    <Field name="field_name" type="field_type" visibility="public|private|protected" static="true|false">
      <Documentation>Field documentation</Documentation>
    </Field>
    
    <Relationship type="inherits|implements|extends|composes|uses" target="fully.qualified.name" />
  </Component>
</Module>
```

#### Enhanced Schema (Planned)
```xml
<Module name="module_name" namespace="namespace">
  <Metadata>
    <ApiSurface version="1.0" />
    <LastModified date="2025-05-14T10:30:00Z" />
  </Metadata>
  
  <Dependencies>
    <Import module="external_module" version="^2.0.0" />
    <Import module="internal_module" path="../relative/path" />
    <Export name="ExportedComponent" />
  </Dependencies>
  
  <Component name="component_name" type="class" path="file_path" isPublicApi="true">
    <Documentation>Component documentation text</Documentation>
    
    <!-- Generic Type Support -->
    <TypeParameters>
      <TypeParameter name="T" constraint="Comparable<T>" />
      <TypeParameter name="R" constraint="Record" />
    </TypeParameters>
    
    <!-- Type Hierarchies -->
    <Relationships>
      <Relationship type="extends" target="BaseClass<T>" />
      <Relationship type="implements" target="Serializable" />
      <Relationship type="implements" target="Comparable<T>" />
    </Relationships>
    
    <!-- Contract Verification -->
    <Contracts>
      <InterfaceImplementation interface="Comparable<T>" status="complete" />
      <InterfaceImplementation interface="Serializable" status="partial">
        <MissingMethod name="writeObject" />
      </InterfaceImplementation>
    </Contracts>
    
    <Method name="process" visibility="public" static="false">
      <Documentation>Processes input data and returns transformed results</Documentation>
      <TypeParameters>
        <TypeParameter name="V" constraint="Object" />
      </TypeParameters>
      
      <Parameters>
        <Parameter name="input" type="List<V>" optional="false" />
        <Parameter name="options" type="ProcessOptions" optional="true" />
      </Parameters>
      
      <Returns type="Map<String, T>" nullable="false" />
      
      <Throws type="ProcessException" condition="when input is invalid" />
      
      <!-- Data Flow -->
      <DataFlow>
        <ParameterFlow param="input" target="transformer.transform" paramPosition="0" />
        <ReturnValueFlow source="mapper.createMap" target="return" />
      </DataFlow>
      
      <!-- Dependency Direction -->
      <Dependencies>
        <Calls target="transformer.transform" direction="outgoing" />
        <Calls target="mapper.createMap" direction="outgoing" />
        <CalledBy source="ApiController.processRequest" direction="incoming" />
      </Dependencies>
    </Method>
    
    <Field name="transformer" type="Transformer<T, V>" visibility="private" static="false">
      <Documentation>Handles data transformation logic</Documentation>
    </Field>
    
    <Field name="mapper" type="DataMapper" visibility="private" static="false">
      <Documentation>Maps processed data to output format</Documentation>
    </Field>
  </Component>
</Module>
```

The enhanced schema provides:

- **Generic Type Support**: `<TypeParameters>` section with constraints
- **Dependency Direction**: `direction` attribute on `<Calls>` and `<CalledBy>` elements
- **Data Flow**: `<DataFlow>` tracks how data moves between methods
- **Type Hierarchies**: `<Relationships>` captures inheritance and implementation
- **Module Dependencies**: `<Dependencies>` at module level tracks imports/exports
- **API Surface**: `isPublicApi` attribute marks public API components
- **Contract Verification**: `<Contracts>` tracks interface implementation status

### Execution Flow

The system follows a plan-driven workflow:
1. User defines development phases in `plan.yaml`
2. Current phase sets `xml_focus` to control loaded context
3. Extractors generate/update component XMLs
4. XML indexes are built to provide focused views
5. AI assistance or visualization works with these focused views

---

_"Structure first, implementation second. Architectum equips systems for intelligent conversation."_
