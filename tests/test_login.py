import pytest

from pages.internal_pages.dashboard_page import DashboardPage
from pages.internal_pages.login_page import LoginWindowPage
from pages.internal_pages.main_page import MainPage
from value_objects.user import User


@pytest.mark.nondestructive
@pytest.mark.smoke
@pytest.mark.webtest
def test_login_positive(driver, main_page, login_page, dashboard_page, user):
    # user = User(username="admin", password="pass", real_name="Admin")

    main_page.sign_in_menu.click()
    assert login_page.is_this_page()
    login_page.enter_credentials(user.username, user.password)
    assert login_page.wait_authentication()
    assert dashboard_page.active_menu.text == "DASHBOARD"
    assert dashboard_page.title.text == "MY DASHBOARD"
    # assert dashboard_page.is_this_page()
    assert dashboard_page.user_menu.text == user.real_name
    dashboard_page.logout()
    # assert main_page.is_this_page()
