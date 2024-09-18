# https://stackoverflow.com/questions/18439851/how-can-i-download-a-file-on-a-click-event-using-selenium
import my_secrets
import os

from selenium import webdriver
from selenium.common.exceptions import ElementNotSelectableException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver.chrome.service import Service as CService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile as FFProfile
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# FILENAME = "HOA Contact List (PDF).pdf"
# URL = "https://surpriseaz.gov/462/HOA-Community-Contacts"

TEST_FILENAME = "StrengthLeadershipTest.pdf"
TEST_URL = "https://tascs.test/why-tasc"

# FF - WORKING headless
def pdf_download():
    filepath = os.path.join("../output", TEST_FILENAME)
    if os.path.exists(filepath):
        os.remove(filepath)

    options = FFOptions()
    ff_profile = FFProfile()
    options.set_preference('browser.download.folderList', 2)
    options.set_preference('browser.download.manager.showWhenStarting', False)
    options.set_preference('browser.download.manager.focusWhenStarting', False)
    options.set_preference('browser.download.dir', os.path.abspath('../output'))
    options.set_preference('browser.helperApps.alwaysAsk.force', False)
    options.set_preference('browser.download.manager.alertOnEXEOpen', False)
    options.set_preference('browser.download.manager.closeWhenDone', True)
    options.set_preference('browser.download.manager.showAlertOnComplete', False)
    options.set_preference('browser.download.manager.useWindow', False)
    options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')
    options.set_preference('pdfjs.disabled', True) # KEY!!
    options.set_preference("browser.download.alwaysOpenPanel", False)
    options.binary_location = r"P:\Firefox\firefox.exe"
    options.profile = ff_profile
    options.add_argument('-headless')

    service = FFService(f"{my_secrets.firefox_driver}")

    ff_browser = webdriver.Firefox(service=service, options=options)
    ff_browser.get(TEST_URL)

    try:
        pdf_link = WebDriverWait(ff_browser, 30).until(
            EC.presence_of_element_located((By.XPATH,
                # "/html/body/div[4]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/ul/li/a"))) #Surprise
                "/html/body/div[3]/div/div/div[5]/div/div[2]/ul/li[2]/a")))  # LOCAL strengthfinder report

        pdf_link.click()
        ff_browser.implicitly_wait(2)
        ff_browser.close()

    except (ElementNotSelectableException, TimeoutException) as err:
        print(err)

# CHROME ISSUES
# def pdf_download():
# NO WORKIE, pdf just sits there below prefs are not affecting, manual changes work
#     options = COptions()
#     options.add_experimental_option('prefs', {
#         "download.default_directory": "C:\\Users\\todd\\Desktop",
#         "download.prompt_for_download": False,
#         "plugins.always_open_pdf_externally": True
#     })
#
#     service = CService(f"{my_secrets.chrome_driver}")

    # options.add("plugins.plugins_disabled=Chrome PDF Viewer");
    # options.add_argument("--remote-allow-origins=*")

    # options.add_argument("--start-maximized")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option("useAutomationExtension", False)
    # options.add_argument("--disable notifications")

    # chr_browser = webdriver.Chrome(service=service, options=options)
    #
    # chr_browser.get(URL)
    #
    # try:
    #     pdf_link = WebDriverWait(chr_browser, 30).until(
    #         EC.presence_of_element_located((By.XPATH,
    #             # "/html/body/div[4]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/ul/li/a"))) # Surprise web
    #                "/html/body/div[3]/div/div/div[5]/div/div[2]/ul/li[2]/a"))) # LOCAL strengthfinder report
    #
    # except BaseException as err:
    #     print(err)
    #
    #
    # WebDriverWait(chr_browser, 10000)
    # print(pdf_link.get_attribute('href'))
    # pdf_link.click()
    # chr_browser.implicitly_wait(2)


if __name__ == "__main__":
    pdf_download()