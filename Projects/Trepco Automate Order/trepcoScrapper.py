#Tepco order script
import sys
import os
import time

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


try:
	print(type(browser))

	# Navigate to Trepco.com and Login to User Account
	browser.get(trepcoLoginPage)
	accountElement = browser.find_element(By.NAME, 'ACCOUNTCDE')
	accountElement.send_keys(trepcoCreds)
	passwordElement = browser.find_element(By.NAME, 'PASS')
	passwordElement.send_keys(trepcoCreds)
	passwordElement.submit()

	# Find iframe and switch to it
	element = WebDriverWait(browser,5).until(
		EC.presence_of_element_located((By.XPATH,'html/body/div[2]/iframe')))
	print('found!: ' + element.tag_name)
	browser.switch_to.frame(element)

	# within selected iframe find Create element and execute javascript order function
	#<a href="javascript:CrtNewOrdFunc();">Create</a>
	orderElement = WebDriverWait(browser,5).until(
		EC.presence_of_element_located((By.XPATH,'//*[@id="jMenu"]/li[3]/ul/li[4]/a')))
	print('order?: ' + orderElement.tag_name)

	browser.execute_script("arguments[0].click();", orderElement)
	# orderElement.click()
	time.sleep(5)

except Exception as e:
	#print('Unable to locate element')
	print(e)

	# /html/body/div[2]/iframe
	# /html/body/ul/li[3]/ul/li[4]/a
	# /html/body/div[1]/iframe




	#Find new order
	# XPath: //*[@id="jMenu"]/li[3]/ul/li[4]/a
	# FullX: /html/body/ul/li[3]/ul/li[4]/a
	# ifram: /html/body/div[2]/iframe   <-- I can find this one
	# iparent: //*[@tag="div"]/iframe[contains(@style, "height: 100%")]
	
	#browser.implicitly_wait(5)
	#elements = browser.find_element(By.XPATH,'/html/body/div[2]/iframe')
	# elements = browser.find_element(By.XPATH, '//*[@tag="div"]/iframe')
	# browser.implicitly_wait(5)

	# for e in elements:
	# 	print(e)
	# newOrderElement = browser.find_element(By.XPATH, '//*[@id="jMenu"]/li[3]/ul/li[4]/a')
	# print( newOrderElement)
	# newOrderElement.click()
	#time.sleep(5)
