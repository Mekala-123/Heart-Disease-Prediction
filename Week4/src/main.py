from fastapi import FastAPI
from src.api.items_router import router as items_router

app = FastAPI(
    title="Week 4 - CRUD Module",
    description="Items CRUD + pagination + JSON store",
    version="1.0.0",
)

app.include_router(items_router, prefix="/items", tags=["Items"])


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": "1.0.0"}
