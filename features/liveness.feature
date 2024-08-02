Feature: Liveness Probe
    As a user
    I want to check the liveness of the application
    So that I can know if the application is running

    @e2e @liveness @probe
    Scenario: Check the liveness of the application
        Given the application is running
        When I send a GET request to "/liveness"
        Then the response status code should be 200
        And the response should contain the message "Application is running"
        And the response should contain the current time

    @e2e @liveness @probe
    Scenario: Check the liveness of the application when it is not running
        Given the application is not running
        When I send a GET request to "/liveness"
        Then the response status code should be 503
        And the response should contain the message "Application is not running"
        And the response should contain the current time

    @e2e @liveness @probe
    Scenario: Check the liveness of the application in a degraded state
        Given the application is running in a degraded state
        When I send a GET request to "/liveness"
        Then the response status code should be 200
        And the response should contain the message "Application is running in a degraded state"
        And the response should contain the current time

    @e2e @liveness @probe
    Scenario: Check the liveness of the application under heavy load
        Given the application is running under heavy load
        When I send a GET request to "/liveness"
        Then the response status code should be 200
        And the response should contain the message "Application is running under heavy load"
        And the response should contain the current time
