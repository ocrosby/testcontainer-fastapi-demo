import os

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from app.core.config import settings
from app.core.logging import logger


def check_database_connection() -> bool:
    """
    Check the database connection using SQLAlchemy.

    :return: True if the connection is successful, False otherwise
    """
    # database_url = f"postgresql://{settings.db_username}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
    database_url = os.environ["DB_CONN"]
    engine = create_engine(database_url)

    logger.info("Checking database connection")
    logger.info(f"Database URL: {database_url}")

    try:
        with engine.connect() as connection:
            connection.execute("SELECT 1")
        logger.info("Database connection successful")
        return True
    except OperationalError as err:
        logger.error("Database connection failed")
        logger.error(err)
        return False
