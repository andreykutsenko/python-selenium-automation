from selenium.webdriver.common.by import By

from hw7.pages.base_page import Page

class ResultsPage(Page):
    TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")

    def verify_header_result(self, expected_test: str):
        self.verify_element_text(expected_test, *self.TOOLBAR_TEXT_BOLD)
