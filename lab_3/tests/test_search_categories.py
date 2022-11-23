import unittest

from selenium import webdriver

from lab_3.pages.base_page import BasePage


class TestSearchCategories(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.base_page = BasePage(self.driver)
        self.driver.get(self.base_page.URL)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_should_succeed_when_navigate_to_women(self):
        self.base_page.get_women_nav().click()
        self.assertEqual(self.base_page.URL + 'women.html', self.driver.current_url,
                         'Women category does not lead to women products page')

    def test_should_succeed_when_navigate_to_men(self):
        self.base_page.get_men_nav().click()
        self.assertEqual(self.base_page.URL + 'men.html', self.driver.current_url,
                         'Men category does not lead to men products page')

    def test_should_succeed_when_navigate_to_accessories(self):
        self.base_page.get_accessories_nav().click()
        self.assertEqual(self.base_page.URL + 'accessories.html', self.driver.current_url,
                         'Accessories category does not lead to accessories products page')

    def test_should_succeed_when_navigate_to_home_and_decor(self):
        self.base_page.get_home_and_decor_nav().click()
        self.assertEqual(self.base_page.URL + 'home-decor.html', self.driver.current_url,
                         'Home & Decor category does not lead to home-decor products page')

    def test_should_succeed_when_navigate_to_sale(self):
        self.base_page.get_sale_nav().click()
        self.assertEqual(self.base_page.URL + 'sale.html', self.driver.current_url,
                         'Sale category does not lead to sale products page')

    def test_should_succeed_when_navigate_to_vip(self):
        self.base_page.get_vip_nav().click()
        self.assertEqual(self.base_page.URL + 'vip.html', self.driver.current_url,
                         'VIP category does not lead to VIP products page')

    def test_should_succeed_when_search_for_men_shirt(self):
        self.base_page.get_search().send_keys('men shirt')
        self.base_page.get_search_button().click()

        self.assertTrue('Men' in self.base_page.get_search_category_box().text,
                        'There is no Men category in men shirt search results')

    def test_should_succeed_when_search_for_boot(self):
        self.base_page.get_search().send_keys('boot')
        self.base_page.get_search_button().click()

        self.assertTrue('Accessories' in self.base_page.get_search_category_box().text,
                        'There is no Accessories category in boot search results')
