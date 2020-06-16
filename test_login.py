from pages.internal_pages.dashboard_page import DashboardPage
from pages.internal_pages.login_page import LoginWindowPage
from pages.internal_pages.main_page import MainPage
from value_objects.user import User


def test_login_positive(driver):
    user = User(username="admin", password="pass", real_name="Admin")

    main_page = MainPage(driver)
    main_page.sign_in_menu.click()
    login_page = LoginWindowPage(driver)
    assert login_page.is_this_page()
    login_page.enter_credentials(user.username, user.password)
    assert login_page.wait_authentication()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.active_menu.text == "DASHBOARD"
    assert dashboard_page.title.text == "MY DASHBOARD"
    # assert dashboard_page.is_this_page()
    assert dashboard_page.user_menu.text == user.real_name
    dashboard_page.logout()
    # assert main_page.is_this_page()
