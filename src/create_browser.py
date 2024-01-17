import logging
import my_secrets

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service

logger = logging.getLogger(__name__)


def selenium_firefox() -> Service:
	"""Create and return a selenium Firefox service to be used on pages and forms"""
	try:
		service = Service(f"{my_secrets.firefox_driver}")
		options = webdriver.FirefoxOptions()

		options.add_argument("--start-maximized")

		logger.info(f"selenium FIREFOX service created with options: {options.arguments}")

		ff_browser = webdriver.Firefox(service=service, options=options)

		return ff_browser

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
		options.add_argument("--start-maximized")

		logger.info(f"selenium CHROME service created with options: {options.arguments}")

		chr_browser = webdriver.Chrome(service=service, options=options)

		return chr_browser

	except (FileNotFoundError, WebDriverException) as e:
		logger.critical(f"{str(e)}")
		exit()