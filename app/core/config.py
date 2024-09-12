from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/dts"
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"

    PROJECT_NAME: str = "Pecha API"


settings = Settings()
