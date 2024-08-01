import pytest

from app.core.database import check_database_connection


@pytest.mark.integration
def test_database_connection(postgres_container):
    assert check_database_connection() is True
