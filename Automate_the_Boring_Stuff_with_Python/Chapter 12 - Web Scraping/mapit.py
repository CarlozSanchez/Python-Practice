#! python3
# mapIt.py - Launches a map in the browser using an aaddress 
# from the command line or clipboard.

import webbrowser, sys, pyperclip

if (len(sys.argv) > 1):
	#Get address from command line.
	address = ' '.join(sys.argv[1:])

	print("the address is " + address)

else:
	#Get address from clipboard.
	address = pyperclip.paste()


webbrowser.open('https://www.google.com/maps/place/' + address)