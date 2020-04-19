# Created by kutsenko at 4/18/20
Feature: iPad cover color

  Scenario: Check every iPad cover color name
    Given Open Amazon iPad cover page
    When Get all iPad cover colors
    And Check every cover color has description
    Then Add Gold case to cart
