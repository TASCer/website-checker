![TASCS LOGO](./assets/logo.png)

# Website Testing Using Selenium
My solution utilized to schedule testing of my various website's html links and forms.


#### TEST STEPS

1. Goes through all links in menu bar
1. Completes the two html php forms to send request e-mail(s)

   a. CONTACT form has captcha, not ran on production. Hardcoded in TEST

1. Visits HOA page to get:
   a. The last date and time rental data was updated 

   b. Legacy Parc rental percentage

   c. Rental percentage for all monitored communities 

1. Visits BLOG site to get:

   a. Count of blogs on first page
   
   b. Latest blog post title

src folder contains: 

1. Python files needed to run tests
   - A managed option (create_broswer_managed) for creating driver/browser using [webdriver-manager](https://pypi.org/project/webdriver-manager/)

assets folder contains:

1. Logo file for README

misc folder contains: 

1. Windows batch file for launching Scheduled Tasks 
2. Shell scripts for launching cron jobs 
3. gecko driver for Firefox
4. my_secrets.py template for environment variables
