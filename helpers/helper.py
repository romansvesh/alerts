import pickle
import os
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pathlib import Path
from constants import helper_constants, tech_constants
from page import sign_in_form, registration_form, menu_page

'''common support defs'''


def wait_for_element(element, driver, time=tech_constants.TIMEOUT):
    wait = WebDriverWait(driver, time)
    wait.until(expected_conditions.visibility_of(element))


'''the authentication logic'''


def save_cookie(driver):
    os.makedirs(tech_constants.COOKIES_FOLDER, exist_ok=True)
    with open(tech_constants.COOKIES_FILE_NAME, 'wb') as f:
        pickle.dump(driver.get_cookies(), f)


def login_with_cookie(driver):
    with open(tech_constants.COOKIES_FILE_NAME, 'rb') as f:
        cookies = pickle.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()


def is_cookie_file_exist():
    return Path(tech_constants.COOKIES_FILE_NAME).exists()


def sign_in_click(driver):
    wait_for_element(registration_form.get_sign_in_button(driver), driver)
    registration_form.get_sign_in_button(driver).click()


def enter_username(driver):
    wait_for_element(sign_in_form.get_username_input(driver), driver)
    sign_in_form.get_username_input(driver).send_keys(helper_constants.LOGIN)


def enter_password(driver):
    sign_in_form.get_password_input(driver).send_keys(helper_constants.PASSWORD)


def press_submit(driver):
    sign_in_form.get_submit_button(driver).click()


'''the logic of tests'''


def login(driver):
    if is_cookie_file_exist():
        login_with_cookie(driver)
    else:
        sign_in_click(driver)
        enter_username(driver)
        enter_password(driver)
        press_submit(driver)
        save_cookie(driver)


def select_input_alert_menu_and_go_to_its_frame(driver):
    wait_for_element(menu_page.get_input_alert_menu(driver), driver)
    menu_page.get_input_alert_menu(driver).click()
    driver.switch_to.frame(
        menu_page.get_input_alert_frame(driver))


def click_the_button(driver):
    menu_page.get_button(driver).click()


def send_text_to_alert_and_accept_it(driver):
    Alert(driver).send_keys(helper_constants.SOME_TEXT)
    Alert(driver).accept()


def get_text_under_button(driver):
    return menu_page.get_text_under_button(driver).text
