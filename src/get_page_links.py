import datetime as dt
import logging
import my_secrets
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)

# browser = create_service.my_selenium_chrome()
# logger.info("SELENIUM SERVICE CREATED FOR: FIREFOX")

# run_tascs.test_site


def collect(browser):
	logger.info("Collecting elements")
	unique_links = set()
	browser.get(my_secrets.test_consult_url)
	a_refs = browser.find_elements(By.XPATH, "//a[@href]")
	print(a_refs, len(a_refs))
	for ref in a_refs:
		link = ref.get_attribute("href")

		if link == '' or '#' in link or 'mailto' in link:
			continue

		unique_links.add(link)

	logger.info(f"{len(unique_links)} unique links found on home page")

	return unique_links
	# for l in links:
	# 	l.click()
	# run_hoa_site
	# run_roadspies_site
