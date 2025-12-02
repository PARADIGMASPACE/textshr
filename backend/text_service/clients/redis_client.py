import json
import logging
from typing import Optional

from .redis_factory import create_RedisSettings

logger = logging.getLogger(__name__)


class RedisClient:
    def __init__(self):
        self.redis = create_RedisSettings()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def set(self, key: str, value: dict, ttl: Optional[int] = None):
        data = json.dumps(value)
        try:
            await self.redis.set(name=key, value=data, ttl=ttl )
            logger.info(f"SET {key} -> {data}")
        except Exception as e:
            raise f"Redis SET error key={key}: {e}"

    async def get(self, key: str) -> dict:
        try:
            data = await self.redis.get(key)
            logger.info(f"GET key={key}")
            data = json.loads(data)
            return data

        except Exception as e:
            raise f"Redis GET error key={key}: {e}"

    async def update(self, key: str, value: dict, ttl: Optional[int] = None):
        try:
            exists = await self._exists(key)
            if exists:
                await self.redis.delete(key)
                await self.redis.set(name=key, value=value, ttl=ttl)
                logger.info(f"UPDATE {key} -> {value}")
                return True
            return False
        except Exception as e:
            raise f"Redis UPDATE error key={key}: {e}"


    async def delete(self, key: str):
        try:
            exists = await self._exists(key)
            if exists:
                await self.redis.delete(key)
                logger.info(f"DELETE key={key}")
                return True
            return False

        except Exception as e:
            raise f"Redis DELETE error key={key}: {e}"

    async def _exists(self, key: str) -> bool:
        try:
            exists = await self.redis.exists(key)
            logger.info(f"EXISTS key={key} exists={exists}")
            return exists

        except Exception as e:
            raise f"Redis EXISTS error key={key}: {e}"

    async def ping(self) -> bool:
        try:
            response = await self.redis.ping()
            logger.info(f"PING success={response}")
            return True if response == "PONG" else False

        except Exception as e:
            logger.error(f"Redis PING failed: {e}")
            return False

    async def close(self):
        await self.redis.close()
        await self.redis.connection_pool.disconnect()
        logger.info("Close Redis connection")


text_client = RedisClient()