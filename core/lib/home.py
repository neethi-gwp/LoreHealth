from core.page_objects.home_page import HomePage


class Home(HomePage):
    def __init__(self, context):
        HomePage.__init__(
            self,
            context)
        self.navigate_to_home_page()

    def navigate_to_signup_page(self):
        self.click_element(self.signup_link)

    def navigate_to_login_page(self):
        self.click_element(self.login_link)

    def navigate_to_header_menu_item(self, menu_tree_string):
        menu = menu_tree_string.split(',')
        self.click_header_menu_item(menu)

    def is_user_logged_in(self):
        return self.logged_in.is_displayed()

    def log_out(self):
        if self.is_user_logged_in():
            self.click_element(self.user_account_dropdown)
            self.click_element(self.user_sign_out_link)
