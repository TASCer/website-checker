![TASCS LOGO](./assets/logo.png)

# Website Testing Using Selenium
My solution utilized to schedule testing of my various website's html links and forms.


#### TESTS

1. Goes through all links in menu bar
2. Completes the two html php forms to send request e-mail(s)

   a. CONTACT form has captcha, not ran on production. Hardcoded in TEST

4. Visits HOA page to get the last date and time rental data was updated 
4. Visits HOA and gets area and Legacy Parc Rental Percentages 
5. Visits BLOG site and gets count of blogs on first page and latest blog title

src folder contains: 

        1. Python files needed to run tests

assets folder contains:

        1. Logo file for README

misc folder contains: 

        1. Windows batch file for launching Scheduled Tasks 
        2. Shell scripts for launching cron jobs 
        3. gecko driver for Firefox
        4. my_secrets.py trmplate for environment variables
