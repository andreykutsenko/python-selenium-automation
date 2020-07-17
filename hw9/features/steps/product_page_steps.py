from behave import given, when, then

@given('Open amazon product {amazon_product} page')
def open_amazon_product_page(context, amazon_product):
    context.app.product_page.open_product_page(amazon_product)

@when('Hover over Add to Cart button')
def hover_over_button(context):
    context.app.product_page.hover_over_button()

@when('Hover over New arrivals')
def hover_over_arrivals(context):
    context.app.product_page.hover_over_new_arrivals()

@then("Verify size selection tooltip is shown")
def verify_size_selection_tooltip(context):
    context.app.product_page.verify_tooltip()

@then("Verify dropdown menu and click the deals for Women")
def verify_selection_dropdown(context):
    context.app.product_page.verify_dropdown()