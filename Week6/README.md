Week6 - Item API
Project Overview

This project implements a simple Item Management API using FastAPI, demonstrating:

Service layer and business logic orchestration

Repository pattern for data access

DTO (Data Transfer Object) mapping between API, service, and repository

Custom error handling mapped to HTTP status codes

CRUD operations: Create, Read, Update, Delete

The API supports in-memory storage for simplicity but is structured for easy integration with a database.

Features

Create Item (POST /items/)
Validates uniqueness of item name and returns ItemResponseDTO with an auto-generated id.

List Items (GET /items/)
Returns all items stored in memory.

Get Item (GET /items/{item_id})
Retrieves an item by its ID. Returns 404 Not Found if the item does not exist.

Update Item (PUT /items/{item_id})
Updates an item’s name and/or description. Returns 404 Not Found if the item does not exist.

Delete Item (DELETE /items/{item_id})
Deletes an item by ID. Returns 404 Not Found if the item does not exist.

Error Handling
Custom service errors mapped to HTTP status codes:

NotFoundError → 404 Not Found

ConflictError → 409 Conflict

ValidationError → 422 Unprocessable Entity

Folder Structure
Week6/
├── main.py                   # FastAPI app entry point
├── src/
│   ├── api/
│   │   └── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── errors.py         # Custom error classes
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── item_repository.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── item_dto.py       # DTO classes
│   ├── services/
│   │   ├── __init__.py
│   │   └── item_service.py   # Business logic
│   └── routers/
│       ├── __init__.py
│       └── item_router.py    # FastAPI routes
├── tests/
│   └── test_item_service.py  # Unit tests for service layer
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation

DTOs (Schemas)

ItemCreateDTO: Input for creating an item

name (str) – required

description (str) – optional

ItemUpdateDTO: Input for updating an item

name (str) – optional

description (str) – optional

ItemResponseDTO: Response returned by API

id (int) – auto-generated

name (str)

description (str)

Running the Project

Clone the repository

git clone <repository-url>
cd Week6


Create a virtual environment and activate it

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Run the FastAPI app

uvicorn main:app --reload


Access Swagger UI
Open http://127.0.0.1:8000/docs
 to test endpoints interactively.

Testing

Run tests using pytest

pytest --cache-clear


Coverage

Ensure service layer has coverage ≥ 28% (as per Week6 KPIs).

Error Handling
Error	HTTP Status	Description
NotFoundError	404	Item not found
ConflictError	409	Duplicate item name
ValidationError	422	Input validation failed
API Endpoints Summary
Method	Endpoint	Description
POST	/items/	Create a new item
GET	/items/	List all items
GET	/items/{id}	Get item by ID
PUT	/items/{id}	Update item
DELETE	/items/{id}	Delete item
Notes

This project uses in-memory storage for demonstration.

Designed following clean architecture: routers → services → repositories.

Custom errors are mapped to proper HTTP responses for clear API communication.