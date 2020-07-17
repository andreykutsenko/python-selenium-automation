# Created by KTS at 7/16/20
Feature: Test for alerts

  Scenario: Create page with Alerts
    Given Open AMZ main page
    When Alert is open
    Then We can close Alert
    When Confirm is open
    Then We can close confirm
    When Prompt is open
    Then We can close Prompt