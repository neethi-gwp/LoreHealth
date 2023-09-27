import time

from core.page_objects.order_page import OrderPage


class Order(OrderPage):
    def __init__(self, context):
        OrderPage.__init__(
            self,
            context)

    def place_order(self):
        self.click_element(self.place_order_button)
        time.sleep(3)

    def get_order_success_message(self):
        return self.get_text(self.order_success_message)

    def get_order_number_message(self):
        return self.get_text(self.order_number_message)