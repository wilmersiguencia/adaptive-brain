from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DATABASE: str

    REDIS_HOST: str
    REDIS_PORT: int

    SECRET_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()