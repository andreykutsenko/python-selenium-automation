from behave import given, when
from selenium.webdriver.common.by import By

# SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
# SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")

@given('Open Amazon landing page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open()

@when('Search for {product}')
def search_product(context, product):
    # search_field = context.driver.find_element(*SEARCH_INPUT)
    # search_field.clear()
    # search_field.send_keys(product)
    # context.driver.find_element(*SEARCH_ICON).click()
    context.app.main_page.search_product(product)