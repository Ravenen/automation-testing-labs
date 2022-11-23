import unittest

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

from lab_3.pages.contacts_page import ContactsPage


class TestContactsForm(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.contacts_page = ContactsPage(self.driver)
        self.driver.get(self.contacts_page.URL)
        faker = Faker()
        self.user_data = {
            'name': faker.name(),
            'email_address': faker.email(),
            'telephone': faker.phone_number(),
            'comment': faker.sentence()
        }

    def tearDown(self) -> None:
        self.driver.quit()

    def _map_data_to_inputs(self, user_data):
        self.contacts_page.get_name_field().send_keys(user_data.get('name'))
        self.contacts_page.get_email_field().send_keys(user_data.get('email_address'))
        self.contacts_page.get_telephone_field().send_keys(user_data.get('telephone'))
        self.contacts_page.get_comment_field().send_keys(user_data.get('comment'))

    def test_should_succeed_when_full_inputs_correct(self):
        self._map_data_to_inputs(self.user_data)
        self.contacts_page.get_submit_button().click()
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, 'success-msg').is_displayed())

    def test_should_succeed_when_no_telephone(self):
        self.user_data['telephone'] = ''
        self._map_data_to_inputs(self.user_data)
        self.contacts_page.get_submit_button().click()
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, 'success-msg').is_displayed())

    def test_should_fail_when_no_name(self):
        self.user_data['name'] = ''
        self._map_data_to_inputs(self.user_data)
        self.contacts_page.get_submit_button().click()
        self.assertEqual('This is a required field.',
                         self.contacts_page.get_error_for(self.contacts_page.get_name_field()).text)

    def test_should_fail_when_no_email(self):
        self.user_data['email_address'] = ''
        self._map_data_to_inputs(self.user_data)
        self.contacts_page.get_submit_button().click()
        self.assertEqual('This is a required field.',
                         self.contacts_page.get_error_for(self.contacts_page.get_email_field()).text)

    def test_should_fail_when_no_comment(self):
        self.user_data['comment'] = ''
        self._map_data_to_inputs(self.user_data)
        self.contacts_page.get_submit_button().click()
        self.assertEqual('This is a required field.',
                         self.contacts_page.get_error_for(self.contacts_page.get_comment_field()).text)

    def test_should_fail_when_no_at_sign_in_email(self):
        self.user_data['email_address'] = 'test'
        self._map_data_to_inputs(self.user_data)
        self.contacts_page.get_submit_button().click()
        self.assertNotEqual('', self.contacts_page.get_email_field().get_attribute("validationMessage"))

    def test_should_fail_when_wrong_domain_in_email(self):
        self.user_data['email_address'] = 'test@test'
        self._map_data_to_inputs(self.user_data)
        self.contacts_page.get_submit_button().click()
        self.assertEqual('Please enter a valid email address. For example johndoe@domain.com.',
                         self.contacts_page.get_error_for(self.contacts_page.get_email_field()).text)
