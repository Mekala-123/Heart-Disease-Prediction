Week 3 – Clean Architecture & Configuration)
# Week 3 – Clean Architecture & Configuration (FastAPI)

🧹 What is Clean Architecture? (Simple Explanation)

Clean Architecture is a way of organizing your code so that:

✅ Your project is clean
✅ Easy to understand
✅ Easy to test
✅ Easy to change
✅ Easy to extend

This week focuses on refactoring the Week 1–2 FastAPI project into a **clean architecture** structure, separating routers, services, and repositories.  
You will also implement **environment-based configuration** and **structured JSON logging**.

---

## 🚀 Project Overview

### **Clean Architecture Layers**


Routers → Services → Repositories


- **Routers** → only handle HTTP requests/responses  
- **Services** → contain business logic  
- **Repositories** → handle data access (in-memory for this week)

### **Environment Configurations**
Using `pydantic-settings` with three environment files:


- `.env.dev` → for local development  
- `.env.test` → for testing  
- `.env.prod` → for production  


---

## 📁 Project Structure



project/
├─ app/
│ ├─ main.py
│ ├─ api/
│ │ └─ sample_router.py
│ ├─ services/
│ │ └─ sample_service.py
│ ├─ repositories/
│ │ └─ sample_repo.py
│ ├─ core/
│ │ ├─ config.py
│ │ └─ logging.py
│ └─ schemas/
│ └─ sample.py
├─ tests/
│ ├─ test_services/
│ │ └─ test_sample_service.py
│ └─ test_repositories/
│ └─ test_sample_repo.py
├─ .env.dev
├─ .env.test
├─ .env.prod
└─ README.md


---

## 🛠️ Installation & Setup

### **1️⃣ Create virtual environment & activate**


python -m venv venv
venv\Scripts\activate # Windows


### **2️⃣ Install dependencies**


pip install -r requirements.txt


---

## ▶️ How to Run the Project

### **Select an environment**

#### DEV:


set ENVIRONMENT=dev
uvicorn app.main:app --reload


#### TEST:


set ENVIRONMENT=test
uvicorn app.main:app --reload


#### PROD:


set ENVIRONMENT=prod
uvicorn app.main:app --reload


### Check environment:
Open browser:

👉 http://127.0.0.1:8000/env

---

## 🌍 API Documentation (Swagger)

After the server runs, open:

👉 **http://localhost:8000/docs**  
👉 **http://localhost:8000/redoc**

---

## 🧩 Core Features Implemented in Week 3

### ✅ 1. **Clean Architecture Refactor**
- Routers moved to `app/api/`
- Services created in `app/services/`
- Repositories created in `app/repositories/`
- No business logic in routers (router → service → repo)

---

### ✅ 2. **Environment-Based Settings**

Using **pydantic-settings**:

- `.env.dev` → for local development  
- `.env.test` → for testing  
- `.env.prod` → for production  

Loaded dynamically based on:


ENVIRONMENT=dev/test/prod


API example:


GET /env → {"environment": "dev"}


---

### ✅ 3. **JSON Logging**

`app/core/logging.py` includes JSON log formatter (Week 3 requirement).

---

### ✅ 4. **Unit Tests Added**
- Service tests in `tests/test_services/`
- Repository tests in `tests/test_repositories/`
- Total coverage ≥ 18% (Week 3 requirement)

---

## 🧪 Example Endpoints

### ✔ GET `/sample/{id}`
Returns sample by ID using service → repository.

### ✔ POST `/sample`
Creates an item using service → repository.

### ✔ GET `/health`


{"status": "ok"}


### ✔ GET `/version`


{"version": "1.0.0"}


### ✔ GET `/env`
Shows currently active environment.

---

## 🔀 Git Branching Rules

- Use branch: **`refactor/clean-architecture`**
- Meaningful commits
- Create Pull Request with:
  - Description of changes
  - Screenshots of Swagger UI
  - Settings explanation
  - Confirmation: **“No business logic in routers”**

---

## 🏁 Week 3 Acceptance Criteria

✔ All routes use the service layer  
✔ Zero business logic in routers  
✔ Environment-based config working  
✔ Logging added  
✔ Tests ≥ 18% coverage  
✔ PR created → reviewed → merged  