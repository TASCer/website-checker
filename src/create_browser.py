# TODO Implement Selenium Manager
# https://www.browserstack.com/guide/python-selenium-webdriver-manager
import logging
import my_secrets
import platform

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.service import Service as FService
from selenium.webdriver.chrome.service import Service as CService

logger = logging.getLogger(__name__)


def firefox() -> webdriver:
    """Create and return a selenium Firefox service to be used on pages and forms"""

    if platform.system() == "Windows":
        FF_DRIVER = my_secrets.firefox_driver_win
        BINARY_LOCATION = r"P:\Firefox\firefox.exe"
    if platform.system() == "Linux":
        FF_DRIVER = my_secrets.firefox_driver_linux
        BINARY_LOCATION = ""
    try:
        service = FService(FF_DRIVER)
        options = webdriver.FirefoxOptions()
        options.headless = True
        options.add_argument("-headless")

        options.binary_location = BINARY_LOCATION

        logger.info(f"\tFIREFOX browser service created w/options: {options.arguments}")

        ff_browser = webdriver.Firefox(service=service, options=options)

        return ff_browser

    except FileNotFoundError as file_err:
        logger.exception(file_err)
        exit()

    except WebDriverException as driver_err:
        logger.critical(f"{str(driver_err)}")
        exit()


def chrome() -> webdriver:
    """Create and return a selenium Firefox service to be used on pages and forms"""
    if platform.system() == "Windows":
        CH_DRIVER = my_secrets.chrome_driver_win

    if platform.system() == "Linux":
        CH_DRIVER = my_secrets.chrome_driver_lin
        print("LIN")

    try:
        service = CService(CH_DRIVER)
        options = webdriver.ChromeOptions()
        options.add_argument("--remote-allow-origins=*")
        # options.add_argument("--start-maximized")
        options.add_argument("--headless=new")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--disable notifications")

        logger.info(f"\tCHROME browser service created w/options: {options.arguments}")

        chr_browser = webdriver.Chrome(service=service, options=options)

        return chr_browser

    except (FileNotFoundError, WebDriverException) as e:
        logger.critical(f"{str(e)}")
        exit()


if __name__ == "__main__":
    pass
