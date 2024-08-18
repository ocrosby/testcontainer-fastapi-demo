"""
This module contains the common fixtures that can be reused across different features.
"""
import os
import pytest
import docker

from testcontainers.core.waiting_utils import wait_for_logs
from testcontainers.core.container import DockerContainer
from testcontainers.postgres import PostgresContainer

from tests.bdd.fixtures.testcontainers import db


POSTGRES_IMAGE = "postgres:12.19"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "test_password"
POSTGRES_DATABASE = "test_database"
POSTGRES_CONTAINER_PORT = 5432


@pytest.fixture
def app_running(scope="session"):
    # Start the FastAPI application using TestContainers with a custom Dockerfile
    container = DockerContainer("demo-fastapi")
    container.with_exposed_ports(8000)
    container.with_command("uvicorn main:app --host 0.0.0.0 --port 8000 --reload")
    container.with_dockerfile("Dockerfile")


# @pytest.fixture(scope="session")
# def postgress_container() -> PostgresContainer:
#     """
#     Set up the Postgres container
#     :return:
#     """
#     postgres = PostgresContainer(
#         image=POSTGRES_IMAGE,
#         user=POSTGRES_USER,
#         password=POSTGRES_PASSWORD,
#         dbname=POSTGRES_DATABASE,
#         port=POSTGRES_CONTAINER_PORT,
#     )
#
#     with postgres:
#         wait_for_logs(
#             postgres,
#             r"UTC \[1\]: LOG:  database system is ready to accept",
#             timeout=5,  # number of seconds to wait for the predicate to be fulfilled
#             interval=0.1,  # interval between checks (in seconds)
#         )
#         yield postgres


@pytest.fixture
def app_not_running():
    """
    This fixture ensures the application is not running.

    :return:
    """
    # Setup code to ensure the application is not running
    yield
    # Teardown code if necessary


@pytest.fixture
def app_degraded_state():
    """
    This fixture ensures the application is in a degraded state.

    :return:
    """
    # Setup code to put the application in a degraded state
    yield
    # Teardown code to restore the application state


@pytest.fixture
def app_heavy_load():
    """
    This fixture ensures the application is running under heavy load.

    :return:
    """
    # Setup code to put the application under heavy load
    yield
    # Teardown code to restore the application state


@pytest.fixture
def db_available():
    """
    This fixture ensures the database is available.

    :return:
    """
    # Setup code to ensure the database is available
    yield
    # Teardown code to disconnect from the database


@pytest.fixture
def db_not_available():
    """
    This fixture puts the database in a not available state.

    :return:
    """
    # Setup code to ensure the database is not available
    yield
    # Teardown code if necessary


@pytest.fixture
def db_degraded_state():
    """
    This fixture puts the database in a degraded state.

    :return:
    """
    # Setup code to put the database in a degraded state
    yield
    # Teardown code to restore the database state


@pytest.fixture
def request_response():
    """
    This fixture returns a request and response object.

    :return:
    """
    return {"request": None, "response": None}
