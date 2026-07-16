from selenium.webdriver.common.by import By


class FeedPageLocators:

    FIRST_ORDER = (
        By.XPATH,
        "(//*[contains(@class,'OrderHistory_listItem')])[1]"
    )

    ORDER_MODAL = (
        By.XPATH,
        "//*[contains(@class,'Modal_modal_opened')]"
    )

    CLOSE_MODAL = (
        By.XPATH,
        "//*[contains(@class,'Modal_modal__close')]"
    )

    TOTAL_COUNTER = (
        By.XPATH,
        "(//*[contains(@class,'OrderFeed_number')])[1]"
    )

    TODAY_COUNTER = (
        By.XPATH,
        "(//*[contains(@class,'OrderFeed_number')])[2]"
    )

    IN_PROGRESS = (
        By.XPATH,
        "//*[contains(@class,'OrderFeed_orderListReady')]"
    )