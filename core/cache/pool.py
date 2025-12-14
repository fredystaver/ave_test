from core.config import config
import redis.asyncio as aioredis
from .redis import RedisBaseTypes
from .session import RedisConnectionPoolConfiguration

REDIS_CONNECTION_POOL: dict[int, aioredis.Redis] | None = None


async def init_redis_pool():
    global REDIS_CONNECTION_POOL
    REDIS_CONNECTION_POOL = {}
    for redis_base in RedisBaseTypes:
        redis_pool = await RedisConnectionPoolConfiguration.configure(
            redis_base, config.redis.connection_url
        )
        REDIS_CONNECTION_POOL[redis_base.value] = redis_pool


def get_redis_pool(base: int = RedisBaseTypes.DEFAULT.value) -> aioredis.Redis:
    if REDIS_CONNECTION_POOL is None:
        raise RuntimeError("Redis connection pool not initialized")
    return REDIS_CONNECTION_POOL[base]


async def close_redis_connections():
    global REDIS_CONNECTION_POOL
    for connection in REDIS_CONNECTION_POOL.values():
        await connection.close()
    REDIS_CONNECTION_POOL = None
