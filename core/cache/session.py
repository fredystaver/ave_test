import redis.asyncio as aioredis
from redis.asyncio.retry import Retry
from redis.backoff import ExponentialBackoff
from redis.client import Redis

from .redis import RedisBaseTypes
from core.config import config


class RedisConnectionPoolConfiguration:
    _DEFAULT_CONNECTION_PARAMS = {
        "max_connections": config.redis.max_connections,
        "health_check_interval": 10,
        "socket_connect_timeout": 5,
        "retry_on_timeout": True,
        "retry_on_error": [ConnectionError, TimeoutError],
        "retry":  Retry(ExponentialBackoff(), 3)
    }

    @classmethod
    async def configure(cls, redis_base: RedisBaseTypes, url: str) -> Redis:
        kwargs = cls._DEFAULT_CONNECTION_PARAMS
        connection_pool_gen = aioredis.from_url(url, db=redis_base.value, **kwargs)

        return await connection_pool_gen
