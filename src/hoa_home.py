import datetime as dt
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

now: dt = dt.date.today()
todays_date: str = now.strftime("%D").replace("/", "-")

logger = logging.getLogger(__name__)


def browse(browser, site: str) -> object:
    try:
        browser.get(site + "/hoa/areaMap.php")
        WebDriverWait(browser, 1000)
        logger.info(f"\tTesting HOA page for: {site}")

    except Exception as e:
        logger.error(e)

    # try:
    # 	browser.find_element(By.LINK_TEXT, "Legacy Parc South (LPS)").click()   # "Neighboring Communities"
    # except Exception as e:
    # 		logger.error(e)
    # time.sleep(6)

    last_db_update = browser.find_element(By.ID, "TS")

    return last_db_update.text
