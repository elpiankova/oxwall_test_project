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


@pytest.mark.parametrize("new_text", post_text_list)
def test_create_post(driver, logged_user, new_text, db):
    dashboard_page = DashboardPage(driver)
    count_posts_before = len(dashboard_page.get_posts())
    dashboard_page.create_post(text=new_text)
    dashboard_page.wait_new_post_appear(count_posts_before)
    assert db.get_last_text_post() == new_text
    posts = dashboard_page.get_posts()
    assert len(posts) == count_posts_before + 1  # Check count posts
    assert posts[0].text == new_text
    assert posts[0].time == "within 1 minute"
    assert posts[0].user == logged_user
