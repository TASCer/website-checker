import datetime as dt
import logging
import create_browser

from datetime import datetime
from my_secrets import test_home_url
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select

now: datetime = dt.date.today()
todays_date: str = now.strftime("%D").replace("/", "-")

logger = logging.getLogger(__name__)


def browse(browser, site: str) -> tuple[str, str]:
    """
    Function vistits the HOA community map to get and return
    -Last db data timestamp
    -Area rental percentage
    -LPS rental percentage
    :param browser:
    :param site:
    :return:
    """
    try:
        browser.get(site + "/hoa/areaMap.php")
        WebDriverWait(browser, 1000)
        logger.info(f"\tTesting HOA page for: {site}")

    except Exception as e:
        logger.error(e)

    last_db_update: str = browser.find_element(By.ID, "TS").text
    area_rental_percent: str = browser.find_element(By.ID, "TPCT").text
    # CANNOT GET THIS TO WORK. SEPERATED LPS TO OWN FILE
    # select = Select(browser.find_element(By.ID, "community-names"))
    # print(select)
    # select_lps = select.first_selected_option
    # print(select_lps.text)

    return last_db_update, area_rental_percent


if __name__ == "__main__":
    BROWSER = create_browser.chrome()
    site2test = test_home_url
    print(browse(BROWSER, site2test))
