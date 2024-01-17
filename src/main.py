import complete_forms
import create_service
import datetime as dt
import test_nav_bar
import logging
import my_secrets

from logging import Logger, Formatter

now: dt = dt.date.today()
todays_date: str = now.strftime('%D').replace('/', '-')

# LOGGING
root_logger: Logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
fh = logging.FileHandler(f'./{todays_date}.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
root_logger.addHandler(fh)
logger: Logger = logging.getLogger(__name__)

MAIL_TEST: bool = True

if __name__ == "__main__":
	logger.info("STARTED WEBSITE TESTING...")
	FIREFOX = create_service.my_selenium_firefox()
	logger.info(f"SELENIUM SERVICE CREATED FOR: {type(FIREFOX)}")
	# if TEST_FORMS:
	# 	contact = complete_forms.contact_form(FIREFOX)
	# 	logger.info(f"{contact}")
		# complete_forms.consult_forms(browser) # CAPTCHA
		# logger.info(f"{consult}")
	# browser.get(my_secrets.test_consult_url)
	# site = browser.current_url
	# else:
	home_page_links = test_nav_bar.collect(FIREFOX, MAIL_TEST)
	# logger.info(f"Navigation Bar links tested. Mail test: {MAIL_TEST}")
	FIREFOX.quit()
		# test_home_links.complete(FIREFOX)
		# print(home_page_links)



