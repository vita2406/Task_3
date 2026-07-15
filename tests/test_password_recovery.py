import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления")
    def test_open_recovery_page(self, driver):
        ...

    @allure.title("Ввод email")
    def test_enter_email(self, driver):
        ...

    @allure.title("Кнопка показать пароль")
    def test_show_password(self, driver):

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery = ForgotPasswordPage(driver)

        main_page.open_login()
        login_page.open_recovery_page()

        recovery.enter_email("test@test.ru")
        recovery.click_recover()

        recovery.wait.until(
            EC.url_contains("reset-password")
        )

        recovery.enter_new_password("123456")
        recovery.click_show_password()

        assert recovery.password_field_is_active()