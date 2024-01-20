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
			fname.clear()
			fname.send_keys("SELENIUM CONSULT")
			WebDriverWait(browser, 1000)

			lname = browser.find_element(By.NAME, 'lastname')
			lname.clear()
			lname.send_keys("TESTER")
			WebDriverWait(browser, 1000)

			email = browser.find_element(By.NAME, 'email')
			email.clear()
			email.send_keys("TESTER@CONSULTFORM.COM")
			WebDriverWait(browser, 1000)

			company = browser.find_element(By.NAME, 'company')
			company.clear()
			company.send_keys("SELENIUM CONSULT TESTING INC.")
			WebDriverWait(browser, 1000)

			phone = browser.find_element(By.NAME, 'telephone')
			phone.clear()
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
			#  RESPONSE msg sometime blank?
			response_element = browser.find_element(By.ID, 'msg')
			response_text = response_element.text

			if response_text == 'Request sent successfully':
				logger.info(f"Consult email: {response_text}")
			else:
				logger.error(f"**CONSULT EMAIL NOT SENT** {response_text}")
		except Exception as e:
			logger.error(e)

	time.sleep(10)

	browser.find_element(By.LINK_TEXT, "WHY TASCS?").click()
	WebDriverWait(browser, 1000)
	browser.find_element(By.LINK_TEXT, "SOLUTIONS").click()
	WebDriverWait(browser, 1000)

	browser.find_element(By.LINK_TEXT, "CONTACT").click()
	if MAIL_TEST:
		# WebDriverWait(browser, 1000)
		logger.info("TESTING SEND MAIL FROM CONTACT FORM")
		name = browser.find_element(By.NAME, 'name')
		name.clear()
		name.send_keys("SELENIUM CONTACT TEST")
		WebDriverWait(browser, 1000)

		email = browser.find_element(By.NAME, 'email')
		email.clear()
		email.send_keys("TESTER@CONTACTFORM.COM")
		WebDriverWait(browser, 1000)

		company = browser.find_element(By.NAME, 'company')
		company.clear()
		company.send_keys("SELENIUM CONTACT TESTING INC")
		WebDriverWait(browser, 1000)

		phone = browser.find_element(By.NAME, 'telephone')
		phone.clear()
		phone.send_keys("1234567890")
		WebDriverWait(browser, 1000)

		comments = browser.find_element(By.NAME, 'message')
		comments.clear()
		comments.send_keys("SELENIUM CONTACT TESTING")
		WebDriverWait(browser, 1000)

		browser.find_element(By.ID, 'submit-form').click()
		time.sleep(1)
		response_element = browser.find_element(By.ID, 'msg')
		response = response_element.text

		if response_text == 'Request sent successfully':
			logger.info(f"Contact email: {response_text}")
		else:
			logger.error(f"**CONTACT EMAIL NOT SENT** {response_text}")

	WebDriverWait(browser, 1000)

	browser.find_element(By.LINK_TEXT, "BLOG").click()
	WebDriverWait(browser, 1000)
	browser.find_element(By.LINK_TEXT, "HOA").click()
	WebDriverWait(browser, 1000)

	logger.info(f"Navigation Bar links tested. Mail test: {MAIL_TEST}")

	return browser
