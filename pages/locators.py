from selenium.webdriver.common.by import By


class DashboardPageLocators:
    TITLE = (By.CSS_SELECTOR, "h1.ow_stdmargin.ow_ic_house")
    POST_TEXT = (By.CSS_SELECTOR, ".ow_newsfeed_content")
    POST_LIST = (By.XPATH, '//*[contains(@id, "action-feed1-")]')

    STATUS_FIELD = (By.XPATH, '//textarea[@name="status"]')
    SAVE_BT = (By.XPATH, '//input[@name="save"]')

    COMMENTS_LIST = (By.CSS_SELECTOR, '.ow_comments_item.clearfix')
    COMMENTS_COUNTER = (By.CLASS_NAME, 'newsfeed_counter_comments')
    COMMENT_BT = (By.CSS_SELECTOR, '.ow_miniic_comment.newsfeed_comment_btn ')
    COMMENT_TEXT_FIELD = (By.XPATH, '//div[@class="ow_comments_input"]/textarea')

    POST_CONTEX_MENU = (By.CLASS_NAME, "ow_newsfeed_context_menu_wrap")
    CONTEXT_MENU = (By.CSS_SELECTOR, '.ow_context_more')
    DELETE_BT = (By.XPATH, '//ul[@class="ow_context_action_list ow_border"]/li/a')


class InternalPageLocators:
    # Right menu elements:
    SIGN_IN = (By.CSS_SELECTOR, ".ow_signin_label")
    SIGN_UP = (By.CLASS_NAME, 'ow_console_item_link')
    USER_BOARD = (By.CLASS_NAME, 'ow_notification_list')
    USER_MENU = (By.CSS_SELECTOR, '.ow_dropdown_menu_item.ow_cursor_pointer')
    SIGN_OUT = (By.XPATH, ".//a[contains(@href, 'sign-out')]")
    USER_ICON = (By.CSS_SELECTOR, ".ow_console_items_wrap > div:nth-child(5)")
    # Left menu elements:
    ACTIVE_MENU = (By.CSS_SELECTOR, ".ow_responsive_menu .ow_main_menu .active")
    MAIN_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_main_menu_index a")
    DASHBOARD_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_dashboard a")
    JOIN_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_base_join_menu_item a")
    MEMBERS_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_users_main_menu_item a")
    PHOTO_MENU = (By.CSS_SELECTOR, ".ow_site_panel .photo_photo a")
    VIDEO_MENU = (By.CSS_SELECTOR, ".ow_site_panel .video_video ")


class LoginWindowLocators:
    USER_FIELD = (By.NAME, "identity")
    PSWD_FIELD = (By.NAME, "password")
    SINGIN_BT = (By.CSS_SELECTOR, ".ow_button span .ow_positive")


class JoinPageLocators:
    TABLE = '//table[@class="ow_table_1 ow_form"]/tbody'
    USERNAME_FIELD = (By.CLASS_NAME, 'ow_username_validator')
    EMAIL_FIELD = (By.CLASS_NAME, 'ow_email_validator')
    PASSWORD_FIELD = (By.NAME, 'password')
    REPEAT_PASSWORD_FIELD  = (By.NAME, 'repeatPassword')
    REAL_NAME_FIELD = (By.XPATH, '//label[contains(text(), "Real name")]/../../td[2]/input')
    GENDER_RADIOBUTTON =  (By.XPATH, '//label[contains(text(), "Gender")]/../../td[2]/ul/li[{}]/input')
    BIRTHDAY_DAY_DROPBOX = (By.XPATH, '//label[contains(text(), "Birthday")]/../../td[2]/div/div[1]/select')
    BIRTHDAY_MOUNTH_DROPBOX = (By.XPATH, '//label[contains(text(), "Birthday")]/../../td[2]/div/div[2]/select')
    BIRTHDAY_YEAR_DROPBOX = (By.XPATH, '//label[contains(text(), "Birthday")]/../../td[2]/div/div[3]/select')
    LOOK_CHECKBOX = (By.XPATH, '//label[contains(text(), "Looking for")]')
    HERE_FOR_CHECKBOX = (By.XPATH, '//label[text()="Here for"]')
    MUSIC_LISTBOX = (By.XPATH, '//label[text()="Music"]')
    BOOKS_LISTBOX = (By.XPATH, '//label[text()="Favorite books"]')
    USER_PHOTO = (By.XPATH, "//input[@name= 'userPhoto'and@type='file']")
    APPLY_BT = (By.XPATH, "//input[@value= 'Apply crop'and@type='button']")
    JOIN_BT = (By.XPATH, "//input[@name= 'joinSubmit'and@type='submit']")


class PostLocator:
    POST_TEXT = (By.CLASS_NAME, 'ow_newsfeed_content')
    POST_USER = (By.CSS_SELECTOR, ".ow_newsfeed_string > a")
    POST_TIME = (By.CSS_SELECTOR, "a.create_time.ow_newsfeed_date")
    LIKES_BUTTON = ()
    LIKES_COUNTER = ()
    COMMENTS_COUNTER = (By.CLASS_NAME, 'newsfeed_counter_comments')
    COMMENTS_BUTTON = ()
