from selenium import webdriver


class BrowserFactory:

    @staticmethod
    def get_driver(browser):

        if browser == "chrome":
            return webdriver.Chrome()

        elif browser == "firefox":
            return webdriver.Firefox()

        raise ValueError(f"Unknown browser: {browser}")
