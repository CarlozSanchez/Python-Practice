from pathlib import path
import os
import barcode

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


for beer in beerList:
	print(beer)
