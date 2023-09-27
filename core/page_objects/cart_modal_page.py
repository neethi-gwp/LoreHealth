from selenium.webdriver.common.by import By
from core.page_objects.base_page import BasePage


class CartModalPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    locator_elements = {
        "checkout_button": (By.XPATH, "//span[text()='Proceed to Checkout']"),
        "view_and_edit_cart_link": (By.CLASS_NAME, "action.viewcart"),
        "total_number_of_items": (By.CLASS_NAME, "items-total"),
        "cart_modal_content": (By.CLASS_NAME, "minicart-items"),
        "empty_cart_modal_content": (By.ID, "minicart-content-wrapper"),
        "product_name_in_cart": (By.CLASS_NAME, "product-item-name"),
        "product_options_toggle_in_cart": (By.CLASS_NAME, "product.options"),
        "product_options_in_cart": (By.CLASS_NAME, "product.options.list")
    }
