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
def main(input, currentRoom):
	command = commands.identify(input)

	# Room-specific list of features as keys and recognized actions as entries
	features, featureDict = utils.getFeaturesDict(currentRoom)

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
		if feature:
			pos = features.index(feature) + 1
			commandUsedSpecified = checkFeatureActions(input, pos, feature, featureDict)

			# Some item and feature both mentioned in same sentence with a legal action.
			if item == 'board' and feature in ['window', 'locker'] and (command in ['move', 'use'] or commandUsedSpecified):
				key = "feat" + str(pos) + "_do"
				return utils.engine_codes_dict[key]

			elif item == 'keys' and feature in ['door', 'chest'] and (command in ['use'] or commandUsedSpecified):
				key = "feat" + str(pos) + "_do"
				return utils.engine_codes_dict[key]

			elif item == 'handle' and feature in ['metal door'] and (command in ['use'] or commandUsedSpecified):
				key = "feat" + str(pos) + "_do"
				return utils.engine_codes_dict[key]

			elif item == 'skeleton key' and feature in ['trap door', 'trapdoor'] and (command in ['use'] or commandUsedSpecified):
				key = "feat" + str(pos) + "_do"
				return utils.engine_codes_dict[key]

			# Unrecognized combination of item, feature, command
			elif command and item:
				print "I'm not sure if I can " + command + " the " + item + " on the " + feature + "."

			# Feature mentioned, no item; no legal action from json
			else:
				# This just lets any specified action on a feature through - maybe too vague?
				if commandUsedSpecified:
					return commandUsedSpecified
				if command:
					print "I'm not sure if I can " + command + " the " + feature + "."
				else:
					print "I don't think I can do that."
				

		# Item but no feature
		elif item and not feature:
			# Hard coded until we get this logic figured out in a more standardized way
			# listOfItems = ['board', 'keys', 'handle', 'skeleton key']
			if item == 'board' and command in ['pull']:
				# This allows the "pull board" command
				return "4"
			elif item == 'board' and command in ['use', 'move']:
				removedItem1 = input.replace(item, ' ')
				item2 = items.identifyItem(removedItem1, listOfItems)
				if item2 == 'keys':
					return "7"
			elif item == 'keys' and (command in ['use'] or commandUsedSpecified):
				if 'lock' in input:
					return "10"

			print "I'm not sure how use the " + item + " that way."

		# No item or feature, unrecognized command
		else: 
			print "I don't understand that command."



# Update to run main function for parseCommands.py separately from main.py
if __name__ == "__main__":
	print 'Starting the script.'
	keepLooping = True
	while (keepLooping != "exit"):
		userInput = raw_input (": ")
		keepLooping = main(userInput, 1)
		print "Code received: " + str(keepLooping)

