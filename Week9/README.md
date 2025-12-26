Week 9 – Redis Caching (FastAPI)
📌 Overview

This project demonstrates Redis caching using the cache-aside pattern in a FastAPI application.
Hot GET endpoints are cached with TTL strategies, and cache invalidation is handled on data mutations.
The goal is to reduce API latency by at least 30% while maintaining clean architecture, test coverage, and documentation.

🎯 Learning Goals

Redis client connection and lifecycle management

Cache-aside pattern implementation

TTL strategies (default & per-route overrides)

Cache invalidation on create/update/delete

Cache hit/miss metrics logging

🧱 Project Folder Structure
Week9/
│
├── src/
│   ├── main.py                     # FastAPI app entry point
│   │
│   ├── api/                        # API / routers layer
│   │   ├── __init__.py
│   │   └── items.py                # /items endpoints
│   │
│   ├── services/                   # Business logic layer
│   │   ├── __init__.py
│   │   └── cache_service.py        # Redis cache utilities & decorators
│   │
│   ├── repositories/               # Data access layer
│   │   ├── __init__.py
│   │   └── item_repository.py      # Item data source (mock/in-memory)
│   │
│   ├── core/                       # Core infrastructure
│   │   ├── __init__.py
│   │   └── redis.py                # Redis client setup & config
│   │
│   └── __init__.py
│
├── tests/
│   ├── services/
│   │   └── test_cache_service.py   # Cache service unit tests
│   │
│   ├── repositories/
│   │   └── test_item_repository.py # Repository unit tests
│   │
│   └── __init__.py
│
├── venv/                           # Virtual environment
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Tech Stack

Python 3.13

FastAPI

Redis

Docker

pytest + pytest-cov

Uvicorn

🚀 How to Run the Application
1️⃣ Clone & Setup Virtual Environment
git clone <repo-url>
cd Week9
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

2️⃣ Start Redis using Docker
docker run -d --name redis-week9 -p 6379:6379 redis


Verify:

docker ps

3️⃣ Set PYTHONPATH (Important)
$env:PYTHONPATH="."

4️⃣ Run FastAPI Server
uvicorn src.main:app --reload


Server:

http://127.0.0.1:8000


Swagger:

http://127.0.0.1:8000/docs

🧠 Cache Design
Cache Pattern

Cache-aside (Lazy Loading)

On GET:

Check Redis → return if hit

Else fetch from repository → store in Redis → return

On POST/PUT/DELETE:

Invalidate related cache keys

TTL Strategy

Default TTL: 60 seconds

Configurable per route if required

📊 Cache Metrics

Cache hit/miss logged via application logs

Used for validating performance improvements

Example log:

CACHE HIT: items:all
CACHE MISS: items:all

🧪 Running Tests & Coverage
pytest --cov=src

✅ Coverage Targets

Services + repositories fully unit-tested

Overall coverage ≥ 38%

⚡ Performance Benchmark (Local)
Scenario	Avg Response Time
Without Cache	~120 ms
With Redis Cache	~70 ms

✅ Latency reduced by ~40%, exceeding KPI.

📦 API Endpoints
Method	Endpoint	Description	Cache
GET	/items/	Get all items	✅
GET	/	Health check	❌
🔍 Code Quality & Rules Followed

PEP8 compliant

Type hints & docstrings

Clean separation of concerns:

API → api/

Business logic → services/

Data access → repositories/

Redis isolated in core/

Unit tests for services & repositories

Swagger updated