import logging
import selenium.common.exceptions as sel_exc
import time

from selenium.webdriver.support.ui import WebDriverWait

from typing import Dict

logger = logging.getLogger(__name__)


def browse(
    browser,
    nav_menu_links: Dict,
    site: str,
) -> object:
    logger.info(f"\tNavigating menu bar: {', '.join(list(nav_menu_links.values()))}")
    try:
        browser.get(site)
        WebDriverWait(browser, 500)
    except sel_exc.WebDriverException as err:
        if "ERR_CONNECTION_REFUSED" in str(err.msg):  # CHROME
            logger.error(f"{err.msg}")
            browser.close()
            exit()

        if "Reached error page" in str(err.msg):  # Firefox
            logger.error(f"{err.msg}")
            browser.close()
            exit()

    for title, href in nav_menu_links.items():
        try:
            browser.get(f"{site}/{href}")
            time.sleep(1)

        except sel_exc.WebDriverException as e:
            logger.exception(e)

    return browser
