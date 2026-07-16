from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    def open_order(self):
        self.click(OrderFeedLocators.FIRST_ORDER)

    def modal_visible(self):
        return self.is_visible(OrderFeedLocators.ORDER_MODAL)

    def total_orders(self):
        return self.get_text(OrderFeedLocators.TOTAL_COUNTER)

    def today_orders(self):
        return self.get_text(OrderFeedLocators.TODAY_COUNTER)

    def orders_in_progress_visible(self):
        return self.is_visible(OrderFeedLocators.IN_PROGRESS)