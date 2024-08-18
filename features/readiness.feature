Feature: Readiness Probe
    As a user
    I want to check the readiness of the application
    So that I can know if the application is ready to serve traffic

    Background:
        Given the application is running

    @e2e @kubernetes @readiness
    Scenario: Running
        Given the application is running
        When I send a GET request to "/health/readiness"
        Then the response status code should be 200
        And the response should contain the message "Application is running"
        And the response should contain the current time
