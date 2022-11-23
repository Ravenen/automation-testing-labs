from selenium import webdriver


class Browser(object):
    _driver = None

    @property
    def driver(self):
        return self._driver if self._driver else webdriver.Chrome()
