import os.path

from pages.internal_pages.dashboard_page import DashboardPage
from pages.internal_pages.join_page import JoinPage
from pages.internal_pages.main_page import MainPage
from conftest import PROJECT_PATH


def test_create_new_user(driver, user):
    main_page = MainPage(driver)
    main_page.open_sign_up_page()

    join_page = JoinPage(driver)
    join_page.input_username_text(user.username)
    join_page.input_email_text(user.email)
    join_page.input_password_text(user.password)
    join_page.input_repeat_password_text(user.password)
    join_page.input_real_name(user.real_name)
    if user.gender is not None:
        join_page.select_gender(user.gender)
    join_page.select_birthday(day=str(user.birthday.day), month=str(user.birthday.month), year=str(user.birthday.year))
    join_page.select_look_for_option([1, 2])
    join_page.select_here_for_option([1, 4])
    join_page.input_music_text('Music1\nMusic2\nMusic3')
    join_page.input_favourite_book_text('Book1\nBook2\nBook3')
    join_page.upload_user_photo(os.path.join(PROJECT_PATH, 'data', '111.png'))
    join_page.press_join_button()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.user_menu.text == user.real_name
