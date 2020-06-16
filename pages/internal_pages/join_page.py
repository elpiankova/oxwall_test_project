from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

from pages.internal_pages.internal_page import InternalPage
from pages.locators import JoinPageLocators


class JoinPage(InternalPage):
    def input_real_name(self, text):
        real_name = self.find_visible_element_from_many_equal(JoinPageLocators.REAL_NAME_FIELD)
        real_name.clear()
        real_name.send_keys(text)

    def select_birthday(self, day, month, year):
        day_select = Select(self.find_visible_element_from_many_equal(JoinPageLocators.BIRTHDAY_DAY_DROPBOX))
        month_select = Select(self.find_visible_element_from_many_equal(JoinPageLocators.BIRTHDAY_MOUNTH_DROPBOX))
        year_select = Select(self.find_visible_element_from_many_equal(JoinPageLocators.BIRTHDAY_YEAR_DROPBOX))

        day_select.select_by_visible_text(day)
        month_select.select_by_value(month)
        year_select.select_by_value(year)

    def select_gender(self, item):
        locator = (JoinPageLocators.GENDER_RADIOBUTTON[0], JoinPageLocators.GENDER_RADIOBUTTON[1].format(item))
        gender = self.find_visible_element_from_many_equal(locator)
        gender.click()

    def select_look_for_option(self, item):
        label = self.find_visible_element_from_many_equal(JoinPageLocators.LOOK_CHECKBOX)
        parent_node = label.find_element(By.XPATH, '../..')
        for i in item:
            lookup = parent_node.find_element(By.XPATH, f'td[2]/ul/li[{i}]/input')
            lookup.click()

    def select_here_for_option(self, item):
        label = self.find_visible_element_from_many_equal(JoinPageLocators.HERE_FOR_CHECKBOX)
        parent_node = label.find_element(By.XPATH, '../..')
        for i in item:
            lookup = parent_node.find_element(By.XPATH, f'td[2]/ul/li[{i}]/input')
            lookup.click()

    def input_music_text(self, text):
        label = self.find_visible_element_from_many_equal(JoinPageLocators.MUSIC_LISTBOX)
        parent_node = label.find_element(By.XPATH, '../..')
        music = parent_node.find_element(By.XPATH, 'td[2]/textarea')
        music.clear()
        music.send_keys(text)

    def input_favourite_book_text(self, text):
        label = self.find_visible_element_from_many_equal(JoinPageLocators.BOOKS_LISTBOX)
        parent_node = label.find_element(By.XPATH, '../..')
        books = parent_node.find_element(By.XPATH, 'td[2]/textarea')
        books.clear()
        books.send_keys(text)

    def upload_user_photo(self, file_path):
        field = self.find_visible_element_from_many_equal(JoinPageLocators.USER_PHOTO)
        field.send_keys(file_path)
        apply = self.wait.until(EC.element_to_be_clickable(JoinPageLocators.APPLY_BT))
        apply.click()

    def input_username_text(self, text):
        text_field = self.find_visible_element_from_many_equal(JoinPageLocators.USERNAME_FIELD)
        text_field.clear()
        text_field.send_keys(text)

    def input_email_text(self, text):
        text_field = self.find_visible_element_from_many_equal(JoinPageLocators.EMAIL_FIELD)
        text_field.clear()
        text_field.send_keys(text)

    def input_password_text(self, text):
        text_field = self.find_visible_element_from_many_equal(JoinPageLocators.PASSWORD_FIELD)
        text_field.clear()
        text_field.send_keys(text)

    def input_repeat_password_text(self, text):
        text_field = self.find_visible_element_from_many_equal(JoinPageLocators.REPEAT_PASSWORD_FIELD)
        text_field.clear()
        text_field.send_keys(text)

    def press_join_button(self):
        join_bt = self.wait.until(EC.element_to_be_clickable(JoinPageLocators.JOIN_BT))
        join_bt.click()

