# Week 15 – Advanced Querying: Pagination, Sorting, Search

## Project Overview

This project demonstrates **advanced querying techniques** in a FastAPI application, including:

- **Offset Pagination** (`page` + `limit`)
- **Cursor Pagination** (`cursor` + `limit`)
- **Sorting** (`?sort=-created_at`)
- **Basic Text Search** (`?q=search_term`)
- **Database Indexing** for optimized queries

The project is designed to handle **large datasets efficiently**, ensuring consistent API responses and high performance.

---

## Folder Structure

project-root/
│
├── src/
│ ├── main.py
│ ├── core/
│ │ ├── database.py
│ │ ├── pagination.py
│ │ ├── search.py
│ │ └── sorting.py
│ ├── models/
│ │ └── user.py
│ ├── schemas/
│ │ └── user.py
│ ├── services/
│ │ └── user_service.py
│ └── api/
│ └── v1/
│ └── users.py
│
├── tests/
│ ├── conftest.py
│ ├── test_pagination.py
│ ├── test_search.py
│ └── test_sorting.py
│
├── scripts/
│ └── seed_users.py
│
├── docs/
│ └── explain_plan.md
├── requirements.txt
└── README.md


---

## Setup Instructions

1. **Clone the repository**:

```bash
git clone <repo-url>
cd Week15
Create and activate virtual environment:

python -m venv venv
venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Configure database:

For SQLite (default):

DATABASE_URL = "sqlite:///./test.db"
For PostgreSQL:

DATABASE_URL = "postgresql://user:password@localhost:5432/appdb"
Create database tables:

python
>>> from src.core.database import Base, engine
>>> from src.models.user import User
>>> Base.metadata.create_all(bind=engine)
>>> exit()
Seed sample data:

python -m scripts.seed_users
Running the API
Start FastAPI server:

uvicorn src.main:app --reload
Open Swagger UI: http://127.0.0.1:8000/docs

API Endpoints
GET /api/v1/users
Retrieve a list of users with pagination, sorting, and search.

Query Parameters:

Parameter	Type	Description
page	int	Page number (offset pagination)
limit	int	Items per page
cursor	int	Cursor ID for cursor pagination
sort	str	Sort field (- prefix for descending)
q	str	Text search on name and email
Examples:

Offset Pagination:

GET /api/v1/users?page=1&limit=5
Cursor Pagination:

GET /api/v1/users?cursor=10&limit=5
Sorting:

GET /api/v1/users?sort=-created_at
Search:

GET /api/v1/users?q=python
Sample Response:

[
  {
    "id": 3,
    "name": "Python Dev",
    "email": "python@test.com",
    "created_at": "2026-01-29T10:30:00"
  },
  {
    "id": 2,
    "name": "Jane",
    "email": "jane@test.com",
    "created_at": "2026-01-28T12:20:00"
  }
]
Testing
Run all tests:

pytest
Tests cover:

Offset pagination

Cursor pagination

Sorting

Search

Sample fixture client is provided in tests/conftest.py using FastAPI TestClient.

Expected result: 3 passed

Performance & Indexing
Recommended database indexes:

CREATE INDEX idx_users_created_at ON users (created_at);
CREATE INDEX idx_users_name_email ON users (name, email);
Use EXPLAIN ANALYZE for query performance:

EXPLAIN ANALYZE
SELECT id, name, email
FROM users
WHERE name ILIKE '%python%'
ORDER BY created_at DESC
LIMIT 10;
Key Notes
Offset Pagination: Easy to implement, works for small datasets.

Cursor Pagination: Efficient for large datasets, prevents skipped row scanning.

Sorting & Search: Works with both pagination types.

FastAPI + SQLAlchemy: Clear separation between core, services, models, and API.

Test coverage ≥ 60% for deliverables.