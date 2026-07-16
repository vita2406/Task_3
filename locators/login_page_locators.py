from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL_INPUT = (
        By.XPATH,
        "//input[@name='name']"
    )

    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@type='password']"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Войти')]"
    )

    FORGOT_PASSWORD_LINK = (
        By.XPATH,
        "//a[contains(text(),'Восстановить пароль')]"
    )