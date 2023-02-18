# Extracting sheet data to make UPC barcodes from item number
#import quickstart

import ezsheets

#The ID and range of a sample spredsheet
SPREADSHEET_ID = '1yvUQJTU1kAATaT_nhfTckbLCTGtyPPnbrRgogZX1XkU'
#RANGE_NAME = 'Corrected Store Inventory!$A$17:$G$100'
#RANGE_NAME = 'Corrected Store Inventory!A17:C100'
#RANGE_NAME = 'Corrected Store Inventory!A17:C100,G17:G100'
#RANGE_NAME = '{Corrected Store Inventory!A2:C,Corrected Store Inventory!G2:G}'
RANGE_NAME = 'Barcode Inventory'


spreadSheets = ezsheets.Spreadsheet(SPREADSHEET_ID)

data = spreadSheets[1]

print(data)

beerList = []

for row in data:
	if row[3] == 'BEER':
		beerList.append(row)

print(beerList)

for row in beerList:
	# Print columns A and E, which correspond to indices 0 and 4.
	print('%s, %s, %s, %s ' % (row[0], row[1], row[2], row[3]))


#values = quickstart.getValues(SPREADSHEET_ID, RANGE_NAME)

#print('ItemNum, ItemName: , ItemName 2, Department: ')

#print(values)
#for row in data:
	# Print columns A and E, which correspond to indices 0 and 4.
	#print('%s, %s, %s, %s ' % (row[0], row[1], row[2], row[3]))


# Creats a list of only beer products