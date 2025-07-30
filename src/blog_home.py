import datetime as dt
import logging

from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

now: datetime = dt.date.today()
todays_date: str = now.strftime("%D").replace("/", "-")

logger = logging.getLogger(__name__)


def browse(browser, site: str) -> object:
    try:
        browser.get(site)
        WebDriverWait(browser, 1000)
        logger.info(f"\tTesting Blog page for: {site}")

    except Exception as e:
        logger.error(e)

    blog_entries = browser.find_elements(By.CLASS_NAME, "entry-title")
    blog_titles = [e.text for e in blog_entries]
    logger.info(f"\t\tFirst Page Blog Count: {len(blog_titles)}")
    logger.info(f"\t\tLatest Blog Title: {blog_titles[0]}")

    return browser
