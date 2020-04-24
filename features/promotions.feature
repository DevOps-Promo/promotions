Feature: The promotion store service back-end
    As a promotion Store Owner
    I need a RESTful catalog service
    So that I can keep track of all my promotions

Background:
    Given the following promotions
        | name       | description        | start_date                | end_date             |
        | promo      | tenpercent         | 2020-04-23 12:00:00       | 2020-04-24 12:00:00  |
        | discount   | twentypercent      | 2020-04-23 12:00:00       | 2020-04-24 12:00:00  |
        | sale       | fivepercent        | 2020-04-23 12:00:00       | 2020-04-24 12:00:00  |

Scenario: The server is running
    When I visit the "Home Page"
    Then I should see "Promotion RESTful Service" in the title
    And I should not see "404 Not Found"

Scenario: Create a promotion
    When I visit the "Home Page"
    And I set the "Name" to "discount"
    And I set the "Description" to "sale"
    And I set the "Start_date" to "2020-04-23 12:00:00"
    And I set the "End_date" to "2020-04-24 12:00:00"
    And I press the "Create" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    Then the "Id" field should be empty
    And the "Name" field should be empty
    And the "Description" field should be empty
    And the "Start_date" field should be empty
    And the "End_date" field should be empty
    When I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see "discount" in the "Name" field
    And I should see "sale" in the "Description" field
    And I should see "2020-04-23 12:00:00" in the "Start_date" field
    And I should see "2020-04-24 12:00:00" in the "End_date" field

Scenario: Update a Promotion
    When I visit the "Home Page"
    And I set the "Name" to "promo"
    And I press the "Search" button
    Then I should see "promo" in the "Name" field
    And I should see "tenpercent" in the "Description" field
    When I change "Name" to "discount"
    And I press the "Update" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see "discount" in the "Name" field
    When I press the "Clear" button
    And I press the "Search" button
    Then I should see "discount" in the results
    Then I should not see "promo" in the results