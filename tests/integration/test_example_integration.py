import pytest

from app.db.tools import table_exists
from app.core.database import check_database_connection


@pytest.mark.integration
def test_database_connection(db):
    assert check_database_connection(), "Database connection failed"
    assert table_exists("addresses"), "Table 'addresses' does not exist"
    assert table_exists("cities"), "Table 'cities' does not exist"
    assert table_exists("countries"), "Table 'countries' does not exist"
    assert table_exists("posts"), "Table 'posts' does not exist"
    assert table_exists("states"), "Table 'states' does not exist"
    assert table_exists("users"), "Table 'users' does not exist"
