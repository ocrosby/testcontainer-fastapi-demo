import os
import pytest
import docker

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from testcontainers.core.waiting_utils import wait_for_logs
from testcontainers.postgres import PostgresContainer
from testcontainers.core.container import DockerContainer

from app.models.base import Base  # Ensure this imports the Base class from your models

from app.utils.filesystem import find_root_dir

POSTGRES_IMAGE = "postgres:16-alpine"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "test_password"
POSTGRES_DATABASE = "test_database"
POSTGRES_CONTAINER_PORT = 5432
POSTGRES_CONTAINER_NAME = "test_postgres_container"


@pytest.fixture(scope="session")
def postgres_container():
    """
    Set up the Postgres container

    :return: Postgres container
    """
    postgres = PostgresContainer(
        image=POSTGRES_IMAGE,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        dbname=POSTGRES_DATABASE,
        port=POSTGRES_CONTAINER_PORT
    )

    with postgres:
        os.environ["DB_CONN"] = postgres.get_connection_url()
        os.environ["DB_HOST"] = postgres.get_container_host_ip()
        os.environ["DB_PORT"] = postgres.get_exposed_port(5432)
        os.environ["DB_USERNAME"] = postgres.POSTGRES_USER
        os.environ["DB_PASSWORD"] = postgres.POSTGRES_PASSWORD
        os.environ["DB_NAME"] = postgres.POSTGRES_DB

        wait_for_logs(
            container=postgres,
            predicate="database system is ready to accept connections",
            timeout=30,
            interval=2,
        )

        yield postgres

    postgres.stop()


@pytest.fixture(scope="session")
def database(postgres_container):
    """
    Set up the database

    :param postgres_container: Postgres container
    :return: Database
    """
    engine = create_engine(os.environ["DB_CONN"])
    Base.metadata.create_all(engine)  # Create the database structure
    session_factory = sessionmaker(bind=engine)
    session_instance = session_factory()

    yield session_instance

    session_instance.close()
    engine.dispose()


@pytest.fixture(scope="session")
def api_container(database):
    """
    This fixture sets up the FastAPI application using TestContainers with a custom Dockerfile.
    """
    # Find the root directory of the project
    root_dir = find_root_dir(__file__)

    # Get the path to the Dockerfile
    dockerfile_path = os.path.join(root_dir, "Dockerfile")

    # Use the Docker SDK to build the image
    client = docker.from_env()
    image, _ = client.images.build(path=root_dir, dockerfile=dockerfile_path, tag="demo-fastapi:latest")

    # Get the exposed port from the 'PORT' environment variable
    exposed_port = os.environ.get("PORT", 8000)

    # Run the container using testcontainers
    api = DockerContainer(image.id)
    api.with_env("DB_CONN", os.environ["DB_CONN"])
    api.with_exposed_ports(exposed_port)  # Expose the necessary ports

    # Start the container
    with api:
        api.start()
        wait_for_logs(
            container=api,
            predicate=r"Uvicorn running on",
            timeout=30,
            interval=2,
        )

        # Yield the container for use in tests
        yield api

    # Stop the container
    api.stop()
