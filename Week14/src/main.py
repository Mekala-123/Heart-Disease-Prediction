from fastapi import FastAPI
from src.api.files import router as file_router

app = FastAPI(title="File Service API")

app.include_router(file_router)
