from selenium.webdriver.common.keys import Keys

from custom_waits import presence_of_elements, elements_less_than_number
from pages.internal_pages.internal_page import InternalPage
from pages.locators import DashboardPageLocators
from selenium.webdriver.support import expected_conditions as EC

from pages.page_blocks.post_block import PostBlock


class DashboardPage(InternalPage):
    @property
    def title(self):
        return self.find_visible_element(DashboardPageLocators.TITLE)

    @property
    def post_text_field(self):
        return self.find_clickable_element(DashboardPageLocators.STATUS_FIELD)

    @property
    def save_bt(self):
        return self.find_visible_element(DashboardPageLocators.SAVE_BT)

    def get_posts(self):
        els = self.driver.find_elements(*DashboardPageLocators.POST_LIST)
        posts = [PostBlock(element) for element in els]
        return posts

    def create_post(self, text):
        self.post_text_field.send_keys(text)
        self.save_bt.click()

    def wait_new_post_appear(self, number):
        return self.wait.until(presence_of_elements(DashboardPageLocators.POST_TEXT, number + 1))

    def is_this_page(self):
        return self.active_menu.text == "DASHBOARD" and self.title.text == "MY DASHBOARD"

    # TODO
    def get_comment(self):
        return self.driver.find_elements(*DashboardPageLocators.COMMENTS_LIST)

    def create_new_comment(self, comment, post):
        comment_text = post.find_element(*DashboardPageLocators.COMMENT_TEXT_FIELD)
        if comment_text.size['height'] == 0 and comment_text.size['width'] == 0:
            comment_bt = post.find_element(*DashboardPageLocators.COMMENT_BT)
            comment_bt.click()
            self.wait.until(EC.visibility_of(comment_text))
        comment_text.send_keys(comment)
        comment_text.send_keys(Keys.ENTER)

    def wait_new_comment_appear(self, number):
        return self.wait.until(presence_of_elements(DashboardPageLocators.COMMENTS_LIST, number+1))

    def get_comment_counter(self, post):
        return post.find_element(*DashboardPageLocators.COMMENTS_COUNTER).text

    def delete_last_status(self, post):
        self.action.move_to_element(post)
        self.action.perform()

        context_menu = self.wait.until(EC.presence_of_element_located(DashboardPageLocators.CONTEXT_MENU))
        self.action.move_to_element(context_menu)
        self.action.perform()

        delete_command = self.wait.until(EC.presence_of_element_located(DashboardPageLocators.DELETE_BT))
        self.action.move_to_element(delete_command)
        self.action.click(delete_command)
        self.action.perform()

    def wait_last_post_removed(self, number):
        return self.wait.until(elements_less_than_number(DashboardPageLocators.POST_TEXT, number))