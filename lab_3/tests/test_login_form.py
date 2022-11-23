import unittest

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

from lab_3.pages.login_page import LoginPage
from lab_3.pages.register_page import RegisterPage


class TestLoginForm(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        register_page = RegisterPage(self.driver)
        self.driver.get(register_page.URL)
        faker = Faker()
        self.user_data = {
            'first_name': faker.first_name(),
            'middle_name': faker.first_name(),
            'last_name': faker.last_name(),
            'email_address': faker.email(),
            'password': faker.password()
        }
        register_page.get_first_name_field().send_keys(self.user_data.get('first_name'))
        register_page.get_middle_name_field().send_keys(self.user_data.get('middle_name'))
        register_page.get_last_name_field().send_keys(self.user_data.get('last_name'))
        register_page.get_email_field().send_keys(self.user_data.get('email_address'))
        register_page.get_password_field().send_keys(self.user_data.get('password'))
        register_page.get_confirm_password_field().send_keys(self.user_data.get('password'))
        register_page.get_register_button().click()
        self.driver.delete_all_cookies()
        self.login_page = LoginPage(self.driver)
        self.driver.get(self.login_page.URL)

    def tearDown(self) -> None:
        self.driver.quit()

    def _map_data_to_inputs(self, user_data):
        self.login_page.get_email_field().send_keys(user_data.get('email_address'))
        self.login_page.get_password_field().send_keys(user_data.get('password'))

    def test_should_succeed_when_full_inputs_correct(self):
        self._map_data_to_inputs(self.user_data)
        self.login_page.get_login_button().click()
        self.assertEqual('http://demo-store.seleniumacademy.com/customer/account/',
                         self.driver.current_url)

    def test_should_fail_when_no_email(self):
        self.user_data['email_address'] = ''
        self._map_data_to_inputs(self.user_data)
        self.login_page.get_login_button().click()
        self.assertEqual('This is a required field.',
                         self.login_page.get_error_for(self.login_page.get_email_field()).text)

    def test_should_fail_when_no_password(self):
        self.user_data['password'] = ''
        self._map_data_to_inputs(self.user_data)
        self.login_page.get_login_button().click()
        self.assertEqual('This is a required field.',
                         self.login_page.get_error_for(self.login_page.get_password_field()).text)

    def test_should_fail_when_short_password(self):
        self.user_data['password'] = '123'
        self._map_data_to_inputs(self.user_data)
        self.login_page.get_login_button().click()
        self.assertEqual('Please enter 6 or more characters. Leading or trailing spaces will be ignored.',
                         self.login_page.get_error_for(self.login_page.get_password_field()).text)

    def test_should_fail_when_no_at_sign_in_email(self):
        self.user_data['email_address'] = 'test'
        self._map_data_to_inputs(self.user_data)
        self.login_page.get_login_button().click()
        self.assertNotEqual('', self.login_page.get_email_field().get_attribute("validationMessage"))

    def test_should_fail_when_wrong_domain_in_email(self):
        self.user_data['email_address'] = 'test@test'
        self._map_data_to_inputs(self.user_data)
        self.login_page.get_login_button().click()
        self.assertEqual('Please enter a valid email address. For example johndoe@domain.com.',
                         self.login_page.get_error_for(self.login_page.get_email_field()).text)

    def test_should_fail_when_wrong_email(self):
        self.user_data['email_address'] = 'wrong' + self.user_data['email_address']
        self._map_data_to_inputs(self.user_data)
        self.login_page.get_login_button().click()
        self.assertEqual('Invalid login or password.',
                         self.driver.find_element(By.CLASS_NAME, 'error-msg').text)

    def test_should_fail_when_wrong_password(self):
        self.user_data['password'] = 'wrong' + self.user_data['password']
        self._map_data_to_inputs(self.user_data)
        self.login_page.get_login_button().click()
        self.assertEqual('Invalid login or password.',
                         self.driver.find_element(By.CLASS_NAME, 'error-msg').text)
