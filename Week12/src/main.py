from fastapi import FastAPI
from src.api.health import router as health_router

app = FastAPI(title="Week 12 Testing Discipline")

app.include_router(health_router)
