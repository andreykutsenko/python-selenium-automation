from behave import then
from selenium.webdriver.common.by import By

# TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")

@then('Search result for {product} is shown')
def verify_result(context, product):
    # result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
    # assert result_text == product, f"Expected text is {product}, but got {result_text}"
    context.app.results_page.verify_header_result(product)