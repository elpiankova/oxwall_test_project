from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from custom_waits import presence_of_elements


class OxwallHelper:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 7)
        self.action = ActionChains(driver)

    def wait_new_post_appear(self, count_posts_before):
        return self.wait.until(presence_of_elements((By.CSS_SELECTOR, ".ow_newsfeed_content"), count_posts_before + 1),
                          message="less than")

    def get_posts(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".ow_newsfeed_content")

    def logout(self):
        # Hover on user icon in header
        user_icon = self.driver.find_element(By.CSS_SELECTOR, ".ow_console_items_wrap > div:nth-child(5)")
        hover = self.action.move_to_element(user_icon)
        hover.perform()
        # Log_out
        log_out = self.driver.find_element(By.XPATH, "//li[7]/div/a")
        hover_and_click = self.action.move_to_element(log_out)
        hover_and_click.click()
        hover_and_click.perform()

    def create_post(self, text):
        # Post new msg
        newsfeed_fld = self.driver.find_element(By.CSS_SELECTOR, "textarea[name='status']")
        newsfeed_fld.click()
        newsfeed_fld.send_keys(text)
        send_btn = self.driver.find_element(By.CSS_SELECTOR, ".ow_submit_auto_click .ow_button")
        send_btn.click()

    def login(self, username, password):
        # Login form + authorization
        sign_in = self.driver.find_element(By.CSS_SELECTOR, ".ow_signin_label")
        sign_in.click()
        username_fld = self.driver.find_element(By.NAME, "identity")
        username_fld.clear()
        username_fld.send_keys(username)
        password_fld = self.driver.find_element(By.NAME, "password")
        password_fld.clear()
        password_fld.send_keys(password)
        sign_in_btn = self.driver.find_element(By.CSS_SELECTOR, ".ow_button span .ow_positive")
        sign_in_btn.click()
        # wait.until_not(EC.invisibility_of_element((By.XPATH, "//body/div[4]/div/div/div/a")))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".newsfeed_update_status_info .ow_smallmargin")))
