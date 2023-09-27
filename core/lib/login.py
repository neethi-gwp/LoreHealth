from core.page_objects.login_page import LoginPage


class Login(LoginPage):
    def __init__(self, context):
        LoginPage.__init__(
            self,
            context)

    def fill_email(self, email):
        self.fill_text_field_with_input(self.email, email)

    def fill_password(self, password):
        self.fill_text_field_with_input(self.password, password)

    def click_login_button(self):
        return self.click_element(self.login_button)

    def get_email_error_message(self):
        return self.get_text(self.email_error_message)

    def get_password_error_message(self):
        return self.get_text(self.password_error_message)

    def get_successful_login_message(self):
        return self.get_text(self.successful_login_message)

    def get_failed_login_message(self):
        return self.get_text(self.failed_login_message)
