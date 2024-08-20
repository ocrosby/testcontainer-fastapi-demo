Feature: Readiness Probe
    As a user
    I want to check the readiness of the application
    So that I can know if the application is ready to serve traffic

    @e2e @kubernetes @readiness
    Scenario: Running
        When I send a GET request to "/health/readiness"
        Then there should be no errors
        And the response status code should be 200
        And the response should contain the message "Application is running"

