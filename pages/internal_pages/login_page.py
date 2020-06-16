from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page
from pages.locators import LoginWindowLocators, InternalPageLocators


class LoginWindowPage(Page):
    @property
    def username_field(self):
        return self.find_clickable_element(LoginWindowLocators.USER_FIELD)

    @property
    def password_field(self):
        return self.find_clickable_element(LoginWindowLocators.PSWD_FIELD)

    @property
    def sign_in_bt(self):
        return self.find_clickable_element(LoginWindowLocators.SINGIN_BT)

    def enter_credentials(self, username, password):
        self.username_field.clear()
        self.username_field.send_keys(username)
        self.password_field.clear()
        self.password_field.send_keys(password)
        self.sign_in_bt.click()

    def wait_authentication(self):
        try:
            self.wait.until(EC.element_to_be_clickable(InternalPageLocators.USER_BOARD),
                            message="Authentication failed!")
            return True
        except TimeoutException:
            return False

    def is_this_page(self):
        # TODO !!
        return True
