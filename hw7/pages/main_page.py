from selenium.webdriver.common.by import By

from hw7.pages.base_page import Page

class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")

    def open(self):
        self.open_page('https://www.amazon.com/')

    def search_product(self, text: str):
        self.input(text, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_ICON)