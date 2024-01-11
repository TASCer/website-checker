import create_service
import datetime as dt
import logging
import my_secrets

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementNotSelectableException
# from selenium.webdriver.support.expected_conditions import presence_of_element_located

now: dt = dt.date.today()
todays_date: str = now.strftime('%D').replace('/', '-')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


fh = logging.FileHandler(f'../{todays_date}.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)




def contact_form(s: Service):
	"""Takes in a Selenium service s and populates the CONTACT REQUEST FORM on Contact-Us web page"""
	try:
		s.get(my_secrets.local_contact_url)
		s.find_element(By.ID, "captcha-form")


	except ElementNotSelectableException as e:
		logger.critical(f'{str(e)} website must be down')

	name = s.find_element(By.NAME, 'name')
	name.send_keys("TEST")
	WebDriverWait(s, 1000)

	email = s.find_element(By.NAME, 'email')
	email.send_keys("TESTER@TESTER.COM")
	WebDriverWait(s, 1000)

	company = s.find_element(By.NAME, 'company')
	company.send_keys("TESTER INC")
	WebDriverWait(s, 1000)

	phone = s.find_element(By.NAME, 'telephone')
	phone.send_keys("1234567890")
	WebDriverWait(s, 1000)

	comments = s.find_element(By.NAME, 'message')
	comments.send_keys("SELENIUM TESTING")
	WebDriverWait(s, 1000)

	s.find_element(By.ID, 'submit-form').click()
	WebDriverWait(s, 1000)

	logger.info("CONTACT FORM SUBMITTED")

	s.quit()

def consult_form(s: Service):
	"""Takes in a Selenium Service s and populates the CONSULTATION REQUEST FORM on home web page"""
	# TODO captcha issues - disable or hard code answer for testing
	try:
		s.get(my_secrets.contact_url)
		s.find_element(By.XPATH, '//*[@id="captcha-form"]/div')
	except ElementNotSelectableException as e:
		print(f'{str(e)} website must be down')

	fname = s.find_element(By.NAME, 'firstname')
	fname.send_keys("TEST")
	WebDriverWait(s, 1000)

	lname = s.find_element(By.NAME, 'lastname')
	lname.send_keys("TESTer")
	WebDriverWait(s, 1000)

	email = s.find_element(By.NAME, 'email')
	email.send_keys("TESTER@TESTER.COM")
	WebDriverWait(s, 1000)

	company = s.find_element(By.NAME, 'company')
	company.send_keys("TESTER INC.")
	WebDriverWait(s, 1000)

	phone = s.find_element(By.NAME, 'telephone')
	phone.send_keys("1234567890")
	WebDriverWait(s, 1000)

	captcha = s.find_element(By.NAME, 'captcha')
	captcha.send_keys('13')
	WebDriverWait(s, 1000)

	s.find_element(By.NAME, 'submit').click()

	logger.info("CONSULT FORM SUBMITTED")


if __name__ == "__main__":
	s = create_service.my_selenium_chrome()
	contact_form(s)
	# webdriver.Quit()  # try to close ff windoe
	# consult_form(selenium_service())
