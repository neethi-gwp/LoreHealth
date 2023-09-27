import time

from core.page_objects.shipping_page import ShippingPage


class Shipping(ShippingPage):
    def __init__(self, context):
        ShippingPage.__init__(
            self,
            context)

    def navigate_to_order_review_page(self):
        self.click_element(self.next_button)
        time.sleep(3)

    def input_email_address(self, email_address):
        self.fill_text_field_with_input(self.email_address, email_address)

    def input_first_name(self, first_name):
        self.fill_text_field_with_input(self.first_name, first_name)

    def input_last_name(self, last_name):
        self.fill_text_field_with_input(self.last_name, last_name)

    def input_company(self, company):
        self.fill_text_field_with_input(self.company, company)

    def input_street_address_1(self, street_address_1):
        self.fill_text_field_with_input(self.street_address_1, street_address_1)

    def input_street_address_2(self, street_address_2):
        self.fill_text_field_with_input(self.street_address_2, street_address_2)

    def input_street_address_3(self, street_address_3):
        self.fill_text_field_with_input(self.street_address_3, street_address_3)

    def input_city(self, city):
        self.fill_text_field_with_input(self.city, city)

    def input_zip(self, zip):
        self.fill_text_field_with_input(self.zip, zip)

    def input_phone_number(self, phone_number):
        self.fill_text_field_with_input(self.phone_number, phone_number)

    def select_state(self, state):
        self.select_dropdown(self.state, state)

    def select_country(self, country):
        self.select_dropdown(self.country, country)

    def get_number_of_items_in_order_summary(self):
        return self.get_text(self.order_summary)

    def select_shipping_method(self):
        self.click_element(self.shipping_method)

    def get_shipping_method_error_message(self):
        return self.get_text(self.shipping_method_error_message)

    def get_required_field_error_message(self):
        return self.get_text(self.required_field_error)

    def get_incorrectly_formatted_email_error_message(self):
        return self.get_text(self.incorrectly_formatted_email_error)

    def is_user_logged_in(self):
        return not self.login_link.is_displayed()
