from pathlib import Path
from PyPDF2 import PdfReader
import re

# Document name
documentName = 'Sazerac On Prem.pdf' 
midPath = 'Google Drive/VFMarket1510'

#filePath = Path.home()  / 'Files/Programming/Python'\
#	/'Automate the Boring Stuff with Python'\
#	/'automate_online-materials'/ documentName

#Create Path to file
filePath = Path.home() / midPath / documentName


#Open files with PFD Reader
reader = PdfReader(filePath)

#Count the pages
numberOfPages = len(reader.pages)


#Read the first page and convert text to array of lines
'''page = reader.pages[0]
text = page.extract_text()
lines = list(text.split("\n"))'''

#print ('the file name is' + textOutput)

#Create file Writer
outFileName =  documentName.split('.')[0] + '_Content.txt'
filePath = Path.home() / midPath / outFileName

#open file
file = open(filePath, 'w')

counter = 0

#Regex
idRegex = re.compile(r' \d{5,6} ')
descriptionRegex = re.compile(r'[B,C,P]\d{1,3}\/|\d{1,2}\/|[B,C,P]\d{1,3} \d{1,3}')

def processLeft(string):
		#Find Description from left half line
		descriptionFound = descriptionRegex.search(string)
		
		#Extract and remove Brand from string
		brand = string[0:descriptionFound.span()[0]]
		string = string[descriptionFound.span()[0]:len(string)]

		#split remaining left side onto string list, unit price is located in last index of list
		left = string.split(' ')
		unitPerCase = left[-1]

		#description is
		description = string[0: len(string) - len(unitPerCase)]


		#write all found elements to text file
		file.write(brand.ljust(30, ' ') + '|' + description.ljust(18, ' ') + '|' 
			+ unitPerCase.ljust(5, ' ') + '|' + productID.ljust(10, ' ') + '|'
			 + rightSide + '\n')


#iterate through pdf and copy content to output txt file
for i, page in enumerate(reader.pages):
#for i in range(1):
	page = reader.pages[0]
	print('Page: ' + str(i))
	text = page.extract_text()
	lines = list(text.split('\n'))

	#skip the first 10 lines, 
	for j, line in enumerate(lines[10:], start =10):

		#check for footer and skip rest of lineing
		if line.startswith('Pricing as of'):
			break

		#Find product ID 
		idFound = idRegex.search(line)
		productID = idFound.group().strip()

		#Split line into two string in between id  [leftSide] [id] [rightSide]
		newList = line.split(idFound.group())
		leftSide = newList[0]
		rightSide = newList[1]

		processLeft(leftSide)


		counter +=1
		
'''

		#Find Description from left half line
		descriptionFound = descriptionRegex.search(leftSide)
		
		#Extract Brand then cut off from left side list
		brand = leftSide[0:descriptionFound.span()[0]]
		leftSide = leftSide[descriptionFound.span()[0]:len(leftSide)]

		#split remaining left side onto string list, unit price is located in last index of list
		left = leftSide.split(' ')
		unitPerCase = left[-1]

		#description is
		description = leftSide[0: len(leftSide) - len(unitPerCase)]


		#write all found elements to text file
		file.write(brand.ljust(30, ' ') + '|' + description.ljust(18, ' ') + '|' 
			+ unitPerCase.ljust(5, ' ') + '|' + productID.ljust(10, ' ') + '|'
			 + rightSide + '\n')

		counter += 1
'''

file.close()

print(str(counter) + ': items processed')




#print('Total pages: ' + line(numberOfPages))
#print('----------------------------------')
#for i, line in enumerate(lines):
#	print("[" + line(i) + "] " + line.replace(' ', '*'))



#print(text)
#text = page2.extract_text()
#print('----------------------------------')
#print(text)




