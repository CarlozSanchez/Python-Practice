import sys
from selenium import webdriver


print('version: ' + sys.version)

browser = webdriver.Firefox()

type(browser)

browser.get('https://inventwithpython.com')