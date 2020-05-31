from selenium.webdriver.common.by import By


class DashboardPageLocators:
    POST_TEXT = (By.CSS_SELECTOR, ".ow_newsfeed_content")


class InternalPageLocators:
    SIGN_IN = (By.CSS_SELECTOR, ".ow_signin_label")
    SIGN_UP = ()

    MAIN_MENU = ()
    JOIN_MENU = ()
    USER_ICON = (By.CSS_SELECTOR, ".ow_console_items_wrap > div:nth-child(5)")


class LoginPageLocators:
    USERNAME_FIELD = (By.NAME, "identity")
    PASSWORD_FIELD = (By.NAME, "password")
    SIGN_IN = (By.CSS_SELECTOR, ".ow_button span .ow_positive")
