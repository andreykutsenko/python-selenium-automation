# Created by kutsenko at 2/16/20
Feature: User can search for historic books on Amazon
  # Enter feature description here
  Scenario: Count historic books
    # Enter steps here
    Given Open Amazon main page
    When Search input fill history book
    And Click search button
    Then Count books on the first page and last book "BS" add to cart