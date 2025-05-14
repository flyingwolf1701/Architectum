# Architectum Multi-Level Indexing Configuration

The multi-level indexing system in Architectum is controlled through a flexible configuration approach that allows users to precisely define what components are indexed and at what level of detail.

## Configuration File: `architectum.yaml`

```yaml
# Architectum Configuration
project:
  name: "MyApplication"
  root: "."
  description: "Multi-tiered application with frontend and backend components"

# Language-specific settings
languages:
  typescript:
    enabled: true
    extensions: [".ts", ".tsx"]
    exclude_patterns: ["**/*.test.ts", "**/node_modules/**"]
  
  python:
    enabled: true
    extensions: [".py"]
    exclude_patterns: ["**/venv/**", "**/tests/**"]
  
  react:
    enabled: true
    extensions: [".jsx", ".tsx"]
    parser_options:
      track_props: true
      track_hooks: true
      track_context: true
      track_hoc: true  # Higher-Order Components
  
  vue:
    enabled: true
    extensions: [".vue"]
    parser_options:
      track_props: true
      track_events: true
      track_slots: true

# Index definitions
indexes:
  # System-wide overview index
  system:
    name: "system_index"
    include: ["**/*"]
    detail_level: "minimal"    # Only component names and public APIs
    relationship_depth: 1      # Only direct relationships
    output: "structure/indexes/system_index.xml"
  
  # Frontend module index
  frontend:
    name: "frontend_index"
    include: ["src/ui/**/*"]   # This includes src/ui/ and all subdirectories/files
    detail_level: "standard"   # Include all public methods and properties
    relationship_depth: 2      # Include relationships up to 2 levels deep
    output: "structure/indexes/frontend_index.xml"
    
  # Backend module index
  backend:
    name: "backend_index"
    include: ["src/api/**/*", "src/services/**/*", "src/db/**/*"]
    detail_level: "standard"
    relationship_depth: 2
    output: "structure/indexes/backend_index.xml"
    
  # User management module index
  user_module:
    name: "user_module_index"
    include: ["src/users/**/*", "src/auth/**/*"]  # Includes both directories and their children
    detail_level: "detailed"   # Include all methods, properties, and parameters
    relationship_depth: 3      # Deep relationship tracking
    output: "structure/indexes/user_module_index.xml"
  
  # Active development focus index
  active_development:
    name: "active_index"
    # Component names are resolved from the include paths
    # You can provide fully qualified names like "src/users/UserProfile.vue"
    # or let the system find components by name across the codebase
    include_components: ["UserProfile", "AuthService"]  # Specific components
    include_from_plan: true    # Pull components from current plan phase
    detail_level: "full"       # Maximum detail
    relationship_depth: "full" # All relationships
    output: "structure/indexes/active_index.xml"
    
  # Method-focused index
  method_focus:
    name: "method_focus_index"
    component_methods: [
      "UserProfile.updateUserDetails",
      "AuthService.validateToken",
      "PaymentProcessor.processPayment"
    ]
    # This creates an index with just these specific methods
    # and their immediate relationships
    detail_level: "full"
    output: "structure/indexes/method_focus_index.xml"
    
  # File structure mirror index (creates detailed XMLs matching file structure)
  file_mirror:
    name: "file_mirror"
    include: ["src/**/*"]
    output_mode: "file_mirror"  # Creates one XML per source file
    output_dir: "structure/detailed"
    detail_level: "detailed"
    # This will create a directory structure in structure/detailed
    # that mirrors your source code structure, with one XML per file

# Detail level definitions
detail_levels:
  minimal:
    include_private: false
    include_parameters: false
    include_documentation: false
    include_types: false
    
  standard:
    include_private: false
    include_parameters: true
    include_documentation: true
    include_types: true
    
  detailed:
    include_private: true
    include_parameters: true
    include_documentation: true
    include_types: true
    include_parameter_metadata: true
    
  full:
    include_private: true
    include_parameters: true
    include_documentation: true
    include_types: true
    include_parameter_metadata: true
    include_dataflow: true
    include_contracts: true
    
  # Component-focused level (for focused work on specific components)
  component_focused:
    include_private: true
    include_parameters: true
    include_documentation: true
    include_types: true
    include_parameter_metadata: true
    include_props: true         # Component props/inputs
    include_events: true        # Component events/outputs
    include_state: true         # Component state management
    include_lifecycle: true     # Component lifecycle methods
    track_prop_flow: true       # Track where props are used
    
  # Method-focused level (for focused work on specific methods)
  method_focused:
    include_method_body: false  # No implementation details
    include_parameters: true
    include_parameter_usage: true  # Track how parameters are used
    include_dataflow: true      # Track data flow through method
    include_calls: true         # Methods called by this method
    include_callers: true       # Methods that call this method
    
# Visualization settings
visualization:
  enabled: true
  output_dir: "structure/viz"
  formats: ["d3", "mermaid", "dot"]
  views:
    - name: "component_dependencies"
      type: "dependency_graph"
      root_components: ["App", "MainController"]
      max_depth: 3
    
    - name: "service_layer"
      type: "layer_diagram"
      include: ["src/services/**/*"]
      group_by: "package"

# Integration settings
integrations:
  vscode:
    enabled: true
    extension_path: "./vscode-extension"
    
  ci:
    enabled: true
    generate_on_commit: true
    store_history: true
    diff_with_previous: true
```

## Key Configuration Features

### 1. Path-Based Indexing

```yaml
frontend:
  include: ["src/ui/**/*"]
  detail_level: "standard"
```

This approach allows indexing entire directories or specific files using glob patterns. The pattern `src/ui/**/*` includes the `src/ui` directory and all its children (subdirectories and files), essentially creating an index of the entire frontend.

### 2. Component-Based Indexing

```yaml
active_development:
  include_components: ["UserProfile", "AuthService"]
```

Target specific named components by name. Architectum resolves these names to actual files by:
1. Looking for exact file matches (e.g., UserProfile.vue)
2. Searching for component definitions within files
3. Using a component registry that maps names to file paths

You can also use fully qualified paths (e.g., "src/users/UserProfile.vue") for explicit mapping.

### 3. Method-Focused Indexing

```yaml
method_focus:
  component_methods: ["UserProfile.updateUserDetails", "AuthService.validateToken"]
```

Focus on specific methods across multiple components, creating a targeted index of just those methods and their relationships, perfect for focused development tasks.

### 4. File Structure Mirroring

```yaml
file_mirror:
  include: ["src/**/*"]
  output_mode: "file_mirror"
  output_dir: "structure/detailed"
```

Creates a directory structure in `structure/detailed` that mirrors your source code structure, with one detailed XML file per source file. This preserves the original organization while providing structured XML representations.

### 5. Plan-Driven Indexing

```yaml
active_development:
  include_from_plan: true
```

Automatically include components being worked on in the current phase of the development plan, providing dynamic context based on active development.

### 4. Detail Level Control

```yaml
detail_levels:
  minimal:
    include_private: false
    include_parameters: false
  
  full:
    include_private: true
    include_parameters: true
    include_dataflow: true
```

Define multiple detail levels from minimal (component names and public APIs only) to full (complete structural information), and apply them selectively to different indexes.

### 5. Relationship Depth Control

```yaml
relationship_depth: 2  # Include relationships up to 2 levels deep
```

Control how far to trace relationships between components, from direct dependencies only (depth 1) to full transitive closure of the entire system.

## Command Line Interface

```bash
# Generate all defined indexes
architectum index

# Generate a specific index
architectum index --name frontend

# Generate an ad-hoc index from components
architectum index --components UserProfile,AuthService --detail full

# Generate an index focused on active files in your IDE
architectum index --from-editor --editor vscode

# Generate visualization for a specific index
architectum visualize --index frontend --format d3
```

## IDE Integration

The configuration can be supplemented with editor-driven indexing, where the current file or selection in the IDE determines what gets indexed:

```javascript
// VS Code Extension pseudocode
function createFocusedIndex() {
  const activeEditor = vscode.window.activeTextEditor;
  if (!activeEditor) return;
  
  const activeFile = activeEditor.document.uri.fsPath;
  const selection = activeEditor.selection;
  
  // Extract component name under cursor
  const componentName = getComponentAtPosition(activeFile, selection);
  
  // Create focused index on this component
  execCommand(`architectum index --components ${componentName} --detail full`);
}
```

## Benefits of This Approach

1. **Precision**: Target exactly what you need, from entire modules to specific components
2. **Flexibility**: Multiple indexes for different purposes (overview, focused development)
3. **Integration**: Connect to development workflow via plan.yaml or editor integration
4. **Efficiency**: Generate only what you need at the detail level you need
5. **Contextual**: Dynamic indexes that follow your development focus

## Applying to a Vue 3 Frontend

For a large Vue 3 frontend, this configuration allows you to:

1. Create a high-level "bird's eye view" of the entire frontend
2. Generate detailed indexes of specific feature modules
3. Focus on active components during development
4. Track prop and event relationships between components

Example Vue-specific configuration:

```yaml
indexes:
  vue_components:
    name: "vue_components_index"
    include: ["src/components/**/*.vue"]
    detail_level: "vue_components"
    relationship_types: ["props", "events", "slots"]
    output: "structure/indexes/vue_components_index.xml"

detail_levels:
  vue_components:
    include_private: false
    include_props: true
    include_events: true
    include_slots: true
    include_store_usage: true
    trace_prop_flow: true  # Track props from provider to consumer
    trace_event_flow: true # Track events from emitter to handler
```

Example React-specific configuration:

```yaml
indexes:
  react_components:
    name: "react_components_index"
    include: ["src/components/**/*.tsx", "src/components/**/*.jsx"]
    detail_level: "react_components"
    relationship_types: ["props", "context", "hooks", "hoc"]
    output: "structure/indexes/react_components_index.xml"

detail_levels:
  react_components:
    include_private: false
    include_props: true
    include_hooks: true
    include_context: true
    include_memo_deps: true  # Track dependencies for useMemo/useCallback
    include_effect_deps: true  # Track dependencies for useEffect
    trace_prop_drilling: true  # Track props passed through component hierarchies
    track_context_usage: true  # Track Context.Provider and useContext patterns
```

## Implementation Notes

The multi-level indexing system requires:

1. A configuration parser for the YAML format
2. Index generators that respect the detail level and relationship depth settings
3. Component resolvers that can find components by name across files
4. Relationship trackers that can follow dependencies to the specified depth
5. Output formatters for the XML structure

With this flexible configuration approach, Architectum can adapt to codebases of any size and complexity, from small projects to enterprise systems.
