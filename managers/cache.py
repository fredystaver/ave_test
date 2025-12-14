from core.cache.pool import get_redis_pool as redis
from core.cache.redis import RedisBaseTypes


class CacheManager:
    @classmethod
    async def get(
            cls,
            key: str,
            base: str | int = RedisBaseTypes.DEFAULT.value
    ) -> str | None:
        return await redis(base).get(key)


    @classmethod
    async def set(
            cls,
            key: str,
            value: str,
            base: str | int = RedisBaseTypes.DEFAULT.value
    ) -> None:
        await redis(base).set(key, value)


    @classmethod
    async def delete(
            cls,
            key: str,
            base: str | int = RedisBaseTypes.DEFAULT.value
    ) -> None:
        await redis(base).delete(key)


    @classmethod
    async def is_exists(
            cls,
            key: str,
            base: str | int = RedisBaseTypes.DEFAULT.value
    ) -> int:
        return await redis(base).exists(key)
