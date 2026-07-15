from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL_INPUT = (
        By.XPATH,
        "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input"
    )

    PASSWORD_INPUT = (
        By.XPATH,
        "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//*[@id='root']/div/main/div/form/button"
    )

    FORGOT_PASSWORD_LINK = (
        By.XPATH,
        "//a[text()='Восстановить пароль']"
    )

    ERROR_TEXT = (
        By.XPATH,
        "//p[contains(@class,'input__error')]"
    )