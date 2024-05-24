import os
import time

from notifypy import Notify
from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import bookwork_logger.constants as c
from utils.path import get_resource_path
from utils.settings import get_setting

def login(driver: webdriver.Chrome) -> None:
    """Logs user in"""
    WebDriverWait(driver, timeout=c.TIMEOUT).until(EC.visibility_of_element_located(c.USERNAME_LOCATOR))

    username = get_setting(*c.USERNAME_SETTING_LOCATOR)
    password = get_setting(*c.PASSWORD_SETTING_LOCATOR)

    uname_entry = driver.find_element(*c.USERNAME_LOCATOR)
    uname_entry.send_keys(username)
    password_entry = driver.find_element(*c.PASSWORD_LOCATOR)
    password_entry.send_keys(password)

    WebDriverWait(driver, timeout=c.TIMEOUT).until(EC.visibility_of_element_located(c.COOKIE_ACCEPT_LOCATOR))

    driver.find_element(*c.COOKIE_ACCEPT_LOCATOR).click()
    driver.find_element(*c.LOGIN_BUTTON_LOCATOR).click()

def question(gui, driver: webdriver.Chrome) -> None:
    """Gets data from question"""
    while "task" not in driver.current_url:
        time.sleep(c.POLLING_FREQUENCY)

    time.sleep(c.POLLING_FREQUENCY)
    if "wac" in driver.current_url:
        try:
            bookwork_check(gui, driver)
        except FileNotFoundError:
            send_notification("Error",
                              "Bookwork code image not found",
                              get_resource_path(c.NOTIFICATION_ICON_PATH),
                              get_resource_path(c.NOTIFICATION_SOUND_PATH))
    else:
        answer_correct = driver.find_element(*c.RESULT_MESSAGE_BANNER_LOCATOR).get_attribute("innerHTML")

        question_info = driver.find_element(*c.BOOKWORK_INFO_LOCATOR).get_attribute("innerHTML")
        bookwork = question_info.split(": ")[1].strip()
        bookwork_path = get_resource_path(os.path.join(c.SCREENSHOTS_FOLDER_PATH, f"{bookwork}.png"))

        if "Correct" in answer_correct and not os.path.exists(bookwork):
            driver.save_screenshot(bookwork_path)
            driver.find_element(*c.CONTINUE_LOCATOR).click()

def bookwork_check(gui, driver: webdriver.Chrome) -> None:
    """Gets data from bookwork check"""
    question_info = driver.find_element(*c.BOOKWORK_INFO_LOCATOR).get_attribute("innerHTML")
    bookwork = question_info.split(" ")[1].strip()

    image = get_bookwork_image(bookwork)

    gui.bookwork_check(image, bookwork)

def get_bookwork_image(bookwork: str) -> ImageTk.PhotoImage:
    image_path = get_resource_path(os.path.join(c.SCREENSHOTS_FOLDER_PATH, f"{bookwork}.png"))
    pillow_image = Image.open(image_path)

    width, height = pillow_image.size
    resized = pillow_image.resize((round(width*0.75), round(height*0.75)))

    return ImageTk.PhotoImage(resized)
   
def end_hw_session() -> None:
    folder_path = get_resource_path(c.SCREENSHOTS_FOLDER_PATH)
    for filename in os.listdir(folder_path): 
        file_path = os.path.join(folder_path, filename)  
        os.remove(file_path)

def create_files() -> None:
    if not os.path.exists(get_resource_path(c.SCREENSHOTS_FOLDER_PATH)):
        os.makedirs(get_resource_path(c.SCREENSHOTS_FOLDER_PATH))

def send_notification(title: str, message: str, icon_path: str, sound_path: str) -> None:
    notification = Notify()
    notification.title = title
    notification.message = message
    notification.icon = icon_path
    notification.audio = sound_path
    notification.send()