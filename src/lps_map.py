import create_browser
import logging

from my_secrets import test_home_url
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)


def lps_rental_data(browser, site: str) -> str:
    """
    Function gets current rental percent from site

    :param browser:
    :param site: url
    :return: percentage of rentals
    """
    try:
        browser.get(site + "/hoa/lpsMap.php")
        lps_rental_percent = browser.find_element(By.ID, "PCT")
    except Exception as e:
        logger.error(e)

    return lps_rental_percent.text


if __name__ == "__main__":
    BROWSER = create_browser.chrome()
    site2test = test_home_url
    print(lps_rental_data(BROWSER, site2test))
