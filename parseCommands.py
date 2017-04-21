# This will parse a string input from the command line.
# Also has some random bits as I try to figure out how to use Python.


# To-do list:
# 1. Reorganize so some "main" function is sending a list of acceptable values instead of hard coding
# 2. Cull some unused / experimental functions
# 3. Study how to put some of these extraneous functions into a different file


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
	elif ((command == "look_at") or (command == "examine") or (command == "view")):
		return "look_at"
	elif ((command == "go") or (command == "move_to")):
		return "go"
	elif ((command == "take") or (command == "pick_up")):
		return "take"
	elif (command == "help"):
		return "help"
	elif ((command == "drop") or (command == "remove")):
		return "drop"
	elif ((command == "quit") or (command == "exit")):
		return "quit"
	else:
		return "unknown"


# working off the assumption that the first word used is the command / verb.
# Returns the "category" of the verb if known, otherwise returns "unknown"
def checkCommand(wordArray):
	# Special handling for look vs look at since only command is sent
	# Maybe needs more refinement to make "look at door" and "look door" the same
	if ((len(wordArray) > 1) and ((wordArray[0] == "look") and (wordArray[1] == "at"))):
		category = checkCategory ("look_at")
	else:
		category = checkCategory(wordArray[0])

	# Unrecognized command - print an error message
	if (category == "unknown"):
		print "You want to " + wordArray[0] + " something, but you don't know how.  Try a different command."
	return category

# This identifies where in a sentence an item is located
# if it doesn't match any known items, then it will guess at words
# after particles (after "the", "a", ), then prepositions ("in", "on")
# Returns a negative value if the word was a guess, but positive
# if the item was confirmed (on the list of items in a room)
def itemPositionInSentence(wordArray, listOfItems):

	# Single word input, so there is no item:
	if (len(wordArray) == 1):
		return 0

	# Loop through and compare words with list of items in room:
	for wordPos in range (0, len(wordArray)):
		for itemPos in range (0, len(listOfItems)):
			if (wordArray[wordPos] == listOfItems[itemPos]):
				#print str(wordArray[wordPos]) + ' is equal to ' + str(listOfItems[itemPos])
				return wordPos

	# anything past this point is strictly optional - the item is not a known object in room

	# item name is not found - infer an answer based on particles
	particles = ['the', 'a']
	for wordPos in range (0, len(wordArray)):
		for articlePos in range (0, len(particles)):
			if (wordArray[wordPos] == particles[articlePos]):
				# turning this negative so we know it was not a recognized object
				return -wordPos

	# item name is still not found - assume it is right after the command 
	# command is assumed to be the first word in the sentence
	return -1


# Displays an error message for an invalid action
# TODO: randomize the error messages
def randomErrorMessage(wordArray, word):
	print "You try to " + wordArray[0] + " the " + word + " but you realize you don't have one."


# Identifies the verb and item, as well as location, for easier handling
def findItemUsed(wordArray, listOfItems):

	# The verb is _probably_ in the first word used, identify category (meaning/intent of the word)
	command = wordArray[0]
	category = checkCategory(command)

	# Identify the item and its position in the sentence
	positionOfItem = itemPositionInSentence(wordArray, listOfItems)
	#print "Debug: positionOfItem: " + str(positionOfItem)
	if (positionOfItem < 0):
		# Object was not found in room, so guessed at it for a response
		# displaying a message stating so
		word = wordArray[abs(positionOfItem)]
		randomErrorMessage(wordArray, word)
		return "invalid"
	else:
		word = wordArray[positionOfItem]
		return word

	# Prepositions are either between the command and item, or after the item
	#positionPreposition = findPreposition(wordArray, positionOfItem)


# This executes the specified command by calling whichever functions
# The command and item should have been validated before calling this
# _maybe_ can combine with findCategory() but would need to restructure
def executeCommand(wordArray, category, item):
	if (category == "savegame"):
		# saveGame()
		print "Game would be saved here."
	elif (category == "loadgame"):
		# loadGame()
		print "Game would be loaded here."
		# not sure how this should be handled - maybe destroy this instance? so return False?
	elif (category == "inventory"):
		# showInventory()
		print "This is your imaginary inventory!"
	elif (category == "look"):
		# look()
		print "You look around and see things.... (list objects / long description)"
	elif (category == "look_at"):
		# lookAt(item)
		# check if item is unspecified / undefined and give error message accordingly.
		# Maybe this should be handled in another function.
		if (wordArray[0] == item):
			print "Look at what?"
		else: 
			print "You look at the " + item + "."
	elif (category == "go"):
		# go(place)
		print "You go to the " + item + " (place?)."
	elif (category == "take"):
		# take()
		print "You take the " + item + "."
	elif (category == "help"):
		# help(room)
		print "These are the items in the room..."
	elif (category == "drop"):
		# drop(item)
		print "You drop the " + item + "."
	elif (category == "quit"):
		# quit()
		print "Exiting the game."
		return False
	else:
		# Some custom handling here - ex. individual actions? add more elifs?
		print "You " + wordArray[0] + " the " + item + "."
	return True


# Putting this into a function to mimic what probably happens in overall program.
def getInput():
	lineInput = raw_input('Your action: ')
	# Split sentence into its component words
	wordArray = lineInput.split(" ")
	command = wordArray[0]
	# Probably need to insert a check if a valid object is specified, or how to handle missing prepositions
	# For that matter, determine where the item is going to be in a sentence (wordArray[1] or wordArray[2])
	# maybe keep a list of items in the room, loop and check each word, then return a contextual response?
	listOfItems = ['key', 'door', 'plant', 'bird', 'plane', 'superman']

	# Check if the command used is known / valid
	category = checkCommand(wordArray)
	if (category == "unknown"):
		# an error should have already been displayed.  Begin loop again.
		print "Loop again and ask for input.  Invalid command."
	# This should probably be handled better, but in order to test this portion....
	elif (category == "quit"):
		return False
	else: 
		item = findItemUsed(wordArray, listOfItems)
		#print "Item found: " + item
		if (item == "invalid"):
			# begin loop again- error message should already have been displayed
			print "Loop again and ask for input.  Invalid item."
		else: 
			# At this point it should be a valid command and item
			# Call individual functions to handle command accordingly?
			executeCommand(wordArray, category, item)
	return True

# "main" function - temporary until we can coordinate as a group
keepLooping = True
print 'Starting the script!'
while (keepLooping):
	keepLooping = getInput()


