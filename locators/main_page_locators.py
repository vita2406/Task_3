from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Войти в аккаунт')]"
    )

    PROFILE_BUTTON = (
        By.XPATH,
        "//a[@href='/account']"
    )

    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[contains(text(),'Конструктор')]/ancestor::a"
    )

    FEED_BUTTON = (
        By.XPATH,
        "//a[@href='/feed']"
    )

    FIRST_BUN = (
        By.XPATH,
        "(//a[contains(@href,'ingredient')])[1]"
    )

    MODAL = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal_opened')]"
    )

    CLOSE_MODAL = (
        By.XPATH,
        "//button[contains(@class,'Modal_modal__close')]"
    )

    INGREDIENT_COUNTER = (
        By.XPATH,
        "(//p[contains(text(),'Краторная булка')]/ancestor::a//p[contains(@class,'counter_counter')])[1]"
    )

    BURGER_CONSTRUCTOR = (
        By.XPATH,
        "//section[contains(@class,'BurgerConstructor_basket')]"
    )