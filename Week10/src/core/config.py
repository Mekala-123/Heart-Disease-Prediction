# src/core/config.py
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """
    Application settings using Pydantic BaseSettings.
    Supports environment variables via .env file.
    """

    # Environment
    ENV: str = "development"

    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]

    # Rate limiting (sliding window)
    RATE_LIMIT_REQUESTS: int = 5       # limit for testing
    RATE_LIMIT_WINDOW: int = 60        # seconds

    # Request size limit
    MAX_REQUEST_SIZE: int = 10_000  # 100 KB, smaller than test payload to trigger 413

    # Secrets
    SECRET_KEY: str = "change-me"

    # Pydantic v2 config
    model_config = {
        "env_file": ".env",
        "case_sensitive": True
    }


# Instantiate global settings object
settings = Settings()
