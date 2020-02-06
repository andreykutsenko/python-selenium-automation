# Created by kutsenko at 1/31/20

#Enter feature name here
Feature: Verifies that Your Shopping Cart is empty

  # Enter feature description here
  Scenario: User checks his shopping cart
    # Enter steps here
    Given Open main page
    When Click cart button
    Then Check results for Your Shopping Cart is empty are shown