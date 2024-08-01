"""
This module is responsible for reading the environment variables from the .env file.
"""

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    This class is responsible for reading the environment variables from the .env file.
    """
    app_name: str = "FastAPI Demo Application"
    admin_email: str = "omar.crosby@gmail.com"
    database_url: str

    class Config:
        """
        This class is responsible for reading the environment variables
        from the .env file.
        """
        env_file = ".env"


settings = Settings()
