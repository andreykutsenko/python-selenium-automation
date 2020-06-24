# Created by kutsenko at 4/25/20
Feature: Test for Amazon Search functionality

  Scenario: User can search for a product
    Given Open Amazon landing page
    When Search for dress
    Then Search result for "dress" is shown

  Scenario Outline: User can search for different products
    Examples:
    |search_word      |expected_search_result   |
    |dress            |"dress"                  |
    |toys             |"toys"                   |

    Given Open Amazon landing page
    When Search for <search_word>
    Then Search result for <expected_search_result> is shown