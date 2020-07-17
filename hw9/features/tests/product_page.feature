# Created by KTS at 7/15/20
Feature: Tests for product page

  Scenario: Size tooltip is shown upon hovering over Add to Cart buttom
    Given Open amazon product B074TBCSC8 page
    When Hover over Add to Cart button
    Then Verify size selection tooltip is shown

  Scenario: Hover over New arrivals and click the deals for Women
    Given Open amazon product B074TBCSC8 page
    When Hover over New arrivals
    Then Verify dropdown menu and click the deals for Women