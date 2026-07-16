import pytest

from utils.browser_factory import BrowserFactory
from data import BASE_URL
from api.user_api import UserAPI


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )


@pytest.fixture
def driver(request):

    browser = request.config.getoption("--browser")

    driver = BrowserFactory.get_driver(browser)

    driver.set_window_size(1920, 1080)

    driver.get(BASE_URL)
    driver.delete_all_cookies()
    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def user():
    user = UserAPI.create_user()

    yield user

    UserAPI.delete_user(user["access_token"])