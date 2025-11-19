from fastapi import FastAPI
from app.api.sample_router import router as sample_router
from app.core.config import get_settings

app = FastAPI(
    title="Week 3 – Clean Architecture",
    description="Routers → Services → Repositories",
    version="1.0.0"
)

settings = get_settings()  # load current environment

app.include_router(sample_router)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}

@app.get("/env")
def env():
    return {"environment": settings.environment}
