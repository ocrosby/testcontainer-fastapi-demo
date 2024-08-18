"""
This module contains the common steps that can be reused across different features.
"""

import datetime

import httpx

from pytest_bdd import given, when, then, parsers


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
def send_request_to_resource(method: str, resource: str, request_response):
    """
    This step sends a request to the specified resource.

    :param method:
    :param resource:
    :return:
    """

    # Use httpx to send the request

    headers = {
        "accept": "application/json",
    }

    # build the URL from the resource
    url = f"http://localhost:8000{resource}"

    # Create a request object
    request = httpx.Request(method=method, url=url, headers=headers)

    # Send the request using an httpx.Client instance
    with httpx.Client() as client:
        response = client.send(request)

    request_response['request'] = request
    request_response['response'] = response


@then(parsers.parse('the response status code should be {status_code:d}'))
def response_status_code_should_be(status_code: int, request_response):
    """
    This step checks the response status code.

    :param status_code:
    :return:
    """
    response = request_response['response']
    assert response.status_code == status_code


@then('the response should contain the current time')
def response_should_contain_current_time(request_response):
    """
    This step checks if the response contains the current time.

    :return:
    """
    response = request_response['response']
    response_json = response.json()

    if 'time' not in response_json:
        raise AssertionError("Response does not contain 'time' field [1]")

    response_time_str = response_json.get('time', None)
    if response_time_str is None:
        raise AssertionError("Response does not contain 'time' field [2]")

    response_time = datetime.datetime.fromisoformat(response_time_str)
    current_time = datetime.datetime.now(datetime.timezone.utc)

    # Allow for a small difference between the current time and the response time
    time_difference = abs((current_time - response_time).total_seconds())
    assert time_difference < 5, f"Time difference is {time_difference} seconds"


@then(parsers.parse('the response should contain the message "{message}"'))
def response_should_contain_message(message: str, request_response):
    """
    This step checks if the response contains the specified message.

    :param message:
    :return:
    """
    response = request_response['response']
    assert message in response.text, f"Response does not contain message '{message}'"
