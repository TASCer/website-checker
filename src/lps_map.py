import logging

from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)


def check_lps_rental(browser, site: str) -> str:
    """
    Function gets current rental percent from site

    :param browser:
    :param site: url
    :return: percentage of rentals
    """
    try:
        browser.get(site + "/hoa/lpsMap.php")
        lps_rental_percent = browser.find_element(By.ID, "PCT")
    except ElementNotVisibleException as e:
        logger.error(e)

    return lps_rental_percent.text
