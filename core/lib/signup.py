from core.page_objects.signup_page import SignupPage


class Signup(SignupPage):
    def __init__(self, context):
        SignupPage.__init__(
            self,
            context)

    def fill_firstname(self, firstname):
        self.fill_text_field_with_input(self.first_name, firstname)

    def fill_lastname(self, lastname):
        self.fill_text_field_with_input(self.last_name, lastname)

    def fill_email(self, email):
        self.fill_text_field_with_input(self.email, email)

    def fill_password(self, password):
        self.fill_text_field_with_input(self.password, password)

    def fill_confirm_password(self, confirm_password):
        self.fill_text_field_with_input(self.confirm_password, confirm_password)

    def click_create_account_button(self):
        self.click_element(self.create_account_button)

    def get_firstname_error_message(self):
        return self.get_text(self.first_name_error_message)

    def get_lastname_error_message(self):
        return self.get_text(self.last_name_error_message)

    def get_email_error_message(self):
        return self.get_text(self.email_error_message)

    def get_password_error_message(self):
        return self.get_text(self.password_error_message)

    def get_confirm_password_error_message(self):
        return self.get_text(self.confirm_password_error_message)

    def get_result_message(self):
        return self.get_text(self.result_message)
