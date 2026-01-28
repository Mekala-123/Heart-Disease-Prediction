from fastapi import FastAPI
from app.api.routers import user

app = FastAPI(title="Week 13 Async & Concurrency")

app.include_router(user.router, prefix="/api/users", tags=["Users"])
