import pytest

from app.core.database import check_database_connection


@pytest.mark.integration
def test_database_connection(db):
    assert check_database_connection(), "Database connection failed"
