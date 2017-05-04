import re

# This should probably receive a filename or room name as input
# then buffer = parameter name (file/room name)
def getItemList():
	buffer = open('data/rooms/room3.json')

	for line in buffer:
		line = line.rstrip()
		listOfFeatures = re.findall('"feat\d*": ("[a-z A-Z]*")', line)
		for i in range (0, len(listOfFeatures)):
			if listOfFeatures[i].startswith('"') and listOfFeatures[i].endswith('"'):
				listOfFeatures[i] = listOfFeatures[i][1:-1]
				print listOfFeatures[i]

# Reference: Python for Informatics (http://www.py4inf.com/)
# http://stackoverflow.com/questions/3085382/python-how-can-i-strip-first-and-last-double-quotes

getItemList();