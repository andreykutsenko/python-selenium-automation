from selenium.webdriver.common.by import By

from hw7_1_2.pages.base_page import Page

class MainPage(Page):
    SEARCH_ORDERS = (By.ID, 'nav-orders')
    SEARCH_CART = (By.ID, 'nav-cart')

    def open(self):
        self.open_page('https://www.amazon.com/')

    def click_orders(self):
        self.click(*self.SEARCH_ORDERS)

    def click_cart(self):
        self.click(*self.SEARCH_CART)