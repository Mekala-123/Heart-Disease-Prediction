from fastapi import FastAPI, Request
from app.config import settings

app = FastAPI(title=settings.APP_NAME)

REQUEST_COUNT = 0

@app.middleware("http")
async def count_requests(request: Request, call_next):
    global REQUEST_COUNT
    REQUEST_COUNT += 1
    response = await call_next(request)
    return response

@app.get("/health")
def health():
    return {
        "status": "ok",
        "env": settings.ENV
    }

@app.get("/metrics")
def metrics():
    return {
        "requests_total": REQUEST_COUNT
    }
