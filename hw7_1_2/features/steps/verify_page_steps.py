from behave import then

@then('Verify {signin_text} page is opened')
def verify_result(context, signin_text):
    context.app.verify_page.verify_header_result(signin_text)

@then('Verify {header_text} text present')
def verify_text_present(context, header_text):
    context.app.verify_page.verify_header2_result(header_text)

@then('{count} menu items are present')
def verify_count_items(context, count):
    count = int(count)
    context.app.verify_page.verify_menu_items(count)