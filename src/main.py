import create_browser
import datetime as dt
import logging
import my_secrets
import nav_bar_links
import hoa_home
from logging import Logger, Formatter

now: dt = dt.date.today()
todays_date: str = now.strftime('%D').replace('/', '-')

# LOGGING
root_logger: Logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
fh = logging.FileHandler(f'./{todays_date}.log')
fh.setLevel(logging.DEBUG)
formatter: Formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
root_logger.addHandler(fh)
logger: Logger = logging.getLogger(__name__)

# CHROME = create_browser.my_selenium_chrome()
tascs_site = my_secrets.prod_home_url
test_tascs_site = my_secrets.test_home_url
local_tascs_site = my_secrets.local_home_url
test_hoa_site = my_secrets.test_hoa_url

MAIL_TEST: bool = True

if __name__ == "__main__":
	logger.info("STARTED SELENIUM WEBSITE TESTING...")
	BROWSER = create_browser.my_selenium_chrome()
	home_page_links = nav_bar_links.browse(BROWSER, MAIL_TEST, test_tascs_site)
	# hoa_community = hoa_home.browse(BROWSER, test_hoa_site)
	# BROWSER.quit()



