'''
Chapter 12 Web Scraping

2048

2048 is a simple game where you combine tiles by sliding them up, down,
left, or right with the arrow keys. You can actually get a fairly high score
by repeatedly sliding in an up, right, down, and left pattern over and over
again. Write a program that will open the game at https://gabrielecirulli
.github.io/2048/ and keep sending up, right, down, and left keystrokes to
automatically play the game.

'''
# URL has changed since the release of the book, is now:
GAMEURL='https://play2048.co/'

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

with webdriver.Firefox() as browser:
    browser.get(GAMEURL)
    htmlElem = browser.find_element_by_tag_name('html')
    
    while True:
        try:
            browser.find_element_by_css_selector('.game-over')
            break
        except NoSuchElementException:
            htmlElem.send_keys(Keys.ARROW_UP)
            htmlElem.send_keys(Keys.ARROW_RIGHT)
            htmlElem.send_keys(Keys.ARROW_DOWN)
            htmlElem.send_keys(Keys.ARROW_LEFT)   
    
    scoreElem = browser.find_element_by_css_selector('.score-container')
    print(f'Your score is: {scoreElem.text}')