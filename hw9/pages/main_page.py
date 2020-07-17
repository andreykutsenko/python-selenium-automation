from hw9.pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class MainPage(Page):
    ORDERS_BUTTON_LOCATOR = (By.ID, 'nav-orders')
    CART_BUTTON_LOCATOR = (By.ID, 'nav-cart')
    HAMBURGER_MENU_BUTTON_LOCATOR = (By.ID, 'nav-hamburger-menu')
    SEARCH_INPUT_LOCATOR = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON_LOCATOR = (By.CSS_SELECTOR, 'input.nav-input[type="submit"]')
    SELECT_DEPARTMENTS_LOCATOR = (By.ID, 'searchDropdownBox')

    def open(self):
        self.open_page('https://www.amazon.com')

    def search_product(self, text: str):
        self.input(text, *self.SEARCH_INPUT_LOCATOR)
        self.click(*self.SEARCH_ICON_LOCATOR)

    def open_amazon_orders(self):
        self.click(*self.ORDERS_BUTTON_LOCATOR)

    def open_amazon_cart(self):
        self.click(*self.CART_BUTTON_LOCATOR)

    def open_amazon_hamburger_menu(self):
        self.click(*self.HAMBURGER_MENU_BUTTON_LOCATOR)

    def select_search_category(self, option):
        select = Select(self.find_element(*self.SELECT_DEPARTMENTS_LOCATOR))
        select.select_by_visible_text(option)