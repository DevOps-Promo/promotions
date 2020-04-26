Feature: The promotion store service back-end
    As a promotion Store Owner
    I need a RESTful catalog service
    So that I can keep track of all my promotions

Background:
    Given the following promotions
        | name       | description | start_date                  | end_date               |
        | fido       | dog         | 2020-04-23 22:04:08.0       | 2020-04-24 22:04:08.0  |
        | kitty      | cat         | 2020-04-23 22:04:08.0       | 2020-04-24 22:04:08.0  |
        | leo        | lion        | 2020-04-23 22:04:08.0       | 2020-04-24 22:04:08.0  |

Scenario: The server is running
    When I visit the "Home Page"
    Then I should see "Promotion RESTful Service" in the title
    And I should not see "404 Not Found"

    Scenario: Create a promotion
    When I visit the "Home Page"
    And I set the "Name" to "fido"
    And I set the "description" to "dog"
    And I select "2020-04-23 22:04:08.0" in the "start_date" dropdown
    And I press the "Create" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    Then the "Id" field should be empty
    And the "Name" field should be empty
    And the "Category" field should be empty
    When I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see "Happy" in the "Name" field
    And I should see "Hippo" in the "Category" field
    And I should see "False" in the "Available" dropdown

Scenario: List all promotions
    When I visit the "Home Page"
    And I press the "Search" button
    Then I should see "fido" in the results
    And I should see "kitty" in the results
    And I should not see "leo" in the results

Scenario: List all dogs
    When I visit the "Home Page"
    And I set the "Category" to "dog"
    And I press the "Search" button
    Then I should see "fido" in the results
    And I should not see "kitty" in the results
    And I should not see "leo" in the results

Scenario: Update a promotion
    When I visit the "Home Page"
    And I set the "Name" to "fido"
    And I press the "Search" button
    Then I should see "fido" in the "Name" field
    And I should see "dog" in the "Category" field
    When I change "Name" to "Boxer"
    And I press the "Update" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see "Boxer" in the "Name" field
    When I press the "Clear" button
    And I press the "Search" button
    Then I should see "Boxer" in the results
    Then I should not see "fido" in the results