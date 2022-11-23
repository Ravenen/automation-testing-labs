from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lab_3.pages.base_page import BasePage


class ContactsPage(BasePage):
    URL = BasePage.URL + 'contacts/'

    NAME_FIELD_SELECTOR = (By.ID, 'name')
    EMAIL_FIELD_SELECTOR = (By.ID, 'email')
    TELEPHONE_FIELD_SELECTOR = (By.ID, 'telephone')
    COMMENT_FIELD_SELECTOR = (By.ID, 'comment')
    SUBMIT_BUTTON_SELECTOR = (By.CSS_SELECTOR, "button[type='submit'][title='Submit']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_name_field(self):
        return self._find(self.NAME_FIELD_SELECTOR)

    def get_email_field(self):
        return self._find(self.EMAIL_FIELD_SELECTOR)

    def get_telephone_field(self):
        return self._find(self.TELEPHONE_FIELD_SELECTOR)

    def get_comment_field(self):
        return self._find(self.COMMENT_FIELD_SELECTOR)

    def get_submit_button(self):
        return self._find(self.SUBMIT_BUTTON_SELECTOR)

    def get_error_for(self, element: WebElement):
        return element.find_element(By.XPATH, "following-sibling::*")
