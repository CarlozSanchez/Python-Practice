import requests, bs4
import os
from pathlib import Path

# Opening an HTML from website
res = requests.get('https://nostarch.com')
res.raise_for_status();
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))

 # Opening an HTML file from hardrive
workingDirectory = Path(os.path.dirname(os.path.abspath(__file__)))
exampleFile = open(workingDirectory / 'example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
print(type(exampleSoup))
print('\n------------')

# Working with selectors
elements = exampleSoup.select('#author')
type(elements) #elements is a list of Tag Objects

print('element list ' + str(len(elements)))
print('type: ' + str(elements[0]))
print('as string: ' + str(elements[0]))  # The Tag Objects as a string
print('get Text: ' + elements[0].getText())
print('attributes: ' + str(elements[0].attrs))

print('\n------------')

# Extractig <p> element
pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())

# Getting Data
print('\n------------')
spanElem = exampleSoup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)

