from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.v1.routes import routes
from core.cache.pool import init_redis_pool, close_redis_connections
from core.config import config

def create_app() -> FastAPI:
    app = FastAPI(
        title=config.api.title,
        description=config.api.description,
        version=config.api.version,
        lifespan=lifespan
    )

    for route in routes:
        app.include_router(route)

    return app


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_redis_pool()
    yield
    await close_redis_connections()
