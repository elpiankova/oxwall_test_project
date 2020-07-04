from pytest_bdd import given, when, then

from value_objects.user import User


@given("initial amount of post in Oxwall database")
def initial_posts(app):
    return app.dashboard_page.get_posts()


@given("I as a logged user")
def logged_user(config, app):
    user = User(**config["admin"])
    app.main_page.sign_in_menu.click()
    app.login_window.enter_credentials(user.username, user.password)
    yield user
    app.main_page.logout()


@when("I add a new post with <text> in Dashboard page")
def create_post(app, text):
    app.dashboard_page.create_post(text=text)


@then("a new post block appears before old table of posts")
def wait_new_post(app, initial_posts):
    app.dashboard_page.wait_new_post_appear(len(initial_posts))


@then("this post block has this <text> and author as this user and time \"within 1 minute\"")
def verify_new_post(app, text, logged_user):
    new_post = app.dashboard_page.get_posts()[0]
    assert new_post.text == text, f"Visible post text is not equal input text: {new_post.text} != {text}"
    assert new_post.time == "within 1 minute", f"Post time is not 'within 1 minute: {new_post.time}'"
    assert new_post.user == logged_user, f"Visible user text is not signin user: {new_post.user} != {logged_user}"

