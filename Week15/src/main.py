from fastapi import FastAPI
from src.api.v1.users import router as user_router

app = FastAPI(title="Week 15 Advanced Querying")

app.include_router(user_router, prefix="/api/v1")
