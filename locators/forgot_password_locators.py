from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    EMAIL_INPUT = (
        By.XPATH,
        "//label[contains(text(),'Email')]/following-sibling::input"
    )

    RECOVERY_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Восстановить')]"
    )

    PASSWORD_INPUT = (
        By.XPATH,
        "//label[contains(text(),'Пароль')]/following-sibling::input"
    )

    SHOW_PASSWORD_BUTTON = (
        By.XPATH,
        "//input[@type='password']/following-sibling::div"
    )

    SAVE_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Сохранить')]"
    )
    
    LOGIN_LINK = (
    By.XPATH,
    "//a[contains(text(),'Войти')]"
    )