from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str

    REDIS_HOST: str
    REDIS_PORT: int

    SECRET_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()