# Created by kutsenko at 1/31/20

#Enter feature name here
Feature: Lego search

  # Enter scenario name here
  Scenario: Find header on goods page
    # Enter steps here
    Given Open Amazon main page
    When Search input fill Lego
    And Click search button
    Then Assert Lego header on page