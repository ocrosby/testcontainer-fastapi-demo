"""
This file contains the database connection and session creation.
"""
import os

import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import OperationalError
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from app.core.logging import logger
from app.core.config import settings


def create_database():
    """
    Create the database if it does not exist
    """
    conn = psycopg2.connect(
        dbname="postgres",
        user=settings.db_username,
        password=settings.db_password,
        host=settings.db_host,
        port=settings.db_port
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{settings.db_name}'")
    exists = cur.fetchone()
    if not exists:
        logger.info(f"Database {settings.db_name} does not exist")
        logger.info(f"Creating database {settings.db_name}")
        cur.execute(f"CREATE DATABASE {settings.db_name}")
        logger.info(f"Database {settings.db_name} created")
    else:
        logger.info(f"Database {settings.db_name} already exists")

    cur.close()
    conn.close()


def get_db_connection():
    """
    Get the database connection

    :return: database connection
    """
    settings.db_name = os.environ.get("DB_NAME", settings.db_name)
    settings.db_username = os.environ.get("DB_USERNAME", settings.db_username)
    settings.db_password = os.environ.get("DB_PASSWORD", settings.db_password)
    settings.db_host = os.environ.get("DB_HOST", settings.db_host)
    settings.db_port = os.environ.get("DB_PORT", settings.db_port)

    logger.info("Creating database connection")
    logger.info(f"DB_NAME: {settings.db_name}")
    logger.info(f"DB_USERNAME: {settings.db_username}")
    logger.info(f"DB_PORT: {settings.db_port}")
    logger.info(f"DB_HOST: {settings.db_host}")

    # Ensure the database exists
    create_database()

    conn = psycopg2.connect(
        dbname=settings.db_name,
        user=settings.db_username,
        password=settings.db_password,
        host=settings.db_host,
        port=settings.db_port,
        cursor_factory=RealDictCursor
    )

    return conn


def check_database_connection() -> bool:
    """
    Check the database connection

    :return: True if the connection is successful, False otherwise
    """
    logger.info("Checking database connection")
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        connection.close()
        logger.info("Database connection successful")
        return True
    except OperationalError as err:
        logger.error("Database connection failed")
        logger.error(err)
        return False
