import logging
from logging import Logger

from selenium.common.exceptions import ElementNotSelectableException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from mailer import email_server

logger: Logger = logging.getLogger(__name__)


def submit_consult(driver, site: str) -> bool:
    """
    Function fills out and submits a Request Consultation form.

    :param driver:
    :param site: url
    :raises TimeoutException:
    :return: True if no issues
    """
    logger.info("\tCOMPLETING CONSULT")

    if site == "https://tascs.net":
        logger.info(f"\t\tSKIPPING: {site} HAS CAPTCHA IN PLAY FOR CONSULT FORM")
        return False

    try:
        driver.get(site)
        WebDriverWait(driver, 10)

    except TimeoutException as e:
        logger.error(e)

    else:
        try:
            fname = driver.find_element(By.NAME, "firstname")
            fname.send_keys("SELENIUM CONSULT")
            WebDriverWait(driver, 10)

            lname = driver.find_element(By.NAME, "lastname")
            lname.send_keys("TESTER")
            WebDriverWait(driver, 10)

            email = driver.find_element(By.NAME, "email")
            email.send_keys("TESTER@CONSULTFORM.COM")
            WebDriverWait(driver, 10)

            company = driver.find_element(By.NAME, "company")
            company.send_keys("SELENIUM CONSULT TESTING INC.")
            WebDriverWait(driver, 10)

            phone = driver.find_element(By.NAME, "telephone")
            phone.send_keys("1234567890")
            WebDriverWait(driver, 10)

        except ElementNotSelectableException as e:
            logger.error(e)

        try:
            captcha = driver.find_element(By.NAME, "captcha")
            WebDriverWait(driver, 10)
            captcha.send_keys("7")
            WebDriverWait(driver, 10)

            driver.find_element(By.NAME, "submit").click()
            WebDriverWait(driver, 3000)

            try:
                msg: bool = WebDriverWait(driver, 15).until(
                    EC.text_to_be_present_in_element(
                        (By.ID, "msg"), text_="Request sent successfully"
                    )
                )

                if not msg:
                    raise TimeoutException

            except TimeoutException:
                logger.exception(
                    f"\t\temail not sent: Check {site}'s server logs", exc_info=False
                )
                return False

        except ElementNotSelectableException as e:
            logger.error(e)
            return False

    logger.info("\t\tEmail sent")

    return True


def submit_contact(driver, site: str) -> bool:
    """
    Function fills out and submits a Request Contact form.

    :param driver:
    :param site: url
    :raises TimeoutException:
    :return: True if no issues
    """
    logger.info("\tCOMPLETING CONTACT FORM")
    try:
        driver.get(site)
        WebDriverWait(driver, 1000)

    except TimeoutException as e:
        logger.error(e)

    name = driver.find_element(By.NAME, "name")
    name.send_keys("SELENIUM CONTACT TEST")
    WebDriverWait(driver, 1000)

    email = driver.find_element(By.NAME, "email")
    email.send_keys("TESTER@CONTACTFORM.COM")
    WebDriverWait(driver, 1000)

    company = driver.find_element(By.NAME, "company")
    company.send_keys("SELENIUM CONTACT TESTING INC")
    WebDriverWait(driver, 1000)

    phone = driver.find_element(By.NAME, "telephone")
    phone.send_keys("1234567890")
    WebDriverWait(driver, 1000)

    comments = driver.find_element(By.NAME, "message")
    comments.send_keys("SELENIUM CONTACT TESTING")
    WebDriverWait(driver, 10)

    try:
        driver.find_element(By.ID, "submit-form").click()
        msg: bool = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, "msg"), text_="Request sent successfully"
            )
        )

    except TimeoutException:
        logger.exception(f"\t\tCheck {email_server}'s logs", TimeoutException.args)
        return False

    except ElementNotSelectableException:
        logger.exception(f"\t\tEmail element Failure: Check {site}'s server logs")
        return False

    logger.info("\t\tEmail sent")

    return msg
