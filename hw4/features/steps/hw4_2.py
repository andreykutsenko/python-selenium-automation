from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT_LOCATOR = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "input.nav-input[value='Go']")
HEADER_GOODS_PAGE_LOCATOR = (By.XPATH, "//div[@id='search']//span[@class='a-color-state a-text-bold']")
BOOKS_LIST_LOCATOR = (By.CSS_SELECTOR, ".rush-component .s-result-list.s-search-results.sg-row .s-result-item")
BOOKS_BEST_SELLER_LIST_LOCATOR = (By.CSS_SELECTOR, ".rush-component .s-result-list.s-search-results.sg-row .s-result-item .a-badge-text")
ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')

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

@then ('Count books on the first page and last book "BS" add to cart')
def count_books_on_page(context):
    historic_books_link_list = context.driver.find_elements(*BOOKS_LIST_LOCATOR)
    bs_books_link_list = context.driver.find_elements(*BOOKS_BEST_SELLER_LIST_LOCATOR)
    count_books = len(historic_books_link_list)
    print(f'\nThe number of books = {count_books}, including best sellers = {len(bs_books_link_list)}')

    # locator_last_book_bs_on_page = "div[data-index='" + str(count_books - 1) + "']"
    locator_last_book_bs_on_page = "div[data-index='" + str(count_books - 1) + "'] span[id*='best-seller-label']"

    last_book_bs_list = context.driver.find_elements(By.CSS_SELECTOR, locator_last_book_bs_on_page)
    sleep(4)

    if len(last_book_bs_list) > 0:
        locator_last_book_on_page = "div[data-index='" + str(count_books - 1) + "'] h2.a-spacing-none a.a-link-normal"
        context.driver.find_element(By.CSS_SELECTOR, locator_last_book_on_page).click()
        add_to_cart_button = context.driver.find_element(*ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
        sleep(2)

