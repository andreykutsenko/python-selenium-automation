from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_LOCATOR = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "input.nav-input[value='Go']")
FIRST_GOOD_SEARCH = (By.CSS_SELECTOR, ".s-result-list.s-search-results div[data-index='0'] h2.a-size-mini > .a-link-normal")
ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
NO_COVERAGE_BUTTON = (By.CSS_SELECTOR, ".a-button-stack #siNoCoverage-announce")
DELETE_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".a-declarative input[value='Delete']")

@when('Good search input {search_text}')
def goods_search_input(context, search_text):
    search_input = context.driver.find_element(*SEARCH_LOCATOR)
    search_input.clear()
    search_input.send_keys(search_text)

@when('Press search button')
def click_search_button(context):
    amazon_search_button = context.driver.find_element(*SEARCH_BUTTON_LOCATOR)
    amazon_search_button.click()
    sleep(2)

@when('Choose first item')
def add_good_to_cart(context):
    first_good_search = context.driver.find_element(*FIRST_GOOD_SEARCH)
    first_good_search.click()

@when('Add good to cart')
def add_good_to_cart(context):
    add_to_cart_button = context.driver.find_element(*ADD_TO_CART_BUTTON)
    add_to_cart_button.click()

@when('Click button no coverage')
def click_no_coverage(context):
    no_coverage_button = context.driver.find_element(*NO_COVERAGE_BUTTON)
    no_coverage_button.click()
    sleep(2)

@when('Remove good from cart')
def click_delete_button(context):
    amazon_delete_button = context.driver.find_element(*DELETE_BUTTON_LOCATOR)
    amazon_delete_button.click()
    sleep(2)