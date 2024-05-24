from selenium.webdriver.common.by import By
import os

# Locators
COOKIE_ACCEPT_LOCATOR = (By.ID, "cookie-accept-all")
USERNAME_LOCATOR = (By.ID, "username")
PASSWORD_LOCATOR = (By.ID, "password")
LOGIN_BUTTON_LOCATOR = (By.XPATH, "//*[@id='login-form']/div[3]/button")
BOOKWORK_INFO_LOCATOR = (By.CLASS_NAME, "_Chip_bu06u_1")
ANSWER_BUTTON_LOCATOR = (By.XPATH, "//*[@id='BottomBar']/div/button")
RESULT_MESSAGE_BANNER_LOCATOR = (By.ID, "RESULT_POPOVER")
CONTINUE_LOCATOR = (By.XPATH, "//*[@id='RESULT_POPOVER']/div/div[3]")

# Main
FILES_PATH = os.path.join("bookwork_logger", "files")
URL_FILE = os.path.join(FILES_PATH, "url.txt")
POLLING_FREQUENCY = 1
TIMEOUT = 60
SCREENSHOTS_FOLDER_PATH = os.path.join("bookwork_logger", "screenshots")

# App
ASSETS_FOLDER_PATH = os.path.join("bookwork_logger", "assets")
MAIN_TITLE = "Sparx Bookwork Logger"
MAIN_GEOMETRY = "960x540+480+270"
THEME_PATH = os.path.join(ASSETS_FOLDER_PATH, "theme.json")
IMAGES_PATH = os.path.join("bookwork_logger", "images")
WINDOW_ICON_PATH = os.path.join(IMAGES_PATH, "logo.ico")

# Settings
SETTINGS_TITLE = "Settings"
SETTINGS_GEOMETRY = "660x240+580+370"
SETTINGS_INI_PATH = os.path.join(FILES_PATH, "settings.ini")

CREDENTIALS_SETTING_SECTION_NAME = "CREDENTIALS"
USERNAME_SETTING_LOCATOR = (CREDENTIALS_SETTING_SECTION_NAME, "username")
PASSWORD_SETTING_LOCATOR = (CREDENTIALS_SETTING_SECTION_NAME, "password")
URL_SETTING_LOCATOR = (CREDENTIALS_SETTING_SECTION_NAME, "url")

DEFAULT_SETTINGS = {
    CREDENTIALS_SETTING_SECTION_NAME: {
        USERNAME_SETTING_LOCATOR[1]: "",
        PASSWORD_SETTING_LOCATOR[1]: "",
        URL_SETTING_LOCATOR[1]: ""
    }
}

ENV_PATH = os.path.join(FILES_PATH, "credentials.env")

# Images
FIND_IMAGE = {"light": os.path.join(IMAGES_PATH, "find.png"),
                       "dark": os.path.join(IMAGES_PATH, "find.png")}
RUN_IMAGE = {"light": os.path.join(IMAGES_PATH, "run.png"),
                       "dark": os.path.join(IMAGES_PATH, "run.png")}
SAVE_IMAGE = {"light": os.path.join(IMAGES_PATH, "save_file.png"),
                       "dark": os.path.join(IMAGES_PATH, "save_file.png")}
SETTINGS_IMAGE = {"light": os.path.join(IMAGES_PATH, "settings.png"),
                       "dark": os.path.join(IMAGES_PATH, "settings.png")}

# Notifications
NOTIFICATION_ICON_PATH = os.path.join(IMAGES_PATH, "logo.png")
NOTIFICATION_SOUND_PATH = os.path.join(FILES_PATH, "notification.wav")