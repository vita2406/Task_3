import allure

from pages.main_page import MainPage
from pages.feed_page import FeedPage


@allure.feature("Лента заказов")
class TestFeed:

    @allure.title("Переход в ленту заказов")
    def test_open_feed(self, driver):

        main_page = MainPage(driver)

        main_page.open_feed()

        assert "feed" in driver.current_url

    @allure.title("Открытие модального окна заказа")
    def test_open_order_modal(self, driver):

        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.open_feed()

        feed_page.open_first_order()

        assert feed_page.modal_opened()