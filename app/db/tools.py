"""
This module contains tools for database operations.
"""

import os

from sqlalchemy import create_engine, inspect

from app.core.logging import logger


def table_exists(table_name):
    """
    Check if a table exists in the database.

    :param table_name: Name of the table to check
    :return: True if the table exists, False otherwise
    """
    database_port = os.environ["DB_PORT"]
    connection_string = os.environ["DB_CONN"]
    engine = create_engine(connection_string)
    inspector = inspect(engine)
    table_names = inspector.get_table_names()
    engine.dispose()

    table_count = len(table_names)

    logger.info(f"Database Port: {database_port}")
    logger.info(f"Connection String: {connection_string}")

    found = False
    if table_count == 0:
        logger.error("No tables found in the database")
    else:
        logger.info(f"Found {table_count} tables in the database")
        logger.info(f"Table names: {table_names}")
        found = table_name in table_names

    return found
