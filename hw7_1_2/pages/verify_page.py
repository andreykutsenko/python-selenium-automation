from selenium.webdriver.common.by import By

from hw7_1_2.pages.base_page import Page

class VerifyPage(Page):
    TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1.a-spacing-small")
    H2_TEXT_BOLD = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty")
    HMENU_ITEM = (By.CSS_SELECTOR, '.hmenu.hmenu-visible.hmenu-translateX li a[class="hmenu-item"]')

    def verify_header_result(self, expected_test: str):
        self.verify_element_text(expected_test, *self.TOOLBAR_TEXT_BOLD)

    def verify_header2_result(self, expected_test: str):
        self.verify_element_text(expected_test, *self.H2_TEXT_BOLD)

    def verify_menu_items(self, expected_value: int):
        self.verify_element_count(expected_value, *self.HMENU_ITEM)

