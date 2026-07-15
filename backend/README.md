# Backend

## Overview

This directory contains the backend implementation of the Integrated Research Environment.

The backend is responsible for providing the platform's core services, scientific capabilities, data management, evidence tracking, and application programming interfaces (APIs).

Rather than serving as a traditional CRUD application, the backend implements the domain model that supports evidence-based scientific workflows.

---

## Technology Stack

Current technologies include:

* Python
* FastAPI
* PostgreSQL *(planned)*
* SQLAlchemy *(planned)*
* Alembic *(planned)*
* uv
* Docker *(planned)*

Additional technologies will be introduced as the platform evolves.

---

## Architecture

The backend follows a layered architecture inspired by Domain-Driven Design and Clean Architecture.

```text
Presentation (API)
        ↓
Application
        ↓
Domain
        ↓
Infrastructure
```

This separation ensures that scientific concepts remain independent of implementation technologies.

---

## Planned Structure

```text
backend/
│
├── app/
│   ├── api/
│   ├── application/
│   ├── core/
│   ├── domain/
│   ├── infrastructure/
│   ├── plugins/
│   ├── shared/
│   └── main.py
│
├── tests/
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Development Philosophy

Development follows these principles:

* Architecture before implementation
* Domain before database
* Evidence before automation
* Scientific reproducibility by design
* Modularity and extensibility
* Testable components
* Comprehensive documentation

The initial implementation focuses on building the platform foundation before introducing domain-specific biological functionality.

---

## Running the Development Server

After installing the project dependencies:

```bash
uv run fastapi dev app/main.py
```

or, depending on the final project configuration:

```bash
uv run uvicorn app.main:app --reload
```

---

## Current Status

The backend is in its foundational stage.

Upcoming milestones include:

1. Core project structure
2. Domain model
3. Platform services
4. Plugin framework
5. Biological Discovery Studio

