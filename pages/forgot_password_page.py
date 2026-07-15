from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):

    def enter_email(self, email):
        self.send_keys(ForgotPasswordLocators.EMAIL_INPUT, email)

    def click_recover(self):
        self.click(ForgotPasswordLocators.RECOVER_BUTTON)

    def enter_new_password(self, password):
        self.send_keys(ForgotPasswordLocators.PASSWORD_INPUT, password)

    def click_show_password(self):
        self.click(ForgotPasswordLocators.SHOW_PASSWORD_BUTTON)

    def password_field_is_active(self):
        element = self.find(ForgotPasswordLocators.PASSWORD_INPUT)
        return element == self.driver.switch_to.active_element