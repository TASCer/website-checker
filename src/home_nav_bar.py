import logging
import sys
import time

import selenium.common.exceptions as sel_exc
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)


def check(
    driver,
    nav_menu_links: dict,
    site: str,
) -> object:
    """
    Function browses through the site navigation bar links

    :param driver:
    :param nav_menu_links: html links found in navigation bar
    :param site: url
    :return: driver
    """
    logger.info(f"Browsing menu bar... {', '.join(list(nav_menu_links.values()))}")
    try:
        driver.get(site)
        WebDriverWait(driver, 500)
    except sel_exc.WebDriverException as err:
        if "ERR_CONNECTION_REFUSED" in str(err.msg):  # CHROME
            logger.error(f"{err.msg}")
            driver.close()
            sys.exit()

        if "Reached error page" in str(err.msg):  # Firefox
            logger.error(f"{err.msg}")
            driver.close()
            sys.exit()

    for href in nav_menu_links.values():
        try:
            driver.get(f"{site}/{href}")
            time.sleep(1)

        except sel_exc.WebDriverException:
            logger.exception("driver issue")

    return driver
