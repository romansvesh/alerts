from selenium.webdriver.common.by import By

__INPUT_ALERT_MENU = (By.XPATH, '//a[@href="#example-1-tab-2"]')
__BUTTON = (By.TAG_NAME, 'BUTTON')
__TEXT_UNDER_BUTTON_ = (By.ID, 'demo')
__MENU_INPUT_ALERT_FRAME = (By.XPATH, '//div[@id = "example-1-tab-2"]//iframe')


def get_input_alert_menu(driver):
    return driver.find_element(*__INPUT_ALERT_MENU)


def get_button(driver):
    return driver.find_element(*__BUTTON)


def get_text_under_button(driver):
    return driver.find_element(*__TEXT_UNDER_BUTTON_)


def get_input_alert_frame(driver):
    return driver.find_element(*__MENU_INPUT_ALERT_FRAME)