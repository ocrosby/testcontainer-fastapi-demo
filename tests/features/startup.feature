Feature: Startup Probe
    As a user
    I want to check the startup of the application
    So that I can know if the application is started

    @e2e @startup @probe
    Scenario: Check the startup of the application
        Given the application is running
        When I send a GET request to "/health/startup"
        Then the response status code should be 200
        And the response should contain the message "Started"
        And the response should contain the current time


    @e2e @startup @probe
    Scenario: Check the startup of the application when it is not started
        Given the application is not running
        When I send a GET request to "/health/startup"
        Then the response status code should be 503
        And the response should contain the message "Not Started"
        And the response should contain the current time

    @e2e @startup @probe
    Scenario: Check the startup of the application in a degraded state
        Given the application is running in a degraded state
        When I send a GET request to "/health/startup"
        Then the response status code should be 200
        And the response should contain the message "Started in a degraded state"
        And the response should contain the current time

    @e2e @startup @probe
    Scenario: Check the startup of the application under heavy load
        Given the application is running under heavy load
        When I send a GET request to "/health/startup"
        Then the response status code should be 200
        And the response should contain the message "Started under heavy load"
        And the response should contain the current time

    @e2e @startup @probe
    Scenario: Check the startup of the application when the database is available
        Given the database is available
        When I send a GET request to "/health/startup"
        Then the response status code should be 200
        And the response should contain the message "Started and database is available"
        And the response should contain the current time


    @e2e @startup @probe
    Scenario: Check the startup of the application when the database is not available
        Given the database is not available
        When I send a GET request to "/health/startup"
        Then the response status code should be 503
        And the response should contain the message "Not Started but database is not available"
        And the response should contain the current time


    @e2e @startup @probe
    Scenario: Check the startup of the application when the database is in a degraded state
        Given the database is in a degraded state
        When I send a GET request to "/health/startup"
        Then the response status code should be 200
        And the response should contain the message "Started but database is in a degraded state"
        And the response should contain the current time
