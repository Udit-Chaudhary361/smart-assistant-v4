# Smart Assistant V4 🤖

A Personal Assistant built in Python with SQLite database integration and modular architecture.

## Features

* User Management (Set Name, View Name)
* Task Management (CRUD)
* Notes Management (CRUD)
* Task Statistics
* Random Joke Generator
* Logging System
* Command History Tracking
* Persistent Storage using SQLite Database
* Modular Design using Packages

## What's New in V4

* Migrated storage from JSON to SQLite
* Implemented database tables for users, notes, and tasks
* Learned and applied SQL CRUD operations
* Improved scalability and data persistence
* Better foundation for future AI features

## Tech Stack

* Python
* SQLite
* SQL
* File Handling
* OOP Design

## Project Structure

```text
smart_assistant_v4/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── logger.py
│   └── tools/
│       └── joke_tool.py
│
├── data/
│   ├── assistant.db
│   └── History.txt
│
├── tests/
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Database Tables

### User

Stores assistant user information.

### Notes

Stores user notes.

### Tasks

Stores tasks and completion status.

## Purpose

This project is part of my journey toward building an AI Personal Assistant and Research Agent.

Smart Assistant V4 is an upgraded version of Smart Assistant V3, where JSON-based storage was replaced with SQLite database storage to learn real-world database concepts and software architecture.

## Learning Outcomes

* SQLite Integration with Python
* SQL CRUD Operations
* Database Design Fundamentals
* Project Refactoring
* Error Handling and Validation
* Modular Software Development

## Future Roadmap

```text
Smart Assistant V4
↓
Flask Web App
↓
LLM Integration
↓
Embeddings
↓
Vector Databases
↓
RAG
↓
AI Agents
```

## Author

Built by a B.Tech student learning Software Engineering, AI Systems, and Agent Development.
