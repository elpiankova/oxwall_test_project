from pages.internal_pages.dashboard_page import DashboardPage
from pages.internal_pages.login_page import LoginWindowPage
from pages.internal_pages.main_page import MainPage


class OxwallHelper:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.dashboard_page = DashboardPage(driver)
        self.login_window = LoginWindowPage(driver)

        # self.wait = WebDriverWait(driver, 7)
        # self.action = ActionChains(driver)

    # def open_login_form(self):
    #     login_bt = self.wait.until(EC.element_to_be_clickable(InternalPageLocators.SIGN_IN))
    #     login_bt.click()
    #
    # def enter_credentials(self, username, password):
    #     user = self.wait.until(EC.element_to_be_clickable(LoginWindowLocators.USER_FIELD))
    #     user.clear()
    #     user.send_keys(username)
    #
    #     passwr = self.wait.until(EC.element_to_be_clickable(LoginWindowLocators.PSWD_FIELD))
    #     passwr.clear()
    #     passwr.send_keys(password)
    #
    #     sign_bt = self.wait.until(EC.element_to_be_clickable(LoginWindowLocators.SINGIN_BT))
    #     sign_bt.click()
    #     self.wait.until(EC.element_to_be_clickable(InternalPageLocators.USER_BOARD))
    #
    # def get_posts(self):
    #     return self.driver.find_elements(*DashboardPageLocators.POST_LIST)
    #
    # def create_post(self, text):
    #     text_field = self.wait.until(EC.element_to_be_clickable(DashboardPageLocators.STATUS_FIELD))
    #     text_field.send_keys(text)
    #
    #     save_bt = self.driver.find_element(*DashboardPageLocators.SAVE_BT)
    #     save_bt.click()
    #
    # def wait_new_post_appear(self, number):
    #     return self.wait.until(presence_of_elements(DashboardPageLocators.POST_TEXT, number+1))
    #
    # def logout(self):
    #     user = self.driver.find_element(*InternalPageLocators.USER_ICON)
    #     self.action = ActionChains(self.driver)
    #     self.action.move_to_element(user)
    #     self.action.perform()
    #
    #     logout = user.find_element(*InternalPageLocators.SIGN_OUT)
    #     self.action.move_to_element(logout)
    #     self.action.click()
    #     self.action.perform()
    #
    # def get_comment(self):
    #     return self.driver.find_elements(*DashboardPageLocators.COMMENTS_LIST)
    #
    # def create_new_comment(self, comment, post):
    #     comment_text = post.find_element(*DashboardPageLocators.COMMENT_TEXT_FIELD)
    #     if comment_text.size['height'] == 0 and comment_text.size['width'] == 0:
    #         comment_bt = post.find_element(*DashboardPageLocators.COMMENT_BT)
    #         comment_bt.click()
    #         self.wait.until(EC.visibility_of(comment_text))
    #     comment_text.send_keys(comment)
    #     comment_text.send_keys(Keys.ENTER)
    #
    # def wait_new_comment_appear(self, number):
    #     return self.wait.until(presence_of_elements(DashboardPageLocators.COMMENTS_LIST, number+1))
    #
    # def get_comment_counter(self, post):
    #     return post.find_element(*DashboardPageLocators.COMMENTS_COUNTER).text
    #
    # def delete_last_status(self, post):
    #     self.action.move_to_element(post)
    #     self.action.perform()
    #
    #     context_menu = self.wait.until(EC.presence_of_element_located(DashboardPageLocators.CONTEXT_MENU))
    #     self.action.move_to_element(context_menu)
    #     self.action.perform()
    #
    #     delete_command = self.wait.until(EC.presence_of_element_located(DashboardPageLocators.DELETE_BT))
    #     self.action.move_to_element(delete_command)
    #     self.action.click(delete_command)
    #     self.action.perform()
    #
    # def wait_last_post_removed(self, number):
    #     return self.wait.until(elements_less_than_number(DashboardPageLocators.POST_TEXT, number))
    #
    # def open_sign_up_page(self):
    #     login_bt = self.wait.until(EC.element_to_be_clickable(InternalPageLocators.SIGN_UP))
    #     login_bt.click()
    #
    # def find_visible_element_from_many_equal(self, locator):
    #     els = self.wait.until(EC.visibility_of_any_elements_located(locator),
    #                           message=f"No any visible elements with locator='{locator}'")
    #     return els[0]
    #     # elements = self.driver.find_elements(*locator)
    #     # for item in elements:
    #     #     if item.size['height'] != 0 and item.size['width'] != 0:
    #     #         return item
    #     # return None
    #
    # def input_real_name(self, text):
    #     real_name = self.find_visible_element_from_many_equal(JoinPageLocators.REAL_NAME_FIELD)
    #     real_name.clear()
    #     real_name.send_keys(text)
    #
    # def select_birthday(self, day, month, year):
    #     day_select = Select(self.find_visible_element_from_many_equal(JoinPageLocators.BIRTHDAY_DAY_DROPBOX))
    #     month_select = Select(self.find_visible_element_from_many_equal(JoinPageLocators.BIRTHDAY_MOUNTH_DROPBOX))
    #     year_select = Select(self.find_visible_element_from_many_equal(JoinPageLocators.BIRTHDAY_YEAR_DROPBOX))
    #
    #     day_select.select_by_visible_text(day)
    #     month_select.select_by_visible_text(month)
    #     year_select.select_by_visible_text(year)
    #
    # def select_gender(self, item):
    #     locator = (JoinPageLocators.GENDER_RADIOBUTTON[0], JoinPageLocators.GENDER_RADIOBUTTON[1].format(item))
    #     gender = self.find_visible_element_from_many_equal(locator)
    #     gender.click()
    #
    # def select_look_for_option(self, item):
    #     label = self.find_visible_element_from_many_equal(JoinPageLocators.LOOK_CHECKBOX)
    #     parent_node = label.find_element(By.XPATH, '../..')
    #     for i in item:
    #         lookup = parent_node.find_element(By.XPATH, f'td[2]/ul/li[{i}]/input')
    #         lookup.click()
    #
    # def select_here_for_option(self, item):
    #     label = self.find_visible_element_from_many_equal(JoinPageLocators.HERE_FOR_CHECKBOX)
    #     parent_node = label.find_element(By.XPATH, '../..')
    #     for i in item:
    #         lookup = parent_node.find_element(By.XPATH, f'td[2]/ul/li[{i}]/input')
    #         lookup.click()
    #
    # def input_music_text(self, text):
    #     label = self.find_visible_element_from_many_equal(JoinPageLocators.MUSIC_LISTBOX)
    #     parent_node = label.find_element(By.XPATH, '../..')
    #     music = parent_node.find_element(By.XPATH, 'td[2]/textarea')
    #     music.clear()
    #     music.send_keys(text)
    #
    # def input_favourite_book_text(self, text):
    #     label = self.find_visible_element_from_many_equal(JoinPageLocators.BOOKS_LISTBOX)
    #     parent_node = label.find_element(By.XPATH, '../..')
    #     books = parent_node.find_element(By.XPATH, 'td[2]/textarea')
    #     books.clear()
    #     books.send_keys(text)
    #
    # def upload_user_photo(self, file_path):
    #     field = self.find_visible_element_from_many_equal(JoinPageLocators.USER_PHOTO)
    #     field.send_keys(file_path)
    #     apply = self.wait.until(EC.element_to_be_clickable(JoinPageLocators.APPLY_BT))
    #     apply.click()
    #
    # def input_username_text(self, text):
    #     text_field = self.find_visible_element_from_many_equal(JoinPageLocators.USERNAME_FIELD)
    #     text_field.clear()
    #     text_field.send_keys(text)
    #
    # def input_email_text(self, text):
    #     text_field = self.find_visible_element_from_many_equal(JoinPageLocators.EMAIL_FIELD)
    #     text_field.clear()
    #     text_field.send_keys(text)
    #
    # def input_password_text(self, text):
    #     text_field = self.find_visible_element_from_many_equal(JoinPageLocators.PASSWORD_FIELD)
    #     text_field.clear()
    #     text_field.send_keys(text)
    #
    # def input_repeat_password_text(self, text):
    #     text_field = self.find_visible_element_from_many_equal(JoinPageLocators.REPEAT_PASSWORD_FIELD)
    #     text_field.clear()
    #     text_field.send_keys(text)
    #
    # def press_join_button(self):
    #     join_bt = self.wait.until(EC.element_to_be_clickable(JoinPageLocators.JOIN_BT))
    #     join_bt.click()
    #
    # def get_logged_in_user(self):
    #     return self.wait.until(EC.element_to_be_clickable(InternalPageLocators.USER_ICON))
