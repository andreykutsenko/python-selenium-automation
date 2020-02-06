from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "div#nav-tools a#nav-cart")
HEADER_GOODS_PAGE_LOCATOR = (By.CSS_SELECTOR, "div#sc-active-cart h1.sc-empty-cart-header")

@given('Open main page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')

@when('Click cart button')
def click_cart_button(context):
    amazon_search_button = context.driver.find_element(*SEARCH_BUTTON_LOCATOR)
    amazon_search_button.click()

@then ('Check results for {search_text} are shown')
def check_shopping_cart_page(context, search_text):
    assert 'Your Shopping Cart is empty' in context.driver.find_element(*HEADER_GOODS_PAGE_LOCATOR).text, f'Expected "Lego", but got {search_text}'