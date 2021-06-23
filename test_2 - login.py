import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_logout(self):
        driver = self.driver
        driver.get("https://www.python.org/psf-landing/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Sign In")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("//input[@name='login']")
        elem.send_keys("aliaksandra_savelyeva")
        time.sleep(3)
        elem = driver.find_element_by_xpath("//input[@name='password']")
        elem.send_keys("08011942")
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertIn("Your account", driver.page_source)
        time.sleep(3)
        print(driver.page_source)
        driver.get("https://www.python.org/accounts/logout/")
        time.sleep(3)
        elem = driver.find_element_by_css_selector(
            'div.container section.main-content form button'
        )
        elem.click()
        time.sleep(3)
        self.assertNotIn("Your account", driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()