# File Service API – Week 14 (File & Media Handling)

## Overview

This project implements a **secure File & Media Handling API** using **FastAPI**. It supports safe file uploads, controlled downloads, and a clean storage abstraction that can be extended to cloud providers later.

This task is part of **Week 14** and focuses on backend engineering best practices such as validation, separation of concerns, and test coverage.

---

## Features

* Secure file upload with **size and content-type validation**
* Secure file download using **server-generated file identifiers**
* **Storage abstraction layer** (local filesystem now, cloud-ready later)
* Clean **Service–Repository architecture**
* Interactive **Swagger (OpenAPI) documentation**
* Automated tests with **pytest + coverage**

---

## Tech Stack

* Python 3.13
* FastAPI
* Uvicorn
* Pytest + pytest-cov
* httpx
* python-multipart

---

## Project Structure

```
project-root/
│
├── src/
│   ├── main.py
│   │
│   ├── api/
│   │   └── files.py              # API routes
│   │
│   ├── services/
│   │   └── file_service.py       # Business logic
│   │
│   ├── repositories/
│   │   └── file_repo.py          # Storage abstraction
│   │
│   ├── core/
│   │   └── config.py             # Configurations
│   │
│   └── __init__.py
│
├── storage/
│   └── uploads/                  # Stored files (local)
│
├── tests/
│   └── test_files.py             # API tests
│
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```
git clone <repository-url>
cd Week14
```

### 2. Create and Activate Virtual Environment

**Windows**

```
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux**

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install fastapi uvicorn python-multipart pytest pytest-cov httpx
```

---

## Running the Application

From the project root:

```
uvicorn src.main:app --reload
```

Application will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Upload File

**POST** `/files`

* Accepts multipart file upload
* Validates file type and size

Allowed types:

* application/pdf
* image/png
* image/jpeg

Max size:

* 5 MB

**Response Example**

```json
{
  "file_id": "e7c1f2c2-1b5e-4f9b-8c77-8d93c22c1111",
  "stored_name": "e7c1f2c2-1b5e-4f9b-8c77-8d93c22c1111_sample.pdf"
}
```

---

### Download File

**GET** `/files/{stored_name}`

* Downloads a previously uploaded file
* Uses server-generated stored filename

Example:

```
/files/e7c1f2c2-1b5e-4f9b-8c77-8d93c22c1111_sample.pdf
```

---

## Running Tests

Run all tests:

```
pytest
```

Run tests with coverage:

```
pytest --cov=src --cov-report=term
```

### Acceptance Criteria

* File upload & download work correctly
* Invalid files are rejected
* Test coverage ≥ **58%**

---

## Design Decisions

* **Service Layer** handles validation and error translation
* **Repository Layer** abstracts storage and prevents direct filesystem access
* File paths are never exposed to clients
* Ready for cloud storage (S3, Azure Blob, GCP) with minimal changes

---

## Security Considerations

* File type validation
* File size limits
* Path traversal protection
* No client filesystem access

---

## Git Workflow

```
git checkout -b feature/file-service
```

PR checklist:

* Clear commit messages
* Storage decisions documented
* Tests passing
* Coverage ≥ 58%

---

## Future Enhancements

* Signed / expiring download URLs
* Cloud storage adapters (S3, Azure Blob)
* Database-backed file metadata
* Virus scanning

---

## One-Line Summary

A production-ready FastAPI service for secure file upload and download with clean architecture, validation, and test coverage.
