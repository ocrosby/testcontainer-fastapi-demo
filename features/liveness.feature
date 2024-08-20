Feature: Liveness
    As a user
    I want to check the liveness of the application
    So that I can know if the application is running

    @e2e @kubernetes @liveness
    Scenario: Running
        When I send a GET request to "/health/liveness"
        Then there should be no errors
        And the response status code should be 200
        And the response should contain the message "Application is running"

