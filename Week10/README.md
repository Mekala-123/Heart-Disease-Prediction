Week 10 – API Security Hardening
Overview

This project demonstrates FastAPI API security hardening using best practices such as:

CORS configuration

Redis-based rate limiting

Request size limiting

Secure HTTP headers

Test coverage using pytest

It includes a sample /items/ endpoint for demonstration purposes and a health check endpoint.

Folder Structure
src/
├── api/
│   └── items.py               # Item endpoints (GET, POST)
├── core/
│   ├── config.py              # Configuration using Pydantic BaseSettings
│   └── redis.py               # Redis client setup
├── middleware/
│   └── security.py            # Security middlewares (CORS, rate limiting, size limiter, headers)
├── main.py                    # FastAPI application
tests/
├── test_security.py           # Pytest tests for middleware and endpoints

Features
1. CORS Configuration

Configurable allowed origins via settings.ALLOWED_ORIGINS.

Uses fastapi.middleware.cors.CORSMiddleware.

2. Rate Limiting

Redis-based sliding window implementation.

Configurable via settings.RATE_LIMIT_REQUESTS and settings.RATE_LIMIT_WINDOW.

Returns 429 Too Many Requests when exceeded.

3. Request Size Limiting

Rejects requests exceeding settings.MAX_REQUEST_SIZE.

Returns 413 Request Entity Too Large.

4. Secure Headers

Adds the following headers to all responses:

X-Content-Type-Options: nosniff

X-Frame-Options: DENY

X-XSS-Protection: 1; mode=block

Strict-Transport-Security: max-age=63072000

5. Testing

Uses pytest and fastapi.testclient for automated testing.

Tests include:

Health check endpoint

Secure headers

Request size limit enforcement

Installation

Clone the repository:

git clone <repo-url>
cd Week10


Create a virtual environment and activate it:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Set up Redis (if using rate limiting):

# Windows
redis-server
# Linux/macOS
redis-server --daemonize yes

Configuration

All settings are in src/core/config.py and can be overridden via a .env file.

ENV=development
ALLOWED_ORIGINS=http://localhost:3000
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW=60
MAX_REQUEST_SIZE=100000
SECRET_KEY=change-me

Running the App
uvicorn src.main:app --reload


Access health check: GET / → returns {"status": "ok"}

Access items endpoint:

GET /items/ → list items

POST /items/ → create item (request size limited)

Running Tests
pytest -v


Test results will validate:

Secure headers

Request size limits

Health check


Example Request
POST /items/ HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
  "data": "Hello World"
}
