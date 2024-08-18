# import os
#
# import pytest
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from testcontainers.core.waiting_utils import wait_for_logs
# from testcontainers.postgres import PostgresContainer
#
# from app.models import *  # Ensure this imports all your models
#
# POSTGRES_IMAGE = "postgres:16-alpine"
# POSTGRES_USER = "postgres"
# POSTGRES_PASSWORD = "test_password"
# POSTGRES_DATABASE = "test_database"
# POSTGRES_CONTAINER_PORT = 5432
# POSTGRES_CONTAINER_NAME = "test_postgres_container"
#
#
# @pytest.fixture(scope="session")
# def postgres_container():
#     """
#     Set up the Postgres container
#
#     :return: Postgres container
#     """
#     postgres = PostgresContainer(
#         image=POSTGRES_IMAGE,
#         user=POSTGRES_USER,
#         password=POSTGRES_PASSWORD,
#         dbname=POSTGRES_DATABASE,
#         port=POSTGRES_CONTAINER_PORT
#     )
#
#     with postgres:
#         os.environ["DB_CONN"] = postgres.get_connection_url()
#         os.environ["DB_HOST"] = postgres.get_container_host_ip()
#         os.environ["DB_PORT"] = postgres.get_exposed_port(5432)
#         os.environ["DB_USERNAME"] = postgres.POSTGRES_USER
#         os.environ["DB_PASSWORD"] = postgres.POSTGRES_PASSWORD
#         os.environ["DB_NAME"] = postgres.POSTGRES_DB
#
#         print(os.environ["DB_CONN"])
#
#         wait_for_logs(
#             container=postgres,
#             predicate="database system is ready to accept connections",
#             timeout=30,
#             interval=0.5,
#         )
#
#         yield postgres
#
#     postgres.stop()
#
#
# @pytest.fixture(scope="session")
# def db(postgres_container):
#     """
#     Set up the database
#
#     :param postgres_container: Postgres container
#     :return: Database
#     """
#     engine = create_engine(os.environ["DB_CONN"], echo=True)
#     Base.metadata.create_all(engine)  # Create the database structure
#     session_factory = sessionmaker(bind=engine)
#     session_instance = session_factory()
#
#     yield session_instance
#
#     session_instance.close()
#     engine.dispose()
