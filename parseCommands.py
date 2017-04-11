# This will parse a string input from the command line.
# Also has some random bits as I try to figure out how to use Python.


# if it's a known command, return true, otherwise false
#def isCommand(command):
	# loop through array of reserved words, etc
# booleans are capitalized in Python
#	return True 

# This returns a string for what "category" the input belongs to
# Need a better way to organize this.  Multiple arrays / dictionary? Needs research.
def checkCategory(command):
	if ((command == "savegame") or (command == "save")):
		return "savegame"
	elif ((command == "loadgame") or (command == "load")):
		return "loadgame"
	elif ((command == "inventory") or (command == "bag")):
		return "inventory"
	elif ((command == "look") or (command == "explore")):
		return "look"
	elif ((command == "look_at") or (command == "examine")):
		return "look_at"
	elif ((command == "go") or (command == "move_to")):
		return "go"
	elif ((command == "take") or (command == "pick_up")):
		return "take"
	elif (command == "help"):
		return "help"
	elif ((command == "drop") or (command == "remove")):
		return "drop"
	else:
		return "unknown"

# This assumes the first word is a command
def checkCommand(command):
	# checking if command is one of the expected words
	# "if not" checks for truth, "!=" checks for equality
	#if not isCommand(command):
	#	print 'Unknown command.'
	#	return
	#else: 

	# No switches in python - implement dictionary method?
	# Need to add an additional function to sort input into a category
	category = checkCategory(command)

	if (category == "savegame"):
		print 'Game has been saved.  Well, no not really.'
	elif (category == "loadgame"):
		print 'Game has been loaded.  Fictionally.'
	elif (category == "inventory"):
		inventory = ['socks', 'banana', 'rubber ducky']
		print 'This is your inventory: ' + ', '.join(inventory)
	elif (category == "look"):
		print 'This is the long description of the room.  It is very detailed and fascinating.'
	elif (category == "look_at"):
		print 'This is a really interesting description of an item.  Support this with no underscore.'
	elif (category == "go"):
		print 'Go... where?'
	elif (category == "take"):
		print 'You picked up the item, whatever it is, and added it to your inventory.'
	elif (category == "help"):
		possibleActions = ['explore', 'fly', 'touch', 'dance']
		print 'This is a list of things you can do in the room: ' + ', '.join(possibleActions)
	elif (category == "drop"):
		print 'You dropped the object on the floor.'
	else:
		print 'Unrecognized command, or something broke.'
	return

# This goes through the items in the list and identifies which word references the item.
def itemPositionInSetence(wordArray, listofItems):
	# loop through list of items and see if one matches
	return 2

#wordArray = ['look', 'at', 'object']

# Putting this into a function to mimic what probably happens in overall program.
def getInput():
	print 'Starting the script!'
	lineInput = raw_input('Your action: ')
	# Split sentence into its component words
	wordArray = lineInput.split(" ")
	command = wordArray[0]
	# Probably need to insert a check if a valid object is specified, or how to handle missing prepositions
	# For that matter, determine where the item is going to be in a sentence (wordArray[1] or wordArray[2])
	# maybe keep a list of items in the room, loop and check each word, then return a contextual response?
	listofItems = ['key', 'door', 'houseplant']
	positionOfItem = itemPositionInSetence(wordArray, listofItems)
	print 'Item is located in position: ' + str(positionOfItem)
	# checkIfValidItem()
	checkCommand(lineInput)
	return

# "main" function
getInput()
