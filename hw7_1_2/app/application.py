from hw7_1_2.pages.main_page import MainPage
from hw7_1_2.pages.verify_page import VerifyPage
from hw7_1_2.pages.hamburger_menu_page import HamburgerMenuPage

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.verify_page = VerifyPage(self.driver)
        self.hamburgermenu_page = HamburgerMenuPage(self.driver)