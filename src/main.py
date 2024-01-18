import create_browser
import datetime as dt
import nav_bar_links
import logging

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

MAIL_TEST: bool = True

if __name__ == "__main__":
	logger.info("STARTED WEBSITE TESTING...")
	BROWSER = create_browser.my_selenium_chrome()
	home_page_links = nav_bar_links.browse(BROWSER, MAIL_TEST)
	BROWSER.quit()



