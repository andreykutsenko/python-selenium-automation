# Created by kutsenko at 4/21/20
Feature: User can manipulate with windows and tabs

  Scenario: User can open and close pages
    Given Open Amazon page
    When Store original windows
    And Click to blog link
    And Switch to the newly opened window
    Then Check this page has url blog.aboutamazon.com
    And User can close new window and switch back to original