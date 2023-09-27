import time

from core.page_objects.cart_modal_page import CartModalPage


class CartModal(CartModalPage):
    def __init__(self, context):
        CartModalPage.__init__(
            self,
            context)

    def get_empty_cart_modal_content(self):
        return self.get_text(self.empty_cart_modal_content)

    def proceed_to_checkout(self):
        self.click_element(self.checkout_button)
        time.sleep(3)

    def view_and_edit_cart(self):
        self.click_element(self.view_and_edit_cart_link)

    def click_product_options_toggle_in_cart(self):
        self.product_options_toggle_in_cart.click()

    def get_item_name_in_cart(self):
        return self.get_text(self.product_name_in_cart)

    def get_item_options_in_cart(self):
        return self.get_text(self.product_options_in_cart)
