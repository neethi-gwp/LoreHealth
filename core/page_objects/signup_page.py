from selenium.webdriver.common.by import By
from core.page_objects.base_page import BasePage


class SignupPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    locator_elements = {
        "first_name": (By.ID, "firstname"),
        "last_name": (By.ID, "lastname"),
        "email": (By.ID, "email_address"),
        "password": (By.ID, "password"),
        "confirm_password": (By.ID, "password-confirmation"),
        "create_account_button": (By.CLASS_NAME, "action.submit.primary"),
        "first_name_error_message": (By.ID, "firstname-error"),
        "last_name_error_message": (By.ID, "lastname-error"),
        "email_error_message": (By.ID, "email_address-error"),
        "password_error_message": (By.ID, "password-error"),
        "confirm_password_error_message": (By.ID, "password-confirmation-error"),
        "result_message": (By.CLASS_NAME, "page.messages")
    }
