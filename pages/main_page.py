from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def open_login(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    def open_profile(self):
        # Ждем появления кнопки личного кабинета после авторизации
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.PROFILE_BUTTON)
        )

        self.click(MainPageLocators.PROFILE_BUTTON)

        # Ждем открытия страницы аккаунта
        self.wait.until(
            EC.url_contains("/account")
        )

    def open_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def open_feed(self):
        self.click(MainPageLocators.FEED_BUTTON)

    def open_first_ingredient(self):
        self.click(MainPageLocators.FIRST_BUN)

    def close_modal(self):
        self.click(MainPageLocators.CLOSE_MODAL)

    def ingredient_modal_visible(self):
        return self.is_visible(MainPageLocators.MODAL)

    def ingredient_modal_closed(self):
        return self.is_not_visible(MainPageLocators.MODAL)

    def add_bun_to_constructor(self):
        ingredient = self.wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.FIRST_BUN
            )
        )

        constructor = self.wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.BURGER_CONSTRUCTOR
            )
        )

        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            source.dispatchEvent(new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));
        """, ingredient, constructor)

        self.wait.until(
            lambda d: self.ingredient_counter() == "2"
        )

    def ingredient_counter(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)

    def create_order(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    def order_number_visible(self):
        return self.is_visible(MainPageLocators.ORDER_NUMBER)