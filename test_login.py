from pages.internal_page import MainPage


def test_login_positive(driver):
    main_page = MainPage(driver)
    main_page.main_menu.click()
    main_page.sign_in_menu.click()

