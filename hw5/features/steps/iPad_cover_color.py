from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

COLORS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#variation_color_name ul[role='radiogroup'] li")
COLOR_TITLE_LOCATOR = (By.CSS_SELECTOR, "#variation_color_name .selection")
ADD_CART_BUTTON = (By.ID, 'add-to-cart-button')
CART_BUTTON = (By.ID, 'hlb-view-cart-announce')


@given('Open Amazon iPad cover page')
def open_dress_page(context):
    context.driver.get('https://www.amazon.com/ProCase-iPad-Case-2018-2017/dp/B0798DMRBP')

@when('Get all iPad cover colors')
def get_all_dress_colors(context):
    context.cover_colors = context.driver.find_elements(*COLORS_BUTTON_LOCATOR)

@when('Check every cover color has description')
def color_has_description(context):
    context.color_title = context.driver.find_element(*COLOR_TITLE_LOCATOR)
    for cover_color in context.cover_colors:
        cover_color.click()
        print(f"{context.color_title.text} IN {cover_color.get_attribute('title')}")
        assert context.color_title.text in cover_color.get_attribute('title'), \
            f"Expected {context.color_title.text} in {cover_color.get_attribute('title')}"

@when('Add good to cart')
def add_good_to_cart(context):
    # sleep(2)
    context.wait.until_not(EC.element_to_be_clickable(ADD_CART_BUTTON))
    add_to_cart_button = context.driver.find_element(*ADD_CART_BUTTON)
    add_to_cart_button.click()

@when('Look shopping cart')
def look_shopping_cart(context):
    cart_button = context.driver.find_element(*CART_BUTTON)
    cart_button.click()

@then('Add {color_case} case to cart')
def add_case_to_cart(context, color_case):
    for cover_color in context.cover_colors:
        if color_case in cover_color.get_attribute('title'):
            cover_color.click()
            context.execute_steps(f'when Add good to cart')
            context.execute_steps(f'when Look shopping cart')
            sleep(2)
            break