import pytest
from selenium import webdriver

from oxwall_helper import OxwallHelper
from pages.internal_pages.login_page import LoginWindowPage
from pages.internal_pages.main_page import MainPage
from value_objects.user import User


@pytest.fixture()
def driver():
    base_url = "http://127.0.0.1/oxwall/"
    dr = webdriver.Chrome()
    dr.maximize_window()
    dr.get(base_url)
    yield dr
    dr.quit()


@pytest.fixture()
def oxwall(driver):
    return OxwallHelper(driver)


@pytest.fixture()
def logged_user(driver):
    user = User(username="admin", password="pass", real_name="Admin")
    main_page = MainPage(driver)
    main_page.sign_in_menu.click()
    login_page = LoginWindowPage(driver)
    login_page.enter_credentials(user.username, user.password)
    yield user
    main_page.logout()
