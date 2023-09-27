from selenium.webdriver.common.by import By
from core.page_objects.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    locator_elements = {
        "filtered_products": (By.CLASS_NAME, "product-item-info"),
        "size": (By.XPATH, "//div[@option-label=\"{}\"]"),
        "color": (By.XPATH, "//div[@option-label=\"{}\"]"),
        "add_item_to_cart_button": (By.ID, "product-addtocart-button"),
        "item_quantity_input_field": (By.ID, "qty"),
        "message_notification": (By.CLASS_NAME, "page.messages"),
        "cart_page_link": (By.LINK_TEXT, "shopping cart"),
        "cart_icon": (By.CLASS_NAME, "action.showcart"),
        "cart_quantity": (By.CLASS_NAME, "counter-number"),
    }
