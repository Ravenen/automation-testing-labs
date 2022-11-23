import unittest

from lab_3.tests.test_contacts_form import TestContactsForm
from lab_3.tests.test_login_form import TestLoginForm
from lab_3.tests.test_register_form import TestRegisterForm
from lab_3.tests.test_register_page_open import TestRegisterPageOpen
from lab_3.tests.test_search_categories import TestSearchCategories

if __name__ == '__main__':
    test_suite = unittest.TestSuite()

    test_suite.addTests({
        unittest.defaultTestLoader.loadTestsFromTestCase(TestSearchCategories),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestRegisterPageOpen),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestRegisterForm),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestLoginForm),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestContactsForm),
    })
