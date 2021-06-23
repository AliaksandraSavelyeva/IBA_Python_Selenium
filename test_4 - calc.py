import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Kalkpro(unittest.TestCase):
    # https://kalk.pro/finish/wallpaper/
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://kalk.pro/finish/wallpaper/')

    def tearDown(self):
        self.driver.close()

    def input_walls_data(self, hei, wid, len):
        driver = self.driver
        elem = driver.find_element_by_id("js--roomСeiling_height")
        elem.clear()
        elem.send_keys(hei)
        elem = driver.find_element_by_id("js--roomSizes_width")
        elem.clear()
        elem.send_keys(wid)
        elem = driver.find_element_by_id("js--roomSizes_length")
        elem.clear()
        elem.send_keys(len)

    def test_walls(self):
        driver = self.driver
        self.input_walls_data(1, 1, 1)
        elem = driver.find_element_by_class_name(
            "js--calcModelFormSubmit"
        )
        elem.click()
        self.assertIn('Результаты расчета', driver.page_source)
        elem = driver.find_element_by_css_selector(
            "ul.data-list li:nth-child(4) strong"
        )
        self.assertEqual('4 м²', elem.text)

        self.input_walls_data(0, 1, 1)
        elem = driver.find_element_by_class_name(
            "js--calcModelFormSubmit"
        )
        elem.click()
        self.assertIn('Ошибки', driver.page_source)
        elems = driver.find_elements_by_css_selector(
            "a.js--onclick-goToField"
        )
        self.assertEqual(len(elems), 1)

        self.input_walls_data('a', 'b', 'c')
        elem = driver.find_element_by_class_name(
            "js--calcModelFormSubmit"
        )
        elem.click()
        self.assertIn('Ошибки', driver.page_source)
        elems = driver.find_elements_by_css_selector(
            "a.js--onclick-goToField"
        )
        self.assertEqual(len(elems), 3)

    def test_windows(self):
        driver = self.driver
        self.input_walls_data(1, 1, 1)
        elem = driver.find_element_by_css_selector(
            "fieldset[name=windows] button"
        )
        elem.click()
        elem = driver.find_element_by_id("js--windows_height_0")
        elem.clear()
        elem.send_keys(1)
        elem = driver.find_element_by_id("js--windows_width_0")
        elem.clear()
        elem.send_keys(1)
        elem = driver.find_element_by_id("js--windows_count_0")
        elem.clear()
        elem.send_keys(1)
        elem = driver.find_element_by_class_name(
            "js--calcModelFormSubmit"
        )
        elem.click()
        self.assertIn('Результаты расчета', driver.page_source)
        elem = driver.find_element_by_css_selector(
            "ul.data-list li:nth-child(4) strong"
        )
        self.assertEqual('3 м²', elem.text)

        elem = driver.find_element_by_css_selector(
            "fieldset[name=doors] button"
        )
        elem.click()
        elem = driver.find_element_by_id("js--doors_height_0")
        elem.clear()
        elem.send_keys(1)
        elem = driver.find_element_by_id("js--doors_width_0")
        elem.clear()
        elem.send_keys(1)
        elem = driver.find_element_by_id("js--doors_count_0")
        elem.clear()
        elem.send_keys(1)
        elem = driver.find_element_by_class_name(
            "js--calcModelFormSubmit"
        )
        elem.click()
        self.assertIn('Результаты расчета', driver.page_source)
        elem = driver.find_element_by_css_selector(
            "ul.data-list li:nth-child(4) strong"
        )
        self.assertEqual('2 м²', elem.text)


if __name__ == '__main__':
    unittest.main()
