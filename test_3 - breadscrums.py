import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_about_breadcrumbs(self):
        driver = self.driver
        driver.get("http://www.python.org")
        elems = driver.find_elements_by_css_selector('#about ul li a')
        href_list = []
        name_list = []
        for e in elems:
            href_list.append(e.get_attribute("href"))
            name_list.append(e.get_attribute('innerHTML'))

        for i in range(len(href_list)):
            driver.get(href_list[i])
            elem = driver.find_element_by_css_selector('.breadcrumbs')
            self.assertIn("About", elem.get_attribute('innerHTML'))
            self.assertIn(
                name_list[i],
                elem.get_attribute('innerHTML')
            )
            time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
