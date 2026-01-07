from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import BaseModel
import uuid

from src.api.health import router as health_router
from src.middleware.logging import LoggingMiddleware
from src.core.errors import (
    http_exception_handler,
    validation_exception_handler,
    internal_exception_handler,
)

app = FastAPI(title="Week 11 Error Handling & Logging")

# ---------------------------
# Middleware
# ---------------------------
app.add_middleware(LoggingMiddleware)

# ---------------------------
# Routers
# ---------------------------
app.include_router(health_router)

# ---------------------------
# Exception handlers
# ---------------------------
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, internal_exception_handler)

# ---------------------------
# Test Endpoints for Week 11
# ---------------------------
@app.post("/validate")
def validate_input(data: BaseModel):
    """Trigger 400 Validation Error"""
    return {"message": "Valid input"}


@app.get("/unauthorized")
def unauthorized():
    """Trigger 401 Unauthorized"""
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Unauthorized access"
    )


@app.get("/forbidden")
def forbidden():
    """Trigger 403 Forbidden"""
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Forbidden"
    )


@app.get("/conflict")
def conflict():
    """Trigger 409 Conflict"""
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Resource already exists"
    )


@app.get("/crash")
def crash():
    """Trigger 500 Internal Server Error"""
    1 / 0  # force exception
