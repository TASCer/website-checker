import datetime as dt
import logging
import my_secrets

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotSelectableException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

now: dt = dt.date.today()
todays_date: str = now.strftime('%D').replace('/', '-')

logger = logging.getLogger(__name__)


def submit_consult(browser, site: str) -> object:
	try:
		browser.get(site)
		WebDriverWait(browser, 1000)

	except TimeoutException as e:
		logger.error(e)

	if site == 'https://tascs.net':
		logger.warning(f"PROD SITE {site} HAS CAPTCHA IN PLAY, SKIPPING")
		return None

	else:
		logger.info("SENDING EMAIL FROM CONSULT FORM")
		logger.info(f"\t\tHARD CODED captcha: {my_secrets.test_home_url}**")

		try:

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
			WebDriverWait(browser, 1000)

			try:
				# browser.find_element(By.ID, 'submit-form').click()
				submit_response = WebDriverWait(browser, 15).until(
					EC.text_to_be_present_in_element((By.ID, 'msg'), text_="Request sent successfully")
				)

				logger.info(f"\t\t CONSULT email sent? {submit_response}")

				return browser

			except Exception as e:
				# submit_response = response = "No message"
				logger.exception(f"CONSULT email not sent: {e}")

		except ElementNotSelectableException as e:
			logger.error(e)

		browser.find_element(By.LINK_TEXT, "CONTACT").click()
		WebDriverWait(browser, 3000)


def submit_contact(browser, site: str) -> object:
	try:
		browser.get(site+'/contact-us')
		WebDriverWait(browser, 1000)
		logger.info("SENDING EMAIL FROM CONTACT FORM")

	except TimeoutException as e:
		logger.error(e)

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

	try:
		browser.find_element(By.ID, 'submit-form').click()
		submit_response = WebDriverWait(browser, 15).until(
			EC.text_to_be_present_in_element((By.ID, 'msg'), text_="Request sent successfully")
		)

		logger.info(f"\t\t CONTACT email sent? {submit_response}")

		return browser

	except Exception as e:
		submit_response = None
		logger.exception(f"Contact not sent: {e}")
