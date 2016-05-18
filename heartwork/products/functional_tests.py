__author__ = 'dimitris'
from selenium import webdriver
import unittest
import time
from django.conf import settings

class NewTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.browser.implicitly_wait(13)

    def tearDown(self):
        self.browser.quit()

    def test_it(self):
        # self.browser.get('http://localhost:8000/products/')
        # self.assertIn('Static Top Navbar Example for Bootstrap', self.browser.title)
        # time.sleep(3)
        self.browser.get('http://localhost:8000/admin/')

        admin_name = self.browser.find_element_by_id('id_username')
        admin_name.send_keys('dimitris.rongotis@gmail.com')
        password = self.browser.find_element_by_id('id_password')
        password.send_keys('1')
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()
        time.sleep(3)
        self.browser.get('http://localhost:8000/admin/')
        time.sleep(3)
        self.browser.get('http://localhost:8000/admin/products/product/')
        time.sleep(2)
        self.browser.get('http://localhost:8000/admin/products/product/add/')
        title = self.browser.find_element_by_id("id_title")
        title.send_keys('Selenium Product')
        price = self.browser.find_element_by_id('id_price')
        price.send_keys('50.00')
        sales_price = self.browser.find_element_by_id('id_sales_price')
        sales_price.send_keys('10')
        time.sleep(2)
        title.clear()
        title.send_keys('Selenium NEW Product')
        time.sleep(1)
        self.browser.find_element_by_xpath('//input[@type="submit"]').click()
        time.sleep(5)
        self.browser.get('http://localhost:8000/admin/products/product/')
        time.sleep(5)



if __name__ == '__main__':
    unittest.main()
