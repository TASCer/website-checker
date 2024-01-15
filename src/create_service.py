import logging
import my_secrets

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service

logger = logging.getLogger(__name__)


def my_selenium_firefox():
	"""Create and return a selenium Firefox service to be used on pages and forms"""
	try:
		ser = Service(f"{my_secrets.firefox_driver}")
		op = webdriver.FirefoxOptions()

		logger.info(f"selenium FIREFOX service created with options: {op}")

		return webdriver.Chrome(service=ser, options=op)

	except (FileNotFoundError, WebDriverException) as e:
		logger.critical(f"{str(e)}")
		exit()


def my_selenium_chrome():
	"""Create and return a selenium Firefox service to be used on pages and forms"""
	try:
		service = Service(f"{my_secrets.chrome_driver}")
		options = webdriver.ChromeOptions()
		options.add_argument("--remote-allow-origins=*")
		options.add_argument("--disable notifications")

		logger.info(f"selenium CHROME service created with options: {options}")

		return webdriver.Chrome(service=service, options=options)

	except (FileNotFoundError, WebDriverException) as e:
		logger.critical(f"{str(e)}")
		exit()