from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT_LOCATOR = (By.ID, 'helpsearch')
SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "span#helpSearchSubmit input[type='submit']")
HEADER_GOODS_PAGE_LOCATOR = (By.CSS_SELECTOR, "div.help-content > h1")

@given('Open Amazon Help link')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('Search input {text}')
def search_input(context, text):
    amazon_search_input = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    amazon_search_input.clear()
    amazon_search_input.send_keys(text)

@when('Click button')
def click_button(context):
    amazon_search_button = context.driver.find_element(*SEARCH_BUTTON_LOCATOR)
    amazon_search_button.click()
    sleep(2)

@then ('Assert results for {ass_text} are shown')
def check_results_page(context, ass_text):
    assert 'Cancel Items or Orders' in context.driver.find_element(*HEADER_GOODS_PAGE_LOCATOR).text, f'Expected "Cancel Items or Orders", but got {ass_text}'