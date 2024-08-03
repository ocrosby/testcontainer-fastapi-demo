"""
This module is responsible for reading the environment variables from the .env file.
"""
import sys

from pydantic import ValidationError
from pydantic_settings import BaseSettings

from app.config.logging import logger


class Settings(BaseSettings):
    """
    This class is responsible for reading the environment variables from the .env file.
    """
    host: str = "0.0.0.0"
    port: int = 8000
    app_name: str = "FastAPI Demo Application"
    admin_email: str = "omar.crosby@gmail.com"
    # database_url: str
    summary: str = "This is a demo FastAPI application"
    description: str = """
    This is a demo FastAPI application, intended to be used as a template for new projects.

    ## Posts

    You can **read posts**
    """

    contact: dict[str, str] = {
        "name": "Omar Crosby",
        "email": "omar.crosby@gmail.com",
    }

    license_info: dict[str, str] = {
        "name": "MIT",
        "identifier": "MIT",
    }

    tag_metadata: list[dict[str, str]] = [
        {
            "name": "kubernetes",
            "description": "Operations related to Kubernetes",
        },
        {
            "name": "posts",
            "description": "Operations related to posts",
        },
    ]

    def __init__(self):
        """
        Initialize the Settings class
        """
        super().__init__()

        version = "0.0.0"

        try:
            with open("VERSION", "r", encoding="utf-8") as version_file:
                version = version_file.read().strip()
        except FileNotFoundError:
            logger.warning("VERSION file not found, using default version '0.1.0'")
        finally:
            self.version = version

    class Config:
        """
        This class is responsible for reading the environment variables
        from the .env file.
        """
        env_file = ".env"


try:
    settings = Settings()
except ValidationError as e:
    logger.error(f"Error reading environment variables: {e}")
    sys.exit(1)
