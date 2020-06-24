from selenium.webdriver.common.by import By

from hw7_1_2.pages.base_page import Page

class HamburgerMenuPage(Page):
    SEARCH_H_MENU = (By.ID, 'nav-hamburger-menu')
    SEARCH_A_MENU = (By.CSS_SELECTOR, '.hmenu.hmenu-visible a[data-menu-id="3"]')

    def click_hamburger_menu(self):
        self.click(*self.SEARCH_H_MENU)

    def click_amazon_music_menu(self):
        self.click(*self.SEARCH_A_MENU)