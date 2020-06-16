from pages.base_page import Page
from pages.locators import InternalPageLocators
from selenium.webdriver.support import expected_conditions as EC


class InternalPage(Page):
    @property
    def sign_in_menu(self):
        return self.find_element(InternalPageLocators.SIGN_IN)

    @property
    def sign_up_menu(self):
        return self.find_visible_element(InternalPageLocators.SIGN_UP)

    @property
    def user_menu(self):
        return self.find_clickable_element(InternalPageLocators.USER_ICON)

    @property
    def sigh_out_bt(self):
        return self.user_menu.find_element(*InternalPageLocators.SIGN_OUT)

    @property
    def main_menu(self):
        return self.find_element(InternalPageLocators.MAIN_MENU)

    @property
    def active_menu(self):
        return self.find_element(InternalPageLocators.ACTIVE_MENU)

    # def open_login_form(self):
    #     self.sign_in_menu.click()

    def open_sign_up_page(self):
        self.sign_up_menu.click()

    def logout(self):
        self.action.move_to_element(self.user_menu)
        self.action.perform()

        self.action.move_to_element(self.sigh_out_bt)
        self.action.click()
        self.action.perform()
