import os.path
import json
import pytest
from selenium import webdriver

from db.db_connector import OxwallDB
from oxwall_helper import OxwallHelper
from pages.internal_pages.dashboard_page import DashboardPage
from pages.internal_pages.login_page import LoginWindowPage
from pages.internal_pages.main_page import MainPage
from value_objects.user import User

# import sys
# PROJECT_PATH = sys.path[0]

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="session")
def config():
    with open(os.path.join(PROJECT_PATH, "config.json")) as f:
        return json.load(f)


@pytest.fixture()
def driver(config, selenium):
    base_url = config["base_url"]
    dr = selenium
    dr.maximize_window()
    dr.get(base_url)
    yield dr
    dr.quit()


@pytest.fixture()
def app(driver):
    return OxwallHelper(driver)

@pytest.fixture()
def main_page(driver):
    return MainPage(driver)

@pytest.fixture()
def login_page(driver):
    return LoginWindowPage(driver)

@pytest.fixture()
def dashboard_page(driver):
    return DashboardPage(driver)

@pytest.fixture()
def logged_user(driver):
    user = User(username="admin", password="pass", real_name="Admin")
    main_page = MainPage(driver)
    main_page.sign_in_menu.click()
    login_page = LoginWindowPage(driver)
    login_page.enter_credentials(user.username, user.password)
    yield user
    main_page.logout()


@pytest.fixture()
def db(config):
    db = OxwallDB(**config['db'])
    yield db
    db.close()

filename = os.path.join(PROJECT_PATH, "data", "user.json")
with open(filename, encoding="utf8") as f:
    user_list = json.load(f)


@pytest.fixture(params=user_list, ids=[str(user) for user in user_list])
def user(request, db):
    user = User(**request.param)
    db.create_user(user)
    yield user
    db.delete_user(user)


