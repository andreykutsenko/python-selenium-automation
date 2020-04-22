from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BLOG_LINK_LOCATOR = (By.XPATH, "//div[@id='main-content']//a[text()='Learn more at blog.aboutamazon.com']")

@given('Open Amazon page')
def open_main_page(context):
    context.driver.get('https://www.amazon.com')


@when('Store original windows')
def store_original_window(context):
    context.init_window = context.driver.current_window_handle
    print(context.init_window)


@when('Click to blog link')
def click_to_blog_link(context):
    blog_link = context.driver.find_element(*BLOG_LINK_LOCATOR)
    blog_link.click()
    context.all_windows = context.driver.window_handles

@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.switch_to.window(context.all_windows[1])
    sleep(2)


@then('Check this page has url {expected_url}')
def check_page_has_url(context, expected_url):
    assert expected_url in context.driver.current_url


@then('User can close new window and switch back to original')
def go_back_to_origin_window(context):
    # all_windows = context.driver.window_handles
    context.driver.close()
    context.driver.switch_to.window(context.init_window)
    # context.driver.refresh()
    sleep(2)