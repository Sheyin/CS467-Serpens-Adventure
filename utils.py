import re

# These are misc. functions that are parsing-related
# Producing a feature list / dictionary, room connection list, anything hard coded

# Probably better to centralize this so we aren't maintaining multiple code lists.
engine_codes_dict = {
	# Items
	'board_look': "5", 'board_take': "12", 'board_drop': "14", 
	'keys_look': "8", 'keys_take': "13", 'keys_drop': "15",
	'handle_look': "32", 'handle_take': "28", 'handle_drop': "29",
	'skeleton key_look': "33", 'skeleton key_take': "30", 'skeleton key_drop': "31",
	# Features
	'feat1_look': "1", 'feat1_do': "2",	'feat2_look': "3", 'feat2_do': "4",
	'feat3_look': "6", 'feat3_do': "7",	'feat4_look': "9", 'feat4_do': "10",
	'feat5_look': "18", 'feat5_do': "19", 'feat6_look': "20", 'feat6_do': "21",
	# Movement
	'go_north': "22", 'go_south': "23", 'go_west': "24", 'go_east': "25",
	'go_up': "26", 'go_down': "27",
	# Other
	'inventory': "17", 'look_room': "11", 'help': "16",
	'save': 'save', 'load': 'load', 'exit': 'exit', 'look_room': '11'
}


# Python-3-safe way of getting list of keys: k = list(b.keys())
# Python-2 way of getting list of keys: k = b.keys()
def getFeaturesDict(currentRoom):
	filename = 'data/rooms/room' + str(currentRoom) + '.json'
	file = open(filename)
	featuresList = []
	featuresDict = {}
	actionsList = []

	for line in file:
		line = line.rstrip()
		results = re.findall('"feat\d*": ("\D*"),', line)
		actions = re.findall('"feat\d*interactOptions": ("\D*"),', line)
		
		if (results != ""):
			for i in range (0, len(results)):
				# This will strip opening and closing parenthesis
				if results[i].startswith('"') and results[i].endswith('"'):
					results[i] = results[i][1:-1]
					featuresList.append(results[i])

		if (actions != ""):
			for j in range (0, len(actions)):
				# This will strip opening and closing parenthesis
				if actions[j].startswith('"') and actions[j].endswith('"'):
					actions[j] = actions[j][1:-1]
					actionsList.append((actions[j]))
					
	file.close()

	# Concatenate into a dictionary
	for itemPos in range (0, len(featuresList)):
		featuresDict[featuresList[itemPos]] =  actionsList[itemPos]

	return (featuresList, featuresDict)

# When supplied a room number, it picks out the appropriate connections
# and returns it in a list.  Ordering is significant.
# 0: north, 1: south, 2: west, 3: east, 4: up, 5: down
def getRoomConnections(currentRoom):
	filename = 'data/rooms/room' + str(currentRoom) + '.json'
	file = open(filename)
	connectionsList = []

	# This appends the room number to the list, but we need to translate
	# each room number into it's common name(s).  Also case sensitivity.

	for line in file:
		line = line.rstrip()
		results = re.findall('"north": (\d*)', line)
		for i in range (0, len(results)):
			if results[i].startswith('"') and results[i].endswith('"'):
				results[i] = results[i][1:-1]
			connectionsList.append(('north', results[0]))
		results = re.findall('"south": (\d*)', line)
		for i in range (0, len(results)):
			if results[i].startswith('"') and results[i].endswith('"'):
				results[i] = results[i][1:-1]
			connectionsList.append(('south', results[0]))
		results = re.findall('"west": (\d*)', line)
		for i in range (0, len(results)):
			if results[i].startswith('"') and results[i].endswith('"'):
				results[i] = results[i][1:-1]
			connectionsList.append(('west', results[0]))
		results = re.findall('"east": (\d*)', line)	
		for i in range (0, len(results)):
			if results[i].startswith('"') and results[i].endswith('"'):
				results[i] = results[i][1:-1]
			connectionsList.append(('east', results[0]))
		results = re.findall('"up": (\d*)', line)
		for i in range (0, len(results)):
			if results[i].startswith('"') and results[i].endswith('"'):
				results[i] = results[i][1:-1]
			connectionsList.append(('up', 'upstairs', results[0]))
		results = re.findall('"down": (\d*)', line)
		for i in range (0, len(results)):
			if results[i].startswith('"') and results[i].endswith('"'):
				results[i] = results[i][1:-1]
			connectionsList.append(('down', 'downstairs', results[0]))

	file.close()
	return connectionsList


# Tries to translate input into a legal movement (direction)
# Returns a cardinal direction
def translateRoom(input, currentRoom):
	# pull list of connected rooms
	connectedList = getRoomInfo(currentRoom)

	# Search each tuple to see if the input word matches some direction
	for dirPos in range (0, len(connectedList)):
		for namePos in range (0, len(connectedList[dirPos])):
			if connectedList[dirPos][namePos] in input:
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
	roomConnections2 = [('north',), ('south',), ('west',), ('east', 'hallway', 'door'), ('up', 'upstairs'), ('down', 'downstairs')]
	roomConnections3 = [('north', 'examination', 'entryway'), ('south', 'brig', 'barred door'), ('west', 'storage', 'wooden door'), ('east', 'observation', 'metal door'), ('up', 'ladder', 'trap door', 'upstairs'), ('down', 'downstairs')]
	roomConnections4 = [('north',), ('south',), ('west', 'hallway', 'door'), ('east',), ('up', 'upstairs'), ('down', 'downstairs')]
	roomConnections5 = [('north',), ('south', 'hallway', 'entryway'), ('west',), ('east',), ('up', 'upstairs'), ('down', 'downstairs')]
	allRooms = [roomConnections1, roomConnections2, roomConnections3, roomConnections4, roomConnections5]
	return allRooms[currentRoom - 1]


# This changes room numbers to room names / other recognizable forms.
# Might need to incorporate feature list as well to get doors, ladders, etc.
# The int is needed to make it interact with rooms properly.
def changeRoomNumbers(roomConnections, rooms):
	connectionsList = []
	if roomConnections[0].isdigit():
		roomNumber = int(roomConnections[0])
		roomName = str(rooms[roomNumber].name.lower())
		connectionsList.append(('north', roomName))
	elif not roomConnections[0]:
		connectionsList.append(('north'))

	if roomConnections[1].isdigit():
		roomNumber = int(roomConnections[1])
		roomName = str(rooms[roomNumber].name.lower())
		connectionsList.append(('south', roomName))
	elif not roomConnections[1]:
		connectionsList.append(('south'))

	if roomConnections[2].isdigit():
		roomNumber = int(roomConnections[2])
		roomName = str(rooms[roomNumber].name.lower())
		connectionsList.append(('west', roomName))
	elif not roomConnections[2]:
		connectionsList.append(('west'))

	if roomConnections[3] and roomConnections[3].isdigit():
		roomNumber = int(roomConnections[3])
		roomName = str(rooms[roomNumber].name.lower())
		connectionsList.append(('east', roomName))
	elif not roomConnections[3]:
		connectionsList.append(('east'))

	if roomConnections[4] and roomConnections[4].isdigit():
		roomNumber = int(roomConnections[4])
		roomName = str(rooms[roomNumber].name.lower())
		connectionsList.append(('up', 'upstairs', roomName))
	elif not roomConnections[4]:
		connectionsList.append(('up', 'upstairs'))

	if roomConnections[5] and roomConnections[5].isdigit():
		roomNumber = int(roomConnections[5])
		roomName = str(rooms[roomNumber].name.lower())
		connectionsList.append(('down', 'downstairs', roomName))
	elif not roomConnections[5]:
		connectionsList.append(('down', 'downstairs'))

	return connectionsList


# Packages variables together in expected formats for parse.main() or maybe "help"
# Produce list (features), dict (features), list (items), list of tuples (room Connections)
# The str() is required to change the data from unicode and remove the u' marks
def formatRoomData(rooms, objects, currentRoom):
	featuresList = []
	featuresDict = {}
	itemList = []
	#roomList = []
	featuresNeeded = ['feat1', 'feat2', 'feat3', 'feat4', 'feat5', 'feat6']
	featInteractionsNeeded = ['feat1interactOptions', 'feat2interactOptions', 'feat3interactOptions', 'feat4interactOptions', 'feat5interactOptions', 'feat6interactOptions']

	room = rooms[currentRoom]
	tempfeaturesList = [room.feat1, room.feat2, room.feat3, room.feat4, room.feat5, room.feat6]

	# Strip unicode markings
	for _ in range(0, len(tempfeaturesList)):
		tempfeaturesList[_] = str(tempfeaturesList[_])

	# Save features to dictionary using the feature itself as a key
	featuresDict[tempfeaturesList[0]] = str(room.feat1interactOptions)
	featuresDict[tempfeaturesList[1]] = str(room.feat2interactOptions)
	featuresDict[tempfeaturesList[2]] = str(room.feat3interactOptions)
	featuresDict[tempfeaturesList[3]] = str(room.feat4interactOptions)
	featuresDict[tempfeaturesList[4]] = str(room.feat5interactOptions)
	featuresDict[tempfeaturesList[5]] = str(room.feat6interactOptions)

	# Remove the 'feature - NA' lines, if present, from features and dictionary
	for word in tempfeaturesList:
		if ' - NA' not in word:
			featuresList.append(word)

	for key in list(featuresDict):
		if ' - NA' in key:
			featuresDict.pop(key)

	# This should be limited based on info from the gamestate (item location)
	# Currently it just takes all the possible items (but will be shown to user if they use help)
	itemDict = {}
	itemSynonyms = []
	itemList = objects.keys()
	for item in itemList:
		itemSynonyms = objects[item].synonyms
		synonymList = []
		for object in itemSynonyms:
			synonymList.append(str(object))
		itemDict[str(item)] = synonymList

	# Strip unicode markings
	for _ in range(0, len(itemList)):
		itemList[_] = str(itemList[_])

	roomList = [str(room.north), str(room.south), str(room.east), str(room.west), str(room.up), str(room.down)]

	roomConnections = changeRoomNumbers(roomList, rooms)

	return featuresList, featuresDict, itemDict, roomConnections

	# How to get object variables / information
	#roomkeys = room.__dict__.keys()
	#roomdict = room.__dict__

# Reference: Python for Informatics (http://www.py4inf.com/)
# http://stackoverflow.com/questions/3085382/python-how-can-i-strip-first-and-last-double-quotes
# http://stackoverflow.com/questions/8953627/python-dictionary-keys-error
# http://stackoverflow.com/questions/1767513/read-first-n-lines-of-a-file-in-python

# Below is just for my testing purposes
#if __name__ == "__main__":