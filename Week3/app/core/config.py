from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    environment: str = "dev"   # default value

    model_config = SettingsConfigDict(
        env_file=".env.dev",
        env_file_encoding="utf-8"
    )

def get_settings():
    env = os.getenv("ENVIRONMENT", "dev")  # read terminal ENVIRONMENT variable

    # choose correct file
    env_file = f".env.{env}"

    # load settings from correct file
    return Settings(_env_file=env_file)
