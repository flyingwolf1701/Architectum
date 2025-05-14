# Architectum Configuration Q&A

## Understanding The Configuration Options

### Q1: Does frontend include show src/ui and all of its children?

Yes. The pattern `src/ui/**/*` includes the `src/ui` directory and all of its children (subdirectories and files). This would create a consolidated XML index containing the entire frontend structure. The `**` means "any subdirectory (including nested subdirectories)" and `*` means "any file".

### Q2: Does the User management module include src/users and src/auth and their children?

Exactly. The include pattern `["src/users/**/*", "src/auth/**/*"]` tells Architectum to include both the `src/users` and `src/auth` directories and all their child directories and files in this index. This creates a focused index for just the user management-related code, even though it spans multiple directories.

### Q3: How does the active development index know where components are?

The system resolves component names through several mechanisms:

1. **By File Name**: Searching the codebase for files named like the component
2. **By Component Definition**: Looking for classes/functions that define components with those names
3. **Through a Component Registry**: A mapping of component names to file paths that can be built automatically
4. **Explicitly Qualified Names**: You can provide paths like "src/users/UserProfile.vue" for direct mapping

You can use just the component name ("UserProfile") or fully qualified paths ("src/users/UserProfile.vue") depending on your needs.

### Q4: Components vs. Files - What's the difference?

Your instinct to use them interchangeably makes sense in many cases, but there's a subtle distinction:

- **File**: A physical source code file (e.g., UserProfile.vue)
- **Component**: A logical unit of code that may be defined in a file (e.g., the UserProfile component)

In many frameworks (especially Vue, React), there's often a 1:1 mapping between files and components, so using them interchangeably works well. However, some files might define multiple components, or a component might span multiple files.

Architectum handles both concepts:
- Path-based indexing works with files
- Component-based indexing works with logical components
- In most cases, they align naturally

### Q5: How would the most detailed version work?

The most detailed version would include:
- Top-level component data (props, events, types)
- All methods with their signatures and relationships
- Parameter information and data flow
- All relevant relationships

This is captured in the `full` detail level, and you can apply it to specific components you're focusing on. The `component_focused` detail level specifically prioritizes component-specific details like props and events.

### Q6: How do I create a group of just 2-3 specific components?

The `active_development` index type does exactly this. For example:

```yaml
focused_components:
  name: "focused_group"
  include_components: ["LoginForm", "AuthService", "UserProfile"]
  detail_level: "component_focused"
  output: "structure/indexes/focused_group.xml"
```

This creates a single XML file containing just these specific components, regardless of where they are in the codebase.

### Q7: How does the file structure mirroring work?

The `file_mirror` configuration creates a directory structure that matches your source code:

```yaml
file_mirror:
  include: ["src/**/*"]
  output_mode: "file_mirror"
  output_dir: "structure/detailed"
```

This will:
1. Scan all files under `src/`
2. Create a matching directory structure under `structure/detailed/`
3. Generate one XML file per source file

For example:
- `src/users/UserProfile.vue` → `structure/detailed/users/UserProfile.xml`
- `src/auth/AuthService.js` → `structure/detailed/auth/AuthService.xml`

This creates a complete, detailed map of your entire codebase organized just like the original files.
