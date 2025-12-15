import json
import logging
from typing import  Optional
import redis.asyncio
from .redis_factory import create_redis_client

logger = logging.getLogger(__name__)
redis_client = create_redis_client()



async def set(key: str,value: dict,ttl : Optional[int] = None):
    data = json.dumps(value)
    try:
        await redis_client.set(name=key,value = data,  ex=ttl)
        logger.info(f"Redis set {key} -> {data}")
    except Exception as e:
        logger.error(f"Redis Set eror key={key}: {e}")
        raise Exception(f"Redis Set error key={key}: {e}")

async def get(key: str) -> Optional[dict]:
    try:
        data = await redis_client.get(key)
        if not data:
            logger.warning(f"Redis get {key} -> NOt found")
            return None
        logger.info(f"Redis get ={key}")
        data = json.loads(data)
        return data
    except Exception as e:
        logger.error(f"Redis GET error key={key}: {e}")
        raise Exception(f"Redis Get error key={key}: {e}")


async def delete(key: str):
    try:
        result = await redis_client.delete(key)
        logger.info(f"Redis Delete {key} -> {result}")
        return result
    except Exception as e:
        logger.error(f"Redis Delete error key={key}: {e}")
        raise Exception(f"Redis Delete error key={key}: {e}")

async def exists (key: str) -> bool:
    try:
        exists = await redis_client.exists(key)
        logger.info(f"Redis exists {key} -> {exists}")
        return bool(exists)
    except Exception as e:
        logger.error(f"Redis Exists error key={key}: {e}")
        raise Exception(f"Redis Exists error key={key}: {e}")

async def update (key: str,value: dict,ttl : Optional[int] = None):
    await set(key,value,ttl)

    async def close(self):
        try:
            await self.redis.close()
            logger.info("Redis connection closed")
        except Exception as e:
            logger.error(f"Redis close error: {e}")

