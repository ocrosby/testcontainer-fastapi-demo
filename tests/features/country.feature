# Created by omar at 8/16/24
Feature: Countries API Endpoint
  As a user
  I want to interact with the /countries endpoint
  So that I can manage country data

  Scenario: Retrieve a list of countries
    Given the database contains the following countries:
      | id | name       |
      | 1  | USA        |
      | 2  | Canada     |
    When I send a GET request to "/countries"
    Then the response status code should be 200
    And the response should contain the following countries:
      | id | name       |
      | 1  | USA        |
      | 2  | Canada     |

  Scenario: Retrieve a single country by ID
    Given the database contains a country with id 1 and name "USA"
    When I send a GET request to "/countries/1"
    Then the response status code should be 200
    And the response should contain the following country:
      | id | name       |
      | 1  | USA        |

  Scenario: Create a new country
    When I send a POST request to "/countries" with the following data:
      | name       |
      | Mexico     |
    Then the response status code should be 201
    And the response should contain the following country:
      | id | name       |
      | 3  | Mexico     |

  Scenario: Update an existing country
    Given the database contains a country with id 1 and name "USA"
    When I send a PUT request to "/countries/1" with the following data:
      | name       |
      | United States |
    Then the response status code should be 200
    And the response should contain the following country:
      | id | name           |
      | 1  | United States  |

  Scenario: Delete an existing country
    Given the database contains a country with id 1 and name "USA"
    When I send a DELETE request to "/countries/1"
    Then the response status code should be 204
    And the country with id 1 should not exist in the database


  Scenario: Delete a country that does not exist
    Given the database does not contain a country with id 1
    When I send a DELETE request to "/countries/1"
    Then the response status code should be 404
    And the response should contain the following error:
      | message           |
      | Country not found |