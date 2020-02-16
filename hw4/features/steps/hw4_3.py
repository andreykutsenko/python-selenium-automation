from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "div#nav-tools a#nav-cart")
HEADER_GOODS_PAGE_LOCATOR = (By.CSS_SELECTOR, "div#sc-active-cart h1.sc-empty-cart-header")

CARDS_BENEFIT_LOCATOR = (By.CSS_SELECTOR, "#prime-benefit-cards .card-category")

@given('Open Amazonprime page')
def open_amazonprime_page(context):
    context.driver.get('https://www.amazon.com/amazonprime')

@then ('Verify there are {expected_elements} boxes')
def check_shopping_cart_page(context, expected_elements):
    card_links_list = context.driver.find_elements(*CARDS_BENEFIT_LOCATOR)
    if len(card_links_list) > 0:
        assert len(card_links_list) == int(expected_elements), f'Expected {expected_elements}, but got {len(card_links_list)}'
    else:
        print("Коробок нет ;)")

