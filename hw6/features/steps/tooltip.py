from behave   import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

TOOLTIP_LOCATOR = (By.CSS_SELECTOR, '.nav-signin-tt.nav-flyout')

@given('Open Amazon main page')
def open_main_page(context):
    context.driver.get('https://www.amazon.com')


@when('Sign in tooltip is clickable')
def wait_signin_tooltip_clickable(context):
    context.wait.until(EC.element_to_be_clickable(TOOLTIP_LOCATOR))

@when('Sign In tooltip will hide')
def wait_signin_tooltip_disappears(context):
    context.wait.until(EC.invisibility_of_element(TOOLTIP_LOCATOR))

@then('Tooltip is not clickable')
def wait_tooltip_not_clickable(context):
    context.wait.until_not(EC.element_to_be_clickable(TOOLTIP_LOCATOR))