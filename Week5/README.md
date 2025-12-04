Week 5 – MongoDB Integration

This project demonstrates how to integrate MongoDB with a FastAPI application using the asynchronous Motor driver. It follows a clean, production-ready structure using repositories, routers, models, and schemas. The application exposes full CRUD operations backed by MongoDB and is organized in a way that supports scalability, testing, and maintenance.

Overview

The primary goal of this project is to build a modular FastAPI backend where:

MongoDB acts as the database.

Motor provides asynchronous database access.

FastAPI handles routing and API responses.

Repository pattern separates database logic from API logic.

Pydantic models validate the request and response bodies.

Environment variables store database configuration.

This architecture is suitable for real-world backend systems and can be extended with authentication, additional collections, or business logic.

Project Structure
Week5/
├── app/
│   ├── main.py                    # FastAPI app entry point
│   ├── core/
│   │   ├── config.py              # Settings / environment variables
│   │   └── db.py                  # MongoDB connection
│   ├── models/
│   │   └── item.py                # Pydantic model for request validation
│   ├── repositories/
│   │   └── item_repo_mongo.py     # MongoDB CRUD operations
│   ├── routers/
│   │   └── item_router.py         # API endpoints
│   ├── schemas/
│   │   └── item_schema.py         # MongoDB response schema
│   ├── tests/
│   │   └── test_item_repo.py      # Repository layer tests
│   └── utils/
│       └── oid.py                 # ObjectId utility functions
├── pyproject.toml
├── requirements.txt
└── .env


This structure ensures the application remains organized, testable, and easy to expand.

Requirements and Installation
Prerequisites

Python 3.10+

MongoDB (local or via Docker)

Virtual environment (recommended)

Install dependencies:

pip install -r requirements.txt

Environment Variables

The .env file stores your MongoDB configuration:

MONGO_URI=mongodb://localhost:27017
MONGO_DB=chartflow_dev


config.py loads these values into the application settings.

MongoDB Setup
Option 1: Local MongoDB

If MongoDB is installed on your system:

net start MongoDB

Option 2: Docker-based MongoDB
docker run -p 27017:27017 -d --name week5-mongo mongo:6.0


This command pulls and runs MongoDB inside a container.

Running the FastAPI Application

Start the backend server using Uvicorn:

uvicorn app.main:app --reload


You can now access:

Interactive API documentation: http://127.0.0.1:8000/docs

Alternative API documentation: http://127.0.0.1:8000/redoc

Home route: http://127.0.0.1:8000/

API Features

The Item module provides the following operations:

Create a new item
POST /items/


Adds a new document to the MongoDB collection.

Get an item by ID
GET /items/{id}


Retrieves a single item using its MongoDB ObjectId.

Get all items
GET /items/


Returns a list of all items.

Update an item
PUT /items/{id}


Updates existing data in the MongoDB document.

Delete an item
DELETE /items/{id}


Removes a document from the database.

All endpoints return JSON responses.

Testing

Test cases are located under:

app/tests/test_item_repo.py


Run tests:

pytest


These tests validate the repository layer, ensuring CRUD operations work correctly and independently from the API.