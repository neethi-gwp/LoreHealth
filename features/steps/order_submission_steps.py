from behave import *
from core.lib.order import Order


@when("user places the order")
def place_order(context):
    order = Order(context)
    order.place_order()


@then("order should be placed successfully")
def verify_order_placed(context):
    order = Order(context)
    assert "Thank you for your purchase!" in order.get_order_success_message()
    assert "Your order number is:" in order.get_order_number_message()
