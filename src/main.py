import blog_home
import create_browser
import datetime as dt
import form_submission
import hoa_home
import logging
import mailer
import my_secrets
import nav_bar_links
from logging import Logger, Formatter

now: dt = dt.date.today()
todays_date: str = now.strftime('%D').replace('/', '-')

root_logger: Logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# NEEDED ABSOLUTE PATH FOR SCHEDULED TASKS?
fh = logging.FileHandler(rf'D:\PycharmProjects\Selenium\{todays_date}.log')
fh.setLevel(logging.DEBUG)
formatter: Formatter = Formatter('%(asctime)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
root_logger.addHandler(fh)
logger: Logger = logging.getLogger(__name__)

tascs_site = my_secrets.prod_home_url
test_tascs_site = my_secrets.test_home_url
local_tascs_site = my_secrets.local_home_url

MENU = {
		'WHY TASCS?': 'why-tasc',
		'Solutions': 'solutions',
		'Contact': 'contact-us',
		'Blog': 'blog',
		'HOA': 'hoa'
}

site2test = test_tascs_site


def main(site: str):
	BROWSER = create_browser.selenium_firefox()
	nav_bar_links.browse(BROWSER, MENU, site=site2test)
	contact_response = form_submission.submit_contact(browser=BROWSER, site=site+'/contact-us')
	consult_response = form_submission.submit_consult(browser=BROWSER, site=site)

	last_rentals = hoa_home.browse(BROWSER, site)
	last_rentals_update = last_rentals.replace("\n", " ")
	logger.info(f"\tLast HOA DB Update: {last_rentals_update}")
	blog_home.browse(BROWSER, site + '/blog')

	if not contact_response or not consult_response:
		mailer.send_mail(f"FORM EMAIL ERROR IN WEB TESTING: {contact_response=} {consult_response=}")
		logger.warning(f"----- FORM EMAIL ERROR IN COMPLETING WEB TESTING FOR SITE: {site2test.upper()} -----")

	if contact_response and consult_response:
		mailer.send_mail(f"COMPLETED SELENIUM WEB TESTING WITHOUT FORM ERRORS")
		logger.info(f"***** COMPLETED WEB TESTING FOR SITE: {site2test.upper()} WITHOUT FORM ERRORS *****")

	BROWSER.close()


if __name__ == "__main__":
	logger.info(f"***** STARTED WEB TESTING FOR SITE: {site2test.upper()} *****")
	main(site2test)
