from behave import *
from core.lib.product import Product
from core.lib.cart_modal import CartModal
from core.lib.shipping import Shipping


@when("user proceeds to checkout page")
def navigate_to_checkout_page(context):
    product = Product(context)
    cart_modal = CartModal(context)
    product.navigate_to_cart()
    cart_modal.proceed_to_checkout()


@when("user proceeds to order review page")
def navigate_to_order_review_page(context):
    shipping = Shipping(context)
    shipping.navigate_to_order_review_page()


@when("user selects \"{shipping_method}\" shipping method")
def select_shipping_method(context, shipping_method):
    shipping = Shipping(context)
    if shipping_method == "no":
        return
    shipping.select_shipping_method()


def generate_shipping_info_fields(shipping_info):
    if shipping_info == "all_required_fields":
        return {"email": "testuser@lorehealth.com",
                "first_name": "John",
                "last_name": "Smith",
                "street_address": "123 St",
                "city": "gotham",
                "zip": "11111",
                "state": "New York",
                "country": "United States",
                "phone_number": "1231231234"}
    elif shipping_info == "partially_filled_fields":
        return {"email": "testuser@lorehealth.com",
                "first_name": "John",
                "last_name": "Smith",
                "street_address": "",
                "city": "",
                "zip": "",
                "state": "",
                "country": "United States",
                "phone_number": "1231231234"}
    elif shipping_info == "all_fields_empty":
        return {"email": "",
                "first_name": "",
                "last_name": "",
                "street_address": "",
                "city": "",
                "zip": "",
                "state": "",
                "country": "",
                "phone_number": ""}
    elif shipping_info == "invalid_email_format":
        return {"email": "lorehealth.com",
                "first_name": "John",
                "last_name": "Smith",
                "street_address": "123 St",
                "city": "gotham",
                "zip": "11111",
                "state": "New York",
                "country": "United States",
                "phone_number": "1231231234"}


@when("user fills \"{shipping_info}\" shipping info")
def fill_shipping_info(context, shipping_info):
    shipping_info_fields = generate_shipping_info_fields(shipping_info)
    shipping = Shipping(context)
    if not shipping.is_user_logged_in():
        shipping.input_email_address(shipping_info_fields["email"])
        shipping.input_first_name(shipping_info_fields["first_name"])
        shipping.input_last_name(shipping_info_fields["last_name"])
    shipping.input_street_address_1(shipping_info_fields["street_address"])
    shipping.input_city(shipping_info_fields["city"])
    shipping.input_zip(shipping_info_fields["zip"])
    if len(shipping_info_fields["state"]) > 0:
        shipping.select_state(shipping_info_fields["state"])
    shipping.select_country(shipping_info_fields["country"])
    shipping.input_phone_number(shipping_info_fields["phone_number"])


@then("user \"{result}\" reach order review page")
def is_order_review_page(context, result):
    shipping = Shipping(context)
    if result == "can":
        assert "payment" in shipping.get_current_url()
    else:
        assert "payment" not in shipping.get_current_url()


@then("{error_type} error message is displayed")
def validate_error_messages(context, error_type):
    shipping = Shipping(context)
    if error_type == "None":
        return
    if error_type == "shipping_method_not_selected":
        assert "The shipping method is missing. Select the shipping method and try again" in \
               shipping.get_shipping_method_error_message()
    if error_type == "required_field_error":
        assert "This is a required field." in shipping.get_required_field_error_message()
    if error_type == "invalid_email_address_error":
        assert "Please enter a valid email address (Ex: johndoe@domain.com)." in \
               shipping.get_incorrectly_formatted_email_error_message()
