from hw9.pages.product_page import Product
from hw9.pages.main_page import MainPage
from hw9.pages.results_page import ResultsPage
from hw9.pages.alerts import Alerts


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.product_page = Product(self.driver)
        self.main_page = MainPage(self.driver)
        self.results_page = ResultsPage(self.driver)
        self.alerts = Alerts(self.driver)