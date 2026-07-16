import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

        self.wait_url_not_contains("/login")

    @allure.step("Проверить успешную авторизацию")
    def login_successful(self):
        self.wait_url_not_contains("/login")
        return not self.url_contains("/login")

    @allure.step("Открыть страницу восстановления пароля")
    def open_recovery_page(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)
        self.wait_for_url_contains("forgot-password")

