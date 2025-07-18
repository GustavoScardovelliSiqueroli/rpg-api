from decimal import Decimal
from functools import lru_cache

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    START_DAY: int = 0
    START_HOUR: int = 0

    START_PRODUCTIVITY: float = 100
    START_ENERGY: int = 10
    START_MONEY: Decimal = Decimal(1000.0)
    START_NETWORK: Decimal = Decimal(0)

    DB_USER: str = 'root'
    DB_PASSWORD: str = ''
    DB_HOST: str = 'localhost'
    DB_NAME: str = 'fastapi'
    MYSQL_ROOT_PASSWORD: str = '123'
    MYSQL_DATABASE: str = 'rpg'
    MYSQL_USER: str = 'dev'
    MYSQL_PASSWORD: str = '123'
    DB_PORT: int = 3306
    API_KEY: str = 'apikeydev'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    def get_db_url_alembic(self) -> str:
        return f'mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


@lru_cache()
def get_settings() -> Config:
    return Config()
