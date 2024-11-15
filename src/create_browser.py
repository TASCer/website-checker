import logging
import my_secrets

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service

logger = logging.getLogger(__name__)


def firefox() -> webdriver:
    """Create and return a selenium Firefox service to be used on pages and forms"""
    try:
        service = Service(f"{my_secrets.firefox_driver}")
        options = webdriver.FirefoxOptions()
        # options.headless = True
        # options.add_argument("--start-maximized")
        # options.add_argument("-headless")
        options.binary_location = r"P:\Firefox\firefox.exe"

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
    try:
        service = Service(f"{my_secrets.chrome_driver}")
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