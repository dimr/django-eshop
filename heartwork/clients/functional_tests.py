from selenium import webdriver
import unittest
import time


class NewUser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()

    def test_successful_registration(self):
        self.browser.get('http://localhost:8000/clients/register/')
        name = self.browser.find_element_by_name("email")
        name.send_keys("dxxwq@gmail.com")

        password1 = self.browser.find_element_by_name("password")
        password1.send_keys("1")

        password2 = self.browser.find_element_by_name("password2")
        password2.send_keys("1")
        time.sleep(4)
        # self.browser.find_element_by_xpath('//input[@type="submit"]').click()
        self.browser.find_element_by_xpath('//input[@type="submit"]').click()

        time.sleep(15)



if __name__ == '__main__':
    unittest.main()
