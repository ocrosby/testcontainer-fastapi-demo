Feature: Post Management
  As a user
  I want to manage posts
  So that I can create, retrieve, update, and delete posts

  @e2e @post @create
  Scenario: Create a new post
    Given I have a post payload with title "My First Post" and content "This is the content of my first post"
    When I send a POST request to "/posts"
    Then the response status code should be 201
    And the response should contain the post ID
    And the response should contain the title "My First Post"
    And the response should contain the content "This is the content of my first post"

  @e2e @post @read
  Scenario: Retrieve all posts
    When I send a GET request to "/posts"
    Then the response status code should be 200
    And the response should contain a list of posts

  @e2e @post @read
  Scenario: Retrieve a post by ID
    Given there is a post with ID 1
    When I send a GET request to "/posts/1"
    Then the response status code should be 200
    And the response should contain the post ID 1
    And the response should contain the title "My First Post"
    And the response should contain the content "This is the content of my first post"

  @e2e @post @update
  Scenario: Update a post by ID
    Given there is a post with ID 1
    And I have an updated post payload with title "Updated Post" and content "This is the updated content"
    When I send a PUT request to "/posts/1"
    Then the response status code should be 200
    And the response should contain the post ID 1
    And the response should contain the title "Updated Post"
    And the response should contain the content "This is the updated content"

  @e2e @post @delete
  Scenario: Delete a post by ID
    Given there is a post with ID 1
    When I send a DELETE request to "/posts/1"
    Then the response status code should be 200
    And the response should contain the message "Post deleted successfully"