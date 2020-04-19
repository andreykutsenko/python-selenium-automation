# Created by kutsenko at 4/18/20
Feature: Count best sellers in fantasy books on Amazon
  # Enter feature description here
  Scenario: Count fantasy books
    # Enter steps here
    Given Open Amazon main page
    When Search input fill fantasy books
    And Click search button
    Then Count best seller books