from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

import bookwork_logger.helpers as h
import bookwork_logger.constants as c
from utils.settings import get_setting

def main(gui):
    try:
        driver = webdriver.Chrome()

        url = get_setting(*c.URL_SETTING_LOCATOR)
        driver.get(url)

        while True:
            try:
                h.login(driver)
            except (NoSuchElementException, TimeoutException):
                pass
            else:
                break

        while True:
            try:
                h.question(gui, driver)
            except NoSuchElementException:
                pass

            time.sleep(c.POLLING_FREQUENCY)
    finally:
        driver.quit()