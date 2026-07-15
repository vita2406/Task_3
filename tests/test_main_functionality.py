import allure

from data import BASE_URL
from pages.main_page import MainPage


class TestMainFunctionality:

    @allure.title("Переход в конструктор")
    def test_open_constructor(self, driver):

        driver.get(BASE_URL)

        main_page = MainPage(driver)

        main_page.open_feed()
        main_page.open_constructor()

        assert driver.current_url == BASE_URL

    @allure.title("Переход в ленту заказов")
    def test_open_feed(self, driver):

        driver.get(BASE_URL)

        main_page = MainPage(driver)

        main_page.open_feed()

        assert "feed" in driver.current_url

    @allure.title("Открытие окна ингредиента")
    def test_open_ingredient_modal(self, driver):

        driver.get(BASE_URL)

        main_page = MainPage(driver)

        main_page.open_first_ingredient()

        assert main_page.ingredient_modal_visible()

    @allure.title("Закрытие окна ингредиента")
    def test_close_ingredient_modal(self, driver):

        driver.get(BASE_URL)

        main_page = MainPage(driver)

        main_page.open_first_ingredient()
        main_page.close_modal()

        assert main_page.ingredient_modal_closed()
    

    @allure.title("Увеличение счетчика ингредиента")
    def test_ingredient_counter(self, driver):

        driver.get(BASE_URL)

        main_page = MainPage(driver)

        assert main_page.ingredient_counter() == "0"

        main_page.add_bun_to_constructor()

        assert main_page.ingredient_counter() == "2"