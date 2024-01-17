import datetime as dt
import logging
import my_secrets

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

now: dt = dt.date.today()
todays_date: str = now.strftime('%D').replace('/', '-')

logger = logging.getLogger(__name__)


def collect(browser, MAIL_TEST):
	logger.info("Testing navigation bar links")
	browser.get(my_secrets.test_home_url)
	WebDriverWait(browser, 1000)
	browser.find_element(By.LINK_TEXT, "WHY TASCS?").click()
	WebDriverWait(browser, 1000)
	browser.find_element(By.LINK_TEXT, "SOLUTIONS").click()
	WebDriverWait(browser, 1000)
	browser.find_element(By.LINK_TEXT, "CONTACT").click()

	if MAIL_TEST:
		# WebDriverWait(browser, 1000)
		logger.info("TESTING SEND MAIL")
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
		WebDriverWait(browser, 1000)

	WebDriverWait(browser, 1000)

	browser.find_element(By.LINK_TEXT, "BLOG").click()
	WebDriverWait(browser, 1000)
	browser.find_element(By.LINK_TEXT, "HOA").click()
	WebDriverWait(browser, 1000)

	logger.info(f"Navigation Bar links tested. Mail test: {MAIL_TEST}")

	return browser



# print(a_refs.)

# for ref in a_refs:
# 	link = ref.get_attribute("href")
#
# 	if link == '' or '#' in link or 'mailto' in link or "vreasolutions" in link:
# 		continue
#
# 	unique_links.add(link)
#
# with open(f"./output/links.txt", "w+") as fh:
# 	for unique_link in unique_links:
# 		fh.write(unique_link + '\n')