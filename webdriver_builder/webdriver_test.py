import unittest

from webdriver_builder import WebdriverBuilder


class WebdriverTestClass(unittest.TestCase):

    def test_driver_build_option(self):
        driver_option = {
            "webdriver_type": "chrome",
            "webdriver_path": "../chromedriver.exe"
        }
        driver = WebdriverBuilder().setWebdriverOption(driver_option).build()
        self.assertNotEqual(driver, None)
        self.assertEqual(str(type(driver)), "<class 'selenium.webdriver.chrome.webdriver.WebDriver'>")

    def test_driver_build_non_type(self):
        driver = WebdriverBuilder().build()
        self.assertEqual(driver, None)

    def test_set_driver_non_option(self):
        driver_option = {
            "aaa": "aaa",
            "bbb": "bbb"
        }
        builder = WebdriverBuilder().setWebdriverOption(driver_option)
        self.assertEqual(builder.webdriver_type, None)
        self.assertEqual(builder.webdriver_path, None)

if __name__ == "__main__":
    unittest.main()
