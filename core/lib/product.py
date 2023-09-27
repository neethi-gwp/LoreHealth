import time

from core.page_objects.product_page import ProductPage


class Product(ProductPage):
    def __init__(self, context):
        ProductPage.__init__(
            self,
            context)

    def navigate_to_nth_item_from_product_results(self, n):
        element = self.get_element(self.locator_elements["filtered_products"] + (int(n)-1,))
        element.click()

    def select_size(self, size):
        locator_tuple = self.locator_elements["size"]
        element = self.get_element((locator_tuple[0], locator_tuple[1].format(size)))
        element.click()

    def select_color(self, color):
        locator_tuple = self.locator_elements["color"]
        element = self.get_element((locator_tuple[0], locator_tuple[1].format(color)))
        element.click()

    def add_item_to_cart(self):
        self.click_element(self.add_item_to_cart_button)
        time.sleep(5)

    def navigate_to_cart(self):
        self.click_element(self.cart_page_link)

    def set_item_quantity(self, quantity):
        self.fill_text_field_with_input(self.item_quantity_input_field, quantity)

    def get_total_item_quantity_in_cart(self):
        return self.get_text(self.cart_quantity)

    def get_message_displayed_to_user(self):
        return self.get_text(self.message_notification)

    def open_cart_modal(self):
        self.click_element(self.cart_icon)