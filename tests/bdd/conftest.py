import os
import pytest
import docker
from docker.errors import APIError

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from testcontainers.core.waiting_utils import wait_for_logs
from testcontainers.postgres import PostgresContainer
from testcontainers.core.container import DockerContainer
from testcontainers.core.image import DockerImage

from app.models.base import Base  # Ensure this imports the Base class from your models

from app.core.logging import logger
from app.utils.filesystem import find_root_dir

POSTGRES_IMAGE = "postgres:latest"
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
    root_dir = find_root_dir(__file__)
    logs_path = os.path.join(root_dir, "logs")

    try:
        with PostgresContainer(POSTGRES_IMAGE) as postgres:
            postgres.with_name(POSTGRES_CONTAINER_NAME)
            postgres.with_volume_mapping(logs_path, "/var/lib/postgresql/data/logs")
            os.environ["DB_CONN"] = postgres.get_connection_url()
            os.environ["DB_HOST"] = postgres.get_container_host_ip()
            os.environ["DB_PORT"] = postgres.get_exposed_port(5432)
            # os.environ["DB_USERNAME"] = postgres.POSTGRES_USER
            # os.environ["DB_PASSWORD"] = postgres.POSTGRES_PASSWORD
            # os.environ["DB_NAME"] = postgres.POSTGRES_DB

            wait_for_logs(
                container=postgres,
                predicate="database system is ready to accept connections",
                timeout=10,
                interval=1,
            )

            # Log the port the container is running on
            logger.info(f"Postgres container is running on port: {os.environ["DB_PORT"]}")
            logger.info(f'Connection String: {os.environ["DB_CONN"]}')

            connection_string = os.environ["DB_CONN"]

            try:
                engine = create_engine(connection_string)

                # This is where the error is occurring
                Base.metadata.create_all(engine)  # Create the database structure

                session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
                session_instance = session_factory()
            except SQLAlchemyError as e:
                logger.error(f"Error creating the database: {e}")
    except Exception as err:
        logger.error(str(err))

    def cleanup():
        if session_instance:
            session_instance.close()

        if engine:
            engine.dispose()

        if postgres:
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
    docker_context = find_root_dir(__file__)

    connection_string = os.environ["DB_CONN"]
    logger.info(f"Connection string: {connection_string}")

    client = docker.from_env()

    try:
        # Build the Docker image with caching enabled
        image, logs = client.images.build(
            path=docker_context,
            tag="demo-fastapi:latest",
            rm=True,
            pull=True,
        )

        for log in logs:
            logger.info(log)

        image_string = image.id
        with DockerContainer(image_string) as container:
            container.with_env("DB_CONN", connection_string)
            container.with_exposed_ports(80)
            container.with_bind_ports(8080, 80)

            wait_for_logs(
                container=container,
                predicate="Uvicorn running on",
                timeout=30,
                interval=1,
            )

            # exposed_port = container.get_exposed_port(80)
            # logger.info(f"Exposed port: {exposed_port}")
    except Exception as err:
        logger.error(str(err))

    def cleanup():
        # teardown code
        logger.info("Cleaning up the API container")

    request.addfinalizer(cleanup)

    return {
        "host": "localhost",
        "port": "8080",
    }
