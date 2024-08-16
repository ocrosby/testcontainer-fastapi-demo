from pytest_bdd import scenarios, given, when, then
import requests

scenarios('../features/country.feature')

BASE_URL = "http://localhost:8000/countries"


@given('the database contains the following countries')
def setup_database_with_countries():
    # This function should set up the database with the given countries
    pass


@when('I send a GET request to "/countries"')
def send_get_request_to_countries():
    response = requests.get(BASE_URL)
    return response


@then('the response status code should be 200')
def check_status_code_200(response):
    assert response.status_code == 200


@then('the response should contain the following countries')
def check_response_contains_countries(response):
    # This function should check if the response contains the expected countries
    pass


@given('the database contains a country with id 1 and name "USA"')
def setup_database_with_country():
    # This function should set up the database with the given country
    pass


@when('I send a GET request to "/countries/1"')
def send_get_request_to_country():
    response = requests.get(f"{BASE_URL}/1")
    return response


@then('the response should contain the following country')
def check_response_contains_country(response):
    # This function should check if the response contains the expected country
    pass


@when('I send a POST request to "/countries" with the following data')
def send_post_request_to_countries():
    data = {"name": "Mexico"}
    response = requests.post(BASE_URL, json=data)
    return response


@then('the response status code should be 201')
def check_status_code_201(response):
    assert response.status_code == 201


@then('the response should contain the following country')
def check_response_contains_new_country(response):
    # This function should check if the response contains the new country
    pass


@when('I send a PUT request to "/countries/1" with the following data')
def send_put_request_to_country():
    data = {"name": "United States"}
    response = requests.put(f"{BASE_URL}/1", json=data)
    return response


@then('the response status code should be 200')
def check_status_code_200(response):
    assert response.status_code == 200


@then('the response should contain the following country')
def check_response_contains_updated_country(response):
    # This function should check if the response contains the updated country
    pass


@when('I send a DELETE request to "/countries/1"')
def send_delete_request_to_country():
    response = requests.delete(f"{BASE_URL}/1")
    return response


@then('the response status code should be 204')
def check_status_code_204(response):
    assert response.status_code == 204


@then('the country with id 1 should not exist in the database')
def check_country_not_in_database():
    # This function should check if the country with id 1 does not exist in the database
    pass
