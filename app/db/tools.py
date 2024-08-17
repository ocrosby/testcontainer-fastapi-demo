"""
This module contains tools for database operations.
"""

import os

from sqlalchemy import create_engine, inspect


def table_exists(table_name):
    """
    Check if a table exists in the database.

    :param table_name: Name of the table to check
    :return: True if the table exists, False otherwise
    """
    engine = create_engine(os.environ["DB_CONN"])
    inspector = inspect(engine)
    table_names = inspector.get_table_names()
    engine.dispose()
    return table_name in table_names
