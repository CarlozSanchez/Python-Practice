import barcode
import ezsheets
import os

from pathlib import Path
from barcode.writer import ImageWriter



#   0    |    1     |       2        |   3  |   4   |   5   |    6 
#   A    |    B     |       C        |   D  |   E   |   F   |    G         
#ItemNum | ItemName | ItemName_Extra | Cost | Price | Tax_1 | Dept_ID 
#The ID and range of a sample spredsheet
print('Process Started...\n.\n.')
SPREADSHEET_ID = '1yvUQJTU1kAATaT_nhfTckbLCTGtyPPnbrRgogZX1XkU'

# Store inventory to process
spreadSheets = ezsheets.Spreadsheet(SPREADSHEET_ID)
sheet = spreadSheets[0]
print(spreadSheets.title + 'Aquired !!!\n.\n.')

# Create path to store UPC images
fileName = 'default'
sourcePath = os.path.dirname(os.path.abspath(__file__)) 
barcodeDir = Path(sourcePath) / 'Barcodes'

if not barcodeDir.exists():
	os.makedirs(barcodeDir)

#Create a TXT file to store output results
resultFile = open((barcodeDir / 'Result.txt'), 'w')
errorFile = open((barcodeDir / 'Error_Report.txt'), 'w')

# Initialize upc's for processing
ean8 = barcode.get_barcode_class('ean8')
upca = barcode.get_barcode_class('upca')
ean13 = barcode.get_barcode_class('ean13')
ean14 = barcode.get_barcode_class('ean14')

# Initialize variables
barcode = None
count = 0
missed = 0
prefix = 'upc_'
eanType =''

buf1, buf2, buf3, buf4, buf5 = 8, 24, 16, 38, 20
s1, s2, s3, s4 = '', '', '', ''


print(str(sheet))
print('Processing......  Please Wait!')

# Iterate trough all rows and create approiate UPC
for i, row in enumerate(sheet):
	#if(i >= 50): 
	 	#break

	try: # Decice with type of barcode to make based of column(item_num) info
		if(len(row[0]) == 8):
			barcode = ean8(row[0], ImageWriter())
			eanType = 'ean8'

		elif(len(row[0]) == 12):
			barcode = upca(row[0], ImageWriter())
			eanType = 'ean12'

		elif(len(row[0]) == 13):
			barcode = ean13(row[0], ImageWriter())
			eanType = 'ean13'

		elif(len(row[0]) == 14):
			barcode = ean14(row[0], ImageWriter())
			eanType = 'ean14'

		else:
			raise NoMatchError('Unable to find an EAN Match')

	except Exception as e: #Something went wrong, dont make UPC from current row and log error
		s1 = '[' + str(i) + ']'
		s2 = row[0]
		s3 = '!ERROR! ' + str(len(row[0]))
		s4 = 'item: ' + row[1]
		s5 = str(e.args)

		barcode = None
		missed += 1
		errorFile.write('%s%s%s%s%s\n' 
			% (s1.ljust(buf1), s2.ljust(buf2), s3.ljust(buf3), s4.ljust(buf4), s5.ljust(buf5)))

	else: #All good save barcode as PNG file to barcode Directory
		fileName = prefix + str(row[0])
		result = barcode.save((barcodeDir / fileName), options = {'write_text':False})

		#Output text file info
		s1 =  '[' + str(i) + ']'
		s2 = row[0]
		s3 = 'ean: ' + eanType
		s4 = 'location: ' +  str(barcodeDir)
		s5 = ''

		count += 1

	finally: # Write info about processed item to output file
		resultFile.write('%s%s%s%s%s\n' 
			% (s1.ljust(buf1), s2.ljust(buf2), s3.ljust(buf3), s4.ljust(buf4), s5.ljust(buf5)))
	 
# Print results
message = ('\n----- ' + str(count) + ' items processed, '  + str(missed) 
	+ ' skipped -----')

print(message)
resultFile.write(message)
resultFile.close()
errorFile.close()











# print(sheet)
# for row in sheet:
# 	# Print columns A and E, which correspond to indices 0 and 4.
# 	print('%s, %s, %s, %s ' % (row[0].ljust(14), row[1], row[2], row[3]))




#print('ItemNum, ItemName: , ItemName 2, Department: ')



# Creats a list of only beer products


'''



print(data)

beerList = []

for row in data:
	if row[3] == 'BEER':
		beerList.append(row)

print(beerList)

for row in beerList:
	# Print columns A and E, which correspond to indices 0 and 4.
	print('%s, %s, %s, %s ' % (row[0], row[1], row[2], row[3]))


'''