import allure

from pages.base_page import BasePage
from locators.forgot_password_locators import (
    ForgotPasswordPageLocators
)


class ForgotPasswordPage(BasePage):

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.send_keys(
            ForgotPasswordPageLocators.EMAIL_INPUT,
            email
        )

    @allure.step("Нажать восстановить")
    def click_recover(self):
        self.click(
            ForgotPasswordPageLocators.RECOVERY_BUTTON
        )

    @allure.step("Проверить открытие страницы восстановления")
    def recovery_page_opened(self):
        return self.url_contains(
            "forgot-password"
        )

    @allure.step("Проверить открытие страницы сброса пароля")
    def reset_password_page_opened(self):
        self.wait_for_url_contains(
            "reset-password"
        )
        return self.url_contains(
            "reset-password"
        )

    @allure.step("Ввести новый пароль")
    def enter_new_password(self, password):
        self.send_keys(
            ForgotPasswordPageLocators.PASSWORD_INPUT,
            password
        )

    @allure.step("Нажать показать пароль")
    def click_show_password(self):
        self.click(
            ForgotPasswordPageLocators.SHOW_PASSWORD_BUTTON
        )

    @allure.step("Проверить отображение поля пароля")
    def password_field_is_active(self):
        element = self.find(
            ForgotPasswordPageLocators.PASSWORD_INPUT
        )

        return (
            element.get_attribute("type")
            == "text"
        )

    @allure.step("Перейти на страницу входа")
    def open_login_page(self):
        self.click(
            ForgotPasswordPageLocators.LOGIN_LINK
        )