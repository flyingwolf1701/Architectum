# LSP Integration for Architectum

## Architecture Overview

```
┌─────────────────┐     ┌───────────────────┐     ┌────────────────┐
│                 │     │                   │     │                │
│ Language Server │◄────┤ Architectum LSP   │─────┤ XML Generator │
│ (TS/Python/etc) │     │ Bridge            │     │                │
│                 │     │                   │     │                │
└─────────────────┘     └───────────────────┘     └────────────────┘
                               │                          │
                               │                          │
                               ▼                          ▼
                        ┌──────────────┐          ┌──────────────────┐
                        │              │          │                  │
                        │ Relationship │          │ Component        │
                        │ Analyzer     │          │ XML Files        │
                        │              │          │                  │
                        └──────────────┘          └──────────────────┘
                               │                          │
                               │                          │
                               └──────────────┬───────────┘
                                              │
                                              ▼
                                      ┌───────────────┐
                                      │               │
                                      │ Visualization │
                                      │ Engine        │
                                      │               │
                                      └───────────────┘
```

## Key Components

### 1. Architectum LSP Bridge

A lightweight adapter that:
- Initializes connections to appropriate language servers
- Translates LSP protocol into internal data structures
- Manages document synchronization and queries
- Handles multi-language projects

```typescript
// Example bridge implementation
class ArchitectumLSPBridge {
  private languageServers: Map<string, LanguageServer>;
  
  constructor() {
    this.languageServers = new Map();
  }
  
  async initialize(workspacePath: string): Promise<void> {
    // Detect languages in workspace
    const languages = await detectLanguages(workspacePath);
    
    // Initialize appropriate servers
    for (const lang of languages) {
      this.languageServers.set(lang, await startLanguageServer(lang));
    }
  }
  
  async getSymbol(uri: string, position: Position): Promise<Symbol> {
    const language = detectLanguageFromUri(uri);
    const server = this.languageServers.get(language);
    return await server.getSymbolAt(uri, position);
  }
  
  async getReferences(uri: string, position: Position): Promise<Reference[]> {
    const language = detectLanguageFromUri(uri);
    const server = this.languageServers.get(language);
    return await server.findReferences(uri, position);
  }
  
  // Additional methods for type information, inheritance, etc.
}
```

### 2. XML Generator

Converts LSP data into our XML schema:
- Maps LSP symbol kinds to XML component types
- Extracts signatures and type information
- Builds relationships from reference data
- Handles framework-specific patterns (Vue, React, etc.)

```typescript
class XMLGenerator {
  private bridge: ArchitectumLSPBridge;
  
  constructor(bridge: ArchitectumLSPBridge) {
    this.bridge = bridge;
  }
  
  async generateComponentXML(uri: string): Promise<string> {
    // Get document symbols
    const symbols = await this.bridge.getDocumentSymbols(uri);
    
    // Create root component
    const component = createComponentElement(symbols.mainSymbol);
    
    // Add methods and properties
    for (const childSymbol of symbols.children) {
      if (childSymbol.kind === SymbolKind.Method) {
        const method = await this.createMethodElement(childSymbol, uri);
        component.appendChild(method);
      } else if (childSymbol.kind === SymbolKind.Property) {
        const property = this.createPropertyElement(childSymbol);
        component.appendChild(property);
      }
    }
    
    // Add relationships
    await this.addRelationships(component, symbols.mainSymbol, uri);
    
    return serializeToXML(component);
  }
  
  // Methods for creating XML elements for different symbol types
}
```

### 3. Relationship Analyzer

Specialized component that:
- Builds a graph of all references between entities
- Computes transitive relationships
- Identifies architectural patterns
- Detects framework-specific relationships (props, events)

```typescript
class RelationshipAnalyzer {
  private bridge: ArchitectumLSPBridge;
  private relationshipGraph: Graph;
  
  constructor(bridge: ArchitectumLSPBridge) {
    this.bridge = bridge;
    this.relationshipGraph = new Graph();
  }
  
  async analyzeWorkspace(workspacePath: string): Promise<void> {
    // Get all symbols in workspace
    const symbols = await this.bridge.getAllWorkspaceSymbols(workspacePath);
    
    // Build initial nodes
    for (const symbol of symbols) {
      this.relationshipGraph.addNode(symbol.uri, symbol);
    }
    
    // Build edges (relationships)
    for (const symbol of symbols) {
      const references = await this.bridge.getReferences(symbol.uri, symbol.position);
      for (const ref of references) {
        this.relationshipGraph.addEdge(symbol.uri, ref.uri, {
          type: determineRelationshipType(symbol, ref),
          direction: determineDirection(symbol, ref)
        });
      }
    }
    
    // Analyze for framework-specific patterns
    await this.detectFrameworkPatterns();
  }
  
  // Methods for analyzing relationship types and patterns
}
```

### 4. Visualization Engine

Renders the structure for exploration:
- Interactive component graph
- Dependency visualization
- Architecture diagrams
- Drill-down capabilities

```typescript
class VisualizationEngine {
  private relationshipGraph: Graph;
  private components: Map<string, ComponentData>;
  
  constructor(relationshipGraph: Graph, components: Map<string, ComponentData>) {
    this.relationshipGraph = relationshipGraph;
    this.components = components;
  }
  
  generateDependencyGraph(options: GraphOptions): VisualGraph {
    const graph = new VisualGraph();
    
    // Filter nodes based on options
    const nodes = this.filterNodes(options);
    
    // Add nodes
    for (const node of nodes) {
      graph.addNode(this.createVisualNode(node));
    }
    
    // Add edges
    for (const node of nodes) {
      const edges = this.relationshipGraph.getEdges(node.id);
      for (const edge of edges) {
        if (nodes.has(edge.target)) {
          graph.addEdge(this.createVisualEdge(edge));
        }
      }
    }
    
    return graph;
  }
  
  // Methods for different visualization types
}
```

## Framework-Specific LSP Extensions

For Vue.js, React, Angular, and other frameworks:

```typescript
class VueLSPExtension {
  private bridge: ArchitectumLSPBridge;
  
  constructor(bridge: ArchitectumLSPBridge) {
    this.bridge = bridge;
  }
  
  async enhanceComponent(uri: string, component: XMLElement): Promise<void> {
    // Parse SFC to find template, script, style sections
    const sfcContent = await this.bridge.getDocumentContent(uri);
    const sections = parseSFC(sfcContent);
    
    // Extract props
    const props = await this.extractProps(sections.script);
    for (const prop of props) {
      component.appendChild(this.createPropElement(prop));
    }
    
    // Extract emitted events
    const events = await this.extractEvents(sections.script, sections.template);
    for (const event of events) {
      component.appendChild(this.createEventElement(event));
    }
    
    // Find child components
    const children = await this.findChildComponents(sections.template);
    for (const child of children) {
      component.appendChild(this.createChildElement(child));
    }
  }
  
  // Methods for Vue-specific patterns and relationships
}
```

## Implementation Phases

1. **Basic LSP Integration**
   - Connect to language servers
   - Extract basic symbol information
   - Generate simple component XMLs

2. **Relationship Mapping**
   - Build reference graph
   - Compute dependencies
   - Link components

3. **Framework Support**
   - Add Vue/React/Angular extensions
   - Extract framework-specific patterns
   - Handle template languages

4. **Advanced Visualization**
   - Interactive exploration
   - Architectural views
   - Change tracking
