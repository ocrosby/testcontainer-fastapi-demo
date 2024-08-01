"""
This file contains the database connection and session creation.
"""
import os

import psycopg2
from psycopg2.extras import RealDictCursor


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
