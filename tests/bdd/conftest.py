import os
import pytest
import docker

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from testcontainers.core.waiting_utils import wait_for_logs
from testcontainers.postgres import PostgresContainer
from testcontainers.core.container import DockerContainer

from app.models.base import Base  # Ensure this imports the Base class from your models

from app.core.logging import logger
from app.utils.filesystem import find_root_dir

POSTGRES_IMAGE = "postgres:16-alpine"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "test_password"
POSTGRES_DATABASE = "test_database"
POSTGRES_CONTAINER_PORT = 5432
POSTGRES_CONTAINER_NAME = "test_postgres_container"


@pytest.fixture(scope="session")
def postgres_container(request):
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
            timeout=15,
            interval=0.2,
        )

    # Log the port the container is running on
    logger.info(f"Postgres container is running on port: {os.environ["DB_PORT"]}")
    logger.info(f'Connection String: {os.environ["DB_CONN"]}')

    engine = create_engine(os.environ["DB_CONN"])

    # This is where the error is occurring
    Base.metadata.create_all(engine)  # Create the database structure

    session_factory = sessionmaker(bind=engine)
    session_instance = session_factory()

    def cleanup():
        session_instance.close()
        engine.dispose()
        postgres.stop()

    request.addfinalizer(cleanup)

    return {
        "session": session_instance,
        "container": postgres,
    }


@pytest.fixture(scope="session")
def api_container(request, postgres_container):
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

    # Define the internal and external ports
    internal_port = 80


    # Run the container using testcontainers
    connection_string = os.environ["DB_CONN"]

    logger.info(f"Connection string: {connection_string}")

    api = DockerContainer(image.id)
    api.with_env("DB_CONN", connection_string)
    api.with_env("DB_NAME", os.environ["DB_NAME"])
    api.with_env("DB_USERNAME", os.environ["DB_USERNAME"])
    api.with_env("DB_PASSWORD", os.environ["DB_PASSWORD"])
    api.with_env("DB_HOST", os.environ["DB_HOST"])
    api.with_env("DB_PORT", os.environ["DB_PORT"])
    api.with_env("HOST", "0.0.0.0")
    api.with_env("PORT", str(internal_port))
    api.with_exposed_ports(internal_port)  # Expose the necessary ports

    def cleanup():
        # teardown code
        try:
            api.stop()
            logs = api.get_logs()
            logger.info(f"Container logs: {logs}")
        except Exception as err:
            logger.error(f"Error getting logs: {err}")


    request.addfinalizer(cleanup)

    # Start the container
    with api:
        api.start()

        wait_for_logs(
            container=api,
            predicate=r"Uvicorn running on",
            timeout=15,
            interval=0.2,
        )

        # Retrieve the dynamically assigned external port
        external_port = api.get_exposed_port(internal_port)

        logger.info(f"Exposed port: {external_port}")


    return {
        "container": api,
        "host": "localhost",
        "port": external_port,
    }
