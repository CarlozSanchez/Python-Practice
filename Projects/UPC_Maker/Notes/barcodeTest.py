import os
from io import BytesIO
from pathlib import Path

import barcode
from barcode.writer import SVGWriter
from barcode.writer import ImageWriter

fileName = 'default'
fileDirectory = Path.home() / 'Barcode Output' 
filePath = Path(fileDirectory)

sourcePath = os.path.dirname(os.path.abspath(__file__))
barcodeDir = Path(sourcePath) / 'Barcodes'

if not barcodeDir.exists():
    os.makedirs(barcodeDir)

upca = barcode.get_barcode_class('upca')
ean8 = barcode.get_barcode_class('ean8')
EAN = barcode.get_barcode_class('ean13')

barcode = None

beerList = [
['798373126020', 'Magic Hat 6 bottles', None , 'BEER' ],
['798449008113', 'Ace Cider Pineapple 6pk bottle', None , 'BEER'] ,
['798449008243', 'Ace Cider Pineapple 6pk cans',None , 'BEER' ],
['810058730206', 'Flying Ember Cherry 6pk can', 'Hibiscus - kombucha', 'BEER' ],
['810058730305', 'Flying Ember 6pk can', 'kombucha tropical hop', 'BEER' ],
['01810622', 'Bud Light 12oz 6pk cans', None, 'BEER' ],
['01811524', 'Bud Light 16oz 6pk cans', '6pk cans', 'BEER'] ,
['01812620', 'Budweiser 40oz bottle',None , 'BEER' ],
['01813027', 'King Cobra 32oz bottle', None, 'BEER' ] ,
]

printOptions = {'write_text':True, 'quiet_zone':2}

print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))



prefix = 'upc_'
for item in beerList:

    if(len(item[0]) == 12):
        fileName = prefix + str(item[0])
        barcode = upca(item[0], writer = ImageWriter()) #PNG Version
        #barcode = upca(item[0])  #SVG Version 

    elif(len(item[0]) == 8):
        fileName = prefix + str(item[0])
        barcode = ean8(item[0], writer = ImageWriter())

    else:
        print('Unable to process: ' + i)
        barcode = None


    if barcode:
        result = barcode.save(barcodeDir / fileName, printOptions)
        print(fileName.ljust(16) + " was saved to : " + str(barcodeDir))

    #print( str(len(i[0])))

    #rv = BytesIO()
    #EAN13(str(9300000307), writer=ImageWriter()).write(rv)

#print(barcode.PROVIDED_BARCODES)



#my_ean = EAN(barcodes[0][0])


#print(Path.cwd())
#result = my_ean.save(filePath / fileName)
#print("Your barcode was saved to : " + str(fileDirectory))