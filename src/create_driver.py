# TODO TEST NON HEADLESS FF. Chrome WORKS! and FF headless works with managed drivers
# from selenium.webdriver.chrome.webdriver import WebDriver
import logging
import sys
from logging import Logger

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.service import Service as FirefoxService

# from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

logger: Logger = logging.getLogger(__name__)


def firefox() -> webdriver.Firefox:
    """
    Function creates a FIREFOX Selenium webdriver to be used with web pages and forms.

    :return: Firefox driver
    """
    try:
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")

        firefox_browser = webdriver.Firefox(
            options=options, service=FirefoxService(GeckoDriverManager().install())
        )

        logger.info(f"\tFIREFOX browser service created w/options: {options.arguments}")

        return firefox_browser

    except FileNotFoundError:
        logger.exception("file not found")
        sys.exit()

    except WebDriverException as driver_err:
        logger.critical(f"{driver_err!s}")
        sys.exit()


def chrome() -> webdriver.Chrome:
    """
    Function creates a CHROMIUM Selenium webdriver to be used with web pages and forms.

    :return: Chromium driver
    """
    try:
        options = ChromeOptions()
        # working settings
        options.add_argument("--headless=new")
        # options.add_argument("--window-size=480,960")

        # unknown settings affects
        # options.add_argument("--remote-allow-origins=*")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option("useAutomationExtension", False)
        # options.add_argument("--disable notifications")

        chrome_browser = webdriver.Chrome(
            options=options, service=ChromeService(ChromeDriverManager().install())
        )

        logger.info(f"\tCHROME browser service created w/options: {options.arguments}")

        return chrome_browser

    except (FileNotFoundError, WebDriverException) as e:
        logger.critical(f"{e!s}")
        sys.exit()


def create_for(browser) -> webdriver.Firefox | webdriver.Chrome:
    match browser:
        case "firefox":
            BROWSER = firefox()
        case "chrome":
            BROWSER = chrome()

    return BROWSER


if __name__ == "__main__":
    browser = firefox()
    browser.get("https://hoa.tascs.test")
