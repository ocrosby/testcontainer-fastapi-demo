Feature: Liveness
    As a user
    I want to check the liveness of the application
    So that I can know if the application is running

    @e2e @kubernetes @liveness @probe
    Scenario: Running
        Given the application is running
        When I send a GET request to "/health/liveness"
        Then the response status code should be 200
        And the response should contain the message "Application is running"
        And the response should contain the current time

    @e2e @kubernetes @liveness @probe
    Scenario: Not Running
        Given the application is not running
        When I send a GET request to "/health/liveness"
        Then the response status code should be 503
        And the response should contain the message "Application is not running"
        And the response should contain the current time

    @e2e @kubernetes @liveness @probe
    Scenario: Degraded State
        Given the application is running in a degraded state
        When I send a GET request to "/health/liveness"
        Then the response status code should be 200
        And the response should contain the message "Application is running in a degraded state"
        And the response should contain the current time

    @e2e @kubernetes @liveness @probe
    Scenario: Heavy Load
        Given the application is running under heavy load
        When I send a GET request to "/health/liveness"
        Then the response status code should be 200
        And the response should contain the message "Application is running under heavy load"
        And the response should contain the current time
