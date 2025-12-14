import uvicorn

from application import create_app
from core.config import config

if __name__ == "__main__":
    uvicorn.run(
        app=create_app(),
        host=config.api.host,
        port=config.api.port,
    )
