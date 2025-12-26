from fastapi import FastAPI
from src.api.items import router as items_router

app = FastAPI(title="Week 9 - Redis Caching")

app.include_router(items_router)

@app.get("/")
def health_check():
    return {"status": "ok"}
