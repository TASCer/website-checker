import complete_forms
import create_service
import datetime as dt
import logging

now: dt = dt.date.today()
todays_date: str = now.strftime('%D').replace('/', '-')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(f'../{todays_date}.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)


if __name__ == "__main__":
	s = create_service.my_selenium_chrome()
	# FORMS
	complete_forms.contact_form(s)
	# complete_form.consult_forms(s) # CAPTCHA
	# run_tascs_site
	# run_hoa_site
	# run_roadspies_site