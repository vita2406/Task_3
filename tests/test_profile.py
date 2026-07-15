import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestProfile:

    @allure.title("Переход в личный кабинет")
    def test_open_profile(self, driver, user):

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open_login()

        login_page.login(
            user["email"],
            user["password"]
        )

        main_page.open_profile()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/account")
        )

        print("\nCURRENT URL:", driver.current_url)

        assert profile_page.profile_opened()

    @allure.title("Переход в историю заказов")
    def test_open_order_history(self, driver, user):

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open_login()

        login_page.login(
            user["email"],
            user["password"]
        )

        main_page.open_profile()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/account")
        )

        profile_page.open_history()

        WebDriverWait(driver, 10).until(
            EC.url_contains("order-history")
        )

        assert profile_page.history_opened()

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, user):

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open_login()

        login_page.login(
            user["email"],
            user["password"]
        )

        main_page.open_profile()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/account")
        )

        profile_page.logout()

        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )

        assert profile_page.login_page_opened()