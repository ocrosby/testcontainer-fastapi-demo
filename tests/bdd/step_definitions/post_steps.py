"""
This file contains the step definitions for the post feature.
"""

from pytest_bdd import given, when, then, parsers


@given(parsers.parse('there is a post with ID {post_id:d}'))
def set_post_id(post_id: int):
    pass


@given(parsers.parse('I have an updated post payload with title "{title}" and content "{content}"'))
def set_updated_title_and_content(title: str, content: str):
    pass


@given(parsers.parse('I have a post payload with title "{title}" and content "{content}"'))
def set_post_payload_with_title_and_content(title: str, content: str):
    pass


@when(parsers.parse('I send a {method} request to "{resource}"'))
def send_request_to_resource(method: str, resource: str):
    pass


@then(parsers.parse('the response should contain the post ID {post_id}'))
def response_contains_post_id(post_id: int):
    pass


@then(parsers.parse('the response status code should be {status_code}'))
def response_status_code_should_be(status_code: int):
    pass


@then(parsers.parse('the response should contain the post ID'))
def response_should_contain_the_post_id():
    pass


@then(parsers.parse('the response should contain the message "{message}"'))
def response_should_contain_the_message(message: str):
    pass


@then(parsers.parse('the response should contain the content "{content}"'))
def response_should_contain_the_content(content: str):
    pass


@then(parsers.parse('the response should contain the title {title}'))
def response_contains_title(title: str):
    pass


@then(parsers.parse('the response should contain a list of posts'))
def response_contains_list_of_posts():
    pass
