from selenium.webdriver.common.by import By


class ProfilePageLocators:

    ORDER_HISTORY = (
        By.LINK_TEXT,
        "История заказов"
    )

    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[text()='Выход']"
    )