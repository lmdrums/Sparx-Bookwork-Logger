import logging

from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
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
            except NoSuchWindowException as e:
                raise NoSuchWindowException from e
            except Exception as e:
                logging.exception(e)
            else:
                break

        while True:
            try:
                h.question(gui, driver)
            except NoSuchWindowException as e:
                raise NoSuchWindowException from e
            except Exception as e:
                print("""
                      --------------------------------
                      THIS ERROR IS SUPPOSED TO HAPPEN
                      --------------------------------""")
                logging.exception(e)

            time.sleep(c.POLLING_FREQUENCY)
    except NoSuchWindowException:
        print("Browser window closed, quitting driver...")
    finally:
        driver.quit()