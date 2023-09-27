from behave import *
from core.lib.home import Home
from core.lib.signup import Signup


@given("user navigates to home page")
def navigate_to_home_page(context):
    home = Home(context)
    home.navigate_to_home_page()


@given("user navigates to signup page")
def navigate_to_signup_page(context):
    home = Home(context)
    home.navigate_to_signup_page()


def generate_signup_credential(context, credential):
    time = context.epoch_time
    if credential in ("valid_signup_credential", "repeated_attempt_with_valid_credential"):
        return {"firstname": "John",
                "lastname": "Smith",
                "email": "testuser{0}@lorehealth.com".format(time),
                "password": "Hello1234!",
                "confirm_password": "Hello1234!"}
    elif credential == "all_fields_empty":
        return {"firstname": "",
                "lastname": "",
                "email": "",
                "password": "",
                "confirm_password": ""}
    elif credential == "mismatched_passwords":
        return {"firstname": "John",
                "lastname": "Smith",
                "email": "testuser{0}@lorehealth.com".format(time),
                "password": "Hello1234!",
                "confirm_password": "Hello12345!"}
    elif credential == "unsupported_passwords":
        return {"firstname": "John",
                "lastname": "Smith",
                "email": "testuser{0}@lorehealth.com".format(time),
                "password": "Hello12",
                "confirm_password": "Hello12"}
    elif credential == "invalid_email_format":
        return {"firstname": "John",
                "lastname": "Smith",
                "email": "lorehealth.com",
                "password": "Hello12",
                "confirm_password": "Hello12"}


@when("user signs up with \"{credential}\"")
def signup_with_credential(context, credential):
    context.credential = generate_signup_credential(context, credential)
    signup = Signup(context)
    signup.fill_firstname(context.credential["firstname"])
    signup.fill_lastname(context.credential["lastname"])
    signup.fill_email(context.credential["email"])
    signup.fill_password(context.credential["password"])
    signup.fill_confirm_password(context.credential["confirm_password"])
    signup.click_create_account_button()


@then("sign up attempt should \"{result}\"")
def validate_signup_error_message(context, result):
    signup = Signup(context)
    if result == "pass":
        assert "Thank you for registering with Main Website Store." in signup.get_result_message()
    elif result == "fail":
        assert "There is already an account with this email address." in signup.get_result_message()


@then("\"{error}\" message prevents signup")
def signup_error_message(context, error):
    signup = Signup(context)
    if error == "required_field_error":
        assert "This is a required field." in signup.get_firstname_error_message()
        assert "This is a required field." in signup.get_lastname_error_message()
        assert "This is a required field." in signup.get_email_error_message()
        assert "This is a required field." in signup.get_password_error_message()
        assert "This is a required field." in signup.get_confirm_password_error_message()
    elif error == "invalid_email_address_error":
        assert "Please enter a valid email address (Ex: johndoe@domain.com)." \
               in signup.get_email_error_message()
    elif error == "different_value_error":
        assert "Please enter the same value again." in signup.get_confirm_password_error_message()
    elif error == "min_length_error":
        assert "Minimum length of this field must be equal or greater than 8 symbols. " \
               "Leading and trailing spaces will be ignored." in signup.get_password_error_message()
