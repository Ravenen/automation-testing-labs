import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from lab_3.pages.base_page import BasePage
from lab_3.pages.register_page import RegisterPage


class TestRegisterPageOpen(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.base_page = BasePage(self.driver)
        self.driver.get(self.base_page.URL)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_should_succeed_when_open_from_account_dropdown(self):
        self.base_page.get_account().click()
        self.base_page.get_account_dropdown_register().click()
        self.assertEqual(RegisterPage.URL, self.driver.current_url)

    def test_should_succeed_when_open_from_account_login_page(self):
        self.base_page.get_account().click()
        self.base_page.get_account_dropdown_login().click()
        self.driver.find_element(By.XPATH, '//*[@id="login-form"]/div/div[1]/div[2]/a').click()
        self.assertEqual(RegisterPage.URL, self.driver.current_url)
