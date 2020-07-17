from selenium.webdriver.common.by import By

from hw9.pages.base_page import Page

class Product(Page):
    ADD_TO_CART_BUTTON_LOCATOR = (By.ID, 'add-to-cart-button')
    SIZE_TOOLTIP_LOCATOR = (By.ID, 'a-popover-content-1')
    NEW_ARRIVALS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#nav-subnav a[href*='sv_sl_6']")
    # NEW_ARRIVALS_BUTTON_LOCATOR = (By.CSS_SELECTOR, '.nav-hasArrow[tabindex="68"]')
    DROPDOWN_MENU_LOCATOR = (By.XPATH, "//h3[text()='Women']")

    def open_product_page(self, amazon_product):
        product_url = f'https://www.amazon.com/gp/product/{amazon_product}'
        self.open_page(product_url)

    def hover_over_button(self):
        self.hover_over_element(*self.ADD_TO_CART_BUTTON_LOCATOR)

    def hover_over_new_arrivals(self):
        self.hover_over_element(*self.NEW_ARRIVALS_BUTTON_LOCATOR)

    def verify_tooltip(self):
        self.wait_for_element_appear(*self.SIZE_TOOLTIP_LOCATOR)

    def verify_dropdown(self):
        self.wait_for_element_appear(*self.DROPDOWN_MENU_LOCATOR)
        self.click(*self.DROPDOWN_MENU_LOCATOR)