from selenium.webdriver.common.by import By
from core.page_objects.base_page import BasePage


class ShippingPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    locator_elements = {
        "email_address": (By.ID, "customer-email"),
        "first_name": (By.NAME, "firstname"),
        "last_name": (By.NAME, "lastname"),
        "company": (By.NAME, "company"),
        "street_address_1": (By.NAME, "street[0]"),
        "street_address_2": (By.NAME, "street[1]"),
        "street_address_3": (By.NAME, "street[2]"),
        "city": (By.NAME, "city"),
        "state": (By.NAME, "region_id"),
        "zip": (By.NAME, "postcode"),
        "country": (By.NAME, "country_id"),
        "phone_number": (By.NAME, "telephone"),
        "shipping_method": (By.CLASS_NAME, "radio"),
        "order_summary": (By.CLASS_NAME, "opc-block-summary"),
        "next_button": (By.CLASS_NAME, "button.action.continue.primary"),
        "shipping_method_error_message": (By.CLASS_NAME, "message.notice"),
        "required_field_error": (By.CLASS_NAME, "field-error"),
        "incorrectly_formatted_email_error": (By.ID, "customer-email-error"),
        "login_link": (By.CLASS_NAME, "authentication-wrapper")
    }