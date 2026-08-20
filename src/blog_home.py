import datetime as dt
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

now = dt.datetime.now().astimezone().date()
todays_date: str = now.strftime("%D").replace("/", "-")

logger = logging.getLogger(__name__)


def browse(browser, site: str) -> object:
    """
    Function browses the blog site and determines count of entries and latest title.

    :param browser:
    :param site: url
    :return: browser
    """
    try:
        browser.get(site)
        WebDriverWait(browser, 1000)
        logger.info(f"\tTesting Blog page for: {site}")

    except TimeoutException:
        logger.error("timed out")

    blog_entries = browser.find_elements(By.CLASS_NAME, "entry-title")

    if blog_entries:
        blog_titles = [e.text for e in blog_entries]
        logger.info(f"\t\tFirst Page Blog Count: {len(blog_titles)}")
        logger.info(f"\t\tLatest Blog Title: {blog_titles[0]}")

    return browser
