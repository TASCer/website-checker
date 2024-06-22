import datetime as dt
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

now: dt = dt.date.today()
todays_date: str = now.strftime("%D").replace("/", "-")

logger = logging.getLogger(__name__)


def browse(browser, site: str) -> object:
    try:
        browser.get(site)
        WebDriverWait(browser, 1000)
        logger.info(f"\tBlog posts: {site}")

    except Exception as e:
        logger.error(e)

    blog_entries = browser.find_elements(By.CLASS_NAME, "entry-title")
    blog_titles = [e.text for e in blog_entries]
    logger.info(f"\tFirst Page Blog Count: {len(blog_titles)}")

    return browser
