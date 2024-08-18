Feature: Startup Probe
    As a user
    I want to check the startup of the application
    So that I can know if the application is started

    @e2e @kubernetes @startup
    Scenario: Check the startup of the application
        Given the application is running
        When I send a GET request to "/health/startup"
        Then the response status code should be 200
        And the response should contain the message "Started"
        And the response should contain the current time
