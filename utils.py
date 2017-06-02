import re
import data
from data import *
import textwrap
from items import itemKeysDict

# These are misc. functions that are parsing-related
# Producing a feature list / dictionary, room connection list, anything hard coded

# Probably better to centralize this so we aren't maintaining multiple code lists.
engine_codes_dict = {
	# Deck 1 Items
	'board_look': "5", 'board_take': "12", 'board_drop': "14", 
	'keys_look': "8", 'keys_take': "13", 'keys_drop': "15",
	'handle_look': "32", 'handle_take': "28", 'handle_drop': "29",
	'skeleton key_look': "33", 'skeleton key_take': "30", 'skeleton key_drop': "31",
	# Deck 2 Items
	'small key_look': "34", 'small key_take': "35", 'small key_drop': "36",
	'gun_look': "37", 'gun_take': "38", 'gun_drop': "39",
	# Deck 3 Items - guesses
	'paperclip_look': "40", 'paperclip_take': "41", 'paperclip_drop': "42",
	'lockpick_look':"43", 'lockpick_take': "44", 'lockpick_drop': "45",
	'keycard_look': "46", 'keycard_take':"45", 'keycard_drop': "46",
	'cryptex_look': "47", 'cryptex_take': "48", 'cryptex_drop': "49", 
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

# Produces formatted text and displays on console.  Input is a string, no return.
def display(text):
   textToPrint = textwrap.wrap(text, 70)
   for line in textToPrint:
      print '  ' + line


# Prints the help information from features + items
def printHelp(featureDict, itemDict):
	display("HELPFUL TIPS:")
	display("Take a closer look at the room's features.  Sometimes you may need to examine a detail on a feature even more closely.")
	display("Don't forget to take (pick up) items after you've revealed them.")
	print ""
	display("Features and Actions:")
	features = featureDict.keys()
	for feature in features:
		actionsForFeature = featureDict[feature]
		actionList = actionsForFeature.split(", ")
		actions = ""
		for _ in actionList:
			if _ == actionList[0]:
				actions = _
			else:
				actions = actions + ", " + _
		display(str(feature) + ": " + actions)
	itemKeys = itemDict.keys()
	itemList = ""
	for _ in itemKeys:
		if _ == itemKeys[0]:
			itemList = _
		else:
			itemList = itemList + ", " + _
	print ""
	display("Items: ")
	display(itemList)


# Tries to translate input into a legal movement (direction)
# Returns a cardinal direction
def translateRoom(input, rooms):
	# Search each tuple to see if the input word matches some direction
	for dirPos in range (0, len(rooms)):
		for namePos in range (0, len(rooms[dirPos])):
			if rooms[dirPos][namePos] in input:
				return rooms[dirPos][0]

	# Unable to match destination with a room
	# Check if the word 'door' is present and only one connection in the room
	numSingleConnections = 0
	for connection in rooms:
		if len(connection) == 1:
			numSingleConnections += 1
	if numSingleConnections == 3:
		for word in ['door', 'outside', 'head out', 'leave room', 'out']:
			if word in input:
				# This casual term matches and there is only one exit anyways
				# find out which connection it was - probably of the first 4
				for i in range (0, 4):
					if len(rooms[i]) > 1:
						return rooms[i][0]
	return -1


# This changes room numbers to room names / other recognizable forms.
# Might need to incorporate feature list as well to get doors, ladders, etc.
# The int() is needed to make it interact with rooms properly.
# Assumption that 'synonyms' will be the member name of room aliases
def changeRoomNumbers(roomConnections, rooms):
	connectionsList = []
	roomAliases = {}

	if roomConnections[0].isdigit():
		roomNumber = int(roomConnections[0])
		roomName = str(rooms[roomNumber].name.lower())
		aliases = rooms[roomNumber].aliases
		aliases = stripUnicode(aliases)
		roomAliasList = ['north', roomName]
		for alias in aliases:
			roomAliasList.append(alias)
		aliasTuple = tuple(roomAliasList)
		connectionsList.append(aliasTuple)
	elif not roomConnections[0]:
		connectionsList.append(('north',))

	if roomConnections[1].isdigit():
		roomNumber = int(roomConnections[1])
		roomName = str(rooms[roomNumber].name.lower())
		aliases = rooms[roomNumber].aliases
		aliases = stripUnicode(aliases)
		roomAliasList = ['south', roomName]
		for alias in aliases:
			roomAliasList.append(alias)
		aliasTuple = tuple(roomAliasList)
		connectionsList.append(aliasTuple)
	elif not roomConnections[1]:
		connectionsList.append(('south',))

	if roomConnections[2].isdigit():
		roomNumber = int(roomConnections[2])
		roomName = str(rooms[roomNumber].name.lower())
		aliases = rooms[roomNumber].aliases
		aliases = stripUnicode(aliases)
		roomAliasList = ['east', roomName]
		for alias in aliases:
			roomAliasList.append(alias)
		aliasTuple = tuple(roomAliasList)
		connectionsList.append(aliasTuple)
	elif not roomConnections[2]:
		connectionsList.append(('east',))

	if roomConnections[3].isdigit():
		roomNumber = int(roomConnections[3])
		roomName = str(rooms[roomNumber].name.lower())
		aliases = rooms[roomNumber].aliases
		aliases = stripUnicode(aliases)
		roomAliasList = ['west', roomName]
		for alias in aliases:
			roomAliasList.append(alias)
		aliasTuple = tuple(roomAliasList)
		connectionsList.append(aliasTuple)
	elif not roomConnections[3]:
		connectionsList.append(('west',))

	if roomConnections[4].isdigit():
		roomNumber = int(roomConnections[4])
		roomName = str(rooms[roomNumber].name.lower())
		aliases = rooms[roomNumber].aliases
		aliases = stripUnicode(aliases)
		roomAliasList = ['up', 'upstairs', roomName]
		for alias in aliases:
			roomAliasList.append(alias)
		aliasTuple = tuple(roomAliasList)
		connectionsList.append(aliasTuple)
	elif not roomConnections[4]:
		connectionsList.append(('up', 'upstairs'))

	if roomConnections[5].isdigit():
		roomNumber = int(roomConnections[5])
		roomName = str(rooms[roomNumber].name.lower())
		aliases = rooms[roomNumber].aliases
		aliases = stripUnicode(aliases)
		roomAliasList = ['down', 'downstairs', roomName]
		for alias in aliases:
			roomAliasList.append(alias)
		aliasTuple = tuple(roomAliasList)
		connectionsList.append(aliasTuple)
	elif not roomConnections[5]:
		connectionsList.append(('down', 'downstairs'))

	return connectionsList


# Strips unicode from data; returns clean version
def stripUnicode(data):
	# List requires a double loop
	if type(data) is list:
		for _ in range(0, len(data)):
			data[_] = str(data[_])
		return data

	# Single str() required
	else:
		return str(data)


# Packages variables together in expected formats for parse.main() or maybe "help"
# Produce list (features), dict (features), list (items), list of tuples (room Connections)
# The str() is required to change the data from unicode and remove the u' marks
def formatRoomData(rooms, objects, currentState):
	currentRoom = int(currentState.currRoom)

	featuresList = []
	featuresDict = {}
	itemList = []
	featuresNeeded = ['feat1', 'feat2', 'feat3', 'feat4', 'feat5', 'feat6']
	featInteractionsNeeded = ['feat1interactOptions', 'feat2interactOptions', 'feat3interactOptions', 'feat4interactOptions', 'feat5interactOptions', 'feat6interactOptions']

	room = rooms[currentRoom]
	tempFeaturesList = [room.feat1, room.feat2, room.feat3, room.feat4, room.feat5, room.feat6]

	# Strip unicode markings
	tempFeaturesList = stripUnicode(tempFeaturesList)

	# Save features to dictionary using the feature itself as a key
	featuresDict[tempFeaturesList[0]] = str(room.feat1interactOptions)
	featuresDict[tempFeaturesList[1]] = str(room.feat2interactOptions)
	featuresDict[tempFeaturesList[2]] = str(room.feat3interactOptions)
	featuresDict[tempFeaturesList[3]] = str(room.feat4interactOptions)
	featuresDict[tempFeaturesList[4]] = str(room.feat5interactOptions)
	featuresDict[tempFeaturesList[5]] = str(room.feat6interactOptions)

	# Remove the 'feature - NA' lines, if present, from features and dictionary
	for word in tempFeaturesList:
		if ' - NA' not in word:
			featuresList.append(word)

	for key in list(featuresDict):
		if ' - NA' in key:
			featuresDict.pop(key)

	# This should be limited based on info from the gamestate (item location)
	# Currently it just takes all the possible items (but will be shown to user if they use help)

	# Get only the items present in room (gamestate - flagged as 1)
	itemList = []
	# Check if these items are present
	for thing in itemKeysDict.keys():
		itemFlag = getattr(currentState, thing)
		if itemFlag:
			itemList.append(itemKeysDict[thing])

	itemDict = {}
	itemSynonyms = []

	for item in itemList:
		itemSynonyms = objects[item].synonyms
		synonymList = []
		for object in itemSynonyms:
			synonymList.append(str(object))
		itemDict[str(item)] = synonymList

	# Strip unicode markings
	itemList = stripUnicode(itemList)

	roomList = [str(room.north), str(room.south), str(room.east), str(room.west), str(room.up), str(room.down)]

	roomConnections = changeRoomNumbers(roomList, rooms)

	return featuresList, featuresDict, itemDict, roomConnections


# singleDoorCheck(): To facilitate "go door" when there is only one door in the room
# Putting it as an alias for another room can cause logical errors
def singleDoorCheck(roomConnections):
	return True


	# How to get object variables / information
	#roomkeys = room.__dict__.keys()
	#roomdict = room.__dict__

# Reference: Python for Informatics (http://www.py4inf.com/)
# http://stackoverflow.com/questions/3085382/python-how-can-i-strip-first-and-last-double-quotes
# http://stackoverflow.com/questions/8953627/python-dictionary-keys-error
# http://stackoverflow.com/questions/1767513/read-first-n-lines-of-a-file-in-python

# Below is just for my testing purposes
if __name__ == "__main__":
	data.load_objects()
	cryptex = objects['cryptex']
	print "Test 1:"
	print cryptex.name
	print stripUnicode(cryptex.name)

	print "Test 2:"
	print cryptex.synonyms
	print stripUnicode(cryptex.synonyms)