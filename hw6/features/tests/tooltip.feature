# Created by kutsenko at 4/21/20
Feature: Test scenarios for tooltip

  Scenario: Check when tooltip will hide
    Given Open Amazon main page
    When Sign in tooltip is clickable
    When Sign In tooltip will hide
    Then Tooltip is not clickable