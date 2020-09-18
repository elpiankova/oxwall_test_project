import allure
import pytest
import json
import os.path
from conftest import PROJECT_PATH
from data.randon_string import random_string
from pages.internal_pages.dashboard_page import DashboardPage

filename = os.path.join(PROJECT_PATH, "data", "posts.json")
with open(filename, encoding="utf8") as f:
    post_text_list = json.load(f)

post_text_list.append(random_string(enter=True, spaces=True))
post_text_list.append(
    pytest.param(random_string(maxlen=100, spaces=True, whitespases=True),
                 marks=[pytest.mark.smoke, pytest.mark.xfail])
)


@allure.title("Post create test")
@allure.feature("Post feature")
@allure.story("Create text post (without photos)")
@pytest.mark.regression
@pytest.mark.webtest
@pytest.mark.parametrize("new_text", post_text_list, ids=[str(p) for p in post_text_list])
def test_create_post(driver, logged_user, new_text, db):
    with allure.step("GIVEN initial amount of post in Oxwall database"):
        dashboard_page = DashboardPage(driver)
        count_posts_before = len(dashboard_page.get_posts())


    dashboard_page.create_post(text=new_text)

    with allure.step("THEN a new status appears in DB"):
        assert new_text == db.get_last_text_post()
    with allure.step("THEN a new status block appears before old list of posts"):
        dashboard_page.wait_new_post_appear(count_posts_before)
        posts = dashboard_page.get_posts()
        assert len(posts) == count_posts_before + 1  # Check count posts
    with allure.step(f'Then this status block has this {new_text} '
                     f'and author {logged_user.real_name} '
                     f'and time "within 1 minute"'):
        assert posts[0].text == new_text
        assert posts[0].user == logged_user
        assert posts[0].time == "within 1 minute"


@allure.feature("Post feature")
@allure.title("Post delete test")
def test_delete_post():
    pass
