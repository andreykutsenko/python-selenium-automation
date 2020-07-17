from behave import then

@then('Result will contain {search_value}')
def check_result(context, search_value):
    context.app.results_page.verify_header_result(search_value)