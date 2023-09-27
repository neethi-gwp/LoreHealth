from selenium.webdriver.common.by import By
from core.page_objects.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    locator_elements = {
        "email": (By.ID, "email"),
        "password": (By.ID, "pass"),
        "login_button": (By.ID, "send2"),
        "email_error_message": (By.ID, "email-error"),
        "password_error_message": (By.ID, "pass-error"),
        "successful_login_message": (By.CLASS_NAME, "logged-in"),
        "failed_login_message": (By.CLASS_NAME, "page.messages")
    }
