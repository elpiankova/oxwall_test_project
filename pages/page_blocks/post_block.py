from pages.locators import PostLocator
from value_objects.user import User


class PostBlock:
    def __init__(self, element):
        self.element = element

    @property
    def text(self):
        return self.element.find_element(*PostLocator.POST_TEXT).text

    @property
    def time(self):
        return self.element.find_element(*PostLocator.POST_TIME).text

    @property
    def user(self):
        el = self.element.find_element(*PostLocator.POST_USER)
        real_name = el.text
        username = el.get_attribute("href").split("/")[-1]
        return User(username=username, real_name=real_name)

    # TODO
    # @property
    # def likes_count(self):
    #     return None
    #
    # def add_like(self):
    #     self.likes_bt.click()
    #
    # def add_comment(self, text):



