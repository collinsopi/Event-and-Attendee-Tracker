## Event and Attendee Tracker 🎟️

This is a command-line interface (CLI) application for managing events and tracking attendees. Built with Python and SQLAlchemy, it demonstrates a complete ORM-based application with a focus on a clear hierarchical structure and many-to-many relationships.

## Core Technologies
->Python 3.12: The primary programming language used for the application logic.

->SQLAlchemy: A powerful SQL toolkit and Object-Relational Mapper (ORM) for Python. It is used to interact with the database using Python objects instead of raw SQL.

->Pipenv: A dependency manager that handles a project's virtual environment and package dependencies, ensuring a consistent development environment.

->Alembic: A lightweight database migration tool for SQLAlchemy. It's used to manage and apply changes to the database schema.

->SQLite: A lightweight, file-based relational database engine used for local data storage.

## Features
->Event Management: Create, view, update, and delete events. Each event has a name, date, and location.

->Attendee Management: Register new attendees with a name and email, and view or delete existing attendees.

->Event Registration: Link attendees to events, allowing you to track which events a person is attending and who is registered for a specific event.

->Data Persistence: All data is stored in a local SQLite database file, events.db, ensuring your information is saved between sessions.

## Project Structure
The project is organized into a logical folder structure to separate concerns.

.
├── Pipfile
├── README.md
└── lib/
    ├── cli.py            # Main CLI application
    ├── helpers.py        # Utility functions for the CLI
    └── db/
        ├── alembic.ini   # Alembic configuration file
        ├── database.py   # Database engine and session setup
        ├── models.py     # SQLAlchemy ORM models
        ├── seed.py       # Script to populate the database with sample data
        └── migrations/   # Alembic migration scripts


## Project done by:

Collins Opiayo