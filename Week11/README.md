Week 11 – Error Handling & Logging (FastAPI)
Project Overview

This project implements centralized error handling, structured JSON logging, and request correlation IDs in a FastAPI application.
It follows production-grade backend engineering practices and meets all Week 11 acceptance criteria.

The goal is to ensure:

All errors are standardized

Logs are machine-parseable (JSON)

Every request can be traced using a correlation ID

Learning Goals

Centralized global exception handling

Structured JSON logging

Request correlation ID propagation

Testable and observable backend services

Tech Stack

Python 3.13

FastAPI

Starlette Middleware

Pytest

Logging (JSON format)

Folder Structure
Week11/
│
├── src/
│   ├── main.py
│   │
│   ├── api/
│   │   └── health.py
│   │
│   ├── core/
│   │   └── errors.py
│   │
│   ├── middleware/
│   │   └── logging.py
│   │
│   └── tests/
│       ├── test_errors.py
│       └── test_logging.py
│
├── pyproject.toml
└── README.md

Features Implemented
1. Centralized Error Handling

Global exception handlers are implemented for:

HTTP Code	Description
400	Request validation errors
401	Unauthorized
403	Forbidden
404	Not Found
409	Conflict
500	Internal Server Error

All error responses return a consistent JSON structure:

{
  "error": "Error message",
  "trace_id": "uuid"
}

2. Structured JSON Logging

Every request is logged in JSON format with the following fields:

level

timestamp

path

method

status_code

user

trace_id

duration

error (only for failures)

Example log:

{
  "level": "INFO",
  "timestamp": "2026-01-02T14:44:05",
  "path": "/health",
  "method": "GET",
  "status_code": 200,
  "user": "anonymous",
  "trace_id": "8791d81b-b3bc-4a30-b4ba-166fa664faf2",
  "duration": 0.0032
}

3. Request Correlation ID

A unique trace_id is generated per request

Stored in request.state.trace_id

Automatically included in:

Logs

Error responses

Enables full request tracing across logs

API Endpoints
Health Check
GET /health


Response:

{
  "status": "ok"
}

Crash Endpoint (Testing 500 Errors)
GET /crash


Purpose:

Intentionally raises an exception

Used to verify 500 error handling and logging

Running the Application
uvicorn src.main:app --reload


Open in browser:

http://127.0.0.1:8000/health

http://127.0.0.1:8000/openapi.json

Running Tests
Set PYTHONPATH (Windows PowerShell)
$env:PYTHONPATH="D:\PYTHON\Week11"
pytest src/tests/

Expected Result

All tests pass

Error handlers validated

Logging middleware verified

Coverage ≥ 43%

Testing Strategy
test_errors.py

400 validation errors

404 not found

500 internal server error

Ensures standardized error responses

test_logging.py

Verifies logs are generated

Ensures JSON fields exist

Confirms correlation ID usage

Acceptance Criteria Checklist

Centralized exception handling implemented

JSON structured logs

Correlation IDs present in logs and responses

Test coverage above required threshold

Sample logs included

Clean architecture followed