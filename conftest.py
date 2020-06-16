import pytest
from selenium import webdriver

from oxwall_helper import OxwallHelper


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
def logged_user(oxwall):
    username = "admin"
    oxwall.login(username=username, password="pass")
    yield username
    oxwall.logout()
