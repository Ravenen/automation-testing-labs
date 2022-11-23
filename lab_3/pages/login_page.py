from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lab_3.pages.base_page import BasePage


class LoginPage(BasePage):
    URL = BasePage.URL + 'customer/account/login/'

    EMAIL_FIELD_SELECTOR = (By.ID, 'email')
    PASSWORD_FIELD_SELECTOR = (By.ID, 'pass')
    LOGIN_BUTTON_SELECTOR = (By.ID, 'send2')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_email_field(self):
        return self._find(self.EMAIL_FIELD_SELECTOR)

    def get_password_field(self):
        return self._find(self.PASSWORD_FIELD_SELECTOR)

    def get_login_button(self):
        return self._find(self.LOGIN_BUTTON_SELECTOR)

    def get_error_for(self, element: WebElement):
        return element.find_element(By.XPATH, "following-sibling::*")
