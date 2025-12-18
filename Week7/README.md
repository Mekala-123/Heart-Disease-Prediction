Week 7 – Authentication (JWT)
Overview

This project implements a complete JWT-based authentication system using FastAPI.
It follows the OAuth2 Password Grant flow and supports access tokens, refresh tokens, and protected routes.
The implementation is modular, testable, and aligned with production-ready backend standards.

Learning Goals

Understand OAuth2 password flow

Implement JWT access and refresh tokens

Secure password storage using hashing

Protect API routes using token-based authentication

Tech Stack

Python 3.13

FastAPI

PyJWT

Passlib (bcrypt)

Pytest

Project Structure
Week7/
├── src/
│   ├── main.py
│   ├── api/
│   │   └── auth.py
│   ├── schemas/
│   │   └── user_schema.py
│   ├── services/
│   │   └── auth_service.py
│   ├── core/
│   │   └── security.py
│
├── tests/
│   └── test_auth.py
│
├── README.md
└── requirements.txt

Engineering Tasks Implemented
1. User Schema

Email (unique identifier)

Hashed password

Roles (default: user)

2. Authentication APIs
Method	Endpoint	Description
POST	/auth/register	Register a new user
POST	/auth/login	Authenticate user and issue tokens
POST	/auth/refresh	Refresh access token
GET	/auth/me	Protected route (JWT required)
3. Security

Password hashing using passlib

JWT creation and validation using pyjwt

Access token + refresh token mechanism

Token decoding and expiry validation

Authentication Flow (Sequence Diagram)
Client
  |
  | POST /auth/register (email, password)
  |
Auth Service
  |
  | Password hashed and user stored
  |
Client
  |
  | POST /auth/login (email, password)
  |
Auth Service
  |
  | Validate password
  | Generate access & refresh tokens
  |
Client
  |
  | GET /auth/me (Authorization: Bearer <access_token>)
  |
Auth Service
  |
  | Decode & validate token
  | Return user info

How to Run the Project
1. Create virtual environment
python -m venv venv
venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Run the application
uvicorn src.main:app --reload

4. Open Swagger UI
http://127.0.0.1:8000/docs

Running Tests
pytest -v

Test Coverage

Authentication flow tested

Token validation tested

Coverage ≥ 32% (auth module)

Acceptance Criteria / KPIs

User registration and login work correctly

JWT access and refresh tokens are validated

Protected route /auth/me accessible only with valid token

Test coverage meets minimum requirement

Git & Review Checklist

Feature branch: feature/auth-jwt

Clean commit history

Tests included for auth flows

Sequence diagram included in README

Code follows separation of concerns (API, service, core, schemas)

Notes

This module is designed to be easily extendable for:

Role-based access control (RBAC)

Database integration

Token blacklisting / logout

OAuth providers (Google, GitHub)