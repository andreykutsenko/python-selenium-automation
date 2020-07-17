from behave import when, then

@given('Open AMZ main page')
def open_amazon(context):
    context.app.main_page.open()

@when('Select {option} option')
def hover_over_button(context, option):
    context.app.main_page.select_search_category(option)

@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search_product(product)

@then('Our searching will be in {category} category')
def verify_tooltip_shown(context, category):
    context.app.results_page.verify_department_header_result(category)