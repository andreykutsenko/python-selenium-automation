# Created by kutsenko at 4/22/20
Feature: Check the search result and empty cart

  Scenario: Search for goods with verification and Add the last of found items to Cart after run Empty the Cart
    Given Open main page
    When Search input fill stainless work table
    Then Check the search result with the word Table
    And Add the last of found items to Cart
    Then Empty Cart