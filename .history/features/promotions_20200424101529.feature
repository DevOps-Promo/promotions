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