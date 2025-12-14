import yaml
from pydantic_settings import BaseSettings

from core.constants import CONFIG_PATH


class ApiConfig(BaseSettings):
    title: str
    description: str
    version: str
    port: int
    host: str


class RedisConfig(BaseSettings):
    connection_url: str
    max_connections: int


class Config(BaseSettings):
    api: ApiConfig
    redis: RedisConfig

def _get_config() -> Config:
    with open(CONFIG_PATH) as f:
        _config = Config.model_validate(yaml.load(f, Loader=yaml.FullLoader))

    return _config

config = _get_config()