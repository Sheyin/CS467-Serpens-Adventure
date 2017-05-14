# This will parse a string input from the command line and call a corresponding function.
# Also has some random bits as I try to figure out how to use Python.

import items
import commands
import utils

# Prints out the available actions for a specified feature
# This will probably be integrated into the engine or something
def getActions(feature, featureDict):
	actions = featureDict[feature]
	actionsList = actions.split(", ")
	return actionsList

# Check if the command was one specific to operating upon a feature (listed in json)
def checkFeatureActions(input, pos, feature, featureDict):		
	actionsList = getActions(feature, featureDict)

	# Check list of specified actions for a given feature
	for verb in actionsList:
		if verb in input:
			key = "feat" + str(pos) + "_do"
			return utils.engine_codes_dict[key]


# This receives input from engine/engineTest, validates and returns an engine code
def getInput(input, currentRoom):
	command = commands.identify(input)

	# Room-specific list of features as keys and recognized actions as entries
	featureDict = utils.getFeaturesDict(currentRoom)
	features = featureDict.keys()

	# Hard coded list of legal items (for now)
	listOfItems = ['board', 'keys', 'handle', 'skeleton key']

	if command and command.isdigit():
		return command

	elif command in ['exit', 'inventory', 'save', 'load']:
		return utils.engine_codes_dict[command]

	elif command == "go":
		# This will identify a direction or a feature, if found
		# Currently redundant because feature synonyms are included in directions list
		# location = items.findLocation(input, features)
		direction = utils.translateRoom(input, currentRoom)
		if (direction == -1):
			print "I can't go that way."
			return -1
		else:
			key = "go_" + str(direction)
			return utils.engine_codes_dict[key]

	elif command == "unknown":
		print "I don't understand that command."

	# This might actually be handled by the engine instead + can be 
	# combined with save/exit/inventory/quit
	elif command == "help":
		print "Possible items: " + str(listOfItems)
		print "Possible features and actions: " 
		for feature in features:
			print str(feature) + ": " + str(getActions(feature, featureDict))
		return utils.engine_codes_dict['help']

	elif command in ["take", "drop"]:
		item = items.identifyItem(input, listOfItems)
		if item:
			if command == "take":
				key = item + "_take"
				return utils.engine_codes_dict[key]
			if command == "drop":
				key = item + "_drop"
				return utils.engine_codes_dict[key]
		else:
			print "I can't do that."

	elif command == "look at":
		item = items.identifyItem(input, listOfItems)
		if item:
			key = item + "_look"
			return utils.engine_codes_dict[key]
		else:
			feature = items.findLocation(input, features)
			if feature:
				pos = features.index(feature) + 1
				key = "feat" + str(pos) + "_look"
				return utils.engine_codes_dict[key]
			else:
				print "I can't do that."

	else:
		feature = items.identifyFeature(input, features)
		item = items.identifyItem(input, listOfItems)

		# Check if the command was one specific to operating upon a feature (listed in json)
		if feature and not item:
			pos = features.index(feature) + 1
			commandUsedSpecified = checkFeatureActions(input, pos, feature, featureDict)
			if commandUsedSpecified:
				return commandUsedSpecified
			# Some recognized command like move, hit, etc. on a feature but not added to json
			elif command: 
				print "I'm not sure if I can " + command + " the " + feature + "."

		# Item and feature both mentioned in same sentence.
		# This might let just about anything through in its current state
		elif item and feature:
			# Hard coded until we get this logic figured out in a more standardized way
			if item == 'keys' and feature == 'door':
				return "10"

			# _hopefully_ the player used the correct item and feature and some meaningful word
			pos = features.index(feature) + 1
			key = "feat" + str(pos) + "_do"
			return utils.engine_codes_dict[key]

		# Item but no feature
		elif item and not feature:
			# Hard coded until we get this logic figured out in a more standardized way
			# listOfItems = ['board', 'keys', 'handle', 'skeleton key']
			if command == 'use' and item == 'board':
				removedItem1 = input.replace(item, ' ')
				item2 = items.identifyItem(input, listOfItems)
				if item == 'board' and item2 == 'keys':
					return "7"

			print "I'm not sure how use the " + item + " that way."

		# No item or feature, unrecognized command
		else: 
			print "I don't understand that command"



# Update to run main function for parseCommands.py separately from main.py
if __name__ == "__main__":
	print 'Starting the script.'
	keepLooping = True
	while (keepLooping != "exit"):
		userInput = raw_input (": ")
		keepLooping = getInput(userInput, 3)
		print "Code received: " + str(keepLooping)

