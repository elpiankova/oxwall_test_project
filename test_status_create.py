import pytest
import json
from pages.internal_pages.dashboard_page import DashboardPage

with open("data/posts.json", encoding="utf8") as f:
    post_text_list =json.loads(f.read())


@pytest.mark.parametrize("new_text", post_text_list)
def test_create_post(driver, logged_user, new_text):
    dashboard_page = DashboardPage(driver)
    count_posts_before = len(dashboard_page.get_posts())
    dashboard_page.create_post(text=new_text)
    dashboard_page.wait_new_post_appear(count_posts_before)
    posts = dashboard_page.get_posts()
    assert len(posts) == count_posts_before + 1  # Check count posts
    assert posts[0].text == new_text
    assert posts[0].time == "within 1 minute"
    assert posts[0].user == logged_user
