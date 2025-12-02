import redis.asyncio as redis
from ..config import RedisSettings

def create_RedisSettings():
    settings = RedisSettings()
    return redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        password=settings.REDIS_PASSWORD,
        decode_responses=True
    )
