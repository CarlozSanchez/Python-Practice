#Tepco order script
import sys
import os
import time

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

global browser

#Trepco website
trepcoLoginPage = 'http://199.26.120.133:2010/cgi-bin/webcon/gateway.pgm?DIRECT=UUPDXFR'

# Get Trepco Login info
filename = 'TrepcoCreds.txt'
filePath = Path.home() / filename
file = open(filePath)
trepcoCreds = file.read().strip()
file.close()

# Lauch Browser
print('version: ' + sys.version)
browser = webdriver.Firefox()

# Orders
#<a href="javascript:CrtNewOrdFunc();">Create</a>

try:
	print(type(browser))
	browser.get(trepcoLoginPage)
	accountElement = browser.find_element(By.NAME, 'ACCOUNTCDE')
	accountElement.send_keys(trepcoCreds)
	passwordElement = browser.find_element(By.NAME, 'PASS')
	passwordElement.send_keys(trepcoCreds)
	passwordElement.submit()

	#Find new order
	newOrderElement = browser.find_element(By.PARTIAL_LINK_TEXT, 'Create')
	newOrderElement.click()
	time.sleep(5)

except Exception as e:
	print(e)