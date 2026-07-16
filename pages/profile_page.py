import allure

from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):

    @allure.step("Открыть историю заказов")
    def open_history(self):
        self.click(ProfilePageLocators.ORDER_HISTORY)
        self.wait_for_url_contains("order-history")

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)
        self.wait_for_url_contains("login")

    @allure.step("Проверить, что открыт профиль")
    def profile_opened(self):
        self.wait_for_url_contains("/account")
        return "/account" in self.get_current_url()

    @allure.step("Проверить, что открыта история заказов")
    def history_opened(self):
        self.wait_for_url_contains("order-history")
        return "order-history" in self.get_current_url()

    @allure.step("Проверить, что открыта страница входа")
    def login_page_opened(self):
        self.wait_for_url_contains("login")
        return "login" in self.get_current_url()

