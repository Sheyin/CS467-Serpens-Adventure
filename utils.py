import re

# These should probably receive a filename or room name as input
# then buffer = parameter name (file/room name)
def getFeaturesList():
	file = open('data/rooms/room3.json')
	featuresList = []

	for line in file:
		line = line.rstrip()
		results = re.findall('"feat\d*": ("\D*")', line)
		for i in range (0, len(results)):
			if results[i].startswith('"') and results[i].endswith('"'):
				results[i] = results[i][1:-1]
				featuresList.append([results[i]])
	file.close()
	return featuresList


def getDescriptionsList():
	file = open('data/rooms/room3.json')
	descriptionsList = []

	for line in file:
		line = line.rstrip()
		results = re.findall('"feat\d*desc": ("\D*")', line)
		for i in range (0, len(results)):
			if results[i].startswith('"') and results[i].endswith('"'):
				results[i] = results[i][1:-1]
				descriptionsList.append([results[i]])
	file.close()
	return descriptionsList

# Reference: Python for Informatics (http://www.py4inf.com/)
# http://stackoverflow.com/questions/3085382/python-how-can-i-strip-first-and-last-double-quotes

# Below is just for my testing purposes
if __name__ == "__main__":
	featuresList = getFeaturesList();
	descriptionsList = getDescriptionsList();
	print "features: " + str(featuresList)
	print "descriptions: " + str(descriptionsList)