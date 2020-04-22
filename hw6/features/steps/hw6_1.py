from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

BS_LINK_LOCATOR = (By.XPATH, "//div[@id='nav-xshop-container']//a[text()='Best Sellers']")
LIST_ITEMS_LOCATOR = (By.CSS_SELECTOR, ".zg_item.zg_homeWidgetItem")
ADD_CART_BUTTON = (By.ID, 'add-to-cart-button')
LINK_CART_COUNT = (By.ID, 'nav-cart-count')

@when('Click to Best Sellers link')
def click_to_bs_link_new_tab(context):
    bs_link = context.driver.find_element(*BS_LINK_LOCATOR)
    # this is the solution for MAC OSX. In other cases you can use the standard Keys.CONTROL
    bs_link.send_keys(Keys.COMMAND, Keys.ENTER)
    context.all_windows = context.driver.window_handles


@when('Add good to cart')
def add_good_to_cart(context):
    add_to_cart_button = context.driver.find_element(*ADD_CART_BUTTON)
    add_to_cart_button.click()

@then('Add first item to cart')
def add_first_item_to_cart(context):
    list_items = context.driver.find_elements(*LIST_ITEMS_LOCATOR)
    list_items[1].click()
    context.execute_steps(f'when Add good to cart')

@then('Refresh init window')
def refresh_origin_window(context):
    context.driver.refresh()

@then('Verify cart has {count} item')
def verify_cart_count_item(context, count):
    count_items = int(context.driver.find_element(*LINK_CART_COUNT).text)
    assert int(count) == count_items, \
        f'Expected what will be in the cart {int(count)}, but got {count_items}'
