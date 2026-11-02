import logging
import sys
from logging import Logger

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
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

        driver = webdriver.Firefox(
            options=options, service=FirefoxService(GeckoDriverManager().install())
        )

        return driver

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

        driver = webdriver.Chrome(
            options=options, service=ChromeService(ChromeDriverManager().install())
        )

        logger.info(f"\tCHROME browser service created w/options: {options.arguments}")

        return driver

    except (FileNotFoundError, WebDriverException) as e:
        logger.critical(f"{e!s}")
        sys.exit()


def create_for(browser) -> webdriver.Firefox | webdriver.Chrome:
    match browser:
        case "firefox":
            driver = firefox()
        case "chrome":
            driver = chrome()

    return driver


if __name__ == "__main__":
    browser = firefox()
    browser.get("https://hoa.tascs.test")
