# This will parse a string input from the command line and call a corresponding function.
# Also has some random bits as I try to figure out how to use Python.

import items
import commands
import utils
import data
from data import *
from utils import display

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
# This expects: input(string), features(List), feature(Dict), items(Dict), rooms(List of tuples)
def main(rawinput, features, featureDict, itemDict, rooms):
	input = rawinput.lower()
	command = commands.identify(input)
	itemList = itemDict.keys()
	splitString = input.split()
	if splitString:
		rawCommand = splitString[0]
	else:
		rawCommand = "null"

	if rawCommand is "null":
		return "invalid"

	# For testing only - delete when numeric commands no longer supported
	elif (command and command.isdigit()):
		return command

	elif command in ['exit', 'inventory', 'savegame', 'loadgame', 'help']:
		# Temporary: for debugging - should be in engine
		return command

	elif command == "go":
		# This will identify a direction or a feature, if found
		# Currently redundant because feature synonyms are included in directions list
		# location = items.findLocation(input, features)
		direction = utils.translateRoom(input, rooms)
		if (direction == -1):
			display("I can't go that way.")
		else:
			key = "go_" + str(direction)
			return utils.engine_codes_dict[key]

	elif command in ["take", "drop"]:
		item = items.identifyItem(input, itemDict)
		'''
		if not item:
			for possibleItem in ['board', 'cryptex', 'gun', 'handle', 'keys', 'lockpick', 'skeleton key', 'smallKey', 'paper clip']:
				if possibleItem in input:
					item = possibleItem'''
		if item:
			if command == "take":
				key = item + "_take"
				return utils.engine_codes_dict[key]
			if command == "drop":
				key = item + "_drop"
				return utils.engine_codes_dict[key]
		else:
			# Not one of the items	
			display("I can't do that.")

	elif command == "look at":
		item = items.identifyItem(input, itemDict)
		if item:
			key = item + "_look"
			return utils.engine_codes_dict[key]
		else:
			feature = items.identifyFeature(input, features)
			if feature:
				pos = features.index(feature) + 1
				commandUsedSpecified = checkFeatureActions(input, pos, feature, featureDict)
				# This is an override if examine is used as an interaction rather than look
				if commandUsedSpecified:
					key = "feat" + str(pos) + "_do"
				else: 
					key = "feat" + str(pos) + "_look"
				return utils.engine_codes_dict[key]
			else:
				display("I can't do that.")

	# Strictly a for-fun command.  Not sure what parameters are really needed yet.
	elif command == "escape":
		commands.escape()

	# Had to remove "look" from commands.synonyms because it was causing problems - prioritization
	elif "look" in input:
		return utils.engine_codes_dict["look_room"]

	else:
		feature = items.identifyFeature(input, features)
		item = items.identifyItem(input, itemDict)

		# Check if the command was one specific to operating upon a feature (listed in json)
		if feature:
			pos = features.index(feature) + 1
			commandUsedSpecified = checkFeatureActions(input, pos, feature, featureDict)

			# Recognized command on a feature.  May want this to be highest priority.
			if commandUsedSpecified:
				return commandUsedSpecified

			# Some item and feature both mentioned in same sentence with a legal action.
			elif item == 'board' and feature in ['window', 'locker'] and (command in ['move', 'use'] or commandUsedSpecified):
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

			# Unrecognized combination of item, feature, command - not sure when this will be used
			elif command and feature and item:
				display("I'm not sure if I can " + command + " the " + item + " on the " + feature + ".")

			elif command == 'eat':
				commands.eat(rawCommand, feature)

			# Kicking a recognized feature
			elif command == 'hit':
				commands.kick(rawCommand, feature)

			elif command == 'move':
				commands.pull(rawCommand, feature, "feature")

			# Feature mentioned, no item; no legal action from json
			else:
				# This is for the go requirement - if you specify "metal door" only act as go
				direction = utils.translateRoom(input, rooms, "strict")
				# Not a valid room alias
				if (direction == -1):
					display("I don't think I can do that to the " + feature + ".")
				# Identical to "go"
				else:
					key = "go_" + str(direction)
					return utils.engine_codes_dict[key]

		# Item but no feature
		elif item and not feature:
			# Catch the silly commands first
			if command == "eat":
				commands.eat(rawCommand, item)
			elif command == "hit":
				commands.kick(rawCommand, item)
			elif command == "move":
				if "door" in input:
					display ("Open a door?  Which door?")
				else:
					commands.pull(rawCommand, item, "item")
			elif item == "board":
				# For "use board on keys"
				if "keys" in input and command in ['use', 'move']:
					return "7"

				# Default - "pull board"
				elif command in ['move', 'pull']:
					return "4"
				
				# Some default return
				else:
					display("What do you want to do with this " + item + "?")
					return "invalid"
			elif item == 'keys' and command in ['use']:
				# "Use board on keys" - shouldn't really be needed, just in case
				if "board" in input:
					return "7"
				# "Use keys on lock"
				if 'lock' in input:
					return "10"
				else:
					display("What do you want to do with this " + item + "?")
					return "invalid"
			# Test the following interactions
			elif item == 'gun' and rawCommand in ['use', 'fire', 'shoot']:
				return utils.engine_codes_dict['gun_use']
			elif item == 'paper clip' and rawCommand in ['bend', 'twist', 'change', 'turn']:
				return utils.engine_codes_dict['paper clip_bend']
			elif item == 'cryptex' and rawCommand in ['open', 'unlock']:
				return utils.engine_codes_dict['cryptex_open']
			else:
				# No recognized item and command
				display("I'm not sure how to " + rawCommand + " the " + item + " that way.")

		# No item or feature, unrecognized command
		else:
			if 'pots' in input and (command in ['hit', 'move']):
				return "2"
			else:
				# This is for the go requirement - if you specify "metal door" only act as go
				direction = utils.translateRoom(input, rooms, "strict")
				# Not a valid room alias
				if (direction == -1):
					display("I don't understand.")
				# Identical to "go"
				else:
					key = "go_" + str(direction)
					return utils.engine_codes_dict[key]


# Update to run main function for parseCommands.py separately from main.py
if __name__ == "__main__":
	print 'Starting the script.'
	keepLooping = True
	currentRoom = 1
	while (keepLooping != "exit"):
		userInput = raw_input (": ")
		featureList, featureDict, itemDict, roomList = utils.formatRoomData(rooms, objects, currentRoom)
		keepLooping = main(userInput, featureList, featureDict, itemDict, roomList)
		print "Code received: " + str(keepLooping)

