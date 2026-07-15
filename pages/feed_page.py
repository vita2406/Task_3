from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):

    def open_first_order(self):
        self.click(FeedPageLocators.FIRST_ORDER)

    def modal_opened(self):
        return self.is_visible(FeedPageLocators.ORDER_MODAL)

    def close_modal(self):
        self.click(FeedPageLocators.CLOSE_MODAL)

    def total_counter(self):
        return int(self.get_text(FeedPageLocators.TOTAL_COUNTER))

    def today_counter(self):
        return int(self.get_text(FeedPageLocators.TODAY_COUNTER))

    def in_progress_visible(self):
        return self.is_visible(FeedPageLocators.IN_PROGRESS)