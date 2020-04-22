from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_INPUT_LOCATOR = (By.ID, 'searchval')
SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".banner-search-btn[value='Search']")
TABLE_LOCATOR = (By.CSS_SELECTOR, ".details a.description")
ADD_TO_CART_LOCATOR = (By.CSS_SELECTOR, ".add-to-cart input[type='submit']")
# POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, ".notification button[type='button']")
POPUP_TEXT_LOCATOR = (By.XPATH, "//div[@class='notification']//a[text()='View Cart']")
EMPTY_CART_LOCATOR = (By.XPATH, "//div[@class='cartItems']//a[text()='Empty Cart']")
ACCEPT_EMPTY_CART_LOCATOR = (By.XPATH, "//div[@class='modal-footer']//button[text()='Empty Cart']")


@given('Open main page')
def open_amazon_page(context):
    context.driver.get('https://www.webstaurantstore.com/')

@when('Search input fill {search_text}')
def search_input_fill(context, search_text):
    web_search_input = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    web_search_input.clear()
    web_search_input.send_keys(search_text)
    context.execute_steps(f'when Click search button')

@when('Click search button')
def click_search_button(context):
    web_search_button = context.driver.find_element(*SEARCH_BUTTON_LOCATOR)
    web_search_button.click()
    # sleep(4)

@then('Check the search result with the word {word_incl}')
def check_result(context, word_incl):
    # list_items = context.driver.find_elements(*ITEMS_LIST_LOCATOR)
    table_list = context.driver.find_elements(*TABLE_LOCATOR)
    for i in range(len(table_list)):
        assert word_incl in table_list[i].text
    print(f'Last -> {context.driver.find_elements(*TABLE_LOCATOR)[-1].text}')

@then('Add the last of found items to Cart')
def add_last_item_to_cart(context):
    context.driver.find_elements(*ADD_TO_CART_LOCATOR)[-1].click()
    # popup_close_buttons = context.driver.find_elements(*POPUP_CLOSE_BUTTON)
    # if len(popup_close_buttons) > 0:
    #     popup_close_buttons[0].click()
    context.execute_steps(f'then View Cart')

@then('View Cart')
def view_cart(context):
    context.wait.until(EC.visibility_of_element_located(POPUP_TEXT_LOCATOR))
    context.driver.find_element(*POPUP_TEXT_LOCATOR).click()

@then('Empty Cart')
def empty_cart(context):
    context.wait.until(EC.element_to_be_clickable(EMPTY_CART_LOCATOR))
    context.driver.find_element(*EMPTY_CART_LOCATOR).click()
    sleep(2)
    context.execute_steps(f'then Accept Empty Cart')

@then('Accept Empty Cart')
def accept_empty_cart(context):
    context.wait.until(EC.visibility_of_element_located(ACCEPT_EMPTY_CART_LOCATOR))
    context.driver.find_element(*ACCEPT_EMPTY_CART_LOCATOR).click()
    # context.driver.refresh()
    sleep(2)