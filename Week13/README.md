📌 Week 13 – Async & Concurrency FastAPI Project
Project Overview

This project demonstrates asynchronous FastAPI routes, async database operations, and structured concurrency using asyncio.

It is built with:

FastAPI – web framework

SQLAlchemy Async – async ORM

SQLite (aiosqlite) – async database for simplicity

pytest + pytest-asyncio + pytest-cov – for testing & coverage

Learning Goals:

Convert synchronous DB calls and services to async

Implement concurrent tasks with asyncio.gather

Handle timeouts and task cancellations

Measure performance improvement (P95 latency)

Folder Structure
project-root/
│
├── app/
│   ├── main.py               # FastAPI app
│   ├── core/                 # config & async DB
│   ├── models/               # SQLAlchemy models
│   ├── schemas/              # Pydantic schemas
│   ├── repositories/         # Async DB calls
│   ├── services/             # Business logic + concurrency
│   ├── utils/                # Timeout & cancellation helpers
│   └── tests/                # Async test cases
├── README.md
├── requirements.txt
└── .env

Features / Endpoints
Endpoint	Method	Description	Input	Output
/api/users/	POST	Create a new user	{ "name": "Mekala", "email": "mekala@gmail.com", "age": 24 }	{ "id": "uuid", "name": "...", "email": "...", "age": 24 }
/api/users/{id}	GET	Fetch user by ID	Path param: user_id	{ "id": "uuid", "name": "...", "email": "...", "age": 24 }
/api/users/{id}/dashboard	GET	Fetch multiple user data concurrently	Path param: user_id	{ "profile": {...}, "activity": {...}, "settings": {...} }
/api/users/{id}/external-profile	GET	Async external call with timeout	Path param: user_id	{ "linkedin": "..." } or { "error": "Timeout" }
Async & Concurrency Implementation

All routes, repositories, and services are fully async (async def)

Concurrent tasks implemented using:

profile, activity, settings = await asyncio.gather(
    fetch_profile(),
    fetch_activity(),
    fetch_settings()
)


Timeout handling:

try:
    await asyncio.wait_for(external_call(), timeout=2)
except asyncio.TimeoutError:
    return {"error": "Timeout"}


Cancellation patterns supported via asyncio.CancelledError.

Performance Improvement
Endpoint	Before (Sync)	After (Async)
Dashboard	~450ms	~180ms

P95 latency significantly improved thanks to structured concurrency.

Setup & Run

Clone & Navigate

git clone <repo_url>
cd Week13


Create & activate virtual environment

python -m venv venv
.\venv\Scripts\activate   # Windows
# source venv/bin/activate # macOS/Linux


Install dependencies

pip install -r requirements.txt


Create DB tables

python -m app.init_db


Run FastAPI server

uvicorn app.main:app --reload


Swagger UI

Open: http://127.0.0.1:8000/docs

Run Tests & Coverage
# Ensure venv is active
$env:PYTHONPATH="."
pytest --cov=app


Expected Coverage: ≥ 55% (ours: 75%)

Testing Async & Concurrency

/dashboard demonstrates parallel fetching of profile, activity, settings

/external-profile demonstrates timeout handling

Unit tests cover async services & repositories