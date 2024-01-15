![TASCS LOGO](./assets/logo.png)

# Selenium Website Testing
My Selenium solution used to test my website's various html links and forms.
Using Python 3.11 
Depdendancies noted in requirements.txt

# Links
1. Securely download compressed log files from website hosting provider
2. Decompress log files 
3. PARSE exported log files


# Forms
4. LOAD unique sources from parsed logs into sources table
        - New entries into lookup table will have a NULL COUNTRY and DESCRIPTION value
5. LOAD parsed logs into MySQL 5.7.20-log log table
6. Convert ASN country Alpha-2 code to full country name using IPWhois 
7. SET full county names, ASN Descriptions, and ALPHA2 Codes in sources table
     a. If IPWhois error during source ip lookup, exception message is entered as country name
     b. If country ALPHA2 code not found, log source
8. Visuals of webserver activity saved in output directory

src folder contains: 

        1. Python files needed to run tests

assets folder contains:

        1. sample_log with 1 day of my webserver anonymized logfile (testlog.csv)
        2. Plotting examples
        3, A .env template


