from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):
    URL = 'http://demo-store.seleniumacademy.com/'

    SEARCH_SELECTOR = (By.ID, 'search')
    SEARCH_BUTTON_SELECTOR = (By.CSS_SELECTOR, "button[type='submit'][title='Search']")
    SEARCH_CATEGORY_SELECTOR = (By.XPATH, '//*[@id="narrow-by-list"]/dd/ol')

    WOMEN_NAV_SELECTOR = (By.XPATH, '//*[@id="nav"]/ol/li[1]/a')
    MEN_NAV_SELECTOR = (By.XPATH, '//*[@id="nav"]/ol/li[2]/a')
    ACCESSORIES_NAV_SELECTOR = (By.XPATH, '//*[@id="nav"]/ol/li[3]/a')
    HOME_AND_DECOR_NAV_SELECTOR = (By.XPATH, '//*[@id="nav"]/ol/li[4]/a')
    SALE_NAV_SELECTOR = (By.XPATH, '//*[@id="nav"]/ol/li[5]/a')
    VIP_NAV_SELECTOR = (By.XPATH, '//*[@id="nav"]/ol/li[6]/a')

    ACCOUNT_SELECTOR = (By.XPATH, '//*[@id="header"]/div/div[2]/div/a')
    ACCOUNT_DD_REGISTER_SELECTOR = (By.XPATH, '//*[@id="header-account"]/div/ul/li[5]/a')
    ACCOUNT_DD_LOGIN_SELECTOR = (By.XPATH, '//*[@id="header-account"]/div/ul/li[6]/a')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _find(self, selector):
        return self.driver.find_element(*selector)

    def get_search(self):
        return self._find(self.SEARCH_SELECTOR)

    def get_search_button(self):
        return self._find(self.SEARCH_BUTTON_SELECTOR)

    def get_search_category_box(self):
        return self._find(self.SEARCH_CATEGORY_SELECTOR)

    def get_women_nav(self):
        return self._find(self.WOMEN_NAV_SELECTOR)

    def get_men_nav(self):
        return self._find(self.MEN_NAV_SELECTOR)

    def get_accessories_nav(self):
        return self._find(self.ACCESSORIES_NAV_SELECTOR)

    def get_home_and_decor_nav(self):
        return self._find(self.HOME_AND_DECOR_NAV_SELECTOR)

    def get_sale_nav(self):
        return self._find(self.SALE_NAV_SELECTOR)

    def get_vip_nav(self):
        return self._find(self.VIP_NAV_SELECTOR)

    def get_account(self):
        return self._find(self.ACCOUNT_SELECTOR)

    def get_account_dropdown_register(self):
        return self._find(self.ACCOUNT_DD_REGISTER_SELECTOR)

    def get_account_dropdown_login(self):
        return self._find(self.ACCOUNT_DD_LOGIN_SELECTOR)
