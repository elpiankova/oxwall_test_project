from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 7)
        self.action = ActionChains(driver)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def find_element(self, locator):
        el = self.wait.until(EC.presence_of_element_located(locator),
                             message=f"No element with locator='{locator}'")
        return el

    def find_elements(self, locator):
        el = self.wait.until(EC.presence_of_all_elements_located(locator),
                             message=f"No any elements with locator='{locator}'")
        return el

    def find_visible_element(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator),
                             message=f"No visible element with locator='{locator}'")
        return el

    def find_clickable_element(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator),
                             message=f"No clickable element with locator='{locator}'")
        return el

    def find_all_visible_elements(self, locator):
        els = self.wait.until(EC.visibility_of_all_elements_located(locator),
                             message=f"Not all elements visible with locator={locator}")
        return els

    def find_visible_element_from_many_equal(self, locator):
        els = self.wait.until(EC.visibility_of_any_elements_located(locator),
                              message=f"No any visible elements with locator='{locator}'")
        return els[0]
        # elements = self.driver.find_elements(*locator)
        # for item in elements:
        #     if item.size['height'] != 0 and item.size['width'] != 0:
        #         return item
        # return None
