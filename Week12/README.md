Week 12 – Testing Discipline
Overview

This week focuses on establishing testing discipline for Python backend development. The main goals are:

Implement unit and integration tests using PyTest

Use fixtures and mocking for repeatable tests

Apply the test pyramid principle (unit → integration → end-to-end)

Enforce test coverage thresholds (≥50%)

Automate tests on pull requests via GitHub Actions

Project Structure
week12-testing-discipline/
│
├── src/
│   ├── main.py                  # App entry point
│   ├── api/
│   │   └── health.py            # Health check route
│   ├── services/
│   │   └── user_service.py      # Business logic
│   └── repositories/
│       └── user_repository.py   # Database simulation
│
├── tests/
│   ├── conftest.py              # PyTest fixtures
│   ├── unit/
│   │   └── test_user_service.py # Unit tests for services
│   └── integration/
│       └── test_health_route.py # Integration tests for API
│
├── pyproject.toml               # PyTest and coverage config
├── requirements.txt             # Dependencies
└── .github/
    └── workflows/
        └── tests.yml            # CI workflow

Setup

Create a virtual environment:

python -m venv venv


Activate the environment:

Windows (PowerShell):

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt

Running Tests Locally

Run all tests:

pytest


Run tests with coverage report:

pytest --cov=src


Expected coverage: ≥50% (configured in pyproject.toml)

PyTest Fixtures

test_app – FastAPI app instance

client – Test client for integration tests

mock_repo – Mocked database repository for unit tests

Test Coverage

Configured in pyproject.toml:

addopts = "--cov=src --cov-report=term-missing --cov-fail-under=50"


Coverage must meet 50% threshold

CI fails if coverage < 50%

Running API Locally
uvicorn src.main:app --reload


Test the health endpoint:

curl http://127.0.0.1:8000/health


Response:

{
  "status": "ok"
}

GitHub Actions CI

Runs automatically on pull requests to main

Installs dependencies, runs tests, and checks coverage

CI passes only if all tests pass and coverage ≥50%

Acceptance Criteria / KPIs

✅ Unit tests for all services

✅ Integration tests for all routers

✅ Fixtures for app, client, and DB

✅ Coverage ≥50%

✅ CI green on pull request

✅ PR contains description + screenshot of CI