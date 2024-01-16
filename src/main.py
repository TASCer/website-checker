import complete_forms
import create_service
import datetime as dt
import get_page_links
import logging
import my_secrets

now: dt = dt.date.today()
todays_date: str = now.strftime('%D').replace('/', '-')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(f'./{todays_date}.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# CHROME = create_service.my_selenium_chrome()
TEST_FORMS: bool = False

if __name__ == "__main__":
	logger.info("STARTED WEBSITE TESTING...")
	FIREFOX = create_service.my_selenium_firefox()
	logger.info(f"SELENIUM SERVICE CREATED FOR: FIREFOX {type(FIREFOX)}")
	if TEST_FORMS:
		contact = complete_forms.contact_form(FIREFOX)
		logger.info(f"{contact}")
		# complete_forms.consult_forms(browser) # CAPTCHA
		# logger.info(f"{consult}")
	# browser.get(my_secrets.test_consult_url)
	# site = browser.current_url
	else:
		home_page_links = get_page_links.collect(FIREFOX)
		FIREFOX.quit()


