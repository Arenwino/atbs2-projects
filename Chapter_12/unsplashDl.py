'''
Chapter 12 Web Scraping

Image Site Downloader

Write a program that goes to a photo-sharing site like Flickr or Imgur,
searches for a category of photos, and then downloads all the resulting
images. You could write a program that works with any photo site that
has a search feature.
'''

# unsplashDl.py - Downloads all images on unsplash.com which are
# tagged with the searchterm
# USAGE: python unsplashDl.py searchterm

from selenium import webdriver
import logging, time, requests, re, sys

UNSPLASHSEARCHURL = 'https://unsplash.com/s/photos/'
UNSPLASHDOWNLOADURLSUFFIX = '/download?force=true'
SCROLL_PAUSE_TIME = 1
FILENAMEREGEX = r'(&dl=)(.*?)$'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Selenium Loggers are really spammy, so their level is set to ERROR
urllib3Logger = logging.getLogger('urllib3.connectionpool')
urllib3Logger.setLevel(logging.ERROR)
seleniumRemoteLogger = logging.getLogger('selenium.webdriver.remote.remote_connection')
seleniumRemoteLogger.setLevel(logging.ERROR)

if(len(sys.argv) > 1):

    searchTerm = '-'.join(sys.argv[1:])

    searchURL = UNSPLASHSEARCHURL + searchTerm
    logging.debug(searchURL)

    last_height = 0

    with webdriver.Firefox() as browser:
        browser.get(searchURL)

        time.sleep(2)

        # Unsplash has a endless scrolling, to download ALL images you have to
        # scroll to the true bottom of the page.
        while True:
            # Scroll down to bottom
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # all photos have a "a"-attribute named itemprop  
        photoLinkElements = browser.find_elements_by_css_selector("a[itemprop=contentUrl]")
        logging.debug(f'found {len(photoLinkElements)} photos for {searchTerm}')
        
        for photoLinkElement in photoLinkElements:
            photoDeepLink = f'{photoLinkElement.get_attribute("href")}{UNSPLASHDOWNLOADURLSUFFIX}'
            logging.info(f'downloading {photoDeepLink}')
            res = requests.get(f'{photoDeepLink}')
            
            filenameMo = re.search(FILENAMEREGEX, res.url)
            if(filenameMo is None):
                logging.warning('failed to extract filename, skipping file')
                continue
            else:
                photoFilename = filenameMo.group(2)
            logging.debug(f'writing {photoFilename}')
            with open(photoFilename, mode='wb') as photoFile:
                for chunk in res.iter_content(100000):
                    photoFile.write(chunk) 

else:
    print('USAGE: python unsplashDl.py searchterm')