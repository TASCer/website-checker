import argparse
import blog_home
import create_browser
import datetime as dt
from enum import Enum
import form_submission
import hoa_home
import logging
import mailer
import my_secrets
import nav_bar_links
from logging import Logger, Formatter

now: dt = dt.date.today()
todays_date: str = now.strftime("%D").replace("/", "-")

root_logger: Logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# NEEDED ABSOLUTE PATH FOR SCHEDULED TASKS?
fh = logging.FileHandler(rf"D:\PycharmProjects\Selenium\{todays_date}.log")
fh.setLevel(logging.DEBUG)
formatter: Formatter = Formatter("%(asctime)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
root_logger.addHandler(fh)
logger: Logger = logging.getLogger(__name__)


class Sites(str, Enum):
    prod = my_secrets.prod_home_url
    test = my_secrets.test_home_url
    local = my_secrets.local_home_url


MENU = {
    "WHY TASCS?": "why-tasc",
    "Solutions": "solutions",
    "Contact": "contact-us",
    "Blog": "blog",
    "HOA": "hoa",
}


# TODO issue with ff headless?
def main(site: Sites | None) -> None:
    logger.info(f"***** STARTED WEB TESTING FOR SITE: {site.upper()} *****")
    BROWSER = create_browser.chrome()
    nav_bar_links.browse(BROWSER, MENU, site=site)
    contact_response = form_submission.submit_contact(browser=BROWSER, site=site + "/contact-us")
    consult_response = form_submission.submit_consult(browser=BROWSER, site=site)

    timestamp, area_percent_rentals = hoa_home.browse(BROWSER, site)
    last_timestamp: str = timestamp.replace("\n", " ")
    logger.info(f"\t\tHOA DB TIMESTAMP: {last_timestamp}")

    logger.info(f"\t\tAREA RENTAL %: {area_percent_rentals}")
    # logger.info(f"\t\tLPS RENTAL %: {lps_rentals}")
    blog_home.browse(BROWSER, site + "/blog")

    if not contact_response:
        mailer.send_mail(f"FAIL SENDING CONTACT FORM: {site}", f"../{todays_date}.log")
        logger.error(f"FAIL SENDING CONTACT FORM: {contact_response=} {site}: {site.upper()} -----")

    if contact_response and consult_response and site == Sites.test:
        mailer.send_mail(f"SUCCESS TESTING SITE: {site}", f"../{todays_date}.log")
        logger.info(f"***** SUCCESS TESTING SITE: {site.upper()} *****")

    if not consult_response and site == Sites.test:
        mailer.send_mail(f"FAIL SENDING CONSULT FORM: {site}", f"../{todays_date}.log")
        logger.error(f"FAIL SENDING CONSULT FORM: {contact_response=} {site}: {site.upper()} -----")

    BROWSER.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Select which website for Selenium to test")
    parser.add_argument("site", choices=[site.name for site in Sites])

    args = parser.parse_args()
    site2test = Sites[args.site].value

    main(site=site2test)
