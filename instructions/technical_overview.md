# Architectum Technical Overview
status: in progress

## System Pillars

### 1. LSP-Powered Extraction

Architectum uses Language Server Protocol (LSP) to accurately extract code structure:
- **TypeScript**: Connects to TypeScript Language Server
- **Python**: Integrates with Pyright
- **Vue.js**: Uses Volar for Vue SFC analysis
- **React**: Leverages TypeScript/JavaScript language servers
- **Other Languages**: Connects to appropriate LSP providers

The LSP bridge provides IDE-grade accuracy for symbols, types, and relationships while abstracting away language-specific parsing complexities.

### 2. JSON Structure Design

Architectum preserves LSP's native JSON format, optimized for token efficiency:

```json
{
  "component": {
    "name": "UserProfile",
    "type": "class",
    "path": "src/components/UserProfile.js",
    "methods": [
      {
        "name": "fetchUserData",
        "visibility": "public",
        "parameters": [
          {"name": "userId", "type": "string"}
        ],
        "returns": {"type": "Promise<UserData>"},
        "dependencies": {
          "calls": ["apiService.fetchUser"]
        }
      }
    ],
    "relationships": [
      {"type": "extends", "target": "BaseComponent"}
    ]
  }
}
```

This structure captures component architecture while deliberately omitting implementation details, maximizing token efficiency for AI context.

### 3. Multi-Level Indexing

Architectum's multi-level indexing system provides flexible, configurable views of your codebase tailored for different AI assistance scenarios. This approach allows for precise control over which parts of the code structure are loaded into the AI's context window.

#### Indexing Levels

The system supports several types of indexes, each serving a different purpose:

1. **System-Wide Index**: A high-level overview of all files and their contained symbols, providing global architectural context while minimizing token usage

```json
{
  "src/components/UserProfile.vue": {
    "symbols": {
      "UserProfile": {
        "kind": "class",
        "relationships": {
          "calls_on": [
            {"file": "src/services/UserService.js", "symbol": "UserService"},
            {"file": "src/services/AuthService.js", "symbol": "AuthService"}
          ],
          "called_by": []
        }
      },
      "formatUserData": {
        "kind": "function",
        "relationships": {
          "calls_on": [],
          "called_by": [
            {"file": "src/components/UserProfile.vue", "symbol": "UserProfile"}
          ]
        }
      }
    }
  },
  "src/services/UserService.js": {
    "symbols": {
      "UserService": {
        "kind": "class",
        "relationships": {
          "calls_on": [
            {"file": "src/api/ApiClient.js", "symbol": "ApiClient"}
          ],
          "called_by": [
            {"file": "src/components/UserProfile.vue", "symbol": "UserProfile"},
            {"file": "src/components/UserSettings.vue", "symbol": "UserSettings"}
          ]
        }
      },
      "createUserPayload": {
        "kind": "function",
        "relationships": {
          "calls_on": [],
          "called_by": [
            {"file": "src/services/UserService.js", "symbol": "UserService"}
          ]
        }
      }
    }
  }
}
```
   
2. **Module-Based Indexes**: Focused views of specific subsystems or directories, providing more detail for a targeted area of the codebase

```json
{
  "name": "auth_module_index",
  "path": "src/auth",
  "components": [
    {
      "name": "AuthService",
      "kind": "class",
      "methods": [
        {"name": "login", "kind": "method", "visibility": "public"},
        {"name": "validateToken", "kind": "method", "visibility": "public"}
      ],
      "relationships": {
        "calls_on": ["UserService", "TokenValidator"],
        "called_by": ["LoginForm", "NavigationGuard"]
      }
    },
    {
      "name": "TokenValidator",
      "kind": "class",
      "methods": [
        {"name": "validate", "kind": "method", "visibility": "public"}
      ],
      "relationships": {
        "calls_on": [],
        "called_by": ["AuthService"]
      }
    }
  ]
}
```
   
3. **Component-Focused Indexes**: Detailed representations of specific components and their immediate relationships, ideal for concentrated development tasks

```json
{
  "name": "login_focus_index",
  "components": [
    {
      "name": "LoginForm",
      "kind": "class",
      "methods": [
        {
          "name": "authenticate",
          "kind": "method",
          "parameters": [
            {"name": "username", "type": "string"},
            {"name": "password", "type": "string"}
          ],
          "returns": {"type": "Promise<boolean>"},
          "relationships": {
            "calls_on": ["AuthService.login", "this.validateForm"]
          }
        }
      ],
      "relationships": {
        "calls_on": ["AuthService"],
        "called_by": ["LoginPage"]
      }
    }
  ]
}
```
   
4. **Method-Level Indexes**: Ultra-focused views highlighting specific methods/functions across components, perfect for targeted modifications

```json
{
  "name": "payment_methods_index",
  "methods": [
    {
      "component": "PaymentForm",
      "name": "submitPayment",
      "kind": "method",
      "parameters": [
        {"name": "amount", "type": "number"},
        {"name": "cardDetails", "type": "CardDetails"}
      ],
      "relationships": {
        "calls_on": ["PaymentService.processPayment"],
        "called_by": ["CheckoutPage.completeOrder"]
      },
      "implementation_summary": "Validates input, calls payment service, shows result"
    },
    {
      "component": "PaymentService",
      "name": "processPayment",
      "kind": "method",
      "parameters": [
        {"name": "paymentData", "type": "PaymentData"}
      ],
      "returns": {"type": "Promise<PaymentResult>"},
      "relationships": {
        "calls_on": ["PaymentGateway.executeTransaction"],
        "called_by": ["PaymentForm.submitPayment"]
      }
    }
  ]
}
```

#### YAML Configuration

Indexes are defined through a clear YAML configuration:

```yaml
indexes:
  # System-wide overview index with minimal detail
  system:
    name: "system_index"
    include: ["**/*"]                 # Include all files
    exclude: ["**/tests/**", "**/node_modules/**"]
    detail_level: "minimal"           # Basic structure only
    relationship_depth: 1             # Only direct relationships
    output: "structure/system_index.json"
    
  # Module-specific index with standard detail
  auth_module:
    name: "auth_module_index"
    include: ["src/auth/**/*", "src/users/**/*"]  # Auth-related paths
    detail_level: "standard"          # Include methods and parameters
    relationship_depth: 2             # Include secondary relationships
    output: "structure/auth_module_index.json"
  
  # Component-focused index with detailed information
  login_components:
    name: "login_focus_index"
    include_components: ["LoginForm", "AuthService", "UserSession"]
    detail_level: "detailed"          # Full component details
    relationship_depth: "full"        # All relevant relationships
    output: "structure/login_focus_index.json"
    
  # Method-specific index with implementation insights
  payment_processing:
    name: "payment_methods_index"
    include_methods: [
      "PaymentForm.submitPayment", 
      "PaymentService.processPayment",
      "PaymentGateway.executeTransaction"
    ]
    detail_level: "method_focused"    # Method-specific details
    implementation_hints: true        # Include pseudocode summary
    output: "structure/payment_methods_index.json"
```

#### Detail Levels

The system supports configurable detail levels through the YAML configuration:

```yaml
detail_levels:
  minimal:
    include_private: false            # Omit private elements
    include_parameters: false         # Omit parameter details
    include_signatures: false         # Omit method signatures
    include_documentation: false      # Omit documentation blocks
    
  standard:
    include_private: false
    include_parameters: true          # Include parameter info
    include_signatures: true          # Include method signatures
    include_documentation: true       # Include key documentation
    
  detailed:
    include_private: true             # Include private elements
    include_parameters: true
    include_signatures: true
    include_documentation: true
    include_relationship_details: true # Show detailed relationships
```

#### Dynamic Focus

Architectum can also generate indexes dynamically based on the current development focus:

1. **Editor Integration**: Automatically create indexes based on the files open in your editor
2. **Git Integration**: Generate indexes for files changed in the current branch or commit
3. **Plan-Driven**: Extract indexes based on the current phase in your development plan

This multi-level indexing approach ensures the AI assistant receives precisely the right amount of context for the task at hand - comprehensive enough for meaningful assistance while optimized for token efficiency.

By controlling both the scope (which components to include) and detail level (how much information about each component), developers can dramatically improve the quality and relevance of AI assistance for different scenarios from high-level architecture discussions to targeted implementation help.

### 4. Framework-Specific Analysis

Architectum extends LSP with framework-specific knowledge:

- **Vue.js**: Analyzes SFCs to extract props, events, slots, and component relationships
- **React**: Identifies hooks, context usage, component props, and component hierarchies
- **Framework-Agnostic**: Falls back to general code structure for other frameworks

## Technical Stack

### Core Components

- **LSP Bridge**: Connects to language servers for accurate code analysis
- **JSON Generator**: Processes and organizes LSP data into standardized formats
- **Index Builder**: Creates multi-level views based on configuration
- **Visualization Engine**: Renders component relationships graphically

### Technology Choices

- **JavaScript**: For communication with LSP and visualization
- **Python**: For CLI tools and orchestration
- **Go**: Optional high-performance backend for large-scale processing
- **WebAssembly (Zig)**: Optional for performance-critical components
- **JSON**: For native LSP data representation
- **YAML**: For configuration and plan definitions

## Pipeline Architecture

```
┌─────────────────┐     ┌───────────────────┐     ┌──────────────────┐     ┌────────────────┐
│                 │     │                   │     │                  │     │                │
│ Language Server ├────►│ Architectum LSP   ├────►│ Structure Model  ├────►│ JSON Generator │
│                 │     │ Bridge            │     │                  │     │                │
└─────────────────┘     └───────────────────┘     └──────────────────┘     └────────────────┘
                                                          │                         │
                                                          │                         │
                                                          ▼                         ▼
                                                   ┌──────────────┐         ┌───────────────┐
                                                   │              │         │               │
                                                   │ Relationship │         │ Index Files   │
                                                   │ Analyzer     │         │ (JSON)        │
                                                   │              │         │               │
                                                   └──────────────┘         └───────────────┘
                                                          │                         │
                                                          │                         │
                                                          ▼                         ▼
                                                   ┌──────────────┐         ┌───────────────┐
                                                   │              │         │               │
                                                   │ Visualization │◄────────┤ YAML Config   │
                                                   │ Engine       │         │               │
                                                   │              │         │               │
                                                   └──────────────┘         └───────────────┘
```

1. LSP Bridge connects to language-specific servers
2. Structure Model builds an in-memory representation
3. JSON Generator creates standardized output
4. Relationship Analyzer enhances with framework-specific insights
5. Index files are created based on YAML configuration
6. Visualization Engine renders relationships graphically

## Engineering Principles

- **Accuracy Over Inference**: Use precise LSP extraction rather than regex or simple AST parsing
- **Structure Over Implementation**: Capture architectural elements, not implementation details
- **Framework-Aware Analysis**: Provide special handling for popular frameworks
- **Configurable Detail Levels**: Support different levels of detail for different use cases
- **Minimal Token Usage**: Optimize the representation for AI consumption
- **Extensible Architecture**: Allow new language and framework support to be added easily

## Implementation Approach

### LSP Integration

Architectum communicates with language servers using standard LSP protocol:

```javascript
async function getDocumentSymbols(uri) {
  const params = { textDocument: { uri } };
  return await languageServer.sendRequest(
    'textDocument/documentSymbol', 
    params
  );
}
```

### JSON Processing

LSP symbol information is preserved while enhancing with relationships:

```javascript
function processSymbols(symbols) {
  // Preserve LSP's kind and structure while enhancing with relationships
  return {
    name: symbols.main.name,
    kind: "class",  // Human-readable kind instead of numeric code
    detail: symbols.main.detail,
    methods: symbols.methods.map(method => ({
      name: method.name,
      kind: "method",
      detail: method.detail,
      range: method.range,
      selectionRange: method.selectionRange
    })),
    relationships: detectRelationships(symbols)
  };
}
```

### Multi-level Indexing

Indexes are built according to YAML configuration:

```javascript
function buildIndex(config) {
  const files = resolveGlobPatterns(config.include);
  const components = [];
  
  for (const file of files) {
    const symbols = getSymbolsForFile(file);
    const processedComponent = processSymbols(symbols);
    
    if (shouldIncludeInIndex(processedComponent, config)) {
      const detailedComponent = applyDetailLevel(processedComponent, config.detailLevel);
      components.push(detailedComponent);
    }
  }
  
  return { name: config.name, components };
}
```

## Index Types

## Index Types

Architectum provides multiple index types for different use cases:

### 1. System-Wide Index

Provides a high-level overview of the entire codebase:

```json
{
  "name": "system_index",
  "components": [
    {
      "name": "UserProfile",
      "kind": "class",
      "path": "src/components/UserProfile.vue",
      "imports": ["UserService", "AuthService"],
      "methods": [
        {"name": "fetchUserData", "kind": "method", "visibility": "public"},
        {"name": "updateProfile", "kind": "method", "visibility": "public"}
      ],
      "properties": [
        {"name": "userId", "kind": "property", "type": "string"},
        {"name": "theme", "kind": "property", "type": "string"} 
      ]
    },
    {
      "name": "UserService",
      "kind": "class",
      "path": "src/services/UserService.js",
      "methods": [
        {"name": "getUserData", "kind": "method", "visibility": "public"},
        {"name": "updateUser", "kind": "method", "visibility": "public"}
      ]
    },
    {
      "name": "AuthService",
      "kind": "class",
      "path": "src/services/AuthService.js",
      "methods": [
        {"name": "login", "kind": "method", "visibility": "public"},
        {"name": "validateToken", "kind": "method", "visibility": "public"}
      ]
    }
  ]
}
```

**For comprehensive examples of more detailed indexes, see the Advanced Examples section below.**

### 2. Path-Based Index

Organizes components by directory structure:

```json
{
  "name": "ui_components_index",
  "path": "src/ui/components",
  "components": [
    {
      "name": "LoginForm",
      "kind": "class",
      "methods": [
        {"name": "authenticate", "kind": "method"},
        {"name": "validateForm", "kind": "method"}
      ],
      "props": [
        {"name": "redirectUrl", "kind": "property", "type": "string"},
        {"name": "showRememberMe", "kind": "property", "type": "boolean"}
      ]
    },
    {
      "name": "UserProfile",
      "kind": "class",
      "methods": [
        {"name": "fetchUserData", "kind": "method"},
        {"name": "updateProfile", "kind": "method"}
      ],
      "props": [
        {"name": "userId", "kind": "property", "type": "string"},
        {"name": "editable", "kind": "property", "type": "boolean"}
      ]
    }
  ]
}
```

### 3. Focus-Based Index

Selects specific components and methods for targeted development:

```json
{
  "name": "auth_focus_index",
  "components": [
    {
      "name": "LoginForm",
      "kind": "class",
      "path": "src/ui/components/LoginForm.vue",
      "methods": [
        {
          "name": "authenticate",
          "kind": "method",
          "visibility": "public",
          "parameters": [
            {"name": "username", "type": "string"},
            {"name": "password", "type": "string"}
          ],
          "returns": {"type": "Promise<boolean>"},
          "calls": ["AuthService.login", "this.validateForm"]
        }
      ]
    },
    {
      "name": "AuthService",
      "kind": "class",
      "path": "src/services/AuthService.js",
      "methods": [
        {
          "name": "validateToken",
          "kind": "method",
          "visibility": "public",
          "parameters": [
            {"name": "token", "type": "string"}
          ],
          "returns": {"type": "boolean"}
        }
      ]
    }
  ]
}
```

### 4. Functional Index

Groups related components by feature or domain:

```json
{
  "name": "payment_system_index",
  "feature": "payment_processing",
  "components": [
    {
      "name": "PaymentForm",
      "kind": 5,
      "path": "src/components/PaymentForm.vue",
      "public_api": [
        {
          "kind": 6,
          "name": "submitPayment",
          "signature": "submitPayment(): Promise<PaymentResult>"
        },
        {
          "kind": 14,  // Event
          "name": "payment-success"
        }
      ]
    },
    {
      "name": "PaymentService",
      "kind": 5,
      "path": "src/services/PaymentService.js",
      "public_api": [
        {
          "kind": 6,
          "name": "processPayment",
          "signature": "processPayment(paymentData): Promise<PaymentResult>"
        }
      ]
    }
  ],
  "workflow": {
    "steps": [
      "User submits PaymentForm",
      "PaymentForm calls PaymentService.processPayment",
      "PaymentService returns result to PaymentForm"
    ]
  }
}
```

## Advanced Examples

For more comprehensive examples showing detailed representations, see the examples directory.

## Configuration Options

### Detail Levels

YAML configuration supports multiple detail levels:

```yaml
detail_levels:
  minimal:
    include_private: false
    include_parameters: false
    include_types: false
    
  standard:
    include_private: false
    include_parameters: true
    include_types: true
    
  detailed:
    include_private: true
    include_parameters: true
    include_types: true
    include_dataflow: true
```

### Framework-Specific Options

Special configuration for framework-specific analysis:

```yaml
framework_options:
  vue:
    track_props: true
    track_events: true
    track_slots: true
    track_store: true
    
  react:
    track_props: true
    track_hooks: true
    track_context: true
    track_memo: true
```

---

_"Structure first, implementation second. Architectum equips systems for intelligent conversation."_
