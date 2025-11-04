from fastapi import FastAPI
from src.core.config import settings


def create_app() -> FastAPI:
    """App factory for the FastAPI application."""
    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        description="LHI Base FastAPI App (Local Week 1)",
    )

    @app.get("/health", tags=["Health"])
    async def health_check():
        """Basic health check endpoint"""
        return {"status": "ok"}

    @app.get("/version", tags=["Health"])
    async def get_version():
        """Return version information"""
        return {"version": settings.version}

    return app


# Uvicorn entry point
app = create_app()
