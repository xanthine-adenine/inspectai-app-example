from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for the API service."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    redis_host: str = "localhost"
    redis_port: int = 6379
    data_volume_path: str = "/usr/local/app/data"

settings = Settings()
