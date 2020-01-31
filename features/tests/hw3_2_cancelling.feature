# Created by kutsenko at 1/31/20

Feature: User can search for Cancelling an order on Amazon
  # Enter feature description here
  Scenario: Find header on help page
    # Enter steps here
    Given Open Amazon Help link
    When Search Input Cancel order
    And Click button
    Then Assert results for Cancel Items or Orders are shown