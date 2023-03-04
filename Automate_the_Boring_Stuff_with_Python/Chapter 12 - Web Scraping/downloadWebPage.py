import requests 
import os
from pathlib import Path

filename = 'RomeAndJuliet.txt'
sourcePath = os.path.dirname(os.path.abspath(__file__))
fileDir = Path(sourcePath) / filename


#Functions
def displayResult():
	print("connection: " + str(res.status_code == requests.codes.ok))
	print(str(len(res.text)) + ' characters long')
	print(res.text[:2250])

#Start
webAddress = 'https://automatetheboringstuff.com/files/rj.txt'
res = requests.get(webAddress)
type(res)

try:
	res.raise_for_status()
	# 'wb' Write Binary to perserve Unicode encoding
	playFile = open(fileDir, 'wb')
	for chunk in res.iter_content(100000):
		playFile.write(chunk)

	playFile.close()

	displayResult()
except Exception as exc:
	print('Error: %s' % (exc))







# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# res.raise_for_status()




