import unittest
from selenium import webdriver

from helpers import helper
from constants.helper_constants import SOME_TEXT


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('lib\chromedriver.exe')
        self.driver.get(
            "http://way2automation.com/way2auto_jquery/index.php")
        self.driver.maximize_window()
        helper.login(self.driver)

    def test_alert(self):
        self.driver.get(
            "http://way2automation.com/way2auto_jquery/alert.php")
        helper.select_input_alert_menu_and_go_to_its_frame(self.driver)
        helper.click_the_button(self.driver)
        helper.send_text_to_alert_and_accept_it(self.driver)
        self.assertRegex(helper.get_text_under_button(self.driver), SOME_TEXT)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
