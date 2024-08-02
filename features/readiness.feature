Feature: Readiness Probe
    As a user
    I want to check the readiness of the application
    So that I can know if the application is ready to serve traffic

    Background:
        Given the application is running

    @e2e @readiness @probe
    Scenario: Check the readiness of the application
        Given the application is running
        When I send a GET request to "/readiness"
        Then the response status code should be 200
        And the response should contain the message "Application is running"
        And the response should contain the current time

    @e2e @readiness @probe    
    Scenario: Check the readiness of the application when it is not running
        Given the application is not running
        When I send a GET request to "/readiness"
        Then the response status code should be 503
        And the response should contain the message "Application is not running"
        And the response should contain the current time

    @e2e @readiness @probe
    Scenario: Check the readiness of the application in a degraded state
        Given the application is running in a degraded state
        When I send a GET request to "/readiness"
        Then the response status code should be 200
        And the response should contain the message "Application is running in a degraded state"
        And the response should contain the current time

    @e2e @readiness @probe
    Scenario: Check the readiness of the application under heavy load
        Given the application is running under heavy load
        When I send a GET request to "/readiness"
        Then the response status code should be 200
        And the response should contain the message "Application is running under heavy load"
        And the response should contain the current time

    @e2e @readiness @probe
    Scenario: Check the readiness of the application when the database is available
        Given the database is available
        When I send a GET request to "/readiness"
        Then the response status code should be 200
        And the response should contain the message "Application is running and database is available"
        And the response should contain the current time

    @e2e @readiness @probe
    Scenario: Check the readiness of the application when the database is not available
        Given the database is not available
        When I send a GET request to "/readiness"
        Then the response status code should be 503
        And the response should contain the message "Application is running but database is not available"
        And the response should contain the current time

    @e2e @readiness @probe
        Scenario: Check the readiness of the application when the database is in a degraded state
        Given the database is in a degraded state
        When I send a GET request to "/readiness"
        Then the response status code should be 503
        And the response should contain the message "Application is running but database is in a degraded state"
        And the response should contain the current time
