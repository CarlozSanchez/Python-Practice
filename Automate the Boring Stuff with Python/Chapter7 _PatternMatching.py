import re


line = 'AALBORG AAL JUBIL AQUA B6/700ML 6 323252 $109.37 8-17469-01001-9 $18.23 8-17469-01001-9 1/1/2023 12/31/2039'


idRegex = re.compile(r' \d{5,6} ')
upcRegex = re.compile(r'\d-\d{5}-\d{5}-\d')
priceRegex = re.compile(r'\$\d{0,6}\.\d\d')

#description1Regex = re.compile(r'[A-Z]\d{1,2}\/\d{1,3}[A-Z]{1,2}')
descriptionRegex = re.compile(r'[B,C,P]\d{1,3}')

#print(upcRegex.search(line))
upc = upcRegex.findall(line)

price =priceRegex.findall(line)

productID = idRegex.search(line)



# split line in half between product ID
result = line.split(productID.group())
leftSide = result[0]
rightSide = result[1]


# find description from left half
description = descriptionRegex.search(leftSide)

# find the beggining of description
descriptionStartIndex = description.span()[0]

brand = leftSide[0:descriptionStartIndex] 
theRest = leftSide[descriptionStartIndex:len(leftSide)]

newList = theRest.split(' ')

unitPerCase = newList[-1]

des = leftSide[descriptionStartIndex: len(leftSide) - (len(unitPerCase)) -1] 

print('Brand: '+ brand)

#print(theRest)
print('Description: ' + des)
print('Unit Per Case: ' + unitPerCase)
print( 'Produce ID: ' + productID.group())
#brand = result[0: description.span()[0]] 

#print (brand)
