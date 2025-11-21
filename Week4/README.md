📌 Week 4 – Python CRUD Module (Clean Architecture + JSON Store)

This project is part of Chartflow Internship – Week 4 Assignment, implementing a production-style CRUD module using FastAPI, Clean Architecture, and a JSON file as the persistent data store.

The module manages an Item entity with full CRUD operations, search, pagination, validation, and unit tests.

🚀 Features
✅ CRUD Endpoints

Create Item – POST /items/

List Items – GET /items/?page=&size=&q=

Get Item by ID – GET /items/{id}

Update Item – PUT /items/{id}

Delete Item – DELETE /items/{id}

🔍 Advanced Features

Search (?q=) on name and description

Pagination (?page=&size=)

JSON File Persistence (data/items.json)

Clean Architecture Layers

api → Routing layer

services → Business logic

repositories → JSON persistence

schemas → Pydantic models

core → Utilities (pagination)

🧪 Test Coverage

Repository tests

Service tests

Pagination tests

Coverage report ≥ 22%

📁 Project Structure
week4_crud/
├─ app/
│  ├─ main.py
│  ├─ api/
│  │  └─ items_router.py
│  ├─ services/
│  │  └─ item_service.py
│  ├─ repositories/
│  │  └─ item_repo.py
│  ├─ schemas/
│  │  └─ item.py
│  └─ core/
│     └─ pagination.py
├─ data/
│  └─ items.json
├─ tests/
│  ├─ test_repositories/
│  └─ test_services/
├─ requirements.txt
└─ README.md

🛠️ Tech Stack

Python 3.10+

FastAPI

Pydantic

Uvicorn

Pytest

JSON File Storage

Clean Architecture Principles

📦 Installation

Clone the repository:

git clone <your-repo-url>
cd week4_crud


Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

▶️ Run the Application

Start the FastAPI server:

uvicorn app.main:app --reload


Open Swagger UI:

👉 http://127.0.0.1:8000/docs

👉 http://127.0.0.1:8000/redoc

🧪 Run Tests

To run unit tests:

pytest -q


With coverage:

pytest --cov=app --cov-report=term-missing

🧵 API Summary
POST /items/

Create a new item:

{
  "name": "Pen",
  "description": "Blue ink pen"
}

GET /items/?page=1&size=10&q=pen

Fetch all items with search + pagination.

PUT /items/1

Update item:

{
  "name": "Marker"
}

DELETE /items/1

Deletes an item permanently.

📘 Design Principles Followed
✔ Clean Architecture

Independent layers

Business logic separated from controllers

Repository pattern for data access

✔ Validation

Input validation using Pydantic

Custom exceptions for not found errors

✔ Scalability

Can easily switch JSON store → SQLite/MySQL in the same structure

Pagination and search built in

🖥️ Screenshots (Add in PR)

Include:

Swagger UI screenshot

GitHub branch & commit screenshot

Test results screenshot



PR Checklist:

 Code builds successfully

 Endpoints tested in Swagger

 Unit tests passing

 Coverage report > 22%

 Screenshots uploaded
