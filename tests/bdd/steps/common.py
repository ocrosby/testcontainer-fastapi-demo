"""
This module contains the common steps that can be reused across different features.
"""

from pytest_bdd import given, when, then, parsers


@given('the application is running')
def the_application_is_running():
    pass


@given('the application is not running')
def the_application_is_not_running():
    pass


@given('the application is running in a degraded state')
def the_application_is_running_in_degraded_state():
    pass


@given('the application is running under heavy load')
def the_application_is_running_under_heavy_load():
    pass


@given('the database is available')
def the_database_is_available():
    pass


@given('the database is not available')
def the_database_is_not_available():
    pass


@given('the database is in a degraded state')
def the_database_is_in_degraded_state():
    pass


@when(parsers.parse('I send a {method} request to "{resource}"'))
def send_request_to_resource(method: str, resource: str):
    pass


@then(parsers.parse('the response status code should be {status_code}'))
def response_status_code_should_be(status_code: int):
    pass


@then('the response should contain the current time')
def response_should_contain_current_time():
    pass
