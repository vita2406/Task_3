from selenium.webdriver.common.by import By


class OrderFeedLocators:

    FIRST_ORDER = (
        By.CSS_SELECTOR,
        ".OrderHistory_listItem"
    )

    ORDER_MODAL = (
        By.CSS_SELECTOR,
        ".Modal_modal_opened"
    )

    TOTAL_COUNTER = (
        By.CSS_SELECTOR,
        ".OrderFeed_number"
    )

    TODAY_COUNTER = (
        By.CSS_SELECTOR,
        ".OrderFeed_number:nth-of-type(2)"
    )

    IN_PROGRESS = (
        By.CSS_SELECTOR,
        ".OrderFeed_orderListReady"
    )