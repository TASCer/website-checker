import datetime as dt
import logging
import selenium.common.exceptions as sel_exc
import time

# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import ElementNotSelectableException
# from selenium.webdriver.support import expected_conditions as EC
from typing import Dict

now: dt = dt.date.today()
todays_date: str = now.strftime('%D').replace('/', '-')

logger = logging.getLogger(__name__)


def browse(browser,  nav_menu_links: Dict, site: str,) -> object:
	try:
		browser.get(site)
		WebDriverWait(browser, 1000)
		logger.info(f"\tNavigating menu bar links {nav_menu_links}")
	except sel_exc.WebDriverException as e:
		logger.error(e)

	for title, href in nav_menu_links.items():
		try:
			browser.get(f"{site}/{href}")
			time.sleep(5)

		except sel_exc.WebDriverException as e:
			logger.exception(e)

	return browser


	# navbar_items = browser.find_elements(By.TAG_NAME, 'a')
	# print(navbar_items)
	# for item in navbar_items:
	# 	print(item)
	# 	print(item.title)
	# WebDriverWait(browser, 1000)

	# browser.find_element(By.LINK_TEXT, "BLOG").click()
	# WebDriverWait(browser, 1000)
	# browser.find_element(By.LINK_TEXT, "HOA").click()
	# WebDriverWait(browser, 1000)
	#
	# logger.info("FINISHED SELENIUM WEBSITE NAVBAR TESTING")
	#
	# browser.find_element(By.LINK_TEXT, "WHY TASCS?").click()
	# WebDriverWait(browser, 1000)
	#
	# browser.find_element(By.LINK_TEXT, "SOLUTIONS").click()
	# WebDriverWait(browser, 1000)

	# browser.close()
