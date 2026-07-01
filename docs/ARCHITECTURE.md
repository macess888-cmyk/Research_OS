# Research OS Architecture

Research OS is a modular Streamlit-based research management platform.

## Layers

Content Layer
- Markdown files
- JSON registries
- Research profile data

Service Layer
- Registry Engine
- Search Engine
- Graph Engine
- Health Engine
- Validation Engine
- Workspace Engine
- Intelligence Engine
- PDF Generator

Presentation Layer
- Streamlit pages
- Sidebar navigation
- Dashboard views
- Build Center

Output Layer
- PDF dossiers
- Backups
- Future website exports

## Core Principle

Content is separated from code.

Markdown and JSON provide the source of truth.
The application reads, validates, searches, analyzes, and exports that content.