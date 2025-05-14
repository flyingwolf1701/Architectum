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

The XML format follows a hierarchical structure:
- `<Application>` - Top-level container
  - `<Component>` - Individual module or file
    - `<Function>` - Method or function
      - `<Description>` - Documentation
      - `<Returns>` - Return type information
      - `<Calls>` - Outgoing function calls
      - `<CalledBy>` - Incoming references
    - `<Type>` - Class or data structure
      - `<Property>` - Field or property

Future enhancements will add:
- Parameter type information
- Generic type constraints
- Documentation extraction
- More detailed relationship mapping

### Execution Flow

The system follows a plan-driven workflow:
1. User defines development phases in `plan.yaml`
2. Current phase sets `xml_focus` to control loaded context
3. Extractors generate/update component XMLs
4. XML indexes are built to provide focused views
5. AI assistance or visualization works with these focused views

---

_"Structure first, implementation second. Architectum equips systems for intelligent conversation."_