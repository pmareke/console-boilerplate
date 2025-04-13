from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    logger_name: str = "console"


settings = Settings()
