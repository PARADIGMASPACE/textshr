from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class RedisSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str
    REDIS_DB: int


@lru_cache()
def get_redis_settings() -> RedisSettings:
    return RedisSettings()