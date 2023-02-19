import quickstart

#   A    |    B     |       C        |   D  |   E   | F     | G         
#rowNum | rowName | rowName_Extra | Cost | Price | Tax_1 | Dept_ID 

#The ID and range of a sample spredsheet
SPREADSHEET_ID = '1yvUQJTU1kAATaT_nhfTckbLCTGtyPPnbrRgogZX1XkU'
RANGE_NAME = 'Store Inventory'

sheet = quickstart.getValues(SPREADSHEET_ID, RANGE_NAME)

print(sheet)

for row in sheet:
	# Print columns A and E, which correspond to indices 0 and 4.
	print('%s, %s, %s, %s ' % (row[0], row[1], row[2], row[3]))

