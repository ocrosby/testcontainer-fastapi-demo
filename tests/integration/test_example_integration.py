import pytest

from app.db.tools import table_exists
from app.core.database import check_database_connection
from tests.bdd.fixtures.testcontainers import database


@pytest.mark.integration
def test_database_connection(database):
    assert check_database_connection(), "Database connection failed"


@pytest.mark.integration
def test_addresses_table_exists(database):
    assert table_exists("addresses"), "Table 'addresses' does not exist"


@pytest.mark.integration
def test_cities_table_exists(database):
    assert table_exists("cities"), "Table 'cities' does not exist"


@pytest.mark.integration
def test_countries_table_exists(database):
    assert table_exists("countries"), "Table 'countries' does not exist"


@pytest.mark.integration
def test_posts_table_exists(database):
    assert table_exists("posts"), "Table 'posts' does not exist"


@pytest.mark.integration
def test_states_table_exists(database):
    assert table_exists("states"), "Table 'states' does not exist"


@pytest.mark.integration
def test_users_table_exists(database):
    assert table_exists("users"), "Table 'users' does not exist"
