from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://library_user:admin@localhost/library_db"
    class Config:
        env_file = ".env"
settings = Settings()
