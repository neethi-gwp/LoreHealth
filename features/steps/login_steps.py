from behave import *
from core.lib.home import Home
from core.lib.login import Login


@given("user navigates to login page")
def navigate_to_login_page(context):
    home = Home(context)
    home.navigate_to_login_page()


def generate_login_credential(context, credential):
    if credential == "valid_signup_credential":
        return {"email": "testuser{0}@lorehealth.com".format(context.epoch_time),
                "password": "Hello1234!"}
    elif credential == "valid_credential":
        return {"email": "testuser@lorehealth.com",
                "password": "Hello1234!"}
    elif credential == "invalid_credential":
        return {"email": "testuser@lorehealth.com",
                "password": "Hello12345!"}
    elif credential == "all_fields_empty":
        return {"email": "",
                "password": ""}
    elif credential == "invalid_email_format":
        return {"email": "lorehealth.com",
                "password": "Hello1234!"}


@when("user logs in with \"{credential}\"")
def login_with_credential(context, credential):
    context.credential = generate_login_credential(context, credential)
    login = Login(context)
    if "login" not in login.get_current_url():
        navigate_to_login_page(context)
    login.fill_email(context.credential["email"])
    login.fill_password(context.credential["password"])
    login.click_login_button()


@when("user logs out")
def log_out_user(context):
    home = Home(context)
    home.log_out()


@then("log in attempt should \"{result}\"")
def validate_login(context, result):
    login = Login(context)
    if result == "pass":
        assert "Welcome, " in login.get_successful_login_message()
    elif result == "fail":
        assert "The account sign-in was incorrect or your account is disabled temporarily. " \
               "Please wait and try again later." in login.get_failed_login_message()


@then("\"{error}\" message prevents login")
def validate_login_error_message(context, error):
    login = Login(context)
    if error == "required_field_error":
        assert "This is a required field." in login.get_email_error_message()
        assert "This is a required field." in login.get_password_error_message()
    elif error == "invalid_email_address_error":
        assert "Please enter a valid email address (Ex: johndoe@domain.com)." \
               in login.get_email_error_message()
