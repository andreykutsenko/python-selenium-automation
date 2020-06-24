from selenium.webdriver.support.wait import WebDriverWait

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 15)

    def open_page(self, url: str):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def verify_element_text(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text} text, but got {actual_text} text'

    def verify_element_count(self, expected_value: int, *locator):
        actual_value = int(len(self.driver.find_elements(*locator)))
        assert actual_value == expected_value, f'Expected {expected_value} elements, but got {actual_value} elements'