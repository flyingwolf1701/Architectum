#!/usr/bin/env node
/**
 * Architectum Project Initialization Script
 * Creates the complete project_docs structure for new projects.
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');

// Create readline interface for user input
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

/**
 * Promisify readline question
 */
function question(query) {
    return new Promise(resolve => rl.question(query, resolve));
}

/**
 * Create the project_docs directory structure
 */
function createDirectoryStructure() {
    const basePath = 'project_docs';
    
    const directories = [
        'catalogs',
        'core_documents',
        'epics',
        'supporting_documents'
    ];
    
    directories.forEach(directory => {
        const dirPath = path.join(basePath, directory);
        fs.mkdirSync(dirPath, { recursive: true });
        console.log(`✓ Created ${dirPath}`);
    });
}



/**
 * Create initial catalog YAML files
 */
function createCatalogFiles() {
    const catalogsPath = path.join('project_docs', 'catalogs');
    
    // Write project catalog
    const projectCatalogPath = path.join(catalogsPath, 'project_catalog.yaml');
    fs.writeFileSync(projectCatalogPath, 'files: []\n');
    console.log(`✓ Created ${projectCatalogPath}`);
    
    // Write feature catalog
    const featureCatalogPath = path.join(catalogsPath, 'feature_catalog.yaml');
    fs.writeFileSync(featureCatalogPath, 'features: []\n');
    console.log(`✓ Created ${featureCatalogPath}`);

    // Write test catalog
    const testCatalogPath = path.join(catalogsPath, 'test_catalog.yaml');
    fs.writeFileSync(testCatalogPath, 'tests: []\n');
    console.log(`✓ Created ${testCatalogPath}`);
}

/**
 * Create template files for core documents
 */
function createTemplateFiles() {
    const coreDocsPath = path.join('project_docs', 'core_documents');
    
    // Project brief template
    const projectBriefTemplate = `# Project Brief: {Project Name}

## Problem Statement
{Describe the core problem being solved}

## Vision & Goals
- **Vision:** {High-level desired future state}
- **Primary Goals:**
  - Goal 1: {Specific, measurable goal}
  - Goal 2: {Another specific goal}

## Target Users
{Describe primary users and their characteristics}

## Key Features (MVP Scope)
- Feature 1: {Core functionality}
- Feature 2: {Essential capability}

## Known Constraints
- Technical: {Any known limitations}
- Timeline: {Time constraints}
- Budget: {Resource constraints}

## Success Metrics
{How will success be measured}
`;
    
    // PRD template
    const prdTemplate = `# {Project Name} Product Requirements Document

## Status: Draft

## Goals & Context
{Copy from project brief and expand}

## Functional Requirements (MVP)
{Core functionality requirements}

## Non-Functional Requirements
{Performance, security, scalability requirements}

## Technical Assumptions
{Technology choices and constraints}

## Epic Overview
{High-level epic breakdown}

## Out of Scope (Post-MVP)
{Features deliberately excluded from MVP}
`;
    
    // Architecture template
    const architectureTemplate = `# {Project Name} Architecture Document

## Status: Draft

## Technical Summary
{Brief overview of architecture approach}

## High-Level Overview
{System architecture and key components}

## Technology Stack
{Definitive technology selections}

## Component Architecture
{Detailed component breakdown}

## Data Models
{Core data structures and relationships}

## API Design
{API contracts and interfaces}

## Security & Compliance
{Security approach and requirements}

## Testing Strategy
{Testing approach and coverage}

## Deployment & Operations
{Deployment and operational considerations}
`;

    // Frontend Architecture template
    const frontendArchitectureTemplate = `# {Project Name} Frontend Architecture Document

## Status: Draft

## Technical Summary
{Brief overview of frontend architecture approach}

## Frontend Framework & Technology Stack
{Frontend technology selections and frameworks}

## Component Architecture
{Component organization and structure}

## State Management
{State management approach and patterns}

## Routing & Navigation
{Routing strategy and navigation structure}

## Build & Deployment
{Frontend build process and deployment strategy}

## Testing Strategy
{Frontend testing approach and coverage}

## Performance & Optimization
{Frontend performance considerations}
`;
    
    // Write template files
    const templates = [
        ['project_brief.md', projectBriefTemplate],
        ['prd.md', prdTemplate],
        ['architecture.md', architectureTemplate],
        ['frontend-architecture.md', frontendArchitectureTemplate]
    ];
    
    templates.forEach(([filename, content]) => {
        const filePath = path.join(coreDocsPath, filename);
        fs.writeFileSync(filePath, content);
        console.log(`✓ Created ${filePath}`);
    });
}

/**
 * Create the master index.md file with integrated project status tracking
 */
function createIndexFile() {
    const indexContent = `# {Project Name} Documentation Index

## Project Status
**Current Phase:** initialization  
**Last Updated:** auto-generated  
**Agent Context:** project_planner

### Phase Progress
- [ ] **1. Ideation** - project_brief.md
- [ ] **2. Requirements** - prd.md  
- [ ] **3. Architecture** - architecture.md
- [ ] **4. Frontend Architecture** - frontend-architecture.md (if applicable)
- [ ] **5. Epic Breakdown** - epic-*.md files
- [ ] **6. Story Preparation** - story-*.md files
- [ ] **7. Doc Sharding** - supporting_documents/*
- [ ] **8. Ready for Dev** - all artifacts complete

**Current Epic:** None  
**Current Story:** None

### Notes
*Project notes and key decisions will be tracked here*

## Core Documents
- [Project Brief](core_documents/project_brief.md) - Initial project definition
- [Product Requirements](core_documents/prd.md) - Detailed requirements and epics  
- [Architecture](core_documents/architecture.md) - Technical architecture and design
- [Frontend Architecture](core_documents/frontend-architecture.md) - Frontend-specific architecture (if applicable)

## Epics & Stories
{Epic directories will be created during planning phase}

## Supporting Documents
{Detailed documentation will be generated during sharding phase}

## Catalogs
- [Project Catalog](catalogs/project_catalog.yaml) - File and component inventory
- [Feature Catalog](catalogs/feature_catalog.yaml) - Feature-to-code mapping
- [Test Catalog](catalogs/test_catalog.yaml) - Test code mapping

---
*This index is automatically maintained by Architectum agents*
`;
    
    const indexPath = path.join('project_docs', 'index.md');
    fs.writeFileSync(indexPath, indexContent);
    console.log(`✓ Created ${indexPath}`);
}



/**
 * Main initialization function
 */
async function main() {
    try {
        console.log('🚀 Initializing Architectum project structure...');
        
        // Check if project_docs already exists
        if (fs.existsSync('project_docs')) {
            const response = await question('project_docs/ directory already exists. Continue? (y/N): ');
            if (response.toLowerCase() !== 'y') {
                console.log('❌ Initialization cancelled.');
                rl.close();
                process.exit(1);
            }
        }
        
        // Create structure
        createDirectoryStructure();
        createCatalogFiles();
        createTemplateFiles();
        createIndexFile();
        
        console.log('\n✅ Architectum project structure initialized successfully!');
        console.log('\nNext steps:');
        console.log('1. Run the project_planner agent');
        console.log('2. Start with ideation and project brief creation');
        console.log('3. Track progress using the phase checklist in project_docs/index.md');
        console.log('\nProject structure created in: project_docs/');
        
        rl.close();
        
    } catch (error) {
        console.error('❌ Error during initialization:', error.message);
        rl.close();
        process.exit(1);
    }
}

// Run the script
if (require.main === module) {
    main();
}

module.exports = {
    createDirectoryStructure,
    createCatalogFiles,
    createTemplateFiles,
    createIndexFile,
    main
};