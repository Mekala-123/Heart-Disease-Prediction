# main.py
from fastapi import FastAPI
from src.routers.item_router import router as item_router

app = FastAPI(title="Business Logic Services & DTOs", version="0.1.0")

app.include_router(item_router)
