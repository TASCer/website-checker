import datetime as dt
import logging
import create_browser

from my_secrets import test_home_url
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

    last_db_update = browser.find_element(By.ID, "TS")
    area_rental_percent = browser.find_element(By.ID, "TPCT")

    return last_db_update.text, float(area_rental_percent.text)

    # TODO TESTING CLICKING LPS FROM DROPDPWN
    # drop = browser.find_element(By.ID, "community-names").click()
    # print(drop)

# GET LPS RENTAL AVG - WORKS. Add to above? NO browser/url issue
#     try:
#         browser.get(site + "/hoa/lpsMap.php")
#         lps_rental_percent = browser.find_element(By.ID, "PCT")   # "Neighboring Communities"
#     except Exception as e:
#         logger.error(e)
#
#     print(float(lps_rental_percent.text))
#
#     return last_db_update.text, float(area_rental_percent.text), float(lps_rental_percent)


if __name__ == "__main__":
    BROWSER = create_browser.chrome()
    site2test = test_home_url
    print(browse(BROWSER, site2test))
