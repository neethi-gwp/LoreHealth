from selenium.webdriver.common.by import By
from core.page_objects.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    locator_elements = {
        "place_order_button": (By.CLASS_NAME, "action.primary.checkout"),
        "checkout_error_message": (By.CLASS_NAME, "message.message-error.error"),
        "order_success_message": (By.CLASS_NAME, "base"),
        "order_number_message": (By.CLASS_NAME, "checkout-success")
    }
