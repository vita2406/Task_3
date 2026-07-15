from selenium.webdriver.common.by import By


class FeedPageLocators:

    FIRST_ORDER = (
        By.XPATH,
        "(//li[contains(@class,'OrderHistory_listItem')])[1]"
    )

    ORDER_MODAL = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal_opened')]"
    )

    CLOSE_MODAL = (
        By.XPATH,
        "//button[contains(@class,'Modal_modal__close')]"
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
        "//ul[contains(@class,'OrderFeed_orderListReady')]"
    )