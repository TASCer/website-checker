import datetime as dt
import logging

from datetime import datetime
from logging import Logger
from my_secrets import test_home_url
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

now: datetime = dt.date.today()
todays_date: str = now.strftime("%D").replace("/", "-")

logger: Logger = logging.getLogger(__name__)


def browse(browser, site: str) -> tuple[str, str]:
    """
    Function browses the HOA site and links to get information.
    :param browser:
    :param site:
    :return: area rental percentage, LPS rental percentage
    """
    try:
        browser.get(site + "/hoa/areaMap.php")
        WebDriverWait(browser, 1000)
        logger.info(f"\tTesting HOA page for: {site}")

    except Exception as e:
        logger.error(e)

    last_db_update: str = browser.find_element(By.ID, "TS").text
    area_rental_percent: str = browser.find_element(By.ID, "TPCT").text

    return last_db_update, area_rental_percent


if __name__ == "__main__":
    import create_browser, create_browser_managed
    BROWSER = create_browser_managed.chrome() #cannot find chrome binary
    site2test = test_home_url
    print(browse(BROWSER, site2test))
