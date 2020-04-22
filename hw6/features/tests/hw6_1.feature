# Created by kutsenko at 4/21/20
Feature: User can manipulate with windows and verify that user can add a product from today’s deals into the cart

  Scenario: User can open and close pages, cart items would be saved in memory
    Given Open Amazon page
    When Store original windows
    And Click to Best Sellers link
    And Switch to the newly opened window
    Then Add first item to cart
    And User can close new window and switch back to original
    And Refresh init window
    Then Verify cart has 1 item
