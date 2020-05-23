def test_create_status(driver, oxwall, logged_user):
    new_text = "World"

    count_posts_before = len(oxwall.get_posts())
    oxwall.create_post(text=new_text)
    posts = oxwall.wait_new_post_appear(count_posts_before)
    assert len(posts) == count_posts_before + 1  # Check count posts
    assert posts[0].text == new_text
