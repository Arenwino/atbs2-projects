'''
Chapter 12 Web Scraping

Command Line Emailer

Write a program that takes an email address and string of text on the
command line and then, using selenium, logs in to your email account
and sends an email of the string to the provided address. (You might
want to set up a separate email account for this program.)
This would be a nice way to add a notification feature to your programs.
You could also write a similar program to send messages from
a Facebook or Twitter account.
'''

emailAddress = 'my@emailaddress'
emailRecipient = ''
emailLoginPage = 'https://webmailer.hosteurope.de/login.php?server=squirrel&version=1&'
emailComposePage = 'https://webmailer.hosteurope.de/squirrelmail_new/src/compose.php?mailbox=INBOX&startMessage=1'
emailMessage = ''
logoutLink = 'Abmelden'

from selenium import webdriver
import pyinputplus as pyip

import logging, sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if(len(sys.argv) >= 2):
    emailRecipient = sys.argv[1]
    emailMessage = ''.join(sys.argv[2:])

    logging.debug(f'sending {emailMessage} to recipient {emailRecipient}')    

    with webdriver.Firefox() as browser:

        browser.get(emailLoginPage)

        usernameElement = browser.find_element_by_id('username')
        usernameElement.send_keys(emailAddress)

        passwordElement = browser.find_element_by_id('password')
        passwordInput = pyip.inputPassword()

        passwordElement.send_keys(passwordInput)

        submitElement = browser.find_element_by_id('form_submit')
        submitElement.click()
        logging.info(f'Logging in with {emailAddress}')

        # User is logged in, get the compose page
        browser.get(emailComposePage)

        toElement = browser.find_element_by_name('send_to')
        toElement.send_keys(emailRecipient)

        subjectElement = browser.find_element_by_name('subject')
        subjectElement.send_keys('Testmessage')

        mailBodyElement = browser.find_element_by_name('body')
        mailBodyElement.send_keys(emailMessage)

        submitButton = browser.find_element_by_name('send')
        # submit() doesn't seem to work, using click()
        submitButton.click()
        logging.info(f'Email successfully sent')

        logoutLinkElement = browser.find_element_by_partial_link_text(logoutLink)
        logoutLinkElement.click()

else:
    print("USAGE: python commandLineEmail.py emailRecipient EmailMessage")


