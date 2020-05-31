from pages.base_page import Page
from pages.locators import InternalPageLocators


class InternalPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

        # self.sign_in_menu = self.find_element(InternalPageLocators.SIGN_IN)
        # self.sign_up_menu = self.find_element(InternalPageLocators.SIGN_UP)
        #
        # self.main_menu = self.find_element(InternalPageLocators.MAIN_MENU)
        # self.join_menu = self.find_element(InternalPageLocators.JOIN_MENU)

    @property
    def sign_in_menu(self):
        return self.find_element(InternalPageLocators.SIGN_IN)

    @property
    def main_menu(self):
        return self.find_element(InternalPageLocators.MAIN_MENU)

    # def click_sign_in(self):
    #     self.sign_in_menu.click()


class MainPage(InternalPage):
    pass

class LoginPage(Page):
    pass


