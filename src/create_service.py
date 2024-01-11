import logging

logger = logging.getLogger(__name__)

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.service import Service

def my_selenium_chrome():
	"""Create and return a selenium Firefox service to be used on pages and forms"""
	try:
		ser = Service("D:\\geckodriver.exe")
		op = webdriver.FirefoxOptions()

		logger.info(f"selenium FF/Gecko service created with options: {op}")

		return webdriver.Chrome(service=ser, options=op)

	except (FileNotFoundError, WebDriverException) as e:
		logger.critical(f"{str(e)}")
		exit()

