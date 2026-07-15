from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators


class LoginPage(BasePage):

    def login(self, email, password):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

        self.click(LoginPageLocators.LOGIN_BUTTON)

        # Ждем успешной авторизации
        self.wait.until(
            lambda driver: "/login" not in driver.current_url
        )

        # Ждем появления кнопки "Личный кабинет"
        self.wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.PROFILE_BUTTON
            )
        )

    def open_recovery_page(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def get_error_text(self):
        try:
            return self.get_text(LoginPageLocators.ERROR_TEXT)
        except Exception:
            return "Ошибка не найдена"