# TODO Implement Selenium Manager - FF working, need to istall chromium to test
# https://www.browserstack.com/guide/python-selenium-webdriver-
# https://pypi.org/project/webdriver-manager/
import logging
# import my_secrets
# import platform

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from typing import Literal
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

logger = logging.getLogger(__name__)


def firefox() -> webdriver.Firefox:
    """Create and return a selenium Firefox service to be used on pages and forms"""

    try:
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")

        firefox_browser = webdriver.Firefox(
            options=options, service=FirefoxService(GeckoDriverManager().install())
        )

        logger.info(f"\tFIREFOX browser service created w/options: {options.arguments}")

        return firefox_browser

    except FileNotFoundError as file_err:
        logger.exception(file_err)
        exit()

    except WebDriverException as driver_err:
        logger.critical(f"{str(driver_err)}")
        exit()


def chrome() -> webdriver.Chrome:
    """Create and return a selenium Firefox service to be used on pages and forms"""

    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--remote-allow-origins=*")
        options.add_argument("--headless=new")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--disable notifications")
        chrome_browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )

        logger.info(f"\tCHROME browser service created w/options: {options.arguments}")

        return chrome_browser

    except (FileNotFoundError, WebDriverException) as e:
        logger.critical(f"{str(e)}")
        exit()


if __name__ == "__main__":
    browser = firefox()
    browser.get("https://hoa.tascs.test")
