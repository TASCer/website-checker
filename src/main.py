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

# LOGGING
root_logger: Logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# NEEDED TO ABSOLUTE FOR SCHEDULED TASKS
fh = logging.FileHandler(f'D:\PycharmProjects\Selenium\{todays_date}.log')
fh.setLevel(logging.DEBUG)
formatter: Formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
root_logger.addHandler(fh)
logger: Logger = logging.getLogger(__name__)

# CHROME = create_browser.my_selenium_chrome()
tascs_site = my_secrets.prod_home_url
test_tascs_site = my_secrets.test_home_url
local_tascs_site = my_secrets.local_home_url

site2test = test_tascs_site

if __name__ == "__main__":
	logger.info(f"STARTED SELENIUM TESTING FOR SITE: {site2test}...")
	BROWSER = create_browser.selenium_firefox()
	home_page_links = nav_bar_links.browse(BROWSER, site= site2test)
	form_submission.submit_consult(browser=BROWSER, site=site2test)
	form_submission.submit_contact(browser=BROWSER, site= site2test)


	last_rentals = hoa_home.browse(BROWSER, site2test)
	last_rentals_update = last_rentals.replace("\n"," " )
	logger.info(f"Last HOA DB Update: {last_rentals_update}")
	blog_titles = blog_home.browse(BROWSER, site2test+'/blog')
	# mailer.send_mail(f"Python web testing complete")


	BROWSER.close()