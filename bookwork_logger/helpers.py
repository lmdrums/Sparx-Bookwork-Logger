import os, sys
import time
from dotenv import set_key, load_dotenv

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image, ImageTk

import bookwork_logger.constants as c

def get_resource_path(relative_path: str="") -> str:
    """Gets absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def login(driver: webdriver.Chrome) -> None:
    """Logs user in"""
    WebDriverWait(driver, timeout=c.TIMEOUT).until(EC.visibility_of_element_located(c.USERNAME_LOCATOR))

    username = get_username()
    password = get_password()

    uname = driver.find_element(*c.USERNAME_LOCATOR)
    uname.send_keys(username)
    password_entry = driver.find_element(*c.PASSWORD_LOCATOR)
    password_entry.send_keys(password)
    try:
        driver.find_element(*c.COOKIE_ACCEPT_LOCATOR).click()
        driver.find_element(*c.LOGIN_BUTTON_LOCATOR).click()
    except Exception:
        pass

def question(gui, driver: webdriver.Chrome) -> None:
    """Gets data from question"""
    while "task" not in driver.current_url:
        time.sleep(c.POLLING_FREQUENCY)

    time.sleep(c.POLLING_FREQUENCY)
    if "wac" in driver.current_url:
        bookwork_check(gui, driver)

    WebDriverWait(driver, c.TIMEOUT).until(EC.visibility_of_element_located(c.ANSWER_BUTTON_LOCATOR))

    question_info = driver.find_element(*c.BOOKWORK_INFO_LOCATOR).get_attribute("innerHTML")
    bookwork = question_info.split(": ")[1].strip()

    WebDriverWait(driver, c.TIMEOUT).until(EC.visibility_of_element_located(c.RESULT_MESSAGE_BANNER_LOCATOR))

    answer_correct = driver.find_element(*c.RESULT_MESSAGE_BANNER_LOCATOR).get_attribute("innerHTML")
    bookwork_path = get_resource_path(os.path.join(c.SCREENSHOTS_FOLDER_PATH, f"{bookwork}.png"))

    if "Correct" in answer_correct and not os.path.exists(bookwork):
        driver.save_screenshot(bookwork_path)
        try:
            driver.find_element(*c.CONTINUE_LOCATOR).click()
        except Exception:
            pass

def bookwork_check(gui, driver: webdriver.Chrome) -> None:
    """Gets data from bookwork check"""
    WebDriverWait(driver, c.TIMEOUT).until(EC.visibility_of_element_located(c.BOOKWORK_INFO_LOCATOR))

    question_info = driver.find_element(*c.BOOKWORK_INFO_LOCATOR).get_attribute("innerHTML")
    try:
        bookwork = question_info.split(" ")[1].strip()
        time.sleep(c.POLLING_FREQUENCY)
        image = get_bookwork_image(bookwork)
        gui.bookwork_check(image, bookwork)
    except Exception:
        pass

def get_bookwork_image(bookwork: str) -> ImageTk.PhotoImage | None:
    image_path = get_resource_path(os.path.join(c.SCREENSHOTS_FOLDER_PATH, f"{bookwork}.png"))
    if os.path.exists(image_path):
        pillow_image = Image.open(image_path)
        width, height = pillow_image.size
        resized = pillow_image.resize((round(width*0.75), round(height*0.75)))
        return ImageTk.PhotoImage(resized)
   
def end_hw_session() -> None:
    folder_path = c.SCREENSHOTS_FOLDER_PATH
    for filename in os.listdir(folder_path): 
        file_path = os.path.join(folder_path, filename)  
        os.remove(file_path)

def create_files() -> None:
    if not os.path.exists(get_resource_path(c.ENV_PATH)):
        open(get_resource_path(c.ENV_PATH), "w")
        if not os.path.exists(get_resource_path(c.URL_FILE)):
            open(get_resource_path(c.URL_FILE), "w")
        set_key(get_resource_path(c.ENV_PATH), "SPARXUSERNAME", "")
        set_key(get_resource_path(c.ENV_PATH), "PASSWORD", "")

def change_username_password(username: str, password: str) -> None:
    open(get_resource_path(c.ENV_PATH), "w")
    set_key(get_resource_path(c.ENV_PATH), "SPARXUSERNAME", username)
    set_key(get_resource_path(c.ENV_PATH), "PASSWORD", password)

def get_username() -> str:
    load_dotenv(get_resource_path(c.ENV_PATH))
    username = os.getenv("SPARXUSERNAME")
    return username

def get_password() -> str:
    load_dotenv(get_resource_path(c.ENV_PATH))
    password = os.getenv("PASSWORD")
    return password

def get_url() -> str:
    with open(c.URL_FILE, "r") as f:
        return f.read()

def change_url(url: str) -> None:
    with open(c.URL_FILE, "w") as f:
        f.write(url)