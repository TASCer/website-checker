import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotSelectableException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)


def submit_consult(browser, site: str) -> bool:
    logger.info("\tCOMPLETING CONSULT")

    if site == "https://tascs.net":
        logger.info(f"\t\tSKIPPING: {site} HAS CAPTCHA IN PLAY FOR CONSULT FORM")
        return False

    try:
        browser.get(site)
        WebDriverWait(browser, 10)

    except TimeoutException as e:
        logger.error(e)

    else:
        try:
            fname = browser.find_element(By.NAME, "firstname")
            fname.send_keys("SELENIUM CONSULT")
            WebDriverWait(browser, 10)

            lname = browser.find_element(By.NAME, "lastname")
            lname.send_keys("TESTER")
            WebDriverWait(browser, 10)

            email = browser.find_element(By.NAME, "email")
            email.send_keys("TESTER@CONSULTFORM.COM")
            WebDriverWait(browser, 10)

            company = browser.find_element(By.NAME, "company")
            company.send_keys("SELENIUM CONSULT TESTING INC.")
            WebDriverWait(browser, 10)

            phone = browser.find_element(By.NAME, "telephone")
            phone.send_keys("1234567890")
            WebDriverWait(browser, 10)

        except ElementNotSelectableException as e:
            logger.error(e)

        try:
            captcha = browser.find_element(By.NAME, "captcha")
            WebDriverWait(browser, 10)
            captcha.send_keys("7")
            WebDriverWait(browser, 10)

            browser.find_element(By.NAME, "submit").click()
            WebDriverWait(browser, 3000)

            try:
                msg = WebDriverWait(browser, 15).until(
                    EC.text_to_be_present_in_element(
                        (By.ID, "msg"), text_="Request sent successfully"
                    )
                )

                if not msg:
                    raise TimeoutException

            except TimeoutException as to_err:
                logger.error(f"\t\t{to_err}: Check {site}'s server logs")
                return False

        except ElementNotSelectableException as e:
            logger.error(e)
            return False

    logger.info("\t\tEmail sent")

    return True


def submit_contact(browser, site: str) -> bool:
    logger.info("\tCOMPLETING CONTACT FORM")
    try:
        browser.get(site)
        WebDriverWait(browser, 1000)

    except TimeoutException as e:
        logger.error(e)

    name = browser.find_element(By.NAME, "name")
    name.send_keys("SELENIUM CONTACT TEST")
    WebDriverWait(browser, 1000)

    email = browser.find_element(By.NAME, "email")
    email.send_keys("TESTER@CONTACTFORM.COM")
    WebDriverWait(browser, 1000)

    company = browser.find_element(By.NAME, "company")
    company.send_keys("SELENIUM CONTACT TESTING INC")
    WebDriverWait(browser, 1000)

    phone = browser.find_element(By.NAME, "telephone")
    phone.send_keys("1234567890")
    WebDriverWait(browser, 1000)

    comments = browser.find_element(By.NAME, "message")
    comments.send_keys("SELENIUM CONTACT TESTING")
    WebDriverWait(browser, 10)

    try:
        browser.find_element(By.ID, "submit-form").click()
        msg: bool = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, "msg"), text_="Request sent successfully"
            )
        )

    except TimeoutException as to_err:
        logger.error(f"\t\t{to_err.msg}: Check {site}'s server logs")
        return False

    except ElementNotSelectableException as elem_err:
        logger.error(
            f"\t\tEmail element Failure: Check {site}'s server logs {elem_err}"
        )
        return False

    except Exception as base_err:
        logger.error(f"\t\tEmail base Failure: {site} -> {base_err}")
        return False

    logger.info("\t\tEmail sent")

    return msg
