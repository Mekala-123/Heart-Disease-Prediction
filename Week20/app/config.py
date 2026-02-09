from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "week20-cloud-service"
    ENV: str = "dev"
    LOG_LEVEL: str = "INFO"

    model_config = ConfigDict(env_file=".env")

settings = Settings()
