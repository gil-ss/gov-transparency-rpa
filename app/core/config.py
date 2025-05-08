"""App configuration and environment loading."""

from pydantic import BaseSettings

class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    # Add your environment variables here
    BASE_URL: str = "https://portaldatransparencia.gov.br"

settings = Settings()
