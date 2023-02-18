from io import BytesIO
import os

from pathlib import Path

from barcode import EAN13
import barcode
from barcode.writer import SVGWriter
from barcode.writer import ImageWriter

fileName = 'test'
fileDirectory = 'Files/Programming/Python/python-barcode'
filePath = Path.home() / fileDirectory/fileName

barcodes = [
    ['009300000307', 'Mount Olive Sweet Relish'],
    ['9800001088', 'tic tac cherry'],
    ['9800007608', 'tic tac fruit'],
    ['9800007615', 'tic tac freshmint'],
    ['9800007639', 'tic tac orange'],
    ['9800007677', 'tic tac wintergreen'],
    ['9800123018', 'Ferrero Rocher'],
]

for i in barcodes:
	print(i)

    #rv = BytesIO()
    #EAN13(str(9300000307), writer=ImageWriter()).write(rv)

barcode.PROVIDED_BARCODES

EAN = barcode.get_barcode_class('ean13')

my_ean = EAN(barcodes[0][0])

result = my_ean.save(filePath)