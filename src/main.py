# TODO Make into a pytest - https://medium.com/@sayalidhoot07/creating-a-selenium-pytest-framework-from-scratch-6fadd32f9574
# TODO "test different screen sizes selenium python"
import argparse
import datetime as dt
import logging
import os
from enum import Enum
from logging import Formatter, Logger
from pathlib import Path

from dotenv import load_dotenv

import blog_home
import create_driver
import form_submission
import hoa_home
import home_nav_bar
import mailer
from lps_map import check_lps_rental

now = dt.datetime.now().astimezone().date()

todays_date: str = now.strftime("%D").replace("/", "-")

root_logger: Logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

fh = logging.FileHandler(rf"../{todays_date}.log")
fh.setLevel(logging.DEBUG)
formatter: Formatter = Formatter(
    "%(asctime)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s"
)
fh.setFormatter(formatter)
root_logger.addHandler(fh)
logger: Logger = logging.getLogger(__name__)

load_dotenv()


class Sites(str, Enum):
    """
     Class specifies the base HTML URL for website domains to be tested

    EXAMPLE: https://site.tested.com

    """

    prod = os.environ["PROD_HOME_URL"]
    test = os.environ["TEST_HOME_URL"]
    intra = os.environ["INTRANET_HOME_URL"]


class Browsers(str, Enum):
    firefox = "firefox"
    chrome = "chrome"
    chromium = "chromium"
    edge = "edge"


SCREEN_SIZES = [
    (1920, 671),  # MyDesktop - MAIN
    (1600, 491),  # MyLaptop
    (479, 960),  # MyMobile (Alcatel 5059R)
    # (1920, 1080), # MyDesktop - MAIN
]


SITE_MENU: dict[str, str] = {
    "WHY TASCS?": "why-tasc",
    "Solutions": "solutions",
    "Contact": "contact-us",
    "Blog": "blog",
    "HOA": "hoa",
}


def main(site: str, driver) -> None:
    """
    Function controls the application

    :param site: website url to check
    :param driver: driver to check with
    """
    home_nav_bar.check(driver, nav_menu_links=SITE_MENU, site=site)
    # contact_response: bool = form_submission.submit_contact(
    #     driver=driver, site=site + "/contact-us"
    # )
    # consult_response: bool = form_submission.submit_consult(driver, site)

    timestamp, area_percent_rentals = hoa_home.check(driver, site)
    last_timestamp: str = timestamp.replace("\n", " ")
    logger.info(f"\t\tHOA DB {last_timestamp=}")

    area_percent_rentals: float = float(area_percent_rentals)
    logger.info(f"\t\tAREA RENTAL %: {area_percent_rentals}")

    lps_percent_rentals = float(check_lps_rental(driver, site))
    lps_rental_delta = float(f"{lps_percent_rentals - area_percent_rentals}")
    logger.info(f"\t\tLPS RENTAL %: {lps_percent_rentals}")

    if lps_rental_delta > 0.0:
        logger.info(
            f"LPS RENTAL % is {lps_rental_delta:.2f} HIGHER than community average"
        )

    else:
        logger.info(
            f"LPS RENTAL % is {lps_rental_delta:.2f} LOWER than community average"
        )

    blog_home.check(driver, site + "/blog")

    # if not contact_response:
    #     mailer.send_mail(
    #         f"FAIL SENDING CONTACT FORM: {site}",
    #         attachment_path=Path(f"../{todays_date}.log"),
    #     )
    #     logger.error(
    #         f"FAIL SENDING CONTACT FORM: {contact_response=} {site}: {site.upper()} -----"
    #     )

    # if contact_response and consult_response and site == Sites.test:
    #     mailer.send_mail(f"SUCCESS: {site}", None)
    #     logger.info(f"***** SUCCESS: {site.upper()} *****")

    # if contact_response and not consult_response and site == Sites.prod:
    #     mailer.send_mail(f"SUCCESS: {site}", None)
    #     logger.info(f"***** SUCCESS: {site.upper()} *****")

    # if not consult_response and site == Sites.test:
    #     mailer.send_mail(
    #         f"FAIL SENDING CONSULT FORM: {site}", Path(f"../{todays_date}.log")
    #     )
    #     logger.error(
    #         f"FAIL SENDING CONSULT FORM: {consult_response=} {site}: {site.upper()} -----"
    #     )

    driver.close()
    driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="website-checker",
        description="Select website URL and browser to test",
        epilog="i.e 'uv run main,py prod chrome')",
    )
    parser.add_argument(
        "--site",
        choices=[site.name for site in Sites],
        help="please enter the URL of the website to test",
        default="test",
    )
    parser.add_argument(
        "--browser",
        choices=[browser.name for browser in Browsers],
        help="please enter the browser you want to use for the web driver",
        default="firefox",
    )

    args = parser.parse_args()
    site2test_url: str = Sites[args.site].value
    site2test_browser = Browsers[args.browser].value
    logger.info("\t\t\t\t***STARTING WEBSITE TESTING***")
    logger.info(f"{site2test_url=} with {site2test_browser=}")
    browser_driver = create_driver.create_for(site2test_browser)
    logger.info(f"{site2test_browser} options {browser_driver.options.arguments}")  #

    main(site=site2test_url, driver=browser_driver)
