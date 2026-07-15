from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[text()='Конструктор']"
    )

    FEED_BUTTON = (
        By.XPATH,
        "//p[text()='Лента Заказов']"
    )

    PROFILE_BUTTON = (
        By.XPATH,
        "//p[text()='Личный Кабинет']/parent::a"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Войти в аккаунт']"
    )

    FIRST_BUN = (
        By.XPATH,
        "(//a[contains(@class,'BurgerIngredient_ingredient')])[1]"
    )

    FIRST_SAUCE = (
        By.XPATH,
        "(//a[contains(@class,'BurgerIngredient_ingredient')])[3]"
    )

    BURGER_CONSTRUCTOR = (
        By.XPATH,
        "//section[contains(@class,'BurgerConstructor_basket')]//ul"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Оформить заказ']"
    )

    INGREDIENT_COUNTER = (
        By.XPATH,
        "(//p[contains(@class,'counter_counter')])[1]"
    )

    MODAL = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal_opened')]"
    )

    CLOSE_MODAL = (
        By.XPATH,
        "//button[contains(@class,'Modal_modal__close')]"
    )

    ORDER_NUMBER = (
        By.XPATH,
        "//h2[contains(@class,'Modal_modal__title_shadow')]"
    )