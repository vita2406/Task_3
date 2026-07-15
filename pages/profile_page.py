from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):

    def open_history(self):
        self.click(ProfilePageLocators.ORDER_HISTORY)

        self.wait.until(
            EC.url_contains("order-history")
        )

    def logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)

        self.wait.until(
            EC.url_contains("login")
        )

    def profile_opened(self):
        self.wait.until(
            EC.url_contains("/account")
        )
        return "/account" in self.driver.current_url

    def history_opened(self):
        self.wait.until(
            EC.url_contains("order-history")
        )
        return "order-history" in self.driver.current_url

    def login_page_opened(self):
        self.wait.until(
            EC.url_contains("login")
        )
        return "login" in self.driver.current_url