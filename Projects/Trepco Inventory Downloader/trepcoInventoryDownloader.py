

import sys
import requests
import os
import re
import csv
from pathlib import Path

print('version: ' + sys.version)

fileName = 'prodSelect_501305.js'
sourcePath = os.path.dirname(os.path.abspath(__file__))
fileDir = Path(sourcePath) / fileName


with open(fileDir,'r') as file:
	file_contents = file.read()


print(file_contents[:300] + '\n')

# Extract data from string
start_index = file_contents.index('[')
end_index = file_contents.rindex(']')
data = file_contents[start_index:end_index+1]

# Convert data to list of lists
data = data.replace('[', '').replace(']','')
data = data.split('\n')
data = [x.strip().replace('"', '').split(',') for x in data if len(x.strip()) > 0]

# Remove <a> tags from first element of each inner list
data = [[re.sub(r'<[^>]+>', '', x[0]), x[1]] for x in data]

for i in range(len(data)):
    data[i][0], data[i][1] = data[i][1], data[i][0]

for i, item in enumerate(data):
	print('[%s] %s , %s' % (i,data[i][0], data[i][1]))
	if i > 9:
		break

# Save data to CSV file
output_file = Path(sourcePath) / 'product_data.csv'
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

# Print location of saved file
print('\n%s items were processed!' % (str(len(data))))
print('Data saved to: {}'.format(os.path.abspath(output_file)))

# print(len(data))
# for index, item in enumerate(data):
# 	print(item)
# 	if index >= 10:
# 		break


# def displayResult():
# 	print('connection ' + str(result.status_code == requests.codes.ok))
# 	print(str(len(result.text)) + ' characters long')
# 	print(result.text[:200])

# dataBaseAddress = 'http://199.26.120.133:2010/webcon/appdata/prodSelect_501305.js?_=1678096427899'
# result = requests.get(dataBaseAddress)
# type(result)

# try:
# 	result.raise_for_status()
# 	dbFile = open(fileDir, 'wb')
# 	for chunk in result.iter_content(100000):
# 			dbFile.write(chunk)

# 	dbFile.close()

# 	displayResult()
# except Exception as exc:
# 	print('Error: %s' % (exc))