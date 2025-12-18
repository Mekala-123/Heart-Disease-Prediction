# src/main.py

from fastapi import FastAPI
#from api.auth import router as auth_router
from src.api.auth import router as auth_router

app = FastAPI(title="Week 7 - JWT Authentication")

# Simple GET route
@app.get("/")
def home():
    return {"message": "Week 7 Authentication API is running!"}

# Include authentication routes
app.include_router(auth_router)