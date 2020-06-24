from behave import given, when

@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open()

@when('Click Amazon Orders link')
def click_orders_button(context):
    context.app.main_page.click_orders()

@when('Click on cart icon')
def click_cart_button(context):
    context.app.main_page.click_cart()