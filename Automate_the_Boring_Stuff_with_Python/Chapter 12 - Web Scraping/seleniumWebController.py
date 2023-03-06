import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


print('version: ' + sys.version)
browser = webdriver.Firefox()
print(type(browser))


# # Finding element by class name
# try:
# 	browser.get('https://inventwithpython.com')
# 	elem = browser.find_element(By.CLASS_NAME, 'cover-thumb')
# 	print('found <%s> element with that class name!' % (elem.tag_name))

# except Exception as e:
# 	print('Was not able to find an element with that name.')
# 	print(e)

# # Finding link by text name and clicking
# try:
# 	linkElem = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
# 	linkElem.click()
# 	# browser.implicitly_wait(5) # seconds
# 	time.sleep(5)
# 	chap1Elem = browser.find_element(By.LINK_TEXT,'Introduction')
# 	chap1Elem.click()

# except Exception as e:
# 	print(e)


# # Find text field and submiting info
# # Look in pyinputplus.inputPassword() Chapter 8
# try:
# 	browser.get('https://login.metafilter.com')
# 	userElem = browser.find_element(By.ID,'user_name')
# 	userElem.send_keys('Sabasan')

# 	passwordElem = browser.find_element(By.ID,'user_pass')
# 	passwordElem.send_keys('love1034r')
# 	passwordElem.submit()
# except Exception as e:
# 	print(e)


# #Scrolling Browser
# try:
# 	browser.get('https://nostarch.com')
# 	htmlElement = browser.find_element(By.TAG_NAME,'html')
# 	htmlElement.send_keys(Keys.END)
# 	time.sleep(5)
# 	htmlElement = browser.find_element(By.TAG_NAME,'html')
# 	htmlElement.send_keys(Keys.HOME)

# except Exception as e:
# 	print(e)


try:
	browser.get("https://www.tutorialspoint.com/index.htm")
	javaElement = browser.find_element(By.XPATH,"//*[text()='Library']")
	print('found: ' + javaElement.tag_name)

	browser.execute_script("arguments[0].click();",javaElement)

	print('Page title after clic: ' + browser.title)
	time.sleep(5)
except Exception as e:
	print(e)
