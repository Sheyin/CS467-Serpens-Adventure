# This will parse a string input from the command line and call a corresponding function.
# Also has some random bits as I try to figure out how to use Python.

import parseCategory
import parseItem
import parseArticles
import parsePreposition
import stubs
import utils

# Cheryl's To-do list:
# 1. Reorganize so some "main" function is sending a list of acceptable values instead of hard coding
# 2. Tidy up process so it isn't trying to parse things that won't be found (ex. single word input)
# 3. Consider renaming .py files to be more in line with rest of group - requires editing main.py
# 4. Consider if 'invalid' and 'none' can be standardized

# Returns the "category" of the verb if known, otherwise returns "unknown"
# Working off the assumption that the first word used is the command / verb.
def checkCommand(wordArray, featureDict):
	# Special handling for look vs look at since only command is sent
	if ((len(wordArray) > 1) and ((wordArray[0] == "look") and (wordArray[1] == "at"))):
		return "look_at"
	else:
		category = parseCategory.identify(wordArray[0])
	return category


# This executes the specified command by calling whichever functions
# The command and item should have been validated before calling this.
# _maybe_ can combine with findCategory() but would need to restructure
# TODO: Maybe separate out commands that don't require items early on
# 	ex. moving "save" and "load" to be handled and skip over item / prep process
#	The default arguments may or may not be required here.
# TODO: Note that single-item commands may need a different function than
# 	the double-item commands (take item != take item to the feature)
def executeCommand(wordArray, category, item1='none', item2='none', listOfItems=[], listOfFeatures=[], currentRoom=0):
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
		'inventory': "17", 'look_room': "11", 'help': "16"
	}
	# Features: Pull a list from text file or hard coded.
	# Go: Pull a list from text file or hard coded.

	if (category == "savegame"):
		return stubs.saveGame()
	elif (category == "loadgame"):
		return stubs.loadGame()
	elif (category == "inventory"):
		return engine_codes_dict['inventory']
		#return stubs.showInventory()
	elif (category == "look"):
		return engine_codes_dict['look_room']
		#return stubs.look(wordArray, item1)
	elif (category == "look_at"):
		if (item1 in listOfItems):
			key = item1 + "_look"
			return engine_codes_dict[key]
		elif (item1 in listOfFeatures):
			pos = listOfFeatures.index(item1) + 1
			key = "feat" + str(pos) + "_look"
			return engine_codes_dict[key]
		else:
			print "Look at what?"
			return -1	
		#return stubs.lookAt(item1)
	elif (category == "go"):
		direction = utils.translateRoom(item1, currentRoom)
		if (direction == -1):
			print "I can't go there."
			return -1
		else:
			key = "go_" + str(direction)
			return engine_codes_dict[key]
		#return stubs.goTo(item1)
	elif (category == "take"):
		if (item1 == "invalid"):
			print "Take what?"
			return -1
		elif (item1 in listOfFeatures):
			print "You can't take that."
			return -1
		else:
			key = item1 + "_take"
			return engine_codes_dict[key]
		#if (item2 != 'none'):
		#	return stubs.bring(item1, item2)
		#else:
		#	return stubs.take(item1)
	elif (category == "help"):
		print "Possible items: " + str(listOfItems)
		print "Possible features: " + str(listOfFeatures)
		return engine_codes_dict['help']
	elif (category == "drop"):
		if (item1 not in listOfItems):
			print "Drop what?"
			return -1
		else:
			key = item1 + "_drop"
			return engine_codes_dict[key]
		#return stubs.drop(item1)
	elif (category == "quit"):
		# Currently this is never reached because it is also handled in getInput() before it reaches here
		return stubs.quit()
	elif (category == "use"):
		return stubs.use(item1, item2)
	elif (category == "move"):
		# Adjust this later so that moving an object (that can be picked up) works like a take action instead
		return stubs.move(item1)
	elif (category == "hit"):
		return stubs.hit(item1)
	elif (category == "do"):
		# This is just a default category for when an explicitly approved word is used for this feature.
		# This is a stopgap measure for now.
		pos = listOfFeatures.index(item1) + 1
		key = "feat" + str(pos) + "_do"
		return engine_codes_dict[key]
	else:
		# Some custom handling here - ex. new actions? add more elifs?
		#print "You " + wordArray[0] + " the " + item1 + "."
		print "You can't do that right now."
	return "unknown"


# This receives input from engine/engineTest, validates and returns an engine code
def getInput(lineInput, currentRoom):
	item1 = 'none'
	item2 = 'none'

	# Stripping determiners/articles from sentence ('the', 'a', 'an')
	newString = parseArticles.removeArticles(lineInput)

	# Split sentence into its component words
	wordArray = newString.split(" ")
	command = wordArray[0]

	# This should be populated from a text file
	# Uncomment this when room files are populated
	testList = utils.getFeaturesList(currentRoom)
	print "Test list: " + str(testList)

	# Room-specific list of features as keys and recognized actions as entries
	featureDict = utils.getFeaturesList(currentRoom)
	listOfFeatures_dyn = featureDict.keys()
	print "Actions: " + str(listOfFeatures_dyn)

	# **** Hopefully all of this will change when we load from text files ****
	# Hard coded stuff for now
	listOfItems = ['board', 'keys', 'handle', 'skeleton key']

	# The following might not work correctly
	# 1: Brig, 2: Storage, 3: Lower Hallway, 4: Observation, 5: Examination
	listOfFeatures1 = ['straw', 'bench', 'window', 'door']
	listOfFeatures2 = ['locker', 'paper', 'door']
	listOfFeatures3 = ['entryway', 'barred door', 'metal door', 'wooden door', 'ladder', 'trap door']
	listOfFeatures4 = ['door', 'barred window' 'window', 'chest', 'bottles', 'papers']
	listOfFeatures5 = ['entryway', 'table', 'mirror']
	listOfFeatures_dict = {1: listOfFeatures1, 2: listOfFeatures2, 3: listOfFeatures3, 4: listOfFeatures4, 5: listOfFeatures5}
	# **** End hard coded stuff ****

	# Is this a valid command?
	category = checkCommand(wordArray, featureDict)

	if (category == "quit"):
		return "exit"

	elif (category == "unknown"):
		# This is to continue support of engine codes (numerical input)
		if lineInput.isdigit():
			return lineInput
		else:
			print "You want to " + command + " but you don't know how.  Try a different command."
	else: 
		# One-word command
		if (len(wordArray) == 1):
			# Maybe should add a check here to see if a single word input was allowed for that command
			# Instead of within the executeCommand() function
			return executeCommand(wordArray, category, "none", "none", listOfItems, listOfFeatures_dict[currentRoom], currentRoom)
		if (len(wordArray) == 2):
			if (command == "go"):
				return executeCommand(wordArray, category, wordArray[1], "none", listOfItems, listOfFeatures_dict[currentRoom], currentRoom)
			# Might need to rethink item logic + where this is being called. 
		item1 = parseItem.findItemUsed(wordArray, listOfItems, listOfFeatures_dict[currentRoom])
		# Temporary bypass.  Should reorganize since this is so messy.
		# Check if item is a feature, and if so, check if command matches a verb.  If so, category = "do"
		if (item1 in featureDict):
			actions = featureDict[item1]
			actionsList = actions.split(", ")
			for verb in actionsList:
				if (command == verb):
					category = "do"
					return executeCommand(wordArray, "do", wordArray[1], "none", listOfItems, listOfFeatures_dict[currentRoom], currentRoom)
		
		# Two-word command
		if (len(wordArray) > 2):
			# Create a second string / array to skip over first known item and find the second
			removedItem1 = newString.replace(item1, ' ')
			wordArray2 = removedItem1.split(' ')
			item2 = parseItem.findItemUsed(wordArray2, listOfItems, listOfFeatures_dict[currentRoom])
			#print "Item1: " + item1 + " Item 2: " + item2
			if (item2 != "invalid"):
				# not sure what to do with the preposition function yet, or if it even belongs here
				preposition = parsePreposition.identify(wordArray, item1, item2)
		return executeCommand(wordArray, category, item1, item2, listOfItems, listOfFeatures_dict[currentRoom], currentRoom)


'''
# Update to run main function for parseCommands.py separately from main.py
if __name__ == "__main__":
   print 'Starting the script.'
   keepLooping = True
	while (keepLooping):
		userInput = raw_input (": ")
		keepLooping = getInput(userInput)
'''
