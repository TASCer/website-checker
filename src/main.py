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
formatter: Formatter = Formatter(
    "%(asctime)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s"
)
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


def main(site: Sites | None) -> None:
    logger.info(f"***** STARTED WEB TESTING FOR SITE: {site.upper()} *****")
    BROWSER = create_browser.selenium_chrome()
    nav_bar_links.browse(BROWSER, MENU, site=site)
    contact_response = form_submission.submit_contact(browser=BROWSER, site=site + "/contact-us")
    consult_response = form_submission.submit_consult(browser=BROWSER, site=site)

    last_rentals = hoa_home.browse(BROWSER, site)
    last_rentals_update = last_rentals.replace("\n", " ")
    logger.info(f"\t\tLast HOA DB Update: {last_rentals_update}")
    blog_home.browse(BROWSER, site + "/blog")

    if not contact_response:
        mailer.send_mail(
            f"ERROR - CONTACT FORM EMAIL SENDING: {contact_response=} {site}"
        )
        logger.error(
            f"----- CONTACT FORM EMAIL NOT SENT: {contact_response=} {site}: {site.upper()} -----"
        )

    if contact_response and consult_response and site == Sites.test:
        mailer.send_mail(
            f"COMPLETED SELENIUM WEB TESTING ON: {site} WITHOUT FORM ERRORS"
        )
        logger.info(
            f"***** COMPLETED WEB TESTING FOR SITE: {site.upper()} WITHOUT FORM ERRORS *****"
        )

    BROWSER.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Select which website for Selenium to test"
    )
    parser.add_argument("site", choices=[c.name for c in Sites])

    args = parser.parse_args()
    site2test = Sites[args.site].value

    main(site=site2test)
