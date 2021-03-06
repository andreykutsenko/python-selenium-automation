from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT_LOCATOR = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "input.nav-input[value='Go']")
HEADER_GOODS_PAGE_LOCATOR = (By.XPATH, "//div[@id='search']//span[@class='a-color-state a-text-bold']")

@given('Open Amazon main page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')

@when('Search input fill {search_text}')
def search_input_fill(context, search_text):
    amazon_search_input = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    amazon_search_input.clear()
    amazon_search_input.send_keys(search_text)

@when('Click search button')
def click_search_button(context):
    amazon_search_button = context.driver.find_element(*SEARCH_BUTTON_LOCATOR)
    amazon_search_button.click()
    sleep(2)

@then ('Assert {search_text} header on page')
def check_header_goods_page(context, search_text):
    assert 'Lego' in context.driver.find_element(*HEADER_GOODS_PAGE_LOCATOR).text, f'Expected "Lego", but got {search_text}'