"""
This module contains the functions to get the Postgres connection DSN and connection.
"""

import os

import psycopg2 as psycopg


def get_connection_dsn() -> str:
    """
    Get the Postgres connection DSN

    :return: Postgres connection DSN
    """
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    username = os.getenv("DB_USERNAME", "postgres")
    password = os.getenv("DB_PASSWORD", "postgres")
    database = os.getenv("DB_NAME", "postgres")

    dsn = f"host={host} port={port} user={username} password={password} dbname={database}"

    return dsn


def get_connection():
    """
    Get the Postgres connection

    :return: Postgres connection
    """
    dsn = get_connection_dsn()
    connection = psycopg.connect(dsn)

    return connection
