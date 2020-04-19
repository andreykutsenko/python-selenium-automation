# Created by kutsenko at 4/18/20
Feature: Dress color

  Scenario: Check every dress color name
    Given Open Amazon dress page
    When Get all dress colors
    Then Check every color has description