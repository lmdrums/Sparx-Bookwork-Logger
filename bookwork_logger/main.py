from selenium import webdriver
from selenium.common.exceptions import TimeoutException

import bookwork_logger.helpers as h
import bookwork_logger.constants as c

def main(gui):
    try:
        driver = webdriver.Chrome()

        url = open(h.get_resource_path(c.URL_FILE), "r").read()
        driver.get(url)

        h.login(driver)

        while True:
            try:
                h.question(gui, driver)
            except TimeoutException:
                pass
    finally:
        driver.quit()