import datetime as dt
import logging
from datetime import date
from logging import Logger

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

now: date = dt.datetime.now().astimezone().date()
todays_date: str = now.strftime("%D").replace("/", "-")

logger: Logger = logging.getLogger(__name__)


def browse(browser, site: str) -> tuple[str, str]:
    """
    Function browses the HOA site and links to get information.
    :param browser:
    :param site: url
    :return: area rental percentage, LPS rental percentage
    """
    # TODO ESTING GETTING TITLE FROM LIMESURVEY PAGE/APP. NEED INSTALLED IN TEST!!!!
    # try:
    #     browser.get(f"{site}/hoa")
    #     survey_link_location = browser.find_element(By.ID, "middlebox")
    #     print(survey_link_location)
    #     survey_link = survey_link_location.find_element(
    #         By.LINK_TEXT, "Community Member Survey"
    #     )
    #     survey_link.click()
    #     survey_active: str = browser.find_element(By.ID, "TPCT").text

    #     logger.info(f"\tTesting HOA page for: {site}")

    # except TimeoutException:
    #     logger.exception("time out")

    try:
        browser.get(site + "/hoa/areaMap.php")
        WebDriverWait(browser, 1000)
        logger.info(f"\tTesting HOA page for: {site}")

    except TimeoutException:
        logger.exception("time out")

    last_db_update: str = browser.find_element(By.ID, "TS").text
    area_rental_percent: str = browser.find_element(By.ID, "TPCT").text

    return last_db_update, area_rental_percent
