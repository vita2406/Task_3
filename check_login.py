from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

EMAIL = "test123456@yandex.ru"
PASSWORD = "Password123!"

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

try:
    driver.get("https://qa-stellarburgers.education-services.ru/login")

    email = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
        )
    )

    password = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")
        )
    )

    email.send_keys(EMAIL)
    password.send_keys(PASSWORD)

    print("Email:", email.get_attribute("value"))
    print("Password:", password.get_attribute("value"))

    button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/div/main/div/form/button")
        )
    )

    print("Кнопка найдена")

    button.click()

    print("Клик выполнен")

    # ждем 10 секунд
    for i in range(10):
        print(i + 1, driver.current_url)
        time.sleep(1)

    input("Браузер не закроется. Нажми Enter...")

finally:
    driver.quit()