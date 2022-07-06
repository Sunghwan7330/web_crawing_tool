import unittest

import selenium

from webdriver_builder import WebdriverBuilder


class WebdriverTestClass(unittest.TestCase):

    def test_driver_build(self):
        driver_option = {
            "webdriver_type": "chrome",
            "webdriver_path": "../chromedriver.exe"
        }
        driver = WebdriverBuilder().setWebdriverOption(driver_option).build()
        self.assertNotEqual(driver, None)
        self.assertEqual(str(type(driver)), "<class 'selenium.webdriver.chrome.webdriver.WebDriver'>")


if __name__ == "__main__":
    unittest.main()
