from behave import *
from random import randint
from core.lib.home import Home
from core.lib.product import Product
from core.lib.cart_modal import CartModal


@given("user has added a random item to cart")
def add_random_item_to_cart(context):
    home = Home(context)
    home.navigate_to_header_menu_item("Gear,Watches")
    nth_item = randint(1, 9)
    open_nth_item_from_results(context, nth_item)
    add_item_to_cart(context)
    verify_expected_number_of_items_have_been_added_to_cart(context, 1)


@when("user filters products by \"{category}\"")
def filter_products_by_category(context, category):
    home = Home(context)
    home.navigate_to_header_menu_item(category)


@when("user opens the \"{nth}\" product")
def open_nth_item_from_results(context, nth):
    product = Product(context)
    product.navigate_to_nth_item_from_product_results(nth)


@when("user selects size \"{size}\"")
def select_item_size(context, size):
    if size == "None":
        return
    product = Product(context)
    product.select_size(size)


@when("user selects color \"{color}\"")
def select_item_color(context, color):
    if color == "None":
        return
    product = Product(context)
    product.select_color(color)


@when("user adds item to cart")
def add_item_to_cart(context):
    product = Product(context)
    product.add_item_to_cart()


def navigate_to_cart(context):
    product = Product(context)
    product.navigate_to_cart()


@when("user sets item quantity to \"{quantity}\"")
def set_item_quantity(context, quantity):
    product = Product(context)
    product.set_item_quantity(quantity)


@when("users sets \"{quantity}\" and adds item to cart")
def set_quantity_and_add_to_cart(context, quantity):
    quantity_list = quantity.split(',')
    for num in quantity_list:
        set_item_quantity(context, num)
        add_item_to_cart(context)


@then("verify \"{item_name}\" \"{size}\" \"{color}\" \"{item_num}\" has been added to cart")
def verify_expected_item_has_been_added_to_cart(context, item_name, size, color, item_num):
    if item_num == "0":
        return
    product = Product(context)
    product.open_cart_modal()
    cart_modal = CartModal(context)
    assert item_name in cart_modal.get_item_name_in_cart()
    if size != "None" or color != "None":
        cart_modal.click_product_options_toggle_in_cart()
    if size != "None":
        assert size in cart_modal.get_item_options_in_cart()
    if color != "None":
        assert color in cart_modal.get_item_options_in_cart()


@then("verify \"{expected_number_in_cart}\" items added to cart")
def verify_expected_number_of_items_have_been_added_to_cart(context, number):
    product = Product(context)
    if number == "0":
        verify_cart_is_empty(context)
    else:
        assert int(product.get_total_item_quantity_in_cart()) == int(number)


@then("verify cart is empty")
def verify_cart_is_empty(context):
    product = Product(context)
    product.open_cart_modal()
    cart_modal = CartModal(context)
    assert "You have no items in your shopping cart." in cart_modal.get_empty_cart_modal_content()


@then("\"{notification_type}\" is displayed to user")
def validate_notification_message(context, notification_type):
    product = Product(context)
    if notification_type == "success":
        assert "You added" in product.get_message_displayed_to_user()
        assert "to your shopping cart." in product.get_message_displayed_to_user()
    elif notification_type == "maximum_limit":
        assert "The requested qty exceeds the maximum qty allowed in shopping cart" in \
               product.get_message_displayed_to_user()
    elif notification_type == "out_of_stock":
        assert "The requested qty is not available" in product.get_message_displayed_to_user()
