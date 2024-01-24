import datetime as dt
import logging
import my_secrets
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotSelectableException


now: dt = dt.date.today()
todays_date: str = now.strftime('%D').replace('/', '-')

logger = logging.getLogger(__name__)


def browse(browser, MAIL_TEST: bool, site: str) -> object:
	try:
		browser.get(site)
		WebDriverWait(browser, 1000)
		logger.info(f"Testing navigation bar links for: {site}. Email test: {MAIL_TEST}")
	except Exception as e:
		logger.error(e)

	if MAIL_TEST and site == 'https://tascs.test':
		logger.info("TESTING SEND MAIL FROM CONSULT FORM")
		logger.info(f"**HARD CODED ANSWER FOR captcha: {my_secrets.test_home_url}**")

		try:

			browser.find_element(By.ID, "refresh-captcha").click()

			fname = browser.find_element(By.NAME, 'firstname')
			fname.send_keys("SELENIUM CONSULT")
			WebDriverWait(browser, 1000)

			lname = browser.find_element(By.NAME, 'lastname')
			lname.send_keys("TESTER")
			WebDriverWait(browser, 1000)

			email = browser.find_element(By.NAME, 'email')
			email.send_keys("TESTER@CONSULTFORM.COM")
			WebDriverWait(browser, 1000)

			company = browser.find_element(By.NAME, 'company')
			company.send_keys("SELENIUM CONSULT TESTING INC.")
			WebDriverWait(browser, 1000)

			phone = browser.find_element(By.NAME, 'telephone')
			phone.send_keys("1234567890")
			WebDriverWait(browser, 1000)

		except ElementNotSelectableException as e:
			logger.error(e)

		try:
			captcha = browser.find_element(By.NAME, 'captcha')
			captcha.send_keys('17')
			WebDriverWait(browser, 1000)

			browser.find_element(By.NAME, 'submit').click()
			time.sleep(1)
			time.sleep(2)
			try:
				response_element = browser.find_element(By.ID, 'msg')
				response = response_element.text
				time.sleep(1)
			except Exception as e:
				response = None
				logger.exception(f"{response}-- {e}")

			if response == 'Request sent successfully':
				logger.info(f"CONSULT email: {response}")

			else:
				logger.error(f"**CONSULT EMAIL NOT SENT** {response}")

		except ElementNotSelectableException as e:
			logger.error(e)

	time.sleep(5)

	# browser.find_element(By.LINK_TEXT, "WHY TASCS?").click()
	# WebDriverWait(browser, 1000)
	# browser.find_element(By.LINK_TEXT, "SOLUTIONS").click()
	# WebDriverWait(browser, 1000)

	browser.find_element(By.LINK_TEXT, "CONTACT").click()
	browser.get(site + '/contact-us')
	WebDriverWait(browser, 1000)

	if MAIL_TEST:
		# WebDriverWait(browser, 1000)
		logger.info("TESTING SEND MAIL FROM CONTACT FORM")
		name = browser.find_element(By.NAME, 'name')
		name.send_keys("SELENIUM CONTACT TEST")
		WebDriverWait(browser, 1000)

		email = browser.find_element(By.NAME, 'email')
		email.send_keys("TESTER@CONTACTFORM.COM")
		WebDriverWait(browser, 1000)

		company = browser.find_element(By.NAME, 'company')
		company.send_keys("SELENIUM CONTACT TESTING INC")
		WebDriverWait(browser, 1000)

		phone = browser.find_element(By.NAME, 'telephone')
		phone.send_keys("1234567890")
		WebDriverWait(browser, 1000)

		comments = browser.find_element(By.NAME, 'message')
		comments.send_keys("SELENIUM CONTACT TESTING")
		WebDriverWait(browser, 1000)

		browser.find_element(By.ID, 'submit-form').click()
		time.sleep(1)
		time.sleep(2)

		try:
			response_element = browser.find_element(By.ID, 'msg')
			response = response_element.text
			time.sleep(1)
		except Exception as e:
			response = None
			logger.exception(f"{response}-- {e}")

		if response == 'Request sent successfully':
			logger.info(f"Contact email: {response}")
		else:
			logger.error(f"**CONTACT EMAIL NOT SENT** {response}")

	WebDriverWait(browser, 1000)

	browser.find_element(By.LINK_TEXT, "BLOG").click()
	WebDriverWait(browser, 1000)
	browser.find_element(By.LINK_TEXT, "HOA").click()
	WebDriverWait(browser, 1000)

	logger.info(f"Navigation Bar links tested. Mail test: {MAIL_TEST}")

	browser.close()
	# return browser
