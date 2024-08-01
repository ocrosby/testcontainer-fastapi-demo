Feature: Kubernetes Health Routes
  As a Kubernetes cluster
  I want to check the health of the application
  So that I can ensure it is running and ready to serve traffic

  Scenario: Check readiness probe
    When I send a GET request to "/health/ready"
    Then the response status code should be 200
    And the response should contain the message "Ready"

  Scenario: Check liveness probe
    When I send a GET request to "/health/live"
    Then the response status code should be 200
    And the response should contain the message "Alive"

  Scenario: Check startup probe
    When I send a GET request to "/health/startup"
    Then the response status code should be 200
    And the response should contain the message "Started"
