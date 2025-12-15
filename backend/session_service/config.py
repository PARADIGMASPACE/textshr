from pydantic import BaseSettings


class RedisSettings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str
    REDIS_DB: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

redis_settings = RedisSettings()
