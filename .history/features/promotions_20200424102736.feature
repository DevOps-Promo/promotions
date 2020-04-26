Feature: The promotion store service back-end
    As a promotion Store Owner
    I need a RESTful catalog service
    So that I can keep track of all my promotions

Background:
    Given the following promotions
        | name       | description | start_date                  | end_date               |
        | discount   | dog         | 2020-04-23 22:04:08.0       | 2020-04-24 22:04:08.0  |
        | kitty      | cat         | 2020-04-23 22:04:08.0       | 2020-04-24 22:04:08.0  |
        | leo        | lion        | 2020-04-23 22:04:08.0       | 2020-04-24 22:04:08.0  |

Scenario: The server is running
    When I visit the "Home Page"
    Then I should see "Promotion RESTful Service" in the title
    And I should not see "404 Not Found"

Scenario: Create a promotion
    When I visit the "Home Page"
    And I set the "Name" to "discount"
    And I set the "Description" to "sale"
    And I set the "Start date" to "2020-04-23 22:04:08.0"
    And I set the "End date" to "2020-04-24 22:04:08.0"
    And I press the "Create" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    Then the "Id" field should be empty
    And the "Name" field should be empty
    And the "Description" field should be empty
    And the "Start date" field should be empty
    And the "End date" field should be empty
    When I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see "discount" in the "Name" field
    And I should see "sale" in the "Description" field
    And I should see "2020-04-23 22:04:08.0" in the "Start date" field
    And I should see "2020-04-24 22:04:08.0" in the "End date" field