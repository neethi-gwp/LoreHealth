import logging

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

LOGGER = logging.getLogger(__name__)


class BasePage(object):

    def __init__(self, browser, base_url="https://magento.softwaretestingboard.com/"):
        self.base_url = base_url
        self.browser = browser
        self.timeout = 5

    def navigate_to_url(self, url):
        self.browser.get(url)

    def get_current_url(self):
        return self.browser.current_url

    def navigate_to_home_page(self):
        if self.browser.current_url != self.base_url:
            self.browser.get(self.base_url)

    def wait_for_element_to_become_clickable(self, element):
        WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable(element))

    def click_element(self, element):
        self.wait_for_element_to_become_clickable(element)
        self.browser.execute_script("arguments[0].click();", element)

    def get_visible_elements(self, locator):
        elements = None
        try:
            elements = WebDriverWait(self.browser, self.timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except:
            print("Elements not visible: " + str(locator))
        return elements

    def get_present_elements(self, locator):
        elements = None
        try:
            elements = WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except:
            print("Elements not present: " + str(locator))
        return elements

    def get_elements(self, locator):
        elements = self.get_present_elements(locator)
        if not elements:
            elements = self.get_visible_elements(locator)
        if not elements:
            raise NoSuchElementException
        return elements

    def get_element(self, locator):
        if len(locator) > 2:
            index = locator[-1]
            locator = locator[:-1]
        else:
            index = 0
        elements = self.get_elements(locator)
        return elements[index]

    def clear_text_field(self, element):
        self.wait_for_element_to_become_clickable(element)
        element.clear()

    def fill_text_field_with_input(self, element, input_text):
        self.wait_for_element_to_become_clickable(element)
        element.clear()
        ActionChains(self.browser).double_click(element).perform()
        element.send_keys(input_text)

    def get_text(self, element):
        return element.text

    def select_dropdown(self, element, text):
        element = Select(element)
        element.select_by_visible_text(text)

    def open_new_tab(self):
        self.browser.execute_script("window.open('');")
        self.browser.switch_to.window(self.browser.window_handles[1])

    def close_new_tab(self):
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    def click_header_menu_item(self, menu):
        actions = ActionChains(self.browser)
        for item in menu:
            menu_item = self.browser.find_element(By.XPATH, "//span[text()='{}']".format(item))
            actions.move_to_element(menu_item).perform()

        actions.click().perform()

    def __getattr__(self, attr):
        try:
            if attr in self.locator_elements.keys():
                return self.get_element(self.locator_elements[attr])
        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(attr)
