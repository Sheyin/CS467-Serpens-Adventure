import re

# These should probably receive a filename or room name as input
# then buffer = parameter name (file/room name)
def getFeaturesList(currentRoom):
	#currentRoom = 3
	filename = 'data/rooms/room' + str(currentRoom) + '.json'
	file = open(filename)
	featuresList = []

	for line in file:
		line = line.rstrip()
		results = re.findall('"feat\d*": ("\D*"),', line)
		#results = re.findall('"feat\d*": *', line)
		
		for i in range (0, len(results)):
			# This will strip opening and closing parenthesis
			if results[i].startswith('"') and results[i].endswith('"'):
				results[i] = results[i][1:-1]
				featuresList.append(results[i])
	file.close()
	return featuresList


def getDescriptionsList(currentRoom):
	filename = 'data/rooms/room' + str(currentRoom) + '.json'
	file = open(filename)
	descriptionsList = []

	for line in file:
		line = line.rstrip()
		results = re.findall('"feat\d*desc": ("\D*")', line)
		for i in range (0, len(results)):
			if results[i].startswith('"') and results[i].endswith('"'):
				results[i] = results[i][1:-1]
				descriptionsList.append(results[i])
	file.close()
	return descriptionsList

# Tries to translate input into a legal movement (direction)
# Returns a cardinal direction
def translateRoom(input, currentRoom):
	directions = {0: "north", 1: "south", 2: "west", 3: "east", 4: "up", 5: "down"}
	# pull list of connected rooms
	connectedList = getRoomInfo(currentRoom)

	# Search each tuple to see if the input word is valid 
	for dirPos in range (0, len(connectedList)):
		for namePos in range (0, len(connectedList[dirPos])):
			if (input == connectedList[dirPos][namePos]):
				return connectedList[dirPos][0]
	# Unable to match destination with a room
	return -1


# Given a room number, returns an ordered list of connections
# Should be pulled from json files eventually, this is a temporary measure to make the rest work
# 0: north, 1: south, 2: west, 3: east, 4: up, 5: down
# 1: Brig, 2: Storage, 3: Lower Hallway, 4: Observation, 5: Examination
def getRoomInfo(currentRoom):
	# Hard-coded stuff.  Hopefully I got the directions right.
	roomConnections1 = [('north', 'hallway', 'door', 'out'), ('south',), ('west',), ('east',), ('up', 'upstairs'), ('down', 'downstairs')]
	roomConnections2 = [('north',), ('south',), ('west',), ('east', 'hallway'), ('up', 'upstairs'), ('down', 'downstairs')]
	roomConnections3 = [('north', 'examination'), ('south', 'brig'), ('west', 'storage'), ('east', 'hallway', 'observation'), ('up', 'ladder', 'deck', 'upstairs'), ('down', 'downstairs')]
	roomConnections4 = [('north',), ('south',), ('west', 'hallway'), ('east',), ('up', 'upstairs'), ('down', 'downstairs')]
	roomConnections5 = [('north',), ('south', 'hallway'), ('west',), ('east',), ('up', 'upstairs'), ('down', 'downstairs')]
	allRooms = [roomConnections1, roomConnections2, roomConnections3, roomConnections4, roomConnections5]
	return allRooms[currentRoom + 1]


# Reference: Python for Informatics (http://www.py4inf.com/)
# http://stackoverflow.com/questions/3085382/python-how-can-i-strip-first-and-last-double-quotes

# Below is just for my testing purposes
if __name__ == "__main__":
	featuresList = getFeaturesList();
	descriptionsList = getDescriptionsList();
	print "features: " + str(featuresList)
	print "descriptions: " + str(descriptionsList)