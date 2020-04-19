from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_INPUT_LOCATOR = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "input.nav-input[value='Go']")
BOOKS_LIST_LOCATOR = (By.CSS_SELECTOR, ".rush-component .s-result-list.s-search-results.sg-row .s-result-item")
BOOKS_BEST_SELLER_LIST_LOCATOR = (By.CSS_SELECTOR, ".rush-component .s-result-list.s-search-results.sg-row .s-result-item .a-badge-text")

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

@then ('Count best seller books')
def count_books_on_page(context):
    fantasy_books_link_list = context.driver.find_elements(*BOOKS_LIST_LOCATOR)
    bs_books_link_list = context.driver.find_elements(*BOOKS_BEST_SELLER_LIST_LOCATOR)
    count_books = len(fantasy_books_link_list)
    print(f'\nThe number of books = {count_books}, including best sellers = {len(bs_books_link_list)}')

