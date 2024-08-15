"""
This module contains the common fixtures that can be reused across different features.
"""
import os
import pytest
import docker

from fastapi.testclient import TestClient

from testcontainers.core import utils
from testcontainers.core.waiting_utils import wait_for_logs
from testcontainers.core.container import DockerContainer
from testcontainers.postgres import PostgresContainer

from app.main import api

from pytest_bdd import scenario

from app.utils.filesystem import find_root_dir
from testcontainers.core.container import DockerContainer

from tests.bdd.step_definitions.common_steps import *
from tests.bdd.step_definitions.liveness_steps import *


POSTGRES_IMAGE = "postgres:12.19"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "test_password"
POSTGRES_DATABASE = "test_database"
POSTGRES_CONTAINER_PORT = 5432


@pytest.fixture(scope="module", autouse=True)
def app_container():
    # Create a container from the Dockerfile at the root of the project
    # Start the container

    root_dir = find_root_dir(__file__)  # Find the root directory of the project

    dockerfile_path = os.path.join(root_dir, "Dockerfile")  # Path to the Dockerfile

    # Use the Docker SDK to build the image
    client = docker.from_env()
    image, _ = client.images.build(path=root_dir, dockerfile=dockerfile_path, tag="demo-fastapi:latest")

    # Run the container using testcontainers
    container = DockerContainer(image.id)

    container.with_exposed_ports(80)  # Expose the necessary ports

    # Start the container
    container.start()

    # Yield the container for use in tests
    yield container

    # Stop the container
    container.stop()


def get_session():
    pass


def initialize_test_db(engine):
    pass


@pytest.fixture
def app_running(scope="session"):
    # Start the FastAPI application using TestContainers with a custom Dockerfile
    container = DockerContainer("demo-fastapi")
    container.with_exposed_ports(8000)
    container.with_command("uvicorn main:app --host 0.0.0.0 --port 8000 --reload")
    container.with_dockerfile("Dockerfile")


@pytest.fixture(scope="session")
def postgress_container() -> PostgresContainer:
    """
    Set up the Postgres container
    :return:
    """
    postgres = PostgresContainer(
        image=POSTGRES_IMAGE,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        dbname=POSTGRES_DATABASE,
        port=POSTGRES_CONTAINER_PORT,
    )

    with postgres:
        wait_for_logs(
            postgres,
            r"UTC \[1\]: LOG:  database system is ready to accept",
            timeout=5,  # number of seconds to wait for the predicate to be fulfilled
            interval=0.1,  # interval between checks (in seconds)
        )
        yield postgres


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
