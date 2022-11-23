from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lab_3.pages.base_page import BasePage


class RegisterPage(BasePage):
    URL = BasePage.URL + 'customer/account/create/'

    FIRST_NAME_FIELD_SELECTOR = (By.ID, 'firstname')
    MIDDLE_NAME_FIELD_SELECTOR = (By.ID, 'middlename')
    LAST_NAME_FIELD_SELECTOR = (By.ID, 'lastname')
    EMAIL_FIELD_SELECTOR = (By.ID, 'email_address')
    PASSWORD_FIELD_SELECTOR = (By.ID, 'password')
    CONFIRM_PASSWORD_FIELD_SELECTOR = (By.ID, 'confirmation')
    REGISTER_BUTTON_SELECTOR = (By.CSS_SELECTOR, "button[type='submit'][title='Register']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_first_name_field(self):
        return self._find(self.FIRST_NAME_FIELD_SELECTOR)

    def get_middle_name_field(self):
        return self._find(self.MIDDLE_NAME_FIELD_SELECTOR)

    def get_last_name_field(self):
        return self._find(self.LAST_NAME_FIELD_SELECTOR)

    def get_email_field(self):
        return self._find(self.EMAIL_FIELD_SELECTOR)

    def get_password_field(self):
        return self._find(self.PASSWORD_FIELD_SELECTOR)

    def get_confirm_password_field(self):
        return self._find(self.CONFIRM_PASSWORD_FIELD_SELECTOR)

    def get_register_button(self):
        return self._find(self.REGISTER_BUTTON_SELECTOR)

    def get_error_for(self, element: WebElement):
        return element.find_element(By.XPATH, "following-sibling::*")
