from fastapi import FastAPI
from src.api.items import router as items_router
from src.middleware.security import (
    setup_cors,
    RateLimiterMiddleware,
    RequestSizeLimiterMiddleware,
    SecureHeadersMiddleware,
)

app = FastAPI(title="Week 10 – API Security Hardening")

# Routers
app.include_router(items_router)

# Security middlewares
setup_cors(app)
app.add_middleware(RateLimiterMiddleware)
app.add_middleware(RequestSizeLimiterMiddleware)
app.add_middleware(SecureHeadersMiddleware)

@app.get("/")
def health_check():
    return {"status": "ok"}
