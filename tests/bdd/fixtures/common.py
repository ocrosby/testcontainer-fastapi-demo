"""
This module contains the common fixtures that can be reused across different features.
"""
import pytest


@pytest.fixture(scope="function")
def context():
    """
    This fixture returns a context object.

    :return:
    """
    return {
        "request": None,
        "response": None,
        "errors": [],
    }
