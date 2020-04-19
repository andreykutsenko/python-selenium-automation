# Created by kutsenko at 4/17/20
Feature: Counter in Steps

  Scenario: Store your data
    Given Init new counter
    When Push red button
    And One more time
    And One more time
    Then Expected counter equal 3