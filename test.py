import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions


class TestUrlShortening(unittest.TestCase):
    def test_ShortenUrl(self):
        # arrange
        self.driver = self.open_browser()
        self.driver.get(' https://bitly.com/')
        # act
        original_url = 'https://docs.python.org/3.6/installing/index.html'
        shorten_url = self.shorten_url(original_url)
        # assert
        self.driver.get(shorten_url)
        self.assertEqual(self.driver.current_url, original_url)
        self.driver.quit()

    def shorten_url(self, url):
        wait = ui.WebDriverWait(self.driver, 10)
        url_field = self.driver.find_element_by_id('shorten_url')
        url_field.send_keys(url)
        self.driver.find_element_by_id('shorten_btn').click()
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "copy_shortlink")))
        return url_field.get_attribute('value')

    @staticmethod
    def open_browser():
        path = 'chromedriver_win32/chromedriver.exe' if os.name == 'nt' else 'chromedriver_linux64/chromedriver'
        return webdriver.Chrome(path)


if __name__ == '__main__':
    unittest.main()
