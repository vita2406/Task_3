import allure

from data import BASE_URL
from pages.main_page import MainPage


class TestMainFunctionality:

    @allure.title("Переход в конструктор")
    def test_open_constructor(self, driver):

        main_page = MainPage(driver)

        main_page.open(BASE_URL)
        main_page.open_feed()
        main_page.open_constructor()

        assert main_page.main_page_opened()

    @allure.title("Переход в ленту заказов")
    def test_open_feed(self, driver):

        main_page = MainPage(driver)

        main_page.open(BASE_URL)
        main_page.open_feed()

        assert main_page.feed_opened()

    @allure.title("Открытие окна ингредиента")
    def test_open_ingredient_modal(self, driver):

        main_page = MainPage(driver)

        main_page.open(BASE_URL)
        main_page.open_first_ingredient()

        assert main_page.ingredient_modal_visible()

    @allure.title("Закрытие окна ингредиента")
    def test_close_ingredient_modal(self, driver):

        main_page = MainPage(driver)

        main_page.open(BASE_URL)
        main_page.open_first_ingredient()
        main_page.close_modal()

        assert main_page.ingredient_modal_closed()

    @allure.title("Увеличение счетчика ингредиента")
    def test_ingredient_counter(self, driver):

        main_page = MainPage(driver)

        main_page.open(BASE_URL)

        assert main_page.ingredient_counter() == "0"

        main_page.add_bun_to_constructor()

        assert main_page.ingredient_counter() == "2"