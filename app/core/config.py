from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: Optional[str] = "sqlite:///api.db"

    class Config:
        case_sensitive = True


settings = Settings()
