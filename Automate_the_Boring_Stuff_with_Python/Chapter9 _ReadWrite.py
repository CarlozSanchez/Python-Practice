from pathlib import Path
import os

#Creates a file path using file name, directoy and Home 
fileName = 'MyFile.txt'
fileDirectory = 'Files/Programming/Python'\
	+ '/Automate the Boring Stuff with Python'
filePath = Path.home() / fileDirectory/ fileName;

#Open file with writing privliges
file = open(filePath, 'w')

#write to file
file.write("This work?")

#close the file
file.close()

print('Process Complete')
