"""
This file contains the database connection and session creation.
"""
import os

import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import OperationalError


def get_db_connection():
    """
    Get the database connection

    :return: database connection
    """
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME", "postgres"),
        user=os.getenv("DB_USERNAME", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        cursor_factory=RealDictCursor
    )

    return conn


def check_database_connection() -> bool:
    """
    Check the database connection

    :return: True if the connection is successful, False otherwise
    """
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        connection.close()
        return True
    except OperationalError:
        return False
