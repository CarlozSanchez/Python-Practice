import requests 

#Functions
def displayResult():
	print("connection: " + str(res.status_code == requests.codes.ok))
	print(str(len(res.text)) + ' characters long')
	print(res.text[:2250])

#Start
webAddress = 'https://xxxautomatetheboringstuff.com/files/rj.txt'
res = requests.get(webAddress)
type(res)

try:
	res.raise_for_status()
	displayResult()
except Exception as exc:
	print('Error: %s' % (exc))





