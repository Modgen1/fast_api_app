import os
from pydantic_settings import BaseSettings, SettingsConfigDict
# docker-compose down --volumes


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    PGDATA: str
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )


settings = Settings()
