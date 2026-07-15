import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestLogin:

    @allure.title("Вход существующего пользователя")
    def test_login(self, driver, user):

        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.open_login()

        login_page.login(
            user["email"],
            user["password"]
        )

        assert "login" not in driver.current_url