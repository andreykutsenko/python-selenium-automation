# Created by kutsenko at 4/22/20
Feature: User clicks on Best Sellers link on the top menu and verify that new page opens

  Scenario: User clicks on each top link and verify that new page opens
    Given Open Amazon page
    When Clicks on Best Sellers link on the top menu
    Then Clicks on each top link and verify that new page opens