import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage


class TestLogin:

    @allure.title("Вход по кнопке «Войти в аккаунт»")
    def test_login_from_main_page(self, driver, user):

        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.open_login()

        login_page.login(
            user["email"],
            user["password"]
        )

        assert login_page.login_successful()

    @allure.title("Вход через кнопку «Личный кабинет»")
    def test_login_from_profile_button(self, driver, user):

        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.open_profile()

        login_page.login(
            user["email"],
            user["password"]
        )

        assert login_page.login_successful()

    @allure.title("Вход через страницу восстановления пароля")
    def test_login_from_recovery_page(self, driver, user):

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = ForgotPasswordPage(driver)

        main_page.open_login()

        login_page.open_recovery_page()

        # переход обратно на страницу входа
        recovery_page.open_login_page()

        login_page.login(
            user["email"],
            user["password"]
        )

        assert login_page.login_successful()