"""
This module contains the common steps that can be reused across different features.
"""

from pytest_bdd import given, when, then, parsers

# from tests.bdd.fixtures.common import app_running, app_not_running, app_degraded_state, app_heavy_load, db_available \
#     , db_not_available, db_degraded_state


class StepNotImplementedError(Exception):
    def __init__(self, step_name):
        super().__init__(f"Step '{step_name}' has not been implemented")
        self.step_name = step_name


@given('the application is running', target_fixture="app_running")
def the_application_is_running():
    """
    This fixture starts the FastAPI application using TestContainers with a custom Dockerfile.

    :param app_running:
    :return:
    """


@given('the application is not running', target_fixture="app_not_running")
def the_application_is_not_running():
    """
    This fixture stops the FastAPI application.

    :param app_not_running:
    :return:
    """


@given('the application is running in a degraded state', target_fixture="app_degraded_state")
def the_application_is_running_in_degraded_state():
    """
    This fixture starts the FastAPI application in a degraded state.

    :param app_degraded_state:
    :return:
    """


@given('the application is running under heavy load', target_fixture="app_heavy_load")
def the_application_is_running_under_heavy_load():
    """
    This fixture starts the FastAPI application under heavy load.

    :param app_heavy_load:
    :return:
    """


@given('the database is available', target_fixture="db_available")
def the_database_is_available():
    """
    This fixture starts the database using TestContainers with a custom Dockerfile.

    :param db_available:
    :return:
    """


@given('the database is not available', target_fixture="db_not_available")
def the_database_is_not_available():
    """
    This fixture stops the database.

    :param db_not_available:
    :return:
    """


@given('the database is in a degraded state', target_fixture="db_degraded_state")
def the_database_is_in_degraded_state():
    """
    This fixture starts the database in a degraded state.

    :param db_degraded_state:
    :return:
    """


@when(parsers.parse('I send a {method} request to "{resource}"'))
def send_request_to_resource(method: str, resource: str):
    """
    This step sends a request to the specified resource.

    :param method:
    :param resource:
    :return:
    """
    raise StepNotImplementedError(f"I send a {method} request to '{resource}'")


@then(parsers.parse('the response status code should be {status_code}'))
def response_status_code_should_be(status_code: int):
    """
    This step checks the response status code.

    :param status_code:
    :return:
    """
    raise StepNotImplementedError("the response status code should be {status_code}")


@then('the response should contain the current time')
def response_should_contain_current_time():
    """
    This step checks if the response contains the current time.

    :return:
    """
    raise StepNotImplementedError("the response should contain the current time")


@then(parsers.parse('the response should contain the message "{message}"'))
def response_should_contain_message(message: str):
    """
    This step checks if the response contains the specified message.

    :param message:
    :return:
    """
    raise StepNotImplementedError(f"the response should contain the message '{message}'")
