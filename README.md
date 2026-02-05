# SOLID Principles API Project

A RESTful API built with Flask and Python, demonstrating SOLID principles and clean architecture patterns. This project manages people and their associated pets through a well-structured, maintainable codebase.

## 📋 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Testing](#testing)
- [Development](#development)

## ✨ Features

- **Person Management**: Create and retrieve person records
- **Pet Management**: List and delete pet records
- **Data Validation**: Input validation for person creation
- **Error Handling**: Comprehensive error handling with appropriate HTTP status codes
- **SOLID Principles**: Implementation of Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion principles
- **Clean Architecture**: Separation of concerns with controllers, views, repositories, and composers

## 🏗️ Architecture

This project follows a **Clean Architecture** pattern with clear separation of concerns:

- **Controllers**: Business logic and validation
- **Views**: HTTP request/response handling
- **Repositories**: Data access layer (SQLite)
- **Composers**: Dependency injection and object composition
- **Validators**: Input validation
- **Error Handlers**: Centralized error management

### Design Patterns

- **Dependency Injection**: Controllers receive repository interfaces
- **Repository Pattern**: Data access abstraction
- **Composer Pattern**: Dependency composition and wiring
- **Interface Segregation**: Small, focused interfaces

## 🛠️ Tech Stack

- **Python 3.x**
- **Flask 3.1.2**: Web framework
- **SQLAlchemy 2.0.45**: ORM for database operations
- **SQLite**: Lightweight database
- **Flask-CORS 6.0.2**: Cross-Origin Resource Sharing support
- **Pytest 9.0.2**: Testing framework
- **Pylint 4.0.4**: Code quality and linting

## 📁 Project Structure

```
Solid/
├── init/
│   └── schema.sql              # Database schema and initial data
├── src/
│   ├── controllers/            # Business logic controllers
│   │   ├── interfaces/         # Controller interfaces
│   │   ├── person_creator_controller.py
│   │   ├── person_finder_controller.py
│   │   ├── pet_lister_controller.py
│   │   └── pet_deleter_controller.py
│   ├── errors/                 # Error handling
│   │   ├── error_handler.py
│   │   └── error_types/        # Custom error types
│   ├── main/                   # Application entry point
│   │   ├── composer/           # Dependency injection composers
│   │   ├── routes/             # Flask route definitions
│   │   └── server/             # Flask app configuration
│   ├── models/                 # Data models and repositories
│   │   └── sqlite/
│   │       ├── entities/       # SQLAlchemy models
│   │       ├── interfaces/     # Repository interfaces
│   │       ├── repositories/   # Repository implementations
│   │       └── settings/       # Database connection
│   ├── validators/             # Input validation
│   └── views/                  # HTTP request/response handling
│       ├── http_types/         # HTTP request/response types
│       └── interfaces/         # View interfaces
├── run.py                      # Application entry point
├── requirements.txt            # Python dependencies
└── storage.db                  # SQLite database file
```

## 🚀 Installation

### Prerequisites

- Python 3.x installed
- pip package manager

### Setup Steps

1. **Clone the repository** (if applicable) or navigate to the project directory

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```
   Or on Windows:
   ```bash
   py -m venv .venv
   ```

3. **Activate the virtual environment**:
   
   On Windows (PowerShell):
   ```bash
   .\.venv\Scripts\Activate.ps1
   ```
   
   On Linux/Mac:
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Initialize the database**:
   The database will be automatically created when you first run the application. The schema is defined in `init/schema.sql`.

## 💻 Usage

### Running the Application

Start the Flask development server:

```bash
python run.py
```

The API will be available at `http://localhost:3000`

### Running in Debug Mode

The application runs in debug mode by default (as configured in `run.py`), which provides:
- Automatic reloading on code changes
- Detailed error messages
- Interactive debugger

## 📡 API Endpoints

### Person Endpoints

#### Create Person
```http
POST /person
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe",
  "age": 30,
  "pet_id": 1
}
```

**Response** (201 Created):
```json
{
  "data": {
    "type": "Person",
    "count": 1,
    "attributes": {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "age": 30,
      "pet_id": 1
    }
  }
}
```

#### Get Person by ID
```http
GET /person/{person_id}
```

**Response** (200 OK):
```json
{
  "data": {
    "type": "Person",
    "count": 1,
    "attributes": {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "age": 30,
      "pet_id": 1,
      "pet_name": "cobra",
      "pet_type": "snake"
    }
  }
}
```

### Pet Endpoints

#### List All Pets
```http
GET /pets
```

**Response** (200 OK):
```json
{
  "data": {
    "type": "Pets",
    "count": 7,
    "attributes": [
      {
        "pet_id": 1,
        "pet_name": "cobra",
        "pet_type": "snake"
      },
      {
        "pet_id": 2,
        "pet_name": "cao",
        "pet_type": "dog"
      }
    ]
  }
}
```

#### Delete Pet by Name
```http
DELETE /pets/{name}
```

**Response** (200 OK):
```json
{
  "data": {
    "type": "Pet",
    "count": 1,
    "attributes": {
      "message": "Pet deleted successfully"
    }
  }
}
```

### Error Responses

The API returns appropriate HTTP status codes:

- **400 Bad Request**: Invalid input data (e.g., invalid name format)
- **404 Not Found**: Resource not found
- **422 Unprocessable Entity**: Validation errors
- **500 Internal Server Error**: Server errors

## 🗄️ Database Schema

### Pets Table
```sql
CREATE TABLE pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL
);
```

### People Table
```sql
CREATE TABLE people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    pet_id INTEGER NOT NULL,
    FOREIGN KEY (pet_id) REFERENCES pets(id)
);
```

### Initial Data

The database is pre-populated with sample pets:
- cobra (snake)
- cao (dog)
- gato (cat)
- jorgin (hamster)
- burro (donkey)
- shrek (ogro)
- belinha (dog)

## 🧪 Testing

The project includes test files for controllers and repositories. Run tests using pytest:

```bash
pytest
```

Test files are located alongside their corresponding implementation files with the `_test.py` suffix.

## 🔧 Development

### Code Quality

The project uses **Pylint** for code quality checks:

```bash
pylint src/
```

### Pre-commit Hooks

Install pre-commit hooks (if configured):

```bash
pip install pre-commit
pre-commit install
```

### Adding New Features

When adding new features, follow the existing architecture:

1. **Create Interface**: Define interface in `interfaces/` directory
2. **Implement Controller**: Business logic in `controllers/`
3. **Create Repository**: Data access in `repositories/`
4. **Create View**: HTTP handling in `views/`
5. **Create Composer**: Dependency injection in `composer/`
6. **Add Route**: Register route in `routes/`
7. **Add Tests**: Create test file with `_test.py` suffix

### Validation Rules

- **Person Names**: Must contain only letters (a-z, A-Z)
- **Age**: Must be a valid integer
- **Pet ID**: Must reference an existing pet

## 📝 Notes

- The project uses SQLite for simplicity, but the repository pattern allows easy migration to other databases
- All dependencies are managed through `requirements.txt`
- The database file (`storage.db`) is created automatically on first run
- CORS is enabled for cross-origin requests

## 🤝 Contributing

This is a learning project demonstrating SOLID principles and clean architecture. Feel free to explore the codebase and use it as a reference for your own projects.

## 📄 License

This project is for educational purposes.

