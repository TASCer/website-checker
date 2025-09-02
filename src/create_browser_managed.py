# TODO Implement Selenium Manager - FF working, need to istall chromium to test if needed
# https://www.browserstack.com/guide/python-selenium-webdriver-
# https://pypi.org/project/webdriver-manager/
import logging

from logging import Logger
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

logger: Logger = logging.getLogger(__name__)


def firefox() -> webdriver.Firefox:
    """
    Function creates a FIREFOX Selenium webdriver to be used with web pages and forms.
    Returns created FIREFOX Selenium webdriver.
    """
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
    """
    Function creates a CHROMIUM Selenium webdriver to be used with web pages and forms.
    Returns created CHROMIUM Selenium webdriver.
    """
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
