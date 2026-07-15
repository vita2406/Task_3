from selenium.webdriver.common.by import By


class OrderFeedLocators:

    FIRST_ORDER = (
        By.XPATH,
        "(//li[contains(@class,'OrderHistory_listItem')])[1]"
    )

    ORDER_MODAL = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal_opened')]"
    )

    TOTAL_COUNTER = (
        By.XPATH,
        "(//p[contains(@class,'OrderFeed_number')])[1]"
    )

    TODAY_COUNTER = (
        By.XPATH,
        "(//p[contains(@class,'OrderFeed_number')])[2]"
    )

    IN_PROGRESS = (
        By.XPATH,
        "(//ul[contains(@class,'OrderFeed_orderListReady')])[1]"
    )