from selenium.webdriver.common.by import By
from core.page_objects.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    locator_elements = {
        "login_link": (By.LINK_TEXT, "Sign In"),
        "signup_link": (By.LINK_TEXT, "Create an Account"),
        "logged_in": (By.CLASS_NAME, "logged-in"),
        "user_account_dropdown": (By.CLASS_NAME, "customer-name"),
        "user_sign_out_link": (By.LINK_TEXT, "Sign Out")
    }
