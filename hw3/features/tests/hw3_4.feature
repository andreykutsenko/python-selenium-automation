# Created by kutsenko at 2/15/20

Feature: Test Your Shopping Cart Scenario
  
  Scenario: User add good, remove it and get empty cart
    Given Open main page
    When Good search input laptop
    And Press search button
    When Choose first item
    And Add good to cart
    And Click button no coverage
    When Click cart button
    And Remove good from cart
    Then Check results for Your Shopping Cart is empty are shown