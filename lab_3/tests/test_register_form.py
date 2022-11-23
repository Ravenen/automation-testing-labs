import unittest

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

from lab_3.pages.register_page import RegisterPage


class TestRegisterForm(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.register_page = RegisterPage(self.driver)
        self.driver.get(self.register_page.URL)
        faker = Faker()
        self.user_data = {
            'first_name': faker.first_name(),
            'middle_name': faker.first_name(),
            'last_name': faker.last_name(),
            'email_address': faker.email(),
            'password': faker.password()
        }

    def tearDown(self) -> None:
        self.driver.quit()

    def _map_data_to_inputs(self, user_data):
        self.register_page.get_first_name_field().send_keys(user_data.get('first_name'))
        self.register_page.get_middle_name_field().send_keys(user_data.get('middle_name'))
        self.register_page.get_last_name_field().send_keys(user_data.get('last_name'))
        self.register_page.get_email_field().send_keys(user_data.get('email_address'))
        self.register_page.get_password_field().send_keys(user_data.get('password'))
        self.register_page.get_confirm_password_field().send_keys(user_data.get('password'))

    def test_should_succeed_when_full_inputs_correct(self):
        self._map_data_to_inputs(self.user_data)
        self.register_page.get_register_button().click()
        self.assertEqual('Thank you for registering with Madison Island.',
                         self.driver.find_element(By.CLASS_NAME, 'success-msg').text)

    def test_should_succeed_when_no_middle_name(self):
        self.user_data['middle_name'] = ''
        self._map_data_to_inputs(self.user_data)
        self.register_page.get_register_button().click()
        self.assertEqual('Thank you for registering with Madison Island.',
                         self.driver.find_element(By.CLASS_NAME, 'success-msg').text)

    def test_should_fail_when_no_first_name(self):
        self.user_data['first_name'] = ''
        self._map_data_to_inputs(self.user_data)
        self.register_page.get_register_button().click()
        self.assertEqual('This is a required field.',
                         self.register_page.get_error_for(self.register_page.get_first_name_field()).text)

    def test_should_fail_when_no_last_name(self):
        self.user_data['last_name'] = ''
        self._map_data_to_inputs(self.user_data)
        self.register_page.get_register_button().click()
        self.assertEqual('This is a required field.',
                         self.register_page.get_error_for(self.register_page.get_last_name_field()).text)

    def test_should_fail_when_no_email(self):
        self.user_data['email_address'] = ''
        self._map_data_to_inputs(self.user_data)
        self.register_page.get_register_button().click()
        self.assertEqual('This is a required field.',
                         self.register_page.get_error_for(self.register_page.get_email_field()).text)

    def test_should_fail_when_no_password(self):
        self._map_data_to_inputs(self.user_data)
        self.register_page.get_password_field().clear()
        self.register_page.get_register_button().click()
        self.assertEqual('This is a required field.',
                         self.register_page.get_error_for(self.register_page.get_password_field()).text)

    def test_should_fail_when_no_confirm_password(self):
        self._map_data_to_inputs(self.user_data)
        self.register_page.get_confirm_password_field().clear()
        self.register_page.get_register_button().click()
        self.assertEqual('This is a required field.',
                         self.register_page.get_error_for(self.register_page.get_confirm_password_field()).text)

    def test_should_fail_when_short_password(self):
        self.user_data['password'] = '123'
        self._map_data_to_inputs(self.user_data)
        self.register_page.get_register_button().click()
        self.assertEqual('Please enter 6 or more characters. Leading or trailing spaces will be ignored.',
                         self.register_page.get_error_for(self.register_page.get_password_field()).text)

    def test_should_fail_when_wrong_confirm_password(self):
        self._map_data_to_inputs(self.user_data)
        self.register_page.get_confirm_password_field().clear()
        self.register_page.get_confirm_password_field().send_keys(self.user_data.get('password') + 'salt')
        self.register_page.get_register_button().click()
        self.assertEqual('Please make sure your passwords match.',
                         self.register_page.get_error_for(self.register_page.get_confirm_password_field()).text)

    def test_should_fail_when_no_at_sign_in_email(self):
        self.user_data['email_address'] = 'test'
        self._map_data_to_inputs(self.user_data)
        self.register_page.get_register_button().click()
        self.assertNotEqual('', self.register_page.get_email_field().get_attribute("validationMessage"))

    def test_should_fail_when_wrong_domain_in_email(self):
        self.user_data['email_address'] = 'test@test'
        self._map_data_to_inputs(self.user_data)
        self.register_page.get_register_button().click()
        self.assertEqual('Please enter a valid email address. For example johndoe@domain.com.',
                         self.register_page.get_error_for(self.register_page.get_email_field()).text)

    def test_should_fail_when_same_email(self):
        self._map_data_to_inputs(self.user_data)
        self.register_page.get_register_button().click()
        self.driver.delete_all_cookies()
        self.driver.get(self.register_page.URL)
        self._map_data_to_inputs(self.user_data)
        self.register_page.get_register_button().click()
        self.assertEqual('There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account.',
                         self.driver.find_element(By.CLASS_NAME, 'error-msg').text)
