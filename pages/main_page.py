import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Открыть страницу входа")
    def open_login(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    @allure.step("Открыть личный кабинет")
    def open_profile(self):
        self.click(MainPageLocators.PROFILE_BUTTON)

    @allure.step("Открыть конструктор")
    def open_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_url_contains("/")

    @allure.step("Открыть ленту заказов")
    def open_feed(self):
        self.click(MainPageLocators.FEED_BUTTON)
        self.wait_for_url_contains("/feed")

    @allure.step("Открыть первый ингредиент")
    def open_first_ingredient(self):
        self.click(MainPageLocators.FIRST_BUN)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.CLOSE_MODAL)

    @allure.step("Проверить отображение модального окна")
    def ingredient_modal_visible(self):
        return self.is_visible(MainPageLocators.MODAL)

    @allure.step("Проверить закрытие модального окна")
    def ingredient_modal_closed(self):
        return self.is_not_visible(MainPageLocators.MODAL)

    @allure.step("Добавить булку в конструктор")
    def add_bun_to_constructor(self):
        ingredient = self.find(MainPageLocators.FIRST_BUN)
        constructor = self.find(MainPageLocators.BURGER_CONSTRUCTOR)

        self.execute_script("""
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true,
                dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true,
                dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragover', {
                bubbles: true,
                dataTransfer
            }));

            target.dispatchEvent(new DragEvent('drop', {
                bubbles: true,
                dataTransfer
            }));

            source.dispatchEvent(new DragEvent('dragend', {
                bubbles: true,
                dataTransfer
            }));
        """, ingredient, constructor)

        self.wait.until(lambda d: self.ingredient_counter() == "2")

    @allure.step("Получить значение счетчика ингредиента")
    def ingredient_counter(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Оформить заказ")
    def create_order(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Проверить отображение номера заказа")
    def order_number_visible(self):
        return self.is_visible(MainPageLocators.ORDER_NUMBER)

    @allure.step("Проверить, что открыта главная страница")
    def main_page_opened(self):
        return not self.url_contains("/feed")
    

    @allure.step("Проверить, что открыта лента заказов")
    def feed_opened(self):
        return "feed" in self.get_current_url()